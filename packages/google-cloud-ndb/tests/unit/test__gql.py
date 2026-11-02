# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime

import pytest

from google.cloud.ndb import _gql as gql_module
from google.cloud.ndb import exceptions, key, model
from google.cloud.ndb import query as query_module

GQL_QUERY = """
    SELECT prop1, prop2 FROM SomeKind WHERE prop3>5 and prop2='xxx'
    ORDER BY prop4, prop1 DESC LIMIT 10 OFFSET 5 HINT ORDER_FIRST
"""


class TestLiteral:
    @staticmethod
    def test_constructor():
        literal = gql_module.Literal("abc")
        assert literal.__dict__ == {"_value": "abc"}

    @staticmethod
    def test_Get():
        literal = gql_module.Literal("abc")
        assert literal.Get() == "abc"

    @staticmethod
    def test___repr__():
        literal = gql_module.Literal("abc")
        assert literal.__repr__() == "Literal('abc')"

    @staticmethod
    def test___eq__():
        literal = gql_module.Literal("abc")
        literal2 = gql_module.Literal("abc")
        literal3 = gql_module.Literal("xyz")
        assert literal.__eq__(literal2) is True
        assert literal.__eq__(literal3) is False
        assert literal.__eq__(42) is NotImplemented


class TestGQL:
    @staticmethod
    def test_constructor():
        gql = gql_module.GQL(GQL_QUERY)
        assert gql.kind() == "SomeKind"

    @staticmethod
    def test_constructor_with_namespace():
        gql = gql_module.GQL(GQL_QUERY, namespace="test-namespace")
        assert gql._namespace == "test-namespace"

    @staticmethod
    def test_constructor_bad_query():
        with pytest.raises(exceptions.BadQueryError):
            gql_module.GQL("BAD, BAD QUERY")

    @staticmethod
    def test_constructor_incomplete_query():
        with pytest.raises(exceptions.BadQueryError):
            gql_module.GQL("SELECT")

    @staticmethod
    def test_constructor_extra_query():
        with pytest.raises(exceptions.BadQueryError):
            gql_module.GQL("SELECT * FROM SomeKind; END")

    @staticmethod
    def test_constructor_empty_where():
        with pytest.raises(exceptions.BadQueryError):
            gql_module.GQL("SELECT * FROM SomeKind WHERE")

    @staticmethod
    def test_constructor_empty_where_condition():
        with pytest.raises(exceptions.BadQueryError):
            gql_module.GQL("SELECT * FROM SomeKind WHERE")

    @staticmethod
    def test_constructor_bad_where_condition():
        with pytest.raises(exceptions.BadQueryError):
            gql_module.GQL("SELECT * FROM SomeKind WHERE WE_ARE")

    @staticmethod
    def test_constructor_reserved_where_identifier():
        with pytest.raises(exceptions.BadQueryError):
            gql_module.GQL("SELECT * FROM SomeKind WHERE WHERE")

    @staticmethod
    def test_constructor_empty_where_condition_value():
        with pytest.raises(exceptions.BadQueryError):
            gql_module.GQL("SELECT * FROM SomeKind WHERE prop1=")

    @staticmethod
    def test_filters():
        Literal = gql_module.Literal
        gql = gql_module.GQL(GQL_QUERY)
        assert gql.filters() == {
            ("prop2", "="): [("nop", [Literal("xxx")])],
            ("prop3", ">"): [("nop", [Literal(5)])],
        }

    @staticmethod
    def test_hint():
        gql = gql_module.GQL("SELECT * FROM SomeKind HINT ORDER_FIRST")
        assert gql.hint() == "ORDER_FIRST"
        gql = gql_module.GQL("SELECT * FROM SomeKind HINT FILTER_FIRST")
        assert gql.hint() == "FILTER_FIRST"
        gql = gql_module.GQL("SELECT * FROM SomeKind HINT ANCESTOR_FIRST")
        assert gql.hint() == "ANCESTOR_FIRST"
        with pytest.raises(exceptions.BadQueryError):
            gql_module.GQL("SELECT * FROM SomeKind HINT TAKE_THE_HINT")

    @staticmethod
    def test_limit():
        gql = gql_module.GQL("SELECT * FROM SomeKind LIMIT 10")
        assert gql.limit() == 10
        gql = gql_module.GQL("SELECT * FROM SomeKind LIMIT 10, 5")
        assert gql.limit() == 5
        with pytest.raises(exceptions.BadQueryError):
            gql_module.GQL("SELECT * FROM SomeKind LIMIT 0")
        with pytest.raises(exceptions.BadQueryError):
            gql_module.GQL("SELECT * FROM SomeKind LIMIT -1")
        with pytest.raises(exceptions.BadQueryError):
            gql_module.GQL("SELECT * FROM SomeKind LIMIT -1, 10")
        with pytest.raises(exceptions.BadQueryError):
            gql_module.GQL("SELECT * FROM SomeKind LIMIT THE_SKY")

    @staticmethod
    def test_offset():
        gql = gql_module.GQL("SELECT * FROM SomeKind")
        assert gql.offset() == 0
        gql = gql_module.GQL("SELECT * FROM SomeKind OFFSET 10")
        assert gql.offset() == 10
        gql = gql_module.GQL("SELECT * FROM SomeKind LIMIT 10, 5")
        assert gql.offset() == 10
        with pytest.raises(exceptions.BadQueryError):
            gql_module.GQL("SELECT * FROM SomeKind OFFSET -1")
        with pytest.raises(exceptions.BadQueryError):
            gql_module.GQL("SELECT * FROM SomeKind LIMIT 5, 10 OFFSET 8")
        with pytest.raises(exceptions.BadQueryError):
            gql_module.GQL("SELECT * FROM SomeKind OFFSET ZERO")

    @staticmethod
    def test_orderings():
        gql = gql_module.GQL(GQL_QUERY)
        assert gql.orderings() == [("prop4", 1), ("prop1", 2)]

    @staticmethod
    def test_is_keys_only():
        gql = gql_module.GQL(GQL_QUERY)
        assert gql.is_keys_only() is False
        gql = gql_module.GQL("SELECT __key__ from SomeKind")
        assert gql.is_keys_only() is True

    @staticmethod
    def test_projection():
        gql = gql_module.GQL(GQL_QUERY)
        assert gql.projection() == ("prop1", "prop2")

    @staticmethod
    def test_is_distinct():
        gql = gql_module.GQL(GQL_QUERY)
        assert gql.is_distinct() is False
        gql = gql_module.GQL("SELECT DISTINCT prop1 from SomeKind")
        assert gql.is_distinct() is True

    @staticmethod
    def test_kind():
        gql = gql_module.GQL(GQL_QUERY)
        assert gql.kind() == "SomeKind"
        assert gql._entity == "SomeKind"

    @staticmethod
    def test_cast():
        gql = gql_module.GQL("SELECT * FROM SomeKind WHERE prop1=user('js')")
        assert gql.filters() == {("prop1", "="): [("user", [gql_module.Literal("js")])]}

    @staticmethod
    def test_in_list():
        Literal = gql_module.Literal
        gql = gql_module.GQL("SELECT * FROM SomeKind WHERE prop1 IN (1, 2, 3)")
        assert gql.filters() == {
            ("prop1", "IN"): [("list", [Literal(1), Literal(2), Literal(3)])]
        }

    @staticmethod
    def test_not_in_list():
        Literal = gql_module.Literal
        gql = gql_module.GQL("SELECT * FROM SomeKind WHERE prop1 NOT IN (1, 2, 3)")
        assert gql.filters() == {
            ("prop1", "NOT_IN"): [("list", [Literal(1), Literal(2), Literal(3)])]
        }

    @staticmethod
    def test_cast_list_no_in():
        with pytest.raises(exceptions.BadQueryError):
            gql_module.GQL("SELECT * FROM SomeKind WHERE prop1=(1, 2, 3)")

    @staticmethod
    def test_not_without_in():
        with pytest.raises(exceptions.BadQueryError):
            gql_module.GQL("SELECT * FROM SomeKind WHERE prop1 NOT=1")

    @staticmethod
    def test_reference():
        gql = gql_module.GQL("SELECT * FROM SomeKind WHERE prop1=:ref")
        assert gql.filters() == {("prop1", "="): [("nop", ["ref"])]}

    @staticmethod
    def test_ancestor_is():
        gql = gql_module.GQL("SELECT * FROM SomeKind WHERE ANCESTOR IS 'AnyKind'")
        assert gql.filters() == {(-1, "is"): [("nop", [gql_module.Literal("AnyKind")])]}

    @staticmethod
    def test_ancestor_multiple_ancestors():
        with pytest.raises(exceptions.BadQueryError):
            gql_module.GQL(
                (
                    "SELECT * FROM SomeKind WHERE ANCESTOR IS 'AnyKind' AND "
                    "ANCESTOR IS 'OtherKind'"
                )
            )

    @staticmethod
    def test_ancestor_no_is():
        with pytest.raises(exceptions.BadQueryError):
            gql_module.GQL("SELECT * FROM SomeKind WHERE ANCESTOR='OtherKind'")

    @staticmethod
    def test_is_no_ancestor():
        with pytest.raises(exceptions.BadQueryError):
            gql_module.GQL("SELECT * FROM SomeKind WHERE prop1 IS 'OtherKind'")

    @staticmethod
    def test_func():
        gql = gql_module.GQL("SELECT * FROM SomeKind WHERE prop1=key(:1)")
        assert gql.filters() == {("prop1", "="): [("key", [1])]}

    @staticmethod
    def test_null():
        gql = gql_module.GQL("SELECT * FROM SomeKind WHERE prop1=NULL")
        assert gql.filters() == {("prop1", "="): [("nop", [gql_module.Literal(None)])]}

    @staticmethod
    def test_true():
        gql = gql_module.GQL("SELECT * FROM SomeKind WHERE prop1=TRUE")
        assert gql.filters() == {("prop1", "="): [("nop", [gql_module.Literal(True)])]}

    @staticmethod
    def test_false():
        gql = gql_module.GQL("SELECT * FROM SomeKind WHERE prop1=FALSE")
        assert gql.filters() == {("prop1", "="): [("nop", [gql_module.Literal(False)])]}

    @staticmethod
    def test_float():
        gql = gql_module.GQL("SELECT * FROM SomeKind WHERE prop1=3.14")
        assert gql.filters() == {("prop1", "="): [("nop", [gql_module.Literal(3.14)])]}

    @staticmethod
    def test_quoted_identifier():
        gql = gql_module.GQL('SELECT * FROM SomeKind WHERE "prop1"=3.14')
        assert gql.filters() == {("prop1", "="): [("nop", [gql_module.Literal(3.14)])]}

    @staticmethod
    def test_order_by_ascending():
        gql = gql_module.GQL("SELECT * FROM SomeKind ORDER BY prop1 ASC")
        assert gql.orderings() == [("prop1", 1)]

    @staticmethod
    def test_order_by_no_arg():
        with pytest.raises(exceptions.BadQueryError):
            gql_module.GQL("SELECT * FROM SomeKind ORDER BY")

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_get_query():
        class SomeKind(model.Model):
            prop1 = model.StringProperty()
            prop2 = model.StringProperty()
            prop3 = model.IntegerProperty()
            prop4 = model.IntegerProperty()

        rep = (
            "Query(namespace='test-namespace', kind='SomeKind', filters=AND(FilterNode('prop2', '=', {}"
            "), FilterNode('prop3', '>', 5)), order_by=[PropertyOrder(name="
            "'prop4', reverse=False), PropertyOrder(name='prop1', "
            "reverse=True)], limit=10, offset=5, "
            "projection=['prop1', 'prop2'])"
        )
        gql = gql_module.GQL(GQL_QUERY, namespace="test-namespace")
        query = gql.get_query()
        compat_rep = "'xxx'"
        assert repr(query) == rep.format(compat_rep)

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_get_query_distinct():
        class SomeKind(model.Model):
            prop1 = model.StringProperty()

        gql = gql_module.GQL("SELECT DISTINCT prop1 FROM SomeKind")
        query = gql.get_query()
        assert query.distinct_on == ("prop1",)

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_get_query_no_kind():
        class SomeKind(model.Model):
            prop1 = model.StringProperty()

        gql = gql_module.GQL("SELECT *")
        query = gql.get_query()
        assert query.kind is None

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_get_query_in():
        class SomeKind(model.Model):
            prop1 = model.IntegerProperty()

        gql = gql_module.GQL("SELECT prop1 FROM SomeKind WHERE prop1 IN (1, 2, 3)")
        query = gql.get_query()
        assert query.filters == query_module.OR(
            query_module.FilterNode("prop1", "=", 1),
            query_module.FilterNode("prop1", "=", 2),
            query_module.FilterNode("prop1", "=", 3),
        )

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_get_query_not_in():
        class SomeKind(model.Model):
            prop1 = model.IntegerProperty()

        gql = gql_module.GQL("SELECT prop1 FROM SomeKind WHERE prop1 NOT IN (1, 2)")
        query = gql.get_query()
        assert query.filters == query_module.FilterNode("prop1", "not_in", [1, 2])

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_get_query_in_parameterized():
        class SomeKind(model.Model):
            prop1 = model.StringProperty()

        gql = gql_module.GQL("SELECT prop1 FROM SomeKind WHERE prop1 IN (:1, :2, :3)")
        query = gql.get_query()
        assert "'in'," in str(query.filters)

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_get_query_not_in_parameterized():
        class SomeKind(model.Model):
            prop1 = model.StringProperty()

        gql = gql_module.GQL(
            "SELECT prop1 FROM SomeKind WHERE prop1 NOT IN (:1, :2, :3)"
        )
        query = gql.get_query()
        assert "'not_in'," in str(query.filters)

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_get_query_keys_only():
        class SomeKind(model.Model):
            prop1 = model.StringProperty()

        gql = gql_module.GQL("SELECT __key__ FROM SomeKind WHERE prop1='a'")
        query = gql.get_query()
        assert query.keys_only is True
        assert "keys_only=True" in query.__repr__()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_get_query_date():
        class SomeKind(model.Model):
            prop1 = model.DateProperty()

        gql = gql_module.GQL(
            "SELECT prop1 FROM SomeKind WHERE prop1 = Date(2020, 3, 26)"
        )
        query = gql.get_query()
        assert query.filters == query_module.FilterNode(
            "prop1", "=", datetime.datetime(2020, 3, 26, 0, 0, 0)
        )

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_get_query_date_one_parameter():
        class SomeKind(model.Model):
            prop1 = model.DateProperty()

        gql = gql_module.GQL(
            "SELECT prop1 FROM SomeKind WHERE prop1 = Date('2020-03-26')"
        )
        query = gql.get_query()
        assert query.filters == query_module.FilterNode(
            "prop1", "=", datetime.datetime(2020, 3, 26, 0, 0, 0)
        )

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_get_query_date_parameterized():
        class SomeKind(model.Model):
            prop1 = model.DateProperty()

        gql = gql_module.GQL("SELECT prop1 FROM SomeKind WHERE prop1 = Date(:1)")
        query = gql.get_query()
        assert "'date'" in str(query.filters)

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_get_query_date_one_parameter_bad_date():
        class SomeKind(model.Model):
            prop1 = model.DateProperty()

        gql = gql_module.GQL(
            "SELECT prop1 FROM SomeKind WHERE prop1 = Date('not a date')"
        )
        with pytest.raises(exceptions.BadQueryError):
            gql.get_query()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_get_query_date_one_parameter_bad_type():
        class SomeKind(model.Model):
            prop1 = model.DateProperty()

        gql = gql_module.GQL("SELECT prop1 FROM SomeKind WHERE prop1 = Date(42)")
        with pytest.raises(exceptions.BadQueryError):
            gql.get_query()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_get_query_date_too_many_values():
        class SomeKind(model.Model):
            prop1 = model.DateProperty()

        gql = gql_module.GQL(
            "SELECT prop1 FROM SomeKind WHERE prop1 = Date(1, 2, 3, 4)"
        )
        with pytest.raises(exceptions.BadQueryError):
            gql.get_query()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_get_query_date_bad_values():
        class SomeKind(model.Model):
            prop1 = model.DateProperty()

        gql = gql_module.GQL(
            "SELECT prop1 FROM SomeKind WHERE prop1 = Date(100, 200, 300)"
        )
        with pytest.raises(exceptions.BadQueryError):
            gql.get_query()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_get_query_datetime():
        class SomeKind(model.Model):
            prop1 = model.DateTimeProperty()

        gql = gql_module.GQL(
            "SELECT prop1 FROM SomeKind WHERE prop1 = DateTime(2020, 3, 26,12, 45, 5)"
        )
        query = gql.get_query()
        assert query.filters == query_module.FilterNode(
            "prop1", "=", datetime.datetime(2020, 3, 26, 12, 45, 5)
        )

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_get_query_datetime_ome_parameter():
        class SomeKind(model.Model):
            prop1 = model.DateTimeProperty()

        gql = gql_module.GQL(
            "SELECT prop1 FROM SomeKind WHERE prop1 = DateTime('2020-03-26 12:45:05')"
        )
        query = gql.get_query()
        assert query.filters == query_module.FilterNode(
            "prop1", "=", datetime.datetime(2020, 3, 26, 12, 45, 5)
        )

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_get_query_datetime_parameterized():
        class SomeKind(model.Model):
            prop1 = model.DateTimeProperty()

        gql = gql_module.GQL("SELECT prop1 FROM SomeKind WHERE prop1 = DateTime(:1)")
        query = gql.get_query()
        assert "'datetime'" in str(query.filters)

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_get_query_datetime_one_parameter_bad_date():
        class SomeKind(model.Model):
            prop1 = model.DateTimeProperty()

        gql = gql_module.GQL(
            "SELECT prop1 FROM SomeKind WHERE prop1 = DateTime('not a date')"
        )
        with pytest.raises(exceptions.BadQueryError):
            gql.get_query()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_get_query_datetime_one_parameter_bad_type():
        class SomeKind(model.Model):
            prop1 = model.DateTimeProperty()

        gql = gql_module.GQL("SELECT prop1 FROM SomeKind WHERE prop1 = DateTime(42)")
        with pytest.raises(exceptions.BadQueryError):
            gql.get_query()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_get_query_datetime_bad_values():
        class SomeKind(model.Model):
            prop1 = model.DateTimeProperty()

        gql = gql_module.GQL(
            "SELECT prop1 FROM SomeKind WHERE prop1 = DateTime(100, 200, 300)"
        )
        with pytest.raises(exceptions.BadQueryError):
            gql.get_query()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_get_query_time():
        class SomeKind(model.Model):
            prop1 = model.TimeProperty()

        gql = gql_module.GQL("SELECT prop1 FROM SomeKind WHERE prop1 = Time(12, 45, 5)")
        query = gql.get_query()
        assert query.filters == query_module.FilterNode(
            "prop1", "=", datetime.datetime(1970, 1, 1, 12, 45, 5)
        )

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_get_query_time_one_parameter():
        class SomeKind(model.Model):
            prop1 = model.TimeProperty()

        gql = gql_module.GQL(
            "SELECT prop1 FROM SomeKind WHERE prop1 = Time('12:45:05')"
        )
        query = gql.get_query()
        assert query.filters == query_module.FilterNode(
            "prop1", "=", datetime.datetime(1970, 1, 1, 12, 45, 5)
        )

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_get_query_time_one_parameter_int():
        class SomeKind(model.Model):
            prop1 = model.TimeProperty()

        gql = gql_module.GQL("SELECT prop1 FROM SomeKind WHERE prop1 = Time(12)")
        query = gql.get_query()
        assert query.filters == query_module.FilterNode(
            "prop1", "=", datetime.datetime(1970, 1, 1, 12)
        )

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_get_query_time_parameterized():
        class SomeKind(model.Model):
            prop1 = model.TimeProperty()

        gql = gql_module.GQL("SELECT prop1 FROM SomeKind WHERE prop1 = Time(:1)")
        query = gql.get_query()
        assert "'time'" in str(query.filters)

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_get_query_time_one_parameter_bad_time():
        class SomeKind(model.Model):
            prop1 = model.TimeProperty()

        gql = gql_module.GQL(
            "SELECT prop1 FROM SomeKind WHERE prop1 = Time('not a time')"
        )
        with pytest.raises(exceptions.BadQueryError):
            gql.get_query()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_get_query_time_one_parameter_bad_type():
        class SomeKind(model.Model):
            prop1 = model.TimeProperty()

        gql = gql_module.GQL("SELECT prop1 FROM SomeKind WHERE prop1 = Time(3.141592)")
        with pytest.raises(exceptions.BadQueryError):
            gql.get_query()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_get_query_time_too_many_values():
        class SomeKind(model.Model):
            prop1 = model.TimeProperty()

        gql = gql_module.GQL(
            "SELECT prop1 FROM SomeKind WHERE prop1 = Time(1, 2, 3, 4)"
        )
        with pytest.raises(exceptions.BadQueryError):
            gql.get_query()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_get_query_time_bad_values():
        class SomeKind(model.Model):
            prop1 = model.TimeProperty()

        gql = gql_module.GQL(
            "SELECT prop1 FROM SomeKind WHERE prop1 = Time(100, 200, 300)"
        )
        with pytest.raises(exceptions.BadQueryError):
            gql.get_query()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_get_query_geopt():
        class SomeKind(model.Model):
            prop1 = model.GeoPtProperty()

        gql = gql_module.GQL(
            "SELECT prop1 FROM SomeKind WHERE prop1 = GeoPt(20.67, -100.32)"
        )
        query = gql.get_query()
        assert query.filters == query_module.FilterNode(
            "prop1", "=", model.GeoPt(20.67, -100.32)
        )

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_get_query_geopt_parameterized():
        class SomeKind(model.Model):
            prop1 = model.GeoPtProperty()

        gql = gql_module.GQL("SELECT prop1 FROM SomeKind WHERE prop1 = GeoPt(:1)")
        query = gql.get_query()
        assert "'geopt'" in str(query.filters)

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_get_query_geopt_too_many_values():
        class SomeKind(model.Model):
            prop1 = model.GeoPtProperty()

        gql = gql_module.GQL(
            "SELECT prop1 FROM SomeKind WHERE prop1 = GeoPt(20.67,-100.32, 1.5)"
        )
        with pytest.raises(exceptions.BadQueryError):
            gql.get_query()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_get_query_key():
        class SomeKind(model.Model):
            prop1 = model.KeyProperty()

        gql = gql_module.GQL(
            "SELECT prop1 FROM SomeKind WHERE prop1 = Key('parent', 'c', 'child', 42)"
        )
        query = gql.get_query()
        assert query.filters == query_module.FilterNode(
            "prop1", "=", key.Key("parent", "c", "child", 42)
        )

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_get_query_key_parameterized():
        class SomeKind(model.Model):
            prop1 = model.KeyProperty()

        gql = gql_module.GQL("SELECT prop1 FROM SomeKind WHERE prop1 = Key(:1)")
        query = gql.get_query()
        assert "'key'" in str(query.filters)

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_get_query_key_odd_values():
        class SomeKind(model.Model):
            prop1 = model.KeyProperty()

        gql = gql_module.GQL(
            "SELECT prop1 FROM SomeKind WHERE prop1 = Key(100, 200, 300)"
        )
        with pytest.raises(exceptions.BadQueryError):
            gql.get_query()


class TestNotImplementedFUNCTIONS:
    @staticmethod
    def test_user():
        with pytest.raises(NotImplementedError):
            gql_module.FUNCTIONS["user"]("any arg")

    @staticmethod
    def test_nop():
        with pytest.raises(NotImplementedError):
            gql_module.FUNCTIONS["nop"]("any arg")

    @staticmethod
    def test_time_2_args_and_invalid():
        import datetime

        assert gql_module._time_function([10, 30]) == datetime.time(10, 30)
        with pytest.raises(exceptions.BadQueryError):
            gql_module._time_function([])

    @staticmethod
    def test_ancestor_condition_not_is():
        gql = gql_module.GQL("SELECT * FROM Kind")
        with pytest.raises(ValueError, match="condition must be 'is'"):
            gql._AddProcessedParameterFilter("ancestor", "!=", "nop", ["param"])
