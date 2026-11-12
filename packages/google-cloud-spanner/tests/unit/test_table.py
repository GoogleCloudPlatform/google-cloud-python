# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

import mock
from google.cloud.exceptions import NotFound

from google.cloud.spanner_v1.types import StructType, Type, TypeCode


class _BaseTest(unittest.TestCase):
    TABLE_ID = "test_table"
    TABLE_SCHEMA = ""

    def _make_one(self, *args, **kwargs):
        return self._get_target_class()(*args, **kwargs)


class TestTable(_BaseTest):
    def _get_target_class(self):
        from google.cloud.spanner_v1.table import Table

        return Table

    def test_ctor(self):
        from google.cloud.spanner_v1.database import Database

        database = mock.create_autospec(Database, instance=True)
        table = self._make_one(self.TABLE_ID, database)
        self.assertEqual(table.table_id, self.TABLE_ID)

    def test_exists_executes_query(self):
        from google.cloud.spanner_admin_database_v1 import DatabaseDialect
        from google.cloud.spanner_v1.database import Database, SnapshotCheckout
        from google.cloud.spanner_v1.snapshot import Snapshot
        from google.cloud.spanner_v1.table import _EXISTS_TEMPLATE

        database = mock.create_autospec(Database, instance=True)
        database.default_schema_name = ""
        database.database_dialect = DatabaseDialect.GOOGLE_STANDARD_SQL
        snapshot_checkout = mock.create_autospec(SnapshotCheckout, instance=True)
        snapshot = mock.create_autospec(Snapshot, instance=True)
        database.snapshot.return_value = snapshot_checkout
        snapshot_checkout.__enter__.return_value = snapshot
        snapshot.execute_sql.return_value = [[False]]
        table = self._make_one(self.TABLE_ID, database, schema_name=self.TABLE_SCHEMA)
        exists = table.exists()
        self.assertFalse(exists)
        snapshot.execute_sql.assert_called_with(
            _EXISTS_TEMPLATE.format(
                "WHERE TABLE_SCHEMA = @schema_name AND TABLE_NAME = @table_id"
            ),
            params={"schema_name": self.TABLE_SCHEMA, "table_id": self.TABLE_ID},
            param_types={
                "schema_name": Type(code=TypeCode.STRING),
                "table_id": Type(code=TypeCode.STRING),
            },
        )

    def test_exists_executes_query_postgresql(self):
        from google.cloud.spanner_admin_database_v1 import DatabaseDialect
        from google.cloud.spanner_v1.database import Database, SnapshotCheckout
        from google.cloud.spanner_v1.snapshot import Snapshot
        from google.cloud.spanner_v1.table import _EXISTS_TEMPLATE

        database = mock.create_autospec(Database, instance=True)
        database.database_dialect = DatabaseDialect.POSTGRESQL
        database.default_schema_name = "public"
        snapshot_checkout = mock.create_autospec(SnapshotCheckout, instance=True)
        snapshot = mock.create_autospec(Snapshot, instance=True)
        database.snapshot.return_value = snapshot_checkout
        snapshot_checkout.__enter__.return_value = snapshot
        snapshot.execute_sql.return_value = [[True]]
        table = self._make_one(self.TABLE_ID, database, schema_name="public")
        self.assertTrue(table.exists())
        snapshot.execute_sql.assert_called_with(
            _EXISTS_TEMPLATE.format("WHERE TABLE_SCHEMA=$1 AND TABLE_NAME = $2"),
            params={"p1": "public", "p2": self.TABLE_ID},
            param_types={
                "p1": Type(code=TypeCode.STRING),
                "p2": Type(code=TypeCode.STRING),
            },
        )

    def test_schema_executes_query(self):
        from google.cloud.spanner_admin_database_v1 import DatabaseDialect
        from google.cloud.spanner_v1.database import Database, SnapshotCheckout
        from google.cloud.spanner_v1.snapshot import Snapshot
        from google.cloud.spanner_v1.table import _GET_SCHEMA_TEMPLATE

        database = mock.create_autospec(Database, instance=True)
        database.default_schema_name = ""
        database.database_dialect = DatabaseDialect.GOOGLE_STANDARD_SQL
        snapshot_checkout = mock.create_autospec(SnapshotCheckout, instance=True)
        snapshot = mock.create_autospec(Snapshot, instance=True)
        database.snapshot.return_value = snapshot_checkout
        snapshot_checkout.__enter__.return_value = snapshot
        table = self._make_one(self.TABLE_ID, database, schema_name=self.TABLE_SCHEMA)
        schema = table.schema
        self.assertIsInstance(schema, list)
        expected_query = _GET_SCHEMA_TEMPLATE.format(f"`{self.TABLE_ID}`")
        snapshot.execute_sql.assert_called_with(expected_query)

    def test_schema_executes_query_postgresql(self):
        from google.cloud.spanner_admin_database_v1 import DatabaseDialect
        from google.cloud.spanner_v1.database import Database, SnapshotCheckout
        from google.cloud.spanner_v1.snapshot import Snapshot
        from google.cloud.spanner_v1.table import _GET_SCHEMA_TEMPLATE

        database = mock.create_autospec(Database, instance=True)
        database.default_schema_name = "public"
        database.database_dialect = DatabaseDialect.POSTGRESQL
        snapshot_checkout = mock.create_autospec(SnapshotCheckout, instance=True)
        snapshot = mock.create_autospec(Snapshot, instance=True)
        database.snapshot.return_value = snapshot_checkout
        snapshot_checkout.__enter__.return_value = snapshot
        table = self._make_one(self.TABLE_ID, database, schema_name="public")
        schema = table.schema
        self.assertIsInstance(schema, list)
        expected_query = _GET_SCHEMA_TEMPLATE.format(f'"{self.TABLE_ID}"')
        snapshot.execute_sql.assert_called_with(expected_query)

    def test_schema_with_escaped_identifiers(self):
        from google.cloud.spanner_admin_database_v1 import DatabaseDialect
        from google.cloud.spanner_v1.database import Database, SnapshotCheckout
        from google.cloud.spanner_v1.snapshot import Snapshot
        from google.cloud.spanner_v1.table import _GET_SCHEMA_TEMPLATE

        database = mock.create_autospec(Database, instance=True)
        database.default_schema_name = ""
        database.database_dialect = DatabaseDialect.GOOGLE_STANDARD_SQL
        snapshot_checkout = mock.create_autospec(SnapshotCheckout, instance=True)
        snapshot = mock.create_autospec(Snapshot, instance=True)
        database.snapshot.return_value = snapshot_checkout
        snapshot_checkout.__enter__.return_value = snapshot
        table = self._make_one("tab`name\\", database)
        _ = table.schema
        expected_query = _GET_SCHEMA_TEMPLATE.format("`tab\\`name\\\\`")
        snapshot.execute_sql.assert_called_with(expected_query)

    def test_schema_with_control_characters_raises_value_error(self):
        from google.cloud.spanner_admin_database_v1 import DatabaseDialect
        from google.cloud.spanner_v1.database import Database

        database = mock.create_autospec(Database, instance=True)
        database.default_schema_name = ""
        database.database_dialect = DatabaseDialect.GOOGLE_STANDARD_SQL
        table = self._make_one("table\nname", database)
        with self.assertRaises(ValueError):
            _ = table.schema

    def test_schema_returns_cache(self):
        from google.cloud.spanner_v1.database import Database

        database = mock.create_autospec(Database, instance=True)
        table = self._make_one(self.TABLE_ID, database)
        table._schema = [StructType.Field(name="col1")]
        schema = table.schema
        self.assertEqual(schema, [StructType.Field(name="col1")])

    def test_reload_raises_notfound(self):
        from google.cloud.spanner_admin_database_v1 import DatabaseDialect
        from google.cloud.spanner_v1.database import Database, SnapshotCheckout
        from google.cloud.spanner_v1.snapshot import Snapshot

        database = mock.create_autospec(Database, instance=True)
        database.database_dialect = DatabaseDialect.GOOGLE_STANDARD_SQL
        snapshot_checkout = mock.create_autospec(SnapshotCheckout, instance=True)
        snapshot = mock.create_autospec(Snapshot, instance=True)
        database.snapshot.return_value = snapshot_checkout
        snapshot_checkout.__enter__.return_value = snapshot
        snapshot.execute_sql.return_value = [[False]]
        table = self._make_one(self.TABLE_ID, database)
        with self.assertRaises(NotFound):
            table.reload()

    def test_reload_executes_queries(self):
        from google.cloud.spanner_admin_database_v1 import DatabaseDialect
        from google.cloud.spanner_v1.database import Database, SnapshotCheckout
        from google.cloud.spanner_v1.snapshot import Snapshot
        from google.cloud.spanner_v1.streamed import StreamedResultSet

        database = mock.create_autospec(Database, instance=True)
        database.default_schema_name = ""
        database.database_dialect = DatabaseDialect.GOOGLE_STANDARD_SQL
        snapshot_checkout = mock.create_autospec(SnapshotCheckout, instance=True)
        snapshot = mock.create_autospec(Snapshot, instance=True)
        results = mock.create_autospec(StreamedResultSet, instance=True)
        database.snapshot.return_value = snapshot_checkout
        snapshot_checkout.__enter__.return_value = snapshot
        results.fields = [StructType.Field(name="col1")]
        snapshot.execute_sql.side_effect = [
            [[True]],
            results,
        ]
        table = self._make_one(self.TABLE_ID, database)
        table.reload()
        self.assertEqual(table.schema, [StructType.Field(name="col1")])

    def test_quote_identifier_googlesql(self):
        from google.cloud.spanner_admin_database_v1 import DatabaseDialect
        from google.cloud.spanner_v1.database import Database

        database = mock.create_autospec(Database, instance=True)
        database.database_dialect = DatabaseDialect.GOOGLE_STANDARD_SQL
        database.default_schema_name = ""
        table = self._make_one("normal_table", database)

        self.assertEqual(table._quote_identifier("normal"), "`normal`")
        self.assertEqual(table._quote_identifier("tab`name"), "`tab\\`name`")
        self.assertEqual(table._quote_identifier("tab\\name"), "`tab\\\\name`")
        self.assertEqual(table._quote_identifier("tab\\"), "`tab\\\\`")
        self.assertEqual(table._quote_identifier("tab\\\\"), "`tab\\\\\\\\`")
        self.assertEqual(
            table._quote_identifier("tab\\\\`name"), "`tab\\\\\\\\\\`name`"
        )
        self.assertEqual(
            table._quote_identifier("users` WHERE 1=1 UNION ALL SELECT ... --"),
            "`users\\` WHERE 1=1 UNION ALL SELECT ... --`",
        )

    def test_quote_identifier_postgresql(self):
        from google.cloud.spanner_admin_database_v1 import DatabaseDialect
        from google.cloud.spanner_v1.database import Database

        database = mock.create_autospec(Database, instance=True)
        database.database_dialect = DatabaseDialect.POSTGRESQL
        database.default_schema_name = "public"
        table = self._make_one("normal_table", database)

        self.assertEqual(table._quote_identifier("normal"), '"normal"')
        self.assertEqual(table._quote_identifier('tab"name'), '"tab""name"')
        self.assertEqual(
            table._quote_identifier('users" WHERE 1=1 UNION ALL SELECT ... --'),
            '"users"" WHERE 1=1 UNION ALL SELECT ... --"',
        )

    def test_quote_identifier_invalid_control_characters(self):
        from google.cloud.spanner_admin_database_v1 import DatabaseDialect
        from google.cloud.spanner_v1.database import Database

        database = mock.create_autospec(Database, instance=True)
        database.database_dialect = DatabaseDialect.GOOGLE_STANDARD_SQL
        table = self._make_one("normal_table", database)

        with self.assertRaises(ValueError):
            table._quote_identifier("table\nname")
        with self.assertRaises(ValueError):
            table._quote_identifier("table\rname")
        with self.assertRaises(ValueError):
            table._quote_identifier("table\0name")
        with self.assertRaises(ValueError):
            table._quote_identifier("table\tname")
        with self.assertRaises(ValueError):
            table._quote_identifier("table\x1fname")
        with self.assertRaises(ValueError):
            table._quote_identifier("table\x7fname")

    def test_quote_identifier_backslash_before_backtick(self):
        from google.cloud.spanner_admin_database_v1 import DatabaseDialect
        from google.cloud.spanner_v1.database import Database

        database = mock.create_autospec(Database, instance=True)
        database.database_dialect = DatabaseDialect.GOOGLE_STANDARD_SQL
        table = self._make_one("normal_table", database)
        self.assertEqual(table._quote_identifier("tab\\`name"), "`tab\\\\\\`name`")

    def test_quote_identifier_invalid_types_and_empty(self):
        from google.cloud.spanner_admin_database_v1 import DatabaseDialect
        from google.cloud.spanner_v1.database import Database

        database = mock.create_autospec(Database, instance=True)
        database.database_dialect = DatabaseDialect.GOOGLE_STANDARD_SQL
        table = self._make_one("normal_table", database)

        with self.assertRaises(TypeError):
            table._quote_identifier(None)
        with self.assertRaises(TypeError):
            table._quote_identifier(123)
        with self.assertRaises(TypeError):
            table._quote_identifier(b"byte_name")
        with self.assertRaises(ValueError):
            table._quote_identifier("")

    def test_qualified_table_name_with_custom_schema(self):
        from google.cloud.spanner_admin_database_v1 import DatabaseDialect
        from google.cloud.spanner_v1.database import Database

        database = mock.create_autospec(Database, instance=True)
        database.default_schema_name = ""
        database.database_dialect = DatabaseDialect.GOOGLE_STANDARD_SQL
        table = self._make_one("my_table", database, schema_name="my_schema")
        self.assertEqual(table.qualified_table_name, "`my_schema`.`my_table`")

    def test_qualified_table_name_with_custom_schema_postgresql(self):
        from google.cloud.spanner_admin_database_v1 import DatabaseDialect
        from google.cloud.spanner_v1.database import Database

        database = mock.create_autospec(Database, instance=True)
        database.default_schema_name = "public"
        database.database_dialect = DatabaseDialect.POSTGRESQL
        table = self._make_one("my_table", database, schema_name="my_schema")
        self.assertEqual(table.qualified_table_name, '"my_schema"."my_table"')

    def test_qualified_table_name_with_escaped_schema(self):
        from google.cloud.spanner_admin_database_v1 import DatabaseDialect
        from google.cloud.spanner_v1.database import Database

        database_gsql = mock.create_autospec(Database, instance=True)
        database_gsql.default_schema_name = ""
        database_gsql.database_dialect = DatabaseDialect.GOOGLE_STANDARD_SQL
        table_gsql = self._make_one("my_table", database_gsql, schema_name="my`sch\\")
        self.assertEqual(table_gsql.qualified_table_name, "`my\\`sch\\\\`.`my_table`")

        database_pg = mock.create_autospec(Database, instance=True)
        database_pg.default_schema_name = "public"
        database_pg.database_dialect = DatabaseDialect.POSTGRESQL
        table_pg = self._make_one("my_table", database_pg, schema_name='my"sch')
        self.assertEqual(table_pg.qualified_table_name, '"my""sch"."my_table"')

    def test_qualified_table_name_with_control_characters_in_schema(self):
        from google.cloud.spanner_admin_database_v1 import DatabaseDialect
        from google.cloud.spanner_v1.database import Database

        database = mock.create_autospec(Database, instance=True)
        database.default_schema_name = ""
        database.database_dialect = DatabaseDialect.GOOGLE_STANDARD_SQL
        table = self._make_one("my_table", database, schema_name="my\nschema")
        with self.assertRaises(ValueError):
            _ = table.qualified_table_name

    def test_qualified_table_name_with_empty_schema_postgresql(self):
        from google.cloud.spanner_admin_database_v1 import DatabaseDialect
        from google.cloud.spanner_v1.database import Database

        database = mock.create_autospec(Database, instance=True)
        database.default_schema_name = "public"
        database.database_dialect = DatabaseDialect.POSTGRESQL
        table = self._make_one("my_table", database, schema_name="")
        self.assertEqual(table.schema_name, "public")
        self.assertEqual(table.qualified_table_name, '"my_table"')

    def test_schema_with_escaped_identifiers_postgresql(self):
        from google.cloud.spanner_admin_database_v1 import DatabaseDialect
        from google.cloud.spanner_v1.database import Database, SnapshotCheckout
        from google.cloud.spanner_v1.snapshot import Snapshot
        from google.cloud.spanner_v1.table import _GET_SCHEMA_TEMPLATE

        database = mock.create_autospec(Database, instance=True)
        database.default_schema_name = "public"
        database.database_dialect = DatabaseDialect.POSTGRESQL
        snapshot_checkout = mock.create_autospec(SnapshotCheckout, instance=True)
        snapshot = mock.create_autospec(Snapshot, instance=True)
        database.snapshot.return_value = snapshot_checkout
        snapshot_checkout.__enter__.return_value = snapshot
        table = self._make_one('tab"name', database, schema_name="public")
        _ = table.schema
        expected_query = _GET_SCHEMA_TEMPLATE.format('"tab""name"')
        snapshot.execute_sql.assert_called_with(expected_query)
