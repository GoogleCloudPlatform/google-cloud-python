# Copyright 2021 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

import uuid
from base64 import b64encode
from datetime import timedelta
from decimal import Decimal
from unittest import mock

import sqlparse
from django.conf import settings
from django.core.management.color import no_style
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import JSONField
from django.db.utils import DatabaseError
from django.utils.safestring import mark_safe
from google.cloud.spanner_dbapi.parse_utils import classify_statement
from google.cloud.spanner_dbapi.types import DateStr
from google.cloud.spanner_v1 import JsonObject

from django_spanner.operations import _JsonString
from tests.unit.django_spanner.simple_test import SpannerSimpleTestClass


class TestOperations(SpannerSimpleTestClass):
    def test_max_name_length(self):
        self.assertEqual(self.db_operations.max_name_length(), 128)

    def test_quote_name(self):
        quoted_name = self.db_operations.quote_name("abc")
        self.assertEqual(quoted_name, "abc")

    def test_quote_name_empty_string(self):
        self.assertEqual(self.db_operations.quote_name(""), "")

    def test_quote_name_regular_identifiers(self):
        for identifier in ("_", "_col_1", "TestsAuthor", "col123", "table", "value"):
            with self.subTest(identifier=identifier):
                self.assertEqual(self.db_operations.quote_name(identifier), identifier)

    def test_quote_name_spanner_reserved_keyword_escaped(self):
        quoted_name = self.db_operations.quote_name("ALL")
        self.assertEqual(quoted_name, "`ALL`")

    def test_quote_name_reserved_keywords_case_insensitive(self):
        for keyword in ("all", "SELECT", "group", "UNION"):
            with self.subTest(keyword=keyword):
                self.assertEqual(self.db_operations.quote_name(keyword), f"`{keyword}`")

    def test_quote_name_single_identifier_with_dots(self):
        for identifier in ("my.table", "schema.table.col", "a.", ".a", "a..b", "."):
            with self.subTest(identifier=identifier):
                self.assertEqual(
                    self.db_operations.quote_name(identifier), f"`{identifier}`"
                )

    def test_quote_name_non_regular_identifiers(self):
        for identifier in (
            "0",
            "123col",
            "col name",
            "col-name",
            "café",
            "   ",
            " abc ",
            "\uff40",
            "²",
            "٠",
            "ſ",
            "K",
            "İ",
        ):
            with self.subTest(identifier=identifier):
                self.assertEqual(
                    self.db_operations.quote_name(identifier), f"`{identifier}`"
                )

    def test_quote_name_delimiters_and_injection_payloads(self):
        cases = [
            ("`", r"`\x60`"),
            ("``", r"`\x60\x60`"),
            ("a`", r"`a\x60`"),
            ("`a", r"`\x60a`"),
            ("`0", r"`\x600`"),
            (r"\x60", r"`\\x60`"),
            (" `abc`", r"` \x60abc\x60`"),
            ("`abc` ", r"`\x60abc\x60 `"),
            ("\x00`abc`", r"`\x00\x60abc\x60`"),
            ("`abc`\x00", r"`\x60abc\x60\x00`"),
            ("`a\nb`", r"`\x60a\nb\x60`"),
            ("`a\rb`", r"`\x60a\rb\x60`"),
            ("`a\x00b`", r"`\x60a\x00b\x60`"),
            ("`a\x1fb`", r"`\x60a\x1fb\x60`"),
            ("`a\x7fb`", r"`\x60a\x7fb\x60`"),
            ("col`name", r"`col\x60name`"),
            (r"col\name", r"`col\\name`"),
            ("\\", r"`\\`"),
            ("\\\\", r"`\\\\`"),
            (r"col\`name", r"`col\\\x60name`"),
            (r"`a\`", r"`\x60a\\\x60`"),
            (r"`a\\\`", r"`\x60a\\\\\\\x60`"),
            (r"`a\\`b`", r"`\x60a\\\\\x60b\x60`"),
            (r"`a\`b`", r"`\x60a\\\x60b\x60`"),
            (
                r"`a\` /**/ UNION SELECT 1 # `",
                r"`\x60a\\\x60 /**/ UNION SELECT 1 # \x60`",
            ),
            (
                "`a\\` --\n UNION SELECT secret FROM users -- `",
                r"`\x60a\\\x60 --\n UNION SELECT secret FROM users -- \x60`",
            ),
            (
                r"`a\` ; DROP TABLE users # `",
                r"`\x60a\\\x60 ; DROP TABLE users # \x60`",
            ),
            (r"`\z`", r"`\x60\\z\x60`"),
            (r"`\x`", r"`\x60\\x\x60`"),
            (r"`a\xb`", r"`\x60a\\xb\x60`"),
            (r"`a\xZZb`", r"`\x60a\\xZZb\x60`"),
            (r"`a\u0060b`", r"`\x60a\\u0060b\x60`"),
            (r"`a\060b`", r"`\x60a\\060b\x60`"),
            (r"`a\'b`", r"`\x60a\\'b\x60`"),
            (r"`a\"b`", r'`\x60a\\"b\x60`'),
            ("`a\\\n`", r"`\x60a\\\n\x60`"),
            ("`a` OR 1=1 -- `", r"`\x60a\x60 OR 1=1 -- \x60`"),
            ("`a`.`b`", r"`\x60a\x60.\x60b\x60`"),
            ("`a\\", r"`\x60a\\`"),
            ("col\n` OR 1=1 -- ", r"`col\n\x60 OR 1=1 -- `"),
            ("col`/*`*/; DROP TABLE t`", r"`col\x60/*\x60*/; DROP TABLE t\x60`"),
            ("col` # comment", r"`col\x60 # comment`"),
            ("col`; DROP TABLE t; --", r"`col\x60; DROP TABLE t; --`"),
            ("col' OR '1'='1", "`col' OR '1'='1`"),
            ('col" OR "1"="1', '`col" OR "1"="1`'),
            ("col@p0", "`col@p0`"),
            ("col%s", "`col%s`"),
            (mark_safe("col`; DROP TABLE t"), r"`col\x60; DROP TABLE t`"),
        ]
        for identifier, expected in cases:
            with self.subTest(identifier=identifier):
                self.assertEqual(self.db_operations.quote_name(identifier), expected)

    def test_quote_name_already_quoted_single_identifier(self):
        for identifier in (
            "`abc`",
            "`SELECT`",
            "`a.b`",
            r"`a\x60b`",
            r"`a\x0Ab`",
            r"`a\x7Fb`",
            r"`a\x00b`",
            r"`a\\`",
            r"`a\ab`",
            r"`a\bb`",
            r"`a\fb`",
            r"`a\nb`",
            r"`a\rb`",
            r"`a\tb`",
            r"`a\vb`",
        ):
            with self.subTest(identifier=identifier):
                self.assertEqual(self.db_operations.quote_name(identifier), identifier)

    def test_quote_name_idempotent(self):
        for identifier in (
            "",
            "abc",
            "SELECT",
            "my.table",
            "col`name",
            r"col\name",
            "`a` OR 1=1 -- `",
            "`a`.`b`",
            r"`a\` /**/ UNION SELECT 1 # `",
            "``",
            "`already`",
            r"`a\\`",
            "col\nname",
            "col\x00name",
        ):
            with self.subTest(identifier=identifier):
                once = self.db_operations.quote_name(identifier)
                twice = self.db_operations.quote_name(once)
                self.assertEqual(twice, once)

    def test_quote_name_escapes_control_characters(self):
        named_escapes = {
            "\a": r"\a",
            "\b": r"\b",
            "\f": r"\f",
            "\n": r"\n",
            "\r": r"\r",
            "\t": r"\t",
            "\v": r"\v",
        }
        for code in (*range(0x20), 0x7F):
            char = chr(code)
            expected_escape = named_escapes.get(char, f"\\x{code:02x}")
            with self.subTest(code=code):
                self.assertEqual(
                    self.db_operations.quote_name(f"col{char}name"),
                    f"`col{expected_escape}name`",
                )

        for identifier, expected in (
            ("col\a\b\f\vname", r"`col\a\b\f\vname`"),
            ("abc\n", r"`abc\n`"),
            ("`abc`\n", r"`\x60abc\x60\n`"),
            ("\n`abc`", r"`\n\x60abc\x60`"),
        ):
            with self.subTest(identifier=identifier):
                self.assertEqual(self.db_operations.quote_name(identifier), expected)

    def test_quote_name_sqlparse_safety(self):
        payloads = (
            "`",
            "``",
            "\\",
            r"`a\`",
            "col\rname",
            "col\x00name",
            "-- c",
            "/* c */",
            "# c",
            "col' OR '1'='1",
            'col" OR "1"="1',
            "my.table",
            r"`a\` /**/ UNION SELECT 1 # `",
            "`a\\` --\n UNION SELECT secret FROM users -- `",
            r"`a\` ; DROP TABLE users # `",
            "col\n` OR 1=1 -- ",
            "col`; DROP TABLE t; --",
            "col`/*`*/; DROP TABLE t`",
        )
        for payload in payloads:
            with self.subTest(payload=payload):
                quoted = self.db_operations.quote_name(payload)
                select_sql = f"SELECT {quoted} FROM `users` WHERE `admin` = FALSE"
                delete_sql = f"DELETE FROM {quoted} WHERE 1=1"
                for sql, token_index in ((select_sql, 2), (delete_sql, 4)):
                    self.assertEqual(sqlparse.format(sql, strip_comments=True), sql)
                    self.assertEqual(len(sqlparse.split(sql)), 1)
                    self.assertEqual(
                        str(sqlparse.parse(sql)[0].tokens[token_index]), quoted
                    )
                    parsed = classify_statement(sql)
                    self.assertEqual(parsed.statement.sql, sql)

    def test_quote_name_invalid_types(self):
        for invalid in (None, 123, True, False, 1.5, b"abc", ["abc"], {"a": 1}):
            expected_message = (
                rf"^Identifier must be a string, got {type(invalid).__name__}$"
            )
            with (
                self.subTest(invalid=invalid),
                self.assertRaisesRegex(TypeError, expected_message),
            ):
                self.db_operations.quote_name(invalid)

    def test_quote_name_running_spanner_backend_tests(self):
        with mock.patch.dict(
            "django_spanner.operations.os.environ",
            {"RUNNING_SPANNER_BACKEND_TESTS": "1"},
        ):
            self.assertEqual(
                self.db_operations.quote_name("my col-name"), "my_col_name"
            )
            self.assertEqual(self.db_operations.quote_name("SELECT"), "`SELECT`")
            self.assertEqual(
                self.db_operations.quote_name("my-col.name"), "`my_col.name`"
            )
            self.assertEqual(self.db_operations.quote_name("my-select"), "my_select")
            self.assertEqual(self.db_operations.quote_name("ALL "), "ALL_")
            self.assertEqual(
                self.db_operations.quote_name("my col`; DROP TABLE t"),
                r"`my_col\x60;_DROP_TABLE_t`",
            )
            self.assertEqual(self.db_operations.quote_name("`a b-c`"), "`a_b_c`")
            self.assertEqual(self.db_operations.quote_name("a b\nc"), r"`a_b\nc`")
            self.assertEqual(self.db_operations.quote_name("`already`"), "`already`")
            self.assertEqual(self.db_operations.quote_name(""), "")
            self.assertEqual(self.db_operations.quote_name("   "), "___")
            for sample in ("my col-name", "SELECT", "`a b-c`", "a b\nc"):
                once = self.db_operations.quote_name(sample)
                self.assertEqual(self.db_operations.quote_name(once), once)

        with mock.patch.dict(
            "django_spanner.operations.os.environ",
            {"RUNNING_SPANNER_BACKEND_TESTS": "0"},
        ):
            self.assertEqual(
                self.db_operations.quote_name("my col-name"), "`my col-name`"
            )

        with mock.patch.dict("django_spanner.operations.os.environ", {}, clear=True):
            self.assertEqual(
                self.db_operations.quote_name("my col-name"), "`my col-name`"
            )

    def test_bulk_batch_size(self):
        self.assertEqual(
            self.db_operations.bulk_batch_size(fields=None, objs=None),
            self.db_operations.connection.features.max_query_params,
        )

    def test_sql_flush(self):
        self.assertEqual(
            self.db_operations.sql_flush(style=no_style(), tables=["Table1", "Table2"]),
            ["DELETE FROM Table1 WHERE 1=1", "DELETE FROM Table2 WHERE 1=1"],
        )

    def test_sql_flush_empty_table_list(self):
        self.assertEqual(
            self.db_operations.sql_flush(style=no_style(), tables=[]),
            [],
        )

    def test_adapt_datefield_value(self):
        self.assertIsInstance(
            self.db_operations.adapt_datefield_value("dummy_date"),
            DateStr,
        )

    def test_adapt_datefield_value_none(self):
        self.assertIsNone(
            self.db_operations.adapt_datefield_value(value=None),
        )

    def test_adapt_decimalfield_value(self):
        self.assertIsInstance(
            self.db_operations.adapt_decimalfield_value(value=Decimal("1")),
            Decimal,
        )

    def test_adapt_decimalfield_value_none(self):
        self.assertIsNone(
            self.db_operations.adapt_decimalfield_value(value=None),
        )

    def test_convert_binaryfield_value(self):
        self.assertEqual(
            self.db_operations.convert_binaryfield_value(
                value=b64encode(b"abc"), expression=None, connection=None
            ),
            b"abc",
        )

    def test_convert_binaryfield_value_none(self):
        self.assertIsNone(
            self.db_operations.convert_binaryfield_value(
                value=None, expression=None, connection=None
            ),
        )

    def test_adapt_datetimefield_value_none(self):
        self.assertIsNone(
            self.db_operations.adapt_datetimefield_value(value=None),
        )

    def test_adapt_timefield_value_none(self):
        self.assertIsNone(
            self.db_operations.adapt_timefield_value(value=None),
        )

    def test_convert_uuidfield_value(self):
        uuid_obj = uuid.uuid4()
        self.assertEqual(
            self.db_operations.convert_uuidfield_value(
                str(uuid_obj), expression=None, connection=None
            ),
            uuid_obj,
        )

    def test_convert_uuidfield_value_none(self):
        self.assertIsNone(
            self.db_operations.convert_uuidfield_value(
                value=None, expression=None, connection=None
            ),
        )

    def test_json_field_feature_flags(self):
        self.assertTrue(self.connection.features.has_native_json_field)
        self.assertTrue(self.connection.features.supports_json_field)
        self.assertTrue(self.connection.features.supports_primitives_in_json_field)
        self.assertFalse(self.connection.features.supports_json_field_contains)

    def test_adapt_json_value_dict(self):
        value = {"a": 1, "b": "test"}
        res = self.db_operations.adapt_json_value(value, None)
        self.assertIsInstance(res, _JsonString)
        self.assertIsInstance(res, JsonObject)
        self.assertFalse(res._is_null)
        self.assertFalse(res._is_array)
        self.assertFalse(res._is_scalar_value)
        self.assertEqual(dict(res), {})
        self.assertEqual(repr(res), f"_JsonString({res.serialize()!r})")
        self.assertEqual(res.serialize(), '{"a": 1, "b": "test"}')
        self.assertNotEqual(res, None)

    def test_adapt_json_value_list(self):
        value = [1, 2, 3]
        res = self.db_operations.adapt_json_value(value, None)
        self.assertIsInstance(res, _JsonString)
        self.assertEqual(res.serialize(), "[1, 2, 3]")

    def test_adapt_json_value_none_becomes_json_null(self):
        res = self.db_operations.adapt_json_value(None, None)
        self.assertIsInstance(res, _JsonString)
        self.assertFalse(res._is_null)
        self.assertEqual(dict(res), {})
        self.assertEqual(res.serialize(), "null")
        self.assertNotEqual(res, None)

    def test_adapt_json_value_primitives(self):
        for primitive, expected in [
            ("hello", '"hello"'),
            (42, "42"),
            (True, "true"),
            (3.14, "3.14"),
        ]:
            res = self.db_operations.adapt_json_value(primitive, None)
            self.assertIsInstance(res, _JsonString)
            self.assertEqual(res.serialize(), expected)

    def test_adapt_json_value_custom_encoder(self):
        u = uuid.UUID("12345678-1234-5678-1234-567812345678")
        res = self.db_operations.adapt_json_value(
            {"id": u, "amount": Decimal("12.34")}, DjangoJSONEncoder
        )
        self.assertIsInstance(res, _JsonString)
        self.assertEqual(
            res.serialize(),
            '{"id": "12345678-1234-5678-1234-567812345678", "amount": "12.34"}',
        )

    def test_get_db_converters_jsonfield(self):
        expression = mock.MagicMock()
        expression.output_field = JSONField()
        converters = self.db_operations.get_db_converters(expression)
        self.assertIn(self.db_operations.convert_jsonfield_value, converters)

    def test_convert_jsonfield_value_dict(self):
        obj = JsonObject({"a": 1})
        res = self.db_operations.convert_jsonfield_value(obj, None, None)
        self.assertEqual(res, {"a": 1})

    def test_convert_jsonfield_value_list(self):
        obj = JsonObject([1, "two", {"three": 3}])
        res = self.db_operations.convert_jsonfield_value(obj, None, None)
        self.assertEqual(res, [1, "two", {"three": 3}])

    def test_convert_jsonfield_value_primitives(self):
        for raw, expected in [
            ('"hello"', "hello"),
            ("42", 42),
            ("true", True),
            ("3.14", 3.14),
        ]:
            obj = JsonObject.from_str(raw)
            res = self.db_operations.convert_jsonfield_value(obj, None, None)
            self.assertEqual(res, expected)

    def test_convert_jsonfield_value_null_json_object(self):
        obj = JsonObject.from_str("null")
        res = self.db_operations.convert_jsonfield_value(obj, None, None)
        self.assertIsNone(res)

    def test_convert_jsonfield_value_custom_decoder(self):
        import json

        class CustomDecoder(json.JSONDecoder):
            def decode(self, s):
                data = super().decode(s)
                if isinstance(data, dict):
                    data["decoded"] = True
                return data

        expr = mock.MagicMock()
        expr.output_field = JSONField(decoder=CustomDecoder)
        obj = JsonObject({"a": 1})
        res = self.db_operations.convert_jsonfield_value(obj, expr, None)
        self.assertEqual(res, {"a": 1, "decoded": True})

        null_obj = JsonObject.from_str("null")
        self.assertIsNone(
            self.db_operations.convert_jsonfield_value(null_obj, expr, None)
        )

    def test_convert_jsonfield_value_subclass_with_custom_from_db_value(self):
        class TaggedJSONField(JSONField):
            def from_db_value(self, value, expression, connection):
                return {"wrapped": super().from_db_value(value, expression, connection)}

        expr = mock.MagicMock()
        expr.output_field = TaggedJSONField()
        obj = JsonObject({"a": 1})
        raw = self.db_operations.convert_jsonfield_value(obj, expr, None)
        self.assertEqual(raw, '{"a":1}')
        self.assertEqual(
            expr.output_field.from_db_value(raw, expr, None),
            {"wrapped": {"a": 1}},
        )

    def test_convert_jsonfield_value_none(self):
        res = self.db_operations.convert_jsonfield_value(None, None, None)
        self.assertIsNone(res)

    def test_convert_jsonfield_value_other(self):
        res = self.db_operations.convert_jsonfield_value('{"a": 1}', None, None)
        self.assertEqual(res, {"a": 1})
        invalid_res = self.db_operations.convert_jsonfield_value(
            "{invalid json", None, None
        )
        self.assertEqual(invalid_res, "{invalid json")

    def test_date_extract_sql(self):
        self.assertEqual(
            self.db_operations.date_extract_sql("week", "dummy_field"),
            ("EXTRACT(isoweek FROM dummy_field)", None),
        )

    def test_date_extract_sql_lookup_type_dayofweek(self):
        self.assertEqual(
            self.db_operations.date_extract_sql("dayofweek", "dummy_field"),
            ("EXTRACT(dayofweek FROM dummy_field)", None),
        )

    def test_datetime_extract_sql(self):
        settings.USE_TZ = True
        self.assertEqual(
            self.db_operations.datetime_extract_sql(
                "dayofweek", "dummy_field", None, "IST"
            ),
            (
                'EXTRACT(dayofweek FROM dummy_field AT TIME ZONE "IST")',
                None,
            ),
        )

    def test_datetime_extract_sql_use_tz_false(self):
        settings.USE_TZ = False
        self.assertEqual(
            self.db_operations.datetime_extract_sql(
                "dayofweek", "dummy_field", None, "IST"
            ),
            (
                'EXTRACT(dayofweek FROM dummy_field AT TIME ZONE "UTC")',
                None,
            ),
        )
        settings.USE_TZ = True  # reset changes.

    def test_time_extract_sql(self):
        self.assertEqual(
            self.db_operations.time_extract_sql("dayofweek", "dummy_field"),
            (
                'EXTRACT(dayofweek FROM dummy_field AT TIME ZONE "UTC")',
                None,
            ),
        )

    def test_time_trunc_sql(self):
        self.assertEqual(
            self.db_operations.time_trunc_sql("dayofweek", "dummy_field", None),
            ('TIMESTAMP_TRUNC(dummy_field, dayofweek, "UTC")', None),
        )

    def test_datetime_cast_date_sql(self):
        self.assertEqual(
            self.db_operations.datetime_cast_date_sql("dummy_field", None, "IST"),
            ('DATE(dummy_field, "IST")', None),
        )

    def test_datetime_cast_time_sql(self):
        settings.USE_TZ = True
        self.assertEqual(
            self.db_operations.datetime_cast_time_sql("dummy_field", None, "IST"),
            (
                "TIMESTAMP(FORMAT_TIMESTAMP('%Y-%m-%d %R:%E9S %Z', dummy_field, 'IST'))",
                None,
            ),
        )

    def test_datetime_cast_time_sql_use_tz_false(self):
        settings.USE_TZ = False
        self.assertEqual(
            self.db_operations.datetime_cast_time_sql("dummy_field", None, "IST"),
            (
                "TIMESTAMP(FORMAT_TIMESTAMP('%Y-%m-%d %R:%E9S %Z', dummy_field, 'UTC'))",
                None,
            ),
        )
        settings.USE_TZ = True  # reset changes.

    def test_date_interval_sql(self):
        self.assertEqual(
            self.db_operations.date_interval_sql(timedelta(days=1)),
            "INTERVAL 86400000000 MICROSECOND",
        )

    def test_format_for_duration_arithmetic(self):
        self.assertEqual(
            self.db_operations.format_for_duration_arithmetic(1200),
            "INTERVAL 1200 MICROSECOND",
        )

    def test_combine_expression_mod(self):
        self.assertEqual(
            self.db_operations.combine_expression("%%", ["10", "2"]),
            "MOD(10, 2)",
        )

    def test_combine_expression_power(self):
        self.assertEqual(
            self.db_operations.combine_expression("^", ["10", "2"]),
            "POWER(10, 2)",
        )

    def test_combine_expression_bit_extention(self):
        self.assertEqual(
            self.db_operations.combine_expression(">>", ["10", "2"]),
            "CAST(FLOOR(10 / POW(2, 2)) AS INT64)",
        )

    def test_combine_expression_multiply(self):
        self.assertEqual(
            self.db_operations.combine_expression("*", ["10", "2"]),
            "10 * 2",
        )

    def test_combine_duration_expression_add(self):
        self.assertEqual(
            self.db_operations.combine_duration_expression(
                "+",
                ['TIMESTAMP "2008-12-25 15:30:00+00', "INTERVAL 10 MINUTE"],
            ),
            'TIMESTAMP_ADD(TIMESTAMP "2008-12-25 15:30:00+00, INTERVAL 10 MINUTE)',
        )

    def test_combine_duration_expression_subtract(self):
        self.assertEqual(
            self.db_operations.combine_duration_expression(
                "-",
                ['TIMESTAMP "2008-12-25 15:30:00+00', "INTERVAL 10 MINUTE"],
            ),
            'TIMESTAMP_SUB(TIMESTAMP "2008-12-25 15:30:00+00, INTERVAL 10 MINUTE)',
        )

    def test_combine_duration_expression_database_error(self):
        msg = "Invalid connector for timedelta:"
        with self.assertRaisesRegex(DatabaseError, msg):
            self.db_operations.combine_duration_expression(
                "*",
                ['TIMESTAMP "2008-12-25 15:30:00+00', "INTERVAL 10 MINUTE"],
            )

    def test_lookup_cast_match_lookup_type(self):
        self.assertEqual(
            self.db_operations.lookup_cast(
                "contains",
            ),
            "CAST(%s AS STRING)",
        )

    def test_lookup_cast_unmatched_lookup_type(self):
        self.assertEqual(
            self.db_operations.lookup_cast(
                "dummy",
            ),
            "%s",
        )

    def test_returning_columns(self):
        field1 = mock.MagicMock(column="id")
        field2 = mock.MagicMock(column="name")
        sql, params = self.db_operations.returning_columns([field1, field2])
        self.assertEqual(sql, "THEN RETURN id, name")
        self.assertEqual(params, ())

    def test_returning_columns_with_strings(self):
        sql, params = self.db_operations.returning_columns(["id", "created_at"])
        self.assertEqual(sql, "THEN RETURN id, created_at")
        self.assertEqual(params, ())

    def test_returning_columns_empty(self):
        sql, params = self.db_operations.returning_columns([])
        self.assertEqual(sql, "")
        self.assertEqual(params, ())

    def test_return_insert_columns_alias(self):
        field = mock.MagicMock(column="id")
        sql, params = self.db_operations.return_insert_columns([field])
        self.assertEqual(sql, "THEN RETURN id")
        self.assertEqual(params, ())

    def test_savepoint_sql(self):
        self.assertEqual(self.db_operations.savepoint_create_sql("sp1"), "SELECT 1")
        self.assertEqual(self.db_operations.savepoint_commit_sql("sp1"), "SELECT 1")
        self.assertEqual(self.db_operations.savepoint_rollback_sql("sp1"), "SELECT 1")

    def test_no_limit_value(self):
        self.assertEqual(self.db_operations.no_limit_value(), 9223372036854775807)

    def test_get_limit_offset_params(self):
        limit, offset = self.db_operations._get_limit_offset_params(10, None)
        self.assertEqual(limit, 9223372036854775807 - 10)
        self.assertEqual(offset, 10)

        limit, offset = self.db_operations._get_limit_offset_params(0, 5)
        self.assertEqual(limit, 5)
        self.assertEqual(offset, 0)

    def test_prep_for_like_and_iexact_query(self):
        self.assertEqual(
            self.db_operations.prep_for_like_query("test.val*"), r"test\.val\*"
        )
        self.assertEqual(
            self.db_operations.prep_for_iexact_query("test.val*"), r"test\.val\*"
        )

    def test_bulk_insert_sql(self):
        fields = [mock.MagicMock(column="col1"), mock.MagicMock(column="col2")]
        sql = self.db_operations.bulk_insert_sql(fields, [["%s", "%s"], ["%s", "%s"]])
        self.assertEqual(sql, "VALUES (%s, %s), (%s, %s)")

    def test_date_and_time_trunc_sql(self):
        sql, params = self.db_operations.date_trunc_sql("year", "field", None)
        self.assertEqual(sql, "DATE_TRUNC(CAST(field AS DATE), year)")
        self.assertIsNone(params)

        sql, params = self.db_operations.time_trunc_sql("hour", "field", None)
        self.assertEqual(sql, 'TIMESTAMP_TRUNC(field, hour, "UTC")')
        self.assertIsNone(params)

        sql, params = self.db_operations.datetime_trunc_sql(
            "day", "field", None, tzname="UTC"
        )
        self.assertEqual(sql, 'TIMESTAMP_TRUNC(field, day, "UTC")')
        self.assertIsNone(params)

    def test_datetime_cast_sql(self):
        sql, params = self.db_operations.datetime_cast_date_sql("field", None, "UTC")
        self.assertEqual(sql, 'DATE(field, "UTC")')
        self.assertIsNone(params)

        sql, params = self.db_operations.datetime_cast_time_sql("field", None, "UTC")
        self.assertEqual(
            sql,
            "TIMESTAMP(FORMAT_TIMESTAMP('%Y-%m-%d %R:%E9S %Z', field, 'UTC'))",
        )
        self.assertIsNone(params)
