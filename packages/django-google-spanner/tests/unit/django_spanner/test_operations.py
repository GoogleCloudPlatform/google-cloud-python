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

from django.conf import settings
from django.core.management.color import no_style
from django.db.utils import DatabaseError
from google.cloud.spanner_dbapi.types import DateStr

from tests.unit.django_spanner.simple_test import SpannerSimpleTestClass


class TestOperations(SpannerSimpleTestClass):
    def test_max_name_length(self):
        self.assertEqual(self.db_operations.max_name_length(), 128)

    def test_quote_name(self):
        quoted_name = self.db_operations.quote_name("abc")
        self.assertEqual(quoted_name, "abc")

    def test_quote_name_spanner_reserved_keyword_escaped(self):
        quoted_name = self.db_operations.quote_name("ALL")
        self.assertEqual(quoted_name, "`ALL`")

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
