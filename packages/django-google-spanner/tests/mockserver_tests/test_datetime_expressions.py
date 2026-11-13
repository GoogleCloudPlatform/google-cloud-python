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

import zoneinfo
from datetime import datetime, timedelta, tzinfo
from datetime import timezone as dt_timezone

from django.db.models import Value
from django.db.models.functions import (
    Coalesce,
    Extract,
    ExtractHour,
    Trunc,
    TruncDate,
    TruncDay,
    TruncHour,
    TruncTime,
    TruncWeek,
)
from django.db.utils import OperationalError
from django.test import override_settings
from django.utils import timezone
from google.cloud.spanner_v1 import ExecuteSqlRequest, TypeCode

from tests.mockserver_tests.mock_server_test_base import (
    MockServerTestBase,
    add_single_result,
)
from tests.mockserver_tests.models import Event


class TestDatetimeExpressions(MockServerTestBase):
    def get_last_execute_sql_request(self) -> ExecuteSqlRequest:
        execute_requests = [
            request
            for request in self.spanner_service.requests
            if isinstance(request, ExecuteSqlRequest)
        ]
        self.assertTrue(
            len(execute_requests) > 0,
            "Expected at least one ExecuteSqlRequest in recorded requests",
        )
        return execute_requests[-1]

    def test_extract_hour_parameterized(self):
        sql = (
            "SELECT EXTRACT(hour FROM tests_event.start_time AT TIME ZONE @a0) "
            "AS extracted_hour FROM tests_event"
        )
        add_single_result(sql, "extracted_hour", TypeCode.INT64, [("12",)])
        results = list(
            Event.objects.annotate(
                extracted_hour=ExtractHour("start_time")
            ).values_list("extracted_hour", flat=True)
        )
        self.assertEqual(results, [12])
        execute_request = self.get_last_execute_sql_request()
        self.assertEqual(execute_request.sql, sql)
        self.assertEqual(execute_request.params["a0"], "UTC")
        self.assertEqual(execute_request.param_types["a0"].code, TypeCode.STRING)

    def test_extract_named_timezone_parameterized(self):
        new_york_timezone = zoneinfo.ZoneInfo("America/New_York")
        sql = (
            "SELECT EXTRACT(hour FROM tests_event.start_time AT TIME ZONE @a0) "
            "AS extracted_hour FROM tests_event"
        )
        add_single_result(sql, "extracted_hour", TypeCode.INT64, [("8",)])
        results = list(
            Event.objects.annotate(
                extracted_hour=ExtractHour("start_time", tzinfo=new_york_timezone)
            ).values_list("extracted_hour", flat=True)
        )
        self.assertEqual(results, [8])
        execute_request = self.get_last_execute_sql_request()
        self.assertEqual(execute_request.sql, sql)
        self.assertEqual(execute_request.params["a0"], "America/New_York")
        self.assertEqual(execute_request.param_types["a0"].code, TypeCode.STRING)

    def test_extract_fixed_offset_timezone(self):
        fixed_offset_timezone = timezone.get_fixed_timezone(-283)
        sql = (
            "SELECT EXTRACT(hour FROM tests_event.start_time AT TIME ZONE @a0) "
            "AS extracted_hour FROM tests_event"
        )
        add_single_result(sql, "extracted_hour", TypeCode.INT64, [("7",)])
        results = list(
            Event.objects.annotate(
                extracted_hour=ExtractHour("start_time", tzinfo=fixed_offset_timezone)
            ).values_list("extracted_hour", flat=True)
        )
        self.assertEqual(results, [7])
        execute_request = self.get_last_execute_sql_request()
        self.assertEqual(execute_request.sql, sql)
        self.assertEqual(execute_request.params["a0"], "-0443")
        self.assertEqual(execute_request.param_types["a0"].code, TypeCode.STRING)

    def test_trunc_day_parameterized(self):
        tokyo_timezone = zoneinfo.ZoneInfo("Asia/Tokyo")
        sql = (
            "SELECT TIMESTAMP_TRUNC(tests_event.start_time, day, @a0) "
            "AS truncated_day FROM tests_event"
        )
        add_single_result(
            sql, "truncated_day", TypeCode.TIMESTAMP, [("2026-11-10T00:00:00Z",)]
        )
        results = list(
            Event.objects.annotate(
                truncated_day=TruncDay("start_time", tzinfo=tokyo_timezone)
            ).values_list("truncated_day", flat=True)
        )
        self.assertEqual(len(results), 1)
        execute_request = self.get_last_execute_sql_request()
        self.assertEqual(execute_request.sql, sql)
        self.assertEqual(execute_request.params["a0"], "Asia/Tokyo")
        self.assertEqual(execute_request.param_types["a0"].code, TypeCode.STRING)

    def test_trunc_week_parameterized(self):
        new_york_timezone = zoneinfo.ZoneInfo("America/New_York")
        sql = (
            "SELECT TIMESTAMP_ADD(TIMESTAMP_TRUNC(TIMESTAMP_SUB(tests_event.start_time, INTERVAL 1 DAY), "
            "week, @a0), INTERVAL 1 DAY) AS truncated_week FROM tests_event"
        )
        add_single_result(
            sql, "truncated_week", TypeCode.TIMESTAMP, [("2026-11-09T00:00:00Z",)]
        )
        results = list(
            Event.objects.annotate(
                truncated_week=TruncWeek("start_time", tzinfo=new_york_timezone)
            ).values_list("truncated_week", flat=True)
        )
        self.assertEqual(len(results), 1)
        execute_request = self.get_last_execute_sql_request()
        self.assertEqual(execute_request.sql, sql)
        self.assertEqual(execute_request.params["a0"], "America/New_York")
        self.assertEqual(execute_request.param_types["a0"].code, TypeCode.STRING)

    def test_trunc_date_and_time_cast_parameterized(self):
        new_york_timezone = zoneinfo.ZoneInfo("America/New_York")
        sql_date = "SELECT DATE(tests_event.start_time, @a0) AS truncated_date FROM tests_event"
        add_single_result(sql_date, "truncated_date", TypeCode.DATE, [("2026-11-10",)])
        results_date = list(
            Event.objects.annotate(
                truncated_date=TruncDate("start_time", tzinfo=new_york_timezone)
            ).values_list("truncated_date", flat=True)
        )
        self.assertEqual(len(results_date), 1)
        execute_request_date = self.get_last_execute_sql_request()
        self.assertEqual(execute_request_date.sql, sql_date)
        self.assertEqual(execute_request_date.params["a0"], "America/New_York")

        sql_time = (
            "SELECT TIMESTAMP(FORMAT_TIMESTAMP('1970-01-01 %H:%M:%E9S', "
            "tests_event.start_time, @a0), 'UTC') AS truncated_time FROM tests_event"
        )
        add_single_result(
            sql_time, "truncated_time", TypeCode.TIMESTAMP, [("2026-11-10T12:00:00Z",)]
        )
        results_time = list(
            Event.objects.annotate(
                truncated_time=TruncTime("start_time", tzinfo=new_york_timezone)
            ).values_list("truncated_time", flat=True)
        )
        self.assertEqual(len(results_time), 1)
        execute_request_time = self.get_last_execute_sql_request()
        self.assertEqual(execute_request_time.sql, sql_time)
        self.assertEqual(execute_request_time.params["a0"], "America/New_York")

    def test_extract_compound_expression_preserves_parameter_order(self):
        new_york_timezone = zoneinfo.ZoneInfo("America/New_York")
        fallback_datetime = datetime(2026, 1, 1, 15, 0, tzinfo=dt_timezone.utc)
        sql = (
            "SELECT EXTRACT(hour FROM COALESCE(tests_event.start_time, @a0) "
            "AT TIME ZONE @a1) AS extracted_hour FROM tests_event"
        )
        add_single_result(sql, "extracted_hour", TypeCode.INT64, [("10",)])
        results = list(
            Event.objects.annotate(
                extracted_hour=ExtractHour(
                    Coalesce("start_time", Value(fallback_datetime)),
                    tzinfo=new_york_timezone,
                )
            ).values_list("extracted_hour", flat=True)
        )
        self.assertEqual(results, [10])
        execute_request = self.get_last_execute_sql_request()
        self.assertEqual(execute_request.sql, sql)
        self.assertEqual(execute_request.params["a0"], "2026-01-01T15:00:00.000000Z")
        self.assertEqual(execute_request.params["a1"], "America/New_York")
        self.assertEqual(execute_request.param_types["a0"].code, TypeCode.TIMESTAMP)
        self.assertEqual(execute_request.param_types["a1"].code, TypeCode.STRING)

    @override_settings(USE_TZ=False)
    def test_extract_use_tz_false_defaults_to_utc(self):
        sql = (
            "SELECT EXTRACT(hour FROM tests_event.start_time AT TIME ZONE @a0) "
            "AS extracted_hour_use_tz_false FROM tests_event"
        )
        add_single_result(sql, "extracted_hour_use_tz_false", TypeCode.INT64, [("12",)])
        results = list(
            Event.objects.annotate(
                extracted_hour_use_tz_false=ExtractHour("start_time")
            ).values_list("extracted_hour_use_tz_false", flat=True)
        )
        self.assertEqual(results, [12])
        execute_request = self.get_last_execute_sql_request()
        self.assertEqual(execute_request.sql, sql)
        self.assertEqual(execute_request.params["a0"], "UTC")

    def test_tzname_sql_injection_travels_safely_as_parameter(self):
        class MaliciousTimezone(tzinfo):
            def utcoffset(self, dt):
                return timedelta(0)

            def tzname(self, dt):
                return "UTC'; DROP TABLE tests_event; --"

            def dst(self, dt):
                return timedelta(0)

        malicious_timezone = MaliciousTimezone()
        sql = (
            "SELECT EXTRACT(hour FROM tests_event.start_time AT TIME ZONE @a0) "
            "AS extracted_hour FROM tests_event"
        )
        add_single_result(sql, "extracted_hour", TypeCode.INT64, [("1",)])
        results = list(
            Event.objects.annotate(
                extracted_hour=ExtractHour("start_time", tzinfo=malicious_timezone)
            ).values_list("extracted_hour", flat=True)
        )
        self.assertEqual(results, [1])
        execute_request = self.get_last_execute_sql_request()
        self.assertEqual(execute_request.sql, sql)
        self.assertNotIn("DROP TABLE", execute_request.sql)
        self.assertEqual(
            execute_request.params["a0"], "UTC'; DROP TABLE tests_event; --"
        )
        self.assertEqual(execute_request.param_types["a0"].code, TypeCode.STRING)

    def test_extract_rejects_malicious_lookup_type_before_rpc(self):
        with self.assertRaises(ValueError):
            list(
                Event.objects.annotate(
                    injected=Extract("start_time", "hour'; DROP TABLE tests_event; --")
                ).values_list("injected", flat=True)
            )
        execute_requests = [
            request
            for request in self.spanner_service.requests
            if isinstance(request, ExecuteSqlRequest)
        ]
        self.assertEqual(
            len(execute_requests),
            0,
            "Expected zero ExecuteSqlRequest when lookup_type is invalid",
        )

    def test_trunc_rejects_malicious_lookup_type_before_rpc(self):
        with self.assertRaises(OperationalError):
            list(
                Event.objects.annotate(
                    injected=Trunc("start_time", "day'; DROP TABLE tests_event; --")
                ).values_list("injected", flat=True)
            )
        execute_requests = [
            request
            for request in self.spanner_service.requests
            if isinstance(request, ExecuteSqlRequest)
        ]
        self.assertEqual(
            len(execute_requests),
            0,
            "Expected zero ExecuteSqlRequest when lookup_type is invalid",
        )

    def test_trunc_timefield_defaults_to_utc(self):
        sql = (
            "SELECT TIMESTAMP_TRUNC(tests_event.start_time_of_day, hour, @a0) "
            "AS truncated_hour FROM tests_event"
        )
        add_single_result(
            sql, "truncated_hour", TypeCode.TIMESTAMP, [("1970-01-01T10:00:00Z",)]
        )
        results = list(
            Event.objects.annotate(
                truncated_hour=TruncHour("start_time_of_day")
            ).values_list("truncated_hour", flat=True)
        )
        self.assertEqual(len(results), 1)
        execute_request = self.get_last_execute_sql_request()
        self.assertEqual(execute_request.sql, sql)
        self.assertEqual(execute_request.params["a0"], "UTC")
        self.assertEqual(execute_request.param_types["a0"].code, TypeCode.STRING)

    def test_extract_timefield_defaults_to_utc(self):
        sql = (
            "SELECT EXTRACT(hour FROM tests_event.start_time_of_day AT TIME ZONE @a0) "
            "AS extracted_hour FROM tests_event"
        )
        add_single_result(sql, "extracted_hour", TypeCode.INT64, [("10",)])
        results = list(
            Event.objects.annotate(
                extracted_hour=ExtractHour("start_time_of_day")
            ).values_list("extracted_hour", flat=True)
        )
        self.assertEqual(results, [10])
        execute_request = self.get_last_execute_sql_request()
        self.assertEqual(execute_request.sql, sql)
        self.assertEqual(execute_request.params["a0"], "UTC")
        self.assertEqual(execute_request.param_types["a0"].code, TypeCode.STRING)

    def test_trunc_with_fixed_offset_parameterized(self):
        kolkata_tz = dt_timezone(timedelta(hours=5, minutes=30))
        sql = (
            "SELECT TIMESTAMP_TRUNC(tests_event.start_time, hour, @a0) "
            "AS truncated_hour FROM tests_event"
        )
        add_single_result(
            sql, "truncated_hour", TypeCode.TIMESTAMP, [("2026-11-10T10:00:00Z",)]
        )
        results = list(
            Event.objects.annotate(
                truncated_hour=TruncHour("start_time", tzinfo=kolkata_tz)
            ).values_list("truncated_hour", flat=True)
        )
        self.assertEqual(len(results), 1)
        execute_request = self.get_last_execute_sql_request()
        self.assertEqual(execute_request.sql, sql)
        self.assertEqual(execute_request.params["a0"], "+05:30")
        self.assertEqual(execute_request.param_types["a0"].code, TypeCode.STRING)

    @override_settings(USE_TZ=False)
    def test_cast_date_and_time_use_tz_false(self):
        sql_date = "SELECT DATE(tests_event.start_time, @a0) AS truncated_date FROM tests_event"
        add_single_result(sql_date, "truncated_date", TypeCode.DATE, [("2026-11-10",)])
        results_date = list(
            Event.objects.annotate(truncated_date=TruncDate("start_time")).values_list(
                "truncated_date", flat=True
            )
        )
        self.assertEqual(len(results_date), 1)
        execute_request_date = self.get_last_execute_sql_request()
        self.assertEqual(execute_request_date.sql, sql_date)
        self.assertEqual(execute_request_date.params["a0"], "UTC")

        sql_time = (
            "SELECT TIMESTAMP(FORMAT_TIMESTAMP('1970-01-01 %H:%M:%E9S', "
            "tests_event.start_time, @a0), 'UTC') AS truncated_time FROM tests_event"
        )
        add_single_result(
            sql_time, "truncated_time", TypeCode.TIMESTAMP, [("2026-11-10T12:00:00Z",)]
        )
        results_time = list(
            Event.objects.annotate(truncated_time=TruncTime("start_time")).values_list(
                "truncated_time", flat=True
            )
        )
        self.assertEqual(len(results_time), 1)
        execute_request_time = self.get_last_execute_sql_request()
        self.assertEqual(execute_request_time.sql, sql_time)
        self.assertEqual(execute_request_time.params["a0"], "UTC")

    @override_settings(USE_TZ=False)
    def test_trunc_hour_use_tz_false(self):
        sql = (
            "SELECT TIMESTAMP_TRUNC(tests_event.start_time, hour, @a0) "
            "AS truncated_hour FROM tests_event"
        )
        add_single_result(
            sql, "truncated_hour", TypeCode.TIMESTAMP, [("2026-11-10T12:00:00Z",)]
        )
        results = list(
            Event.objects.annotate(truncated_hour=TruncHour("start_time")).values_list(
                "truncated_hour", flat=True
            )
        )
        self.assertEqual(len(results), 1)
        execute_request = self.get_last_execute_sql_request()
        self.assertEqual(execute_request.sql, sql)
        self.assertEqual(execute_request.params["a0"], "UTC")
        self.assertEqual(execute_request.param_types["a0"].code, TypeCode.STRING)

    @override_settings(USE_TZ=False)
    def test_extract_and_trunc_use_tz_false_with_explicit_timezone(self):
        # Under USE_TZ=False, Django ORM's get_tzname() returns None even if tzinfo
        # is specified on the expression. Our backend then defaults the timezone parameter to 'UTC'.
        fixed_offset_timezone = timezone.get_fixed_timezone(-300)
        sql_extract = (
            "SELECT EXTRACT(hour FROM tests_event.start_time AT TIME ZONE @a0) "
            "AS extracted_hour FROM tests_event"
        )
        add_single_result(sql_extract, "extracted_hour", TypeCode.INT64, [("12",)])
        results_extract = list(
            Event.objects.annotate(
                extracted_hour=ExtractHour("start_time", tzinfo=fixed_offset_timezone)
            ).values_list("extracted_hour", flat=True)
        )
        self.assertEqual(results_extract, [12])
        execute_request_extract = self.get_last_execute_sql_request()
        self.assertEqual(execute_request_extract.sql, sql_extract)
        self.assertEqual(execute_request_extract.params["a0"], "UTC")

        sql_trunc = (
            "SELECT TIMESTAMP_TRUNC(tests_event.start_time, hour, @a0) "
            "AS truncated_hour FROM tests_event"
        )
        add_single_result(
            sql_trunc, "truncated_hour", TypeCode.TIMESTAMP, [("2026-11-10T12:00:00Z",)]
        )
        results_trunc = list(
            Event.objects.annotate(
                truncated_hour=TruncHour("start_time", tzinfo=fixed_offset_timezone)
            ).values_list("truncated_hour", flat=True)
        )
        self.assertEqual(len(results_trunc), 1)
        execute_request_trunc = self.get_last_execute_sql_request()
        self.assertEqual(execute_request_trunc.sql, sql_trunc)
        self.assertEqual(execute_request_trunc.params["a0"], "UTC")
