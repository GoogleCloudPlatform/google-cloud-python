# Copyright 2021 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

from unittest import mock

from django.db.backends.base.introspection import FieldInfo, TableInfo
from google.cloud.spanner_dbapi._helpers import ColumnInfo
from google.cloud.spanner_dbapi.cursor import ColumnDetails
from google.cloud.spanner_v1 import TypeCode

from django_spanner.introspection import DatabaseIntrospection
from tests.unit.django_spanner.simple_test import SpannerSimpleTestClass


class TestUtils(SpannerSimpleTestClass):
    def test_get_field_type_boolean(self):
        """
        Tests get field type for boolean field.
        """
        db_introspection = DatabaseIntrospection(self.connection)
        self.assertEqual(
            db_introspection.get_field_type(TypeCode.BOOL, description=None),
            "BooleanField",
        )

    def test_get_field_type_text_field(self):
        """
        Tests get field type for text field.
        """
        db_introspection = DatabaseIntrospection(self.connection)
        self.assertEqual(
            db_introspection.get_field_type(
                TypeCode.STRING,
                description=ColumnInfo(
                    name="name",
                    type_code=TypeCode.STRING,
                    internal_size="MAX",
                ),
            ),
            "TextField",
        )

    def test_get_table_list(self):
        """
        Tests get table list method.
        """
        db_introspection = DatabaseIntrospection(self.connection)
        cursor = mock.MagicMock()

        def list_tables(*args, **kwargs):
            return [["Table_1", "t"], ["Table_2", "t"]]

        cursor.run_sql_in_snapshot = list_tables
        table_list = db_introspection.get_table_list(cursor=cursor)
        self.assertEqual(
            table_list,
            [
                TableInfo(name="Table_1", type="t"),
                TableInfo(name="Table_2", type="t"),
            ],
        )

    def test_get_table_description(self):
        """
        Tests get table description method.
        """
        db_introspection = DatabaseIntrospection(self.connection)
        cursor = mock.MagicMock()

        def description(*args, **kwargs):
            return [["name", TypeCode.STRING], ["age", TypeCode.INT64]]

        def get_table_column_schema(*args, **kwargs):
            column_details = {}
            column_details["name"] = ColumnDetails(
                null_ok=False, spanner_type="STRING(10)"
            )
            column_details["age"] = ColumnDetails(null_ok=True, spanner_type="INT64")
            return column_details

        cursor.get_table_column_schema = get_table_column_schema
        cursor.description = description()
        table_description = db_introspection.get_table_description(
            cursor=cursor, table_name="Table_1"
        )
        self.assertEqual(
            table_description,
            [
                FieldInfo(
                    name="name",
                    type_code=TypeCode.STRING,
                    display_size=None,
                    internal_size=10,
                    precision=None,
                    scale=None,
                    null_ok=False,
                    default=None,
                    collation=None,
                ),
                FieldInfo(
                    name="age",
                    type_code=TypeCode.INT64,
                    display_size=None,
                    internal_size=None,
                    precision=None,
                    scale=None,
                    null_ok=True,
                    default=None,
                    collation=None,
                ),
            ],
        )

    def test_get_primary_key_column(self):
        """
        Tests get primary column of table.
        """
        db_introspection = DatabaseIntrospection(self.connection)
        cursor = mock.MagicMock()

        def run_sql_in_snapshot(*args, **kwargs):
            return [["PK_column"]]

        cursor.run_sql_in_snapshot = run_sql_in_snapshot
        primary_key = db_introspection.get_primary_key_column(
            cursor=cursor, table_name="Table_1"
        )
        self.assertEqual(
            primary_key,
            ("PK_column",),
        )

    def test_get_primary_key_column_returns_none(self):
        """
        Tests get primary column of table when key is None.
        """
        db_introspection = DatabaseIntrospection(self.connection)
        cursor = mock.MagicMock()

        def run_sql_in_snapshot(*args, **kwargs):
            return None

        cursor.run_sql_in_snapshot = run_sql_in_snapshot
        primary_key = db_introspection.get_primary_key_column(
            cursor=cursor, table_name="Table_1"
        )
        self.assertIsNone(
            primary_key,
        )

    def test_get_constraints(self):
        """
        Tests get constraints applied on table columns.
        """
        db_introspection = DatabaseIntrospection(self.connection)
        cursor = mock.MagicMock()

        def run_sql_in_snapshot(*args, **kwargs):
            # returns dummy data for 'CONSTRAINT_NAME, COLUMN_NAME' query.
            if "CONSTRAINT_NAME, COLUMN_NAME" in args[0]:
                return [["pk_constraint", "id"], ["name_constraint", "name"]]
            # returns dummy data for 'CONSTRAINT_NAME, CONSTRAINT_TYPE' query.
            if "CONSTRAINT_NAME, CONSTRAINT_TYPE" in args[0]:
                return [
                    ["pk_constraint", "PRIMARY KEY"],
                    ["FOREIGN KEY", "dept_id"],
                ]
            # returns dummy data for 'INFORMATION_SCHEMA.INDEXES' table query.
            return [["pk_index", "id", "ASCENDING", "PRIMARY_KEY", True]]

        cursor.run_sql_in_snapshot = run_sql_in_snapshot
        constraints = db_introspection.get_constraints(
            cursor=cursor, table_name="Table_1"
        )

        self.assertEqual(
            constraints,
            {
                "pk_constraint": {
                    "check": False,
                    "columns": ["id"],
                    "foreign_key": None,
                    "index": False,
                    "orders": [],
                    "primary_key": True,
                    "type": None,
                    "unique": True,
                },
                "name_constraint": {
                    "check": False,
                    "columns": ["name"],
                    "foreign_key": None,
                    "index": False,
                    "orders": [],
                    "primary_key": False,
                    "type": None,
                    "unique": False,
                },
                "FOREIGN KEY": {
                    "check": False,
                    "columns": [],
                    "foreign_key": None,
                    "index": False,
                    "orders": [],
                    "primary_key": False,
                    "type": None,
                    "unique": False,
                },
                "pk_index": {
                    "check": False,
                    "columns": ["id"],
                    "foreign_key": None,
                    "index": True,
                    "orders": ["ASCENDING"],
                    "primary_key": True,
                    "type": "PRIMARY_KEY",
                    "unique": True,
                },
            },
        )
