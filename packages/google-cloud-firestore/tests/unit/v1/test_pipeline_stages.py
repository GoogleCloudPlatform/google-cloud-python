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
# limitations under the License

from unittest import mock

import pytest

import google.cloud.firestore_v1.pipeline_stages as stages
from google.cloud.firestore_v1._helpers import GeoPoint
from google.cloud.firestore_v1.base_pipeline import _BasePipeline
from google.cloud.firestore_v1.base_vector_query import DistanceMeasure
from google.cloud.firestore_v1.pipeline_expressions import (
    Constant,
    DocumentMatches,
    Field,
    Ordering,
)
from google.cloud.firestore_v1.types.document import Value
from google.cloud.firestore_v1.vector import Vector


class TestStage:
    def test_ctor(self):
        """
        Base class should be abstract
        """
        with pytest.raises(TypeError):
            stages.Stage()


class TestAddFields:
    def _make_one(self, *args, **kwargs):
        return stages.AddFields(*args, **kwargs)

    def test_ctor(self):
        field1 = Field.of("field1")
        field2_aliased = Field.of("field2").as_("alias2")
        instance = self._make_one(field1, field2_aliased)
        assert instance.fields == [field1, field2_aliased]
        assert instance.name == "add_fields"

    def test_repr(self):
        field1 = Field.of("field1").as_("f1")
        instance = self._make_one(field1)
        repr_str = repr(instance)
        assert repr_str == "AddFields(fields=[Field.of('field1').as_('f1')])"

    def test_to_pb(self):
        field1 = Field.of("field1")
        field2_aliased = Field.of("field2").as_("alias2")
        instance = self._make_one(field1, field2_aliased)
        result = instance._to_pb()
        assert result.name == "add_fields"
        assert len(result.args) == 1
        expected_map_value = {
            "fields": {
                "field1": Value(field_reference_value="field1"),
                "alias2": Value(field_reference_value="field2"),
            }
        }
        assert result.args[0].map_value.fields == expected_map_value["fields"]
        assert len(result.options) == 0


class TestAggregate:
    def _make_one(self, *args, **kwargs):
        return stages.Aggregate(*args, **kwargs)

    def test_ctor_positional(self):
        """test with only positional arguments"""
        sum_total = Field.of("total").sum().as_("sum_total")
        avg_price = Field.of("price").average().as_("avg_price")
        instance = self._make_one(sum_total, avg_price)
        assert list(instance.accumulators) == [sum_total, avg_price]
        assert len(instance.groups) == 0
        assert instance.name == "aggregate"

    def test_ctor_keyword(self):
        """test with only keyword arguments"""
        sum_total = Field.of("total").sum().as_("sum_total")
        avg_price = Field.of("price").average().as_("avg_price")
        group_category = Field.of("category")
        instance = self._make_one(
            accumulators=[avg_price, sum_total], groups=[group_category, "city"]
        )
        assert instance.accumulators == [avg_price, sum_total]
        assert len(instance.groups) == 2
        assert instance.groups[0] == group_category
        assert isinstance(instance.groups[1], Field)
        assert instance.groups[1].path == "city"
        assert instance.name == "aggregate"

    def test_ctor_combined(self):
        """test with a mix of arguments"""
        sum_total = Field.of("total").sum().as_("sum_total")
        avg_price = Field.of("price").average().as_("avg_price")
        count = Field.of("total").count().as_("count")
        with pytest.raises(ValueError):
            self._make_one(sum_total, accumulators=[avg_price, count])

    def test_repr(self):
        sum_total = Field.of("total").sum().as_("sum_total")
        group_category = Field.of("category")
        instance = self._make_one(sum_total, groups=[group_category])
        repr_str = repr(instance)
        assert (
            repr_str
            == "Aggregate(Field.of('total').sum().as_('sum_total'), groups=[Field.of('category')])"
        )

    def test_to_pb(self):
        sum_total = Field.of("total").sum().as_("sum_total")
        group_category = Field.of("category")
        instance = self._make_one(sum_total, groups=[group_category])
        result = instance._to_pb()
        assert result.name == "aggregate"
        assert len(result.args) == 2

        expected_accumulators_map = {
            "fields": {
                "sum_total": Value(
                    function_value={
                        "name": "sum",
                        "args": [Value(field_reference_value="total")],
                    }
                )
            }
        }
        assert result.args[0].map_value.fields == expected_accumulators_map["fields"]

        expected_groups_map = {
            "fields": {"category": Value(field_reference_value="category")}
        }
        assert result.args[1].map_value.fields == expected_groups_map["fields"]
        assert len(result.options) == 0


class TestCollection:
    def _make_one(self, *args, **kwargs):
        return stages.Collection(*args, **kwargs)

    @pytest.mark.parametrize(
        "input_arg,expected",
        [
            ("test", "Collection(path='/test')"),
            ("/test", "Collection(path='/test')"),
        ],
    )
    def test_repr(self, input_arg, expected):
        instance = self._make_one(input_arg)
        repr_str = repr(instance)
        assert repr_str == expected

    def test_to_pb(self):
        input_arg = "test/col"
        instance = self._make_one(input_arg)
        result = instance._to_pb()
        assert result.name == "collection"
        assert len(result.args) == 1
        assert result.args[0].reference_value == "/test/col"
        assert len(result.options) == 0


class TestCollectionGroup:
    def _make_one(self, *args, **kwargs):
        return stages.CollectionGroup(*args, **kwargs)

    def test_repr(self):
        input_arg = "test"
        instance = self._make_one(input_arg)
        repr_str = repr(instance)
        assert repr_str == "CollectionGroup(collection_id='test')"

    def test_to_pb(self):
        input_arg = "test"
        instance = self._make_one(input_arg)
        result = instance._to_pb()
        assert result.name == "collection_group"
        assert len(result.args) == 2
        assert result.args[0].reference_value == ""
        assert result.args[1].string_value == "test"
        assert len(result.options) == 0


class TestDatabase:
    def _make_one(self, *args, **kwargs):
        return stages.Database(*args, **kwargs)

    def test_ctor(self):
        instance = self._make_one()
        assert instance.name == "database"

    def test_repr(self):
        instance = self._make_one()
        repr_str = repr(instance)
        assert repr_str == "Database()"

    def test_to_pb(self):
        instance = self._make_one()
        result = instance._to_pb()
        assert result.name == "database"
        assert len(result.args) == 0
        assert len(result.options) == 0


class TestDistinct:
    def _make_one(self, *args, **kwargs):
        return stages.Distinct(*args, **kwargs)

    def test_ctor(self):
        field1 = Field.of("field1")
        instance = self._make_one("field2", field1)
        assert len(instance.fields) == 2
        assert isinstance(instance.fields[0], Field)
        assert instance.fields[0].path == "field2"
        assert instance.fields[1] == field1
        assert instance.name == "distinct"

    def test_repr(self):
        instance = self._make_one("field1", Field.of("field2"))
        repr_str = repr(instance)
        assert repr_str == "Distinct(fields=[Field.of('field1'), Field.of('field2')])"

    def test_to_pb(self):
        instance = self._make_one("field1", Field.of("field2"))
        result = instance._to_pb()
        assert result.name == "distinct"
        assert len(result.args) == 1
        expected_map_value = {
            "fields": {
                "field1": Value(field_reference_value="field1"),
                "field2": Value(field_reference_value="field2"),
            }
        }
        assert result.args[0].map_value.fields == expected_map_value["fields"]
        assert len(result.options) == 0


class TestDocuments:
    def _make_one(self, *args, **kwargs):
        return stages.Documents(*args, **kwargs)

    def test_ctor(self):
        instance = self._make_one("/projects/p/databases/d/documents/c/doc1", "/c/doc2")
        assert instance.paths == ("/projects/p/databases/d/documents/c/doc1", "/c/doc2")
        assert instance.name == "documents"

    def test_of(self):
        mock_doc_ref1 = mock.Mock()
        mock_doc_ref1.path = "projects/p/databases/d/documents/c/doc1"
        mock_doc_ref2 = mock.Mock()
        mock_doc_ref2.path = "c/doc2"  # Test relative path as well
        instance = stages.Documents.of(mock_doc_ref1, mock_doc_ref2)
        assert instance.paths == (
            "/projects/p/databases/d/documents/c/doc1",
            "/c/doc2",
        )

    def test_repr(self):
        instance = self._make_one("/a/b", "/c/d")
        repr_str = repr(instance)
        assert repr_str == "Documents('/a/b', '/c/d')"

    def test_to_pb(self):
        instance = self._make_one("/projects/p/databases/d/documents/c/doc1", "/c/doc2")
        result = instance._to_pb()
        assert result.name == "documents"
        assert len(result.args) == 2
        assert (
            result.args[0].reference_value == "/projects/p/databases/d/documents/c/doc1"
        )
        assert result.args[1].reference_value == "/c/doc2"
        assert len(result.options) == 0


class TestFindNearest:
    class TestFindNearestOptions:
        def _make_one_options(self, *args, **kwargs):
            return stages.FindNearestOptions(*args, **kwargs)

        def test_ctor_options(self):
            limit_val = 10
            distance_field_val = Field.of("dist")
            instance = self._make_one_options(
                limit=limit_val, distance_field=distance_field_val
            )
            assert instance.limit == limit_val
            assert instance.distance_field == distance_field_val

        def test_ctor_defaults(self):
            instance_default = self._make_one_options()
            assert instance_default.limit is None
            assert instance_default.distance_field is None

        def test_repr(self):
            instance_empty = self._make_one_options()
            assert repr(instance_empty) == "FindNearestOptions()"
            instance_limit = self._make_one_options(limit=5)
            assert repr(instance_limit) == "FindNearestOptions(limit=5)"
            instance_distance = self._make_one_options(distance_field=Field.of("dist"))
            assert (
                repr(instance_distance)
                == "FindNearestOptions(distance_field=Field.of('dist'))"
            )
            instance_full = self._make_one_options(
                limit=5, distance_field=Field.of("dist")
            )
            assert (
                repr(instance_full)
                == "FindNearestOptions(limit=5, distance_field=Field.of('dist'))"
            )

    def _make_one(self, *args, **kwargs):
        return stages.FindNearest(*args, **kwargs)

    def test_ctor_w_str_field(self):
        field_path = "embedding_field"
        vector_val = Vector([1.0, 2.0, 3.0])
        distance_measure_val = DistanceMeasure.EUCLIDEAN
        options_val = stages.FindNearestOptions(
            limit=5, distance_field=Field.of("distance")
        )

        instance_str_field = self._make_one(
            field_path, vector_val, distance_measure_val, options=options_val
        )
        assert isinstance(instance_str_field.field, Field)
        assert instance_str_field.field.path == field_path
        assert instance_str_field.vector == vector_val
        assert instance_str_field.distance_measure == distance_measure_val
        assert instance_str_field.options == options_val
        assert instance_str_field.name == "find_nearest"

    def test_ctor_w_field_obj(self):
        field_path = "embedding_field"
        field_obj = Field.of(field_path)
        vector_val = Vector([1.0, 2.0, 3.0])
        distance_measure_val = DistanceMeasure.EUCLIDEAN
        instance_field_obj = self._make_one(field_obj, vector_val, distance_measure_val)
        assert instance_field_obj.field == field_obj
        assert instance_field_obj.options.limit is None  # Default options
        assert instance_field_obj.options.distance_field is None

    def test_ctor_w_vector_list(self):
        field_path = "embedding_field"
        distance_measure_val = DistanceMeasure.EUCLIDEAN

        vector_list = [4.0, 5.0]
        instance_list_vector = self._make_one(
            field_path, vector_list, distance_measure_val
        )
        assert isinstance(instance_list_vector.vector, Vector)
        assert instance_list_vector.vector == Vector(vector_list)

    def test_repr(self):
        field_path = "embedding_field"
        vector_val = Vector([1.0, 2.0])
        distance_measure_val = DistanceMeasure.EUCLIDEAN
        options_val = stages.FindNearestOptions(limit=5)
        instance = self._make_one(
            field_path, vector_val, distance_measure_val, options=options_val
        )
        repr_str = repr(instance)
        expected_repr = "FindNearest(field=Field.of('embedding_field'), vector=Vector<1.0, 2.0>, distance_measure=<DistanceMeasure.EUCLIDEAN: 1>, options=FindNearestOptions(limit=5))"
        assert repr_str == expected_repr

    @pytest.mark.parametrize(
        "distance_measure_val, expected_str",
        [
            (DistanceMeasure.COSINE, "cosine"),
            (DistanceMeasure.DOT_PRODUCT, "dot_product"),
            (DistanceMeasure.EUCLIDEAN, "euclidean"),
        ],
    )
    def test_to_pb(self, distance_measure_val, expected_str):
        field_path = "embedding"
        vector_val = Vector([0.1, 0.2])
        options_val = stages.FindNearestOptions(
            limit=7, distance_field=Field.of("dist_val")
        )
        instance = self._make_one(
            field_path, vector_val, distance_measure_val, options=options_val
        )

        result = instance._to_pb()
        assert result.name == "find_nearest"
        assert len(result.args) == 3
        # test field arg
        assert result.args[0].field_reference_value == field_path
        # test for vector arg
        assert result.args[1].map_value.fields["__type__"].string_value == "__vector__"
        assert (
            result.args[1].map_value.fields["value"].array_value.values[0].double_value
            == 0.1
        )
        assert (
            result.args[1].map_value.fields["value"].array_value.values[1].double_value
            == 0.2
        )
        # test for distance measure arg
        assert result.args[2].string_value == expected_str
        # test options
        assert len(result.options) == 2
        assert result.options["limit"].integer_value == 7
        assert result.options["distance_field"].field_reference_value == "dist_val"

    def test_to_pb_no_options(self):
        instance = self._make_one("emb", [1.0], DistanceMeasure.DOT_PRODUCT)
        result = instance._to_pb()
        assert len(result.options) == 0
        assert len(result.args) == 3


class TestRawStage:
    def _make_one(self, *args, **kwargs):
        return stages.RawStage(*args, **kwargs)

    @pytest.mark.parametrize(
        "input_args,expected_params",
        [
            (("name",), []),
            (("custom", Value(string_value="val")), [Value(string_value="val")]),
            (("n", Value(integer_value=1)), [Value(integer_value=1)]),
            (("n", Constant.of(1)), [Value(integer_value=1)]),
            (
                ("n", Constant.of(True), Constant.of(False)),
                [Value(boolean_value=True), Value(boolean_value=False)],
            ),
            (
                ("n", Constant.of(GeoPoint(1, 2))),
                [Value(geo_point_value={"latitude": 1, "longitude": 2})],
            ),
            (("n", Constant.of(None)), [Value(null_value=0)]),
            (
                ("n", Constant.of([0, 1, 2])),
                [
                    Value(
                        array_value={
                            "values": [Value(integer_value=n) for n in range(3)]
                        }
                    )
                ],
            ),
            (
                ("n", Value(reference_value="/projects/p/databases/d/documents/doc")),
                [Value(reference_value="/projects/p/databases/d/documents/doc")],
            ),
            (
                ("n", Constant.of({"a": "b"})),
                [Value(map_value={"fields": {"a": Value(string_value="b")}})],
            ),
        ],
    )
    def test_ctor_with_params(self, input_args, expected_params):
        instance = self._make_one(*input_args)
        assert instance.params == expected_params

    def test_ctor_with_options(self):
        options = {"index_field": Field.of("index")}
        field = Field.of("field")
        alias = Field.of("alias")
        standard_unnest = stages.Unnest(
            field, alias, options=stages.UnnestOptions(**options)
        )
        generic_unnest = stages.RawStage("unnest", field, alias, options=options)
        assert standard_unnest._pb_args() == generic_unnest._pb_args()
        assert standard_unnest._pb_options() == generic_unnest._pb_options()
        assert standard_unnest._to_pb() == generic_unnest._to_pb()

    @pytest.mark.parametrize(
        "input_args,expected",
        [
            (("name",), "RawStage(name='name')"),
            (("custom", Value(string_value="val")), "RawStage(name='custom')"),
        ],
    )
    def test_repr(self, input_args, expected):
        instance = self._make_one(*input_args)
        repr_str = repr(instance)
        assert repr_str == expected

    def test_to_pb(self):
        instance = self._make_one("name", Constant.of(True), Constant.of("test"))
        result = instance._to_pb()
        assert result.name == "name"
        assert len(result.args) == 2
        assert result.args[0].boolean_value is True
        assert result.args[1].string_value == "test"
        assert len(result.options) == 0


class TestLimit:
    def _make_one(self, *args, **kwargs):
        return stages.Limit(*args, **kwargs)

    def test_repr(self):
        instance = self._make_one(10)
        repr_str = repr(instance)
        assert repr_str == "Limit(limit=10)"

    def test_to_pb(self):
        instance = self._make_one(5)
        result = instance._to_pb()
        assert result.name == "limit"
        assert len(result.args) == 1
        assert result.args[0].integer_value == 5
        assert len(result.options) == 0


class TestLiterals:
    def _make_one(self, *args, **kwargs):
        return stages.Literals(*args, **kwargs)

    def test_ctor(self):
        val1 = {"a": Field.of("a")}
        val2 = {"b": 2}
        instance = self._make_one(val1, val2)
        assert instance.documents == (val1, val2)
        assert instance.name == "literals"

    def test_ctor_extended_types(self):
        import datetime

        from google.cloud.firestore_v1._helpers import GeoPoint
        from google.cloud.firestore_v1.vector import Vector

        doc = {
            "a": 1,
            "b": "string",
            "c": 3.14,
            "d": True,
            "e": None,
            "f": b"bytes",
            "g": datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc),
            "h": GeoPoint(1.0, 2.0),
            "i": Vector([1.0, 2.0]),
        }
        instance = self._make_one(doc)
        assert instance.documents == (doc,)
        assert instance.name == "literals"

    def test_ctor_w_expressions(self):
        from google.cloud.firestore_v1.pipeline_expressions import FunctionExpression

        expr = FunctionExpression("string_concat", [Constant("A"), Constant("B")])
        doc = {"res": expr}
        instance = self._make_one(doc)
        assert instance.documents == (doc,)
        assert instance.name == "literals"

    def test_repr(self):
        from google.cloud.firestore_v1.pipeline_expressions import Field

        val1 = {"a": Field.of("a")}
        instance = self._make_one(val1, {"b": 2})
        repr_str = repr(instance)
        assert repr_str == "Literals(documents=({'a': Field.of('a')}, {'b': 2}))"

    def test_to_pb_constant_types(self):
        import datetime

        from google.cloud.firestore_v1._helpers import GeoPoint
        from google.cloud.firestore_v1.vector import Vector

        doc = {
            "a": 1,
            "b": "string",
            "c": 3.14,
            "d": True,
            "e": None,
            "f": b"bytes",
            "g": datetime.datetime(2025, 1, 1, tzinfo=datetime.timezone.utc),
            "h": GeoPoint(1.0, 2.0),
            "i": Vector([1.0, 2.0]),
        }
        instance = self._make_one(doc)
        result = instance._to_pb()
        assert result.name == "literals"
        assert len(result.args) == 1

        fields = result.args[0].map_value.fields
        assert fields["a"].integer_value == 1
        assert fields["b"].string_value == "string"
        assert fields["c"].double_value == 3.14
        assert fields["d"].boolean_value is True
        assert fields["e"].null_value == 0
        assert fields["f"].bytes_value == b"bytes"
        assert fields["g"].timestamp_value == datetime.datetime(
            2025, 1, 1, tzinfo=datetime.timezone.utc
        )
        assert fields["h"].geo_point_value.latitude == 1.0
        assert fields["h"].geo_point_value.longitude == 2.0
        assert (
            fields["i"].map_value.fields["value"].array_value.values[0].double_value
            == 1.0
        )
        assert (
            fields["i"].map_value.fields["value"].array_value.values[1].double_value
            == 2.0
        )

    def test_to_pb_w_expression(self):
        from google.cloud.firestore_v1.pipeline_expressions import FunctionExpression

        expr = FunctionExpression("string_concat", [Constant("A"), Constant("B")])
        doc = {"res": expr}
        instance = self._make_one(doc)
        result = instance._to_pb()
        assert result.name == "literals"
        assert len(result.args) == 1

        fields = result.args[0].map_value.fields
        assert fields["res"].function_value.name == "string_concat"
        assert fields["res"].function_value.args[0].string_value == "A"
        assert fields["res"].function_value.args[1].string_value == "B"


class TestOffset:
    def _make_one(self, *args, **kwargs):
        return stages.Offset(*args, **kwargs)

    def test_repr(self):
        instance = self._make_one(20)
        repr_str = repr(instance)
        assert repr_str == "Offset(offset=20)"

    def test_to_pb(self):
        instance = self._make_one(3)
        result = instance._to_pb()
        assert result.name == "offset"
        assert len(result.args) == 1
        assert result.args[0].integer_value == 3
        assert len(result.options) == 0


class TestRemoveFields:
    def _make_one(self, *args, **kwargs):
        return stages.RemoveFields(*args, **kwargs)

    def test_ctor(self):
        field1 = Field.of("field1")
        instance = self._make_one("field2", field1)
        assert len(instance.fields) == 2
        assert isinstance(instance.fields[0], Field)
        assert instance.fields[0].path == "field2"
        assert instance.fields[1] == field1
        assert instance.name == "remove_fields"

    def test_repr(self):
        instance = self._make_one("field1", Field.of("field2"))
        repr_str = repr(instance)
        assert repr_str == "RemoveFields(Field.of('field1'), Field.of('field2'))"

    def test_to_pb(self):
        instance = self._make_one("field1", Field.of("field2"))
        result = instance._to_pb()
        assert result.name == "remove_fields"
        assert len(result.args) == 2
        assert result.args[0].field_reference_value == "field1"
        assert result.args[1].field_reference_value == "field2"
        assert len(result.options) == 0


class TestReplaceWith:
    def _make_one(self, *args, **kwargs):
        return stages.ReplaceWith(*args, **kwargs)

    @pytest.mark.parametrize(
        "in_field,expected_field",
        [
            ("test", Field.of("test")),
            ("test", Field.of("test")),
            ("test", Field.of("test")),
            (Field.of("test"), Field.of("test")),
            (Field.of("test"), Field.of("test")),
        ],
    )
    def test_ctor(self, in_field, expected_field):
        instance = self._make_one(in_field)
        assert instance.field == expected_field
        assert instance.name == "replace_with"

    def test_repr(self):
        instance = self._make_one("test")
        repr_str = repr(instance)
        assert repr_str == "ReplaceWith(field=Field.of('test'))"

    def test_to_pb(self):
        instance = self._make_one(Field.of("test"))
        result = instance._to_pb()
        assert result.name == "replace_with"
        assert len(result.args) == 2
        assert result.args[0].field_reference_value == "test"
        assert result.args[1].string_value == "full_replace"


class TestSample:
    class TestSampleOptions:
        def test_ctor_percent(self):
            instance = stages.SampleOptions(0.25, stages.SampleOptions.Mode.PERCENT)
            assert instance.value == 0.25
            assert instance.mode == stages.SampleOptions.Mode.PERCENT

        def test_ctor_documents(self):
            instance = stages.SampleOptions(10, stages.SampleOptions.Mode.DOCUMENTS)
            assert instance.value == 10
            assert instance.mode == stages.SampleOptions.Mode.DOCUMENTS

        def test_percentage(self):
            instance = stages.SampleOptions.percentage(1)
            assert instance.value == 1
            assert instance.mode == stages.SampleOptions.Mode.PERCENT

        def test_doc_limit(self):
            instance = stages.SampleOptions.doc_limit(2)
            assert instance.value == 2
            assert instance.mode == stages.SampleOptions.Mode.DOCUMENTS

        def test_repr_percentage(self):
            instance = stages.SampleOptions.percentage(0.5)
            assert repr(instance) == "SampleOptions.percentage(0.5)"

        def test_repr_documents(self):
            instance = stages.SampleOptions.doc_limit(10)
            assert repr(instance) == "SampleOptions.doc_limit(10)"

    def _make_one(self, *args, **kwargs):
        return stages.Sample(*args, **kwargs)

    def test_ctor_w_int(self):
        instance_int = self._make_one(10)
        assert isinstance(instance_int.options, stages.SampleOptions)
        assert instance_int.options.value == 10
        assert instance_int.options.mode == stages.SampleOptions.Mode.DOCUMENTS
        assert instance_int.name == "sample"

    def test_ctor_w_options(self):
        options = stages.SampleOptions.percentage(0.5)
        instance_options = self._make_one(options)
        assert instance_options.options == options
        assert instance_options.name == "sample"

    def test_repr(self):
        instance_int = self._make_one(10)
        repr_str_int = repr(instance_int)
        assert repr_str_int == "Sample(options=SampleOptions.doc_limit(10))"

        options = stages.SampleOptions.percentage(0.5)
        instance_options = self._make_one(options)
        repr_str_options = repr(instance_options)
        assert repr_str_options == "Sample(options=SampleOptions.percentage(0.5))"

    def test_to_pb_documents_mode(self):
        instance_docs = self._make_one(10)
        result_docs = instance_docs._to_pb()
        assert result_docs.name == "sample"
        assert len(result_docs.args) == 2
        assert result_docs.args[0].integer_value == 10
        assert result_docs.args[1].string_value == "documents"
        assert len(result_docs.options) == 0

    def test_to_pb_percent_mode(self):
        options_percent = stages.SampleOptions.percentage(0.25)
        instance_percent = self._make_one(options_percent)
        result_percent = instance_percent._to_pb()
        assert result_percent.name == "sample"
        assert len(result_percent.args) == 2
        assert result_percent.args[0].double_value == 0.25
        assert result_percent.args[1].string_value == "percent"
        assert len(result_percent.options) == 0


class TestSearch:
    def test_search_defaults(self):
        options = stages.SearchOptions(query="technology")
        assert options.query.name == "document_matches"
        assert options.limit is None
        assert options.retrieval_depth is None
        assert options.sort is None
        assert options.add_fields is None
        assert options.offset is None
        assert options.language_code is None

        stage = stages.Search(options)
        pb_opts = stage._pb_options()
        assert "query" in pb_opts
        assert "limit" not in pb_opts
        assert "retrieval_depth" not in pb_opts

    def test_search_full_options(self):
        options = stages.SearchOptions(
            query=DocumentMatches("tech"),
            limit=10,
            retrieval_depth=2,
            sort=Ordering("score", Ordering.Direction.DESCENDING),
            add_fields=[Field("extra")],
            offset=5,
            language_code="en",
        )
        assert options.limit == 10
        assert options.retrieval_depth == 2
        assert len(options.sort) == 1
        assert options.offset == 5
        assert options.language_code == "en"

        stage = stages.Search(options)
        pb_opts = stage._pb_options()

        assert pb_opts["limit"].integer_value == 10
        assert pb_opts["retrieval_depth"].integer_value == 2
        assert len(pb_opts["sort"].array_value.values) == 1
        assert pb_opts["offset"].integer_value == 5
        assert pb_opts["language_code"].string_value == "en"
        assert "query" in pb_opts

    def test_search_string_query_wrapping(self):
        options = stages.SearchOptions(query="science")
        assert options.query.name == "document_matches"
        assert options.query.params[0].value == "science"

    def test_search_with_string(self):
        stage = stages.Search("technology")
        assert isinstance(stage.options, stages.SearchOptions)
        assert stage.options.query.name == "document_matches"
        assert stage.options.query.params[0].value == "technology"
        pb_opts = stage._pb_options()
        assert "query" in pb_opts

    def test_search_with_boolean_expression(self):
        expr = DocumentMatches("tech")
        stage = stages.Search(expr)
        assert isinstance(stage.options, stages.SearchOptions)
        assert stage.options.query is expr
        pb_opts = stage._pb_options()
        assert "query" in pb_opts


class TestSelect:
    def _make_one(self, *args, **kwargs):
        return stages.Select(*args, **kwargs)

    def test_repr(self):
        instance = self._make_one("field1", Field.of("field2"))
        repr_str = repr(instance)
        assert (
            repr_str == "Select(projections=[Field.of('field1'), Field.of('field2')])"
        )

    def test_to_pb(self):
        instance = self._make_one("field1", "field2.subfield", Field.of("field3"))
        result = instance._to_pb()
        assert result.name == "select"
        assert len(result.args) == 1
        got_map = result.args[0].map_value.fields
        assert got_map.get("field1").field_reference_value == "field1"
        assert got_map.get("field2.subfield").field_reference_value == "field2.subfield"
        assert got_map.get("field3").field_reference_value == "field3"
        assert len(result.options) == 0


class TestSort:
    def _make_one(self, *args, **kwargs):
        return stages.Sort(*args, **kwargs)

    def test_repr(self):
        order1 = Ordering(Field.of("field1"), "ASCENDING")
        instance = self._make_one(order1)
        repr_str = repr(instance)
        assert repr_str == "Sort(orders=[Field.of('field1').ascending()])"

    def test_to_pb(self):
        order1 = Ordering(Field.of("name"), "ASCENDING")
        order2 = Ordering(Field.of("age"), "DESCENDING")
        instance = self._make_one(order1, order2)
        result = instance._to_pb()
        assert result.name == "sort"
        assert len(result.args) == 2
        got_map = result.args[0].map_value.fields
        assert got_map.get("expression").field_reference_value == "name"
        assert got_map.get("direction").string_value == "ascending"
        assert len(result.options) == 0


class TestUnion:
    def _make_one(self, *args, **kwargs):
        return stages.Union(*args, **kwargs)

    def test_ctor(self):
        mock_pipeline = mock.Mock(spec=_BasePipeline)
        instance = self._make_one(mock_pipeline)
        assert instance.other == mock_pipeline
        assert instance.name == "union"

    def test_repr(self):
        test_pipeline = _BasePipeline(mock.Mock()).sample(5)
        instance = self._make_one(test_pipeline)
        repr_str = repr(instance)
        assert repr_str == f"Union(other={test_pipeline!r})"

    def test_to_pb(self):
        test_pipeline = _BasePipeline(mock.Mock()).sample(5)

        instance = self._make_one(test_pipeline)
        result = instance._to_pb()

        assert result.name == "union"
        assert len(result.args) == 1
        assert result.args[0].pipeline_value == test_pipeline._to_pb().pipeline
        assert len(result.options) == 0


class TestUnnest:
    class TestUnnestOptions:
        def _make_one_options(self, *args, **kwargs):
            return stages.UnnestOptions(*args, **kwargs)

        def test_ctor_options(self):
            index_field_val = "my_index"
            instance = self._make_one_options(index_field=index_field_val)
            assert isinstance(instance.index_field, Field)
            assert instance.index_field.path == index_field_val

        def test_repr(self):
            instance = self._make_one_options(index_field="my_idx")
            repr_str = repr(instance)
            assert repr_str == "UnnestOptions(index_field='my_idx')"

    def _make_one(self, *args, **kwargs):
        return stages.Unnest(*args, **kwargs)

    def test_ctor(self):
        instance = self._make_one("my_field")
        assert isinstance(instance.field, Field)
        assert instance.field.path == "my_field"
        assert isinstance(instance.alias, Field)
        assert instance.alias.path == "my_field"
        assert instance.options is None
        assert instance.name == "unnest"

    def test_ctor_full(self):
        """constructor with alias and options set"""
        field = Field.of("items")
        alias = Field.of("alias")
        options = stages.UnnestOptions(index_field="item_index")
        instance = self._make_one(field, alias, options=options)
        assert isinstance(field, Field)
        assert instance.field == field
        assert isinstance(alias, Field)
        assert instance.alias == alias
        assert instance.options == options
        assert instance.name == "unnest"

    def test_repr(self):
        instance_simple = self._make_one("my_field")
        repr_str_simple = repr(instance_simple)
        assert (
            repr_str_simple
            == "Unnest(field=Field.of('my_field'), alias=Field.of('my_field'), options=None)"
        )

        options = stages.UnnestOptions(index_field="item_idx")
        instance_full = self._make_one(
            Field.of("items"), Field.of("alias"), options=options
        )
        repr_str_full = repr(instance_full)
        assert (
            repr_str_full
            == "Unnest(field=Field.of('items'), alias=Field.of('alias'), options=UnnestOptions(index_field='item_idx'))"
        )

    def test_to_pb(self):
        instance = self._make_one(Field.of("dataPoints"))
        result = instance._to_pb()
        assert result.name == "unnest"
        assert len(result.args) == 2
        assert result.args[0].field_reference_value == "dataPoints"
        assert result.args[1].field_reference_value == "dataPoints"
        assert len(result.options) == 0

    def test_to_pb_full(self):
        field_str = "items"
        alias_str = "single_item"
        options_val = stages.UnnestOptions(index_field="item_index")
        instance = self._make_one(field_str, alias_str, options=options_val)

        result = instance._to_pb()
        assert result.name == "unnest"
        assert len(result.args) == 2
        assert result.args[0].field_reference_value == field_str
        assert result.args[1].field_reference_value == alias_str

        assert len(result.options) == 1
        assert result.options["index_field"].field_reference_value == "item_index"


class TestWhere:
    def _make_one(self, *args, **kwargs):
        return stages.Where(*args, **kwargs)

    def test_repr(self):
        condition = Field.of("age").greater_than(30)
        instance = self._make_one(condition)
        repr_str = repr(instance)
        assert (
            repr_str == "Where(condition=Field.of('age').greater_than(Constant.of(30)))"
        )

    def test_to_pb(self):
        condition = Field.of("city").equal("SF")
        instance = self._make_one(condition)
        result = instance._to_pb()
        assert result.name == "where"
        assert len(result.args) == 1
        got_fn = result.args[0].function_value
        assert got_fn.name == "equal"
        assert len(got_fn.args) == 2
        assert got_fn.args[0].field_reference_value == "city"
        assert got_fn.args[1].string_value == "SF"
        assert len(result.options) == 0


class TestDelete:
    def _make_one(self):
        return stages.Delete()

    def test_to_pb(self):
        instance = self._make_one()
        result = instance._to_pb()
        assert result.name == "delete"
        assert len(result.args) == 0
        assert len(result.options) == 0


class TestUpdate:
    def _make_one(self, *args):
        return stages.Update(*args)

    def test_to_pb_empty(self):
        instance = self._make_one()
        result = instance._to_pb()
        assert result.name == "update"
        assert len(result.args) == 1
        assert result.args[0].map_value.fields == {}
        assert len(result.options) == 0

    def test_to_pb_with_fields(self):
        instance = self._make_one(
            Field.of("score").add(10).as_("score"), Constant.of("active").as_("status")
        )
        result = instance._to_pb()
        assert result.name == "update"
        assert len(result.args) == 1
        assert "score" in result.args[0].map_value.fields
        assert "status" in result.args[0].map_value.fields
        assert len(result.options) == 0
