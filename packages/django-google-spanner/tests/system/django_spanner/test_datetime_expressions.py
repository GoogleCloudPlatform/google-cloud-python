# Copyright 2026 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

import zoneinfo
from datetime import date, datetime, time, timezone

from django.db import connection
from django.db.models.functions import (
    ExtractDay,
    ExtractHour,
    ExtractMinute,
    ExtractMonth,
    ExtractSecond,
    ExtractYear,
    TruncDate,
    TruncDay,
    TruncHour,
    TruncMonth,
    TruncTime,
    TruncYear,
)
from django.test import TransactionTestCase, override_settings

from .models import Event
from .utils import (
    setup_database,
    setup_instance,
    teardown_database,
    teardown_instance,
)


class TestDatetimeExpressions(TransactionTestCase):
    @classmethod
    def setUpClass(cls):
        setup_instance()
        setup_database()
        with connection.schema_editor() as editor:
            editor.create_model(Event)

    @classmethod
    def tearDownClass(cls):
        with connection.schema_editor() as editor:
            editor.delete_model(Event)
        teardown_database()
        teardown_instance()

    def setUp(self):
        super().setUp()
        Event.objects.all().delete()

    def test_extract_and_trunc_with_timezone(self):
        new_york_timezone = zoneinfo.ZoneInfo("America/New_York")
        # 2026-01-01 03:00:00 UTC is 2025-12-31 22:00:00 in America/New_York (UTC-5)
        event = Event.objects.create(
            start_date=datetime(2026, 1, 1, 3, 0, tzinfo=timezone.utc),
            end_date=datetime(2026, 1, 1, 12, 0, tzinfo=timezone.utc),
        )

        # 1. Extract hour in America/New_York (should be 22)
        ny_hour = (
            Event.objects.filter(pk=event.pk)
            .annotate(hour=ExtractHour("start_date", tzinfo=new_york_timezone))
            .values_list("hour", flat=True)
            .get()
        )
        self.assertEqual(ny_hour, 22)

        # 2. Extract day in America/New_York (should be 31)
        ny_day = (
            Event.objects.filter(pk=event.pk)
            .annotate(day=ExtractDay("start_date", tzinfo=new_york_timezone))
            .values_list("day", flat=True)
            .get()
        )
        self.assertEqual(ny_day, 31)

        # 3. Extract in UTC (should be 3)
        utc_hour = (
            Event.objects.filter(pk=event.pk)
            .annotate(hour=ExtractHour("start_date", tzinfo=timezone.utc))
            .values_list("hour", flat=True)
            .get()
        )
        self.assertEqual(utc_hour, 3)

        # 4. TruncDate in America/New_York (should be 2025-12-31)
        ny_date = (
            Event.objects.filter(pk=event.pk)
            .annotate(date=TruncDate("start_date", tzinfo=new_york_timezone))
            .values_list("date", flat=True)
            .get()
        )
        self.assertEqual(ny_date, date(2025, 12, 31))

        # 5. TruncDay in America/New_York
        ny_day_trunc = (
            Event.objects.filter(pk=event.pk)
            .annotate(day_trunc=TruncDay("start_date", tzinfo=new_york_timezone))
            .values_list("day_trunc", flat=True)
            .get()
        )
        self.assertEqual(
            ny_day_trunc, datetime(2025, 12, 31, 5, 0, tzinfo=new_york_timezone)
        )

        # 6. TruncTime in America/New_York (should be 22:00:00)
        ny_time = (
            Event.objects.filter(pk=event.pk)
            .annotate(time=TruncTime("start_date", tzinfo=new_york_timezone))
            .values_list("time", flat=True)
            .get()
        )
        self.assertEqual(str(ny_time), "22:00:00")

    def test_extract_and_trunc_without_timezone(self):
        event = Event.objects.create(
            start_date=datetime(2026, 1, 1, 12, 0, tzinfo=timezone.utc),
            end_date=datetime(2026, 1, 1, 15, 0, tzinfo=timezone.utc),
        )

        # Under USE_TZ=True, omitting tzinfo causes Django to use the current
        # active timezone (settings.TIME_ZONE, which defaults to UTC).
        extracted_hour = (
            Event.objects.filter(pk=event.pk)
            .annotate(hour=ExtractHour("start_date"))
            .values_list("hour", flat=True)
            .get()
        )
        self.assertEqual(extracted_hour, 12)

        truncated_hour = (
            Event.objects.filter(pk=event.pk)
            .annotate(truncated=TruncHour("start_date"))
            .values_list("truncated", flat=True)
            .get()
        )
        self.assertEqual(
            truncated_hour, datetime(2026, 1, 1, 12, 0, tzinfo=timezone.utc)
        )

        truncated_date = (
            Event.objects.filter(pk=event.pk)
            .annotate(truncated=TruncDate("start_date"))
            .values_list("truncated", flat=True)
            .get()
        )
        self.assertEqual(truncated_date, date(2026, 1, 1))

        truncated_time = (
            Event.objects.filter(pk=event.pk)
            .annotate(truncated=TruncTime("start_date"))
            .values_list("truncated", flat=True)
            .get()
        )
        self.assertEqual(truncated_time, time(12, 0, 0))

    @override_settings(USE_TZ=False)
    def test_extract_and_trunc_use_tz_false(self):
        event = Event.objects.create(
            start_date=datetime(2026, 1, 1, 12, 0),
            end_date=datetime(2026, 1, 1, 15, 0),
        )

        # When USE_TZ is False, operations default to UTC timezone arguments so that
        # naive timestamps (stored on the UTC timeline) do not drift based on the
        # database's default timezone (e.g. America/Los_Angeles).
        extracted_hour = (
            Event.objects.filter(pk=event.pk)
            .annotate(hour=ExtractHour("start_date"))
            .values_list("hour", flat=True)
            .get()
        )
        self.assertEqual(extracted_hour, 12)

        truncated_hour = (
            Event.objects.filter(pk=event.pk)
            .annotate(truncated=TruncHour("start_date"))
            .values_list("truncated", flat=True)
            .get()
        )
        self.assertEqual(truncated_hour, datetime(2026, 1, 1, 12, 0))

        truncated_date = (
            Event.objects.filter(pk=event.pk)
            .annotate(truncated=TruncDate("start_date"))
            .values_list("truncated", flat=True)
            .get()
        )
        self.assertEqual(truncated_date, date(2026, 1, 1))

        truncated_time = (
            Event.objects.filter(pk=event.pk)
            .annotate(truncated=TruncTime("start_date"))
            .values_list("truncated", flat=True)
            .get()
        )
        self.assertEqual(truncated_time, time(12, 0, 0))

    def test_date_field_roundtrip_and_expressions(self):
        event = Event.objects.create(
            start_date=datetime(2026, 1, 1, 12, 0, tzinfo=timezone.utc),
            end_date=datetime(2026, 1, 1, 15, 0, tzinfo=timezone.utc),
            event_date=date(2026, 5, 15),
        )
        refetched = Event.objects.get(pk=event.pk)
        self.assertEqual(refetched.event_date, date(2026, 5, 15))

        extracted = (
            Event.objects.filter(pk=event.pk)
            .annotate(
                year=ExtractYear("event_date"),
                month=ExtractMonth("event_date"),
                day=ExtractDay("event_date"),
            )
            .values("year", "month", "day")
            .get()
        )
        self.assertEqual(extracted["year"], 2026)
        self.assertEqual(extracted["month"], 5)
        self.assertEqual(extracted["day"], 15)

        truncated = (
            Event.objects.filter(pk=event.pk)
            .annotate(
                month=TruncMonth("event_date"),
                year=TruncYear("event_date"),
            )
            .values("month", "year")
            .get()
        )
        self.assertEqual(truncated["month"], date(2026, 5, 1))
        self.assertEqual(truncated["year"], date(2026, 1, 1))

    def test_time_field_roundtrip_and_expressions(self):
        event = Event.objects.create(
            start_date=datetime(2026, 1, 1, 12, 0, tzinfo=timezone.utc),
            end_date=datetime(2026, 1, 1, 15, 0, tzinfo=timezone.utc),
            event_time=time(14, 30, 45),
        )
        refetched = Event.objects.get(pk=event.pk)
        self.assertEqual(refetched.event_time, time(14, 30, 45))

        extracted = (
            Event.objects.filter(pk=event.pk)
            .annotate(
                hour=ExtractHour("event_time"),
                minute=ExtractMinute("event_time"),
                second=ExtractSecond("event_time"),
            )
            .values("hour", "minute", "second")
            .get()
        )
        self.assertEqual(extracted["hour"], 14)
        self.assertEqual(extracted["minute"], 30)
        self.assertEqual(extracted["second"], 45)

        truncated_hour = (
            Event.objects.filter(pk=event.pk)
            .annotate(hour=TruncHour("event_time"))
            .values_list("hour", flat=True)
            .get()
        )
        self.assertEqual(truncated_hour, time(14, 0, 0))
