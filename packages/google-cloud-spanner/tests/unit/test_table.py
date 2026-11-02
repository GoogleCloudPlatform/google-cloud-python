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

        db = mock.create_autospec(Database, instance=True)
        table = self._make_one(self.TABLE_ID, db)
        self.assertEqual(table.table_id, self.TABLE_ID)

    def test_exists_executes_query(self):
        from google.cloud.spanner_v1.database import Database, SnapshotCheckout
        from google.cloud.spanner_v1.snapshot import Snapshot
        from google.cloud.spanner_v1.table import _EXISTS_TEMPLATE

        db = mock.create_autospec(Database, instance=True)
        checkout = mock.create_autospec(SnapshotCheckout, instance=True)
        snapshot = mock.create_autospec(Snapshot, instance=True)
        db.snapshot.return_value = checkout
        checkout.__enter__.return_value = snapshot
        snapshot.execute_sql.return_value = [[False]]
        table = self._make_one(self.TABLE_ID, db, schema_name=self.TABLE_SCHEMA)
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

    def test_schema_executes_query(self):
        from google.cloud.spanner_v1.database import Database, SnapshotCheckout
        from google.cloud.spanner_v1.snapshot import Snapshot
        from google.cloud.spanner_v1.table import _GET_SCHEMA_TEMPLATE

        db = mock.create_autospec(Database, instance=True)
        db.default_schema_name = ""
        checkout = mock.create_autospec(SnapshotCheckout, instance=True)
        snapshot = mock.create_autospec(Snapshot, instance=True)
        db.snapshot.return_value = checkout
        checkout.__enter__.return_value = snapshot
        table = self._make_one(self.TABLE_ID, db, schema_name=self.TABLE_SCHEMA)
        schema = table.schema
        self.assertIsInstance(schema, list)
        expected_query = _GET_SCHEMA_TEMPLATE.format("`{}`".format(self.TABLE_ID))
        snapshot.execute_sql.assert_called_with(expected_query)

    def test_schema_returns_cache(self):
        from google.cloud.spanner_v1.database import Database

        db = mock.create_autospec(Database, instance=True)
        table = self._make_one(self.TABLE_ID, db)
        table._schema = [StructType.Field(name="col1")]
        schema = table.schema
        self.assertEqual(schema, [StructType.Field(name="col1")])

    def test_reload_raises_notfound(self):
        from google.cloud.spanner_v1.database import Database, SnapshotCheckout
        from google.cloud.spanner_v1.snapshot import Snapshot

        db = mock.create_autospec(Database, instance=True)
        checkout = mock.create_autospec(SnapshotCheckout, instance=True)
        snapshot = mock.create_autospec(Snapshot, instance=True)
        db.snapshot.return_value = checkout
        checkout.__enter__.return_value = snapshot
        snapshot.execute_sql.return_value = [[False]]
        table = self._make_one(self.TABLE_ID, db)
        with self.assertRaises(NotFound):
            table.reload()

    def test_reload_executes_queries(self):
        from google.cloud.spanner_v1.database import Database, SnapshotCheckout
        from google.cloud.spanner_v1.snapshot import Snapshot
        from google.cloud.spanner_v1.streamed import StreamedResultSet

        db = mock.create_autospec(Database, instance=True)
        checkout = mock.create_autospec(SnapshotCheckout, instance=True)
        snapshot = mock.create_autospec(Snapshot, instance=True)
        results = mock.create_autospec(StreamedResultSet, instance=True)
        db.snapshot.return_value = checkout
        checkout.__enter__.return_value = snapshot
        results.fields = [StructType.Field(name="col1")]
        snapshot.execute_sql.side_effect = [
            [[True]],
            results,
        ]
        table = self._make_one(self.TABLE_ID, db)
        table.reload()
        self.assertEqual(table.schema, [StructType.Field(name="col1")])
