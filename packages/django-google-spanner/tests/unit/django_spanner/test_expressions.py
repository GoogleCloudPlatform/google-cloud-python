# Copyright 2021 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

from django.db.models import F

from django_spanner.compiler import SQLCompiler
from tests.unit.django_spanner.simple_test import SpannerSimpleTestClass

from .models import Report


class TestExpressions(SpannerSimpleTestClass):
    def test_order_by_sql_query_with_order_by_null_last(self):
        qs1 = Report.objects.values("name").order_by(F("name").desc(nulls_last=True))
        compiler = SQLCompiler(qs1.query, self.connection, "default")
        sql_compiled, _ = compiler.as_sql()
        self.assertEqual(
            sql_compiled,
            "SELECT tests_report.name AS name FROM tests_report ORDER BY "
            + "tests_report.name IS NULL, tests_report.name DESC",
        )

    def test_order_by_sql_query_with_order_by_null_first(self):
        qs1 = Report.objects.values("name").order_by(F("name").desc(nulls_first=True))
        compiler = SQLCompiler(qs1.query, self.connection, "default")
        sql_compiled, _ = compiler.as_sql()
        self.assertEqual(
            sql_compiled,
            "SELECT tests_report.name AS name FROM tests_report ORDER BY "
            + "tests_report.name IS NOT NULL, tests_report.name DESC",
        )

    def test_order_by_sql_query_with_order_by_name(self):
        qs1 = Report.objects.values("name")
        compiler = SQLCompiler(qs1.query, self.connection, "default")
        sql_compiled, _ = compiler.as_sql()
        self.assertEqual(
            sql_compiled,
            "SELECT tests_report.name AS name FROM tests_report ORDER BY " + "1 ASC",
        )
