# Copyright 2025 Google LLC All rights reserved.
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

import datetime
import math

import mock
import pytest

import google.cloud.firestore_v1.pipeline_expressions as expr
from google.cloud.firestore_v1 import _helpers
from google.cloud.firestore_v1._helpers import GeoPoint
from google.cloud.firestore_v1.pipeline_expressions import (
    BooleanExpression,
    Constant,
    Expression,
    Field,
    Ordering,
)
from google.cloud.firestore_v1.types import document as document_pb
from google.cloud.firestore_v1.types import query as query_pb
from google.cloud.firestore_v1.types.document import Value
from google.cloud.firestore_v1.vector import Vector


@pytest.fixture
def mock_client():
    client = mock.Mock(spec=["_database_string", "collection"])
    client._database_string = "projects/p/databases/d"
    return client


class TestOrdering:
    @pytest.mark.parametrize(
        "direction_arg,expected_direction",
        [
            ("ASCENDING", Ordering.Direction.ASCENDING),
            ("DESCENDING", Ordering.Direction.DESCENDING),
            ("ascending", Ordering.Direction.ASCENDING),
            ("descending", Ordering.Direction.DESCENDING),
            (Ordering.Direction.ASCENDING, Ordering.Direction.ASCENDING),
            (Ordering.Direction.DESCENDING, Ordering.Direction.DESCENDING),
        ],
    )
    def test_ctor(self, direction_arg, expected_direction):
        instance = Ordering("field1", direction_arg)
        assert isinstance(instance.expr, Field)
        assert instance.expr.path == "field1"
        assert instance.order_dir == expected_direction

    def test_repr(self):
        field_expr = Field.of("field1")
        instance = Ordering(field_expr, "ASCENDING")
        repr_str = repr(instance)
        assert repr_str == "Field.of('field1').ascending()"

        instance = Ordering(field_expr, "DESCENDING")
        repr_str = repr(instance)
        assert repr_str == "Field.of('field1').descending()"

    def test_to_pb(self):
        field_expr = Field.of("field1")
        instance = Ordering(field_expr, "ASCENDING")
        result = instance._to_pb()
        assert result.map_value.fields["expression"].field_reference_value == "field1"
        assert result.map_value.fields["direction"].string_value == "ascending"

        instance = Ordering(field_expr, "DESCENDING")
        result = instance._to_pb()
        assert result.map_value.fields["expression"].field_reference_value == "field1"
        assert result.map_value.fields["direction"].string_value == "descending"


class TestConstant:
    @pytest.mark.parametrize(
        "input_val, to_pb_val",
        [
            ("test", Value(string_value="test")),
            ("", Value(string_value="")),
            (10, Value(integer_value=10)),
            (0, Value(integer_value=0)),
            (10.0, Value(double_value=10)),
            (0.0, Value(double_value=0)),
            (True, Value(boolean_value=True)),
            (b"test", Value(bytes_value=b"test")),
            (None, Value(null_value=0)),
            (
                datetime.datetime(2025, 5, 12),
                Value(timestamp_value={"seconds": 1747008000}),
            ),
            (GeoPoint(1, 2), Value(geo_point_value={"latitude": 1, "longitude": 2})),
            (
                Vector([1.0, 2.0]),
                Value(
                    map_value={
                        "fields": {
                            "__type__": Value(string_value="__vector__"),
                            "value": Value(
                                array_value={
                                    "values": [Value(double_value=v) for v in [1, 2]],
                                }
                            ),
                        }
                    }
                ),
            ),
        ],
    )
    def test_to_pb(self, input_val, to_pb_val):
        instance = Constant.of(input_val)
        assert instance._to_pb() == to_pb_val

    @pytest.mark.parametrize("input", [float("nan"), math.nan])
    def test_nan_to_pb(self, input):
        instance = Constant.of(input)
        assert repr(instance) == "Constant.of(math.nan)"
        pb_val = instance._to_pb()
        assert math.isnan(pb_val.double_value)

    @pytest.mark.parametrize(
        "input_val,expected",
        [
            ("test", "Constant.of('test')"),
            ("", "Constant.of('')"),
            (10, "Constant.of(10)"),
            (0, "Constant.of(0)"),
            (10.0, "Constant.of(10.0)"),
            (0.0, "Constant.of(0.0)"),
            (True, "Constant.of(True)"),
            (b"test", "Constant.of(b'test')"),
            (None, "Constant.of(None)"),
            (
                datetime.datetime(2025, 5, 12),
                "Constant.of(datetime.datetime(2025, 5, 12, 0, 0))",
            ),
            (GeoPoint(1, 2), "Constant.of(GeoPoint(latitude=1, longitude=2))"),
            ([1, 2, 3], "Constant.of([1, 2, 3])"),
            ({"a": "b"}, "Constant.of({'a': 'b'})"),
            (Vector([1.0, 2.0]), "Constant.of(Vector<1.0, 2.0>)"),
        ],
    )
    def test_repr(self, input_val, expected):
        instance = Constant.of(input_val)
        repr_string = repr(instance)
        assert repr_string == expected

    @pytest.mark.parametrize(
        "first,second,expected",
        [
            (Constant.of(1), Constant.of(2), False),
            (Constant.of(1), Constant.of(1), True),
            (Constant.of(1), 1, True),
            (Constant.of(1), 2, False),
            (Constant.of("1"), 1, False),
            (Constant.of("1"), "1", True),
            (Constant.of(None), Constant.of(0), False),
            (Constant.of(None), Constant.of(None), True),
            (Constant.of([1, 2, 3]), Constant.of([1, 2, 3]), True),
            (Constant.of([1, 2, 3]), Constant.of([1, 2]), False),
            (Constant.of([1, 2, 3]), [1, 2, 3], True),
            (Constant.of([1, 2, 3]), object(), False),
        ],
    )
    def test_equality(self, first, second, expected):
        assert (first == second) is expected


class TestSelectable:
    """
    contains tests for each Expression class that derives from Selectable
    """

    def test_ctor(self):
        """
        Base class should be abstract
        """
        with pytest.raises(TypeError):
            expr.Selectable()

    def test_value_from_selectables(self):
        selectable_list = [
            Field.of("field1"),
            Field.of("field2").as_("alias2"),
        ]
        result = expr.Selectable._value_from_selectables(*selectable_list)
        assert len(result.map_value.fields) == 2
        assert result.map_value.fields["field1"].field_reference_value == "field1"
        assert result.map_value.fields["alias2"].field_reference_value == "field2"

    @pytest.mark.parametrize(
        "first,second,expected",
        [
            (Field.of("field1"), Field.of("field1"), True),
            (Field.of("field1"), Field.of("field2"), False),
            (Field.of(None), object(), False),
            (Field.of("f").as_("a"), Field.of("f").as_("a"), True),
            (Field.of("one").as_("a"), Field.of("two").as_("a"), False),
            (Field.of("f").as_("one"), Field.of("f").as_("two"), False),
            (Field.of("field"), Field.of("field").as_("alias"), False),
            (Field.of("field").as_("alias"), Field.of("field"), False),
        ],
    )
    def test_equality(self, first, second, expected):
        assert (first == second) is expected

    class TestField:
        def test_repr(self):
            instance = Field.of("field1")
            repr_string = repr(instance)
            assert repr_string == "Field.of('field1')"

        def test_of(self):
            instance = Field.of("field1")
            assert instance.path == "field1"

        def test_to_pb(self):
            instance = Field.of("field1")
            result = instance._to_pb()
            assert result.field_reference_value == "field1"

        def test_to_map(self):
            instance = Field.of("field1")
            result = instance._to_map()
            assert result[0] == "field1"
            assert result[1] == Value(field_reference_value="field1")

    class TestAliasedExpression:
        def test_repr(self):
            instance = Field.of("field1").as_("alias1")
            assert repr(instance) == "Field.of('field1').as_('alias1')"

        def test_ctor(self):
            arg = Field.of("field1")
            alias = "alias1"
            instance = expr.AliasedExpression(arg, alias)
            assert instance.expr == arg
            assert instance.alias == alias

        def test_to_pb(self):
            arg = Field.of("field1")
            alias = "alias1"
            instance = expr.AliasedExpression(arg, alias)
            result = instance._to_pb()
            assert result.map_value.fields.get("alias1") == arg._to_pb()

        def test_to_map(self):
            instance = Field.of("field1").as_("alias1")
            result = instance._to_map()
            assert result[0] == "alias1"
            assert result[1] == Value(field_reference_value="field1")

        def test_chaining_aliases(self):
            with pytest.raises(
                TypeError, match="Cannot call as_\\(\\) on an AliasedExpression"
            ):
                Field.of("field1").as_("alias1").as_("alias2")

        def test_expr_method_on_aliased_raises_error(self):
            with pytest.raises(
                TypeError, match="Cannot call 'add' on AliasedExpression"
            ):
                Field.of("field1").as_("alias1").add(5)

        def test_static_expr_method_on_aliased_raises_error(self):
            with pytest.raises(
                TypeError, match="Cannot call 'add' on AliasedExpression"
            ):
                expr.Expression.add(Field.of("field1").as_("alias1"), 5)


class TestBooleanExpression:
    def test__from_query_filter_pb_composite_filter_or(self, mock_client):
        """
        test composite OR filters

        should create an or statement, made up of ands checking of existance
        of relevant fields
        """
        filter1_pb = query_pb.StructuredQuery.FieldFilter(
            field=query_pb.StructuredQuery.FieldReference(field_path="field1"),
            op=query_pb.StructuredQuery.FieldFilter.Operator.EQUAL,
            value=_helpers.encode_value("val1"),
        )
        filter2_pb = query_pb.StructuredQuery.UnaryFilter(
            field=query_pb.StructuredQuery.FieldReference(field_path="field2"),
            op=query_pb.StructuredQuery.UnaryFilter.Operator.IS_NULL,
        )

        composite_pb = query_pb.StructuredQuery.CompositeFilter(
            op=query_pb.StructuredQuery.CompositeFilter.Operator.OR,
            filters=[
                query_pb.StructuredQuery.Filter(field_filter=filter1_pb),
                query_pb.StructuredQuery.Filter(unary_filter=filter2_pb),
            ],
        )
        wrapped_filter_pb = query_pb.StructuredQuery.Filter(
            composite_filter=composite_pb
        )

        result = BooleanExpression._from_query_filter_pb(wrapped_filter_pb, mock_client)

        # should include existance checks
        field1 = Field.of("field1")
        field2 = Field.of("field2")
        expected_cond1 = expr.And(field1.exists(), field1.equal(Constant("val1")))
        expected_cond2 = expr.And(field2.exists(), field2.equal(None))
        expected = expr.Or(expected_cond1, expected_cond2)

        assert repr(result) == repr(expected)

    def test__from_query_filter_pb_composite_filter_and(self, mock_client):
        """
        test composite AND filters

        should create an and statement, made up of ands checking of existance of relevant fields
        """
        filter1_pb = query_pb.StructuredQuery.FieldFilter(
            field=query_pb.StructuredQuery.FieldReference(field_path="field1"),
            op=query_pb.StructuredQuery.FieldFilter.Operator.GREATER_THAN,
            value=_helpers.encode_value(100),
        )
        filter2_pb = query_pb.StructuredQuery.FieldFilter(
            field=query_pb.StructuredQuery.FieldReference(field_path="field2"),
            op=query_pb.StructuredQuery.FieldFilter.Operator.LESS_THAN,
            value=_helpers.encode_value(200),
        )

        composite_pb = query_pb.StructuredQuery.CompositeFilter(
            op=query_pb.StructuredQuery.CompositeFilter.Operator.AND,
            filters=[
                query_pb.StructuredQuery.Filter(field_filter=filter1_pb),
                query_pb.StructuredQuery.Filter(field_filter=filter2_pb),
            ],
        )
        wrapped_filter_pb = query_pb.StructuredQuery.Filter(
            composite_filter=composite_pb
        )

        result = BooleanExpression._from_query_filter_pb(wrapped_filter_pb, mock_client)

        # should include existance checks
        field1 = Field.of("field1")
        field2 = Field.of("field2")
        expected_cond1 = expr.And(field1.exists(), field1.greater_than(Constant(100)))
        expected_cond2 = expr.And(field2.exists(), field2.less_than(Constant(200)))
        expected = expr.And(expected_cond1, expected_cond2)
        assert repr(result) == repr(expected)

    def test__from_query_filter_pb_composite_filter_nested(self, mock_client):
        """
        test composite filter with complex nested checks
        """
        # OR (field1 == "val1", AND(field2 > 10, field3 IS NOT NULL))
        filter1_pb = query_pb.StructuredQuery.FieldFilter(
            field=query_pb.StructuredQuery.FieldReference(field_path="field1"),
            op=query_pb.StructuredQuery.FieldFilter.Operator.EQUAL,
            value=_helpers.encode_value("val1"),
        )
        filter2_pb = query_pb.StructuredQuery.FieldFilter(
            field=query_pb.StructuredQuery.FieldReference(field_path="field2"),
            op=query_pb.StructuredQuery.FieldFilter.Operator.GREATER_THAN,
            value=_helpers.encode_value(10),
        )
        filter3_pb = query_pb.StructuredQuery.UnaryFilter(
            field=query_pb.StructuredQuery.FieldReference(field_path="field3"),
            op=query_pb.StructuredQuery.UnaryFilter.Operator.IS_NOT_NULL,
        )
        inner_and_pb = query_pb.StructuredQuery.CompositeFilter(
            op=query_pb.StructuredQuery.CompositeFilter.Operator.AND,
            filters=[
                query_pb.StructuredQuery.Filter(field_filter=filter2_pb),
                query_pb.StructuredQuery.Filter(unary_filter=filter3_pb),
            ],
        )
        outer_or_pb = query_pb.StructuredQuery.CompositeFilter(
            op=query_pb.StructuredQuery.CompositeFilter.Operator.OR,
            filters=[
                query_pb.StructuredQuery.Filter(field_filter=filter1_pb),
                query_pb.StructuredQuery.Filter(composite_filter=inner_and_pb),
            ],
        )
        wrapped_filter_pb = query_pb.StructuredQuery.Filter(
            composite_filter=outer_or_pb
        )

        result = BooleanExpression._from_query_filter_pb(wrapped_filter_pb, mock_client)

        field1 = Field.of("field1")
        field2 = Field.of("field2")
        field3 = Field.of("field3")
        expected_cond1 = expr.And(field1.exists(), field1.equal(Constant("val1")))
        expected_cond2 = expr.And(field2.exists(), field2.greater_than(Constant(10)))
        expected_cond3 = expr.And(field3.exists(), expr.Not(field3.equal(None)))
        expected_inner_and = expr.And(expected_cond2, expected_cond3)
        expected_outer_or = expr.Or(expected_cond1, expected_inner_and)

        assert repr(result) == repr(expected_outer_or)

    def test__from_query_filter_pb_composite_filter_unknown_op(self, mock_client):
        """
        check composite filter with unsupported operator type
        """
        filter1_pb = query_pb.StructuredQuery.FieldFilter(
            field=query_pb.StructuredQuery.FieldReference(field_path="field1"),
            op=query_pb.StructuredQuery.FieldFilter.Operator.EQUAL,
            value=_helpers.encode_value("val1"),
        )
        composite_pb = query_pb.StructuredQuery.CompositeFilter(
            op=query_pb.StructuredQuery.CompositeFilter.Operator.OPERATOR_UNSPECIFIED,
            filters=[query_pb.StructuredQuery.Filter(field_filter=filter1_pb)],
        )
        wrapped_filter_pb = query_pb.StructuredQuery.Filter(
            composite_filter=composite_pb
        )

        with pytest.raises(TypeError, match="Unexpected CompositeFilter operator type"):
            BooleanExpression._from_query_filter_pb(wrapped_filter_pb, mock_client)

    @pytest.mark.parametrize(
        "op_enum, expected_expr_func",
        [
            (
                query_pb.StructuredQuery.UnaryFilter.Operator.IS_NAN,
                lambda x: x.equal(float("nan")),
            ),
            (
                query_pb.StructuredQuery.UnaryFilter.Operator.IS_NOT_NAN,
                lambda x: expr.Not(x.equal(float("nan"))),
            ),
            (
                query_pb.StructuredQuery.UnaryFilter.Operator.IS_NULL,
                lambda x: x.equal(None),
            ),
            (
                query_pb.StructuredQuery.UnaryFilter.Operator.IS_NOT_NULL,
                lambda x: expr.Not(x.equal(None)),
            ),
        ],
    )
    def test__from_query_filter_pb_unary_filter(
        self, mock_client, op_enum, expected_expr_func
    ):
        """
        test supported unary filters
        """
        field_path = "unary_field"
        filter_pb = query_pb.StructuredQuery.UnaryFilter(
            field=query_pb.StructuredQuery.FieldReference(field_path=field_path),
            op=op_enum,
        )
        wrapped_filter_pb = query_pb.StructuredQuery.Filter(unary_filter=filter_pb)

        result = BooleanExpression._from_query_filter_pb(wrapped_filter_pb, mock_client)

        field_expr_inst = Field.of(field_path)
        expected_condition = expected_expr_func(field_expr_inst)
        # should include existance checks
        expected = expr.And(field_expr_inst.exists(), expected_condition)

        assert repr(result) == repr(expected)

    def test__from_query_filter_pb_unary_filter_unknown_op(self, mock_client):
        """
        check unary filter with unsupported operator type
        """
        field_path = "unary_field"
        filter_pb = query_pb.StructuredQuery.UnaryFilter(
            field=query_pb.StructuredQuery.FieldReference(field_path=field_path),
            op=query_pb.StructuredQuery.UnaryFilter.Operator.OPERATOR_UNSPECIFIED,  # Unknown op
        )
        wrapped_filter_pb = query_pb.StructuredQuery.Filter(unary_filter=filter_pb)

        with pytest.raises(TypeError, match="Unexpected UnaryFilter operator type"):
            BooleanExpression._from_query_filter_pb(wrapped_filter_pb, mock_client)

    @pytest.mark.parametrize(
        "op_enum, value, expected_expr_func, expects_existance",
        [
            (
                query_pb.StructuredQuery.FieldFilter.Operator.LESS_THAN,
                10,
                Expression.less_than,
                True,
            ),
            (
                query_pb.StructuredQuery.FieldFilter.Operator.LESS_THAN_OR_EQUAL,
                10,
                Expression.less_than_or_equal,
                True,
            ),
            (
                query_pb.StructuredQuery.FieldFilter.Operator.GREATER_THAN,
                10,
                Expression.greater_than,
                True,
            ),
            (
                query_pb.StructuredQuery.FieldFilter.Operator.GREATER_THAN_OR_EQUAL,
                10,
                Expression.greater_than_or_equal,
                True,
            ),
            (
                query_pb.StructuredQuery.FieldFilter.Operator.EQUAL,
                10,
                Expression.equal,
                True,
            ),
            (
                query_pb.StructuredQuery.FieldFilter.Operator.NOT_EQUAL,
                10,
                Expression.not_equal,
                False,
            ),
            (
                query_pb.StructuredQuery.FieldFilter.Operator.ARRAY_CONTAINS,
                10,
                Expression.array_contains,
                True,
            ),
            (
                query_pb.StructuredQuery.FieldFilter.Operator.ARRAY_CONTAINS_ANY,
                [10, 20],
                Expression.array_contains_any,
                True,
            ),
            (
                query_pb.StructuredQuery.FieldFilter.Operator.IN,
                [10, 20],
                Expression.equal_any,
                True,
            ),
            (
                query_pb.StructuredQuery.FieldFilter.Operator.NOT_IN,
                [10, 20],
                Expression.not_equal_any,
                False,
            ),
        ],
    )
    def test__from_query_filter_pb_field_filter(
        self, mock_client, op_enum, value, expected_expr_func, expects_existance
    ):
        """
        test supported field filters
        """
        field_path = "test_field"
        value_pb = _helpers.encode_value(value)
        filter_pb = query_pb.StructuredQuery.FieldFilter(
            field=query_pb.StructuredQuery.FieldReference(field_path=field_path),
            op=op_enum,
            value=value_pb,
        )
        wrapped_filter_pb = query_pb.StructuredQuery.Filter(field_filter=filter_pb)

        result = BooleanExpression._from_query_filter_pb(wrapped_filter_pb, mock_client)

        field_expr = Field.of(field_path)
        # convert values into constants
        value = (
            [Constant(e) for e in value] if isinstance(value, list) else Constant(value)
        )
        expected_condition = expected_expr_func(field_expr, value)
        if expects_existance:
            # some expressions include extra existance checks
            expected_condition = expr.And(field_expr.exists(), expected_condition)

        assert repr(result) == repr(expected_condition)

    def test__from_query_filter_pb_field_filter_unknown_op(self, mock_client):
        """
        check field filter with unsupported operator type
        """
        field_path = "test_field"
        value_pb = _helpers.encode_value(10)
        filter_pb = query_pb.StructuredQuery.FieldFilter(
            field=query_pb.StructuredQuery.FieldReference(field_path=field_path),
            op=query_pb.StructuredQuery.FieldFilter.Operator.OPERATOR_UNSPECIFIED,  # Unknown op
            value=value_pb,
        )
        wrapped_filter_pb = query_pb.StructuredQuery.Filter(field_filter=filter_pb)

        with pytest.raises(TypeError, match="Unexpected FieldFilter operator type"):
            BooleanExpression._from_query_filter_pb(wrapped_filter_pb, mock_client)

    def test__from_query_filter_pb_unknown_filter_type(self, mock_client):
        """
        test with unsupported filter type
        """
        # Test with an unexpected protobuf type
        with pytest.raises(TypeError, match="Unexpected filter type"):
            BooleanExpression._from_query_filter_pb(document_pb.Value(), mock_client)


class TestFunctionExpression:
    def test_equals(self):
        assert expr.FunctionExpression.sqrt("1") == expr.FunctionExpression.sqrt("1")
        assert expr.FunctionExpression.sqrt("1") != expr.FunctionExpression.sqrt("2")
        assert expr.FunctionExpression.sqrt("1") != expr.FunctionExpression.sum("1")
        assert expr.FunctionExpression.sqrt("1") != object()


class TestArray:
    """Tests for the array class"""

    def test_array(self):
        arg1 = Field.of("field1")
        instance = expr.Array([arg1])
        assert instance.name == "array"
        assert instance.params == [arg1]
        assert repr(instance) == "Array([Field.of('field1')])"

    def test_empty_array(self):
        instance = expr.Array([])
        assert instance.name == "array"
        assert instance.params == []
        assert repr(instance) == "Array([])"

    def test_array_w_primitives(self):
        a = expr.Array([1, Constant.of(2), "3"])
        assert a.name == "array"
        assert a.params == [Constant.of(1), Constant.of(2), Constant.of("3")]
        assert repr(a) == "Array([Constant.of(1), Constant.of(2), Constant.of('3')])"

    def test_array_w_non_list(self):
        with pytest.raises(TypeError):
            expr.Array(1)


class TestMap:
    """Tests for the map class"""

    def test_map(self):
        instance = expr.Map({Constant.of("a"): Constant.of("b")})
        assert instance.name == "map"
        assert instance.params == [Constant.of("a"), Constant.of("b")]
        assert repr(instance) == "Map({'a': 'b'})"

    def test_map_w_primitives(self):
        instance = expr.Map({"a": "b", "0": 0, "bool": True})
        assert instance.params == [
            Constant.of("a"),
            Constant.of("b"),
            Constant.of("0"),
            Constant.of(0),
            Constant.of("bool"),
            Constant.of(True),
        ]
        assert repr(instance) == "Map({'a': 'b', '0': 0, 'bool': True})"

    def test_empty_map(self):
        instance = expr.Map({})
        assert instance.name == "map"
        assert instance.params == []
        assert repr(instance) == "Map({})"

    def test_w_exprs(self):
        instance = expr.Map({Constant.of("a"): expr.Array([1, 2, 3])})
        assert instance.params == [Constant.of("a"), expr.Array([1, 2, 3])]
        assert (
            repr(instance)
            == "Map({'a': Array([Constant.of(1), Constant.of(2), Constant.of(3)])})"
        )


class TestExpressionessionMethods:
    """
    contains test methods for each Expression method
    """

    @pytest.mark.parametrize(
        "first,second,expected",
        [
            (
                Field.of("a").char_length(),
                Field.of("a").char_length(),
                True,
            ),
            (
                Field.of("a").char_length(),
                Field.of("b").char_length(),
                False,
            ),
            (
                Field.of("a").char_length(),
                Field.of("a").byte_length(),
                False,
            ),
            (
                Field.of("a").char_length(),
                Field.of("b").byte_length(),
                False,
            ),
            (
                Constant.of("").byte_length(),
                Field.of("").byte_length(),
                False,
            ),
            (Field.of("").byte_length(), Field.of("").byte_length(), True),
        ],
    )
    def test_equality(self, first, second, expected):
        assert (first == second) is expected

    def _make_arg(self, name="Mock"):
        class MockExpression(Constant):
            def __repr__(self):
                return self.value

        arg = MockExpression(name)
        return arg

    def test_expression_wrong_first_type(self):
        """The first argument should always be an expression or field name"""
        expected_message = "must be called on an Expression or a string representing a field. got <class 'int'>."
        with pytest.raises(TypeError) as e1:
            Expression.logical_minimum(5, 1)
        assert str(e1.value) == f"'logical_minimum' {expected_message}"
        with pytest.raises(TypeError) as e2:
            Expression.sqrt(9)
        assert str(e2.value) == f"'sqrt' {expected_message}"

    def test_expression_w_string(self):
        """should be able to use string for first argument. Should be interpreted as Field"""
        instance = Expression.logical_minimum("first", "second")
        assert isinstance(instance.params[0], Field)
        assert instance.params[0].path == "first"

    def test_and(self):
        arg1 = self._make_arg()
        arg2 = self._make_arg()
        arg3 = self._make_arg()
        instance = expr.And(arg1, arg2, arg3)
        assert instance.name == "and"
        assert instance.params == [arg1, arg2, arg3]
        assert repr(instance) == "And(Mock, Mock, Mock)"

    def test_or(self):
        arg1 = self._make_arg("Arg1")
        arg2 = self._make_arg("Arg2")
        instance = expr.Or(arg1, arg2)
        assert instance.name == "or"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "Or(Arg1, Arg2)"

    def test_nor(self):
        arg1 = self._make_arg("Arg1")
        arg2 = self._make_arg("Arg2")
        instance = expr.Nor(arg1, arg2)
        assert instance.name == "nor"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "Nor(Arg1, Arg2)"

    def test_array_get(self):
        arg1 = self._make_arg("ArrayField")
        arg2 = self._make_arg("Offset")
        instance = Expression.array_get(arg1, arg2)
        assert instance.name == "array_get"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "ArrayField.array_get(Offset)"
        infix_instance = arg1.array_get(arg2)
        assert infix_instance == instance

    def test_offset(self):
        arg1 = self._make_arg("ArrayField")
        arg2 = self._make_arg("Offset")
        instance = Expression.offset(arg1, arg2)
        assert instance.name == "offset"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "ArrayField.offset(Offset)"
        infix_instance = arg1.offset(arg2)
        assert infix_instance == instance

    def test_array_contains(self):
        arg1 = self._make_arg("ArrayField")
        arg2 = self._make_arg("Element")
        instance = Expression.array_contains(arg1, arg2)
        assert instance.name == "array_contains"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "ArrayField.array_contains(Element)"
        infix_instance = arg1.array_contains(arg2)
        assert infix_instance == instance

    def test_array_contains_any(self):
        arg1 = self._make_arg("ArrayField")
        arg2 = self._make_arg("Element1")
        arg3 = self._make_arg("Element2")
        instance = Expression.array_contains_any(arg1, [arg2, arg3])
        assert instance.name == "array_contains_any"
        assert isinstance(instance.params[1], expr.Array)
        assert instance.params[0] == arg1
        assert instance.params[1].params == [arg2, arg3]
        assert (
            repr(instance)
            == "ArrayField.array_contains_any(Array([Element1, Element2]))"
        )
        infix_instance = arg1.array_contains_any([arg2, arg3])
        assert infix_instance == instance

    def test_exists(self):
        arg1 = self._make_arg("Field")
        instance = Expression.exists(arg1)
        assert instance.name == "exists"
        assert instance.params == [arg1]
        assert repr(instance) == "Field.exists()"
        infix_instance = arg1.exists()
        assert infix_instance == instance

    def test_equal(self):
        arg1 = self._make_arg("Left")
        arg2 = self._make_arg("Right")
        instance = Expression.equal(arg1, arg2)
        assert instance.name == "equal"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "Left.equal(Right)"
        infix_instance = arg1.equal(arg2)
        assert infix_instance == instance

    def test_between(self):
        arg1 = self._make_arg("Left")
        arg2 = self._make_arg("Lower")
        arg3 = self._make_arg("Upper")
        instance = Expression.between(arg1, arg2, arg3)
        assert instance.name == "and"
        assert len(instance.params) == 2
        assert instance.params[0].name == "greater_than_or_equal"
        assert instance.params[1].name == "less_than_or_equal"
        assert (
            repr(instance)
            == "And(Left.greater_than_or_equal(Lower), Left.less_than_or_equal(Upper))"
        )
        infix_instance = arg1.between(arg2, arg3)
        assert infix_instance == instance

    def test_geo_distance(self):
        arg1 = self._make_arg("Left")
        arg2 = self._make_arg("Right")
        instance = Expression.geo_distance(arg1, arg2)
        assert instance.name == "geo_distance"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "Left.geo_distance(Right)"
        infix_instance = arg1.geo_distance(arg2)
        assert infix_instance == instance

    def test_geo_distance_with_tuple(self):
        from google.cloud.firestore_v1._helpers import GeoPoint
        from google.cloud.firestore_v1.pipeline_expressions import Constant

        arg1 = self._make_arg("Left")
        instance = Expression.geo_distance(arg1, (1.2, 3.4))
        assert instance.name == "geo_distance"
        assert instance.params[0] == arg1
        assert isinstance(instance.params[1], Constant)
        assert instance.params[1].value == GeoPoint(1.2, 3.4)

        infix_instance = arg1.geo_distance((1.2, 3.4))
        assert infix_instance.name == "geo_distance"
        assert infix_instance.params[0] == arg1
        assert isinstance(infix_instance.params[1], Constant)
        assert infix_instance.params[1].value == GeoPoint(1.2, 3.4)

    def test_document_matches(self):
        arg1 = self._make_arg("Query")
        instance = expr.DocumentMatches(arg1)
        assert instance.name == "document_matches"
        assert instance.params == [arg1]
        assert repr(instance) == "DocumentMatches(Query)"

    def test_score(self):
        instance = expr.Score()
        assert instance.name == "score"
        assert instance.params == []
        assert repr(instance) == "Score()"

    def test_greater_than_or_equal(self):
        arg1 = self._make_arg("Left")
        arg2 = self._make_arg("Right")
        instance = Expression.greater_than_or_equal(arg1, arg2)
        assert instance.name == "greater_than_or_equal"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "Left.greater_than_or_equal(Right)"
        infix_instance = arg1.greater_than_or_equal(arg2)
        assert infix_instance == instance

    def test_greater_than(self):
        arg1 = self._make_arg("Left")
        arg2 = self._make_arg("Right")
        instance = Expression.greater_than(arg1, arg2)
        assert instance.name == "greater_than"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "Left.greater_than(Right)"
        infix_instance = arg1.greater_than(arg2)
        assert infix_instance == instance

    def test_less_than_or_equal(self):
        arg1 = self._make_arg("Left")
        arg2 = self._make_arg("Right")
        instance = Expression.less_than_or_equal(arg1, arg2)
        assert instance.name == "less_than_or_equal"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "Left.less_than_or_equal(Right)"
        infix_instance = arg1.less_than_or_equal(arg2)
        assert infix_instance == instance

    def test_less_than(self):
        arg1 = self._make_arg("Left")
        arg2 = self._make_arg("Right")
        instance = Expression.less_than(arg1, arg2)
        assert instance.name == "less_than"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "Left.less_than(Right)"
        infix_instance = arg1.less_than(arg2)
        assert infix_instance == instance

    def test_not_equal(self):
        arg1 = self._make_arg("Left")
        arg2 = self._make_arg("Right")
        instance = Expression.not_equal(arg1, arg2)
        assert instance.name == "not_equal"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "Left.not_equal(Right)"
        infix_instance = arg1.not_equal(arg2)
        assert infix_instance == instance

    def test_equal_any(self):
        arg1 = self._make_arg("Field")
        arg2 = self._make_arg("Value1")
        arg3 = self._make_arg("Value2")
        instance = Expression.equal_any(arg1, [arg2, arg3])
        assert instance.name == "equal_any"
        assert isinstance(instance.params[1], expr.Array)
        assert instance.params[0] == arg1
        assert instance.params[1].params == [arg2, arg3]
        assert repr(instance) == "Field.equal_any(Array([Value1, Value2]))"
        infix_instance = arg1.equal_any([arg2, arg3])
        assert infix_instance == instance

    def test_not_equal_any(self):
        arg1 = self._make_arg("Field")
        arg2 = self._make_arg("Value1")
        arg3 = self._make_arg("Value2")
        instance = Expression.not_equal_any(arg1, [arg2, arg3])
        assert instance.name == "not_equal_any"
        assert isinstance(instance.params[1], expr.Array)
        assert instance.params[0] == arg1
        assert instance.params[1].params == [arg2, arg3]
        assert repr(instance) == "Field.not_equal_any(Array([Value1, Value2]))"
        infix_instance = arg1.not_equal_any([arg2, arg3])
        assert infix_instance == instance

    def test_is_absent(self):
        arg1 = self._make_arg("Field")
        instance = Expression.is_absent(arg1)
        assert instance.name == "is_absent"
        assert instance.params == [arg1]
        assert repr(instance) == "Field.is_absent()"
        infix_instance = arg1.is_absent()
        assert infix_instance == instance

    def test_if_absent(self):
        arg1 = self._make_arg("Field")
        arg2 = self._make_arg("ThenExpression")
        instance = Expression.if_absent(arg1, arg2)
        assert instance.name == "if_absent"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "Field.if_absent(ThenExpression)"
        infix_instance = arg1.if_absent(arg2)
        assert infix_instance == instance

    def test_is_error(self):
        arg1 = self._make_arg("Value")
        instance = Expression.is_error(arg1)
        assert instance.name == "is_error"
        assert instance.params == [arg1]
        assert repr(instance) == "Value.is_error()"
        infix_instance = arg1.is_error()
        assert infix_instance == instance

    def test_if_error(self):
        arg1 = self._make_arg("Value")
        arg2 = self._make_arg("ThenExpression")
        instance = Expression.if_error(arg1, arg2)
        assert instance.name == "if_error"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "Value.if_error(ThenExpression)"
        infix_instance = arg1.if_error(arg2)
        assert infix_instance == instance

    def test_coalesce(self):
        arg1 = self._make_arg("Arg1")
        arg2 = self._make_arg("Arg2")
        arg3 = self._make_arg("Arg3")
        instance = Expression.coalesce(arg1, arg2, arg3)
        assert instance.name == "coalesce"
        assert instance.params == [arg1, arg2, arg3]
        assert repr(instance) == "Arg1.coalesce(Arg2, Arg3)"
        infix_instance = arg1.coalesce(arg2, arg3)
        assert infix_instance == instance

    def test_switch_on(self):
        arg1 = self._make_arg("Condition1")
        arg2 = self._make_arg("Result1")
        arg3 = self._make_arg("Condition2")
        arg4 = self._make_arg("Result2")
        arg5 = self._make_arg("Default")
        instance = Expression.switch_on(arg1, arg2, arg3, arg4, arg5)
        assert instance.name == "switch_on"
        assert instance.params == [arg1, arg2, arg3, arg4, arg5]
        assert (
            repr(instance)
            == "Condition1.switch_on(Result1, Condition2, Result2, Default)"
        )
        infix_instance = arg1.switch_on(arg2, arg3, arg4, arg5)
        assert infix_instance == instance

    def test_storage_size(self):
        arg1 = self._make_arg("Input")
        instance = Expression.storage_size(arg1)
        assert instance.name == "storage_size"
        assert instance.params == [arg1]
        assert repr(instance) == "Input.storage_size()"
        infix_instance = arg1.storage_size()
        assert infix_instance == instance

    def test_not(self):
        arg1 = self._make_arg("Condition")
        instance = expr.Not(arg1)
        assert instance.name == "not"
        assert instance.params == [arg1]
        assert repr(instance) == "Not(Condition)"

    def test_array_contains_all(self):
        arg1 = self._make_arg("ArrayField")
        arg2 = self._make_arg("Element1")
        arg3 = self._make_arg("Element2")
        instance = Expression.array_contains_all(arg1, [arg2, arg3])
        assert instance.name == "array_contains_all"
        assert isinstance(instance.params[1], expr.Array)
        assert instance.params[0] == arg1
        assert instance.params[1].params == [arg2, arg3]
        assert (
            repr(instance)
            == "ArrayField.array_contains_all(Array([Element1, Element2]))"
        )
        infix_instance = arg1.array_contains_all([arg2, arg3])
        assert infix_instance == instance

    def test_ends_with(self):
        arg1 = self._make_arg("Expression")
        arg2 = self._make_arg("Postfix")
        instance = Expression.ends_with(arg1, arg2)
        assert instance.name == "ends_with"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "Expression.ends_with(Postfix)"
        infix_instance = arg1.ends_with(arg2)
        assert infix_instance == instance

    def test_conditional(self):
        arg1 = self._make_arg("Condition")
        arg2 = self._make_arg("ThenExpression")
        arg3 = self._make_arg("ElseExpression")
        instance = expr.Conditional(arg1, arg2, arg3)
        assert instance.name == "conditional"
        assert instance.params == [arg1, arg2, arg3]
        assert (
            repr(instance) == "Conditional(Condition, ThenExpression, ElseExpression)"
        )

    def test_like(self):
        arg1 = self._make_arg("Expression")
        arg2 = self._make_arg("Pattern")
        instance = Expression.like(arg1, arg2)
        assert instance.name == "like"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "Expression.like(Pattern)"
        infix_instance = arg1.like(arg2)
        assert infix_instance == instance

    def test_regex_contains(self):
        arg1 = self._make_arg("Expression")
        arg2 = self._make_arg("Regex")
        instance = Expression.regex_contains(arg1, arg2)
        assert instance.name == "regex_contains"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "Expression.regex_contains(Regex)"
        infix_instance = arg1.regex_contains(arg2)
        assert infix_instance == instance

    def test_regex_match(self):
        arg1 = self._make_arg("Expression")
        arg2 = self._make_arg("Regex")
        instance = Expression.regex_match(arg1, arg2)
        assert instance.name == "regex_match"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "Expression.regex_match(Regex)"
        infix_instance = arg1.regex_match(arg2)
        assert infix_instance == instance

    def test_starts_with(self):
        arg1 = self._make_arg("Expression")
        arg2 = self._make_arg("Prefix")
        instance = Expression.starts_with(arg1, arg2)
        assert instance.name == "starts_with"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "Expression.starts_with(Prefix)"
        infix_instance = arg1.starts_with(arg2)
        assert infix_instance == instance

    def test_string_contains(self):
        arg1 = self._make_arg("Expression")
        arg2 = self._make_arg("Substring")
        instance = Expression.string_contains(arg1, arg2)
        assert instance.name == "string_contains"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "Expression.string_contains(Substring)"
        infix_instance = arg1.string_contains(arg2)
        assert infix_instance == instance

    def test_xor(self):
        arg1 = self._make_arg("Condition1")
        arg2 = self._make_arg("Condition2")
        instance = expr.Xor([arg1, arg2])
        assert instance.name == "xor"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "Xor(Condition1, Condition2)"

    def test_divide(self):
        arg1 = self._make_arg("Left")
        arg2 = self._make_arg("Right")
        instance = Expression.divide(arg1, arg2)
        assert instance.name == "divide"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "Left.divide(Right)"
        infix_instance = arg1.divide(arg2)
        assert infix_instance == instance

    def test_logical_maximum(self):
        arg1 = self._make_arg("A1")
        arg2 = self._make_arg("A2")
        arg3 = self._make_arg("A3")
        instance = Expression.logical_maximum(arg1, arg2, arg3)
        assert instance.name == "maximum"
        assert instance.params == [arg1, arg2, arg3]
        assert repr(instance) == "A1.logical_maximum(A2, A3)"
        infix_instance = arg1.logical_maximum(arg2, arg3)
        assert infix_instance == instance

    def test_logical_minimum(self):
        arg1 = self._make_arg("A1")
        arg2 = self._make_arg("A2")
        arg3 = self._make_arg("A3")
        instance = Expression.logical_minimum(arg1, arg2, arg3)
        assert instance.name == "minimum"
        assert instance.params == [arg1, arg2, arg3]
        assert repr(instance) == "A1.logical_minimum(A2, A3)"
        infix_instance = arg1.logical_minimum(arg2, arg3)
        assert infix_instance == instance

    def test_to_lower(self):
        arg1 = self._make_arg("Input")
        instance = Expression.to_lower(arg1)
        assert instance.name == "to_lower"
        assert instance.params == [arg1]
        assert repr(instance) == "Input.to_lower()"
        infix_instance = arg1.to_lower()
        assert infix_instance == instance

    def test_to_upper(self):
        arg1 = self._make_arg("Input")
        instance = Expression.to_upper(arg1)
        assert instance.name == "to_upper"
        assert instance.params == [arg1]
        assert repr(instance) == "Input.to_upper()"
        infix_instance = arg1.to_upper()
        assert infix_instance == instance

    def test_trim(self):
        arg1 = self._make_arg("Input")
        instance = Expression.trim(arg1)
        assert instance.name == "trim"
        assert instance.params == [arg1]
        assert repr(instance) == "Input.trim()"
        infix_instance = arg1.trim()
        assert infix_instance == instance

    def test_string_reverse(self):
        arg1 = self._make_arg("Input")
        instance = Expression.string_reverse(arg1)
        assert instance.name == "string_reverse"
        assert instance.params == [arg1]
        assert repr(instance) == "Input.string_reverse()"
        infix_instance = arg1.string_reverse()
        assert infix_instance == instance

    def test_substring(self):
        arg1 = self._make_arg("Input")
        arg2 = self._make_arg("Position")
        instance = Expression.substring(arg1, arg2)
        assert instance.name == "substring"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "Input.substring(Position)"
        infix_instance = arg1.substring(arg2)
        assert infix_instance == instance

    def test_substring_w_length(self):
        arg1 = self._make_arg("Input")
        arg2 = self._make_arg("Position")
        arg3 = self._make_arg("Length")
        instance = Expression.substring(arg1, arg2, arg3)
        assert instance.name == "substring"
        assert instance.params == [arg1, arg2, arg3]
        assert repr(instance) == "Input.substring(Position, Length)"
        infix_instance = arg1.substring(arg2, arg3)
        assert infix_instance == instance

    def test_join(self):
        arg1 = self._make_arg("Array")
        arg2 = self._make_arg("Separator")
        instance = Expression.join(arg1, arg2)
        assert instance.name == "join"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "Array.join(Separator)"
        infix_instance = arg1.join(arg2)
        assert infix_instance == instance

    def test_map_get(self):
        arg1 = self._make_arg("Map")
        arg2 = "key"
        instance = Expression.map_get(arg1, arg2)
        assert instance.name == "map_get"
        assert instance.params == [arg1, Constant.of(arg2)]
        assert repr(instance) == "Map.map_get(Constant.of('key'))"
        infix_instance = arg1.map_get(Constant.of(arg2))
        assert infix_instance == instance

    def test_map_set(self):
        arg1 = self._make_arg("Map")
        arg2 = "key"
        arg3 = "value"
        instance = Expression.map_set(arg1, arg2, arg3)
        assert instance.name == "map_set"
        assert instance.params == [arg1, Constant.of(arg2), Constant.of(arg3)]
        assert repr(instance) == "Map.map_set(Constant.of('key'), Constant.of('value'))"
        infix_instance = arg1.map_set(Constant.of(arg2), arg3)
        assert infix_instance == instance

    def test_map_remove(self):
        arg1 = self._make_arg("Map")
        arg2 = "key"
        instance = Expression.map_remove(arg1, arg2)
        assert instance.name == "map_remove"
        assert instance.params == [arg1, Constant.of(arg2)]
        assert repr(instance) == "Map.map_remove(Constant.of('key'))"
        infix_instance = arg1.map_remove(Constant.of(arg2))
        assert infix_instance == instance

    def test_map_merge(self):
        arg1 = expr.Map({"a": 1})
        arg2 = expr.Map({"b": 2})
        arg3 = {"c": 3}
        instance = Expression.map_merge(arg1, arg2, arg3)
        assert instance.name == "map_merge"
        assert instance.params == [arg1, arg2, expr.Map(arg3)]
        assert repr(instance) == "Map({'a': 1}).map_merge(Map({'b': 2}), Map({'c': 3}))"
        infix_instance = arg1.map_merge(arg2, arg3)
        assert infix_instance == instance

    def test_map_keys(self):
        arg1 = self._make_arg("Map")
        instance = Expression.map_keys(arg1)
        assert instance.name == "map_keys"
        assert instance.params == [arg1]
        assert repr(instance) == "Map.map_keys()"
        infix_instance = arg1.map_keys()
        assert infix_instance == instance

    def test_map_values(self):
        arg1 = self._make_arg("Map")
        instance = Expression.map_values(arg1)
        assert instance.name == "map_values"
        assert instance.params == [arg1]
        assert repr(instance) == "Map.map_values()"
        infix_instance = arg1.map_values()
        assert infix_instance == instance

    def test_map_entries(self):
        arg1 = self._make_arg("Map")
        instance = Expression.map_entries(arg1)
        assert instance.name == "map_entries"
        assert instance.params == [arg1]
        assert repr(instance) == "Map.map_entries()"
        infix_instance = arg1.map_entries()
        assert infix_instance == instance

    def test_mod(self):
        arg1 = self._make_arg("Left")
        arg2 = self._make_arg("Right")
        instance = Expression.mod(arg1, arg2)
        assert instance.name == "mod"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "Left.mod(Right)"
        infix_instance = arg1.mod(arg2)
        assert infix_instance == instance

    def test_multiply(self):
        arg1 = self._make_arg("Left")
        arg2 = self._make_arg("Right")
        instance = Expression.multiply(arg1, arg2)
        assert instance.name == "multiply"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "Left.multiply(Right)"
        infix_instance = arg1.multiply(arg2)
        assert infix_instance == instance

    def test_string_concat(self):
        arg1 = self._make_arg("Str1")
        arg2 = self._make_arg("Str2")
        arg3 = self._make_arg("Str3")
        instance = Expression.string_concat(arg1, arg2, arg3)
        assert instance.name == "string_concat"
        assert instance.params == [arg1, arg2, arg3]
        assert repr(instance) == "Str1.string_concat(Str2, Str3)"
        infix_instance = arg1.string_concat(arg2, arg3)
        assert infix_instance == instance

    def test_subtract(self):
        arg1 = self._make_arg("Left")
        arg2 = self._make_arg("Right")
        instance = Expression.subtract(arg1, arg2)
        assert instance.name == "subtract"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "Left.subtract(Right)"
        infix_instance = arg1.subtract(arg2)
        assert infix_instance == instance

    def test_current_timestamp(self):
        instance = expr.CurrentTimestamp()
        assert instance.name == "current_timestamp"
        assert instance.params == []
        assert repr(instance) == "CurrentTimestamp()"

    def test_timestamp_add(self):
        arg1 = self._make_arg("Timestamp")
        arg2 = self._make_arg("Unit")
        arg3 = self._make_arg("Amount")
        instance = Expression.timestamp_add(arg1, arg2, arg3)
        assert instance.name == "timestamp_add"
        assert instance.params == [arg1, arg2, arg3]
        assert repr(instance) == "Timestamp.timestamp_add(Unit, Amount)"
        infix_instance = arg1.timestamp_add(arg2, arg3)
        assert infix_instance == instance

    def test_timestamp_subtract(self):
        arg1 = self._make_arg("Timestamp")
        arg2 = self._make_arg("Unit")
        arg3 = self._make_arg("Amount")
        instance = Expression.timestamp_subtract(arg1, arg2, arg3)
        assert instance.name == "timestamp_subtract"
        assert instance.params == [arg1, arg2, arg3]
        assert repr(instance) == "Timestamp.timestamp_subtract(Unit, Amount)"
        infix_instance = arg1.timestamp_subtract(arg2, arg3)
        assert infix_instance == instance

    def test_timestamp_to_unix_micros(self):
        arg1 = self._make_arg("Input")
        instance = Expression.timestamp_to_unix_micros(arg1)
        assert instance.name == "timestamp_to_unix_micros"
        assert instance.params == [arg1]
        assert repr(instance) == "Input.timestamp_to_unix_micros()"
        infix_instance = arg1.timestamp_to_unix_micros()
        assert infix_instance == instance

    def test_timestamp_to_unix_millis(self):
        arg1 = self._make_arg("Input")
        instance = Expression.timestamp_to_unix_millis(arg1)
        assert instance.name == "timestamp_to_unix_millis"
        assert instance.params == [arg1]
        assert repr(instance) == "Input.timestamp_to_unix_millis()"
        infix_instance = arg1.timestamp_to_unix_millis()
        assert infix_instance == instance

    def test_timestamp_to_unix_seconds(self):
        arg1 = self._make_arg("Input")
        instance = Expression.timestamp_to_unix_seconds(arg1)
        assert instance.name == "timestamp_to_unix_seconds"
        assert instance.params == [arg1]
        assert repr(instance) == "Input.timestamp_to_unix_seconds()"
        infix_instance = arg1.timestamp_to_unix_seconds()
        assert infix_instance == instance

    def test_unix_micros_to_timestamp(self):
        arg1 = self._make_arg("Input")
        instance = Expression.unix_micros_to_timestamp(arg1)
        assert instance.name == "unix_micros_to_timestamp"
        assert instance.params == [arg1]
        assert repr(instance) == "Input.unix_micros_to_timestamp()"
        infix_instance = arg1.unix_micros_to_timestamp()
        assert infix_instance == instance

    def test_unix_millis_to_timestamp(self):
        arg1 = self._make_arg("Input")
        instance = Expression.unix_millis_to_timestamp(arg1)
        assert instance.name == "unix_millis_to_timestamp"
        assert instance.params == [arg1]
        assert repr(instance) == "Input.unix_millis_to_timestamp()"
        infix_instance = arg1.unix_millis_to_timestamp()
        assert infix_instance == instance

    def test_unix_seconds_to_timestamp(self):
        arg1 = self._make_arg("Input")
        instance = Expression.unix_seconds_to_timestamp(arg1)
        assert instance.name == "unix_seconds_to_timestamp"
        assert instance.params == [arg1]
        assert repr(instance) == "Input.unix_seconds_to_timestamp()"
        infix_instance = arg1.unix_seconds_to_timestamp()
        assert infix_instance == instance

    def test_euclidean_distance(self):
        arg1 = self._make_arg("Vector1")
        arg2 = self._make_arg("Vector2")
        instance = Expression.euclidean_distance(arg1, arg2)
        assert instance.name == "euclidean_distance"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "Vector1.euclidean_distance(Vector2)"
        infix_instance = arg1.euclidean_distance(arg2)
        assert infix_instance == instance

    def test_cosine_distance(self):
        arg1 = self._make_arg("Vector1")
        arg2 = self._make_arg("Vector2")
        instance = Expression.cosine_distance(arg1, arg2)
        assert instance.name == "cosine_distance"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "Vector1.cosine_distance(Vector2)"
        infix_instance = arg1.cosine_distance(arg2)
        assert infix_instance == instance

    def test_regex_find(self):
        arg1 = self._make_arg("String")
        arg2 = self._make_arg("pattern")
        instance = Expression.regex_find(arg1, arg2)
        assert instance.name == "regex_find"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "String.regex_find(pattern)"
        infix_instance = arg1.regex_find(arg2)
        assert infix_instance == instance

    def test_regex_find_all(self):
        arg1 = self._make_arg("String")
        arg2 = self._make_arg("pattern")
        instance = Expression.regex_find_all(arg1, arg2)
        assert instance.name == "regex_find_all"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "String.regex_find_all(pattern)"
        infix_instance = arg1.regex_find_all(arg2)
        assert infix_instance == instance

    def test_split(self):
        arg1 = self._make_arg("String")
        arg2 = self._make_arg("-")
        instance = Expression.split(arg1, arg2)
        assert instance.name == "split"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "String.split(-)"
        infix_instance = arg1.split(arg2)
        assert infix_instance == instance

    def test_string_repeat(self):
        arg1 = self._make_arg("String")
        arg2 = self._make_arg("3")
        instance = Expression.string_repeat(arg1, arg2)
        assert instance.name == "string_repeat"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "String.string_repeat(3)"
        infix_instance = arg1.string_repeat(arg2)
        assert infix_instance == instance

    def test_string_replace_all(self):
        arg1 = self._make_arg("String")
        arg2 = self._make_arg("find")
        arg3 = self._make_arg("replacement")
        instance = Expression.string_replace_all(arg1, arg2, arg3)
        assert instance.name == "string_replace_all"
        assert instance.params == [arg1, arg2, arg3]
        assert repr(instance) == "String.string_replace_all(find, replacement)"
        infix_instance = arg1.string_replace_all(arg2, arg3)
        assert infix_instance == instance

    def test_string_replace_one(self):
        arg1 = self._make_arg("String")
        arg2 = self._make_arg("find")
        arg3 = self._make_arg("replacement")
        instance = Expression.string_replace_one(arg1, arg2, arg3)
        assert instance.name == "string_replace_one"
        assert instance.params == [arg1, arg2, arg3]
        assert repr(instance) == "String.string_replace_one(find, replacement)"
        infix_instance = arg1.string_replace_one(arg2, arg3)
        assert infix_instance == instance

    def test_string_index_of(self):
        arg1 = self._make_arg("String")
        arg2 = self._make_arg("search")
        instance = Expression.string_index_of(arg1, arg2)
        assert instance.name == "string_index_of"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "String.string_index_of(search)"
        infix_instance = arg1.string_index_of(arg2)
        assert infix_instance == instance

    def test_ltrim(self):
        arg1 = self._make_arg("String")
        arg2 = self._make_arg("chars")

        # Without args
        instance = Expression.ltrim(arg1)
        assert instance.name == "ltrim"
        assert instance.params == [arg1]
        assert repr(instance) == "String.ltrim()"
        infix_instance = arg1.ltrim()
        assert infix_instance == instance

        # With args
        instance = Expression.ltrim(arg1, arg2)
        assert instance.name == "ltrim"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "String.ltrim(chars)"
        infix_instance = arg1.ltrim(arg2)
        assert infix_instance == instance

    def test_rtrim(self):
        arg1 = self._make_arg("String")
        arg2 = self._make_arg("chars")

        # Without args
        instance = Expression.rtrim(arg1)
        assert instance.name == "rtrim"
        assert instance.params == [arg1]
        assert repr(instance) == "String.rtrim()"
        infix_instance = arg1.rtrim()
        assert infix_instance == instance

        # With args
        instance = Expression.rtrim(arg1, arg2)
        assert instance.name == "rtrim"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "String.rtrim(chars)"
        infix_instance = arg1.rtrim(arg2)
        assert infix_instance == instance

    def test_dot_product(self):
        arg1 = self._make_arg("Vector1")
        arg2 = self._make_arg("Vector2")
        instance = Expression.dot_product(arg1, arg2)
        assert instance.name == "dot_product"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "Vector1.dot_product(Vector2)"
        infix_instance = arg1.dot_product(arg2)
        assert infix_instance == instance

    @pytest.mark.parametrize(
        "method", ["euclidean_distance", "cosine_distance", "dot_product"]
    )
    @pytest.mark.parametrize(
        "input", [Vector([1.0, 2.0]), [1, 2], Constant.of(Vector([1.0, 2.0])), []]
    )
    def test_vector_ctor(self, method, input):
        """
        test constructing various vector expressions with
        different inputs
        """
        arg1 = self._make_arg("VectorRef")
        instance = getattr(arg1, method)(input)
        assert instance.name == method
        got_second_param = instance.params[1]
        assert isinstance(got_second_param, Constant)
        assert isinstance(got_second_param.value, Vector)

    def test_vector_length(self):
        arg1 = self._make_arg("Array")
        instance = Expression.vector_length(arg1)
        assert instance.name == "vector_length"
        assert instance.params == [arg1]
        assert repr(instance) == "Array.vector_length()"
        infix_instance = arg1.vector_length()
        assert infix_instance == instance

    def test_get_field(self):
        arg1 = self._make_arg("Map")
        arg2 = self._make_arg("Key")
        instance = Expression.get_field(arg1, arg2)
        assert instance.name == "get_field"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "Map.get_field(Key)"
        infix_instance = arg1.get_field(arg2)
        assert infix_instance == instance

    def test_add(self):
        arg1 = self._make_arg("Left")
        arg2 = self._make_arg("Right")
        instance = Expression.add(arg1, arg2)
        assert instance.name == "add"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "Left.add(Right)"
        infix_instance = arg1.add(arg2)
        assert infix_instance == instance

    def test_abs(self):
        arg1 = self._make_arg("Value")
        instance = Expression.abs(arg1)
        assert instance.name == "abs"
        assert instance.params == [arg1]
        assert repr(instance) == "Value.abs()"
        infix_instance = arg1.abs()
        assert infix_instance == instance

    def test_ceil(self):
        arg1 = self._make_arg("Value")
        instance = Expression.ceil(arg1)
        assert instance.name == "ceil"
        assert instance.params == [arg1]
        assert repr(instance) == "Value.ceil()"
        infix_instance = arg1.ceil()
        assert infix_instance == instance

    def test_exp(self):
        arg1 = self._make_arg("Value")
        instance = Expression.exp(arg1)
        assert instance.name == "exp"
        assert instance.params == [arg1]
        assert repr(instance) == "Value.exp()"
        infix_instance = arg1.exp()
        assert infix_instance == instance

    def test_floor(self):
        arg1 = self._make_arg("Value")
        instance = Expression.floor(arg1)
        assert instance.name == "floor"
        assert instance.params == [arg1]
        assert repr(instance) == "Value.floor()"
        infix_instance = arg1.floor()
        assert infix_instance == instance

    def test_ln(self):
        arg1 = self._make_arg("Value")
        instance = Expression.ln(arg1)
        assert instance.name == "ln"
        assert instance.params == [arg1]
        assert repr(instance) == "Value.ln()"
        infix_instance = arg1.ln()
        assert infix_instance == instance

    def test_log(self):
        arg1 = self._make_arg("Value")
        arg2 = self._make_arg("Base")
        instance = Expression.log(arg1, arg2)
        assert instance.name == "log"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "Value.log(Base)"
        infix_instance = arg1.log(arg2)
        assert infix_instance == instance

    def test_log10(self):
        arg1 = self._make_arg("Value")
        instance = Expression.log10(arg1)
        assert instance.name == "log10"
        assert instance.params == [arg1]
        assert repr(instance) == "Value.log10()"
        infix_instance = arg1.log10()
        assert infix_instance == instance

    def test_pow(self):
        arg1 = self._make_arg("Value")
        arg2 = self._make_arg("Exponent")
        instance = Expression.pow(arg1, arg2)
        assert instance.name == "pow"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "Value.pow(Exponent)"
        infix_instance = arg1.pow(arg2)
        assert infix_instance == instance

    def test_round(self):
        arg1 = self._make_arg("Value")
        instance = Expression.round(arg1)
        assert instance.name == "round"
        assert instance.params == [arg1]
        assert repr(instance) == "Value.round()"
        infix_instance = arg1.round()
        assert infix_instance == instance

    def test_sqrt(self):
        arg1 = self._make_arg("Value")
        instance = Expression.sqrt(arg1)
        assert instance.name == "sqrt"
        assert instance.params == [arg1]
        assert repr(instance) == "Value.sqrt()"
        infix_instance = arg1.sqrt()
        assert infix_instance == instance

    def test_trunc(self):
        arg1 = self._make_arg("Value")
        instance = Expression.trunc(arg1)
        assert instance.name == "trunc"
        assert instance.params == [arg1]
        assert repr(instance) == "Value.trunc()"
        infix_instance = arg1.trunc()
        assert infix_instance == instance

        places = self._make_arg("Places")
        instance_with_places = Expression.trunc(arg1, places)
        assert instance_with_places.name == "trunc"
        assert instance_with_places.params == [arg1, places]
        assert repr(instance_with_places) == "Value.trunc(Places)"
        infix_instance_with_places = arg1.trunc(places)
        assert infix_instance_with_places == instance_with_places

    def test_array_length(self):
        arg1 = self._make_arg("Array")
        instance = Expression.array_length(arg1)
        assert instance.name == "array_length"
        assert instance.params == [arg1]
        assert repr(instance) == "Array.array_length()"
        infix_instance = arg1.array_length()
        assert infix_instance == instance

    def test_array_reverse(self):
        arg1 = self._make_arg("ArrayField")
        instance = Expression.array_reverse(arg1)
        assert instance.name == "array_reverse"
        assert instance.params == [arg1]
        assert repr(instance) == "ArrayField.array_reverse()"
        infix_instance = arg1.array_reverse()
        assert infix_instance == instance

    def test_array_filter(self):
        arr = self._make_arg("ArrayField")
        filter_expr = self._make_arg("FilterExpr")
        elm_alias = "element_alias"
        instance = Expression.array_filter(arr, filter_expr, elm_alias)
        assert instance.name == "array_filter"
        assert instance.params == [arr, Constant.of(elm_alias), filter_expr]
        assert (
            repr(instance)
            == "ArrayField.array_filter(FilterExpr, Constant.of('element_alias'))"
        )
        infix_instance = arr.array_filter(filter_expr, elm_alias)
        assert infix_instance == instance

    def test_array_transform(self):
        arr = self._make_arg("ArrayField")
        transform_expr = self._make_arg("TransformExpr")
        elm_alias = "element_alias"
        instance = Expression.array_transform(arr, transform_expr, elm_alias)
        assert instance.name == "array_transform"
        assert instance.params == [arr, Constant.of(elm_alias), transform_expr]
        assert (
            repr(instance)
            == "ArrayField.array_transform(TransformExpr, Constant.of('element_alias'))"
        )
        infix_instance = arr.array_transform(transform_expr, elm_alias)
        assert infix_instance == instance

        idx_alias = "index_alias"
        instance_with_idx = Expression.array_transform(
            arr, transform_expr, elm_alias, idx_alias
        )
        assert instance_with_idx.name == "array_transform"
        assert instance_with_idx.params == [
            arr,
            Constant.of(elm_alias),
            Constant.of(idx_alias),
            transform_expr,
        ]
        assert (
            repr(instance_with_idx)
            == "ArrayField.array_transform(TransformExpr, Constant.of('element_alias'), Constant.of('index_alias'))"
        )
        infix_instance_with_idx = arr.array_transform(
            transform_expr, elm_alias, idx_alias
        )
        assert infix_instance_with_idx == instance_with_idx

    def test_array_concat(self):
        arg1 = self._make_arg("ArrayRef1")
        arg2 = self._make_arg("ArrayRef2")
        instance = Expression.array_concat(arg1, arg2)
        assert instance.name == "array_concat"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "ArrayRef1.array_concat(ArrayRef2)"
        infix_instance = arg1.array_concat(arg2)
        assert infix_instance == instance

    def test_array_concat_multiple(self):
        arg1 = expr.Array([Constant.of(0)])
        arg2 = Field.of("ArrayRef2")
        arg3 = Field.of("ArrayRef3")
        arg4 = [self._make_arg("Constant")]
        instance = arg1.array_concat(arg2, arg3, arg4)
        assert instance.name == "array_concat"
        assert instance.params == [arg1, arg2, arg3, expr.Array(arg4)]
        assert (
            repr(instance)
            == "Array([Constant.of(0)]).array_concat(Field.of('ArrayRef2'), Field.of('ArrayRef3'), Array([Constant]))"
        )

    def test_byte_length(self):
        arg1 = self._make_arg("Expression")
        instance = Expression.byte_length(arg1)
        assert instance.name == "byte_length"
        assert instance.params == [arg1]
        assert repr(instance) == "Expression.byte_length()"
        infix_instance = arg1.byte_length()
        assert infix_instance == instance

    def test_char_length(self):
        arg1 = self._make_arg("Expression")
        instance = Expression.char_length(arg1)
        assert instance.name == "char_length"
        assert instance.params == [arg1]
        assert repr(instance) == "Expression.char_length()"
        infix_instance = arg1.char_length()
        assert infix_instance == instance

    def test_concat(self):
        arg1 = self._make_arg("First")
        arg2 = self._make_arg("Second")
        arg3 = "Third"
        instance = Expression.concat(arg1, arg2, arg3)
        assert instance.name == "concat"
        assert instance.params == [arg1, arg2, Constant.of(arg3)]
        assert repr(instance) == "First.concat(Second, Constant.of('Third'))"
        infix_instance = arg1.concat(arg2, arg3)
        assert infix_instance == instance

    def test_length(self):
        arg1 = self._make_arg("Expression")
        instance = Expression.length(arg1)
        assert instance.name == "length"
        assert instance.params == [arg1]
        assert repr(instance) == "Expression.length()"
        infix_instance = arg1.length()
        assert infix_instance == instance

    def test_collection_id(self):
        arg1 = self._make_arg("Value")
        instance = Expression.collection_id(arg1)
        assert instance.name == "collection_id"
        assert instance.params == [arg1]
        assert repr(instance) == "Value.collection_id()"
        infix_instance = arg1.collection_id()
        assert infix_instance == instance

    def test_document_id(self):
        arg1 = self._make_arg("Value")
        instance = Expression.document_id(arg1)
        assert instance.name == "document_id"
        assert instance.params == [arg1]
        assert repr(instance) == "Value.document_id()"
        infix_instance = arg1.document_id()
        assert infix_instance == instance

    def test_sum(self):
        arg1 = self._make_arg("Value")
        instance = Expression.sum(arg1)
        assert instance.name == "sum"
        assert instance.params == [arg1]
        assert repr(instance) == "Value.sum()"
        infix_instance = arg1.sum()
        assert infix_instance == instance

    def test_average(self):
        arg1 = self._make_arg("Value")
        instance = Expression.average(arg1)
        assert instance.name == "average"
        assert instance.params == [arg1]
        assert repr(instance) == "Value.average()"
        infix_instance = arg1.average()
        assert infix_instance == instance

    def test_count(self):
        arg1 = self._make_arg("Value")
        instance = Expression.count(arg1)
        assert instance.name == "count"
        assert instance.params == [arg1]
        assert repr(instance) == "Value.count()"
        infix_instance = arg1.count()
        assert infix_instance == instance

    def test_base_count(self):
        instance = expr.Count()
        assert instance.name == "count"
        assert instance.params == []
        assert repr(instance) == "Count()"

    def test_count_if(self):
        arg1 = self._make_arg("Value")
        instance = Expression.count_if(arg1)
        assert instance.name == "count_if"
        assert instance.params == [arg1]
        assert repr(instance) == "Value.count_if()"
        infix_instance = arg1.count_if()
        assert infix_instance == instance

    def test_count_distinct(self):
        arg1 = self._make_arg("Value")
        instance = Expression.count_distinct(arg1)
        assert instance.name == "count_distinct"
        assert instance.params == [arg1]
        assert repr(instance) == "Value.count_distinct()"
        infix_instance = arg1.count_distinct()
        assert infix_instance == instance

    def test_minimum(self):
        arg1 = self._make_arg("Value")
        instance = Expression.minimum(arg1)
        assert instance.name == "minimum"
        assert instance.params == [arg1]
        assert repr(instance) == "Value.minimum()"
        infix_instance = arg1.minimum()
        assert infix_instance == instance

    def test_maximum(self):
        arg1 = self._make_arg("Value")
        instance = Expression.maximum(arg1)
        assert instance.name == "maximum"
        assert instance.params == [arg1]
        assert repr(instance) == "Value.maximum()"
        infix_instance = arg1.maximum()
        assert infix_instance == instance

    def test_rand(self):
        instance = expr.Rand()
        assert instance.name == "rand"
        assert instance.params == []
        assert repr(instance) == "Rand()"

    def test_array_agg(self):
        arg1 = self._make_arg("Value")
        instance = Expression.array_agg(arg1)
        assert instance.name == "array_agg"
        assert instance.params == [arg1]
        assert repr(instance) == "Value.array_agg()"
        infix_instance = arg1.array_agg()
        assert infix_instance == instance

    def test_array_agg_distinct(self):
        arg1 = self._make_arg("Value")
        instance = Expression.array_agg_distinct(arg1)
        assert instance.name == "array_agg_distinct"
        assert instance.params == [arg1]
        assert repr(instance) == "Value.array_agg_distinct()"
        infix_instance = arg1.array_agg_distinct()
        assert infix_instance == instance

    def test_first(self):
        arg1 = self._make_arg("Value")
        instance = Expression.first(arg1)
        assert instance.name == "first"
        assert instance.params == [arg1]
        assert repr(instance) == "Value.first()"
        infix_instance = arg1.first()
        assert infix_instance == instance

    def test_last(self):
        arg1 = self._make_arg("Value")
        instance = Expression.last(arg1)
        assert instance.name == "last"
        assert instance.params == [arg1]
        assert repr(instance) == "Value.last()"
        infix_instance = arg1.last()
        assert infix_instance == instance

    def test_cmp(self):
        arg1 = self._make_arg("Value")
        arg2 = self._make_arg("Other")
        instance = Expression.cmp(arg1, arg2)
        assert instance.name == "cmp"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "Value.cmp(Other)"
        infix_instance = arg1.cmp(arg2)
        assert infix_instance == instance

    def test_timestamp_trunc(self):
        arg1 = self._make_arg("Timestamp")
        arg2 = self._make_arg("Granularity")
        arg3 = self._make_arg("Timezone")
        instance = Expression.timestamp_trunc(arg1, arg2)
        assert instance.name == "timestamp_trunc"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "Timestamp.timestamp_trunc(Granularity)"
        infix_instance = arg1.timestamp_trunc(arg2)
        assert infix_instance == instance

        instance_tz = Expression.timestamp_trunc(arg1, arg2, arg3)
        assert instance_tz.name == "timestamp_trunc"
        assert instance_tz.params == [arg1, arg2, arg3]
        assert repr(instance_tz) == "Timestamp.timestamp_trunc(Granularity, Timezone)"
        infix_instance_tz = arg1.timestamp_trunc(arg2, arg3)
        assert infix_instance_tz == instance_tz

    def test_timestamp_extract(self):
        arg1 = self._make_arg("Timestamp")
        arg2 = self._make_arg("Part")
        arg3 = self._make_arg("Timezone")
        instance = Expression.timestamp_extract(arg1, arg2)
        assert instance.name == "timestamp_extract"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "Timestamp.timestamp_extract(Part)"
        infix_instance = arg1.timestamp_extract(arg2)
        assert infix_instance == instance

        instance_tz = Expression.timestamp_extract(arg1, arg2, arg3)
        assert instance_tz.name == "timestamp_extract"
        assert instance_tz.params == [arg1, arg2, arg3]
        assert repr(instance_tz) == "Timestamp.timestamp_extract(Part, Timezone)"
        infix_instance_tz = arg1.timestamp_extract(arg2, arg3)
        assert infix_instance_tz == instance_tz

    def test_timestamp_diff(self):
        arg1 = self._make_arg("End")
        arg2 = self._make_arg("Start")
        arg3 = self._make_arg("Unit")
        instance = Expression.timestamp_diff(arg1, arg2, arg3)
        assert instance.name == "timestamp_diff"
        assert instance.params == [arg1, arg2, arg3]
        assert repr(instance) == "End.timestamp_diff(Start, Unit)"
        infix_instance = arg1.timestamp_diff(arg2, arg3)
        assert infix_instance == instance

    def test_if_null(self):
        arg1 = self._make_arg("Field1")
        arg2 = self._make_arg("Field2")
        arg3 = self._make_arg("Field3")
        instance = Expression.if_null(arg1, arg2, arg3)
        assert instance.name == "if_null"
        assert instance.params == [arg1, arg2, arg3]
        assert repr(instance) == "Field1.if_null(Field2, Field3)"
        infix_instance = arg1.if_null(arg2, arg3)
        assert infix_instance == instance

    def test_type(self):
        arg1 = self._make_arg("Value")
        instance = Expression.type(arg1)
        assert instance.name == "type"
        assert instance.params == [arg1]
        assert repr(instance) == "Value.type()"
        infix_instance = arg1.type()
        assert infix_instance == instance

    def test_is_type(self):
        arg1 = self._make_arg("Value")
        arg2 = self._make_arg("TypeString")
        instance = Expression.is_type(arg1, arg2)
        assert instance.name == "is_type"
        assert instance.params == [arg1, arg2]
        assert repr(instance) == "Value.is_type(TypeString)"
        infix_instance = arg1.is_type(arg2)
        assert infix_instance == instance

    def test_type_enum(self):
        from google.cloud.firestore_v1.pipeline_expressions import PipelineDataType

        arg1 = self._make_arg("Value")
        instance = Expression.is_type(arg1, PipelineDataType.STRING)
        assert instance.name == "is_type"
        assert instance.params[0] == arg1
        assert isinstance(instance.params[1], Constant)
        assert instance.params[1].value == PipelineDataType.STRING.value
        assert repr(instance) == "Value.is_type(Constant.of('string'))"
        infix_instance = arg1.is_type(PipelineDataType.STRING)
        assert infix_instance == instance

    def test_timestamp_enums(self):
        from google.cloud.firestore_v1.pipeline_expressions import (
            TimeGranularity,
            TimePart,
            TimeUnit,
        )

        arg1 = self._make_arg("Value")

        instance_add = Expression.timestamp_add(arg1, TimeUnit.DAY, 1)
        assert instance_add.name == "timestamp_add"
        assert isinstance(instance_add.params[1], Constant)
        assert instance_add.params[1].value == TimeUnit.DAY.value

        instance_trunc = Expression.timestamp_trunc(arg1, TimeGranularity.MONTH)
        assert instance_trunc.name == "timestamp_trunc"
        assert isinstance(instance_trunc.params[1], Constant)
        assert instance_trunc.params[1].value == TimeGranularity.MONTH.value

        instance_trunc_inherited = Expression.timestamp_trunc(
            arg1, TimeGranularity.MICROSECOND
        )
        assert instance_trunc_inherited.name == "timestamp_trunc"
        assert isinstance(instance_trunc_inherited.params[1], Constant)
        assert (
            instance_trunc_inherited.params[1].value
            == TimeGranularity.MICROSECOND.value
        )

        instance_extract = Expression.timestamp_extract(arg1, TimePart.YEAR)
        assert instance_extract.name == "timestamp_extract"
        assert isinstance(instance_extract.params[1], Constant)
        assert instance_extract.params[1].value == TimePart.YEAR.value

        instance_extract_inherited = Expression.timestamp_extract(arg1, TimePart.SECOND)
        assert instance_extract_inherited.name == "timestamp_extract"
        assert isinstance(instance_extract_inherited.params[1], Constant)
        assert instance_extract_inherited.params[1].value == TimePart.SECOND.value

    def test_array_first(self):
        arg1 = self._make_arg("Value")
        instance = Expression.array_first(arg1)
        assert instance.name == "array_first"
        assert instance.params == [arg1]
        assert repr(instance) == "Value.array_first()"
        infix_instance = arg1.array_first()
        assert infix_instance == instance

    def test_array_last(self):
        arg1 = self._make_arg("Value")
        instance = Expression.array_last(arg1)
        assert instance.name == "array_last"
        assert instance.params == [arg1]
        assert repr(instance) == "Value.array_last()"
        infix_instance = arg1.array_last()
        assert infix_instance == instance

    def test_array_first_n(self):
        arg1 = self._make_arg("Value")
        n = 2
        instance = Expression.array_first_n(arg1, n)
        assert instance.name == "array_first_n"
        assert instance.params[0] == arg1
        assert isinstance(instance.params[1], Constant)
        assert instance.params[1].value == n
        assert repr(instance) == "Value.array_first_n(Constant.of(2))"
        infix_instance = arg1.array_first_n(n)
        assert infix_instance == instance

    def test_array_last_n(self):
        arg1 = self._make_arg("Value")
        n = 2
        instance = Expression.array_last_n(arg1, n)
        assert instance.name == "array_last_n"
        assert instance.params[0] == arg1
        assert isinstance(instance.params[1], Constant)
        assert instance.params[1].value == n
        assert repr(instance) == "Value.array_last_n(Constant.of(2))"
        infix_instance = arg1.array_last_n(n)
        assert infix_instance == instance

    def test_array_maximum(self):
        arg1 = self._make_arg("Value")
        instance = Expression.array_maximum(arg1)
        assert instance.name == "maximum"
        assert instance.params == [arg1]
        assert repr(instance) == "Value.array_maximum()"
        infix_instance = arg1.array_maximum()
        assert infix_instance == instance

    def test_array_minimum(self):
        arg1 = self._make_arg("Value")
        instance = Expression.array_minimum(arg1)
        assert instance.name == "minimum"
        assert instance.params == [arg1]
        assert repr(instance) == "Value.array_minimum()"
        infix_instance = arg1.array_minimum()
        assert infix_instance == instance

    def test_array_maximum_n(self):
        arg1 = self._make_arg("Value")
        n = 2
        instance = Expression.array_maximum_n(arg1, n)
        assert instance.name == "maximum_n"
        assert instance.params[0] == arg1
        assert isinstance(instance.params[1], Constant)
        assert instance.params[1].value == n
        assert repr(instance) == "Value.array_maximum_n(Constant.of(2))"
        infix_instance = arg1.array_maximum_n(n)
        assert infix_instance == instance

    def test_array_minimum_n(self):
        arg1 = self._make_arg("Value")
        n = 2
        instance = Expression.array_minimum_n(arg1, n)
        assert instance.name == "minimum_n"
        assert instance.params[0] == arg1
        assert isinstance(instance.params[1], Constant)
        assert instance.params[1].value == n
        assert repr(instance) == "Value.array_minimum_n(Constant.of(2))"
        infix_instance = arg1.array_minimum_n(n)
        assert infix_instance == instance

    def test_array_slice_1_arg(self):
        arg1 = self._make_arg("Value")
        offset = 1
        instance = Expression.array_slice(arg1, offset)
        assert instance.name == "array_slice"
        assert instance.params[0] == arg1
        assert isinstance(instance.params[1], Constant)
        assert instance.params[1].value == offset
        assert len(instance.params) == 2
        assert repr(instance) == "Value.array_slice(Constant.of(1))"
        infix_instance = arg1.array_slice(offset)
        assert infix_instance == instance

    def test_array_slice_2_args(self):
        arg1 = self._make_arg("Value")
        offset = 1
        length = 2
        instance = Expression.array_slice(arg1, offset, length)
        assert instance.name == "array_slice"
        assert instance.params[0] == arg1
        assert isinstance(instance.params[1], Constant)
        assert instance.params[1].value == offset
        assert isinstance(instance.params[2], Constant)
        assert instance.params[2].value == length
        assert len(instance.params) == 3
        assert repr(instance) == "Value.array_slice(Constant.of(1), Constant.of(2))"
        infix_instance = arg1.array_slice(offset, length)
        assert infix_instance == instance

    def test_array_index_of(self):
        arg1 = self._make_arg("Value")
        value = "comedy"
        instance = Expression.array_index_of(arg1, value)
        assert instance.name == "array_index_of"
        assert instance.params[0] == arg1
        assert isinstance(instance.params[1], Constant)
        assert instance.params[1].value == value
        assert isinstance(instance.params[2], Constant)
        assert instance.params[2].value == "first"
        assert len(instance.params) == 3
        assert (
            repr(instance)
            == "Value.array_index_of(Constant.of('comedy'), Constant.of('first'))"
        )
        infix_instance = arg1.array_index_of(value)
        assert infix_instance == instance

    def test_array_index_of_all(self):
        arg1 = self._make_arg("Value")
        value = "comedy"
        instance = Expression.array_index_of_all(arg1, value)
        assert instance.name == "array_index_of_all"
        assert instance.params[0] == arg1
        assert isinstance(instance.params[1], Constant)
        assert instance.params[1].value == value
        assert len(instance.params) == 2
        assert repr(instance) == "Value.array_index_of_all(Constant.of('comedy'))"
        infix_instance = arg1.array_index_of_all(value)
        assert infix_instance == instance
