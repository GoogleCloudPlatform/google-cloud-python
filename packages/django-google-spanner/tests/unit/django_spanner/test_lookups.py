# Copyright 2021 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

from decimal import Decimal

from django.db.models import F, Value
from django.db.models.functions import Concat

from django_spanner.compiler import SQLCompiler
from tests.unit.django_spanner.simple_test import SpannerSimpleTestClass

from .models import Author, Number


class TestLookups(SpannerSimpleTestClass):
    def test_cast_param_to_float_lte_sql_query(self):
        qs1 = Number.objects.filter(decimal_num__lte=Decimal("1.1")).values(
            "decimal_num"
        )
        compiler = SQLCompiler(qs1.query, self.connection, "default")
        sql_compiled, params = compiler.as_sql()
        self.assertEqual(
            sql_compiled,
            "SELECT tests_number.decimal_num AS decimal_num FROM tests_number WHERE "
            + "tests_number.decimal_num <= %s",
        )
        self.assertEqual(params, (Decimal("1.1"),))

    def test_cast_param_to_float_for_int_field_query(self):
        qs1 = Number.objects.filter(num__lte=1.1).values("num")

        compiler = SQLCompiler(qs1.query, self.connection, "default")
        sql_compiled, params = compiler.as_sql()
        self.assertEqual(
            sql_compiled,
            "SELECT tests_number.num AS num FROM tests_number WHERE "
            + "tests_number.num <= %s",
        )
        self.assertEqual(params, (1,))

    def test_cast_param_to_float_for_foreign_key_field_query(self):
        qs1 = Number.objects.filter(item_id__exact="10").values("num")
        compiler = SQLCompiler(qs1.query, self.connection, "default")
        sql_compiled, params = compiler.as_sql()
        self.assertEqual(
            sql_compiled,
            "SELECT tests_number.num AS num FROM tests_number WHERE "
            + "tests_number.item_id = %s",
        )
        self.assertEqual(params, (10,))

    def test_cast_param_to_float_with_no_params_query(self):
        qs1 = Number.objects.filter(item_id__exact=F("num")).values("num")
        compiler = SQLCompiler(qs1.query, self.connection, "default")
        sql_compiled, params = compiler.as_sql()
        expected_sql = (
            "SELECT tests_number.num AS num FROM tests_number WHERE "
            + "tests_number.item_id = (tests_number.num)"
        )
        self.assertEqual(sql_compiled, expected_sql)
        self.assertEqual(params, ())

    def test_startswith_endswith_sql_query_with_startswith(self):
        qs1 = Author.objects.filter(name__startswith="abc").values("num")
        compiler = SQLCompiler(qs1.query, self.connection, "default")
        sql_compiled, params = compiler.as_sql()
        self.assertEqual(
            sql_compiled,
            "SELECT tests_author.num AS num FROM tests_author WHERE "
            + "REGEXP_CONTAINS(CAST(tests_author.name AS STRING), %s)",
        )
        self.assertEqual(params, ("^abc",))

    def test_startswith_endswith_sql_query_with_endswith(self):
        qs1 = Author.objects.filter(name__endswith="abc").values("num")
        compiler = SQLCompiler(qs1.query, self.connection, "default")
        sql_compiled, params = compiler.as_sql()
        self.assertEqual(
            sql_compiled,
            "SELECT tests_author.num AS num FROM tests_author WHERE "
            + "REGEXP_CONTAINS(CAST(tests_author.name AS STRING), %s)",
        )
        self.assertEqual(params, ("abc$",))

    def test_startswith_endswith_sql_query_case_insensitive(self):
        qs1 = Author.objects.filter(name__istartswith="abc").values("num")
        compiler = SQLCompiler(qs1.query, self.connection, "default")
        sql_compiled, params = compiler.as_sql()
        self.assertEqual(
            sql_compiled,
            "SELECT tests_author.num AS num FROM tests_author WHERE "
            + "REGEXP_CONTAINS(CAST(tests_author.name AS STRING), %s)",
        )
        self.assertEqual(params, ("(?i)^abc",))

    def test_startswith_endswith_sql_query_with_bileteral_transform(self):
        qs1 = Author.objects.filter(name__upper__startswith="abc").values("name")

        compiler = SQLCompiler(qs1.query, self.connection, "default")
        sql_compiled, params = compiler.as_sql()
        expected_sql = (
            "SELECT tests_author.name AS name FROM tests_author WHERE "
            + "REGEXP_CONTAINS(CAST(UPPER(tests_author.name) AS STRING), "
            + "REPLACE(REPLACE(REPLACE(CONCAT('^', (UPPER(%s))), "
            + '"\\\\", "\\\\\\\\"), "%%", r"\\%%"), "_", r"\\_"))'
        )
        self.assertEqual(sql_compiled, expected_sql)
        self.assertEqual(params, ("abc",))

    def test_startswith_endswith_case_insensitive_transform_sql_query(self):
        qs1 = Author.objects.filter(name__upper__istartswith="abc").values("name")

        compiler = SQLCompiler(qs1.query, self.connection, "default")
        sql_compiled, params = compiler.as_sql()
        expected_sql = (
            "SELECT tests_author.name AS name FROM tests_author WHERE "
            + "REGEXP_CONTAINS(CAST(UPPER(tests_author.name) AS STRING), "
            + "REPLACE(REPLACE(REPLACE(CONCAT('^(?i)', (UPPER(%s))), "
            + '"\\\\", "\\\\\\\\"), "%%", r"\\%%"), "_", r"\\_"))'
        )
        self.assertEqual(sql_compiled, expected_sql)
        self.assertEqual(params, ("abc",))

    def test_startswith_endswith_endswith_sql_query_with_transform(self):
        qs1 = Author.objects.filter(name__upper__endswith="abc").values("name")

        compiler = SQLCompiler(qs1.query, self.connection, "default")
        sql_compiled, params = compiler.as_sql()

        expected_sql = (
            "SELECT tests_author.name AS name FROM tests_author WHERE "
            + "REGEXP_CONTAINS(CAST(UPPER(tests_author.name) AS STRING), "
            + "REPLACE(REPLACE(REPLACE(CONCAT('', (UPPER(%s)), '$'), "
            + '"\\\\", "\\\\\\\\"), "%%", r"\\%%"), "_", r"\\_"))'
        )
        self.assertEqual(sql_compiled, expected_sql)
        self.assertEqual(params, ("abc",))

    def test_regex_sql_query_case_sensitive(self):
        qs1 = Author.objects.filter(name__regex="abc").values("num")
        compiler = SQLCompiler(qs1.query, self.connection, "default")
        sql_compiled, params = compiler.as_sql()
        self.assertEqual(
            sql_compiled,
            "SELECT tests_author.num AS num FROM tests_author WHERE "
            "REGEXP_CONTAINS(CAST(tests_author.name AS STRING), %s)",
        )
        self.assertEqual(params, ("abc",))

    def test_regex_sql_query_case_insensitive(self):
        qs1 = Author.objects.filter(name__iregex="abc").values("num")
        compiler = SQLCompiler(qs1.query, self.connection, "default")
        sql_compiled, params = compiler.as_sql()
        self.assertEqual(
            sql_compiled,
            "SELECT tests_author.num AS num FROM tests_author WHERE "
            "REGEXP_CONTAINS(CAST(tests_author.name AS STRING), %s)",
        )
        self.assertEqual(params, ("(?i)abc",))

    def test_regex_sql_query_case_sensitive_with_transform(self):
        qs1 = Author.objects.filter(name__upper__regex="abc").values("num")
        compiler = SQLCompiler(qs1.query, self.connection, "default")
        sql_compiled, params = compiler.as_sql()

        expected_sql = (
            "SELECT tests_author.num AS num FROM tests_author WHERE "
            + "REGEXP_CONTAINS(CAST(UPPER(tests_author.name) AS STRING), "
            + "(UPPER(%s)))"
        )
        self.assertEqual(sql_compiled, expected_sql)
        self.assertEqual(params, ("abc",))

    def test_regex_sql_query_case_insensitive_with_transform(self):
        qs1 = Author.objects.filter(name__upper__iregex="abc").values("num")
        compiler = SQLCompiler(qs1.query, self.connection, "default")
        sql_compiled, params = compiler.as_sql()

        expected_sql = (
            "SELECT tests_author.num AS num FROM tests_author WHERE "
            + "REGEXP_CONTAINS(CAST(UPPER(tests_author.name) AS STRING), "
            + "CONCAT('(?i)', (UPPER(%s))))"
        )
        self.assertEqual(sql_compiled, expected_sql)
        self.assertEqual(params, ("abc",))

    def test_contains_sql_query_case_insensitive(self):
        qs1 = Author.objects.filter(name__icontains="abc").values("num")
        compiler = SQLCompiler(qs1.query, self.connection, "default")
        sql_compiled, params = compiler.as_sql()
        self.assertEqual(
            sql_compiled,
            "SELECT tests_author.num AS num FROM tests_author WHERE "
            + "REGEXP_CONTAINS(CAST(tests_author.name AS STRING), %s)",
        )
        self.assertEqual(params, ("(?i)abc",))

    def test_contains_sql_query_case_sensitive(self):
        qs1 = Author.objects.filter(name__contains="abc").values("num")
        compiler = SQLCompiler(qs1.query, self.connection, "default")
        sql_compiled, params = compiler.as_sql()
        self.assertEqual(
            sql_compiled,
            "SELECT tests_author.num AS num FROM tests_author WHERE "
            + "REGEXP_CONTAINS(CAST(tests_author.name AS STRING), %s)",
        )
        self.assertEqual(params, ("abc",))

    def test_contains_sql_query_case_insensitive_transform(self):
        qs1 = Author.objects.filter(name__upper__icontains="abc").values("name")
        compiler = SQLCompiler(qs1.query, self.connection, "default")
        sql_compiled, params = compiler.as_sql()
        expected_sql = (
            "SELECT tests_author.name AS name FROM tests_author WHERE "
            + "REGEXP_CONTAINS(CAST(UPPER(tests_author.name) AS STRING), "
            + "REPLACE(REPLACE(REPLACE(CONCAT('(?i)', (UPPER(%s))), "
            + '"\\\\", "\\\\\\\\"), "%%", r"\\%%"), "_", r"\\_"))'
        )
        self.assertEqual(sql_compiled, expected_sql)
        self.assertEqual(params, ("abc",))

    def test_contains_sql_query_case_sensitive_transform(self):
        qs1 = Author.objects.filter(name__upper__contains="abc").values("name")
        compiler = SQLCompiler(qs1.query, self.connection, "default")
        sql_compiled, params = compiler.as_sql()
        expected_sql = (
            "SELECT tests_author.name AS name FROM tests_author WHERE "
            + "REGEXP_CONTAINS(CAST(UPPER(tests_author.name) AS STRING), "
            + 'REPLACE(REPLACE(REPLACE((UPPER(%s)), "\\\\", "\\\\\\\\"), '
            + '"%%", r"\\%%"), "_", r"\\_"))'
        )
        self.assertEqual(sql_compiled, expected_sql)
        self.assertEqual(params, ("abc",))

    def test_iexact_sql_query_case_insensitive(self):
        qs1 = Author.objects.filter(name__iexact="abc").values("num")
        compiler = SQLCompiler(qs1.query, self.connection, "default")
        sql_compiled, params = compiler.as_sql()

        self.assertEqual(
            sql_compiled,
            "SELECT tests_author.num AS num FROM tests_author WHERE "
            + "REGEXP_CONTAINS(CAST(tests_author.name AS STRING), %s)",
        )
        self.assertEqual(params, ("^(?i)abc$",))

    def test_iexact_sql_query_case_insensitive_function_transform(self):
        qs1 = Author.objects.filter(name__upper__iexact=F("last_name")).values("name")
        compiler = SQLCompiler(qs1.query, self.connection, "default")
        sql_compiled, params = compiler.as_sql()

        expected_sql = (
            "SELECT tests_author.name AS name FROM tests_author WHERE "
            + "REGEXP_CONTAINS((UPPER(tests_author.last_name)), "
            + "CONCAT('^(?i)', CAST(UPPER(tests_author.name) AS STRING), '$'))"
        )
        self.assertEqual(sql_compiled, expected_sql)
        self.assertEqual(params, ())

    def test_iexact_sql_query_case_insensitive_value_match(self):
        qs1 = Author.objects.filter(name__upper__iexact="abc").values("name")
        compiler = SQLCompiler(qs1.query, self.connection, "default")
        sql_compiled, params = compiler.as_sql()

        expected_sql = (
            "SELECT tests_author.name AS name FROM tests_author WHERE "
            + "REGEXP_CONTAINS((UPPER(CONCAT('^(?i)', "
            + "CAST(UPPER(tests_author.name) AS STRING), '$'))), %s)"
        )
        self.assertEqual(sql_compiled, expected_sql)
        self.assertEqual(params, ("abc",))

    def test_icontains_with_lhs_params(self):
        qs = (
            Author.objects.annotate(greeting=Concat(Value("User: "), "name"))
            .filter(greeting__icontains="john")
            .values("name")
        )
        compiler = SQLCompiler(qs.query, self.connection, "default")
        sql, params = compiler.as_sql()
        self.assertEqual(params, ("User: ", "", "", "(?i)john"))

    def test_iexact_with_lhs_params(self):
        qs = (
            Author.objects.annotate(greeting=Concat(Value("User: "), "name"))
            .filter(greeting__iexact="john")
            .values("name")
        )
        compiler = SQLCompiler(qs.query, self.connection, "default")
        sql, params = compiler.as_sql()
        self.assertEqual(params, ("User: ", "", "", "^(?i)john$"))

    def test_istartswith_with_lhs_params(self):
        qs = (
            Author.objects.annotate(greeting=Concat(Value("User: "), "name"))
            .filter(greeting__istartswith="john")
            .values("name")
        )
        compiler = SQLCompiler(qs.query, self.connection, "default")
        sql, params = compiler.as_sql()
        self.assertEqual(params, ("User: ", "", "", "(?i)^john"))

    def test_iendswith_with_lhs_params(self):
        qs = (
            Author.objects.annotate(greeting=Concat(Value("User: "), "name"))
            .filter(greeting__iendswith="john")
            .values("name")
        )
        compiler = SQLCompiler(qs.query, self.connection, "default")
        sql, params = compiler.as_sql()
        self.assertEqual(params, ("User: ", "", "", "(?i)john$"))

    def test_iregex_with_lhs_params(self):
        qs = (
            Author.objects.annotate(greeting=Concat(Value("User: "), "name"))
            .filter(greeting__iregex="^john")
            .values("name")
        )
        compiler = SQLCompiler(qs.query, self.connection, "default")
        sql, params = compiler.as_sql()
        self.assertEqual(params, ("User: ", "", "", "(?i)^john"))
