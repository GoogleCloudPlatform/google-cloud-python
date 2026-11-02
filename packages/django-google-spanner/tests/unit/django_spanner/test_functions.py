# Copyright 2021 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

from django.db.models import CharField, FloatField, Value
from django.db.models.functions import (
    Cast,
    Concat,
    Cot,
    Degrees,
    Left,
    Log,
    Ord,
    Pi,
    Radians,
    Right,
    StrIndex,
    Substr,
)

from django_spanner.compiler import SQLCompiler
from tests.unit.django_spanner.simple_test import SpannerSimpleTestClass

from .models import Author


class TestUtils(SpannerSimpleTestClass):
    def test_cast_with_max_length(self):
        """
        Tests cast field with max length.
        """
        q1 = Author.objects.values("name").annotate(
            name_as_prefix=Cast("name", output_field=CharField(max_length=10)),
        )
        compiler = SQLCompiler(q1.query, self.connection, "default")
        sql_query, params = compiler.query.as_sql(compiler, self.connection)
        self.assertEqual(
            sql_query,
            "SELECT tests_author.name AS name, SUBSTR(CAST(tests_author.name AS "
            + "STRING), 0, 10) AS name_as_prefix FROM tests_author",
        )
        self.assertEqual(params, ())

    def test_cast_without_max_length(self):
        """
        Tests cast field without max length.
        """
        q1 = Author.objects.values("num").annotate(
            num_as_float=Cast("num", output_field=FloatField()),
        )
        compiler = SQLCompiler(q1.query, self.connection, "default")
        sql_query, params = compiler.query.as_sql(compiler, self.connection)
        self.assertEqual(
            sql_query,
            "SELECT tests_author.num AS num, CAST(tests_author.num AS FLOAT64) "
            + "AS num_as_float FROM tests_author",
        )
        self.assertEqual(params, ())

    def test_concatpair(self):
        """
        Tests concatinating pair of columns.
        """
        q1 = Author.objects.values("name").annotate(
            full_name=Concat("name", Value(" "), "last_name", output_field=CharField()),
        )
        compiler = SQLCompiler(q1.query, self.connection, "default")
        sql_query, params = compiler.query.as_sql(compiler, self.connection)
        self.assertEqual(
            sql_query,
            "SELECT tests_author.name AS name, CONCAT(IFNULL(tests_author.name, %s), "
            + "IFNULL(CONCAT(IFNULL(%s, %s), IFNULL(tests_author.last_name, "
            + "%s)), %s)) AS full_name FROM tests_author",
        )
        self.assertEqual(params, ("", " ", "", "", ""))

    def test_cot(self):
        """
        Tests cot function on a column.
        """
        q1 = Author.objects.values("num").annotate(
            num_cot=Cot("num"),
        )
        compiler = SQLCompiler(q1.query, self.connection, "default")
        sql_query, params = compiler.query.as_sql(compiler, self.connection)
        self.assertEqual(
            sql_query,
            "SELECT tests_author.num AS num, (1 / TAN(tests_author.num)) AS num_cot "
            + "FROM tests_author",
        )
        self.assertEqual(params, ())

    def test_degrees(self):
        """
        Tests degrees function on a column.
        """
        q1 = Author.objects.values("num").annotate(
            num_degrees=Degrees("num"),
        )
        compiler = SQLCompiler(q1.query, self.connection, "default")
        sql_query, params = compiler.query.as_sql(compiler, self.connection)
        self.assertEqual(
            sql_query,
            "SELECT tests_author.num AS num, ((tests_author.num) * 180 / "
            + "3.141592653589793) AS num_degrees FROM tests_author",
        )
        self.assertEqual(params, ())

    def test_left(self):
        """
        Tests left function applied to a column.
        """
        q1 = Author.objects.values("num").annotate(
            first_initial=Left("name", 1),
        )
        compiler = SQLCompiler(q1.query, self.connection, "default")
        sql_query, params = compiler.query.as_sql(compiler, self.connection)
        self.assertEqual(
            sql_query,
            "SELECT tests_author.num AS num, SUBSTR(tests_author.name, %s, %s) AS "
            + "first_initial FROM tests_author",
        )
        self.assertEqual(params, (1, 1))

    def test_right(self):
        """
        Tests right function applied to a column.
        """
        q1 = Author.objects.values("num").annotate(
            last_letter=Right("name", 1),
        )
        compiler = SQLCompiler(q1.query, self.connection, "default")
        sql_query, params = compiler.query.as_sql(compiler, self.connection)
        self.assertEqual(
            sql_query,
            "SELECT tests_author.num AS num, SUBSTR(tests_author.name, (%s * %s), %s) "
            + "AS last_letter FROM tests_author",
        )
        self.assertEqual(params, (1, -1, 1))

    def test_log(self):
        """
        Tests log function applied to a column.
        """
        q1 = Author.objects.values("num").annotate(log=Log("num", Value(10)))

        compiler = SQLCompiler(q1.query, self.connection, "default")
        sql_query, params = compiler.query.as_sql(compiler, self.connection)
        self.assertEqual(
            sql_query,
            "SELECT tests_author.num AS num, LOG(%s, tests_author.num) AS log FROM "
            + "tests_author",
        )
        self.assertEqual(params, (10,))

    def test_ord(self):
        """
        Tests ord function applied to a column.
        """
        q1 = Author.objects.values("name").annotate(name_code_point=Ord("name"))

        compiler = SQLCompiler(q1.query, self.connection, "default")
        sql_query, params = compiler.query.as_sql(compiler, self.connection)
        self.assertEqual(
            sql_query,
            "SELECT tests_author.name AS name, TO_CODE_POINTS(tests_author.name)"
            + "[OFFSET(0)] AS name_code_point FROM tests_author",
        )
        self.assertEqual(params, ())

    def test_pi(self):
        """
        Tests pi function applied to a column.
        """
        q1 = Author.objects.filter(num=Pi()).values("num")

        compiler = SQLCompiler(q1.query, self.connection, "default")
        sql_query, params = compiler.query.as_sql(compiler, self.connection)
        expected_sql = (
            "SELECT tests_author.num AS num FROM tests_author WHERE tests_author.num "
            + "= (3.141592653589793)"
        )
        self.assertEqual(
            sql_query,
            expected_sql,
        )
        self.assertEqual(params, ())

    def test_radians(self):
        """
        Tests radians function applied to a column.
        """
        q1 = Author.objects.values("num").annotate(num_radians=Radians("num"))

        compiler = SQLCompiler(q1.query, self.connection, "default")
        sql_query, params = compiler.query.as_sql(compiler, self.connection)
        self.assertEqual(
            sql_query,
            "SELECT tests_author.num AS num, ((tests_author.num) * 3.141592653589793 "
            "/ 180) AS num_radians FROM tests_author",
        )
        self.assertEqual(params, ())

    def test_strindex(self):
        """
        Tests str index function applied to a column.
        """
        q1 = Author.objects.values("name").annotate(
            smith_index=StrIndex("name", Value("Smith"))
        )

        compiler = SQLCompiler(q1.query, self.connection, "default")
        sql_query, params = compiler.query.as_sql(compiler, self.connection)
        self.assertEqual(
            sql_query,
            "SELECT tests_author.name AS name, STRPOS(tests_author.name, %s) AS "
            + "smith_index FROM tests_author",
        )
        self.assertEqual(params, ("Smith",))

    def test_substr(self):
        """
        Tests substr function applied to a column.
        """
        q1 = Author.objects.values("name").annotate(name_prefix=Substr("name", 1, 5))

        compiler = SQLCompiler(q1.query, self.connection, "default")
        sql_query, params = compiler.query.as_sql(compiler, self.connection)
        self.assertEqual(
            sql_query,
            "SELECT tests_author.name AS name, SUBSTR(tests_author.name, %s, %s) AS "
            + "name_prefix FROM tests_author",
        )
        self.assertEqual(params, (1, 5))
