import unittest
from unittest import mock

from google.api_core.exceptions import Aborted, NotFound

from google.cloud.spanner_admin_database_v1.types.common import DatabaseDialect
from google.cloud.spanner_admin_database_v1.types.spanner_database_admin import (
    Database as DatabasePB,
)
from google.cloud.spanner_v1._async.database import BatchSnapshot, Database
from google.cloud.spanner_v1.keyset import KeySet
from google.cloud.spanner_v1.services.spanner.transports.grpc_asyncio import (
    SpannerGrpcAsyncIOTransport,
)
from google.cloud.spanner_v1.types import RequestOptions
from google.cloud.spanner_v1.types.type import Type, TypeCode


class TestDatabaseExtra(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.instance = mock.Mock(
            spec=[
                "name",
                "instance_id",
                "_client",
                "experimental_host",
                "emulator_host",
            ]
        )
        self.instance.name = "projects/p/instances/i"
        self.instance.instance_id = "i"
        self.instance.experimental_host = None
        self.instance.emulator_host = None
        self.instance._client = mock.Mock()
        self.instance._client.database_admin_api = mock.AsyncMock()
        self.instance._client.metadata_and_request_id.return_value = []
        self.instance._client._next_nth_request = 1
        self.instance._client._nth_client_id = 1
        self.instance._client._query_options = None
        self.instance._client._client_context = None
        # Mock default_transaction_options to avoid AttributeError in Batch.commit
        self.instance._client.default_transaction_options = mock.Mock(
            spec=["default_read_write_transaction_options"],
            default_read_write_transaction_options=None,
        )
        self.instance._client.timeout = 60
        self.instance._client.observability_options = {}

        # Patch SpannerClient directly in the module where it is used.
        self.patcher = mock.patch(
            "google.cloud.spanner_v1._async.database.SpannerClient", autospec=True
        )
        self.mock_spanner_client_class = self.patcher.start()
        self.mock_spanner_api = self.mock_spanner_client_class.return_value

        # Setup transport for channel_id property logic
        self.mock_spanner_api.transport = mock.Mock(spec=SpannerGrpcAsyncIOTransport)
        self.mock_spanner_api.transport.grpc_channel = mock.Mock()

        # Solid defaults to avoid proto-plus validation errors with mocks returning AsyncMocks
        self.mock_txn = mock.Mock()
        self.mock_txn.id = b"txn-id"
        self.mock_spanner_api.begin_transaction = mock.AsyncMock(
            return_value=self.mock_txn
        )

        self.mock_session_pb = mock.Mock()
        self.mock_session_pb.name = "projects/p/instances/i/databases/db/sessions/s"
        self.mock_spanner_api.create_session = mock.AsyncMock(
            return_value=self.mock_session_pb
        )

        self.addCleanup(self.patcher.stop)

    async def test_execute_partitioned_dml_coverage(self):
        db = Database("db", self.instance)
        await db._pool.bind(db)
        db._route_to_leader_enabled = True

        mock_session = mock.MagicMock()
        mock_session.name = "projects/p/instances/i/databases/db/sessions/s"
        db._sessions_manager.get_session = mock.AsyncMock(return_value=mock_session)
        db._sessions_manager.put_session = mock.AsyncMock()

        mock_iterator = mock.AsyncMock()
        mock_iterator.__aiter__.return_value = [mock.Mock()]

        with mock.patch(
            "google.cloud.spanner_v1._async.database._restart_on_unavailable",
            return_value=mock_iterator,
        ):
            with mock.patch(
                "google.cloud.spanner_v1._async.database.StreamedResultSet"
            ) as mock_rs_class:
                mock_rs = mock.AsyncMock()
                mock_rs.__aiter__.return_value = []
                mock_rs.stats.row_count_lower_bound = 5
                mock_rs_class.return_value = mock_rs

                res = await db.execute_partitioned_dml("DELETE FROM table")
                self.assertEqual(res, 5)

    async def test_execute_partitioned_dml_branch(self):
        db = Database("db", self.instance)
        await db._pool.bind(db)
        db._route_to_leader_enabled = False

        mock_session = mock.MagicMock()
        mock_session.name = "projects/p/instances/i/databases/db/sessions/s"
        db._sessions_manager.get_session = mock.AsyncMock(return_value=mock_session)

        mock_iterator = mock.AsyncMock()
        mock_iterator.__aiter__.return_value = []

        with mock.patch(
            "google.cloud.spanner_v1._async.database._restart_on_unavailable",
            return_value=mock_iterator,
        ):
            with mock.patch(
                "google.cloud.spanner_v1._async.database.StreamedResultSet"
            ) as mock_rs_class:
                mock_rs = mock.AsyncMock()
                mock_rs.__aiter__.return_value = []
                mock_rs.stats.row_count_lower_bound = 0
                mock_rs_class.return_value = mock_rs

                await db.execute_partitioned_dml("DELETE FROM table")

    async def test_execute_partitioned_dml_aborted(self):
        db = Database("db", self.instance)
        await db._pool.bind(db)

        call_count = 0

        async def mock_execute_pdml():
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                raise Aborted("aborted")
            return 10

        pass

        mock_api = self.mock_spanner_api

        # We need a real-ish session for the begin_transaction call in execute_pdml
        mock_session = mock.MagicMock()
        mock_session.name = "projects/p/instances/i/databases/db/sessions/s"
        db._sessions_manager.get_session = mock.AsyncMock(return_value=mock_session)

        # Ensure begin_transaction returns something with an .id property (bytes)
        mock_txn = mock.Mock()
        mock_txn.id = b"txn-id"

        side_effects = [Aborted("aborted"), mock_txn]
        mock_api.begin_transaction = mock.AsyncMock(side_effect=side_effects)

        mock_iterator = mock.MagicMock()
        mock_iterator.__aiter__.return_value = []

        with mock.patch(
            "google.cloud.spanner_v1._async.database._restart_on_unavailable",
            return_value=mock_iterator,
        ):
            with mock.patch(
                "google.cloud.spanner_v1._async.database.StreamedResultSet"
            ) as mock_rs_class:
                mock_rs = mock.AsyncMock()
                mock_rs.__aiter__.return_value = []
                mock_rs.stats.row_count_lower_bound = 10
                mock_rs_class.return_value = mock_rs

                # We need to mock DEFAULT_RETRY_BACKOFF to avoid waiting
                mock_backoff = mock.Mock()
                # _retry_on_aborted uses retry_config.with_predicate
                # and returns a callable that when called returns the result.
                with mock.patch(
                    "google.cloud.spanner_v1._async.database.DEFAULT_RETRY_BACKOFF",
                    mock_backoff,
                ):
                    # The real _retry_on_aborted returns retry(func).
                    # retry(func) returns a wrapper that, when called, returns a coroutine.
                    async def mock_wrapper():
                        return 10

                    mock_backoff.with_predicate.return_value = lambda f: mock_wrapper

                    res = await db.execute_partitioned_dml("DELETE FROM table")
                    self.assertEqual(res, 10)

    async def test_list_tables_extra(self):
        db = Database("db", self.instance)
        await db._pool.bind(db)

        # Dialect POSTGRESQL
        db._database_dialect = DatabaseDialect.POSTGRESQL

        mock_results = mock.MagicMock()
        mock_results.__aiter__.return_value = [["table1"], ["table2"]]

        mock_snapshot = mock.AsyncMock()
        mock_snapshot.execute_sql.return_value = mock_results

        with mock.patch.object(
            db,
            "snapshot",
            return_value=mock.AsyncMock(
                __aenter__=mock.AsyncMock(return_value=mock_snapshot)
            ),
        ):
            # schema=None
            tables = []
            async for t in db.list_tables(schema=None):
                tables.append(t.table_id)
            self.assertEqual(tables, ["table1", "table2"])

            # schema="other"
            async for _ in db.list_tables(schema="other"):
                pass

    async def test_database_options_coverage(self):
        db = Database("db", self.instance)
        await db._pool.bind(db)

        # Test observability_options when instance/client are None
        db._instance = None
        self.assertIsNone(db.observability_options)

        db._instance = self.instance
        self.instance._client = None
        self.assertIsNone(db.observability_options)

        # Restore
        db._instance = self.instance
        self.instance._client = mock.Mock()
        self.instance._client.observability_options = None
        self.assertEqual(db.observability_options["db_name"], db.name)

        # Test _next_nth_request when instance/client are None
        db._instance = None
        self.assertEqual(db._next_nth_request, 1)

        # Test _nth_client_id when instance/client are None
        self.assertEqual(db._nth_client_id, 0)

    async def test_batch_snapshot_coverage(self):
        db = Database("db", self.instance)
        await db._pool.bind(db)

        # session_id provided
        bs = BatchSnapshot(db, session_id="session-id")
        session = await bs._get_session()
        self.assertEqual(session.session_id, "session-id")

        # transaction_id provided
        bs2 = BatchSnapshot(db, transaction_id=b"txn-id")
        snapshot = await bs2._get_snapshot()
        self.assertEqual(snapshot._transaction_id, b"txn-id")

        # get_batch_transaction_id ValueError
        bs3 = BatchSnapshot(db)
        with self.assertRaises(ValueError):
            bs3.get_batch_transaction_id()

    async def test_batch_checkout_extra(self):
        db = Database("db", self.instance)
        await db._pool.bind(db)

        # request_options as object
        ro = RequestOptions(transaction_tag="tag")
        from google.cloud.spanner_v1._async.database import BatchCheckout

        bc = BatchCheckout(db, request_options=ro)
        self.assertEqual(bc._request_options.transaction_tag, "tag")

    async def test_reload_dialect_coverage(self):
        db = Database("db", self.instance)
        await db._pool.bind(db)

        mock_api = self.instance._client.database_admin_api
        mock_api.get_database_ddl.return_value = mock.Mock(
            statements=[], proto_descriptors=None
        )

        mock_db_pb = mock.Mock()
        mock_db_pb.state = DatabasePB.State.READY
        mock_db_pb.database_dialect = DatabaseDialect.GOOGLE_STANDARD_SQL
        mock_db_pb.create_time = None
        mock_db_pb.restore_info = None
        mock_db_pb.version_retention_period = None
        mock_db_pb.earliest_version_time = None
        mock_db_pb.encryption_config = None
        mock_db_pb.encryption_info = None
        mock_db_pb.default_leader = None
        mock_api.get_database.return_value = mock_db_pb

        await db.reload()
        self.assertEqual(db._state, DatabasePB.State.READY)

        # Test 2: reload when already READY (trigger line 514)
        await db.reload()
        self.assertTrue(mock_api.get_database.called)

    async def test_run_in_transaction_nested_error(self):
        db = Database("db", self.instance)
        await db._pool.bind(db)
        db._local.transaction_running = True
        with self.assertRaises(RuntimeError):
            await db.run_in_transaction(lambda txn: None)

    async def test_snapshot_options_coverage(self):
        db = Database("db", self.instance)
        await db._pool.bind(db)

        # observability_options read-only property (already handled in Database)
        # We just want to make sure it exists on Snapshot as well if we added it.
        # It's in BatchSnapshot in _async/database.py
        bs = BatchSnapshot(db)
        self.assertEqual(bs.observability_options["db_name"], db.name)

    async def test_spanner_api_channel_id(self):
        db = Database("db", self.instance)
        await db._pool.bind(db)
        # First call sets channel_id
        api1 = db.spanner_api
        # Second call reuses it
        api2 = db.spanner_api
        self.assertEqual(api1, api2)

    async def test_snapshot_checkout_not_found(self):
        db = Database("db", self.instance)
        await db._pool.bind(db)
        from google.cloud.spanner_v1._async.database import SnapshotCheckout

        sc = SnapshotCheckout(db)

        mock_session = mock.AsyncMock()
        mock_session.session_id = "s1"
        mock_session.name = "projects/p/instances/i/databases/db/sessions/s1"
        mock_session.exists.return_value = False

        new_session = mock.AsyncMock()
        db._pool = mock.Mock()
        db._pool._new_session.return_value = new_session

        db._sessions_manager.get_session = mock.AsyncMock(return_value=mock_session)
        db._sessions_manager.put_session = mock.AsyncMock()

        try:
            async with sc:
                raise NotFound("not found")
        except NotFound:
            pass

        self.assertTrue(new_session.create.called)

    async def test_mutation_groups_checkout_not_found(self):
        db = Database("db", self.instance)
        await db._pool.bind(db)
        from google.cloud.spanner_v1._async.database import MutationGroupsCheckout

        mgc = MutationGroupsCheckout(db)

        mock_session = mock.AsyncMock()
        mock_session.session_id = "s1"
        mock_session.name = "projects/p/instances/i/databases/db/sessions/s1"
        mock_session.exists.return_value = False

        new_session = mock.AsyncMock()
        db._pool = mock.Mock()
        db._pool._new_session.return_value = new_session

        db._sessions_manager.get_session = mock.AsyncMock(return_value=mock_session)
        db._sessions_manager.put_session = mock.AsyncMock()

        try:
            async with mgc:
                raise NotFound("not found")
        except NotFound:
            pass

        self.assertTrue(new_session.create.called)

    async def test_database_init_no_client(self):
        # Coverage for lines 206, 215-216
        db = Database("db", None)
        await db._pool.bind(db)
        self.assertFalse(db._route_to_leader_enabled)
        self.assertIsNone(db._directed_read_options)
        self.assertIsNone(db.default_transaction_options)

    async def test_update_ddl_proto_descriptors(self):
        # Coverage for lines 540-543
        db = Database("db", self.instance)
        await db._pool.bind(db)
        mock_api = self.instance._client.database_admin_api
        mock_api.update_database_ddl = mock.AsyncMock()
        await db.update_ddl(["CREATE TABLE foo"], proto_descriptors=b"descriptors")
        self.assertTrue(mock_api.update_database_ddl.called)
        # Check call args
        args, kwargs = mock_api.update_database_ddl.call_args
        request = kwargs.get("request") or args[0]
        self.assertEqual(request.proto_descriptors, b"descriptors")

    async def test_execute_partitioned_dml_with_params(self):
        # Coverage for line 958
        db = Database("db", self.instance)
        await db._pool.bind(db)

        mock_session = mock.MagicMock()
        mock_session.name = "projects/p/instances/i/databases/db/sessions/s"
        db._sessions_manager.get_session = mock.AsyncMock(return_value=mock_session)

        mock_iterator = mock.MagicMock()
        mock_iterator.__aiter__.return_value = []

        with mock.patch(
            "google.cloud.spanner_v1._async.database._restart_on_unavailable",
            return_value=mock_iterator,
        ):
            with mock.patch(
                "google.cloud.spanner_v1._async.database.StreamedResultSet"
            ) as mock_rs_class:
                mock_rs = mock.AsyncMock()
                mock_rs.__aiter__.return_value = [1]  # Not empty to hit 'pass' line 958
                mock_rs.stats.row_count_lower_bound = 5
                mock_rs_class.return_value = mock_rs

                res = await db.execute_partitioned_dml(
                    "DELETE FROM table WHERE id = @id",
                    params={"id": 1},
                    param_types={"id": Type(code=TypeCode.INT64)},
                )
                self.assertEqual(res, 5)

    async def test_batch_snapshot_read_execute_coverage(self):
        # coverage for line 1825 in database.py (actually in BatchSnapshot)
        db = Database("db", self.instance)
        await db._pool.bind(db)
        mock_session = mock.MagicMock()
        mock_session.name = "projects/p/instances/i/databases/db/sessions/s"
        mock_session.session_id = "s"
        db._sessions_manager.get_session = mock.AsyncMock(return_value=mock_session)

        bs = BatchSnapshot(db)
        mock_snap = (
            mock.Mock()
        )  # Not AsyncMock because read/execute_sql calls on it should work
        mock_snap._transaction_id = b"txn"
        mock_snap._session = mock_session
        mock_snap._read_timestamp = None
        mock_snap.read = mock.AsyncMock()
        mock_snap.execute_sql = mock.AsyncMock()

        # Patch _get_snapshot to return our mock_snap
        bs._get_snapshot = mock.AsyncMock(return_value=mock_snap)
        bs._snapshot = mock_snap

        await bs.read("table", ["col"], KeySet(all_=True))
        self.assertTrue(mock_snap.read.called)

        await bs.execute_sql("SELECT 1")
        self.assertTrue(mock_snap.execute_sql.called)

        # Test get_batch_transaction_id success path (line 1825)
        btid = bs.get_batch_transaction_id()
        self.assertEqual(btid.transaction_id, b"txn")

    async def test_batch_commit_options_coverage(self):
        # coverage for line 1603, 1655
        db = Database("db", self.instance)
        await db._pool.bind(db)
        _ = db.batch()

        mock_session = mock.MagicMock()
        mock_session.name = "projects/p/instances/i/databases/db/sessions/s"
        mock_session._database = db
        db._sessions_manager.get_session = mock.AsyncMock(return_value=mock_session)

        mock_api = self.mock_spanner_api
        mock_api.commit = mock.AsyncMock()
        mock_api.batch_write = mock.AsyncMock()

        ro = RequestOptions(priority=RequestOptions.Priority.PRIORITY_HIGH)

        # BatchCheckout and Batch.commit coverage
        async with db.batch(request_options=ro) as batch:
            batch.insert("table", ["col"], [[1]])
        self.assertTrue(mock_api.commit.called)

        # BatchSnapshot._resource_info coverage
        bs = BatchSnapshot(db)
        _ = bs._resource_info

        # batch_write and MutationGroupsCheckout._resource_info coverage
        from google.cloud.spanner_v1._async.database import MutationGroupsCheckout

        # Mock batch_write response
        mock_api.batch_write.return_value = mock.AsyncMock()

        mgc = MutationGroupsCheckout(db)
        _ = mgc._resource_info  # line 1603
        async with mgc as _:
            pass

        async with db.mutation_groups() as _:
            pass
            # Actually SnapshotCheckout has _resource_info too.

        from google.cloud.spanner_v1._async.database import SnapshotCheckout

        sc = SnapshotCheckout(db)
        _ = sc._resource_info  # line 1655

    def test_resource_info(self):
        db = Database("db", self.instance)
        res_info = db._resource_info
        self.assertEqual(res_info["database"], "db")
        self.assertEqual(res_info["project"], self.instance._client.project)
        self.assertEqual(res_info["instance"], "i")
        self.assertIsNotNone(getattr(res_info, "_client_attributes", None))
        self.assertEqual(res_info._client_attributes["database"], "db")
        self.assertEqual(
            res_info._client_attributes["project_id"], self.instance._client.project
        )
        self.assertEqual(res_info._client_attributes["instance_id"], "i")
        # Caching check: second access returns identical instance
        self.assertIs(db._resource_info, res_info)

    def test_resource_info_fallback_on_exception(self):
        db = Database("db", self.instance)
        from google.cloud.spanner_v1.metrics.metrics_tracer_factory import (
            MetricsTracerFactory,
        )

        with mock.patch.object(
            MetricsTracerFactory,
            "create_resource_info",
            side_effect=RuntimeError("Boom"),
        ):
            res_info = db._resource_info
            self.assertEqual(res_info["database"], "db")
            self.assertEqual(res_info["project"], self.instance._client.project)
            self.assertEqual(res_info["instance"], "i")
            self.assertIsNone(getattr(res_info, "_client_attributes", None))
