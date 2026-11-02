# Copyright 2017 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import datetime
import decimal
import math
import operator as op
import re
import unittest

import pytest

import google.cloud._helpers
from google.cloud.bigquery import query, table
from google.cloud.bigquery.dbapi import _helpers
from google.cloud.bigquery.dbapi import exceptions


class TestQueryParameters(unittest.TestCase):
    def test_scalar_to_query_parameter(self):
        expected_types = [
            (True, "BOOL"),
            (False, "BOOL"),
            (123, "INT64"),
            (-123456789, "INT64"),
            (1.25, "FLOAT64"),
            (b"I am some bytes", "BYTES"),
            ("I am a string", "STRING"),
            (datetime.date(2017, 4, 1), "DATE"),
            (datetime.time(12, 34, 56), "TIME"),
            (datetime.datetime(2012, 3, 4, 5, 6, 7), "DATETIME"),
            (
                datetime.datetime(
                    2012, 3, 4, 5, 6, 7, tzinfo=google.cloud._helpers.UTC
                ),
                "TIMESTAMP",
            ),
            (decimal.Decimal("1.25"), "NUMERIC"),
            (decimal.Decimal("9.9999999999999999999999999999999999999E+28"), "NUMERIC"),
            (decimal.Decimal("1.0E+29"), "BIGNUMERIC"),  # more than max NUMERIC value
            (decimal.Decimal("1.123456789"), "NUMERIC"),
            (decimal.Decimal("1.1234567891"), "BIGNUMERIC"),  # scale > 9
            (decimal.Decimal("12345678901234567890123456789.012345678"), "NUMERIC"),
            (
                decimal.Decimal("12345678901234567890123456789012345678"),
                "BIGNUMERIC",  # larger than max NUMERIC value, despite precision <=38
            ),
        ]

        for value, expected_type in expected_types:
            msg = "value: {} expected_type: {}".format(value, expected_type)
            parameter = _helpers.scalar_to_query_parameter(value)
            self.assertIsNone(parameter.name, msg=msg)
            self.assertEqual(parameter.type_, expected_type, msg=msg)
            self.assertEqual(parameter.value, value, msg=msg)
            named_parameter = _helpers.scalar_to_query_parameter(value, name="myvar")
            self.assertEqual(named_parameter.name, "myvar", msg=msg)
            self.assertEqual(named_parameter.type_, expected_type, msg=msg)
            self.assertEqual(named_parameter.value, value, msg=msg)

    def test_scalar_to_query_parameter_w_unexpected_type(self):
        with self.assertRaises(exceptions.ProgrammingError):
            _helpers.scalar_to_query_parameter(value={"a": "dictionary"})

    def test_scalar_to_query_parameter_w_special_floats(self):
        nan_parameter = _helpers.scalar_to_query_parameter(float("nan"))
        self.assertTrue(math.isnan(nan_parameter.value))
        self.assertEqual(nan_parameter.type_, "FLOAT64")
        inf_parameter = _helpers.scalar_to_query_parameter(float("inf"))
        self.assertTrue(math.isinf(inf_parameter.value))
        self.assertEqual(inf_parameter.type_, "FLOAT64")

    def test_array_to_query_parameter_valid_argument(self):
        expected_types = [
            ([True, False], "BOOL"),
            ([123, -456, 0], "INT64"),
            ([1.25, 2.50], "FLOAT64"),
            ([decimal.Decimal("1.25")], "NUMERIC"),
            ([decimal.Decimal("{d38}.{d38}".format(d38="9" * 38))], "BIGNUMERIC"),
            ([b"foo", b"bar"], "BYTES"),
            (["foo", "bar"], "STRING"),
            ([datetime.date(2017, 4, 1), datetime.date(2018, 4, 1)], "DATE"),
            ([datetime.time(12, 34, 56), datetime.time(10, 20, 30)], "TIME"),
            (
                [
                    datetime.datetime(2012, 3, 4, 5, 6, 7),
                    datetime.datetime(2013, 1, 1, 10, 20, 30),
                ],
                "DATETIME",
            ),
            (
                [
                    datetime.datetime(
                        2012, 3, 4, 5, 6, 7, tzinfo=google.cloud._helpers.UTC
                    ),
                    datetime.datetime(
                        2013, 1, 1, 10, 20, 30, tzinfo=google.cloud._helpers.UTC
                    ),
                ],
                "TIMESTAMP",
            ),
        ]

        for values, expected_type in expected_types:
            msg = "value: {} expected_type: {}".format(values, expected_type)
            parameter = _helpers.array_to_query_parameter(values)
            self.assertIsNone(parameter.name, msg=msg)
            self.assertEqual(parameter.array_type, expected_type, msg=msg)
            self.assertEqual(parameter.values, values, msg=msg)
            named_param = _helpers.array_to_query_parameter(values, name="my_param")
            self.assertEqual(named_param.name, "my_param", msg=msg)
            self.assertEqual(named_param.array_type, expected_type, msg=msg)
            self.assertEqual(named_param.values, values, msg=msg)

    def test_array_to_query_parameter_empty_argument(self):
        with self.assertRaises(exceptions.ProgrammingError):
            _helpers.array_to_query_parameter([])

    def test_array_to_query_parameter_unsupported_sequence(self):
        unsupported_iterables = [{10, 20, 30}, "foo", b"bar", bytearray([65, 75, 85])]
        for iterable in unsupported_iterables:
            with self.assertRaises(exceptions.ProgrammingError):
                _helpers.array_to_query_parameter(iterable)

    def test_array_to_query_parameter_sequence_w_invalid_elements(self):
        with self.assertRaises(exceptions.ProgrammingError):
            _helpers.array_to_query_parameter([object(), 2, 7])

    def test_to_query_parameters_w_dict(self):
        parameters = {"somebool": True, "somestring": "a-string-value"}
        query_parameters = _helpers.to_query_parameters(parameters, {})
        query_parameter_tuples = []
        for param in query_parameters:
            query_parameter_tuples.append((param.name, param.type_, param.value))
        self.assertSequenceEqual(
            sorted(query_parameter_tuples),
            sorted(
                [
                    ("somebool", "BOOL", True),
                    ("somestring", "STRING", "a-string-value"),
                ]
            ),
        )

    def test_to_query_parameters_w_dict_array_param(self):
        parameters = {"somelist": [10, 20]}
        query_parameters = _helpers.to_query_parameters(parameters, {})

        self.assertEqual(len(query_parameters), 1)
        param = query_parameters[0]

        self.assertEqual(param.name, "somelist")
        self.assertEqual(param.array_type, "INT64")
        self.assertEqual(param.values, [10, 20])

    def test_to_query_parameters_w_dict_dict_param(self):
        parameters = {"my_param": {"foo": "bar"}}

        with self.assertRaises(NotImplementedError):
            _helpers.to_query_parameters(parameters, {})

    def test_to_query_parameters_w_list(self):
        parameters = [True, "a-string-value"]
        query_parameters = _helpers.to_query_parameters(parameters, [None, None])
        query_parameter_tuples = []
        for param in query_parameters:
            query_parameter_tuples.append((param.name, param.type_, param.value))
        self.assertSequenceEqual(
            sorted(query_parameter_tuples),
            sorted([(None, "BOOL", True), (None, "STRING", "a-string-value")]),
        )

    def test_to_query_parameters_w_list_array_param(self):
        parameters = [[10, 20]]
        query_parameters = _helpers.to_query_parameters(parameters, [None])

        self.assertEqual(len(query_parameters), 1)
        param = query_parameters[0]

        self.assertIsNone(param.name)
        self.assertEqual(param.array_type, "INT64")
        self.assertEqual(param.values, [10, 20])

    def test_to_query_parameters_w_list_dict_param(self):
        parameters = [{"foo": "bar"}]

        with self.assertRaises(NotImplementedError):
            _helpers.to_query_parameters(parameters, [None])

    def test_to_query_parameters_none_argument(self):
        query_parameters = _helpers.to_query_parameters(None, None)
        self.assertEqual(query_parameters, [])


class TestToBqTableRows(unittest.TestCase):
    def test_empty_iterable(self):
        rows_iterable = iter([])
        result = _helpers.to_bq_table_rows(rows_iterable)
        self.assertEqual(list(result), [])

    def test_non_empty_iterable(self):
        pytest.importorskip("numpy")
        pytest.importorskip("pyarrow")
        from tests.unit.helpers import _to_pyarrow

        rows_iterable = [
            dict(
                one=_to_pyarrow(1.1),
                four=_to_pyarrow(1.4),
                two=_to_pyarrow(1.2),
                three=_to_pyarrow(1.3),
            ),
            dict(
                one=_to_pyarrow(2.1),
                four=_to_pyarrow(2.4),
                two=_to_pyarrow(2.2),
                three=_to_pyarrow(2.3),
            ),
        ]

        result = _helpers.to_bq_table_rows(rows_iterable)

        rows = list(result)
        self.assertEqual(len(rows), 2)

        row_1, row_2 = rows
        self.assertIsInstance(row_1, table.Row)
        self.assertIsInstance(row_2, table.Row)

        field_value = op.itemgetter(1)

        items = sorted(row_1.items(), key=field_value)
        expected_items = [("one", 1.1), ("two", 1.2), ("three", 1.3), ("four", 1.4)]
        self.assertEqual(items, expected_items)

        items = sorted(row_2.items(), key=field_value)
        expected_items = [("one", 2.1), ("two", 2.2), ("three", 2.3), ("four", 2.4)]
        self.assertEqual(items, expected_items)


class TestRaiseOnClosedDecorator(unittest.TestCase):
    def _make_class(self):
        class Foo(object):
            class_member = "class member"

            def __init__(self):
                self._closed = False
                self.instance_member = "instance member"

            def instance_method(self):
                return self.instance_member

            @classmethod
            def class_method(cls):  # pragma: NO COVER
                return cls.class_member

            @staticmethod
            def static_method():  # pragma: NO COVER
                return "static return value"

            def _private_method(self):
                return self.instance_member

        return Foo

    def test_preserves_method_names(self):
        klass = self._make_class()
        decorated_class = _helpers.raise_on_closed("I'm closed!")(klass)
        instance = decorated_class()

        self.assertEqual(instance.instance_method.__name__, "instance_method")
        self.assertEqual(instance.class_method.__name__, "class_method")
        self.assertEqual(instance.static_method.__name__, "static_method")
        self.assertEqual(instance._private_method.__name__, "_private_method")

    def test_methods_on_not_closed_instance(self):
        klass = self._make_class()
        decorated_class = _helpers.raise_on_closed("I'm closed!")(klass)
        instance = decorated_class()
        instance._closed = False

        self.assertEqual(instance.instance_method(), "instance member")
        self.assertEqual(instance.class_method(), "class member")
        self.assertEqual(instance.static_method(), "static return value")
        self.assertEqual(instance._private_method(), "instance member")

    def test_public_instance_methods_on_closed_instance(self):
        klass = self._make_class()
        decorated_class = _helpers.raise_on_closed("I'm closed!")(klass)
        instance = decorated_class()
        instance._closed = True

        with self.assertRaisesRegex(exceptions.ProgrammingError, "I'm closed!"):
            instance.instance_method()

    def test_methods_wo_public_instance_methods_on_closed_instance(self):
        klass = self._make_class()
        decorated_class = _helpers.raise_on_closed("I'm closed!")(klass)
        instance = decorated_class()
        instance._closed = True

        # no errors expected
        self.assertEqual(instance.class_method(), "class member")
        self.assertEqual(instance.static_method(), "static return value")
        self.assertEqual(instance._private_method(), "instance member")

    def test_custom_class_closed_attribute(self):
        klass = self._make_class()
        decorated_class = _helpers.raise_on_closed(
            "I'm closed!", closed_attr_name="_really_closed"
        )(klass)
        instance = decorated_class()
        instance._closed = False
        instance._really_closed = True

        with self.assertRaisesRegex(exceptions.ProgrammingError, "I'm closed!"):
            instance.instance_method()

    def test_custom_on_closed_error_type(self):
        klass = self._make_class()
        decorated_class = _helpers.raise_on_closed(
            "I'm closed!", exc_class=RuntimeError
        )(klass)
        instance = decorated_class()
        instance._closed = True

        with self.assertRaisesRegex(RuntimeError, "I'm closed!"):
            instance.instance_method()


VALID_BQ_TYPES = [
    (name, getattr(query.SqlParameterScalarTypes, name)._type)
    for name in dir(query.SqlParameterScalarTypes)
    if not name.startswith("_")
]


@pytest.mark.parametrize("alias, type_", VALID_BQ_TYPES)
def test_scalar_to_query_parameter_honors_given_type(alias, type_):
    from google.cloud import bigquery

    assert _helpers.scalar_to_query_parameter(1.23, None, alias) == (
        bigquery.ScalarQueryParameter(None, type_, 1.23)
    )
    assert _helpers.scalar_to_query_parameter(None, "foo", alias) == (
        bigquery.ScalarQueryParameter("foo", type_, None)
    )


def test_scalar_to_query_parameter_honors_given_type_errors_on_invalid():
    with pytest.raises(
        google.cloud.bigquery.dbapi.exceptions.ProgrammingError,
        match="The given parameter type, INT, for foo is not a valid BigQuery scalar type.",
    ):
        _helpers.scalar_to_query_parameter(None, "foo", "INT")


@pytest.mark.parametrize("alias, type_", VALID_BQ_TYPES)
def test_array_to_query_parameter_honors_given_type(alias, type_):
    from google.cloud import bigquery

    assert _helpers.array_to_query_parameter([1.23], None, alias) == (
        bigquery.ArrayQueryParameter(None, type_, [1.23])
    )
    assert _helpers.array_to_query_parameter((), "foo", alias) == (
        bigquery.ArrayQueryParameter("foo", type_, ())
    )


def test_array_to_query_parameter_honors_given_type_errors_on_invalid():
    with pytest.raises(
        google.cloud.bigquery.dbapi.exceptions.ProgrammingError,
        match="The given parameter type, INT, for foo is not a valid BigQuery scalar type.",
    ):
        _helpers.array_to_query_parameter((), "foo", "INT")


def test_to_query_parameters_dict_w_types():
    from google.cloud import bigquery

    assert sorted(
        _helpers.to_query_parameters(
            dict(i=1, x=1.2, y=None, q="hi", z=[]),
            dict(x="numeric", y="string", q="string(9)", z="float64"),
        ),
        key=lambda p: p.name,
    ) == [
        bigquery.ScalarQueryParameter("i", "INT64", 1),
        bigquery.ScalarQueryParameter("q", "STRING", "hi"),
        bigquery.ScalarQueryParameter("x", "NUMERIC", 1.2),
        bigquery.ScalarQueryParameter("y", "STRING", None),
        bigquery.ArrayQueryParameter("z", "FLOAT64", []),
    ]


def test_to_query_parameters_list_w_types():
    from google.cloud import bigquery

    assert _helpers.to_query_parameters(
        [1, 1.2, None, "hi", []], [None, "numeric", "string", "string(9)", "float64"]
    ) == [
        bigquery.ScalarQueryParameter(None, "INT64", 1),
        bigquery.ScalarQueryParameter(None, "NUMERIC", 1.2),
        bigquery.ScalarQueryParameter(None, "STRING", None),
        bigquery.ScalarQueryParameter(None, "STRING", "hi"),
        bigquery.ArrayQueryParameter(None, "FLOAT64", []),
    ]


@pytest.mark.parametrize(
    "value,type_,expect",
    [
        (
            [],
            "ARRAY<INT64>",
            {
                "parameterType": {"type": "ARRAY", "arrayType": {"type": "INT64"}},
                "parameterValue": {"arrayValues": []},
            },
        ),
        (
            [1, 2],
            "ARRAY<INT64>",
            {
                "parameterType": {"type": "ARRAY", "arrayType": {"type": "INT64"}},
                "parameterValue": {"arrayValues": [{"value": "1"}, {"value": "2"}]},
            },
        ),
        (
            dict(
                name="par",
                children=[
                    dict(name="ch1", bdate=datetime.date(2021, 1, 1)),
                    dict(name="ch2", bdate=datetime.date(2021, 1, 2)),
                ],
            ),
            "struct<name string, children array<struct<name string, bdate date>>>",
            {
                "parameterType": {
                    "structTypes": [
                        {"name": "name", "type": {"type": "STRING"}},
                        {
                            "name": "children",
                            "type": {
                                "arrayType": {
                                    "structTypes": [
                                        {"name": "name", "type": {"type": "STRING"}},
                                        {"name": "bdate", "type": {"type": "DATE"}},
                                    ],
                                    "type": "STRUCT",
                                },
                                "type": "ARRAY",
                            },
                        },
                    ],
                    "type": "STRUCT",
                },
                "parameterValue": {
                    "structValues": {
                        "children": {
                            "arrayValues": [
                                {
                                    "structValues": {
                                        "bdate": {"value": "2021-01-01"},
                                        "name": {"value": "ch1"},
                                    }
                                },
                                {
                                    "structValues": {
                                        "bdate": {"value": "2021-01-02"},
                                        "name": {"value": "ch2"},
                                    }
                                },
                            ]
                        },
                        "name": {"value": "par"},
                    }
                },
            },
        ),
        (
            dict(
                name="par",
                children=[
                    dict(name="ch1", bdate=datetime.date(2021, 1, 1)),
                    dict(name="ch2", bdate=datetime.date(2021, 1, 2)),
                ],
            ),
            "struct<name string(9), children array<struct<name string(9), bdate date>>>",
            {
                "parameterType": {
                    "structTypes": [
                        {"name": "name", "type": {"type": "STRING"}},
                        {
                            "name": "children",
                            "type": {
                                "arrayType": {
                                    "structTypes": [
                                        {"name": "name", "type": {"type": "STRING"}},
                                        {"name": "bdate", "type": {"type": "DATE"}},
                                    ],
                                    "type": "STRUCT",
                                },
                                "type": "ARRAY",
                            },
                        },
                    ],
                    "type": "STRUCT",
                },
                "parameterValue": {
                    "structValues": {
                        "children": {
                            "arrayValues": [
                                {
                                    "structValues": {
                                        "bdate": {"value": "2021-01-01"},
                                        "name": {"value": "ch1"},
                                    }
                                },
                                {
                                    "structValues": {
                                        "bdate": {"value": "2021-01-02"},
                                        "name": {"value": "ch2"},
                                    }
                                },
                            ]
                        },
                        "name": {"value": "par"},
                    }
                },
            },
        ),
        (
            ["1", "hi"],
            "ARRAY<string(9)>",
            {
                "parameterType": {"type": "ARRAY", "arrayType": {"type": "STRING"}},
                "parameterValue": {"arrayValues": [{"value": "1"}, {"value": "hi"}]},
            },
        ),
    ],
)
def test_complex_query_parameter_type(type_, value, expect):
    from google.cloud.bigquery.dbapi._helpers import complex_query_parameter

    param = complex_query_parameter("test", value, type_).to_api_repr()
    assert param.pop("name") == "test"
    assert param == expect


def _expected_error_match(expect):
    return "^" + re.escape(expect) + "$"


@pytest.mark.parametrize(
    "value,type_,expect",
    [
        (
            [],
            "ARRAY<INT>",
            "The given parameter type, INT,"
            " is not a valid BigQuery scalar type, in ARRAY<INT>.",
        ),
        ([], "x<INT>", "Invalid parameter type, x<INT>"),
        ({}, "struct<int>", "Invalid struct field, int, in struct<int>"),
        (
            {"x": 1},
            "struct<x int>",
            "The given parameter type, int,"
            " for x is not a valid BigQuery scalar type, in struct<x int>.",
        ),
        ([], "x<<INT>", "Invalid parameter type, x<<INT>"),
        (0, "ARRAY<INT64>", "Array type with non-array-like value with type int"),
        (
            [],
            "ARRAY<ARRAY<INT64>>",
            "Array can't contain an array in ARRAY<ARRAY<INT64>>",
        ),
        ([], "struct<x int>", "Non-mapping value for type struct<x int>"),
        ({}, "struct<x int>", "No field value for x in struct<x int>"),
        ({"x": 1, "y": 1}, "struct<x int64>", "Extra data keys for struct<x int64>"),
        ([], "array<struct<xxx>>", "Invalid struct field, xxx, in array<struct<xxx>>"),
        ([], "array<<>>", "Invalid parameter type, <>"),
    ],
)
def test_complex_query_parameter_type_errors(type_, value, expect):
    from google.cloud.bigquery.dbapi._helpers import complex_query_parameter
    from google.cloud.bigquery.dbapi import exceptions

    with pytest.raises(
        exceptions.ProgrammingError,
        match=_expected_error_match(expect),
    ):
        complex_query_parameter("test", value, type_)


@pytest.mark.parametrize(
    "parameters,parameter_types,expect",
    [
        (
            [[], dict(name="ch1", b_date=datetime.date(2021, 1, 1))],
            ["ARRAY<INT64>", "struct<name string, b_date date>"],
            [
                {
                    "parameterType": {"arrayType": {"type": "INT64"}, "type": "ARRAY"},
                    "parameterValue": {"arrayValues": []},
                },
                {
                    "parameterType": {
                        "structTypes": [
                            {"name": "name", "type": {"type": "STRING"}},
                            {"name": "b_date", "type": {"type": "DATE"}},
                        ],
                        "type": "STRUCT",
                    },
                    "parameterValue": {
                        "structValues": {
                            "b_date": {"value": "2021-01-01"},
                            "name": {"value": "ch1"},
                        }
                    },
                },
            ],
        ),
        (
            dict(ids=[], child=dict(name="ch1", bdate=datetime.date(2021, 1, 1))),
            dict(ids="ARRAY<INT64>", child="struct<name string, bdate date>"),
            [
                {
                    "name": "ids",
                    "parameterType": {"arrayType": {"type": "INT64"}, "type": "ARRAY"},
                    "parameterValue": {"arrayValues": []},
                },
                {
                    "name": "child",
                    "parameterType": {
                        "structTypes": [
                            {"name": "name", "type": {"type": "STRING"}},
                            {"name": "bdate", "type": {"type": "DATE"}},
                        ],
                        "type": "STRUCT",
                    },
                    "parameterValue": {
                        "structValues": {
                            "bdate": {"value": "2021-01-01"},
                            "name": {"value": "ch1"},
                        }
                    },
                },
            ],
        ),
    ],
)
def test_to_query_parameters_complex_types(parameters, parameter_types, expect):
    from google.cloud.bigquery.dbapi._helpers import to_query_parameters

    result = [p.to_api_repr() for p in to_query_parameters(parameters, parameter_types)]
    assert result == expect


def test_to_query_parameters_struct_error():
    from google.cloud.bigquery.dbapi._helpers import to_query_parameters

    with pytest.raises(
        NotImplementedError,
        match=_expected_error_match(
            "STRUCT-like parameter values are not supported, "
            "unless an explicit type is give in the parameter placeholder "
            "(e.g. '%(:struct<...>)s')."
        ),
    ):
        to_query_parameters([dict(x=1)], [None])

    with pytest.raises(
        NotImplementedError,
        match=_expected_error_match(
            "STRUCT-like parameter values are not supported (parameter foo), "
            "unless an explicit type is give in the parameter placeholder "
            "(e.g. '%(foo:struct<...>)s')."
        ),
    ):
        to_query_parameters(dict(foo=dict(x=1)), {})
