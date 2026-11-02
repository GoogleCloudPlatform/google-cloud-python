# Copyright 2021 Google LLC
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

from unittest import mock

import pytest

from google.cloud import bigquery as bq


class TestStandardSqlDataType:
    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.standard_sql import StandardSqlDataType

        return StandardSqlDataType

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_ctor_default_type_kind(self):
        instance = self._make_one()
        assert instance.type_kind == bq.StandardSqlTypeNames.TYPE_KIND_UNSPECIFIED

    def test_to_api_repr_no_type_set(self):
        instance = self._make_one()
        instance.type_kind = None

        result = instance.to_api_repr()

        assert result == {"typeKind": "TYPE_KIND_UNSPECIFIED"}

    def test_to_api_repr_scalar_type(self):
        instance = self._make_one(bq.StandardSqlTypeNames.FLOAT64)

        result = instance.to_api_repr()

        assert result == {"typeKind": "FLOAT64"}

    def test_to_api_repr_array_type_element_type_missing(self):
        instance = self._make_one(
            bq.StandardSqlTypeNames.ARRAY, array_element_type=None
        )

        result = instance.to_api_repr()

        expected = {"typeKind": "ARRAY"}
        assert result == expected

    def test_to_api_repr_array_type_w_element_type(self):
        array_element_type = self._make_one(type_kind=bq.StandardSqlTypeNames.BOOL)
        instance = self._make_one(
            bq.StandardSqlTypeNames.ARRAY, array_element_type=array_element_type
        )

        result = instance.to_api_repr()

        expected = {"typeKind": "ARRAY", "arrayElementType": {"typeKind": "BOOL"}}
        assert result == expected

    def test_to_api_repr_struct_type_field_types_missing(self):
        instance = self._make_one(bq.StandardSqlTypeNames.STRUCT, struct_type=None)

        result = instance.to_api_repr()

        assert result == {"typeKind": "STRUCT"}

    def test_to_api_repr_struct_type_w_field_types(self):
        from google.cloud.bigquery.standard_sql import StandardSqlField
        from google.cloud.bigquery.standard_sql import StandardSqlStructType

        StandardSqlDataType = self._get_target_class()
        TypeNames = bq.StandardSqlTypeNames

        person_type = StandardSqlStructType(
            fields=[
                StandardSqlField("name", StandardSqlDataType(TypeNames.STRING)),
                StandardSqlField("age", StandardSqlDataType(TypeNames.INT64)),
            ]
        )
        employee_type = StandardSqlStructType(
            fields=[
                StandardSqlField("job_title", StandardSqlDataType(TypeNames.STRING)),
                StandardSqlField("salary", StandardSqlDataType(TypeNames.FLOAT64)),
                StandardSqlField(
                    "employee_info",
                    StandardSqlDataType(
                        type_kind=TypeNames.STRUCT,
                        struct_type=person_type,
                    ),
                ),
            ]
        )

        instance = self._make_one(TypeNames.STRUCT, struct_type=employee_type)
        result = instance.to_api_repr()

        expected = {
            "typeKind": "STRUCT",
            "structType": {
                "fields": [
                    {"name": "job_title", "type": {"typeKind": "STRING"}},
                    {"name": "salary", "type": {"typeKind": "FLOAT64"}},
                    {
                        "name": "employee_info",
                        "type": {
                            "typeKind": "STRUCT",
                            "structType": {
                                "fields": [
                                    {"name": "name", "type": {"typeKind": "STRING"}},
                                    {"name": "age", "type": {"typeKind": "INT64"}},
                                ],
                            },
                        },
                    },
                ],
            },
        }
        assert result == expected

    def test_to_api_repr_range_type_element_type_missing(self):
        instance = self._make_one(
            bq.StandardSqlTypeNames.RANGE, range_element_type=None
        )

        result = instance.to_api_repr()

        assert result == {"typeKind": "RANGE"}

    def test_to_api_repr_range_type_w_element_type(self):
        range_element_type = self._make_one(type_kind=bq.StandardSqlTypeNames.DATE)
        instance = self._make_one(
            bq.StandardSqlTypeNames.RANGE, range_element_type=range_element_type
        )

        result = instance.to_api_repr()

        assert result == {
            "typeKind": "RANGE",
            "rangeElementType": {"typeKind": "DATE"},
        }

    def test_from_api_repr_empty_resource(self):
        klass = self._get_target_class()
        result = klass.from_api_repr(resource={})

        expected = klass(
            type_kind=bq.StandardSqlTypeNames.TYPE_KIND_UNSPECIFIED,
            array_element_type=None,
            struct_type=None,
        )
        assert result == expected

    def test_from_api_repr_scalar_type(self):
        klass = self._get_target_class()
        resource = {"typeKind": "DATE"}

        result = klass.from_api_repr(resource=resource)

        expected = klass(
            type_kind=bq.StandardSqlTypeNames.DATE,
            array_element_type=None,
            struct_type=None,
        )
        assert result == expected

    def test_from_api_repr_array_type_full(self):
        klass = self._get_target_class()
        resource = {"typeKind": "ARRAY", "arrayElementType": {"typeKind": "BYTES"}}

        result = klass.from_api_repr(resource=resource)

        expected = klass(
            type_kind=bq.StandardSqlTypeNames.ARRAY,
            array_element_type=klass(type_kind=bq.StandardSqlTypeNames.BYTES),
            struct_type=None,
        )
        assert result == expected

    def test_from_api_repr_array_type_missing_element_type(self):
        klass = self._get_target_class()
        resource = {"typeKind": "ARRAY"}

        result = klass.from_api_repr(resource=resource)

        expected = klass(
            type_kind=bq.StandardSqlTypeNames.ARRAY,
            array_element_type=None,
            struct_type=None,
        )
        assert result == expected

    def test_from_api_repr_struct_type_nested(self):
        from google.cloud.bigquery.standard_sql import StandardSqlField
        from google.cloud.bigquery.standard_sql import StandardSqlStructType

        klass = self._get_target_class()
        TypeNames = bq.StandardSqlTypeNames

        resource = {
            "typeKind": "STRUCT",
            "structType": {
                "fields": [
                    {"name": "job_title", "type": {"typeKind": "STRING"}},
                    {"name": "salary", "type": {"typeKind": "FLOAT64"}},
                    {
                        "name": "employee_info",
                        "type": {
                            "typeKind": "STRUCT",
                            "structType": {
                                "fields": [
                                    {"name": "name", "type": {"typeKind": "STRING"}},
                                    {"name": "age", "type": {"typeKind": "INT64"}},
                                ],
                            },
                        },
                    },
                ],
            },
        }

        result = klass.from_api_repr(resource=resource)

        expected = klass(
            type_kind=TypeNames.STRUCT,
            struct_type=StandardSqlStructType(
                fields=[
                    StandardSqlField("job_title", klass(TypeNames.STRING)),
                    StandardSqlField("salary", klass(TypeNames.FLOAT64)),
                    StandardSqlField(
                        "employee_info",
                        klass(
                            type_kind=TypeNames.STRUCT,
                            struct_type=StandardSqlStructType(
                                fields=[
                                    StandardSqlField("name", klass(TypeNames.STRING)),
                                    StandardSqlField("age", klass(TypeNames.INT64)),
                                ]
                            ),
                        ),
                    ),
                ]
            ),
        )
        assert result == expected

    def test_from_api_repr_struct_type_missing_struct_info(self):
        klass = self._get_target_class()
        resource = {"typeKind": "STRUCT"}

        result = klass.from_api_repr(resource=resource)

        expected = klass(
            type_kind=bq.StandardSqlTypeNames.STRUCT,
            array_element_type=None,
            struct_type=None,
        )
        assert result == expected

    def test_from_api_repr_struct_type_incomplete_field_info(self):
        from google.cloud.bigquery.standard_sql import StandardSqlField
        from google.cloud.bigquery.standard_sql import StandardSqlStructType

        klass = self._get_target_class()
        TypeNames = bq.StandardSqlTypeNames

        resource = {
            "typeKind": "STRUCT",
            "structType": {
                "fields": [
                    {"type": {"typeKind": "STRING"}},  # missing name
                    {"name": "salary"},  # missing type
                ],
            },
        }

        result = klass.from_api_repr(resource=resource)

        expected = klass(
            type_kind=TypeNames.STRUCT,
            struct_type=StandardSqlStructType(
                fields=[
                    StandardSqlField(None, klass(TypeNames.STRING)),
                    StandardSqlField("salary", klass(TypeNames.TYPE_KIND_UNSPECIFIED)),
                ]
            ),
        )
        assert result == expected

    def test_from_api_repr_range_type_full(self):
        klass = self._get_target_class()
        resource = {"typeKind": "RANGE", "rangeElementType": {"typeKind": "DATE"}}

        result = klass.from_api_repr(resource=resource)

        expected = klass(
            type_kind=bq.StandardSqlTypeNames.RANGE,
            range_element_type=klass(type_kind=bq.StandardSqlTypeNames.DATE),
        )
        assert result == expected

    def test_from_api_repr_range_type_missing_element_type(self):
        klass = self._get_target_class()
        resource = {"typeKind": "RANGE"}

        result = klass.from_api_repr(resource=resource)

        expected = klass(
            type_kind=bq.StandardSqlTypeNames.RANGE,
            range_element_type=None,
            struct_type=None,
        )
        assert result == expected

    def test__eq__another_type(self):
        instance = self._make_one()

        class SqlTypeWannabe:
            pass

        not_a_type = SqlTypeWannabe()
        not_a_type._properties = instance._properties

        assert instance != not_a_type  # Can't fake it.

    def test__eq__delegates_comparison_to_another_type(self):
        instance = self._make_one()
        assert instance == mock.ANY

    def test__eq__similar_instance(self):
        kwargs = {
            "type_kind": bq.StandardSqlTypeNames.GEOGRAPHY,
            "array_element_type": bq.StandardSqlDataType(
                type_kind=bq.StandardSqlTypeNames.INT64
            ),
            "struct_type": bq.StandardSqlStructType(fields=[]),
        }
        instance = self._make_one(**kwargs)
        instance2 = self._make_one(**kwargs)
        assert instance == instance2

    @pytest.mark.parametrize(
        ("attr_name", "value", "value2"),
        (
            (
                "type_kind",
                bq.StandardSqlTypeNames.INT64,
                bq.StandardSqlTypeNames.FLOAT64,
            ),
            (
                "array_element_type",
                bq.StandardSqlDataType(type_kind=bq.StandardSqlTypeNames.STRING),
                bq.StandardSqlDataType(type_kind=bq.StandardSqlTypeNames.BOOL),
            ),
            (
                "struct_type",
                bq.StandardSqlStructType(fields=[bq.StandardSqlField(name="foo")]),
                bq.StandardSqlStructType(fields=[bq.StandardSqlField(name="bar")]),
            ),
            (
                "range_element_type",
                bq.StandardSqlDataType(type_kind=bq.StandardSqlTypeNames.DATE),
                bq.StandardSqlDataType(type_kind=bq.StandardSqlTypeNames.DATETIME),
            ),
        ),
    )
    def test__eq__attribute_differs(self, attr_name, value, value2):
        instance = self._make_one(**{attr_name: value})
        instance2 = self._make_one(**{attr_name: value2})
        assert instance != instance2

    def test_str(self):
        instance = self._make_one(type_kind=bq.StandardSqlTypeNames.BOOL)
        bool_type_repr = repr(bq.StandardSqlTypeNames.BOOL)
        assert str(instance) == f"StandardSqlDataType(type_kind={bool_type_repr}, ...)"


class TestStandardSqlField:
    # This class only contains minimum tests to cover what other tests don't

    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.standard_sql import StandardSqlField

        return StandardSqlField

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_name(self):
        instance = self._make_one(name="foo")
        assert instance.name == "foo"
        instance.name = "bar"
        assert instance.name == "bar"

    def test_type_missing(self):
        instance = self._make_one(type=None)
        assert instance.type is None

    def test_type_set_none(self):
        instance = self._make_one(
            type=bq.StandardSqlDataType(type_kind=bq.StandardSqlTypeNames.BOOL)
        )
        instance.type = None
        assert instance.type is None

    def test_type_set_not_none(self):
        instance = self._make_one(type=bq.StandardSqlDataType(type_kind=None))
        instance.type = bq.StandardSqlDataType(type_kind=bq.StandardSqlTypeNames.INT64)
        assert instance.type == bq.StandardSqlDataType(
            type_kind=bq.StandardSqlTypeNames.INT64
        )

    def test__eq__another_type(self):
        instance = self._make_one(
            name="foo",
            type=bq.StandardSqlDataType(type_kind=bq.StandardSqlTypeNames.BOOL),
        )

        class FieldWannabe:
            pass

        not_a_field = FieldWannabe()
        not_a_field._properties = instance._properties

        assert instance != not_a_field  # Can't fake it.

    def test__eq__delegates_comparison_to_another_type(self):
        instance = self._make_one(
            name="foo",
            type=bq.StandardSqlDataType(type_kind=bq.StandardSqlTypeNames.BOOL),
        )
        assert instance == mock.ANY

    def test__eq__similar_instance(self):
        kwargs = {
            "name": "foo",
            "type": bq.StandardSqlDataType(type_kind=bq.StandardSqlTypeNames.INT64),
        }
        instance = self._make_one(**kwargs)
        instance2 = self._make_one(**kwargs)
        assert instance == instance2

    @pytest.mark.parametrize(
        ("attr_name", "value", "value2"),
        (
            (
                "name",
                "foo",
                "bar",
            ),
            (
                "type",
                bq.StandardSqlDataType(type_kind=bq.StandardSqlTypeNames.INTERVAL),
                bq.StandardSqlDataType(type_kind=bq.StandardSqlTypeNames.TIME),
            ),
        ),
    )
    def test__eq__attribute_differs(self, attr_name, value, value2):
        instance = self._make_one(**{attr_name: value})
        instance2 = self._make_one(**{attr_name: value2})
        assert instance != instance2


class TestStandardSqlStructType:
    # This class only contains minimum tests to cover what other tests don't

    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.standard_sql import StandardSqlStructType

        return StandardSqlStructType

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_fields(self):
        instance = self._make_one(fields=[])
        assert instance.fields == []

        new_fields = [bq.StandardSqlField(name="foo"), bq.StandardSqlField(name="bar")]
        instance.fields = new_fields
        assert instance.fields == new_fields

    def test__eq__another_type(self):
        instance = self._make_one(fields=[bq.StandardSqlField(name="foo")])

        class StructTypeWannabe:
            pass

        not_a_type = StructTypeWannabe()
        not_a_type._properties = instance._properties

        assert instance != not_a_type  # Can't fake it.

    def test__eq__delegates_comparison_to_another_type(self):
        instance = self._make_one(fields=[bq.StandardSqlField(name="foo")])
        assert instance == mock.ANY

    def test__eq__similar_instance(self):
        kwargs = {
            "fields": [bq.StandardSqlField(name="foo"), bq.StandardSqlField(name="bar")]
        }
        instance = self._make_one(**kwargs)
        instance2 = self._make_one(**kwargs)
        assert instance == instance2

    def test__eq__attribute_differs(self):
        instance = self._make_one(fields=[bq.StandardSqlField(name="foo")])
        instance2 = self._make_one(
            fields=[bq.StandardSqlField(name="foo"), bq.StandardSqlField(name="bar")]
        )
        assert instance != instance2


class TestStandardSqlTableType:
    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.standard_sql import StandardSqlTableType

        return StandardSqlTableType

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_columns_shallow_copy(self):
        from google.cloud.bigquery.standard_sql import StandardSqlField

        columns = [
            StandardSqlField("foo"),
            StandardSqlField("bar"),
            StandardSqlField("baz"),
        ]

        instance = self._make_one(columns=columns)

        assert len(instance.columns) == 3
        columns.pop()
        assert len(instance.columns) == 3  # Still the same.

    def test_columns_setter(self):
        from google.cloud.bigquery.standard_sql import StandardSqlField

        columns = [StandardSqlField("foo")]
        instance = self._make_one(columns=columns)
        assert instance.columns == columns

        new_columns = [StandardSqlField(name="bar")]
        instance.columns = new_columns
        assert instance.columns == new_columns

    def test_to_api_repr_no_columns(self):
        instance = self._make_one(columns=[])
        result = instance.to_api_repr()
        assert result == {"columns": []}

    def test_to_api_repr_with_columns(self):
        from google.cloud.bigquery.standard_sql import StandardSqlField

        columns = [StandardSqlField("foo"), StandardSqlField("bar")]
        instance = self._make_one(columns=columns)

        result = instance.to_api_repr()

        expected = {
            "columns": [{"name": "foo", "type": None}, {"name": "bar", "type": None}]
        }
        assert result == expected

    def test_from_api_repr_missing_columns(self):
        resource = {}
        result = self._get_target_class().from_api_repr(resource)
        assert result.columns == []

    def test_from_api_repr_with_incomplete_columns(self):
        from google.cloud.bigquery.standard_sql import StandardSqlDataType
        from google.cloud.bigquery.standard_sql import StandardSqlField

        resource = {
            "columns": [
                {"type": {"typeKind": "BOOL"}},  # missing name
                {"name": "bar"},  # missing type
            ]
        }

        result = self._get_target_class().from_api_repr(resource)

        assert len(result.columns) == 2

        expected = StandardSqlField(
            name=None,
            type=StandardSqlDataType(type_kind=bq.StandardSqlTypeNames.BOOL),
        )
        assert result.columns[0] == expected

        expected = StandardSqlField(
            name="bar",
            type=StandardSqlDataType(
                type_kind=bq.StandardSqlTypeNames.TYPE_KIND_UNSPECIFIED
            ),
        )
        assert result.columns[1] == expected

    def test__eq__another_type(self):
        instance = self._make_one(columns=[bq.StandardSqlField(name="foo")])

        class TableTypeWannabe:
            pass

        not_a_type = TableTypeWannabe()
        not_a_type._properties = instance._properties

        assert instance != not_a_type  # Can't fake it.

    def test__eq__delegates_comparison_to_another_type(self):
        instance = self._make_one(columns=[bq.StandardSqlField(name="foo")])
        assert instance == mock.ANY

    def test__eq__similar_instance(self):
        kwargs = {
            "columns": [
                bq.StandardSqlField(name="foo"),
                bq.StandardSqlField(name="bar"),
            ]
        }
        instance = self._make_one(**kwargs)
        instance2 = self._make_one(**kwargs)
        assert instance == instance2

    def test__eq__attribute_differs(self):
        instance = self._make_one(columns=[bq.StandardSqlField(name="foo")])
        instance2 = self._make_one(
            columns=[bq.StandardSqlField(name="foo"), bq.StandardSqlField(name="bar")]
        )
        assert instance != instance2
