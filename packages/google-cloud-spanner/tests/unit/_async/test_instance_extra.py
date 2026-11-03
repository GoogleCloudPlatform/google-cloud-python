# Copyright 2024 Google LLC All rights reserved.
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
from unittest import mock

from google.cloud.spanner_v1._async.instance import Instance


class TestInstanceExtra(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.client = mock.MagicMock()
        self.client.project = "project-id"
        self.client.project_name = "projects/project-id"
        self.instance = Instance("instance-id", self.client)

    async def test_exists(self):
        # coverage for lines 335-352
        self.client.instance_admin_api.get_instance = mock.AsyncMock()
        self.assertTrue(await self.instance.exists())

        from google.cloud.exceptions import NotFound

        self.client.instance_admin_api.get_instance.side_effect = NotFound("not found")
        self.assertFalse(await self.instance.exists())

    async def test_create(self):
        # coverage for lines 292-332
        self.client.instance_admin_api.create_instance = mock.AsyncMock()
        await self.instance.create()
        self.assertTrue(self.client.instance_admin_api.create_instance.called)

    async def test_update(self):
        # coverage for lines 371-413
        self.client.instance_admin_api.update_instance = mock.AsyncMock()
        await self.instance.update()
        self.assertTrue(self.client.instance_admin_api.update_instance.called)

    async def test_delete(self):
        # coverage for lines 416-434
        self.client.instance_admin_api.delete_instance = mock.AsyncMock()
        await self.instance.delete()
        self.assertTrue(self.client.instance_admin_api.delete_instance.called)

    async def test_list_databases(self):
        # coverage for lines 527-549
        self.client.database_admin_api.list_databases = mock.AsyncMock()
        await self.instance.list_databases()
        self.assertTrue(self.client.database_admin_api.list_databases.called)

    async def test_list_backups(self):
        # coverage for lines 646-673
        self.client.database_admin_api.list_backups = mock.AsyncMock()
        await self.instance.list_backups()
        self.assertTrue(self.client.database_admin_api.list_backups.called)

    async def test_database(self):
        # coverage for lines 436-512
        db = await self.instance.database("db-id")
        self.assertEqual(db.database_id, "db-id")

        # test with interceptors
        from google.cloud.spanner_v1._async.testing.database_test import TestDatabase

        db2 = await self.instance.database("db-id-2", enable_interceptors_in_tests=True)
        self.assertIsInstance(db2, TestDatabase)

    async def test_database_pool_database_role(self):
        pool = mock.MagicMock()
        pool.database_role = "pool-role"
        pool.bind.return_value = None

        database = await self.instance.database("db-id", pool=pool)
        self.assertIs(database._pool, pool)
        self.assertEqual(pool.database_role, "pool-role")
        pool.bind.assert_called_once_with(database)

    async def test_database_pool_inherits_database_role(self):
        pool = mock.MagicMock()
        pool.database_role = None

        def _mock_bind(db):
            pool.database_role = pool.database_role or db.database_role

        pool.bind.side_effect = _mock_bind

        database = await self.instance.database(
            "db-id", pool=pool, database_role="db-role"
        )
        self.assertEqual(database.database_role, "db-role")
        self.assertEqual(pool.database_role, "db-role")
        pool.bind.assert_called_once_with(database)

    async def test_database_pool_database_role_precedence(self):
        pool = mock.MagicMock()
        pool.database_role = "pool-role"

        def _mock_bind(db):
            pool.database_role = pool.database_role or db.database_role

        pool.bind.side_effect = _mock_bind

        database = await self.instance.database(
            "db-id", pool=pool, database_role="db-role"
        )
        self.assertEqual(database.database_role, "db-role")
        self.assertEqual(pool.database_role, "pool-role")
        pool.bind.assert_called_once_with(database)

    def test_backup(self):
        # coverage for lines 551-608
        backup = self.instance.backup("backup-id")
        self.assertEqual(backup.backup_id, "backup-id")

        # test with database object
        db = mock.MagicMock()
        db.name = "db-name"
        backup2 = self.instance.backup("backup-id-2", database=db)
        self.assertEqual(backup2.database, "db-name")

    async def test_reload(self):
        # coverage for lines 355-369
        self.client.instance_admin_api.get_instance = mock.AsyncMock()
        resp = mock.MagicMock()
        resp.display_name = "new name"
        resp.config = "config"
        resp.node_count = 1
        resp.processing_units = 1000
        resp.labels = {}
        self.client.instance_admin_api.get_instance.return_value = resp
        await self.instance.reload()
        self.assertEqual(self.instance.display_name, "new name")

    def test_copy_backup(self):
        # coverage for lines 610-643
        backup = self.instance.copy_backup("copy-id", "source-backup")
        self.assertEqual(backup.backup_id, "copy-id")

    async def test_list_backup_operations(self):
        # coverage for lines 676-704
        self.client.database_admin_api.list_backup_operations = mock.AsyncMock()

        # Test mapping logic
        op_pb = mock.MagicMock()
        op_pb.metadata.type_url = "type.googleapis.com/google.spanner.admin.database.v1.CreateDatabaseMetadata"
        self.client.database_admin_api.list_backup_operations.return_value = [op_pb]

        from google.api_core.operation import Operation

        with mock.patch(
            "google.api_core.operation.from_gapic",
            return_value=mock.MagicMock(spec=Operation),
        ):
            res = await self.instance.list_backup_operations()
            list(res)
        self.assertTrue(self.client.database_admin_api.list_backup_operations.called)

    async def test_list_database_operations(self):
        # coverage for lines 707-735
        self.client.database_admin_api.list_database_operations = mock.AsyncMock()
        self.client.database_admin_api.list_database_operations.return_value = []
        res = await self.instance.list_database_operations()
        self.assertTrue(
            hasattr(res, "__iter__") or hasattr(res, "__next__") or isinstance(res, map)
        )

    def test_processing_units_setter(self):
        # coverage for lines 229-236
        self.instance.processing_units = 2000
        self.assertEqual(self.instance.node_count, 2)

    def test_node_count_setter(self):
        # coverage for lines 249-256
        self.instance.node_count = 3
        self.assertEqual(self.instance.processing_units, 3000)

    def test_copy(self):
        # coverage for lines 272-289
        self.client.copy.return_value = self.client
        inst_copy = self.instance.copy()
        self.assertEqual(inst_copy.instance_id, self.instance.instance_id)

    async def test_init_validation(self):
        # coverage for lines 133-137
        from google.api_core.exceptions import InvalidArgument

        with self.assertRaises(InvalidArgument):
            Instance("id", self.client, node_count=1, processing_units=2000)

        # branch at 144
        inst = Instance("id", self.client, processing_units=500)
        self.assertEqual(inst.node_count, 0)

    def test_from_pb(self):
        # coverage for lines 168-200
        from google.cloud.spanner_admin_instance_v1 import Instance as InstancePB

        pb = InstancePB(
            name="projects/project-id/instances/id",
            config="config",
            display_name="display name",
            node_count=1,
            processing_units=1000,
            labels={},
        )
        inst = Instance.from_pb(pb, self.client)
        self.assertEqual(inst.instance_id, "id")

        # error cases
        pb.name = "wrong/name"
        with self.assertRaises(ValueError):
            Instance.from_pb(pb, self.client)

        pb.name = "projects/other/instances/id"
        with self.assertRaises(ValueError):
            Instance.from_pb(pb, self.client)

        pb.name = "projects/project-id/instances/id"
        pb.display_name = ""
        with self.assertRaises(ValueError):
            Instance.from_pb(pb, self.client)

    def test___eq__(self):
        # coverage for lines 259-267
        other = Instance("instance-id", self.client)
        self.assertTrue(self.instance == other)
        self.assertFalse(self.instance == object())
        self.assertFalse(self.instance != other)

    async def test_reload_failure(self):
        # coverage for line 361
        from google.cloud.exceptions import NotFound

        self.client.instance_admin_api.get_instance = mock.AsyncMock(
            side_effect=NotFound("not found")
        )
        with self.assertRaises(NotFound):
            await self.instance.reload()
