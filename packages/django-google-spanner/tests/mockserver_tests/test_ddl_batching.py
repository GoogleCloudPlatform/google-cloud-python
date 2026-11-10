# Copyright 2026 Google LLC All rights reserved.
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

import threading
from contextlib import contextmanager
from unittest import mock

import google.cloud.spanner_v1.types.result_set as result_set
import google.cloud.spanner_v1.types.type as spanner_type
import grpc
from django.db import (
    IntegrityError,
    InterfaceError,
    OperationalError,
    ProgrammingError,
    connection,
    migrations,
    models,
    transaction,
)
from django.db.migrations.executor import MigrationExecutor
from django.db.migrations.state import ProjectState
from django.test.utils import CaptureQueriesContext
from google.cloud.spanner_v1 import TypeCode

from django_spanner.base import DatabaseWrapper
from tests.mockserver_tests.mock_server_test_base import (
    MockServerTestBase,
    add_result,
    add_select1_result,
    add_update_count,
)


def _add_empty_result(sql: str):
    """Register an empty ResultSet on the mock Spanner service for ``sql``."""
    res = result_set.ResultSet(
        dict(
            metadata=result_set.ResultSetMetadata(
                dict(
                    row_type=spanner_type.StructType(
                        dict(
                            fields=[
                                spanner_type.StructType.Field(
                                    dict(
                                        name="c",
                                        type=spanner_type.Type(
                                            dict(code=TypeCode.STRING)
                                        ),
                                    )
                                )
                            ]
                        )
                    )
                )
            )
        )
    )
    add_result(sql, res)


class TestDdlBatching(MockServerTestBase):
    """End-to-end MockServer tests for Django Spanner DDL batching."""

    def _ddl_batches(self):
        return [list(req.statements) for req in self.database_admin_service.requests]

    @contextmanager
    def _auto_batch_ddl(self, enabled=True):
        had_key = "AUTO_BATCH_DDL" in connection.settings_dict
        prev = connection.settings_dict.get("AUTO_BATCH_DDL")
        connection.settings_dict["AUTO_BATCH_DDL"] = enabled
        try:
            yield
        finally:
            if had_key:
                connection.settings_dict["AUTO_BATCH_DDL"] = prev
            else:
                connection.settings_dict.pop("AUTO_BATCH_DDL", None)

    def test_multi_model_migration_batches_all_ddl_into_single_rpc(self):
        mig = migrations.Migration("0001_initial", "batch_app")
        mig.operations = [
            migrations.CreateModel(
                name="Author",
                fields=[
                    ("id", models.BigAutoField(primary_key=True)),
                    ("email", models.CharField(max_length=120, unique=True)),
                    ("name", models.CharField(max_length=80, db_index=True)),
                ],
            ),
            migrations.CreateModel(
                name="Tag",
                fields=[
                    ("id", models.BigAutoField(primary_key=True)),
                    ("slug", models.SlugField(unique=True)),
                ],
            ),
            migrations.CreateModel(
                name="Book",
                fields=[
                    ("id", models.BigAutoField(primary_key=True)),
                    ("title", models.CharField(max_length=200, db_index=True)),
                    (
                        "author",
                        models.ForeignKey("batch_app.Author", on_delete=models.CASCADE),
                    ),
                    ("tags", models.ManyToManyField("batch_app.Tag")),
                ],
            ),
        ]

        state = ProjectState()
        with self._auto_batch_ddl(True):
            with CaptureQueriesContext(connection) as captured:
                with connection.schema_editor(atomic=mig.atomic) as editor:
                    mig.apply(state, editor)

        batches = self._ddl_batches()
        self.assertEqual(len(batches), 1)
        stmts = batches[0]
        self.assertGreaterEqual(len(stmts), 10)
        # All CREATE TABLE statements execute before deferred indexes and FKs.
        first_index_or_fk = next(
            i for i, s in enumerate(stmts) if not s.startswith("CREATE TABLE ")
        )
        for s in stmts[:first_index_or_fk]:
            self.assertTrue(s.startswith("CREATE TABLE "))
        self.assertTrue(all(not s.endswith(";") for s in stmts))
        # CursorDebugWrapper continues to observe every individual DDL statement.
        self.assertEqual(len(captured), len(stmts))
        self.assertFalse(connection.in_ddl_batch)
        self.assertEqual(connection.buffered_ddl_statements, ())

    def test_auto_batch_ddl_false_executes_each_ddl_individually(self):
        mig = migrations.Migration("0001_no_batch", "nobatch_app")
        mig.operations = [
            migrations.CreateModel(
                name="Item",
                fields=[
                    ("id", models.BigAutoField(primary_key=True)),
                    ("code", models.CharField(max_length=40, unique=True)),
                    ("name", models.CharField(max_length=40, db_index=True)),
                ],
            ),
        ]
        # 1. Default (unset) AUTO_BATCH_DDL is False: each DDL statement runs individually.
        self.assertNotIn("AUTO_BATCH_DDL", connection.settings_dict)
        self.assertFalse(connection.auto_batch_ddl)
        with connection.schema_editor(atomic=mig.atomic) as editor:
            mig.apply(ProjectState(), editor)
        batches = self._ddl_batches()
        self.assertEqual(len(batches), 3)
        self.assertTrue(all(len(b) == 1 for b in batches))

        # 2. OPTIONS["auto_batch_ddl"] = True opts in; top-level AUTO_BATCH_DDL = False overrides it.
        self.database_admin_service.clear_requests()
        connection.settings_dict["OPTIONS"]["auto_batch_ddl"] = True
        try:
            self.assertTrue(connection.auto_batch_ddl)
            with connection.schema_editor(atomic=mig.atomic) as editor:
                mig.apply(ProjectState(), editor)
            self.assertEqual(len(self._ddl_batches()), 1)
            self.assertEqual(len(self._ddl_batches()[0]), 3)

            self.database_admin_service.clear_requests()
            with self._auto_batch_ddl(False):
                self.assertFalse(connection.auto_batch_ddl)
                with connection.schema_editor(atomic=mig.atomic) as editor:
                    mig.apply(ProjectState(), editor)
            batches = self._ddl_batches()
            self.assertEqual(len(batches), 3)
            self.assertTrue(all(len(b) == 1 for b in batches))
        finally:
            connection.settings_dict["OPTIONS"].pop("auto_batch_ddl", None)

    def test_apply_migration_without_deferred_sql_flushes_before_recording(self):
        mig = migrations.Migration("0001_simple", "rec_app")
        mig.operations = [
            migrations.CreateModel(
                name="Simple",
                fields=[
                    ("id", models.BigAutoField(primary_key=True)),
                    ("label", models.CharField(max_length=50)),
                ],
            ),
            migrations.CreateModel(
                name="SimpleTwo",
                fields=[
                    ("id", models.BigAutoField(primary_key=True)),
                    ("label", models.CharField(max_length=50)),
                ],
            ),
        ]

        executor = MigrationExecutor.__new__(MigrationExecutor)
        executor.connection = connection
        executor.progress_callback = None
        ddl_count_at_record = []

        def fake_record(*args):
            # Django 5.2 passes (migration,); Django 6.0 passes (app_label, name).
            app_label = args[0].app_label if len(args) == 1 else args[0]
            mig_name = args[0].name if len(args) == 1 else args[1]
            # Simulate MigrationRecorder.record_applied issuing DML via cursor
            # inside the open SchemaEditor block (when deferred_sql is empty).
            add_update_count(
                "INSERT INTO django_migrations (app, name) VALUES (@a0, @a1)", 1
            )
            with connection.cursor() as cur:
                cur.execute(
                    "INSERT INTO django_migrations (app, name) VALUES (%s, %s)",
                    [app_label, mig_name],
                )
            ddl_count_at_record.append(len(self._ddl_batches()))

        executor.record_migration = fake_record
        with self._auto_batch_ddl(True):
            executor.apply_migration(ProjectState(), mig)

        # Both CREATE TABLEs flushed in 1 batch BEFORE django_migrations INSERT!
        self.assertEqual(ddl_count_at_record, [1])
        self.assertEqual(len(self._ddl_batches()), 1)
        self.assertEqual(len(self._ddl_batches()[0]), 2)

    def test_apply_migration_ddl_failure_prevents_recording_migration(self):
        self.database_admin_service.add_error(
            grpc.StatusCode.FAILED_PRECONDITION,
            "Duplicate column or precondition failed",
        )
        mig = migrations.Migration("0001_fail", "fail_app")
        mig.operations = [
            migrations.CreateModel(
                name="Broken",
                fields=[("id", models.BigAutoField(primary_key=True))],
            ),
        ]
        executor = MigrationExecutor.__new__(MigrationExecutor)
        executor.connection = connection
        executor.progress_callback = None
        recorded = []

        def fake_record(*args):
            app_label = args[0].app_label if len(args) == 1 else args[0]
            mig_name = args[0].name if len(args) == 1 else args[1]
            with connection.cursor() as cur:
                cur.execute(
                    "INSERT INTO django_migrations (app, name) VALUES (%s, %s)",
                    [app_label, mig_name],
                )
            recorded.append(mig_name)

        executor.record_migration = fake_record
        with self._auto_batch_ddl(True):
            with self.assertRaises(IntegrityError):
                executor.apply_migration(ProjectState(), mig)

            # DDL batch flushed before INSERT, raised IntegrityError, never recorded!
            self.assertEqual(recorded, [])
            self.assertFalse(connection.in_ddl_batch)
            self.assertEqual(connection.buffered_ddl_statements, ())

            # Subsequent DDL on the same connection succeeds cleanly with zero stale leak.
            with connection.schema_editor() as editor:
                editor.execute(
                    "CREATE TABLE clean_after_err (id INT64) PRIMARY KEY (id)"
                )
        batches = self._ddl_batches()
        self.assertEqual(len(batches), 2)
        self.assertEqual(
            batches[1], ["CREATE TABLE clean_after_err (id INT64) PRIMARY KEY (id)"]
        )

    def test_delete_model_remove_field_and_alter_field_batch_index_drops(self):
        state = ProjectState()
        create_mig = migrations.Migration("0001_init", "edit_app")
        create_mig.operations = [
            migrations.CreateModel(
                name="Article",
                fields=[
                    ("id", models.BigAutoField(primary_key=True)),
                    ("title", models.CharField(max_length=100, db_index=True)),
                    ("code", models.CharField(max_length=40, db_index=True)),
                ],
            )
        ]
        state = create_mig.mutate_state(state, preserve=True)

        with self._auto_batch_ddl(True):
            # 1. AlterField changing nullability of indexed column drops index,
            # alters column, and recreates index in ONE UpdateDatabaseDdl RPC.
            alter_mig = migrations.Migration("0002_alter", "edit_app")
            alter_mig.operations = [
                migrations.AlterField(
                    model_name="article",
                    name="title",
                    field=models.CharField(max_length=100, null=True, db_index=True),
                )
            ]
            with mock.patch.object(
                connection.SchemaEditorClass,
                "_constraint_names",
                return_value=["article_title_idx"],
            ):
                with connection.schema_editor() as editor:
                    state = alter_mig.apply(state, editor)

            self.assertEqual(len(self._ddl_batches()), 1)
            self.assertEqual(len(self._ddl_batches()[0]), 3)
            self.assertTrue(self._ddl_batches()[0][0].startswith("DROP INDEX"))
            self.assertTrue(self._ddl_batches()[0][1].startswith("ALTER TABLE"))
            self.assertTrue(self._ddl_batches()[0][2].startswith("CREATE INDEX"))

            # 2. RemoveField with index drops index + column in ONE RPC.
            self.database_admin_service.clear_requests()
            rem_mig = migrations.Migration("0003_rem", "edit_app")
            rem_mig.operations = [
                migrations.RemoveField(model_name="article", name="code"),
            ]
            with mock.patch.object(
                connection.SchemaEditorClass,
                "_constraint_names",
                side_effect=[["article_code_idx"], []],
            ):
                with connection.schema_editor() as editor:
                    state = rem_mig.apply(state, editor)

            self.assertEqual(len(self._ddl_batches()), 1)
            self.assertEqual(
                self._ddl_batches()[0],
                [
                    "DROP INDEX article_code_idx",
                    "ALTER TABLE edit_app_article DROP COLUMN code",
                ],
            )

            # 3. DeleteModel with multiple indexes drops all indexes + table in ONE RPC.
            self.database_admin_service.clear_requests()
            del_mig = migrations.Migration("0004_del", "edit_app")
            del_mig.operations = [migrations.DeleteModel(name="Article")]
            with mock.patch.object(
                connection.SchemaEditorClass,
                "_constraint_names",
                return_value=["idx_a", "idx_b"],
            ):
                with connection.schema_editor() as editor:
                    del_mig.apply(state, editor)

            self.assertEqual(len(self._ddl_batches()), 1)
            self.assertEqual(
                self._ddl_batches()[0],
                [
                    "DROP INDEX idx_a",
                    "DROP INDEX idx_b",
                    "DROP TABLE edit_app_article",
                ],
            )

    def test_add_field_with_default_flushes_before_update_and_batches_rest(self):
        state = ProjectState()
        init_mig = migrations.Migration("0001_init", "def_app")
        init_mig.operations = [
            migrations.CreateModel(
                name="Member",
                fields=[("id", models.BigAutoField(primary_key=True))],
            )
        ]
        state = init_mig.mutate_state(state, preserve=True)

        add_update_count("UPDATE def_app_member SET score=@a0 WHERE 1=1", 2)
        # Note: SchemaEditor.add_field emits "UPDATE <table> SET <col>=%s"
        add_update_count("UPDATE def_app_member SET score=@a0", 2)

        mig = migrations.Migration("0002_add_score", "def_app")
        mig.operations = [
            migrations.AddField(
                model_name="member",
                name="score",
                field=models.IntegerField(default=10, db_index=True),
            ),
            migrations.AddField(
                model_name="member",
                name="nickname",
                field=models.CharField(max_length=30, null=True, unique=True),
            ),
        ]
        with self._auto_batch_ddl(True):
            with connection.schema_editor() as editor:
                mig.apply(state, editor)

        batches = self._ddl_batches()
        # Batch 1: ADD COLUMN score (flushed automatically before UPDATE DML).
        # Batch 2: ALTER COLUMN score NOT NULL + ADD COLUMN nickname +
        #          CREATE INDEX score + CREATE UNIQUE INDEX nickname!
        self.assertEqual(len(batches), 2)
        self.assertEqual(len(batches[0]), 1)
        self.assertIn("ADD COLUMN score INT64", batches[0][0])
        self.assertEqual(len(batches[1]), 4)
        self.assertIn("ALTER COLUMN score INT64 NOT NULL", batches[1][0])
        self.assertIn("ADD COLUMN nickname STRING(30)", batches[1][1])

    def test_runpython_atomic_and_introspection_flush_prior_ddl(self):
        batches_seen_in_python = []
        add_select1_result()

        def forward_fn(apps, schema_editor):
            # Entering RunPython (with atomic=True on Migration) has ALREADY
            # flushed CREATE TABLE prior to BEGIN!
            batches_seen_in_python.append(len(self._ddl_batches()))
            with schema_editor.connection.cursor() as cur:
                cur.execute("select 1")
                cur.fetchall()

        mig = migrations.Migration("0001_rp", "rp_app")
        mig.operations = [
            migrations.CreateModel(
                name="StageOne",
                fields=[("id", models.BigAutoField(primary_key=True))],
            ),
            migrations.RunPython(forward_fn),
            migrations.CreateModel(
                name="StageTwo",
                fields=[
                    ("id", models.BigAutoField(primary_key=True)),
                    ("code", models.CharField(max_length=20, db_index=True)),
                ],
            ),
        ]
        with self._auto_batch_ddl(True):
            with connection.schema_editor(atomic=mig.atomic) as editor:
                mig.apply(ProjectState(), editor)

        self.assertEqual(batches_seen_in_python, [1])
        batches = self._ddl_batches()
        self.assertEqual(len(batches), 2)
        self.assertEqual(len(batches[0]), 1)  # StageOne CREATE TABLE
        self.assertEqual(len(batches[1]), 2)  # StageTwo CREATE TABLE + index

        # Also verify cursor.run_sql_in_snapshot / list_tables auto-flushes buffered DDL.
        self.database_admin_service.clear_requests()
        _add_empty_result("SELECT table_name FROM information_schema.tables")
        with connection.ddl_batch():
            with connection.cursor() as cur:
                cur.execute("CREATE TABLE snap_t (id INT64) PRIMARY KEY (id)")
                self.assertEqual(len(self._ddl_batches()), 0)
                cur.run_sql_in_snapshot(
                    "SELECT table_name FROM information_schema.tables"
                )
                self.assertEqual(len(self._ddl_batches()), 1)

    def test_runsql_comments_multi_statement_and_parameterized_ddl(self):
        mig = migrations.Migration("0001_sql", "sql_app")
        mig.operations = [
            migrations.RunSQL(
                """
                -- Create two tables in a raw SQL script
                CREATE TABLE raw_a (id INT64 NOT NULL) PRIMARY KEY (id);
                /* second table */
                CREATE TABLE raw_b (id INT64 NOT NULL, a_id INT64) PRIMARY KEY (id);
                -- trailing comment only
                """
            ),
            migrations.RunSQL(
                [
                    (
                        "ALTER TABLE raw_a ADD COLUMN label STRING(50) DEFAULT (%s)",
                        ["it's \\ ok"],
                    )
                ]
            ),
        ]
        with self._auto_batch_ddl(True):
            with connection.schema_editor() as editor:
                mig.apply(ProjectState(), editor)

        self.assertEqual(
            self._ddl_batches(),
            [
                [
                    "CREATE TABLE raw_a (id INT64 NOT NULL) PRIMARY KEY (id)",
                    "CREATE TABLE raw_b (id INT64 NOT NULL, a_id INT64) PRIMARY KEY (id)",
                    r"ALTER TABLE raw_a ADD COLUMN label STRING(50) DEFAULT ('it\'s \\ ok')",
                ]
            ],
        )

    def test_explicit_ddl_batch_groups_multiple_schema_editors_and_rollbacks(self):
        # 1. Explicit ddl_batch() remains active under default AUTO_BATCH_DDL=False,
        # grouping multiple schema_editor() contexts with nested checkpoint rollback.
        self.assertFalse(connection.auto_batch_ddl)
        with connection.ddl_batch():
            with connection.schema_editor() as ed1:
                ed1.execute("CREATE TABLE outer_1 (id INT64) PRIMARY KEY (id)")
            try:
                with connection.schema_editor() as ed_fail:
                    ed_fail.execute(
                        "CREATE TABLE discarded_inner (id INT64) PRIMARY KEY (id)"
                    )
                    raise RuntimeError("abort inner editor only")
            except RuntimeError:
                pass
            with connection.ddl_batch():
                with connection.schema_editor() as ed2:
                    ed2.execute("CREATE TABLE outer_2 (id INT64) PRIMARY KEY (id)")
            self.assertEqual(len(self._ddl_batches()), 0)

        self.assertEqual(
            self._ddl_batches(),
            [
                [
                    "CREATE TABLE outer_1 (id INT64) PRIMARY KEY (id)",
                    "CREATE TABLE outer_2 (id INT64) PRIMARY KEY (id)",
                ]
            ],
        )

        # 2. Uncaught exception inside auto-batched schema_editor() or explicit ddl_batch() sends 0 RPCs.
        self.database_admin_service.clear_requests()
        with self._auto_batch_ddl(True):
            with self.assertRaises(ValueError):
                with connection.schema_editor() as editor:
                    editor.execute(
                        "CREATE TABLE never_sent (id INT64) PRIMARY KEY (id)"
                    )
                    raise ValueError("boom")
            self.assertEqual(self._ddl_batches(), [])
            self.assertFalse(connection.in_ddl_batch)

            # 3. Invalid deferred_sql failing inside SchemaEditor.__exit__ aborts owned batch.
            with self.assertRaises(ProgrammingError):
                with connection.schema_editor() as editor:
                    editor.execute(
                        "CREATE TABLE never_sent_3 (id INT64) PRIMARY KEY (id)"
                    )
                    editor.deferred_sql.append(";")
            self.assertEqual(self._ddl_batches(), [])
            self.assertFalse(connection.in_ddl_batch)

            # Empty auto-batched schema_editor() sends 0 RPCs.
            with connection.schema_editor():
                pass
            self.assertEqual(self._ddl_batches(), [])

        with self.assertRaises(ValueError):
            with connection.ddl_batch():
                with connection.cursor() as cur:
                    cur.execute("CREATE TABLE never_sent_2 (id INT64) PRIMARY KEY (id)")
                raise ValueError("boom outer")
        self.assertEqual(self._ddl_batches(), [])
        self.assertFalse(connection.in_ddl_batch)

        # 4. Empty ddl_batch() and default schema_editor() send 0 RPCs.
        with connection.ddl_batch():
            pass
        with connection.schema_editor():
            pass
        self.assertEqual(self._ddl_batches(), [])

        # 5. ddl_batch() inside transaction.atomic() raises ProgrammingError.
        with transaction.atomic():
            with self.assertRaises(ProgrammingError):
                with connection.ddl_batch():
                    pass

    def test_client_side_start_run_abort_batch_ddl_and_negative_cases(self):
        add_select1_result()
        with connection.cursor() as cur:
            # First run a DQL query on the same cursor to verify buffered DDL
            # resets cursor description/rowcount cleanly.
            cur.execute("select 1")
            self.assertIsNotNone(cur.description)

            cur.execute("/* header */ START BATCH DDL;")
            self.assertTrue(connection.in_ddl_batch)
            self.assertFalse(connection.ddl_batch_auto_flush)
            self.assertIsNone(cur.description)

            cur.execute(
                "CREATE TABLE cs_1 (id INT64) PRIMARY KEY (id); "
                "CREATE INDEX cs_1_idx ON cs_1 (id); -- comment"
            )
            cur.execute("ALTER TABLE cs_1 ADD COLUMN name STRING(50)")
            self.assertEqual(len(self._ddl_batches()), 0)

            # Strict mode rejects DQL, DML, nested START BATCH DDL, START BATCH DML,
            # empty/invalid SQL, parameterized batch control, and executemany
            # without dropping already-queued valid DDL statements!
            for bad_sql in (
                "SELECT 1",
                "INSERT INTO cs_1 (id) VALUES (1)",
                "START BATCH DDL",
                "START BATCH DML",
                "",
                "   ; ; ",
                "-- comment only",
                "CREATE TABLE a (id INT64) PRIMARY KEY (id); SELECT 1",
            ):
                with self.assertRaises(ProgrammingError):
                    cur.execute(bad_sql)
            with self.assertRaises(ProgrammingError):
                cur.execute("RUN BATCH", [1])
            with self.assertRaises(ProgrammingError):
                cur.execute("ABORT BATCH", [1])
            with self.assertRaises(ProgrammingError):
                cur.executemany("INSERT INTO cs_1 (id) VALUES (%s)", [(1,), (2,)])
            with self.assertRaises(ProgrammingError):
                cur.run_sql_in_snapshot("SELECT 1")
            with self.assertRaises(ProgrammingError):
                cur.list_tables()

            # Valid queued DDL executes atomically on RUN BATCH.
            cur.execute("run batch")
            self.assertFalse(connection.in_ddl_batch)

        self.assertEqual(
            self._ddl_batches(),
            [
                [
                    "CREATE TABLE cs_1 (id INT64) PRIMARY KEY (id)",
                    "CREATE INDEX cs_1_idx ON cs_1 (id)",
                    "ALTER TABLE cs_1 ADD COLUMN name STRING(50)",
                ]
            ],
        )

        # ABORT BATCH discards buffered statements with 0 RPCs.
        self.database_admin_service.clear_requests()
        with connection.cursor() as cur:
            with self.assertRaises(ProgrammingError):
                cur.execute("START BATCH DDL", [1])
            cur.execute("START BATCH DDL")
            cur.execute("CREATE TABLE discarded_cs (id INT64) PRIMARY KEY (id)")
            cur.execute("ABORT BATCH;")
            self.assertFalse(connection.in_ddl_batch)
            # RUN / ABORT when no batch is active raises ProgrammingError.
            with self.assertRaises(ProgrammingError):
                cur.execute("RUN BATCH")
            with self.assertRaises(ProgrammingError):
                cur.execute("ABORT BATCH")
        self.assertEqual(self._ddl_batches(), [])

        # Closed cursor raises InterfaceError even for START BATCH DDL / DDL batch.
        closed_cur = connection.create_cursor()
        closed_cur.close()
        with self.assertRaises(InterfaceError):
            closed_cur.execute("START BATCH DDL")

        # Server gRPC INVALID_ARGUMENT and INTERNAL map to ProgrammingError and OperationalError.
        self.database_admin_service.add_error(
            grpc.StatusCode.INVALID_ARGUMENT, "Syntax error in DDL"
        )
        with self.assertRaises(ProgrammingError):
            with connection.ddl_batch():
                with connection.cursor() as cur:
                    cur.execute("CREATE TABLE bad_syn (id INT64) PRIMARY KEY (id)")

        self.database_admin_service.add_error(
            grpc.StatusCode.INTERNAL, "Internal DDL error"
        )
        with self.assertRaises(OperationalError):
            with connection.ddl_batch():
                with connection.cursor() as cur:
                    cur.execute("CREATE TABLE int_err (id INT64) PRIMARY KEY (id)")

    def test_close_discards_unflushed_ddl_and_mixed_multistatement_auto_flush(self):
        add_update_count("INSERT INTO mix_t (id) VALUES (1)", 1)
        connection.start_batch_ddl()
        with connection.cursor() as cur:
            cur.execute("CREATE TABLE drop_on_close (id INT64) PRIMARY KEY (id)")
        with self.assertLogs("django_spanner.base", level="WARNING") as cm:
            connection.close()
        self.assertEqual(len(cm.output), 1)
        self.assertIn("1 un-flushed Cloud Spanner DDL statement(s)", cm.output[0])
        self.assertFalse(connection.in_ddl_batch)
        self.assertEqual(connection.buffered_ddl_statements, ())
        self.assertEqual(self._ddl_batches(), [])

        # Reconnects cleanly and handles mixed multi-statement DDL + DML in auto_flush mode.
        with connection.ddl_batch(auto_flush=True):
            with connection.cursor() as cur:
                cur.execute(
                    "CREATE TABLE mix_t (id INT64) PRIMARY KEY (id); "
                    "INSERT INTO mix_t (id) VALUES (1); "
                    "CREATE INDEX mix_idx ON mix_t (id)"
                )
        self.assertEqual(
            self._ddl_batches(),
            [
                ["CREATE TABLE mix_t (id INT64) PRIMARY KEY (id)"],
                ["CREATE INDEX mix_idx ON mix_t (id)"],
            ],
        )

    def test_concurrent_connections_batch_ddl_independently(self):
        barrier = threading.Barrier(2, timeout=10)
        errors = []

        def make_wrapper(alias):
            from google.cloud.spanner_v1 import PingingPool

            cfg = dict(connection.settings_dict)
            cfg["OPTIONS"] = dict(connection.settings_dict["OPTIONS"])
            # Each DatabaseWrapper receives its own session pool because
            # spanner_v1 PingingPool binds strictly to a single Database object.
            cfg["OPTIONS"]["pool"] = PingingPool(size=5)
            return DatabaseWrapper(cfg, alias=alias)

        def worker_commit():
            conn_a = make_wrapper("worker_a")
            try:
                with conn_a.ddl_batch():
                    with conn_a.cursor() as cur:
                        cur.execute(
                            "CREATE TABLE thread_a1 (id INT64) PRIMARY KEY (id)"
                        )
                        barrier.wait()
                        cur.execute(
                            "CREATE TABLE thread_a2 (id INT64) PRIMARY KEY (id)"
                        )
            except Exception as exc:
                errors.append(exc)
            finally:
                conn_a.close()

        def worker_abort_then_commit():
            conn_b = make_wrapper("worker_b")
            try:
                conn_b.start_batch_ddl()
                with conn_b.cursor() as cur:
                    cur.execute(
                        "CREATE TABLE thread_b_aborted (id INT64) PRIMARY KEY (id)"
                    )
                    barrier.wait()
                conn_b.abort_batch()
                with conn_b.ddl_batch():
                    with conn_b.cursor() as cur:
                        cur.execute(
                            "CREATE TABLE thread_b_kept (id INT64) PRIMARY KEY (id)"
                        )
            except Exception as exc:
                errors.append(exc)
            finally:
                conn_b.close()

        t1 = threading.Thread(target=worker_commit)
        t2 = threading.Thread(target=worker_abort_then_commit)
        t1.start()
        t2.start()
        t1.join(timeout=15)
        t2.join(timeout=15)

        self.assertEqual(errors, [])
        batches = sorted(self._ddl_batches())
        self.assertEqual(
            batches,
            [
                [
                    "CREATE TABLE thread_a1 (id INT64) PRIMARY KEY (id)",
                    "CREATE TABLE thread_a2 (id INT64) PRIMARY KEY (id)",
                ],
                ["CREATE TABLE thread_b_kept (id INT64) PRIMARY KEY (id)"],
            ],
        )
