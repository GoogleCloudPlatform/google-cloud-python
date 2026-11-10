# Copyright 2021 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd


from unittest import mock

from django.db import NotSupportedError, connection, connections
from django.db.models import Index
from django.db.models.fields import AutoField, IntegerField

from django_spanner import gen_rand_int64
from django_spanner.schema import DatabaseSchemaEditor
from tests._helpers import HAS_OPENTELEMETRY_INSTALLED
from tests.unit.django_spanner.simple_test import SpannerSimpleTestClass
from tests.unit.django_spanner.test__opentelemetry_tracing import (
    DATABASE_ID,
    INSTANCE_ID,
    PROJECT,
)

from .models import Author

BASE_ATTRIBUTES = {
    "db.type": "spanner",
    "db.engine": "django_spanner",
    "db.project": PROJECT,
    "db.instance": INSTANCE_ID,
    "db.name": DATABASE_ID,
}


class TestUtils(SpannerSimpleTestClass):
    def test_quote_value(self):
        """
        Tries quoting input value.
        """
        schema_editor = DatabaseSchemaEditor(self.connection)
        self.assertEqual(schema_editor.quote_value(value=1.1), "1.1")

    def test_skip_default(self):
        """
        Tries skipping default as Cloud spanner doesn't support it.
        """
        schema_editor = DatabaseSchemaEditor(self.connection)
        self.assertTrue(schema_editor.skip_default(field=None))

    def test_create_model(self):
        """
        Tries creating a model's table.
        """
        with DatabaseSchemaEditor(self.connection) as schema_editor:
            schema_editor.execute = mock.MagicMock()
            schema_editor.create_model(Author)

            schema_editor.execute.assert_called_once_with(
                "CREATE TABLE tests_author (id INT64 NOT NULL, name STRING(40) "
                + "NOT NULL, last_name STRING(40) NOT NULL, num INT64 NOT "
                + "NULL, created TIMESTAMP NOT NULL, modified TIMESTAMP) "
                + "PRIMARY KEY(id)",
                None,
            )
        if HAS_OPENTELEMETRY_INSTALLED:
            span_list = self.ot_exporter.get_finished_spans()
            self.assertEqual(len(span_list), 1)
            self.assertSpanAttributes(
                "CloudSpannerDjango.create_model",
                attributes=dict(BASE_ATTRIBUTES, model_name="tests_author"),
                span=span_list[0],
            )

    def test_delete_model(self):
        """
        Tests deleting a model
        """
        with DatabaseSchemaEditor(self.connection) as schema_editor:
            schema_editor.execute = mock.MagicMock()
            schema_editor._constraint_names = mock.MagicMock()
            schema_editor.delete_model(Author)

            schema_editor.execute.assert_called_once_with(
                "DROP TABLE tests_author",
            )

        if HAS_OPENTELEMETRY_INSTALLED:
            span_list = self.ot_exporter.get_finished_spans()
            self.assertEqual(len(span_list), 1)
            self.assertSpanAttributes(
                "CloudSpannerDjango.delete_model",
                attributes=dict(BASE_ATTRIBUTES, model_name="tests_author"),
                span=span_list[0],
            )

    def test_delete_model_with_index(self):
        """
        Tests deleting a model with index
        """
        with DatabaseSchemaEditor(self.connection) as schema_editor:
            schema_editor.execute = mock.MagicMock()

            def delete_index_sql(*args, **kwargs):
                # Overriding Statement creation with sql string.
                return "DROP INDEX num_unique"

            def constraint_names(*args, **kwargs):
                return ["num_unique"]

            schema_editor._delete_index_sql = delete_index_sql
            schema_editor._constraint_names = constraint_names
            schema_editor.delete_model(Author)

            calls = [
                mock.call("DROP INDEX num_unique"),
                mock.call("DROP TABLE tests_author"),
            ]

            schema_editor.execute.assert_has_calls(calls)

        if HAS_OPENTELEMETRY_INSTALLED:
            span_list = self.ot_exporter.get_finished_spans()
            self.assertEqual(len(span_list), 2)
            self.assertSpanAttributes(
                "CloudSpannerDjango.delete_model.delete_index",
                attributes=dict(
                    BASE_ATTRIBUTES,
                    model_name="tests_author",
                    index_name="num_unique",
                ),
                span=span_list[0],
            )
            self.assertSpanAttributes(
                "CloudSpannerDjango.delete_model",
                attributes=dict(
                    BASE_ATTRIBUTES,
                    model_name="tests_author",
                ),
                span=span_list[1],
            )

    def test_add_field(self):
        """
        Tests adding fields to models
        """
        with DatabaseSchemaEditor(self.connection) as schema_editor:
            schema_editor.execute = mock.MagicMock()
            new_field = IntegerField(null=True)
            new_field.set_attributes_from_name("age")
            new_field.model = Author
            schema_editor.add_field(Author, new_field)

            schema_editor.execute.assert_called_once_with(
                "ALTER TABLE tests_author ADD COLUMN age INT64", []
            )

    def test_remove_field(self):
        """
        Tests remove fields from models
        """
        with DatabaseSchemaEditor(self.connection) as schema_editor:
            schema_editor.execute = mock.MagicMock()
            schema_editor._constraint_names = mock.MagicMock()
            remove_field = IntegerField(unique=True)
            remove_field.set_attributes_from_name("num")
            remove_field.model = Author
            schema_editor.remove_field(Author, remove_field)

            schema_editor.execute.assert_called_once_with(
                "ALTER TABLE tests_author DROP COLUMN num"
            )

        if HAS_OPENTELEMETRY_INSTALLED:
            span_list = self.ot_exporter.get_finished_spans()
            self.assertEqual(len(span_list), 1)
            self.assertSpanAttributes(
                "CloudSpannerDjango.remove_field",
                attributes=dict(
                    BASE_ATTRIBUTES,
                    model_name="tests_author",
                    field="num",
                ),
                span=span_list[0],
            )

    def test_remove_field_with_index(self):
        """
        Tests remove fields from models
        """
        with DatabaseSchemaEditor(self.connection) as schema_editor:
            schema_editor.execute = mock.MagicMock()

            def delete_index_sql(*args, **kwargs):
                # Overriding Statement creation with sql string.
                return "DROP INDEX num_unique"

            def constraint_names(*args, **kwargs):
                return ["num_unique"]

            schema_editor._delete_index_sql = delete_index_sql
            schema_editor._constraint_names = constraint_names

            remove_field = IntegerField(unique=True)
            remove_field.set_attributes_from_name("num")
            remove_field.model = Author
            schema_editor.remove_field(Author, remove_field)

            calls = [
                mock.call("DROP INDEX num_unique"),
                mock.call("ALTER TABLE tests_author DROP COLUMN num"),
            ]
            schema_editor.execute.assert_has_calls(calls)

        if HAS_OPENTELEMETRY_INSTALLED:
            span_list = self.ot_exporter.get_finished_spans()
            self.assertEqual(len(span_list), 2)
            self.assertSpanAttributes(
                "CloudSpannerDjango.remove_field.delete_index",
                attributes=dict(
                    BASE_ATTRIBUTES,
                    model_name="tests_author",
                    field="num",
                    index_name="num_unique",
                ),
                span=span_list[0],
            )
            self.assertSpanAttributes(
                "CloudSpannerDjango.remove_field",
                attributes=dict(
                    BASE_ATTRIBUTES,
                    model_name="tests_author",
                    field="num",
                ),
                span=span_list[1],
            )

    def test_column_sql_not_null_field(self):
        """
        Tests column sql for not null field
        """
        with DatabaseSchemaEditor(self.connection) as schema_editor:
            schema_editor.execute = mock.MagicMock()
            new_field = IntegerField()
            new_field.set_attributes_from_name("num")
            new_field.model = Author
            sql, params = schema_editor.column_sql(Author, new_field)
            self.assertEqual(sql, "INT64 NOT NULL")
            self.assertEqual(params, [])

    def test_column_sql_nullable_field(self):
        """
        Tests column sql for nullable field
        """
        with DatabaseSchemaEditor(self.connection) as schema_editor:
            schema_editor.execute = mock.MagicMock()
            new_field = IntegerField(null=True)
            new_field.set_attributes_from_name("num")
            new_field.model = Author
            sql, params = schema_editor.column_sql(Author, new_field)
            self.assertEqual(sql, "INT64")
            self.assertEqual(params, [])

    def test_column_add_index(self):
        """
        Tests column add index
        """
        with DatabaseSchemaEditor(self.connection) as schema_editor:
            schema_editor.execute = mock.MagicMock()
            index = Index(name="test_author_index_num", fields=["num"])
            schema_editor.add_index(Author, index)
            name, args, kwargs = schema_editor.execute.mock_calls[0]
            self.assertEqual(
                str(args[0]),
                "CREATE INDEX test_author_index_num ON tests_author (num)",
            )
            self.assertEqual(kwargs["params"], None)
            self.assertEqual(name, "")
        if HAS_OPENTELEMETRY_INSTALLED:
            span_list = self.ot_exporter.get_finished_spans()
            self.assertEqual(len(span_list), 1)
            self.assertSpanAttributes(
                "CloudSpannerDjango.add_index",
                attributes=dict(
                    BASE_ATTRIBUTES,
                    model_name="tests_author",
                    index="num",
                ),
                span=span_list[0],
            )

    def test_alter_field(self):
        """
        Tests altering existing field in table
        """
        with DatabaseSchemaEditor(self.connection) as schema_editor:
            schema_editor.execute = mock.MagicMock()
            old_field = IntegerField()
            old_field.set_attributes_from_name("num")
            old_field.model = Author
            new_field = IntegerField()
            new_field.set_attributes_from_name("author_num")
            new_field.model = Author
            schema_editor.alter_field(Author, old_field, new_field)

            schema_editor.execute.assert_called_once_with(
                "ALTER TABLE tests_author RENAME COLUMN num TO author_num"
            )

    def test_alter_field_change_null_with_single_index(self):
        """
        Tests altering nullability of field with single index
        """
        with DatabaseSchemaEditor(self.connection) as schema_editor:
            schema_editor.execute = mock.MagicMock()

            def delete_index_sql(*args, **kwargs):
                # Overriding Statement creation with sql string.
                return "DROP INDEX num_unique"

            def create_index_sql(*args, **kwargs):
                # Overriding Statement creation with sql string.
                return "CREATE INDEX tests_author ON tests_author (author_num)"

            def constraint_names(*args, **kwargs):
                return ["num_unique"]

            schema_editor._delete_index_sql = delete_index_sql
            schema_editor._create_index_sql = create_index_sql
            schema_editor._constraint_names = constraint_names
            old_field = IntegerField(null=True, db_index=True)
            old_field.set_attributes_from_name("num")
            old_field.model = Author
            new_field = IntegerField(db_index=True)
            new_field.set_attributes_from_name("author_num")
            new_field.model = Author
            schema_editor.alter_field(Author, old_field, new_field)

            calls = [
                mock.call("DROP INDEX num_unique"),
                mock.call("ALTER TABLE tests_author RENAME COLUMN num TO author_num"),
                mock.call(
                    "ALTER TABLE tests_author ALTER COLUMN author_num INT64 NOT NULL",
                    [],
                ),
                mock.call("CREATE INDEX tests_author ON tests_author (author_num)"),
            ]
            schema_editor.execute.assert_has_calls(calls)
        if HAS_OPENTELEMETRY_INSTALLED:
            span_list = self.ot_exporter.get_finished_spans()
            self.assertEqual(len(span_list), 3)
            self.assertSpanAttributes(
                "CloudSpannerDjango.alter_field.delete_index",
                attributes=dict(
                    BASE_ATTRIBUTES,
                    model_name="tests_author",
                    index_name="num_unique",
                    alter_field="num",
                ),
                span=span_list[0],
            )
            self.assertSpanAttributes(
                "CloudSpannerDjango.alter_field",
                attributes=dict(
                    BASE_ATTRIBUTES,
                    model_name="tests_author",
                    alter_field="num",
                ),
                span=span_list[1],
            )
            self.assertSpanAttributes(
                "CloudSpannerDjango.alter_field.recreate_index",
                attributes=dict(
                    BASE_ATTRIBUTES,
                    model_name="tests_author",
                    alter_field="author_num",
                ),
                span=span_list[2],
            )

    def test_alter_field_nullability_change_raise_not_support_error(self):
        """
        Tests altering nullability of existing field in table
        """
        with DatabaseSchemaEditor(self.connection) as schema_editor:
            schema_editor.execute = mock.MagicMock()

            def constraint_names(*args, **kwargs):
                return ["num_unique"]

            schema_editor._constraint_names = constraint_names
            old_field = IntegerField(null=True)
            old_field.set_attributes_from_name("num")
            old_field.model = Author
            new_field = IntegerField()
            new_field.set_attributes_from_name("author_num")
            new_field.model = Author
            with self.assertRaises(NotSupportedError):
                schema_editor.alter_field(Author, old_field, new_field)

    def test_alter_field_change_null_with_multiple_index_error(self):
        """
        Tests altering nullability of field with multiple index not supported
        """
        with DatabaseSchemaEditor(self.connection) as schema_editor:
            schema_editor.execute = mock.MagicMock()

            def constraint_names(*args, **kwargs):
                return ["num_unique", "dummy_index"]

            schema_editor._constraint_names = constraint_names
            old_field = IntegerField(null=True, db_index=True)
            old_field.set_attributes_from_name("num")
            old_field.model = Author
            new_field = IntegerField()
            new_field.set_attributes_from_name("author_num")
            new_field.model = Author
            with self.assertRaises(NotSupportedError):
                schema_editor.alter_field(Author, old_field, new_field)

    def test_autofield_no_default(self):
        """Spanner, default is not provided."""
        field = AutoField(name="field_name")
        assert gen_rand_int64 == field.default

    def test_autofield_default(self):
        """Spanner, default provided."""
        mock_func = mock.Mock()
        field = AutoField(name="field_name", default=mock_func)
        assert gen_rand_int64 != field.default
        assert mock_func == field.default

    def test_autofield_not_spanner(self):
        """Not Spanner, default not provided."""
        connection.settings_dict["ENGINE"] = "another_db"
        field = AutoField(name="field_name")
        assert gen_rand_int64 != field.default
        connection.settings_dict["ENGINE"] = "django_spanner"

    def test_autofield_not_spanner_w_default(self):
        """Not Spanner, default provided."""
        connection.settings_dict["ENGINE"] = "another_db"
        mock_func = mock.Mock()
        field = AutoField(name="field_name", default=mock_func)
        assert gen_rand_int64 != field.default
        assert mock_func == field.default
        connection.settings_dict["ENGINE"] = "django_spanner"

    def test_autofield_spanner_as_non_default_db_random_generation_enabled(
        self,
    ):
        """Not Spanner as the default db, default for field not provided."""
        connections.settings["default"]["ENGINE"] = "another_db"
        connections.settings["secondary"]["ENGINE"] = "django_spanner"
        connections.settings["secondary"]["RANDOM_ID_GENERATION_ENABLED"] = "true"
        field = AutoField(name="field_name")
        assert gen_rand_int64 == field.default
        connections.settings["default"]["ENGINE"] = "django_spanner"
        connections.settings["secondary"]["ENGINE"] = "django_spanner"
        del connections.settings["secondary"]["RANDOM_ID_GENERATION_ENABLED"]

    def test_autofield_random_generation_disabled(self):
        """Spanner, default is not provided."""
        connections.settings["default"]["RANDOM_ID_GENERATION_ENABLED"] = "false"
        field = AutoField(name="field_name")
        assert gen_rand_int64 != field.default
        del connections.settings["default"]["RANDOM_ID_GENERATION_ENABLED"]

    def test_index_include_sql(self):
        """Tests _index_include_sql with normal fields."""
        schema_editor = DatabaseSchemaEditor(self.connection)
        sql = schema_editor._index_include_sql(Author, ["name", "last_name"])
        self.assertEqual(sql, " STORING (name, last_name)")

    def test_index_include_sql_with_field_objects(self):
        """Tests _index_include_sql with Field instances possessing a .column attribute."""
        schema_editor = DatabaseSchemaEditor(self.connection)
        field_mock = mock.MagicMock(column="custom_col")
        sql = schema_editor._index_include_sql(Author, [field_mock])
        self.assertEqual(sql, " STORING (custom_col)")

    def test_index_include_sql_includes_all_fields(self):
        """Tests _index_include_sql formats all included columns directly."""
        schema_editor = DatabaseSchemaEditor(self.connection)
        sql = schema_editor._index_include_sql(Author, ["id", "name"])
        self.assertEqual(sql, " STORING (id, name)")

    def test_index_include_sql_empty(self):
        """Tests _index_include_sql returns empty string when include is empty."""
        schema_editor = DatabaseSchemaEditor(self.connection)
        self.assertEqual(schema_editor._index_include_sql(Author, []), "")
        self.assertEqual(schema_editor._index_include_sql(Author, None), "")

    def test_skip_default_generated_and_db_default(self):
        """Tests skip_default for generated and db_default fields."""
        schema_editor = DatabaseSchemaEditor(self.connection)
        generated_field = mock.MagicMock(generated=True)
        self.assertFalse(schema_editor.skip_default(generated_field))

        db_default_field = mock.MagicMock(
            generated=False, db_default="CURRENT_TIMESTAMP()"
        )
        self.assertFalse(schema_editor.skip_default(db_default_field))

        normal_field = mock.MagicMock(generated=False, db_default=None)
        self.assertTrue(schema_editor.skip_default(normal_field))

    def test_quote_value_googlesql_literals(self):
        import datetime
        import uuid
        from decimal import Decimal

        from django.apps.registry import Apps
        from django.db import models
        from django.db.models.functions import Concat, Lower, Now
        from django.test import override_settings
        from google.cloud.spanner_dbapi.parse_utils import DateStr, TimestampStr
        from google.cloud.spanner_v1 import JsonObject

        schema_editor = DatabaseSchemaEditor(self.connection)
        self.assertEqual(schema_editor.quote_value(True), "TRUE")
        self.assertEqual(schema_editor.quote_value(False), "FALSE")
        self.assertEqual(schema_editor.quote_value(None), "NULL")
        self.assertEqual(schema_editor.quote_value(42), "42")
        self.assertEqual(schema_editor.quote_value(1.5), "1.5")
        self.assertEqual(
            schema_editor.quote_value("it's a \\ test\n\r\t\x00\x7f"),
            r"'it\'s a \\ test\n\r\t\x00\x7f'",
        )
        self.assertEqual(
            schema_editor.quote_value(JsonObject({"k": "it's"})),
            r"""JSON '{"k":"it\'s"}'""",
        )
        self.assertEqual(schema_editor.quote_value(JsonObject(None)), "NULL")
        self.assertEqual(
            schema_editor.quote_value(
                uuid.UUID("12345678-1234-5678-1234-567812345678")
            ),
            "'12345678123456781234567812345678'",
        )
        self.assertEqual(schema_editor.quote_value(b"\x00\xffa"), r"b'\x00\xff\x61'")
        self.assertEqual(
            schema_editor.quote_value(DateStr("2026-11-10")),
            "DATE '2026-11-10'",
        )
        self.assertEqual(
            schema_editor.quote_value(TimestampStr("2026-11-10T01:02:03.000000Z")),
            "TIMESTAMP '2026-11-10T01:02:03.000000Z'",
        )
        self.assertEqual(
            schema_editor.quote_value(datetime.date(2026, 11, 10)),
            "DATE '2026-11-10'",
        )
        with override_settings(USE_TZ=False):
            self.assertEqual(
                schema_editor.quote_value(datetime.datetime(2026, 11, 10, 1, 2, 3)),
                "TIMESTAMP '2026-11-10T01:02:03Z'",
            )
        with override_settings(USE_TZ=True, TIME_ZONE="America/New_York"):
            self.assertEqual(
                schema_editor.quote_value(datetime.datetime(2026, 1, 15, 12, 0, 0)),
                "TIMESTAMP '2026-01-15T17:00:00Z'",
            )
        tz_plus2 = datetime.timezone(datetime.timedelta(hours=2))
        self.assertEqual(
            schema_editor.quote_value(
                datetime.datetime(2026, 11, 10, 3, 2, 3, tzinfo=tz_plus2)
            ),
            "TIMESTAMP '2026-11-10T01:02:03Z'",
        )
        self.assertEqual(
            schema_editor.quote_value(datetime.time(12, 30, 0)),
            "TIMESTAMP '0001-01-01T12:30:00.000000Z'",
        )
        self.assertEqual(
            schema_editor.quote_value(Decimal("12.34")),
            "NUMERIC '12.34'",
        )
        self.assertEqual(
            schema_editor.quote_value(float("nan")),
            "CAST('NaN' AS FLOAT64)",
        )
        self.assertEqual(
            schema_editor.quote_value(float("inf")),
            "CAST('Infinity' AS FLOAT64)",
        )
        self.assertEqual(
            schema_editor.quote_value(float("-inf")),
            "CAST('-Infinity' AS FLOAT64)",
        )
        with self.assertRaises(ValueError):
            schema_editor.quote_value(Decimal("NaN"))
        with self.assertRaises(TypeError):
            schema_editor.quote_value(object())

        class _LiteralModel(models.Model):
            name = models.CharField(max_length=40)
            tag = models.CharField(max_length=20, db_default="it's")
            created_at = models.DateTimeField(db_default=Now())
            gen_tag = models.GeneratedField(
                expression=Concat(models.Value("a'b"), "name"),
                output_field=models.CharField(max_length=80),
                db_persist=True,
            )
            gen_lower = models.GeneratedField(
                expression=Lower("name"),
                output_field=models.CharField(max_length=80),
                db_persist=True,
            )

            class Meta:
                app_label = "tests"
                apps = Apps()

        def_sql, _ = schema_editor.column_sql(
            _LiteralModel, _LiteralModel._meta.get_field("tag")
        )
        self.assertIn(r"DEFAULT ('it\'s')", def_sql)
        now_sql, _ = schema_editor.column_sql(
            _LiteralModel, _LiteralModel._meta.get_field("created_at")
        )
        self.assertIn("DEFAULT (", now_sql)
        gen_sql, _ = schema_editor.column_sql(
            _LiteralModel, _LiteralModel._meta.get_field("gen_tag")
        )
        self.assertIn(r"'a\'b'", gen_sql)
        self.assertTrue(gen_sql.endswith("STORED"))
        gen_np_sql, _ = schema_editor.column_sql(
            _LiteralModel, _LiteralModel._meta.get_field("gen_lower")
        )
        self.assertTrue(gen_np_sql.endswith("STORED"))

    def test_prepare_sql_script_strips_comment_and_empty_fragments(self):
        script = (
            "-- leading comment\n"
            "CREATE TABLE a (id INT64 NOT NULL) PRIMARY KEY (id);\n"
            " ; \n"
            "CREATE INDEX a_idx ON a (id);\n"
            "-- trailing comment\n"
        )
        self.assertEqual(
            self.connection.ops.prepare_sql_script(script),
            [
                "CREATE TABLE a (id INT64 NOT NULL) PRIMARY KEY (id);",
                "CREATE INDEX a_idx ON a (id);",
            ],
        )

    def test_schema_editor_collect_sql_and_atomic_guard(self):
        from django.db.transaction import TransactionManagementError

        self.connection.settings_dict["AUTO_BATCH_DDL"] = True
        try:
            # Lazy unopened connection opens an auto-flushing batch only outside
            # collect_sql=True, atomic blocks, and AUTOCOMMIT=False.
            with DatabaseSchemaEditor(self.connection):
                self.assertTrue(self.connection.in_ddl_batch)
            self.assertFalse(self.connection.in_ddl_batch)

            self.connection.settings_dict["AUTOCOMMIT"] = False
            try:
                with DatabaseSchemaEditor(self.connection):
                    self.assertFalse(self.connection.in_ddl_batch)
            finally:
                self.connection.settings_dict["AUTOCOMMIT"] = True

            with DatabaseSchemaEditor(self.connection, collect_sql=True) as editor:
                self.assertFalse(self.connection.in_ddl_batch)
                editor.create_model(Author)
                with self.assertRaises(TypeError):
                    editor.execute(
                        "INSERT INTO tests_author (name) VALUES (%s)", [object()]
                    )
            self.assertFalse(self.connection.in_ddl_batch)
            self.assertTrue(
                any("CREATE TABLE tests_author" in s for s in editor.collected_sql)
            )

            self.connection.in_atomic_block = True
            try:
                with self.assertRaises(TransactionManagementError):
                    with DatabaseSchemaEditor(self.connection) as editor:
                        self.assertFalse(self.connection.in_ddl_batch)
                        editor.create_model(Author)
            finally:
                self.connection.in_atomic_block = False
        finally:
            self.connection.settings_dict.pop("AUTO_BATCH_DDL", None)
