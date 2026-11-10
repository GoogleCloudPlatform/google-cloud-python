# Copyright 2020 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

from unittest import mock

from tests.unit.django_spanner.simple_test import SpannerSimpleTestClass


class TestBase(SpannerSimpleTestClass):
    def setUp(self):
        super().setUp()
        import django_spanner.base

        django_spanner.base._SPANNER_CLIENT_CACHE = None
        self.client_patcher = mock.patch("django_spanner.base.spanner.Client")
        self.mock_client = self.client_patcher.start()
        self.mock_client.return_value.instance.return_value.instance_id = (
            self.INSTANCE_ID
        )
        self.addCleanup(self.client_patcher.stop)

    def test_property_instance(self):
        with mock.patch("django_spanner.base.spanner") as mock_spanner:
            mock_spanner.Client = mock_client = mock.MagicMock()
            mock_client.return_value.instance = mock_instance = mock.MagicMock()
            _ = self.db_wrapper.instance
            # Instance should be called on the return value of Client()
            self.assertTrue(mock_instance.called)

    def test_property_nodb_connection(self):
        with self.assertRaises(NotImplementedError):
            self.db_wrapper._nodb_connection()

    def test_get_connection_params(self):
        params = self.db_wrapper.get_connection_params()

        self.assertEqual(params["project"], self.PROJECT)
        self.assertEqual(params["instance_id"], self.INSTANCE_ID)
        self.assertEqual(params["database_id"], self.DATABASE_ID)
        self.assertEqual(params["user_agent"], self.USER_AGENT)
        self.assertEqual(params["option"], self.OPTIONS["option"])

    def test_get_new_connection(self):
        self.db_wrapper.Database = mock_database = mock.MagicMock()
        mock_database.connect = mock_connection = mock.MagicMock()
        conn_params = {"test_param": "dummy"}
        self.db_wrapper.get_new_connection(conn_params)
        mock_connection.assert_called_once_with(
            self.INSTANCE_ID,
            client=mock_database.connect.call_args[1]["client"],
            **conn_params,
        )

    def test_init_connection_state(self):
        from google.cloud.spanner_dbapi.connection import Connection

        self.db_wrapper.connection = mock_connection = Connection(
            self.db_wrapper.instance, "dummy_db"
        )
        mock_connection.close = mock_close = mock.MagicMock()
        self.db_wrapper.init_connection_state()
        mock_close.assert_called_once_with()

    def test_create_cursor(self):
        self.db_wrapper.connection = mock_connection = mock.MagicMock()
        mock_connection.cursor = mock_cursor = mock.MagicMock()
        self.db_wrapper.create_cursor()
        mock_cursor.assert_called_once_with()

    def test_set_autocommit(self):
        self.db_wrapper.connection = mock_connection = mock.MagicMock()
        mock_connection.autocommit = False
        self.db_wrapper._set_autocommit(True)
        self.assertEqual(mock_connection.autocommit, True)

    def test_is_usable(self):
        self.db_wrapper.connection = None
        self.assertFalse(self.db_wrapper.is_usable())

        self.db_wrapper.connection = mock_connection = mock.MagicMock()
        mock_connection.is_closed = True
        self.assertFalse(self.db_wrapper.is_usable())

        mock_connection.is_closed = False
        self.assertTrue(self.db_wrapper.is_usable())

    def test_is_usable_with_error(self):
        from google.cloud.spanner_dbapi.exceptions import Error

        self.db_wrapper.connection = mock_connection = mock.MagicMock()
        mock_connection.cursor = mock.MagicMock(side_effect=Error)
        self.assertFalse(self.db_wrapper.is_usable())

    def test_start_transaction_under_autocommit(self):
        self.db_wrapper.connection = mock_connection = mock.MagicMock()
        mock_connection.cursor = mock_cursor = mock.MagicMock()
        self.db_wrapper._start_transaction_under_autocommit()
        mock_cursor.assert_called_once_with()

    def test_auto_batch_ddl_default_and_settings_precedence(self):
        from django.core.exceptions import ImproperlyConfigured

        self.assertFalse(self.db_wrapper.auto_batch_ddl)

        self.db_wrapper.settings_dict["OPTIONS"]["auto_batch_ddl"] = True
        self.assertTrue(self.db_wrapper.auto_batch_ddl)

        # Top-level AUTO_BATCH_DDL takes precedence over OPTIONS["auto_batch_ddl"].
        self.db_wrapper.settings_dict["AUTO_BATCH_DDL"] = "FALSE"
        self.assertFalse(self.db_wrapper.auto_batch_ddl)

        self.db_wrapper.settings_dict["OPTIONS"]["auto_batch_ddl"] = False
        self.db_wrapper.settings_dict["AUTO_BATCH_DDL"] = "true"
        self.assertTrue(self.db_wrapper.auto_batch_ddl)

        for invalid in ("maybe", None, 1):
            self.db_wrapper.settings_dict["AUTO_BATCH_DDL"] = invalid
            with self.assertRaises(ImproperlyConfigured):
                _ = self.db_wrapper.auto_batch_ddl

        self.db_wrapper.settings_dict.pop("AUTO_BATCH_DDL", None)
        self.db_wrapper.settings_dict["OPTIONS"].pop("auto_batch_ddl", None)

    def test_get_new_connection_strips_auto_batch_ddl_option(self):
        self.db_wrapper.Database = mock_database = mock.MagicMock()
        mock_connection = mock_database.connect
        conn_params = {"auto_batch_ddl": True, "test_param": "dummy"}
        self.db_wrapper.get_new_connection(conn_params)
        self.assertNotIn("auto_batch_ddl", mock_connection.call_args[1])
        self.assertEqual(mock_connection.call_args[1]["test_param"], "dummy")

    def test_ddl_batch_reuses_scoped_dbapi_transaction_lifecycle(self):
        import warnings

        from django.db.utils import InterfaceError, ProgrammingError
        from google.cloud.spanner_dbapi.connection import Connection

        mock_db = mock.MagicMock()
        snapshot_cm = mock.MagicMock()
        snapshot_obj = mock.MagicMock()
        snapshot_obj.execute_sql.return_value = iter([])
        snapshot_cm.__enter__.return_value = snapshot_obj
        mock_db.snapshot.return_value = snapshot_cm

        real_conn = Connection(self.db_wrapper.instance, mock_db)
        real_conn.autocommit = True
        self.db_wrapper.connection = real_conn
        self.db_wrapper.autocommit = True

        with (
            mock.patch.object(real_conn, "begin", wraps=real_conn.begin) as spy_begin,
            mock.patch.object(
                real_conn, "commit", wraps=real_conn.commit
            ) as spy_commit,
            mock.patch.object(
                real_conn, "rollback", wraps=real_conn.rollback
            ) as spy_rollback,
            mock.patch.object(
                real_conn,
                "run_prior_DDL_statements",
                wraps=real_conn.run_prior_DDL_statements,
            ) as spy_run_prior,
            warnings.catch_warnings(record=True) as caught_warnings,
        ):
            warnings.simplefilter("always")
            self.db_wrapper.start_batch_ddl(auto_flush=True)
            # Lazy entry: Connection.begin() is not called until the first DDL.
            self.assertEqual(spy_begin.call_count, 0)

            with self.db_wrapper.create_cursor() as cur:
                cur.execute("CREATE TABLE t1 (id INT64) PRIMARY KEY (id)")
                self.assertEqual(spy_begin.call_count, 1)
                cur.execute("CREATE INDEX t1_idx ON t1 (id)")
                self.assertEqual(spy_begin.call_count, 1)
                mock_db.update_ddl.assert_not_called()

                # Snapshot query commits the scoped DDL burst, then executes cleanly.
                cur.run_sql_in_snapshot("SELECT 1")
                self.assertEqual(spy_commit.call_count, 1)
                self.assertEqual(spy_run_prior.call_count, 2)
                mock_db.update_ddl.assert_called_once_with(
                    [
                        "CREATE TABLE t1 (id INT64) PRIMARY KEY (id)",
                        "CREATE INDEX t1_idx ON t1 (id)",
                    ]
                )

                # Explicit client transaction runs unimpeded while outer auto_flush
                # DDL batch stays open, then subsequent DDL opens a new burst.
                cur.execute("BEGIN")
                cur.execute("ROLLBACK")
                self.assertTrue(self.db_wrapper.in_ddl_batch)

                cur.execute("CREATE TABLE aborted_t (id INT64) PRIMARY KEY (id)")
                self.db_wrapper.abort_batch()
                self.assertGreaterEqual(spy_rollback.call_count, 2)
                # Verify abort_batch cleared _ddl_statements so later snapshot SQL
                # never leaks the aborted statement into update_ddl.
                mock_db.update_ddl.reset_mock()
                cur.run_sql_in_snapshot("SELECT 1")
                mock_db.update_ddl.assert_not_called()

            self.assertEqual(caught_warnings, [])

        # First-statement failure in raw cursor rolls back Connection.begin();
        # second-statement failure preserves already-queued DDL until abort/exit.
        self.db_wrapper.start_batch_ddl()
        fail_first = mock.MagicMock(
            spec=["connection", "is_closed", "execute", "close"]
        )
        fail_first.connection = real_conn
        fail_first.is_closed = False
        fail_first.execute.side_effect = RuntimeError("raw execute boom")
        with mock.patch.object(real_conn, "cursor", return_value=fail_first):
            with self.assertRaises(RuntimeError):
                self.db_wrapper.create_cursor().execute(
                    "CREATE TABLE bad1 (id INT64) PRIMARY KEY (id)"
                )
        self.assertEqual(self.db_wrapper.buffered_ddl_statements, ())

        with self.db_wrapper.create_cursor() as cur:
            cur.execute("CREATE TABLE keep1 (id INT64) PRIMARY KEY (id)")
        with mock.patch.object(real_conn, "cursor", return_value=fail_first):
            with self.assertRaises(RuntimeError):
                self.db_wrapper.create_cursor().execute(
                    "CREATE TABLE bad2 (id INT64) PRIMARY KEY (id)"
                )
        self.assertEqual(
            self.db_wrapper.buffered_ddl_statements,
            ("CREATE TABLE keep1 (id INT64) PRIMARY KEY (id)",),
        )
        self.db_wrapper.abort_batch()

        # Closed and disconnected cursors raise PEP 249 InterfaceError / ProgrammingError.
        closed_cur = self.db_wrapper.create_cursor()
        closed_cur.close()
        with self.assertRaises(InterfaceError):
            closed_cur.execute("START BATCH DDL")

        disconnected_raw = mock.MagicMock(
            spec=["connection", "is_closed", "execute", "close"]
        )
        disconnected_raw.connection = None
        disconnected_raw.is_closed = False
        with mock.patch.object(real_conn, "cursor", return_value=disconnected_raw):
            with self.assertRaises(ProgrammingError):
                self.db_wrapper.create_cursor().execute("START BATCH DDL")

    def test_ddl_batch_state_lifecycle_and_errors(self):
        from django.db.utils import (
            IntegrityError,
            OperationalError,
            ProgrammingError,
        )
        from google.api_core.exceptions import (
            AlreadyExists,
            FailedPrecondition,
            InternalServerError,
            InvalidArgument,
            ServiceUnavailable,
        )
        from google.cloud.spanner_dbapi.connection import Connection

        # Empty flush is a no-op without opening a connection.
        self.db_wrapper.connection = None
        self.assertIsNone(self.db_wrapper.flush_ddl_batch())

        # Running or aborting when inactive raises Django ProgrammingError.
        with self.assertRaises(ProgrammingError):
            self.db_wrapper.run_batch()
        with self.assertRaises(ProgrammingError):
            self.db_wrapper.abort_batch()

        # Starting while in atomic block or non-autocommit fails.
        self.db_wrapper.in_atomic_block = True
        try:
            with self.assertRaises(ProgrammingError):
                self.db_wrapper.start_batch_ddl()
        finally:
            self.db_wrapper.in_atomic_block = False

        self.db_wrapper.settings_dict["AUTOCOMMIT"] = False
        try:
            with self.assertRaises(ProgrammingError):
                self.db_wrapper.start_batch_ddl()
        finally:
            self.db_wrapper.settings_dict["AUTOCOMMIT"] = True

        # Start lazy DDL batch before connection exists: nested lazy ddl_batch,
        # lazy checkpoint/rollback, lazy run_batch, lazy abort_batch, and close().
        self.db_wrapper.start_batch_ddl()
        self.assertTrue(self.db_wrapper.in_ddl_batch)
        self.assertTrue(self.db_wrapper.ddl_batch_auto_flush)
        with self.assertRaises(ProgrammingError):
            self.db_wrapper.start_batch_ddl()
        cp = self.db_wrapper.checkpoint_ddl_batch()
        self.assertEqual(cp, (0, 0))
        with self.assertRaises(RuntimeError):
            with self.db_wrapper.ddl_batch(auto_flush=False):
                self.assertFalse(self.db_wrapper.ddl_batch_auto_flush)
                raise RuntimeError("lazy nested rollback")
        self.assertTrue(self.db_wrapper.ddl_batch_auto_flush)
        self.db_wrapper.rollback_ddl_checkpoint(cp)
        self.assertIsNone(self.db_wrapper.run_batch())
        self.assertFalse(self.db_wrapper.in_ddl_batch)

        self.db_wrapper.start_batch_ddl()
        self.assertIsNone(self.db_wrapper.abort_batch())
        self.assertFalse(self.db_wrapper.in_ddl_batch)

        self.db_wrapper.start_batch_ddl()
        self.db_wrapper.close()
        self.assertFalse(self.db_wrapper.in_ddl_batch)
        self.assertEqual(self.db_wrapper.buffered_ddl_statements, ())

        # Bind a real spanner_dbapi.Connection backed by a mock Database.
        mock_db = mock.MagicMock()
        real_conn = Connection(self.db_wrapper.instance, mock_db)
        real_conn.autocommit = True
        self.db_wrapper.connection = real_conn
        self.db_wrapper.autocommit = True

        # Reject starting, staging, flushing, or lazy-initializing DDL on read-only connection.
        ro_conn = Connection(self.db_wrapper.instance, mock_db, read_only=True)
        ro_conn.autocommit = True
        ro_conn.close = mock.MagicMock()
        self.db_wrapper.connection = ro_conn
        with self.assertRaises(ProgrammingError):
            self.db_wrapper.start_batch_ddl()
        self.db_wrapper.connection = None
        self.db_wrapper.start_batch_ddl()
        self.db_wrapper.connection = ro_conn
        with self.assertRaises(ProgrammingError):
            self.db_wrapper.create_cursor().execute(
                "CREATE TABLE ro_t (id INT64) PRIMARY KEY (id)"
            )
        with self.assertRaises(ProgrammingError):
            self.db_wrapper.flush_ddl_batch()
        with self.assertRaises(ProgrammingError):
            self.db_wrapper.init_connection_state()
        self.assertFalse(self.db_wrapper.in_ddl_batch)
        self.db_wrapper.connection = real_conn

        mock_dml_exec = mock.MagicMock()
        mock_dml_exec.run_batch_dml.return_value = "dml_res"
        with mock.patch(
            "google.cloud.spanner_dbapi.connection.BatchDmlExecutor",
            return_value=mock_dml_exec,
        ):
            real_conn.start_batch_dml(real_conn.cursor())
            with self.assertRaises(ProgrammingError):
                self.db_wrapper.start_batch_ddl()
            self.assertEqual(self.db_wrapper.run_batch(), "dml_res")
            mock_dml_exec.run_batch_dml.assert_called_once_with()

            real_conn.start_batch_dml(real_conn.cursor())
            self.db_wrapper.abort_batch()

        with self.assertRaises(ProgrammingError):
            self.db_wrapper.run_batch()
        with self.assertRaises(ProgrammingError):
            self.db_wrapper.abort_batch()

        # Empty flush while connected and active returns None without update_ddl RPC.
        self.db_wrapper.start_batch_ddl()
        self.assertIsNone(self.db_wrapper.flush_ddl_batch())
        self.assertIsNone(self.db_wrapper.run_batch())
        mock_db.update_ddl.assert_not_called()

        # Map GoogleAPICallError subclasses to Django DatabaseError types and emit OTel spans.
        error_cases = [
            (AlreadyExists("dup"), IntegrityError),
            (FailedPrecondition("precond"), IntegrityError),
            (InvalidArgument("bad syntax"), ProgrammingError),
            (InternalServerError("boom"), OperationalError),
            (ServiceUnavailable("transient"), OperationalError),
        ]
        for api_exc, expected_django_exc in error_cases:
            self.ot_exporter.clear()
            mock_db.update_ddl.side_effect = api_exc
            with self.assertRaises(expected_django_exc) as exc_cm:
                with self.db_wrapper.ddl_batch():
                    with self.db_wrapper.create_cursor() as cur:
                        cur.execute("CREATE TABLE t (id INT64) PRIMARY KEY (id)")
            self.assertIn(api_exc.message, str(exc_cm.exception))
            self.assertFalse(self.db_wrapper.in_ddl_batch)
            self.assertEqual(self.db_wrapper.buffered_ddl_statements, ())
            spans = self.ot_exporter.get_finished_spans()
            self.assertEqual(spans[-1].name, "CloudSpannerDjango.flush_ddl_batch")
            self.assertEqual(spans[-1].attributes["statement_count"], 1)

        mock_db.update_ddl.side_effect = None
        mock_db.update_ddl.reset_mock()

        # Flush DDL batch traces non-empty flush while keeping batch active.
        self.ot_exporter.clear()
        self.db_wrapper.start_batch_ddl()
        with self.db_wrapper.create_cursor() as cur:
            cur.execute("CREATE TABLE t_flush (id INT64) PRIMARY KEY (id)")
        self.db_wrapper.flush_ddl_batch()
        spans = self.ot_exporter.get_finished_spans()
        self.assertEqual(spans[-1].name, "CloudSpannerDjango.flush_ddl_batch")
        self.assertEqual(spans[-1].attributes["statement_count"], 1)
        self.assertTrue(self.db_wrapper.in_ddl_batch)
        self.db_wrapper.run_batch()

        # Missing database raises ValueError on cursor execute and flush_ddl_batch.
        no_db_conn = Connection(self.db_wrapper.instance, None)
        no_db_conn.autocommit = True
        self.db_wrapper.connection = no_db_conn
        self.db_wrapper.start_batch_ddl()
        with self.assertRaises(ValueError):
            self.db_wrapper.create_cursor().execute(
                "CREATE TABLE no_db_t (id INT64) PRIMARY KEY (id)"
            )
        with self.assertRaises(ValueError):
            self.db_wrapper.flush_ddl_batch()
        self.db_wrapper.abort_batch()
        self.db_wrapper.connection = real_conn

        # _set_autocommit(False) and _start_transaction_under_autocommit flush
        # in auto_flush mode and raise in strict mode.
        mock_db.update_ddl.reset_mock()
        self.db_wrapper.start_batch_ddl(auto_flush=True)
        with self.db_wrapper.create_cursor() as cur:
            cur.execute("CREATE TABLE t_auto (id INT64) PRIMARY KEY (id)")
        self.db_wrapper._set_autocommit(False)
        mock_db.update_ddl.assert_called_with(
            ["CREATE TABLE t_auto (id INT64) PRIMARY KEY (id)"]
        )
        self.db_wrapper._set_autocommit(True)
        self.db_wrapper.abort_batch()

        self.db_wrapper.start_batch_ddl(auto_flush=True)
        with self.db_wrapper.create_cursor() as cur:
            cur.execute("CREATE TABLE t_tx (id INT64) PRIMARY KEY (id)")
        self.db_wrapper._start_transaction_under_autocommit()
        mock_db.update_ddl.assert_called_with(
            ["CREATE TABLE t_tx (id INT64) PRIMARY KEY (id)"]
        )
        real_conn.rollback()
        self.db_wrapper.abort_batch()

        self.db_wrapper.start_batch_ddl(auto_flush=False)
        with self.assertRaises(ProgrammingError):
            self.db_wrapper._set_autocommit(False)
        with self.assertRaises(ProgrammingError):
            self.db_wrapper._start_transaction_under_autocommit()
        self.db_wrapper.abort_batch()

        # Lazy pre-connect DDL batch stays active across init_connection_state,
        # and manual init_connection_state warns when dropping un-flushed DDL.
        real_conn.close = mock.MagicMock()
        self.db_wrapper.connection = None
        self.db_wrapper.start_batch_ddl(auto_flush=False)
        self.db_wrapper.connection = real_conn
        self.db_wrapper.init_connection_state()
        self.assertTrue(self.db_wrapper.in_ddl_batch)
        self.assertFalse(self.db_wrapper.ddl_batch_auto_flush)
        with self.db_wrapper.create_cursor() as cur:
            cur.execute("CREATE TABLE stale_t (id INT64) PRIMARY KEY (id)")
        self.assertEqual(len(self.db_wrapper.buffered_ddl_statements), 1)
        with self.assertLogs("django_spanner.base", level="WARNING") as cm:
            self.db_wrapper.init_connection_state()
        self.assertTrue(any("re-initialization" in msg for msg in cm.output))
        self.assertFalse(self.db_wrapper.in_ddl_batch)
        self.assertEqual(self.db_wrapper.buffered_ddl_statements, ())

    def test_ddl_cursor_proxy_formatting_and_guard_branches(self):
        import asyncio

        from django.db.utils import ProgrammingError
        from google.cloud.spanner_dbapi import batch_dml_executor
        from google.cloud.spanner_dbapi.connection import Connection

        mock_db = mock.MagicMock()
        snapshot_cm = mock.MagicMock()
        snapshot_obj = mock.MagicMock()
        snapshot_obj.execute_sql.return_value = iter([])
        snapshot_cm.__enter__.return_value = snapshot_obj
        mock_db.snapshot.return_value = snapshot_cm

        real_conn = Connection(self.db_wrapper.instance, mock_db)
        real_conn.autocommit = True
        self.db_wrapper.connection = real_conn
        self.db_wrapper.autocommit = True

        # Async autocommit helper delegates cleanly to _set_autocommit.
        asyncio.run(self.db_wrapper._a_set_autocommit(True))

        # Default AUTO_BATCH_DDL=False keeps schema_editor() unbatched;
        # lazy unopened wrapper with AUTO_BATCH_DDL=True inspects AUTOCOMMIT setting.
        with self.db_wrapper.schema_editor():
            self.assertFalse(self.db_wrapper.in_ddl_batch)

        self.db_wrapper.settings_dict["AUTO_BATCH_DDL"] = True
        try:
            self.db_wrapper.connection = None
            with self.db_wrapper.schema_editor():
                self.assertTrue(self.db_wrapper.in_ddl_batch)
            self.assertFalse(self.db_wrapper.in_ddl_batch)

            # Lazy nested ddl_batch connecting mid-block rolls back checkpoint on error.
            self.db_wrapper.start_batch_ddl(auto_flush=True)
            with self.assertRaises(RuntimeError):
                with self.db_wrapper.ddl_batch(auto_flush=False):
                    self.db_wrapper.connection = real_conn
                    with self.db_wrapper.create_cursor() as lazy_cur:
                        lazy_cur.execute(
                            "CREATE TABLE lazy_drop (id INT64) PRIMARY KEY (id)"
                        )
                    raise RuntimeError("abort after lazy connect")
            self.assertEqual(self.db_wrapper.buffered_ddl_statements, ())
            self.db_wrapper.abort_batch()

            self.db_wrapper.connection = real_conn
            self.db_wrapper.autocommit = False
            with self.db_wrapper.schema_editor():
                self.assertFalse(self.db_wrapper.in_ddl_batch)
            with self.assertRaises(ProgrammingError):
                self.db_wrapper.start_batch_ddl()
            self.db_wrapper.autocommit = True

            real_conn.begin()
            with self.db_wrapper.schema_editor():
                self.assertFalse(self.db_wrapper.in_ddl_batch)
            with self.assertRaises(ProgrammingError):
                self.db_wrapper.start_batch_ddl()
            real_conn.rollback()

            ro_conn = Connection(self.db_wrapper.instance, mock_db, read_only=True)
            ro_conn.autocommit = True
            self.db_wrapper.connection = ro_conn
            with self.db_wrapper.schema_editor():
                self.assertFalse(self.db_wrapper.in_ddl_batch)
            self.db_wrapper.connection = real_conn

            real_conn.start_batch_dml(real_conn.cursor())
            with self.db_wrapper.schema_editor():
                self.assertFalse(self.db_wrapper.in_ddl_batch)
            real_conn.abort_batch()
        finally:
            self.db_wrapper.settings_dict.pop("AUTO_BATCH_DDL", None)

        # Proxy cursor attributes, iteration, client-side comments, callproc, and executemany.
        cur = self.db_wrapper.create_cursor()
        cur.arraysize = 50
        self.assertEqual(cur.arraysize, 50)
        with self.assertRaises(ProgrammingError):
            next(iter(cur))
        with self.assertRaises(ProgrammingError):
            next(cur)
        cur.callproc("sp_noop")
        cur.callproc("sp_args", [1])
        cur.execute("/* leading */ START BATCH DDL; -- trailing")
        with self.assertRaises(ProgrammingError):
            cur.execute("START BATCH DDL; SELECT 1")
        cur.execute("ABORT BATCH")

        # Nested ddl_batch(auto_flush=False) tightens strictness, formats %s / %(k)s
        # GoogleSQL literals safely, blocks parameter injection, and rolls back inner DDL.
        with self.db_wrapper.ddl_batch(auto_flush=True):
            cur.execute("CREATE TABLE outer_ok (id INT64) PRIMARY KEY (id)")
            cur.execute(
                "ALTER TABLE outer_ok ADD COLUMN c STRING(20) DEFAULT (%(d)s)",
                {"d": "a'b"},
            )
            with self.assertRaises(ProgrammingError):
                cur.execute("ALTER TABLE outer_ok ADD COLUMN bad INT64", 123)
            with self.assertRaises(ProgrammingError):
                cur.execute(
                    "ALTER TABLE outer_ok ADD COLUMN bad INT64 DEFAULT (%s)",
                    [1, 2],
                )
            with self.assertRaises(ProgrammingError):
                cur.execute("   ; -- empty with params", [1])
            with self.assertRaises(RuntimeError):
                with self.db_wrapper.ddl_batch(auto_flush=False):
                    self.assertFalse(self.db_wrapper.ddl_batch_auto_flush)
                    cur.execute("CREATE TABLE inner_drop (id INT64) PRIMARY KEY (id)")
                    with self.assertRaises(ProgrammingError):
                        cur.get_table_column_schema("outer_ok")
                    raise RuntimeError("rollback inner")
            self.assertTrue(self.db_wrapper.ddl_batch_auto_flush)
            self.assertEqual(
                self.db_wrapper.buffered_ddl_statements,
                (
                    "CREATE TABLE outer_ok (id INT64) PRIMARY KEY (id)",
                    r"ALTER TABLE outer_ok ADD COLUMN c STRING(20) DEFAULT ('a\'b')",
                ),
            )

            # Snapshot helpers, executemany, and START BATCH DML flush cleanly.
            cur.list_tables()
            self.assertEqual(self.db_wrapper.buffered_ddl_statements, ())
            cur.execute("CREATE TABLE after_list (id INT64) PRIMARY KEY (id)")
            cur.get_table_column_schema("after_list")
            self.assertEqual(self.db_wrapper.buffered_ddl_statements, ())

            with mock.patch.object(
                batch_dml_executor, "run_batch_dml", return_value=mock.MagicMock()
            ):
                cur.execute("CREATE TABLE before_many (id INT64) PRIMARY KEY (id)")
                cur.executemany("INSERT INTO outer_ok (id) VALUES (%s)", [(1,)])
                self.assertEqual(self.db_wrapper.buffered_ddl_statements, ())

            with self.assertRaises(ProgrammingError):
                cur.executemany("DROP TABLE outer_ok", [()])

            # Parameterized DDL double-quote mistake / injection guard and mixed SQL guard.
            with self.assertRaises(ProgrammingError):
                cur.execute(
                    "ALTER TABLE outer_ok ADD COLUMN bad STRING(40) DEFAULT ('%s')",
                    ["x); SELECT 1; --"],
                )
            with self.assertRaises(ProgrammingError):
                cur.execute(
                    "CREATE TABLE m1 (id INT64) PRIMARY KEY (id); "
                    "INSERT INTO m1 (id) VALUES (%s)",
                    [1],
                )

            with self.assertRaises(_SimulatedInterrupt):
                with self.db_wrapper.ddl_batch(auto_flush=True):
                    cur.execute(
                        "CREATE TABLE flushed_in_inner (id INT64) PRIMARY KEY (id)"
                    )
                    cur.list_tables()
                    cur.execute(
                        "CREATE TABLE dropped_post_flush (id INT64) PRIMARY KEY (id)"
                    )
                    raise _SimulatedInterrupt("interrupt inner after flush")
            self.assertEqual(self.db_wrapper.buffered_ddl_statements, ())

            cur.execute("CREATE TABLE pre_dml_b (id INT64) PRIMARY KEY (id)")
            cur.execute("START BATCH DML")
            self.assertEqual(self.db_wrapper.buffered_ddl_statements, ())
            cur.executemany("SELECT 1", [])
            with self.assertRaises(ProgrammingError):
                cur.execute("START BATCH DDL")
            cur.execute("ABORT BATCH")

        # BaseException unwinds outer ddl_batch cleanly; outer error preventing
        # inner finally from restoring auto_flush handles inactive flag safely.
        with self.assertRaises(_SimulatedInterrupt):
            with self.db_wrapper.ddl_batch():
                with self.db_wrapper.ddl_batch(auto_flush=False):
                    with self.db_wrapper.create_cursor() as inner_cur:
                        inner_cur.execute(
                            "CREATE TABLE base_exc_t (id INT64) PRIMARY KEY (id)"
                        )
                    self.db_wrapper.abort_batch()
                    raise _SimulatedInterrupt("ctrl-c")
        self.assertFalse(self.db_wrapper.in_ddl_batch)
        self.assertEqual(self.db_wrapper.buffered_ddl_statements, ())

        # _close() helper discards active DDL batch before super()._close().
        self.db_wrapper.start_batch_ddl()
        real_conn.close = mock.MagicMock()
        self.db_wrapper._close()
        self.assertFalse(self.db_wrapper.in_ddl_batch)

        # _start_transaction_under_autocommit fallback when ALLOW_TRANSACTIONS_IN_AUTO_COMMIT=False.
        raw_cursor = mock.MagicMock()
        mock_conn = mock.MagicMock()
        mock_conn.cursor.return_value = raw_cursor
        self.db_wrapper.connection = mock_conn
        self.db_wrapper.settings_dict["ALLOW_TRANSACTIONS_IN_AUTO_COMMIT"] = False
        try:
            self.db_wrapper._start_transaction_under_autocommit()
            raw_cursor.execute.assert_called_with("SELECT 1")
        finally:
            self.db_wrapper.settings_dict.pop("ALLOW_TRANSACTIONS_IN_AUTO_COMMIT", None)


class _SimulatedInterrupt(BaseException):
    pass
