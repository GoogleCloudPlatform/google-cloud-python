# Copyright 2025 Google LLC All rights reserved.
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
import datetime
import uuid
from decimal import Decimal
from unittest import mock

import django
import google.cloud.spanner_v1.types.result_set as result_set
import google.cloud.spanner_v1.types.type as spanner_type
from django.core.management.commands.migrate import Command as MigrateCommand
from django.db import connection, models, transaction
from django.db.migrations.migration import Migration
from django.db.migrations.operations.models import CreateModel
from django.db.migrations.operations.special import RunPython
from django.db.migrations.state import ProjectState
from google.cloud.spanner_v1 import (
    BatchCreateSessionsRequest,
    CommitRequest,
    CreateSessionRequest,
    ExecuteSqlRequest,
    RollbackRequest,
    TypeCode,
)

from tests.mockserver_tests.mock_server_test_base import (
    MockServerTestBase,
    add_result,
    add_select1_result,
    add_singer_query_result,
    add_single_result,
    add_update_count,
)
from tests.mockserver_tests.models import Detail, Singer
from tests.settings import DATABASES


class TestBasics(MockServerTestBase):
    def verify_select1(self, results):
        result_list = list(results)
        for row in result_list:
            self.assertEqual(row[0], 1)
        self.assertEqual(len(result_list), 1)
        requests = self.spanner_service.requests
        self.assertEqual(len(requests), 3)
        self.assertIsInstance(requests[0], BatchCreateSessionsRequest)
        self.assertIsInstance(requests[1], CreateSessionRequest)
        self.assertIsInstance(requests[2], ExecuteSqlRequest)

    def test_select1(self):
        add_select1_result()
        with self.database.snapshot() as snapshot:
            results = snapshot.execute_sql("select 1")
            self.verify_select1(results)

    def test_django_select1(self):
        add_select1_result()
        with connection.cursor() as cursor:
            cursor.execute("select 1")
            self.verify_select1(cursor.fetchall())

    def test_django_select_singer(self):
        add_singer_query_result(
            "SELECT tests_singer.id, tests_singer.first_name, tests_singer.last_name FROM tests_singer"
        )
        singers = Singer.objects.all()
        self.assertEqual(len(singers), 2)
        requests = self.spanner_service.requests
        self.assertEqual(len(requests), 3)
        self.assertIsInstance(requests[0], BatchCreateSessionsRequest)
        self.assertIsInstance(requests[1], CreateSessionRequest)
        self.assertIsInstance(requests[2], ExecuteSqlRequest)

    def test_django_select_singer_using_other_db(self):
        add_singer_query_result(
            "SELECT tests_singer.id, tests_singer.first_name, tests_singer.last_name FROM tests_singer"
        )
        singers = Singer.objects.using("secondary").all()
        self.assertEqual(len(singers), 2)
        requests = self.spanner_service.requests
        self.assertEqual(len(requests), 3)
        self.assertIsInstance(requests[0], BatchCreateSessionsRequest)
        self.assertIsInstance(requests[1], CreateSessionRequest)
        self.assertIsInstance(requests[2], ExecuteSqlRequest)

    def test_insert_singer(self):
        add_single_result(
            "INSERT INTO tests_singer "
            "(id, first_name, last_name) "
            "VALUES (@a0, @a1, @a2) "
            "THEN RETURN id",
            "id",
            TypeCode.INT64,
            [("1",)],
        )
        singer = Singer(first_name="test", last_name="test")
        singer.save()
        requests = self.spanner_service.requests
        self.assertEqual(len(requests), 4)
        self.assertIsInstance(requests[0], BatchCreateSessionsRequest)
        self.assertIsInstance(requests[1], CreateSessionRequest)
        self.assertIsInstance(requests[2], ExecuteSqlRequest)
        self.assertIsInstance(requests[3], CommitRequest)
        # The ExecuteSqlRequest should have 3 parameters:
        # 1. first_name
        # 2. last_name
        # 3. client-side auto-generated primary key
        self.assertEqual(len(requests[2].params), 3)

    def test_insert_singer_with_disabled_random_primary_key(self):
        for db, config in DATABASES.items():
            if config["ENGINE"] == "django_spanner":
                config["RANDOM_ID_GENERATION_ENABLED"] = "false"

        # Define a class locally in this test method to ensure that
        # it is initialized after disabling random ID generation.
        class LocalSinger(models.Model):
            first_name = models.CharField(max_length=200)
            last_name = models.CharField(max_length=200)

        try:
            add_single_result(
                "INSERT INTO tests_localsinger "
                "(first_name, last_name) "
                "VALUES (@a0, @a1) "
                "THEN RETURN id",
                "id",
                TypeCode.INT64,
                [("1",)],
            )
            singer = LocalSinger(first_name="test", last_name="test")
            singer.save()
            requests = self.spanner_service.requests
            self.assertEqual(len(requests), 4)
            self.assertIsInstance(requests[0], BatchCreateSessionsRequest)
            self.assertIsInstance(requests[1], CreateSessionRequest)
            self.assertIsInstance(requests[2], ExecuteSqlRequest)
            self.assertIsInstance(requests[3], CommitRequest)
            # The ExecuteSqlRequest should have 2 parameters:
            # 1. first_name
            # 2. last_name
            # There should be no client-side auto-generated primary key.
            self.assertEqual(len(requests[2].params), 2)
        finally:
            for db, config in DATABASES.items():
                if config["ENGINE"] == "django_spanner":
                    config.pop("DISABLE_RANDOM_ID_GENERATION", None)

    def test_update_all_without_dbapi_intervention(self):
        """Verify Django generates WHERE 1=1 even when DB-API injection is disabled."""
        with mock.patch(
            "google.cloud.spanner_dbapi.parse_utils.ensure_where_clause",
            side_effect=lambda sql: sql,
        ):
            add_update_count("UPDATE tests_singer SET last_name = @a0 WHERE 1=1", 1)
            Singer.objects.all().update(last_name="Test")

            requests = [
                request
                for request in self.spanner_service.requests
                if isinstance(request, ExecuteSqlRequest)
            ]
            self.assertEqual(len(requests), 1)
            self.assertEqual(
                requests[0].sql,
                "UPDATE tests_singer SET last_name = @a0 WHERE 1=1",
            )

    def test_delete_all_without_dbapi_intervention(self):
        """Verify Django generates WHERE 1=1 even when DB-API injection is disabled."""
        with mock.patch(
            "google.cloud.spanner_dbapi.parse_utils.ensure_where_clause",
            side_effect=lambda sql: sql,
        ):
            add_update_count("DELETE FROM tests_singer WHERE 1=1", 1)
            Singer.objects.all().delete()

            requests = [
                request
                for request in self.spanner_service.requests
                if isinstance(request, ExecuteSqlRequest)
            ]
            self.assertEqual(len(requests), 1)
            self.assertEqual(
                requests[0].sql,
                "DELETE FROM tests_singer WHERE 1=1",
            )

    def _make_detail_result_set(self, rows):
        select_result = result_set.ResultSet(
            dict(
                metadata=result_set.ResultSetMetadata(
                    dict(
                        row_type=spanner_type.StructType(
                            dict(
                                fields=[
                                    spanner_type.StructType.Field(
                                        dict(
                                            name="id",
                                            type=spanner_type.Type(
                                                dict(code=TypeCode.INT64)
                                            ),
                                        )
                                    ),
                                    spanner_type.StructType.Field(
                                        dict(
                                            name="value",
                                            type=spanner_type.Type(
                                                dict(code=TypeCode.JSON)
                                            ),
                                        )
                                    ),
                                ]
                            )
                        )
                    )
                ),
            )
        )
        select_result.rows.extend(rows)
        return select_result

    def test_insert_and_fetch_json_field(self):
        add_single_result(
            "INSERT INTO tests_detail (id, value) VALUES (@a0, @a1) THEN RETURN id",
            "id",
            TypeCode.INT64,
            [("1",)],
        )
        add_result(
            "INSERT INTO tests_detail (id, value) VALUES (@a0, @a1) THEN RETURN id, value",
            self._make_detail_result_set([("1", "null")]),
        )
        add_single_result(
            "INSERT INTO tests_detail (id, value) VALUES (@a0, @a1), (@a2, @a3)",
            "id",
            TypeCode.INT64,
            [("10",), ("11",)],
        )
        add_single_result(
            "UPDATE tests_detail SET value = @a0 WHERE tests_detail.id = @a1",
            "id",
            TypeCode.INT64,
            [("1",)],
        )
        add_result(
            "SELECT tests_detail.id, tests_detail.value FROM tests_detail",
            self._make_detail_result_set(
                [
                    ("1", '{"age": "26", "name": "Jakob"}'),
                    ("2", "[1, 2, 3]"),
                    ("3", None),
                    ("4", '"hello"'),
                    ("5", "42"),
                    ("6", "true"),
                    ("7", "3.14"),
                    ("8", "null"),
                ]
            ),
        )
        add_result(
            "SELECT tests_detail.id, tests_detail.value FROM tests_detail WHERE JSON_QUERY(tests_detail.value, '$.\"name\"') = @a0",
            self._make_detail_result_set([("1", '{"age": "26", "name": "Jakob"}')]),
        )
        add_result(
            "SELECT tests_detail.id, tests_detail.value FROM tests_detail WHERE JSON_QUERY(tests_detail.value, '$.\"name\"') IS NOT NULL",
            self._make_detail_result_set([("1", '{"age": "26", "name": "Jakob"}')]),
        )
        add_result(
            "SELECT tests_detail.id, tests_detail.value FROM tests_detail WHERE tests_detail.value = @a0",
            self._make_detail_result_set([("8", "null")]),
        )
        add_result(
            "SELECT tests_detail.id, tests_detail.value FROM tests_detail WHERE tests_detail.value IS NULL",
            self._make_detail_result_set([("3", None)]),
        )

        # 1. Dict insert
        detail = Detail(value={"name": "Jakob", "age": "26"})
        detail.save()
        self.assertEqual(1, detail.id)

        # 2. SQL NULL insert
        detail_sql_null = Detail(value=None)
        detail_sql_null.save()

        # 3. JSON null insert via Value(None, JSONField())
        detail_json_null = Detail(value=models.Value(None, models.JSONField()))
        detail_json_null.save()

        # 4. Primitives insert (str, int, bool, float)
        for primitive in ("hello", 42, True, 3.14):
            Detail(value=primitive).save()

        # 5. Custom encoder (DjangoJSONEncoder) insert with UUID, Decimal, date
        custom_uuid = uuid.UUID("12345678-1234-5678-1234-567812345678")
        Detail(
            value={
                "uuid": custom_uuid,
                "amount": Decimal("19.99"),
                "date": datetime.date(2026, 4, 8),
            }
        ).save()

        # 6. bulk_create and QuerySet.update
        Detail.objects.bulk_create(
            [
                Detail(id=10, value={"bulk": 1}),
                Detail(id=11, value=None),
            ]
        )
        Detail.objects.filter(id=1).update(value={"name": "Updated"})

        # 7. Fetch all (dict, list, SQL NULL, primitives, JSON null)
        details = list(Detail.objects.all())
        self.assertEqual(len(details), 8)
        self.assertEqual(details[0].value, {"name": "Jakob", "age": "26"})
        self.assertIs(type(details[0].value), dict)
        self.assertEqual(details[1].value, [1, 2, 3])
        self.assertIs(type(details[1].value), list)
        self.assertIsNone(details[2].value)
        self.assertEqual(details[3].value, "hello")
        self.assertEqual(details[4].value, 42)
        self.assertIs(details[5].value, True)
        self.assertEqual(details[6].value, 3.14)
        self.assertIsNone(details[7].value)

        # 8. Filter by JSON key, has_key, JSON null (Value(None, JSONField()) & None), and SQL NULL (value__isnull=True)
        by_key = list(Detail.objects.filter(value__name="Jakob"))
        self.assertEqual(len(by_key), 1)
        self.assertEqual(by_key[0].value, {"name": "Jakob", "age": "26"})

        by_has_key = list(Detail.objects.filter(value__has_key="name"))
        self.assertEqual(len(by_has_key), 1)

        by_json_null_expr = list(
            Detail.objects.filter(value=models.Value(None, models.JSONField()))
        )
        self.assertEqual(len(by_json_null_expr), 1)
        self.assertIsNone(by_json_null_expr[0].value)

        by_json_null_direct = list(Detail.objects.filter(value=None))
        self.assertEqual(len(by_json_null_direct), 1)
        self.assertIsNone(by_json_null_direct[0].value)

        by_sql_null = list(Detail.objects.filter(value__isnull=True))
        self.assertEqual(len(by_sql_null), 1)
        self.assertIsNone(by_sql_null[0].value)

        exec_requests = [
            req
            for req in self.spanner_service.requests
            if isinstance(req, ExecuteSqlRequest)
        ]

        # Dict insert -> JSON string
        self.assertEqual(exec_requests[0].param_types["a1"].code, TypeCode.JSON)
        self.assertEqual(
            exec_requests[0].params["a1"],
            '{"name": "Jakob", "age": "26"}',
        )

        # SQL NULL insert -> None (NULL_VALUE in proto Struct)
        self.assertIsNone(exec_requests[1].params["a1"])

        # JSON null insert -> "null" with TypeCode.JSON
        self.assertEqual(exec_requests[2].param_types["a1"].code, TypeCode.JSON)
        self.assertEqual(exec_requests[2].params["a1"], "null")

        # Primitives insert
        self.assertEqual(exec_requests[3].params["a1"], '"hello"')
        self.assertEqual(exec_requests[4].params["a1"], "42")
        self.assertEqual(exec_requests[5].params["a1"], "true")
        self.assertEqual(exec_requests[6].params["a1"], "3.14")

        # Custom encoder insert
        self.assertEqual(
            exec_requests[7].params["a1"],
            '{"uuid": "12345678-1234-5678-1234-567812345678", "amount": "19.99", "date": "2026-04-08"}',
        )

        # bulk_create request
        self.assertEqual(exec_requests[8].params["a1"], '{"bulk": 1}')
        self.assertIsNone(exec_requests[8].params["a3"])

        # update request
        self.assertEqual(
            exec_requests[9].params["a0"],
            '{"name": "Updated"}',
        )

        # filter(value__name="Jakob") request (JSONPath is inlined as a literal, @a0 is JSON "Jakob")
        self.assertEqual(exec_requests[11].param_types["a0"].code, TypeCode.JSON)
        self.assertEqual(exec_requests[11].params["a0"], '"Jakob"')

        # filter(value=Value(None, JSONField())) request
        self.assertEqual(exec_requests[13].param_types["a0"].code, TypeCode.JSON)
        self.assertEqual(exec_requests[13].params["a0"], "null")

        # filter(value=None) request -> also queries JSON null ("null", TypeCode.JSON)
        self.assertEqual(exec_requests[14].param_types["a0"].code, TypeCode.JSON)
        self.assertEqual(exec_requests[14].params["a0"], "null")

    def test_sync_apps_batches_ddl_when_batch_ddl_option_enabled(self):
        cmd = MigrateCommand()
        cmd.verbosity = 0
        connection.close()
        connection.settings_dict["OPTIONS"]["batch_ddl"] = True
        try:
            with mock.patch.object(
                connection.introspection, "table_names", return_value=[]
            ):
                cmd.sync_apps(connection, ["auth", "contenttypes", "sessions", "sites"])
            self.assertNotIn("batch_ddl", connection.connection._connection_variables)
        finally:
            connection.settings_dict["OPTIONS"].pop("batch_ddl", None)

        ddl_requests = self.database_admin_service.requests
        self.assertEqual(len(ddl_requests), 1)
        self.assertEqual(len(ddl_requests[0].statements), 32)
        self.assertTrue(transaction.get_autocommit())
        self.assertTrue(connection.connection.autocommit)

    def test_default_schema_editor_executes_ddl_per_statement(self):
        class LocalAuthor(models.Model):
            name = models.CharField(max_length=100, unique=True)

            class Meta:
                app_label = "tests"

        with connection.schema_editor() as editor:
            editor.create_model(LocalAuthor)

        # Without OPTIONS["batch_ddl"], CREATE TABLE and CREATE UNIQUE INDEX
        # execute as 2 separate UpdateDatabaseDdlRequest calls.
        ddl_requests = self.database_admin_service.requests
        self.assertEqual(len(ddl_requests), 2)
        self.assertTrue(transaction.get_autocommit())

    def test_migration_with_runpython_and_deferred_sql_with_batch_ddl_option(self):
        add_select1_result()

        def run_query(apps, schema_editor):
            with schema_editor.connection.cursor() as cursor:
                cursor.execute("select 1")

        mig = Migration("0001_batch_runpython", "tests")
        mig.operations = [
            CreateModel(
                name="BatchModelOne",
                fields=[
                    ("id", models.BigAutoField(primary_key=True)),
                    ("code", models.CharField(max_length=50, unique=True)),
                ],
            ),
            RunPython(run_query),
            CreateModel(
                name="BatchModelTwo",
                fields=[
                    ("id", models.BigAutoField(primary_key=True)),
                    ("title", models.CharField(max_length=50, unique=True)),
                ],
            ),
        ]
        state = ProjectState()

        connection.settings_dict["OPTIONS"]["batch_ddl"] = True
        try:
            with connection.schema_editor(atomic=mig.atomic) as editor:
                mig.apply(state, editor)
        finally:
            connection.settings_dict["OPTIONS"].pop("batch_ddl", None)

        ddl_requests = self.database_admin_service.requests
        self.assertEqual(len(ddl_requests), 2)
        self.assertEqual(len(ddl_requests[0].statements), 1)
        self.assertEqual(len(ddl_requests[1].statements), 3)
        self.assertTrue(
            any(isinstance(r, CommitRequest) for r in self.spanner_service.requests)
        )
        self.assertTrue(transaction.get_autocommit())

    def test_schema_editor_exception_discards_queued_ddl_when_batching(self):
        class BrokenModel(models.Model):
            name = models.CharField(max_length=100)

            class Meta:
                app_label = "tests"

        connection.settings_dict["OPTIONS"]["batch_ddl"] = True
        try:
            with self.assertRaises(RuntimeError):
                with connection.schema_editor() as editor:
                    editor.create_model(BrokenModel)
                    raise RuntimeError("abort schema block")
        finally:
            connection.settings_dict["OPTIONS"].pop("batch_ddl", None)

        self.assertEqual(len(self.database_admin_service.requests), 0)
        self.assertTrue(transaction.get_autocommit())
        self.assertTrue(connection.connection.autocommit)

    def test_create_test_db_end_to_end_batches_syncdb_ddls_when_batch_ddl_enabled(self):
        orig_name = connection.settings_dict["NAME"]
        connection.settings_dict["OPTIONS"]["batch_ddl"] = True

        def fake_migrate_syncdb(*args, **kwargs):
            cmd = MigrateCommand()
            cmd.verbosity = 0
            with mock.patch.object(
                connection.introspection, "table_names", return_value=[]
            ):
                cmd.sync_apps(connection, ["sites", "sessions"])

        def fake_call_command(name, *args, **kwargs):
            if name == "migrate":
                fake_migrate_syncdb(*args, **kwargs)

        try:
            with (
                mock.patch.object(
                    connection.creation,
                    "_create_test_db",
                    return_value="test_django_test_db",
                ),
                mock.patch(
                    "django.core.management.call_command",
                    side_effect=fake_call_command,
                ),
            ):
                create_kwargs = {"verbosity": 0, "autoclobber": True}
                if django.VERSION < (6, 0):
                    create_kwargs["serialize"] = False
                connection.creation.create_test_db(**create_kwargs)

            ddl_requests = self.database_admin_service.requests
            self.assertEqual(len(ddl_requests), 1)
            # sites (table + unique index) + sessions (table + expire_date index) = 4 DDLs
            self.assertEqual(len(ddl_requests[0].statements), 4)
            self.assertTrue(transaction.get_autocommit())
        finally:
            connection.settings_dict["OPTIONS"].pop("batch_ddl", None)
            connection.settings_dict["NAME"] = orig_name

    def test_schema_editor_deferred_sql_exception_discards_queued_ddl(self):
        connection.settings_dict["OPTIONS"]["batch_ddl"] = True
        try:
            with self.assertRaises(ValueError):
                with connection.schema_editor() as editor:
                    editor.create_model(Singer)
                    editor.deferred_sql.append(
                        "CREATE INDEX idx_s ON tests_singer (first_name); SELECT 1"
                    )
        finally:
            connection.settings_dict["OPTIONS"].pop("batch_ddl", None)

        self.assertEqual(len(self.database_admin_service.requests), 0)
        self.assertTrue(transaction.get_autocommit())
        self.assertTrue(connection.connection.autocommit)

    def test_schema_editor_server_side_ddl_error_restores_autocommit(self):
        from django.db import IntegrityError, ProgrammingError
        from google.api_core.exceptions import FailedPrecondition, InvalidArgument

        connection.ensure_connection()
        connection.settings_dict["OPTIONS"]["batch_ddl"] = True
        try:
            with mock.patch.object(
                connection.connection.database,
                "update_ddl",
                side_effect=InvalidArgument("400 Invalid DDL syntax"),
            ):
                with self.assertRaises(ProgrammingError):
                    with connection.schema_editor() as editor:
                        editor.create_model(Singer)

            self.assertTrue(transaction.get_autocommit())
            self.assertTrue(connection.connection.autocommit)

            with mock.patch.object(
                connection.connection.database,
                "update_ddl",
                side_effect=FailedPrecondition("400 Duplicate name in schema"),
            ):
                with self.assertRaises(IntegrityError):
                    with connection.schema_editor() as editor:
                        editor.create_model(Singer)
        finally:
            connection.settings_dict["OPTIONS"].pop("batch_ddl", None)

        self.assertTrue(transaction.get_autocommit())
        self.assertTrue(connection.connection.autocommit)

    def test_schema_editor_add_field_with_default_commits_rw_tx_before_alter_column(
        self,
    ):
        add_update_count("UPDATE tests_singer SET stage_name=@a0 WHERE 1=1", 2)
        field = models.CharField(max_length=100, default="anon")
        field.set_attributes_from_name("stage_name")

        event_log = []
        orig_update_ddl = self.database_admin_service.UpdateDatabaseDdl

        def logged_update_ddl(request, context):
            event_log.append(("ddl", list(request.statements)))
            return orig_update_ddl(request, context)

        connection.settings_dict["OPTIONS"]["batch_ddl"] = True
        try:
            with connection.schema_editor() as editor:
                editor.add_field(Singer, field)
                self.assertFalse(connection.connection._spanner_transaction_started)
        finally:
            connection.settings_dict["OPTIONS"].pop("batch_ddl", None)

        ddl_requests = self.database_admin_service.requests
        self.assertEqual(len(ddl_requests), 2)
        self.assertTrue(
            any(isinstance(r, CommitRequest) for r in self.spanner_service.requests)
        )
        self.assertTrue(transaction.get_autocommit())

    def test_schema_editor_atomic_false_skips_batch_ddl(self):
        class NonAtomicModel(models.Model):
            code = models.CharField(max_length=50, unique=True)

            class Meta:
                app_label = "tests"

        connection.settings_dict["OPTIONS"]["batch_ddl"] = True
        try:
            with connection.schema_editor(atomic=False) as editor:
                self.assertTrue(transaction.get_autocommit())
                editor.create_model(NonAtomicModel)
        finally:
            connection.settings_dict["OPTIONS"].pop("batch_ddl", None)

        self.assertEqual(len(self.database_admin_service.requests), 2)
        self.assertTrue(transaction.get_autocommit())

    def test_schema_editor_nested_atomic_integrity_error_rolls_back_and_recovers(self):
        import grpc
        from django.db import IntegrityError

        add_select1_result()
        failing_sql = "UPDATE tests_singer SET first_name=@a0 WHERE id=@a1"
        self.spanner_service.mock_spanner.add_error(
            failing_sql,
            grpc.StatusCode.ALREADY_EXISTS,
            "UNIQUE violation on index",
        )

        connection.settings_dict["OPTIONS"]["batch_ddl"] = True
        try:
            with connection.schema_editor():
                self.assertTrue(transaction.get_autocommit())
                with self.assertRaises(IntegrityError):
                    with transaction.atomic():
                        with connection.cursor() as cursor:
                            cursor.execute(
                                "UPDATE tests_singer SET first_name=%s WHERE id=%s",
                                ["dup", 1],
                            )
                self.assertFalse(connection.needs_rollback)
                with connection.cursor() as cursor:
                    cursor.execute("select 1")
                    self.assertEqual(cursor.fetchone()[0], 1)
        finally:
            self.spanner_service.mock_spanner.errors.pop(failing_sql.lower(), None)
            connection.settings_dict["OPTIONS"].pop("batch_ddl", None)

        self.assertTrue(
            any(isinstance(r, RollbackRequest) for r in self.spanner_service.requests)
        )
        self.assertTrue(transaction.get_autocommit())
        self.assertTrue(connection.connection.autocommit)

    def test_migration_create_model_then_runpython_flushes_ddl_before_atomic(self):
        add_update_count("UPDATE tests_singer SET first_name=@a0 WHERE id=@a1", 1)
        events = []

        def run_atomic_dml(apps, schema_editor):
            events.append(
                (
                    "runpython_state",
                    schema_editor.connection.in_atomic_block,
                    schema_editor.connection.commit_on_exit,
                    len(self.database_admin_service.requests),
                )
            )
            with schema_editor.connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE tests_singer SET first_name=%s WHERE id=%s",
                    ["updated", 1],
                )

        mig = Migration("0001_create_then_runpython", "tests")
        mig.operations = [
            CreateModel(
                name="BatchModelBeforeRunPython",
                fields=[
                    ("id", models.BigAutoField(primary_key=True)),
                    ("code", models.CharField(max_length=50, unique=True)),
                ],
            ),
            RunPython(run_atomic_dml),
        ]
        state = ProjectState()

        connection.settings_dict["OPTIONS"]["batch_ddl"] = True
        try:
            with connection.schema_editor(atomic=mig.atomic) as editor:
                mig.apply(state, editor)
        finally:
            connection.settings_dict["OPTIONS"].pop("batch_ddl", None)

        # CreateModel's CREATE TABLE was flushed before RunPython's atomic() block began,
        # and RunPython ran inside a real outermost atomic block (commit_on_exit=True).
        self.assertEqual(events, [("runpython_state", True, True, 1)])
        # Deferred CREATE UNIQUE INDEX flushed on schema_editor.__exit__.
        ddl_requests = self.database_admin_service.requests
        self.assertEqual(len(ddl_requests), 2)
        self.assertEqual(len(ddl_requests[0].statements), 1)
        self.assertEqual(len(ddl_requests[1].statements), 1)
        self.assertTrue(
            any(isinstance(r, CommitRequest) for r in self.spanner_service.requests)
        )
        self.assertTrue(transaction.get_autocommit())
        self.assertTrue(connection.connection.autocommit)
