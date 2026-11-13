# Copyright 2021 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

from django.core.exceptions import EmptyResultSet
from django.db.models import F, Q, Subquery
from django.db.models.query import QuerySet
from django.db.models.sql import DeleteQuery, UpdateQuery
from django.db.utils import DatabaseError

from django_spanner.compiler import (
    SQLCompiler,
    SQLDeleteCompiler,
    SQLUpdateCompiler,
)
from tests.unit.django_spanner.simple_test import SpannerSimpleTestClass

from .models import Item, Number


class TestCompiler(SpannerSimpleTestClass):
    def test_unsupported_ordering_slicing_raises_db_error(self):
        """
        Tries limit/offset and order by in subqueries which are not supported
        by spanner.
        """
        qs1 = Number.objects.all()
        qs2 = Number.objects.all()
        msg = "LIMIT/OFFSET not allowed in subqueries of compound statements"
        with self.assertRaisesRegex(DatabaseError, msg):
            list(qs1.union(qs2[:10]))
        msg = "ORDER BY not allowed in subqueries of compound statements"
        with self.assertRaisesRegex(DatabaseError, msg):
            list(qs1.order_by("id").union(qs2))

    def test_get_combinator_sql_all_union_sql_generated(self):
        """
        Tries union sql generator.
        """

        qs1 = Number.objects.filter(num__lte=1).values("num")
        qs2 = Number.objects.filter(num__gte=8).values("num")
        qs4 = qs1.union(qs2)

        compiler = SQLCompiler(qs4.query, self.connection, "default")
        sql_compiled, params = compiler.get_combinator_sql("union", True)
        self.assertEqual(
            sql_compiled,
            [
                "SELECT tests_number.num AS num FROM tests_number WHERE "
                + "tests_number.num <= %s UNION ALL SELECT tests_number.num "
                + "AS num FROM tests_number WHERE tests_number.num >= %s"
            ],
        )
        self.assertEqual(params, [1, 8])

    def test_get_combinator_sql_distinct_union_sql_generated(self):
        """
        Tries union sql generator with distinct.
        """

        qs1 = Number.objects.filter(num__lte=1).values("num")
        qs2 = Number.objects.filter(num__gte=8).values("num")
        qs4 = qs1.union(qs2)

        compiler = SQLCompiler(qs4.query, self.connection, "default")
        sql_compiled, params = compiler.get_combinator_sql("union", False)
        self.assertEqual(
            sql_compiled,
            [
                "SELECT tests_number.num AS num FROM tests_number WHERE "
                + "tests_number.num <= %s UNION DISTINCT SELECT "
                + "tests_number.num AS num FROM tests_number WHERE "
                + "tests_number.num >= %s"
            ],
        )
        self.assertEqual(params, [1, 8])

    def test_get_combinator_sql_difference_all_sql_generated(self):
        """
        Tries difference sql generator.
        """
        qs1 = Number.objects.filter(num__lte=1).values("num")
        qs2 = Number.objects.filter(num__gte=8).values("num")
        qs4 = qs1.difference(qs2)

        compiler = SQLCompiler(qs4.query, self.connection, "default")
        sql_compiled, params = compiler.get_combinator_sql("difference", True)

        self.assertEqual(
            sql_compiled,
            [
                "SELECT tests_number.num AS num FROM tests_number WHERE "
                + "tests_number.num <= %s EXCEPT ALL SELECT tests_number.num "
                + "AS num FROM tests_number WHERE tests_number.num >= %s"
            ],
        )
        self.assertEqual(params, [1, 8])

    def test_get_combinator_sql_difference_distinct_sql_generated(self):
        """
        Tries difference sql generator with distinct.
        """
        qs1 = Number.objects.filter(num__lte=1).values("num")
        qs2 = Number.objects.filter(num__gte=8).values("num")
        qs4 = qs1.difference(qs2)

        compiler = SQLCompiler(qs4.query, self.connection, "default")
        sql_compiled, params = compiler.get_combinator_sql("difference", False)

        self.assertEqual(
            sql_compiled,
            [
                "SELECT tests_number.num AS num FROM tests_number WHERE "
                + "tests_number.num <= %s EXCEPT DISTINCT SELECT "
                + "tests_number.num AS num FROM tests_number WHERE "
                + "tests_number.num >= %s"
            ],
        )
        self.assertEqual(params, [1, 8])

    def test_get_combinator_sql_union_and_difference_query_together(self):
        """
        Tries sql generator with union of queryset with queryset of difference.
        """
        qs1 = Number.objects.filter(num__lte=1).values("num")
        qs2 = Number.objects.filter(num__gte=8).values("num")
        qs3 = Number.objects.filter(num__exact=10).values("num")
        qs4 = qs1.union(qs2.difference(qs3))

        compiler = SQLCompiler(qs4.query, self.connection, "default")
        sql_compiled, params = compiler.get_combinator_sql("union", False)
        self.assertEqual(
            sql_compiled,
            [
                "SELECT tests_number.num AS num FROM tests_number WHERE "
                + "tests_number.num <= %s UNION DISTINCT SELECT * FROM ("
                + "SELECT tests_number.num AS num FROM tests_number WHERE "
                + "tests_number.num >= %s EXCEPT DISTINCT "
                + "SELECT tests_number.num AS num FROM tests_number "
                + "WHERE tests_number.num = %s)"
            ],
        )
        self.assertEqual(params, [1, 8, 10])

    def test_get_combinator_sql_parentheses_in_compound_not_supported(self):
        """
        Tries sql generator with union of queryset with queryset of difference,
        adding support for parentheses in compound sql statement.
        """

        qs1 = Number.objects.filter(num__lte=1).values("num")
        qs2 = Number.objects.filter(num__gte=8).values("num")
        qs3 = Number.objects.filter(num__exact=10).values("num")
        qs4 = qs1.union(qs2.difference(qs3))

        compiler = SQLCompiler(qs4.query, self.connection, "default")
        compiler.connection.features.supports_parentheses_in_compound = False
        sql_compiled, params = compiler.get_combinator_sql("union", False)
        self.assertEqual(
            sql_compiled,
            [
                "SELECT tests_number.num AS num FROM tests_number WHERE "
                + "tests_number.num <= %s UNION DISTINCT SELECT * FROM ("
                + "SELECT tests_number.num AS num FROM tests_number WHERE "
                + "tests_number.num >= %s EXCEPT DISTINCT "
                + "SELECT tests_number.num AS num FROM tests_number "
                + "WHERE tests_number.num = %s)"
            ],
        )
        self.assertEqual(params, [1, 8, 10])

    def test_get_combinator_sql_empty_queryset_raises_exception(self):
        """
        Tries sql generator with empty queryset.
        """
        compiler = SQLCompiler(QuerySet().query, self.connection, "default")
        with self.assertRaises(EmptyResultSet):
            compiler.get_combinator_sql("union", False)

    def test_unqualified_delete_appends_dummy_where(self):
        """Test that unqualified DELETE statements automatically append WHERE 1=1."""
        delete_query = Number.objects.all().query.chain(DeleteQuery)
        compiler = SQLDeleteCompiler(delete_query, self.connection, "default")
        sql, _ = compiler.as_sql()
        self.assertEqual(sql, "DELETE FROM tests_number WHERE 1=1")

    def test_qualified_delete_preserves_where(self):
        """Test that qualified DELETE statements do not append extra WHERE 1=1."""
        delete_query = Number.objects.filter(num=1).query.chain(DeleteQuery)
        compiler = SQLDeleteCompiler(delete_query, self.connection, "default")
        sql, parameters = compiler.as_sql()
        self.assertEqual(sql, "DELETE FROM tests_number WHERE tests_number.num = %s")
        self.assertEqual(parameters, (1,))

    def test_unqualified_update_appends_dummy_where(self):
        """Test that unqualified UPDATE statements automatically append WHERE 1=1."""
        update_query = Number.objects.all().query.chain(UpdateQuery)
        update_query.add_update_values({"num": 5})
        compiler = SQLUpdateCompiler(update_query, self.connection, "default")
        sql, _ = compiler.as_sql()
        self.assertEqual(sql, "UPDATE tests_number SET num = %s WHERE 1=1")

    def test_qualified_update_preserves_where(self):
        """Test that qualified UPDATE statements do not append extra WHERE 1=1."""
        update_query = Number.objects.filter(num=1).query.chain(UpdateQuery)
        update_query.add_update_values({"num": 5})
        compiler = SQLUpdateCompiler(update_query, self.connection, "default")
        sql, parameters = compiler.as_sql()
        self.assertEqual(
            sql, "UPDATE tests_number SET num = %s WHERE tests_number.num = %s"
        )
        self.assertEqual(parameters, (5, 1))

    def test_full_result_set_delete_appends_dummy_where(self):
        """Test that DELETE raising FullResultSet automatically appends WHERE 1=1."""
        delete_query = Number.objects.filter(~Q(num__in=[])).query.chain(DeleteQuery)
        compiler = SQLDeleteCompiler(delete_query, self.connection, "default")
        sql, _ = compiler.as_sql()
        self.assertEqual(sql, "DELETE FROM tests_number WHERE 1=1")

    def test_full_result_set_update_appends_dummy_where(self):
        """Test that UPDATE raising FullResultSet automatically appends WHERE 1=1."""
        update_query = Number.objects.filter(~Q(num__in=[])).query.chain(UpdateQuery)
        update_query.add_update_values({"num": 5})
        compiler = SQLUpdateCompiler(update_query, self.connection, "default")
        sql, _ = compiler.as_sql()
        self.assertEqual(sql, "UPDATE tests_number SET num = %s WHERE 1=1")

    def test_joined_delete_does_not_duplicate_where(self):
        """Test that DELETE with joins/annotations retains single WHERE clause."""
        delete_query = Number.objects.annotate(item_name=F("item__name")).query.chain(
            DeleteQuery
        )
        compiler = SQLDeleteCompiler(delete_query, self.connection, "default")
        sql, _ = compiler.as_sql()
        self.assertIn(" WHERE ", sql)
        self.assertEqual(sql.count(" WHERE "), 1)
        self.assertNotIn("WHERE 1=1", sql)

    def test_update_without_values_returns_empty(self):
        """Test that UPDATE without update values compiles to empty string."""
        update_query = Number.objects.all().query.chain(UpdateQuery)
        compiler = SQLUpdateCompiler(update_query, self.connection, "default")
        sql, parameters = compiler.as_sql()
        self.assertEqual(sql, "")
        self.assertEqual(parameters, ())

    def test_select_does_not_append_dummy_where(self):
        """Test that unqualified SELECT statements do not append WHERE 1=1."""
        compiler = SQLCompiler(Number.objects.all().query, self.connection, "default")
        sql, _ = compiler.as_sql()
        self.assertTrue(sql.startswith("SELECT "))
        self.assertNotIn("WHERE", sql)

    def test_update_with_subquery_does_not_add_where_to_subquery(self):
        """Test that subqueries in UPDATE do not get dummy WHERE, but outer UPDATE does."""
        subquery = Item.objects.values("name")[:1]
        update_query = Number.objects.all().query.chain(UpdateQuery)
        update_query.add_update_values({"num": Subquery(subquery)})
        compiler = SQLUpdateCompiler(update_query, self.connection, "default")
        sql, _ = compiler.as_sql()
        self.assertIn(" WHERE 1=1", sql)
        self.assertEqual(sql.count(" WHERE "), 1)
        start_index = sql.index("(")
        end_index = sql.index(")")
        subquery_sql = sql[start_index:end_index]
        self.assertNotIn("WHERE", subquery_sql)

    def test_get_converters_deduplicates_jsonfield_from_db_value(self):
        from django.db.models import JSONField
        from django.db.models.expressions import Col
        from django.db.models.sql import Query

        from django_spanner.compiler import SQLCompiler
        from tests.unit.django_spanner.models import Number

        field = JSONField()
        field.set_attributes_from_name("value")
        expr = Col("tests_detail", field)
        query = Query(Number)
        compiler = SQLCompiler(query, self.connection, "default")
        converters = compiler.get_converters([expr])
        self.assertIn(0, converters)
        convs, _ = converters[0]
        self.assertIn(self.connection.ops.convert_jsonfield_value, convs)
        self.assertNotIn(field.from_db_value, convs)

        class TaggedJSONField(JSONField):
            def from_db_value(self, value, expression, connection):
                return value

        sub_field = TaggedJSONField()
        sub_field.set_attributes_from_name("value")
        sub_expr = Col("tests_detail", sub_field)
        sub_converters = compiler.get_converters([sub_expr])
        sub_convs, _ = sub_converters[0]
        self.assertIn(self.connection.ops.convert_jsonfield_value, sub_convs)
        self.assertIn(sub_field.from_db_value, sub_convs)
