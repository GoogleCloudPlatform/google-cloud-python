# Copyright 2016 Google LLC All rights reserved.
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

from google.cloud.spanner_v1 import DefaultTransactionOptions


class TestInstance(unittest.TestCase):
    PROJECT = "project"
    PARENT = "projects/" + PROJECT
    INSTANCE_ID = "instance-id"
    INSTANCE_NAME = PARENT + "/instances/" + INSTANCE_ID
    CONFIG_NAME = "configuration-name"
    LOCATION = "projects/" + PROJECT + "/locations/" + CONFIG_NAME
    DISPLAY_NAME = "display_name"
    NODE_COUNT = 5
    PROCESSING_UNITS = 5000
    OP_ID = 8915
    OP_NAME = "operations/projects/%s/instances/%soperations/%d" % (
        PROJECT,
        INSTANCE_ID,
        OP_ID,
    )
    TABLE_ID = "table_id"
    TABLE_NAME = INSTANCE_NAME + "/tables/" + TABLE_ID
    TIMEOUT_SECONDS = 1
    DATABASE_ID = "database_id"
    DATABASE_NAME = "%s/databases/%s" % (INSTANCE_NAME, DATABASE_ID)
    LABELS = {"test": "true"}
    FIELD_MASK = ["config", "display_name", "processing_units", "labels"]

    def _getTargetClass(self):
        from google.cloud.spanner_v1.instance import Instance

        return Instance

    def _make_one(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    @staticmethod
    def _make_database_admin_api():
        from google.cloud.spanner_admin_database_v1 import DatabaseAdminClient
        from google.cloud.spanner_admin_database_v1.services.database_admin.transports.base import (
            DatabaseAdminTransport,
        )

        mock_transport = mock.create_autospec(DatabaseAdminTransport, instance=True)
        mock_transport._wrapped_methods = {}
        return DatabaseAdminClient(transport=mock_transport)

    def test_constructor_defaults(self):
        from google.cloud.spanner_v1.instance import DEFAULT_NODE_COUNT

        client = object()
        instance = self._make_one(self.INSTANCE_ID, client)
        self.assertEqual(instance.instance_id, self.INSTANCE_ID)
        self.assertIs(instance._client, client)
        self.assertIs(instance.configuration_name, None)
        self.assertEqual(instance.node_count, DEFAULT_NODE_COUNT)
        self.assertEqual(instance.display_name, self.INSTANCE_ID)
        self.assertEqual(instance.labels, {})

    def test_constructor_non_default(self):
        DISPLAY_NAME = "display_name"
        client = object()

        instance = self._make_one(
            self.INSTANCE_ID,
            client,
            configuration_name=self.CONFIG_NAME,
            node_count=self.NODE_COUNT,
            display_name=DISPLAY_NAME,
            labels=self.LABELS,
        )
        self.assertEqual(instance.instance_id, self.INSTANCE_ID)
        self.assertIs(instance._client, client)
        self.assertEqual(instance.configuration_name, self.CONFIG_NAME)
        self.assertEqual(instance.node_count, self.NODE_COUNT)
        self.assertEqual(instance.display_name, DISPLAY_NAME)
        self.assertEqual(instance.labels, self.LABELS)

    def test_copy(self):
        DISPLAY_NAME = "display_name"

        client = _Client(self.PROJECT)
        instance = self._make_one(
            self.INSTANCE_ID, client, self.CONFIG_NAME, display_name=DISPLAY_NAME
        )
        new_instance = instance.copy()

        # Make sure the client copy succeeded.
        self.assertIsNot(new_instance._client, client)
        self.assertEqual(new_instance._client, client)
        # Make sure the client got copied to a new instance.
        self.assertIsNot(instance, new_instance)
        self.assertEqual(instance, new_instance)

    def test__update_from_pb_success(self):
        from google.cloud.spanner_admin_instance_v1 import Instance

        display_name = "display_name"
        instance_pb = Instance(display_name=display_name)

        instance = self._make_one(None, None, None, None)
        self.assertEqual(instance.display_name, None)
        instance._update_from_pb(instance_pb)
        self.assertEqual(instance.display_name, display_name)

    def test__update_from_pb_no_display_name(self):
        from google.cloud.spanner_admin_instance_v1 import Instance

        instance_pb = Instance()
        instance = self._make_one(None, None, None, None)
        self.assertEqual(instance.display_name, None)
        with self.assertRaises(ValueError):
            instance._update_from_pb(instance_pb)
        self.assertEqual(instance.display_name, None)

    def test_from_pb_bad_instance_name(self):
        from google.cloud.spanner_admin_instance_v1 import Instance

        instance_name = "INCORRECT_FORMAT"
        instance_pb = Instance(name=instance_name)

        klass = self._getTargetClass()
        with self.assertRaises(ValueError):
            klass.from_pb(instance_pb, None)

    def test_from_pb_project_mistmatch(self):
        from google.cloud.spanner_admin_instance_v1 import Instance

        ALT_PROJECT = "ALT_PROJECT"
        client = _Client(project=ALT_PROJECT)

        self.assertNotEqual(self.PROJECT, ALT_PROJECT)

        instance_pb = Instance(name=self.INSTANCE_NAME)

        klass = self._getTargetClass()
        with self.assertRaises(ValueError):
            klass.from_pb(instance_pb, client)

    def test_from_pb_success(self):
        from google.cloud.spanner_admin_instance_v1 import Instance

        client = _Client(project=self.PROJECT)

        instance_pb = Instance(
            name=self.INSTANCE_NAME,
            config=self.CONFIG_NAME,
            display_name=self.INSTANCE_ID,
            labels=self.LABELS,
        )

        klass = self._getTargetClass()
        instance = klass.from_pb(instance_pb, client)
        self.assertIsInstance(instance, klass)
        self.assertEqual(instance._client, client)
        self.assertEqual(instance.instance_id, self.INSTANCE_ID)
        self.assertEqual(instance.configuration_name, self.CONFIG_NAME)
        self.assertEqual(instance.labels, self.LABELS)

    def test_name_property(self):
        client = _Client(project=self.PROJECT)

        instance = self._make_one(self.INSTANCE_ID, client, self.CONFIG_NAME)
        self.assertEqual(instance.name, self.INSTANCE_NAME)

    def test_labels_property(self):
        client = _Client(project=self.PROJECT)

        instance = self._make_one(
            self.INSTANCE_ID, client, self.CONFIG_NAME, labels=self.LABELS
        )
        self.assertEqual(instance.labels, self.LABELS)

    def test___eq__(self):
        client = object()
        instance1 = self._make_one(self.INSTANCE_ID, client, self.CONFIG_NAME)
        instance2 = self._make_one(self.INSTANCE_ID, client, self.CONFIG_NAME)
        self.assertEqual(instance1, instance2)

    def test___eq__type_differ(self):
        client = object()
        instance1 = self._make_one(self.INSTANCE_ID, client, self.CONFIG_NAME)
        instance2 = object()
        self.assertNotEqual(instance1, instance2)

    def test___ne__same_value(self):
        client = object()
        instance1 = self._make_one(self.INSTANCE_ID, client, self.CONFIG_NAME)
        instance2 = self._make_one(self.INSTANCE_ID, client, self.CONFIG_NAME)
        comparison_val = instance1 != instance2
        self.assertFalse(comparison_val)

    def test___ne__(self):
        instance1 = self._make_one("instance_id1", "client1", self.CONFIG_NAME)
        instance2 = self._make_one("instance_id2", "client2", self.CONFIG_NAME)
        self.assertNotEqual(instance1, instance2)

    def test_create_grpc_error(self):
        from google.api_core.exceptions import Unknown

        client = _Client(self.PROJECT)
        client.instance_admin_api = _FauxInstanceAdminAPI(_rpc_error=True)
        instance = self._make_one(
            self.INSTANCE_ID, client, configuration_name=self.CONFIG_NAME
        )

        with self.assertRaises(Unknown):
            instance.create()

    def test_create_already_exists(self):
        from google.cloud.exceptions import Conflict

        client = _Client(self.PROJECT)
        api = client.instance_admin_api = _FauxInstanceAdminAPI(
            _create_instance_conflict=True
        )
        instance = self._make_one(
            self.INSTANCE_ID, client, configuration_name=self.CONFIG_NAME
        )

        with self.assertRaises(Conflict):
            instance.create()

        (parent, instance_id, instance, metadata) = api._created_instance
        self.assertEqual(parent, self.PARENT)
        self.assertEqual(instance_id, self.INSTANCE_ID)
        self.assertEqual(instance.name, self.INSTANCE_NAME)
        self.assertEqual(instance.config, self.CONFIG_NAME)
        self.assertEqual(instance.display_name, self.INSTANCE_ID)
        self.assertEqual(instance.processing_units, 1000)
        self.assertEqual(metadata, [("google-cloud-resource-prefix", instance.name)])

    def test_create_success(self):
        op_future = _FauxOperationFuture()
        client = _Client(self.PROJECT)
        api = client.instance_admin_api = _FauxInstanceAdminAPI(
            _create_instance_response=op_future
        )
        instance = self._make_one(
            self.INSTANCE_ID,
            client,
            configuration_name=self.CONFIG_NAME,
            display_name=self.DISPLAY_NAME,
            node_count=self.NODE_COUNT,
            labels=self.LABELS,
        )

        future = instance.create()

        self.assertIs(future, op_future)

        (parent, instance_id, instance, metadata) = api._created_instance
        self.assertEqual(parent, self.PARENT)
        self.assertEqual(instance_id, self.INSTANCE_ID)
        self.assertEqual(instance.name, self.INSTANCE_NAME)
        self.assertEqual(instance.config, self.CONFIG_NAME)
        self.assertEqual(instance.display_name, self.DISPLAY_NAME)
        self.assertEqual(instance.processing_units, self.PROCESSING_UNITS)
        self.assertEqual(instance.labels, self.LABELS)
        self.assertEqual(metadata, [("google-cloud-resource-prefix", instance.name)])

    def test_create_with_processing_units(self):
        op_future = _FauxOperationFuture()
        client = _Client(self.PROJECT)
        api = client.instance_admin_api = _FauxInstanceAdminAPI(
            _create_instance_response=op_future
        )
        instance = self._make_one(
            self.INSTANCE_ID,
            client,
            configuration_name=self.CONFIG_NAME,
            display_name=self.DISPLAY_NAME,
            processing_units=self.PROCESSING_UNITS,
            labels=self.LABELS,
        )

        future = instance.create()

        self.assertIs(future, op_future)

        (parent, instance_id, instance, metadata) = api._created_instance
        self.assertEqual(parent, self.PARENT)
        self.assertEqual(instance_id, self.INSTANCE_ID)
        self.assertEqual(instance.name, self.INSTANCE_NAME)
        self.assertEqual(instance.config, self.CONFIG_NAME)
        self.assertEqual(instance.display_name, self.DISPLAY_NAME)
        self.assertEqual(instance.processing_units, self.PROCESSING_UNITS)
        self.assertEqual(instance.labels, self.LABELS)
        self.assertEqual(metadata, [("google-cloud-resource-prefix", instance.name)])

    def test_exists_instance_grpc_error(self):
        from google.api_core.exceptions import Unknown

        client = _Client(self.PROJECT)
        client.instance_admin_api = _FauxInstanceAdminAPI(_rpc_error=True)
        instance = self._make_one(self.INSTANCE_ID, client, self.CONFIG_NAME)

        with self.assertRaises(Unknown):
            instance.exists()

    def test_exists_instance_not_found(self):
        client = _Client(self.PROJECT)
        api = client.instance_admin_api = _FauxInstanceAdminAPI(
            _instance_not_found=True
        )
        api._instance_not_found = True
        instance = self._make_one(self.INSTANCE_ID, client, self.CONFIG_NAME)

        self.assertFalse(instance.exists())

        name, metadata = api._got_instance
        self.assertEqual(name, self.INSTANCE_NAME)
        self.assertEqual(metadata, [("google-cloud-resource-prefix", instance.name)])

    def test_exists_success(self):
        from google.cloud.spanner_admin_instance_v1 import Instance

        client = _Client(self.PROJECT)
        instance_pb = Instance(
            name=self.INSTANCE_NAME,
            config=self.CONFIG_NAME,
            display_name=self.DISPLAY_NAME,
            node_count=self.NODE_COUNT,
        )
        api = client.instance_admin_api = _FauxInstanceAdminAPI(
            _get_instance_response=instance_pb
        )
        instance = self._make_one(self.INSTANCE_ID, client)

        self.assertTrue(instance.exists())

        name, metadata = api._got_instance
        self.assertEqual(name, self.INSTANCE_NAME)
        self.assertEqual(metadata, [("google-cloud-resource-prefix", instance.name)])

    def test_reload_instance_grpc_error(self):
        from google.api_core.exceptions import Unknown

        client = _Client(self.PROJECT)
        client.instance_admin_api = _FauxInstanceAdminAPI(_rpc_error=True)
        instance = self._make_one(self.INSTANCE_ID, client, self.CONFIG_NAME)

        with self.assertRaises(Unknown):
            instance.reload()

    def test_reload_instance_not_found(self):
        from google.cloud.exceptions import NotFound

        client = _Client(self.PROJECT)
        api = client.instance_admin_api = _FauxInstanceAdminAPI(
            _instance_not_found=True
        )
        api._instance_not_found = True
        instance = self._make_one(self.INSTANCE_ID, client, self.CONFIG_NAME)

        with self.assertRaises(NotFound):
            instance.reload()

        name, metadata = api._got_instance
        self.assertEqual(name, self.INSTANCE_NAME)
        self.assertEqual(metadata, [("google-cloud-resource-prefix", instance.name)])

    def test_reload_success(self):
        from google.cloud.spanner_admin_instance_v1 import Instance

        client = _Client(self.PROJECT)
        instance_pb = Instance(
            name=self.INSTANCE_NAME,
            config=self.CONFIG_NAME,
            display_name=self.DISPLAY_NAME,
            node_count=self.NODE_COUNT,
            labels=self.LABELS,
        )
        api = client.instance_admin_api = _FauxInstanceAdminAPI(
            _get_instance_response=instance_pb
        )
        instance = self._make_one(self.INSTANCE_ID, client)

        instance.reload()

        self.assertEqual(instance.configuration_name, self.CONFIG_NAME)
        self.assertEqual(instance.node_count, self.NODE_COUNT)
        self.assertEqual(instance.display_name, self.DISPLAY_NAME)
        self.assertEqual(instance.labels, self.LABELS)

        name, metadata = api._got_instance
        self.assertEqual(name, self.INSTANCE_NAME)
        self.assertEqual(metadata, [("google-cloud-resource-prefix", instance.name)])

    def test_update_grpc_error(self):
        from google.api_core.exceptions import Unknown

        client = _Client(self.PROJECT)
        client.instance_admin_api = _FauxInstanceAdminAPI(_rpc_error=True)
        instance = self._make_one(
            self.INSTANCE_ID, client, configuration_name=self.CONFIG_NAME
        )

        with self.assertRaises(Unknown):
            instance.update()

    def test_update_not_found(self):
        from google.cloud.exceptions import NotFound

        from google.cloud.spanner_v1.instance import DEFAULT_NODE_COUNT

        client = _Client(self.PROJECT)
        api = client.instance_admin_api = _FauxInstanceAdminAPI(
            _instance_not_found=True
        )
        instance = self._make_one(
            self.INSTANCE_ID, client, configuration_name=self.CONFIG_NAME
        )

        with self.assertRaises(NotFound):
            instance.update()

        instance, field_mask, metadata = api._updated_instance
        self.assertEqual(field_mask.paths, self.FIELD_MASK)
        self.assertEqual(instance.name, self.INSTANCE_NAME)
        self.assertEqual(instance.config, self.CONFIG_NAME)
        self.assertEqual(instance.display_name, self.INSTANCE_ID)
        self.assertEqual(instance.node_count, DEFAULT_NODE_COUNT)
        self.assertEqual(metadata, [("google-cloud-resource-prefix", instance.name)])

    def test_update_success(self):
        op_future = _FauxOperationFuture()
        client = _Client(self.PROJECT)
        api = client.instance_admin_api = _FauxInstanceAdminAPI(
            _update_instance_response=op_future
        )
        instance = self._make_one(
            self.INSTANCE_ID,
            client,
            configuration_name=self.CONFIG_NAME,
            node_count=self.NODE_COUNT,
            display_name=self.DISPLAY_NAME,
            labels=self.LABELS,
        )

        future = instance.update()

        self.assertIs(future, op_future)

        instance, field_mask, metadata = api._updated_instance
        self.assertEqual(field_mask.paths, self.FIELD_MASK)
        self.assertEqual(instance.name, self.INSTANCE_NAME)
        self.assertEqual(instance.config, self.CONFIG_NAME)
        self.assertEqual(instance.display_name, self.DISPLAY_NAME)
        self.assertEqual(instance.node_count, self.NODE_COUNT)
        self.assertEqual(instance.labels, self.LABELS)
        self.assertEqual(metadata, [("google-cloud-resource-prefix", instance.name)])

    def test_update_success_with_processing_units(self):
        op_future = _FauxOperationFuture()
        client = _Client(self.PROJECT)
        api = client.instance_admin_api = _FauxInstanceAdminAPI(
            _update_instance_response=op_future
        )
        instance = self._make_one(
            self.INSTANCE_ID,
            client,
            configuration_name=self.CONFIG_NAME,
            processing_units=self.PROCESSING_UNITS,
            display_name=self.DISPLAY_NAME,
            labels=self.LABELS,
        )

        future = instance.update()

        self.assertIs(future, op_future)

        instance, field_mask, metadata = api._updated_instance
        self.assertEqual(
            field_mask.paths, ["config", "display_name", "processing_units", "labels"]
        )
        self.assertEqual(instance.name, self.INSTANCE_NAME)
        self.assertEqual(instance.config, self.CONFIG_NAME)
        self.assertEqual(instance.display_name, self.DISPLAY_NAME)
        self.assertEqual(instance.processing_units, self.PROCESSING_UNITS)
        self.assertEqual(instance.labels, self.LABELS)
        self.assertEqual(metadata, [("google-cloud-resource-prefix", instance.name)])

    def test_delete_grpc_error(self):
        from google.api_core.exceptions import Unknown

        client = _Client(self.PROJECT)
        client.instance_admin_api = _FauxInstanceAdminAPI(_rpc_error=True)
        instance = self._make_one(self.INSTANCE_ID, client)

        with self.assertRaises(Unknown):
            instance.delete()

    def test_delete_not_found(self):
        from google.cloud.exceptions import NotFound

        client = _Client(self.PROJECT)
        api = client.instance_admin_api = _FauxInstanceAdminAPI(
            _instance_not_found=True
        )
        instance = self._make_one(self.INSTANCE_ID, client)

        with self.assertRaises(NotFound):
            instance.delete()

        name, metadata = api._deleted_instance
        self.assertEqual(name, self.INSTANCE_NAME)
        self.assertEqual(metadata, [("google-cloud-resource-prefix", instance.name)])

    def test_delete_success(self):
        from google.protobuf.empty_pb2 import Empty

        client = _Client(self.PROJECT)
        api = client.instance_admin_api = _FauxInstanceAdminAPI(
            _delete_instance_response=Empty()
        )
        instance = self._make_one(self.INSTANCE_ID, client, self.CONFIG_NAME)

        instance.delete()

        name, metadata = api._deleted_instance
        self.assertEqual(name, self.INSTANCE_NAME)
        self.assertEqual(metadata, [("google-cloud-resource-prefix", instance.name)])

    def test_database_factory_defaults(self):
        from google.cloud.spanner_v1.database import Database
        from google.cloud.spanner_v1.pool import BurstyPool

        client = _Client(self.PROJECT)
        instance = self._make_one(self.INSTANCE_ID, client, self.CONFIG_NAME)
        DATABASE_ID = "database-id"

        database = instance.database(DATABASE_ID)

        self.assertIsInstance(database, Database)
        self.assertEqual(database.database_id, DATABASE_ID)
        self.assertIs(database._instance, instance)
        self.assertEqual(list(database.ddl_statements), [])
        self.assertIsInstance(database._pool, BurstyPool)
        self.assertIsNone(database._logger)
        pool = database._pool
        self.assertIs(pool._database, database)
        self.assertIsNone(database.database_role)

    def test_database_factory_explicit(self):
        from logging import Logger

        from google.cloud.spanner_v1.database import Database
        from tests._fixtures import DDL_STATEMENTS

        client = _Client(self.PROJECT)
        instance = self._make_one(self.INSTANCE_ID, client, self.CONFIG_NAME)
        DATABASE_ID = "database-id"
        DATABASE_ROLE = "dummy-role"
        pool = _Pool()
        logger = mock.create_autospec(Logger, instance=True)
        encryption_config = {"kms_key_name": "kms_key_name"}
        proto_descriptors = b""

        database = instance.database(
            DATABASE_ID,
            ddl_statements=DDL_STATEMENTS,
            pool=pool,
            logger=logger,
            encryption_config=encryption_config,
            database_role=DATABASE_ROLE,
            proto_descriptors=proto_descriptors,
        )

        self.assertIsInstance(database, Database)
        self.assertEqual(database.database_id, DATABASE_ID)
        self.assertIs(database._instance, instance)
        self.assertEqual(list(database.ddl_statements), DDL_STATEMENTS)
        self.assertIs(database._pool, pool)
        self.assertIs(database._logger, logger)
        self.assertIs(pool._bound, database)
        self.assertIs(database._encryption_config, encryption_config)
        self.assertIs(database.database_role, DATABASE_ROLE)
        self.assertIs(database._proto_descriptors, proto_descriptors)

    def test_database_factory_pool_database_role(self):
        from google.cloud.spanner_v1.database import Database

        client = _Client(self.PROJECT)
        instance = self._make_one(self.INSTANCE_ID, client, self.CONFIG_NAME)
        database_id = "database-id"
        pool = _Pool(database_role="pool-role")

        database = instance.database(
            database_id,
            pool=pool,
        )

        self.assertIsInstance(database, Database)
        self.assertIs(database._pool, pool)
        self.assertIs(pool._bound, database)
        self.assertEqual(pool.database_role, "pool-role")

    def test_database_factory_pool_inherits_database_role(self):
        from google.cloud.spanner_v1.database import Database

        client = _Client(self.PROJECT)
        instance = self._make_one(self.INSTANCE_ID, client, self.CONFIG_NAME)
        database_id = "database-id"
        database_role = "db-role"
        pool = _Pool()

        database = instance.database(
            database_id,
            pool=pool,
            database_role=database_role,
        )

        self.assertIsInstance(database, Database)
        self.assertIs(database._pool, pool)
        self.assertIs(pool._bound, database)
        self.assertEqual(database.database_role, database_role)
        self.assertEqual(pool.database_role, database_role)

    def test_database_factory_pool_database_role_precedence(self):
        from google.cloud.spanner_v1.database import Database

        client = _Client(self.PROJECT)
        instance = self._make_one(self.INSTANCE_ID, client, self.CONFIG_NAME)
        database_id = "database-id"
        pool = _Pool(database_role="pool-role")

        database = instance.database(
            database_id,
            pool=pool,
            database_role="db-role",
        )

        self.assertIsInstance(database, Database)
        self.assertIs(database._pool, pool)
        self.assertIs(pool._bound, database)
        self.assertEqual(database.database_role, "db-role")
        self.assertEqual(pool.database_role, "pool-role")

    def test_list_databases(self):
        from google.cloud.spanner_admin_database_v1 import (
            Database as DatabasePB,
        )
        from google.cloud.spanner_admin_database_v1 import (
            ListDatabasesRequest,
            ListDatabasesResponse,
        )

        api = self._make_database_admin_api()
        client = _Client(self.PROJECT)
        client.database_admin_api = api
        instance = self._make_one(self.INSTANCE_ID, client)

        databases_pb = ListDatabasesResponse(
            databases=[
                DatabasePB(name="{}/databases/aa".format(self.INSTANCE_NAME)),
                DatabasePB(name="{}/databases/bb".format(self.INSTANCE_NAME)),
            ]
        )

        ld_api = api._transport._wrapped_methods[api._transport.list_databases] = (
            mock.Mock(return_value=databases_pb)
        )

        response = instance.list_databases()
        databases = list(response)

        self.assertIsInstance(databases[0], DatabasePB)
        self.assertTrue(databases[0].name.endswith("/aa"))
        self.assertTrue(databases[1].name.endswith("/bb"))

        expected_metadata = (
            ("google-cloud-resource-prefix", instance.name),
            ("x-goog-request-params", "parent={}".format(instance.name)),
        )
        ld_api.assert_called_once_with(
            ListDatabasesRequest(parent=self.INSTANCE_NAME),
            metadata=expected_metadata,
            retry=mock.ANY,
            timeout=mock.ANY,
        )

    def test_list_databases_w_options(self):
        from google.cloud.spanner_admin_database_v1 import (
            ListDatabasesRequest,
            ListDatabasesResponse,
        )

        api = self._make_database_admin_api()
        client = _Client(self.PROJECT)
        client.database_admin_api = api
        instance = self._make_one(self.INSTANCE_ID, client)

        databases_pb = ListDatabasesResponse(databases=[])

        ld_api = api._transport._wrapped_methods[api._transport.list_databases] = (
            mock.Mock(return_value=databases_pb)
        )

        page_size = 42
        response = instance.list_databases(page_size=page_size)
        databases = list(response)

        self.assertEqual(databases, [])

        expected_metadata = (
            ("google-cloud-resource-prefix", instance.name),
            ("x-goog-request-params", "parent={}".format(instance.name)),
        )
        ld_api.assert_called_once_with(
            ListDatabasesRequest(parent=self.INSTANCE_NAME, page_size=page_size),
            metadata=expected_metadata,
            retry=mock.ANY,
            timeout=mock.ANY,
        )

    def test_backup_factory_defaults(self):
        from google.cloud.spanner_v1.backup import Backup

        client = _Client(self.PROJECT)
        instance = self._make_one(self.INSTANCE_ID, client, self.CONFIG_NAME)
        BACKUP_ID = "backup-id"

        backup = instance.backup(BACKUP_ID)

        self.assertIsInstance(backup, Backup)
        self.assertEqual(backup.backup_id, BACKUP_ID)
        self.assertIs(backup._instance, instance)
        self.assertEqual(backup._database, "")
        self.assertIsNone(backup._expire_time)

    def test_backup_factory_explicit(self):
        import datetime
        from datetime import timezone

        from google.cloud._helpers import UTC

        from google.cloud.spanner_admin_database_v1 import CreateBackupEncryptionConfig
        from google.cloud.spanner_v1.backup import Backup

        client = _Client(self.PROJECT)
        instance = self._make_one(self.INSTANCE_ID, client, self.CONFIG_NAME)
        BACKUP_ID = "backup-id"
        DATABASE_NAME = "database-name"
        timestamp = datetime.datetime.now(timezone.utc).replace(tzinfo=UTC)
        encryption_config = CreateBackupEncryptionConfig(
            encryption_type=CreateBackupEncryptionConfig.EncryptionType.CUSTOMER_MANAGED_ENCRYPTION,
            kms_key_name="kms_key_name",
        )

        backup = instance.backup(
            BACKUP_ID,
            database=DATABASE_NAME,
            expire_time=timestamp,
            encryption_config=encryption_config,
        )

        self.assertIsInstance(backup, Backup)
        self.assertEqual(backup.backup_id, BACKUP_ID)
        self.assertIs(backup._instance, instance)
        self.assertEqual(backup._database, DATABASE_NAME)
        self.assertIs(backup._expire_time, timestamp)
        self.assertEqual(backup._encryption_config, encryption_config)

    def test_list_backups_defaults(self):
        from google.cloud.spanner_admin_database_v1 import (
            Backup as BackupPB,
        )
        from google.cloud.spanner_admin_database_v1 import (
            ListBackupsRequest,
            ListBackupsResponse,
        )

        api = self._make_database_admin_api()
        client = _Client(self.PROJECT)
        client.database_admin_api = api
        instance = self._make_one(self.INSTANCE_ID, client)

        backups_pb = ListBackupsResponse(
            backups=[
                BackupPB(name=instance.name + "/backups/op1"),
                BackupPB(name=instance.name + "/backups/op2"),
                BackupPB(name=instance.name + "/backups/op3"),
            ]
        )

        lbo_api = api._transport._wrapped_methods[api._transport.list_backups] = (
            mock.Mock(return_value=backups_pb)
        )

        backups = instance.list_backups()

        for backup in backups:
            self.assertIsInstance(backup, BackupPB)

        expected_metadata = (
            ("google-cloud-resource-prefix", instance.name),
            ("x-goog-request-params", "parent={}".format(instance.name)),
        )
        lbo_api.assert_called_once_with(
            ListBackupsRequest(parent=self.INSTANCE_NAME),
            metadata=expected_metadata,
            retry=mock.ANY,
            timeout=mock.ANY,
        )

    def test_list_backups_w_options(self):
        from google.cloud.spanner_admin_database_v1 import (
            Backup as BackupPB,
        )
        from google.cloud.spanner_admin_database_v1 import (
            ListBackupsRequest,
            ListBackupsResponse,
        )

        api = self._make_database_admin_api()
        client = _Client(self.PROJECT)
        client.database_admin_api = api
        instance = self._make_one(self.INSTANCE_ID, client)

        backups_pb = ListBackupsResponse(
            backups=[
                BackupPB(name=instance.name + "/backups/op1"),
                BackupPB(name=instance.name + "/backups/op2"),
                BackupPB(name=instance.name + "/backups/op3"),
            ]
        )

        ldo_api = api._transport._wrapped_methods[api._transport.list_backups] = (
            mock.Mock(return_value=backups_pb)
        )

        backups = instance.list_backups(filter_="filter", page_size=10)

        for backup in backups:
            self.assertIsInstance(backup, BackupPB)

        expected_metadata = (
            ("google-cloud-resource-prefix", instance.name),
            ("x-goog-request-params", "parent={}".format(instance.name)),
        )
        ldo_api.assert_called_once_with(
            ListBackupsRequest(
                parent=self.INSTANCE_NAME, filter="filter", page_size=10
            ),
            metadata=expected_metadata,
            retry=mock.ANY,
            timeout=mock.ANY,
        )

    def test_list_backup_operations_defaults(self):
        from google.api_core.operation import Operation
        from google.longrunning import operations_pb2
        from google.protobuf.any_pb2 import Any

        from google.cloud.spanner_admin_database_v1 import (
            CreateBackupMetadata,
            ListBackupOperationsRequest,
            ListBackupOperationsResponse,
        )

        api = self._make_database_admin_api()
        client = _Client(self.PROJECT)
        client.database_admin_api = api
        instance = self._make_one(self.INSTANCE_ID, client)

        create_backup_metadata = Any()
        create_backup_metadata.Pack(
            CreateBackupMetadata.pb(
                CreateBackupMetadata(name="backup", database="database")
            )
        )

        operations_pb = ListBackupOperationsResponse(
            operations=[
                operations_pb2.Operation(name="op1", metadata=create_backup_metadata)
            ]
        )

        ldo_api = api._transport._wrapped_methods[
            api._transport.list_backup_operations
        ] = mock.Mock(return_value=operations_pb)

        ops = instance.list_backup_operations()

        expected_metadata = (
            ("google-cloud-resource-prefix", instance.name),
            ("x-goog-request-params", "parent={}".format(instance.name)),
        )
        ldo_api.assert_called_once_with(
            ListBackupOperationsRequest(parent=self.INSTANCE_NAME),
            metadata=expected_metadata,
            retry=mock.ANY,
            timeout=mock.ANY,
        )
        self.assertTrue(all([type(op) is Operation for op in ops]))

    def test_list_backup_operations_w_options(self):
        from google.api_core.operation import Operation
        from google.longrunning import operations_pb2
        from google.protobuf.any_pb2 import Any

        from google.cloud.spanner_admin_database_v1 import (
            CreateBackupMetadata,
            ListBackupOperationsRequest,
            ListBackupOperationsResponse,
        )

        api = self._make_database_admin_api()
        client = _Client(self.PROJECT)
        client.database_admin_api = api
        instance = self._make_one(self.INSTANCE_ID, client)

        create_backup_metadata = Any()
        create_backup_metadata.Pack(
            CreateBackupMetadata.pb(
                CreateBackupMetadata(name="backup", database="database")
            )
        )

        operations_pb = ListBackupOperationsResponse(
            operations=[
                operations_pb2.Operation(name="op1", metadata=create_backup_metadata)
            ]
        )

        ldo_api = api._transport._wrapped_methods[
            api._transport.list_backup_operations
        ] = mock.Mock(return_value=operations_pb)

        ops = instance.list_backup_operations(filter_="filter", page_size=10)

        expected_metadata = (
            ("google-cloud-resource-prefix", instance.name),
            ("x-goog-request-params", "parent={}".format(instance.name)),
        )
        ldo_api.assert_called_once_with(
            ListBackupOperationsRequest(
                parent=self.INSTANCE_NAME, filter="filter", page_size=10
            ),
            metadata=expected_metadata,
            retry=mock.ANY,
            timeout=mock.ANY,
        )
        self.assertTrue(all([type(op) is Operation for op in ops]))

    def test_list_database_operations_defaults(self):
        from google.api_core.operation import Operation
        from google.longrunning import operations_pb2
        from google.protobuf.any_pb2 import Any

        from google.cloud.spanner_admin_database_v1 import (
            CreateDatabaseMetadata,
            ListDatabaseOperationsRequest,
            ListDatabaseOperationsResponse,
            OptimizeRestoredDatabaseMetadata,
        )

        api = self._make_database_admin_api()
        client = _Client(self.PROJECT)
        client.database_admin_api = api
        instance = self._make_one(self.INSTANCE_ID, client)

        create_database_metadata = Any()
        create_database_metadata.Pack(
            CreateDatabaseMetadata.pb(CreateDatabaseMetadata(database="database"))
        )

        optimize_database_metadata = Any()
        optimize_database_metadata.Pack(
            OptimizeRestoredDatabaseMetadata.pb(
                OptimizeRestoredDatabaseMetadata(name="database")
            )
        )

        databases_pb = ListDatabaseOperationsResponse(
            operations=[
                operations_pb2.Operation(name="op1", metadata=create_database_metadata),
                operations_pb2.Operation(
                    name="op2", metadata=optimize_database_metadata
                ),
            ]
        )

        ldo_api = api._transport._wrapped_methods[
            api._transport.list_database_operations
        ] = mock.Mock(return_value=databases_pb)

        ops = instance.list_database_operations()

        expected_metadata = (
            ("google-cloud-resource-prefix", instance.name),
            ("x-goog-request-params", "parent={}".format(instance.name)),
        )
        ldo_api.assert_called_once_with(
            ListDatabaseOperationsRequest(parent=self.INSTANCE_NAME),
            metadata=expected_metadata,
            retry=mock.ANY,
            timeout=mock.ANY,
        )
        self.assertTrue(all([type(op) is Operation for op in ops]))

    def test_list_database_operations_w_options(self):
        from google.api_core.operation import Operation
        from google.longrunning import operations_pb2
        from google.protobuf.any_pb2 import Any

        from google.cloud.spanner_admin_database_v1 import (
            ListDatabaseOperationsRequest,
            ListDatabaseOperationsResponse,
            RestoreDatabaseMetadata,
            RestoreSourceType,
            UpdateDatabaseDdlMetadata,
        )

        api = self._make_database_admin_api()
        client = _Client(self.PROJECT)
        client.database_admin_api = api
        instance = self._make_one(self.INSTANCE_ID, client)

        restore_database_metadata = Any()
        restore_database_metadata.Pack(
            RestoreDatabaseMetadata.pb(
                RestoreDatabaseMetadata(
                    name="database", source_type=RestoreSourceType.BACKUP
                )
            )
        )

        update_database_metadata = Any()
        update_database_metadata.Pack(
            UpdateDatabaseDdlMetadata.pb(
                UpdateDatabaseDdlMetadata(
                    database="database", statements=["statements"]
                )
            )
        )

        databases_pb = ListDatabaseOperationsResponse(
            operations=[
                operations_pb2.Operation(
                    name="op1", metadata=restore_database_metadata
                ),
                operations_pb2.Operation(name="op2", metadata=update_database_metadata),
            ]
        )

        ldo_api = api._transport._wrapped_methods[
            api._transport.list_database_operations
        ] = mock.Mock(return_value=databases_pb)

        ops = instance.list_database_operations(filter_="filter", page_size=10)

        expected_metadata = (
            ("google-cloud-resource-prefix", instance.name),
            ("x-goog-request-params", "parent={}".format(instance.name)),
        )
        ldo_api.assert_called_once_with(
            ListDatabaseOperationsRequest(
                parent=self.INSTANCE_NAME, filter="filter", page_size=10
            ),
            metadata=expected_metadata,
            retry=mock.ANY,
            timeout=mock.ANY,
        )
        self.assertTrue(all([type(op) is Operation for op in ops]))

    def test_type_string_to_type_pb_hit(self):
        from google.cloud.spanner_admin_database_v1 import (
            OptimizeRestoredDatabaseMetadata,
        )
        from google.cloud.spanner_v1 import instance

        type_string = "type.googleapis.com/google.spanner.admin.database.v1.OptimizeRestoredDatabaseMetadata"
        self.assertIn(type_string, instance._OPERATION_METADATA_TYPES)
        self.assertEqual(
            instance._type_string_to_type_pb(type_string),
            OptimizeRestoredDatabaseMetadata,
        )

    def test_type_string_to_type_pb_miss(self):
        from google.protobuf.empty_pb2 import Empty

        from google.cloud.spanner_v1 import instance

        self.assertEqual(instance._type_string_to_type_pb("invalid_string"), Empty)


class _Client(object):
    def __init__(self, project, timeout_seconds=None):
        self.project = project
        self.project_name = "projects/" + self.project
        self.timeout_seconds = timeout_seconds
        self.route_to_leader_enabled = True
        self.directed_read_options = None
        self.default_transaction_options = DefaultTransactionOptions()
        self._client_context = None
        self._experimental_host = None

    def copy(self):
        from copy import deepcopy

        return deepcopy(self)

    def __eq__(self, other):
        return (
            other.project == self.project
            and other.project_name == self.project_name
            and other.timeout_seconds == self.timeout_seconds
        )


class _FauxInstanceAdminAPI(object):
    _create_instance_conflict = False
    _instance_not_found = False
    _rpc_error = False

    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)

    def create_instance(self, parent, instance_id, instance, metadata=None):
        from google.api_core.exceptions import AlreadyExists, Unknown

        self._created_instance = (parent, instance_id, instance, metadata)
        if self._rpc_error:
            raise Unknown("error")
        if self._create_instance_conflict:
            raise AlreadyExists("conflict")
        return self._create_instance_response

    def get_instance(self, name, metadata=None):
        from google.api_core.exceptions import NotFound, Unknown

        self._got_instance = (name, metadata)
        if self._rpc_error:
            raise Unknown("error")
        if self._instance_not_found:
            raise NotFound("error")
        return self._get_instance_response

    def update_instance(self, instance, field_mask, metadata=None):
        from google.api_core.exceptions import NotFound, Unknown

        self._updated_instance = (instance, field_mask, metadata)
        if self._rpc_error:
            raise Unknown("error")
        if self._instance_not_found:
            raise NotFound("error")
        return self._update_instance_response

    def delete_instance(self, name, metadata=None):
        from google.api_core.exceptions import NotFound, Unknown

        self._deleted_instance = name, metadata
        if self._rpc_error:
            raise Unknown("error")
        if self._instance_not_found:
            raise NotFound("error")
        return self._delete_instance_response


class _FauxOperationFuture(object):
    pass


class _Pool(object):
    _bound = None

    def __init__(self, database_role=None):
        self.database_role = database_role

    def bind(self, database):
        self._bound = database
        self.database_role = self.database_role or database.database_role
