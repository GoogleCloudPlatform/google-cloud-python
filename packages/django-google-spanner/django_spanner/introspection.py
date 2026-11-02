# Copyright 2020 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

from django.db.backends.base.introspection import (
    BaseDatabaseIntrospection,
    FieldInfo,
    TableInfo,
)
from django.db.models import Index
from google.cloud.spanner_v1 import TypeCode


class DatabaseIntrospection(BaseDatabaseIntrospection):
    """A Spanner-specific version of Django introspection utilities."""

    data_types_reverse = {
        TypeCode.BOOL: "BooleanField",
        TypeCode.BYTES: "BinaryField",
        TypeCode.DATE: "DateField",
        TypeCode.FLOAT64: "FloatField",
        TypeCode.INT64: "IntegerField",
        TypeCode.STRING: "CharField",
        TypeCode.TIMESTAMP: "DateTimeField",
        TypeCode.NUMERIC: "DecimalField",
        TypeCode.JSON: "JSONField",
    }
    LIST_TABLE_SQL = """
        SELECT
            t.table_name, t.table_type
        FROM
            information_schema.tables AS t
        WHERE
            t.table_catalog = '' and t.table_schema = @schema_name
    """

    def get_field_type(self, data_type, description):
        """A hook for a Spanner database to use the cursor description to
        match a Django field type to the database column.

        :type data_type: int
        :param data_type: One of Spanner's standard data types.

        :type description: :class:`~google.cloud.spanner_dbapi._helpers.ColumnInfo`
        :param description: A description of Spanner column data type.

        :rtype: str
        :returns: The corresponding type of Django field.
        """
        if data_type == TypeCode.STRING and description.internal_size == "MAX":
            return "TextField"
        return super().get_field_type(data_type, description)

    def get_table_list(self, cursor):
        """Return a list of table and view names in the current database.

        :type cursor: :class:`~google.cloud.spanner_dbapi.cursor.Cursor`
        :param cursor: A reference to a Spanner Database cursor.

        :rtype: list
        :returns: A list of table and view names in the current database.
        """
        schema_name = self._get_schema_name(cursor)
        results = cursor.run_sql_in_snapshot(
            self.LIST_TABLE_SQL, params={"schema_name": schema_name}
        )
        tables = []
        # The second TableInfo field is 't' for table or 'v' for view.
        for row in results:
            table_type = "t"
            if row[1] == "VIEW":
                table_type = "v"
            tables.append(TableInfo(row[0], table_type))
        return tables

    def get_table_description(self, cursor, table_name):
        """Return a description of the table with the DB-API cursor.description
        interface.

        :type cursor: :class:`~google.cloud.spanner_dbapi.cursor.Cursor`
        :param cursor: A reference to a Spanner Database cursor.

        :type table_name: str
        :param table_name: The name of the table.

        :rtype: list
        :returns: A description of the table with the DB-API
                  cursor.description interface.
        """
        cursor.execute(
            "SELECT * FROM %s LIMIT 1" % self.connection.ops.quote_name(table_name)
        )
        column_details = cursor.get_table_column_schema(table_name)
        descriptions = []
        for line in cursor.description:
            column_name, type_code = line[0], line[1]
            details = column_details[column_name]
            if details.spanner_type.startswith("STRING"):
                # Extract the size of the string from, e.g. STRING(#).
                internal_size = details.spanner_type[7:-1]
                if internal_size != "MAX":
                    internal_size = int(internal_size)
            else:
                internal_size = None
            descriptions.append(
                FieldInfo(
                    column_name,
                    type_code,
                    None,  # display_size
                    internal_size,
                    None,  # precision
                    None,  # scale
                    details.null_ok,
                    None,  # default
                    None,  # collation
                )
            )

        return descriptions

    def get_relations(self, cursor, table_name):
        """Return a dictionary of {field_name: (field_name_other_table, other_table)}
        representing all the relationships in the table.

        :type cursor: :class:`~google.cloud.spanner_dbapi.cursor.Cursor`
        :param cursor: A reference to a Spanner Database cursor.

        :type table_name: str
        :param table_name: The name of the Cloud Spanner Database.

        :rtype: dict
        :returns: A dictionary representing column relationships to other tables.
        """
        schema_name = self._get_schema_name(cursor)
        results = cursor.run_sql_in_snapshot(
            """
            SELECT
                tc.COLUMN_NAME as col, ccu.COLUMN_NAME as ref_col, ccu.TABLE_NAME as ref_table
            FROM
                INFORMATION_SCHEMA.KEY_COLUMN_USAGE AS tc
            JOIN
                INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS as rc
            ON
                tc.CONSTRAINT_NAME = rc.CONSTRAINT_NAME
            JOIN
                INFORMATION_SCHEMA.CONSTRAINT_COLUMN_USAGE as ccu
            ON
                rc.UNIQUE_CONSTRAINT_NAME = ccu.CONSTRAINT_NAME
            WHERE
                tc.TABLE_SCHEMA=@schema_name AND tc.TABLE_NAME=@view_name
            """,
            params={"schema_name": schema_name, "view_name": table_name},
        )
        return {
            column: (referred_column, referred_table)
            for (column, referred_column, referred_table) in results
        }

    def get_primary_key_column(self, cursor, table_name):
        """Return Primary Key column.

        :type cursor: :class:`~google.cloud.spanner_dbapi.cursor.Cursor`
        :param cursor: A reference to a Spanner Database cursor.

        :type table_name: str
        :param table_name: The name of the table.

        :rtype: str
        :returns: The name of the PK column.
        """
        schema_name = self._get_schema_name(cursor)
        results = cursor.run_sql_in_snapshot(
            """
            SELECT
                ccu.COLUMN_NAME
            FROM
                INFORMATION_SCHEMA.TABLE_CONSTRAINTS as tc
            RIGHT JOIN
                INFORMATION_SCHEMA.KEY_COLUMN_USAGE
            AS
                ccu ON tc.CONSTRAINT_NAME = ccu.CONSTRAINT_NAME
            WHERE
                tc.TABLE_NAME=@table_name AND tc.CONSTRAINT_TYPE='PRIMARY KEY' AND tc.TABLE_SCHEMA=@schema_name
            """,
            params={"schema_name": schema_name, "table_name": table_name},
        )
        return tuple(row[0] for row in results) if results else None

    def get_constraints(self, cursor, table_name):
        """Retrieve the Spanner Table column constraints.

        :type cursor: :class:`~google.cloud.spanner_dbapi.cursor.Cursor`
        :param cursor: The cursor in the linked database.

        :type table_name: str
        :param table_name: The name of the table.

        :rtype: dict
        :returns: A dictionary with constraints.
        """
        constraints = {}
        schema_name = self._get_schema_name(cursor)

        # Firstly populate all available constraints and their columns.
        constraint_columns = cursor.run_sql_in_snapshot(
            """
            SELECT
                CONSTRAINT_NAME, COLUMN_NAME
            FROM
                INFORMATION_SCHEMA.CONSTRAINT_COLUMN_USAGE
               WHERE TABLE_NAME=@table AND TABLE_SCHEMA=@schema_name""",
            params={"table": table_name, "schema_name": schema_name},
        )
        for constraint, column_name in constraint_columns:
            if constraint not in constraints:
                constraints[constraint] = {
                    "check": False,
                    "columns": [],
                    "foreign_key": None,
                    "index": False,
                    "orders": [],
                    "primary_key": False,
                    "type": None,
                    "unique": False,
                }

            constraints[constraint]["columns"].append(column_name)

        # Add the various constraints by type.
        constraint_types = cursor.run_sql_in_snapshot(
            """
            SELECT
                CONSTRAINT_NAME, CONSTRAINT_TYPE
            FROM
                INFORMATION_SCHEMA.TABLE_CONSTRAINTS
            WHERE
                TABLE_NAME=@table AND TABLE_SCHEMA=@schema_name""",
            params={"table": table_name, "schema_name": schema_name},
        )
        for constraint, constraint_type in constraint_types:
            already_added = constraint in constraints
            if constraint_type == "FOREIGN KEY":
                # We don't yet support anything related to FOREIGN KEY.
                # See https://github.com/googleapis/python-spanner-django/issues/313.
                if already_added:
                    del constraints[constraint]
                continue

            if not already_added:
                constraints[constraint] = {
                    "check": False,
                    "columns": [],
                    "foreign_key": None,
                    "index": False,
                    "orders": [],
                    "primary_key": False,
                    "type": None,
                    "unique": False,
                }

            is_primary_key = constraint_type == "PRIMARY KEY"
            constraints[constraint]["check"] = constraint_type == "CHECK"
            constraints[constraint]["index"] = constraint_type == "INDEX"
            constraints[constraint]["unique"] = (
                constraint_type == "UNIQUE" or is_primary_key
            )
            constraints[constraint]["primary_key"] = is_primary_key

        # Add the indices.
        indexes = cursor.run_sql_in_snapshot(
            """
            SELECT
                idx.INDEX_NAME, idx_col.COLUMN_NAME, idx_col.COLUMN_ORDERING, idx.INDEX_TYPE, idx.IS_UNIQUE
            FROM
                INFORMATION_SCHEMA.INDEXES AS idx
            RIGHT JOIN
                INFORMATION_SCHEMA.INDEX_COLUMNS AS idx_col
            ON
                idx_col.INDEX_NAME = idx.INDEX_NAME AND idx_col.TABLE_NAME=@table AND idx_col.TABLE_SCHEMA=idx.TABLE_SCHEMA
            WHERE
                idx.TABLE_NAME=@table AND idx.TABLE_SCHEMA=@schema_name
            ORDER BY
                idx_col.ORDINAL_POSITION
            """,
            params={"table": table_name, "schema_name": schema_name},
        )
        for (
            index_name,
            column_name,
            ordering,
            index_type,
            is_unique,
        ) in indexes:
            if index_name not in constraints:
                constraints[index_name] = {
                    "check": False,
                    "columns": [],
                    "foreign_key": None,
                    "index": False,
                    "orders": [],
                    "primary_key": False,
                    "type": None,
                    "unique": False,
                }

            constraints[index_name]["columns"].append(column_name)
            constraints[index_name]["index"] = True
            constraints[index_name]["orders"].append(ordering)
            # Index_type for PRIMARY KEY is 'PRIMARY_KEY' and NOT 'PRIMARY KEY'
            is_primary_key = index_type == "PRIMARY_KEY"
            constraints[index_name]["primary_key"] = is_primary_key
            constraints[index_name]["type"] = (
                index_type if is_primary_key else Index.suffix
            )
            constraints[index_name]["unique"] = is_unique

        return constraints

    def get_key_columns(self, cursor, table_name):
        """
        Return a list of (column_name, referenced_table, referenced_column)
        for all key columns in the given table.
        """
        key_columns = []
        schema_name = self._get_schema_name(cursor)
        cursor.execute(
            """SELECT
                tc.COLUMN_NAME as column_name,
                ccu.TABLE_NAME as referenced_table,
                ccu.COLUMN_NAME as referenced_column
            FROM
                INFORMATION_SCHEMA.KEY_COLUMN_USAGE AS tc
            JOIN
                INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS as rc
            ON
                tc.CONSTRAINT_NAME = rc.CONSTRAINT_NAME
            JOIN
                INFORMATION_SCHEMA.CONSTRAINT_COLUMN_USAGE as ccu
            ON
                rc.CONSTRAINT_NAME = ccu.CONSTRAINT_NAME
            WHERE
                tc.TABLE_NAME=@table AND tc.TABLE_SCHEMA=@schema_name
            """,
            params={"table": table_name, "schema_name": schema_name},
        )
        key_columns.extend(cursor.fetchall())
        return key_columns

    def _get_schema_name(self, cursor):
        return cursor.connection.current_schema
