# Copyright 2015 Google LLC
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
import decimal
import unittest
from unittest import mock


class Test_UDFResource(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.query import UDFResource

        return UDFResource

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_ctor(self):
        udf = self._make_one("resourceUri", "gs://some_bucket/some_file")
        self.assertEqual(udf.udf_type, "resourceUri")
        self.assertEqual(udf.value, "gs://some_bucket/some_file")

    def test___eq__(self):
        udf = self._make_one("resourceUri", "gs://some_bucket/some_file")
        self.assertEqual(udf, udf)
        self.assertNotEqual(udf, object())
        wrong_val = self._make_one("resourceUri", "gs://some_bucket/other_file")
        self.assertNotEqual(udf, wrong_val)
        wrong_type = self._make_one("inlineCode", udf.value)
        self.assertNotEqual(udf, wrong_type)


class Test__AbstractQueryParameterType(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.query import _AbstractQueryParameterType

        return _AbstractQueryParameterType

    @classmethod
    def _make_one(cls, *args, **kw):
        return cls._get_target_class()(*args, **kw)

    def test_from_api_virtual(self):
        klass = self._get_target_class()
        with self.assertRaises(NotImplementedError):
            klass.from_api_repr({})

    def test_to_api_virtual(self):
        param_type = self._make_one()
        with self.assertRaises(NotImplementedError):
            param_type.to_api_repr()


class Test_ScalarQueryParameterType(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.query import ScalarQueryParameterType

        return ScalarQueryParameterType

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_from_api_repr(self):
        klass = self._get_target_class()
        result = klass.from_api_repr({"type": "BOOLEAN"})
        self.assertEqual(result._type, "BOOLEAN")
        self.assertIsNone(result.name)
        self.assertIsNone(result.description)

    def test_to_api_repr(self):
        param_type = self._make_one("BYTES", name="foo", description="bar")
        result = param_type.to_api_repr()
        self.assertEqual(result, {"type": "BYTES"})

    def test_repr_no_optional_attrs(self):
        param_type = self._make_one("BYTES")
        self.assertEqual(repr(param_type), "ScalarQueryParameterType('BYTES')")

    def test_repr_all_optional_attrs(self):
        param_type = self._make_one("BYTES", name="foo", description="this is foo")
        self.assertEqual(
            repr(param_type),
            "ScalarQueryParameterType('BYTES', name='foo', description='this is foo')",
        )

    def test_with_name_returns_copy_w_changed_name(self):
        param_type = self._make_one("BOOLEAN", name=None, description="Some checkbox.")
        modified_type = param_type.with_name("allow_emails")

        self.assertIsNot(modified_type, param_type)  # Result is a copy.
        self.assertEqual(modified_type.name, "allow_emails")

        # The rest of the The rest of the fields should have been preserved.
        self.assertEqual(modified_type._type, param_type._type)
        self.assertEqual(modified_type.description, param_type.description)

    def test_with_name_clearing_the_value(self):
        param_type = self._make_one(
            "BOOLEAN", name="allow_emails", description="Some checkbox."
        )
        modified_type = param_type.with_name(None)

        self.assertIsNone(modified_type.name)
        self.assertEqual(param_type.name, "allow_emails")  # original unchanged


class Test_ArrayQueryParameterType(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.query import ArrayQueryParameterType

        return ArrayQueryParameterType

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_from_api_repr(self):
        from google.cloud.bigquery.query import StructQueryParameterType

        api_resource = {
            "type": "ARRAY",
            "arrayType": {
                "type": "STRUCT",
                "structTypes": [
                    {
                        "name": "weight",
                        "type": {"type": "INTEGER"},
                        "description": "in kg",
                    },
                    {"name": "last_name", "type": {"type": "STRING"}},
                ],
            },
        }

        klass = self._get_target_class()
        result = klass.from_api_repr(api_resource)

        self.assertIsNone(result.name)
        self.assertIsNone(result.description)
        item_type = result._array_type
        self.assertIsInstance(item_type, StructQueryParameterType)

        self.assertIsNone(item_type.name)
        self.assertIsNone(item_type.description)

        field = item_type.fields[0]
        self.assertEqual(field.name, "weight")
        self.assertEqual(field.description, "in kg")
        self.assertEqual(field._type, "INTEGER")

        field = item_type.fields[1]
        self.assertEqual(field.name, "last_name")
        self.assertIsNone(field.description)
        self.assertEqual(field._type, "STRING")

    def test_to_api_repr(self):
        from google.cloud.bigquery.query import ScalarQueryParameterType
        from google.cloud.bigquery.query import StructQueryParameterType

        array_item_type = StructQueryParameterType(
            ScalarQueryParameterType("INTEGER", name="weight", description="in kg"),
            ScalarQueryParameterType("STRING", name="last_name"),
        )
        param_type = self._make_one(array_item_type, name="foo", description="bar")

        result = param_type.to_api_repr()

        expected_result = {
            "type": "ARRAY",
            "arrayType": {
                "type": "STRUCT",
                "structTypes": [
                    {
                        "name": "weight",
                        "type": {"type": "INTEGER"},
                        "description": "in kg",
                    },
                    {"name": "last_name", "type": {"type": "STRING"}},
                ],
            },
        }
        self.assertEqual(result, expected_result)

    def test_repr_no_optional_attrs(self):
        param_type = self._make_one("BOOLEAN")
        self.assertEqual(repr(param_type), "ArrayQueryParameterType('BOOLEAN')")

    def test_repr_all_optional_attrs(self):
        param_type = self._make_one("INT64", name="bar", description="this is bar")
        self.assertEqual(
            repr(param_type),
            "ArrayQueryParameterType('INT64', name='bar', description='this is bar')",
        )


class Test_StructQueryParameterType(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.query import StructQueryParameterType

        return StructQueryParameterType

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_raises_error_without_any_fields(self):
        with self.assertRaisesRegex(ValueError, ".*at least one field.*"):
            self._make_one()

    def test_from_api_repr(self):
        from google.cloud.bigquery.query import ArrayQueryParameterType
        from google.cloud.bigquery.query import ScalarQueryParameterType

        api_resource = {
            "type": "STRUCT",
            "structTypes": [
                {
                    "name": "age",
                    "type": {"type": "INTEGER"},
                    "description": "in years",
                },
                {
                    "name": "aliases",
                    "type": {"type": "ARRAY", "arrayType": {"type": "STRING"}},
                },
                {
                    "description": "a nested struct",
                    "type": {
                        "type": "STRUCT",
                        "structTypes": [
                            {"type": {"type": "DATE"}, "name": "nested_date"},
                            {
                                "type": {"type": "BOOLEAN"},
                                "description": "nested bool field",
                            },
                        ],
                    },
                },
            ],
        }

        klass = self._get_target_class()
        result = klass.from_api_repr(api_resource)

        self.assertIsNone(result.name)
        self.assertIsNone(result.description)
        self.assertEqual(len(result.fields), 3)

        field = result.fields[0]
        self.assertIsInstance(field, ScalarQueryParameterType)
        self.assertEqual(field.name, "age")
        self.assertEqual(field.description, "in years")

        field = result.fields[1]
        self.assertIsInstance(field, ArrayQueryParameterType)
        self.assertEqual(field.name, "aliases")
        self.assertIsNone(field.description)
        self.assertIsInstance(field._array_type, ScalarQueryParameterType)
        self.assertEqual(field._array_type._type, "STRING")

        field = result.fields[2]
        self.assertIsInstance(field, self._get_target_class())
        self.assertIsNone(field.name)
        self.assertEqual(field.description, "a nested struct")

        date_field = field.fields[0]
        self.assertEqual(date_field._type, "DATE")
        self.assertEqual(date_field.name, "nested_date")
        self.assertIsNone(date_field.description)

        bool_field = field.fields[1]
        self.assertEqual(bool_field._type, "BOOLEAN")
        self.assertIsNone(bool_field.name)
        self.assertEqual(bool_field.description, "nested bool field")

    def test_to_api_repr(self):
        from google.cloud.bigquery.query import ScalarQueryParameterType

        int_type = ScalarQueryParameterType("INTEGER", description="in years")
        date_type = ScalarQueryParameterType("DATE", name="day_of_birth")
        param_type = self._make_one(int_type, date_type, name="foo", description="bar")

        result = param_type.to_api_repr()

        expected_result = {
            "type": "STRUCT",
            "structTypes": [
                {"type": {"type": "INTEGER"}, "description": "in years"},
                {"name": "day_of_birth", "type": {"type": "DATE"}},
            ],
        }
        self.assertEqual(result, expected_result)

    def test_to_api_repr_nested(self):
        from google.cloud.bigquery.query import ScalarQueryParameterType

        struct_class = self._get_target_class()

        int_type = ScalarQueryParameterType("INTEGER", description="in years")
        nested_struct_type = struct_class(
            ScalarQueryParameterType("DATE", name="nested_date"),
            ScalarQueryParameterType("BOOLEAN", description="nested bool field"),
            name="nested",
        )
        param_type = self._make_one(
            int_type, nested_struct_type, name="foo", description="bar"
        )

        result = param_type.to_api_repr()

        expected_result = {
            "type": "STRUCT",
            "structTypes": [
                {"type": {"type": "INTEGER"}, "description": "in years"},
                {
                    "name": "nested",
                    "type": {
                        "type": "STRUCT",
                        "structTypes": [
                            {"type": {"type": "DATE"}, "name": "nested_date"},
                            {
                                "type": {"type": "BOOLEAN"},
                                "description": "nested bool field",
                            },
                        ],
                    },
                },
            ],
        }
        self.assertEqual(result, expected_result)

    def test_repr_no_optional_attrs(self):
        from google.cloud.bigquery.query import ScalarQueryParameterType

        param_type = self._make_one(
            ScalarQueryParameterType("BOOLEAN"), ScalarQueryParameterType("STRING")
        )
        expected = (
            "StructQueryParameterType("
            "ScalarQueryParameterType('BOOLEAN'), ScalarQueryParameterType('STRING')"
            ")"
        )
        self.assertEqual(repr(param_type), expected)

    def test_repr_all_optional_attrs(self):
        from google.cloud.bigquery.query import ScalarQueryParameterType

        param_type = self._make_one(
            ScalarQueryParameterType("BOOLEAN"),
            ScalarQueryParameterType("STRING"),
            name="data_record",
            description="this is it",
        )
        expected = (
            "StructQueryParameterType("
            "ScalarQueryParameterType('BOOLEAN'), ScalarQueryParameterType('STRING'), "
            "name='data_record', description='this is it'"
            ")"
        )
        self.assertEqual(repr(param_type), expected)


class Test_RangeQueryParameterType(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.query import RangeQueryParameterType

        return RangeQueryParameterType

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_ctor_str(self):
        param_type = self._make_one("DATE", name="foo", description="bar")
        self.assertEqual(param_type.type_._type, "DATE")
        self.assertEqual(param_type.name, "foo")
        self.assertEqual(param_type.description, "bar")

    def test_ctor_type(self):
        from google.cloud.bigquery import ScalarQueryParameterType

        scalar_type = ScalarQueryParameterType("DATE")
        param_type = self._make_one(scalar_type, name="foo", description="bar")
        self.assertEqual(param_type.type_._type, "DATE")
        self.assertEqual(param_type.name, "foo")
        self.assertEqual(param_type.description, "bar")

    def test_ctor_unsupported_type_str(self):
        with self.assertRaises(ValueError):
            self._make_one("TIME")

    def test_ctor_unsupported_type_type(self):
        from google.cloud.bigquery import ScalarQueryParameterType

        scalar_type = ScalarQueryParameterType("TIME")
        with self.assertRaises(ValueError):
            self._make_one(scalar_type)

    def test_ctor_wrong_type(self):
        with self.assertRaises(ValueError):
            self._make_one(None)

    def test_from_api_repr(self):
        RESOURCE = {
            "type": "RANGE",
            "rangeElementType": {"type": "DATE"},
        }

        klass = self._get_target_class()
        result = klass.from_api_repr(RESOURCE)
        self.assertEqual(result.type_._type, "DATE")
        self.assertIsNone(result.name)
        self.assertIsNone(result.description)

    def test_to_api_repr(self):
        EXPECTED = {
            "type": "RANGE",
            "rangeElementType": {"type": "DATE"},
        }
        param_type = self._make_one("DATE", name="foo", description="bar")
        result = param_type.to_api_repr()
        self.assertEqual(result, EXPECTED)

    def test__repr__(self):
        param_type = self._make_one("DATE", name="foo", description="bar")
        param_repr = "RangeQueryParameterType(ScalarQueryParameterType('DATE'), name='foo', description='bar')"
        self.assertEqual(repr(param_type), param_repr)

    def test__eq__(self):
        param_type1 = self._make_one("DATE", name="foo", description="bar")
        self.assertEqual(param_type1, param_type1)
        self.assertNotEqual(param_type1, object())

        alias = self._make_one("DATE", name="foo", description="bar")
        self.assertIsNot(param_type1, alias)
        self.assertEqual(param_type1, alias)

        wrong_type = self._make_one("DATETIME", name="foo", description="bar")
        self.assertNotEqual(param_type1, wrong_type)

        wrong_name = self._make_one("DATETIME", name="foo2", description="bar")
        self.assertNotEqual(param_type1, wrong_name)

        wrong_description = self._make_one("DATETIME", name="foo", description="bar2")
        self.assertNotEqual(param_type1, wrong_description)

    def test_with_name(self):
        param_type1 = self._make_one("DATE", name="foo", description="bar")
        param_type2 = param_type1.with_name("foo2")

        self.assertIsNot(param_type1, param_type2)
        self.assertEqual(param_type2.type_._type, "DATE")
        self.assertEqual(param_type2.name, "foo2")
        self.assertEqual(param_type2.description, "bar")


class Test__AbstractQueryParameter(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.query import _AbstractQueryParameter

        return _AbstractQueryParameter

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_from_api_virtual(self):
        klass = self._get_target_class()
        with self.assertRaises(NotImplementedError):
            klass.from_api_repr({})

    def test_to_api_virtual(self):
        param = self._make_one()
        with self.assertRaises(NotImplementedError):
            param.to_api_repr()


class Test_ScalarQueryParameter(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.query import ScalarQueryParameter

        return ScalarQueryParameter

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_ctor(self):
        param = self._make_one(name="foo", type_="INT64", value=123)
        self.assertEqual(param.name, "foo")
        self.assertEqual(param.type_, "INT64")
        self.assertEqual(param.value, 123)

    def test___eq__(self):
        param = self._make_one(name="foo", type_="INT64", value=123)
        self.assertEqual(param, param)
        self.assertNotEqual(param, object())
        alias = self._make_one(name="bar", type_="INT64", value=123)
        self.assertNotEqual(param, alias)
        wrong_type = self._make_one(name="foo", type_="FLOAT64", value=123.0)
        self.assertNotEqual(param, wrong_type)
        wrong_val = self._make_one(name="foo", type_="INT64", value=234)
        self.assertNotEqual(param, wrong_val)

    def test_positional(self):
        klass = self._get_target_class()
        param = klass.positional(type_="INT64", value=123)
        self.assertEqual(param.name, None)
        self.assertEqual(param.type_, "INT64")
        self.assertEqual(param.value, 123)

    def test_ctor_w_scalar_query_parameter_type(self):
        from google.cloud.bigquery import query

        param = self._make_one(
            name="foo",
            type_=query.SqlParameterScalarTypes.BIGNUMERIC,
            value=decimal.Decimal("123.456"),
        )
        self.assertEqual(param.name, "foo")
        self.assertEqual(param.type_, "BIGNUMERIC")
        self.assertEqual(param.value, decimal.Decimal("123.456"))

    def test_from_api_repr_w_name(self):
        RESOURCE = {
            "name": "foo",
            "parameterType": {"type": "INT64"},
            "parameterValue": {"value": 123},
        }
        klass = self._get_target_class()
        param = klass.from_api_repr(RESOURCE)
        self.assertEqual(param.name, "foo")
        self.assertEqual(param.type_, "INT64")
        self.assertEqual(param.value, 123)

    def test_from_api_repr_wo_name(self):
        RESOURCE = {
            "parameterType": {"type": "INT64"},
            "parameterValue": {"value": "123"},
        }
        klass = self._get_target_class()
        param = klass.from_api_repr(RESOURCE)
        self.assertEqual(param.name, None)
        self.assertEqual(param.type_, "INT64")
        self.assertEqual(param.value, 123)

    def test_from_api_repr_wo_value(self):
        # Back-end may not send back values for None params. See #9027
        RESOURCE = {"name": "foo", "parameterType": {"type": "INT64"}}
        klass = self._get_target_class()
        param = klass.from_api_repr(RESOURCE)
        self.assertEqual(param.name, "foo")
        self.assertEqual(param.type_, "INT64")
        self.assertIs(param.value, None)

    def test_to_api_repr_w_name(self):
        EXPECTED = {
            "name": "foo",
            "parameterType": {"type": "INT64"},
            "parameterValue": {"value": "123"},
        }
        param = self._make_one(name="foo", type_="INT64", value=123)
        self.assertEqual(param.to_api_repr(), EXPECTED)

    def test_to_api_repr_wo_name(self):
        EXPECTED = {
            "parameterType": {"type": "INT64"},
            "parameterValue": {"value": "123"},
        }
        klass = self._get_target_class()
        param = klass.positional(type_="INT64", value=123)
        self.assertEqual(param.to_api_repr(), EXPECTED)

    def test_to_api_repr_w_float(self):
        EXPECTED = {
            "parameterType": {"type": "FLOAT64"},
            "parameterValue": {"value": 12.345},
        }
        klass = self._get_target_class()
        param = klass.positional(type_="FLOAT64", value=12.345)
        self.assertEqual(param.to_api_repr(), EXPECTED)

    def test_to_api_repr_w_numeric(self):
        EXPECTED = {
            "parameterType": {"type": "NUMERIC"},
            "parameterValue": {"value": "123456789.123456789"},
        }
        klass = self._get_target_class()
        param = klass.positional(type_="NUMERIC", value="123456789.123456789")
        self.assertEqual(param.to_api_repr(), EXPECTED)

    def test_to_api_repr_w_bignumeric(self):
        big_num_string = "{d38}.{d38}".format(d38="9" * 38)
        EXPECTED = {
            "parameterType": {"type": "BIGNUMERIC"},
            "parameterValue": {"value": big_num_string},
        }
        klass = self._get_target_class()
        param = klass.positional(type_="BIGNUMERIC", value=big_num_string)
        self.assertEqual(param.to_api_repr(), EXPECTED)

    def test_to_api_repr_w_bool(self):
        EXPECTED = {
            "parameterType": {"type": "BOOL"},
            "parameterValue": {"value": "false"},
        }
        klass = self._get_target_class()
        param = klass.positional(type_="BOOL", value=False)
        self.assertEqual(param.to_api_repr(), EXPECTED)

    def test_to_api_repr_w_timestamp_datetime(self):
        from google.cloud._helpers import UTC

        STAMP = "2016-12-20 15:58:27.339328+00:00"
        when = datetime.datetime(2016, 12, 20, 15, 58, 27, 339328, tzinfo=UTC)
        EXPECTED = {
            "parameterType": {"type": "TIMESTAMP"},
            "parameterValue": {"value": STAMP},
        }
        klass = self._get_target_class()
        param = klass.positional(type_="TIMESTAMP", value=when)
        self.assertEqual(param.to_api_repr(), EXPECTED)

    def test_to_api_repr_w_timestamp_micros(self):
        from google.cloud._helpers import _microseconds_from_datetime, UTC

        now = datetime.datetime.now(UTC)
        seconds = _microseconds_from_datetime(now) / 1.0e6
        EXPECTED = {
            "parameterType": {"type": "TIMESTAMP"},
            "parameterValue": {"value": seconds},
        }
        klass = self._get_target_class()
        param = klass.positional(type_="TIMESTAMP", value=seconds)
        self.assertEqual(param.to_api_repr(), EXPECTED)

    def test_to_api_repr_w_datetime_datetime(self):
        from google.cloud._helpers import _datetime_to_rfc3339, UTC

        now = datetime.datetime.now(UTC)
        EXPECTED = {
            "parameterType": {"type": "DATETIME"},
            "parameterValue": {
                "value": _datetime_to_rfc3339(now)[:-1]  # strip trailing 'Z'
            },
        }
        klass = self._get_target_class()
        param = klass.positional(type_="DATETIME", value=now)
        self.assertEqual(param.to_api_repr(), EXPECTED)

    def test_to_api_repr_w_datetime_string(self):
        from google.cloud._helpers import _datetime_to_rfc3339, UTC

        now = datetime.datetime.now(UTC)
        now_str = _datetime_to_rfc3339(now)
        EXPECTED = {
            "parameterType": {"type": "DATETIME"},
            "parameterValue": {"value": now_str},
        }
        klass = self._get_target_class()
        param = klass.positional(type_="DATETIME", value=now_str)
        self.assertEqual(param.to_api_repr(), EXPECTED)

    def test_to_api_repr_w_date_date(self):
        today = datetime.date.today()
        EXPECTED = {
            "parameterType": {"type": "DATE"},
            "parameterValue": {"value": today.isoformat()},
        }
        klass = self._get_target_class()
        param = klass.positional(type_="DATE", value=today)
        self.assertEqual(param.to_api_repr(), EXPECTED)

    def test_to_api_repr_w_date_string(self):
        today = datetime.date.today()
        today_str = (today.isoformat(),)
        EXPECTED = {
            "parameterType": {"type": "DATE"},
            "parameterValue": {"value": today_str},
        }
        klass = self._get_target_class()
        param = klass.positional(type_="DATE", value=today_str)
        self.assertEqual(param.to_api_repr(), EXPECTED)

    def test_to_api_repr_w_unknown_type(self):
        EXPECTED = {
            "parameterType": {"type": "UNKNOWN"},
            "parameterValue": {"value": "unknown"},
        }
        klass = self._get_target_class()
        param = klass.positional(type_="UNKNOWN", value="unknown")
        self.assertEqual(param.to_api_repr(), EXPECTED)

    def test___eq___wrong_type(self):
        field = self._make_one("test", "STRING", "value")
        other = object()
        self.assertNotEqual(field, other)
        self.assertEqual(field, mock.ANY)

    def test___eq___name_mismatch(self):
        field = self._make_one("test", "STRING", "value")
        other = self._make_one("other", "STRING", "value")
        self.assertNotEqual(field, other)

    def test___eq___field_type_mismatch(self):
        field = self._make_one("test", "STRING", None)
        other = self._make_one("test", "INT64", None)
        self.assertNotEqual(field, other)

    def test___eq___value_mismatch(self):
        field = self._make_one("test", "STRING", "hello")
        other = self._make_one("test", "STRING", "world")
        self.assertNotEqual(field, other)

    def test___eq___hit(self):
        field = self._make_one("test", "STRING", "gotcha")
        other = self._make_one("test", "STRING", "gotcha")
        self.assertEqual(field, other)

    def test___ne___wrong_type(self):
        field = self._make_one("toast", "INT64", 13)
        other = object()
        self.assertNotEqual(field, other)
        self.assertEqual(field, mock.ANY)

    def test___ne___same_value(self):
        field1 = self._make_one("test", "INT64", 12)
        field2 = self._make_one("test", "INT64", 12)
        # unittest ``assertEqual`` uses ``==`` not ``!=``.
        comparison_val = field1 != field2
        self.assertFalse(comparison_val)

    def test___ne___different_values(self):
        field1 = self._make_one("test", "INT64", 11)
        field2 = self._make_one("test", "INT64", 12)
        self.assertNotEqual(field1, field2)

    def test___repr__(self):
        field1 = self._make_one("field1", "STRING", "value")
        expected = "ScalarQueryParameter('field1', 'STRING', 'value')"
        self.assertEqual(repr(field1), expected)


class Test_RangeQueryParameter(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.query import RangeQueryParameter

        return RangeQueryParameter

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_ctor(self):
        from google.cloud.bigquery.query import RangeQueryParameterType

        range_element_type = RangeQueryParameterType(type_="DATE")
        param = self._make_one(
            range_element_type="DATE", start="2016-08-11", name="foo"
        )
        self.assertEqual(param.name, "foo")
        self.assertEqual(param.range_element_type, range_element_type)
        self.assertEqual(param.start, "2016-08-11")
        self.assertIs(param.end, None)

    def test_ctor_does_not_print_to_stdout(self):
        # Regression test for a stray debug print() in __init__ that wrote the
        # range element type to stdout on every construction.
        with mock.patch("builtins.print") as mock_print:
            self._make_one(range_element_type="DATE", start="2016-08-11")
        mock_print.assert_not_called()

    def test_ctor_w_datetime_query_parameter_type_str(self):
        from google.cloud.bigquery.query import RangeQueryParameterType

        range_element_type = RangeQueryParameterType(type_="DATETIME")
        start_datetime = datetime.datetime(year=2020, month=12, day=31, hour=12)
        end_datetime = datetime.datetime(year=2021, month=12, day=31, hour=12)
        param = self._make_one(
            range_element_type="DATETIME",
            start=start_datetime,
            end=end_datetime,
            name="foo",
        )
        self.assertEqual(param.range_element_type, range_element_type)
        self.assertEqual(param.start, start_datetime)
        self.assertEqual(param.end, end_datetime)
        self.assertEqual(param.name, "foo")

    def test_ctor_w_datetime_query_parameter_type_type(self):
        from google.cloud.bigquery.query import RangeQueryParameterType

        range_element_type = RangeQueryParameterType(type_="DATETIME")
        param = self._make_one(range_element_type=range_element_type)
        self.assertEqual(param.range_element_type, range_element_type)
        self.assertEqual(param.start, None)
        self.assertEqual(param.end, None)
        self.assertEqual(param.name, None)

    def test_ctor_w_timestamp_query_parameter_typ_str(self):
        from google.cloud.bigquery.query import RangeQueryParameterType

        range_element_type = RangeQueryParameterType(type_="TIMESTAMP")
        start_datetime = datetime.datetime(year=2020, month=12, day=31, hour=12)
        end_datetime = datetime.datetime(year=2021, month=12, day=31, hour=12)
        param = self._make_one(
            range_element_type="TIMESTAMP",
            start=start_datetime,
            end=end_datetime,
            name="foo",
        )
        self.assertEqual(param.range_element_type, range_element_type)
        self.assertEqual(param.start, start_datetime)
        self.assertEqual(param.end, end_datetime)
        self.assertEqual(param.name, "foo")

    def test_ctor_w_timestamp_query_parameter_type_type(self):
        from google.cloud.bigquery.query import RangeQueryParameterType

        range_element_type = RangeQueryParameterType(type_="TIMESTAMP")
        param = self._make_one(range_element_type=range_element_type)
        self.assertEqual(param.range_element_type, range_element_type)
        self.assertEqual(param.start, None)
        self.assertEqual(param.end, None)
        self.assertEqual(param.name, None)

    def test_ctor_w_date_query_parameter_type_str(self):
        from google.cloud.bigquery.query import RangeQueryParameterType

        range_element_type = RangeQueryParameterType(type_="DATE")
        start_date = datetime.date(year=2020, month=12, day=31)
        end_date = datetime.date(year=2021, month=12, day=31)
        param = self._make_one(
            range_element_type="DATE",
            start=start_date,
            end=end_date,
            name="foo",
        )
        self.assertEqual(param.range_element_type, range_element_type)
        self.assertEqual(param.start, start_date)
        self.assertEqual(param.end, end_date)
        self.assertEqual(param.name, "foo")

    def test_ctor_w_date_query_parameter_type_type(self):
        from google.cloud.bigquery.query import RangeQueryParameterType

        range_element_type = RangeQueryParameterType(type_="DATE")
        param = self._make_one(range_element_type=range_element_type)
        self.assertEqual(param.range_element_type, range_element_type)
        self.assertEqual(param.start, None)
        self.assertEqual(param.end, None)
        self.assertEqual(param.name, None)

    def test_ctor_w_name_empty_str(self):
        from google.cloud.bigquery.query import RangeQueryParameterType

        range_element_type = RangeQueryParameterType(type_="DATE")
        param = self._make_one(
            range_element_type="DATE",
            name="",
        )
        self.assertEqual(param.range_element_type, range_element_type)
        self.assertIs(param.start, None)
        self.assertIs(param.end, None)
        self.assertEqual(param.name, "")

    def test_ctor_wo_value(self):
        from google.cloud.bigquery.query import RangeQueryParameterType

        range_element_type = RangeQueryParameterType(type_="DATETIME")
        param = self._make_one(range_element_type="DATETIME", name="foo")
        self.assertEqual(param.range_element_type, range_element_type)
        self.assertIs(param.start, None)
        self.assertIs(param.end, None)
        self.assertEqual(param.name, "foo")

    def test_ctor_w_unsupported_query_parameter_type_str(self):
        with self.assertRaises(ValueError):
            self._make_one(range_element_type="TIME", name="foo")

    def test_ctor_w_unsupported_query_parameter_type_type(self):
        from google.cloud.bigquery.query import RangeQueryParameterType

        range_element_type = RangeQueryParameterType(type_="DATE")
        range_element_type.type_._type = "TIME"
        with self.assertRaises(ValueError):
            self._make_one(range_element_type=range_element_type, name="foo")

    def test_ctor_w_unsupported_query_parameter_type_input(self):
        with self.assertRaises(ValueError):
            self._make_one(range_element_type=None, name="foo")

    def test_positional(self):
        from google.cloud.bigquery.query import RangeQueryParameterType

        range_element_type = RangeQueryParameterType(type_="DATE")
        klass = self._get_target_class()
        param = klass.positional(
            range_element_type="DATE", start="2016-08-11", end="2016-08-12"
        )
        self.assertIs(param.name, None)
        self.assertEqual(param.range_element_type, range_element_type)
        self.assertEqual(param.start, "2016-08-11")
        self.assertEqual(param.end, "2016-08-12")

    def test_from_api_repr_w_name(self):
        from google.cloud.bigquery.query import RangeQueryParameterType

        RESOURCE = {
            "name": "foo",
            "parameterType": {
                "type": "RANGE",
                "rangeElementType": {
                    "type": "DATE",
                },
            },
            "parameterValue": {
                "rangeValue": {"start": {"value": None}, "end": {"value": "2020-12-31"}}
            },
        }
        klass = self._get_target_class()
        param = klass.from_api_repr(RESOURCE)
        range_element_type = RangeQueryParameterType(type_="DATE")
        self.assertEqual(param.name, "foo")
        self.assertEqual(param.range_element_type, range_element_type)
        self.assertEqual(param.start, None)
        self.assertEqual(param.end, "2020-12-31")

    def test_from_api_repr_wo_name(self):
        from google.cloud.bigquery.query import RangeQueryParameterType

        RESOURCE = {
            "parameterType": {
                "type": "RANGE",
                "rangeElementType": {
                    "type": "DATE",
                },
            },
            "parameterValue": {
                "rangeValue": {"start": {"value": None}, "end": {"value": "2020-12-31"}}
            },
        }
        klass = self._get_target_class()
        param = klass.from_api_repr(RESOURCE)
        range_element_type = RangeQueryParameterType(type_="DATE")
        self.assertEqual(param.name, None)
        self.assertEqual(param.range_element_type, range_element_type)
        self.assertEqual(param.start, None)
        self.assertEqual(param.end, "2020-12-31")

    def test_from_api_repr_wo_value(self):
        # Back-end may not send back values for None params. See #9027
        from google.cloud.bigquery.query import RangeQueryParameterType

        RESOURCE = {
            "parameterType": {
                "type": "RANGE",
                "rangeElementType": {
                    "type": "DATE",
                },
            },
        }
        range_element_type = RangeQueryParameterType(type_="DATE")
        klass = self._get_target_class()
        param = klass.from_api_repr(RESOURCE)
        self.assertIs(param.name, None)
        self.assertEqual(param.range_element_type, range_element_type)
        self.assertIs(param.start, None)
        self.assertIs(param.end, None)

    def test_to_api_repr_w_name(self):
        EXPECTED = {
            "name": "foo",
            "parameterType": {
                "type": "RANGE",
                "rangeElementType": {
                    "type": "DATE",
                },
            },
            "parameterValue": {
                "rangeValue": {"start": {"value": None}, "end": {"value": "2016-08-11"}}
            },
        }
        param = self._make_one(range_element_type="DATE", end="2016-08-11", name="foo")
        self.assertEqual(param.to_api_repr(), EXPECTED)

    def test_to_api_repr_wo_name(self):
        EXPECTED = {
            "parameterType": {
                "type": "RANGE",
                "rangeElementType": {
                    "type": "DATE",
                },
            },
            "parameterValue": {
                "rangeValue": {"start": {"value": None}, "end": {"value": "2016-08-11"}}
            },
        }
        klass = self._get_target_class()
        param = klass.positional(range_element_type="DATE", end="2016-08-11")
        self.assertEqual(param.to_api_repr(), EXPECTED)

    def test_to_api_repr_w_date_date(self):
        today = datetime.date.today()
        today_str = today.strftime("%Y-%m-%d")
        EXPECTED = {
            "name": "foo",
            "parameterType": {
                "type": "RANGE",
                "rangeElementType": {
                    "type": "DATE",
                },
            },
            "parameterValue": {
                "rangeValue": {"start": {"value": None}, "end": {"value": today_str}}
            },
        }
        param = self._make_one(range_element_type="DATE", end=today, name="foo")
        self.assertEqual(param.to_api_repr(), EXPECTED)

    def test_to_api_repr_w_datetime_str(self):
        EXPECTED = {
            "parameterType": {
                "type": "RANGE",
                "rangeElementType": {
                    "type": "DATETIME",
                },
            },
            "parameterValue": {
                "rangeValue": {
                    "start": {"value": None},
                    "end": {"value": "2020-01-01T12:00:00.000000"},
                }
            },
        }
        klass = self._get_target_class()
        end_datetime = datetime.datetime(year=2020, month=1, day=1, hour=12)
        param = klass.positional(range_element_type="DATETIME", end=end_datetime)
        self.assertEqual(param.to_api_repr(), EXPECTED)

    def test_to_api_repr_w_datetime_datetime(self):
        from google.cloud._helpers import UTC  # type: ignore
        from google.cloud.bigquery._helpers import _RFC3339_MICROS_NO_ZULU

        now = datetime.datetime.now(UTC)
        now_str = now.strftime(_RFC3339_MICROS_NO_ZULU)
        EXPECTED = {
            "parameterType": {
                "type": "RANGE",
                "rangeElementType": {
                    "type": "DATETIME",
                },
            },
            "parameterValue": {
                "rangeValue": {"start": {"value": None}, "end": {"value": now_str}}
            },
        }
        klass = self._get_target_class()
        param = klass.positional(range_element_type="DATETIME", end=now)
        self.assertEqual(param.to_api_repr(), EXPECTED)

    def test_to_api_repr_w_timestamp_str(self):
        EXPECTED = {
            "parameterType": {
                "type": "RANGE",
                "rangeElementType": {
                    "type": "TIMESTAMP",
                },
            },
            "parameterValue": {
                "rangeValue": {
                    "start": {"value": None},
                    "end": {"value": "2020-01-01 12:00:00+00:00"},
                }
            },
        }
        klass = self._get_target_class()
        end_timestamp = datetime.datetime(year=2020, month=1, day=1, hour=12)
        param = klass.positional(range_element_type="TIMESTAMP", end=end_timestamp)
        self.assertEqual(param.to_api_repr(), EXPECTED)

    def test_to_api_repr_w_timestamp_timestamp(self):
        from google.cloud._helpers import UTC  # type: ignore

        now = datetime.datetime.now(UTC)
        now = now.astimezone(UTC)
        now_str = str(now)
        EXPECTED = {
            "parameterType": {
                "type": "RANGE",
                "rangeElementType": {
                    "type": "TIMESTAMP",
                },
            },
            "parameterValue": {
                "rangeValue": {"start": {"value": None}, "end": {"value": now_str}}
            },
        }
        klass = self._get_target_class()
        param = klass.positional(range_element_type="TIMESTAMP", end=now)
        self.assertEqual(param.to_api_repr(), EXPECTED)

    def test_to_api_repr_wo_values(self):
        EXPECTED = {
            "name": "foo",
            "parameterType": {
                "type": "RANGE",
                "rangeElementType": {
                    "type": "DATE",
                },
            },
            "parameterValue": {
                "rangeValue": {"start": {"value": None}, "end": {"value": None}}
            },
        }
        param = self._make_one(range_element_type="DATE", name="foo")
        self.assertEqual(param.to_api_repr(), EXPECTED)

    def test_to_api_repr_unsupported_value_type(self):
        with self.assertRaisesRegex(
            ValueError, "Cannot convert range element value from type"
        ):
            range_param = self._make_one(
                range_element_type="DATE", start=datetime.date.today()
            )
            range_param.range_element_type.type_._type = "LONG"
            range_param.to_api_repr()

    def test___eq__(self):
        param = self._make_one(
            range_element_type="DATE", start="2016-08-11", name="foo"
        )
        self.assertEqual(param, param)
        self.assertNotEqual(param, object())
        alias = self._make_one(
            range_element_type="DATE", start="2016-08-11", name="bar"
        )
        self.assertNotEqual(param, alias)
        wrong_type = self._make_one(
            range_element_type="DATETIME",
            start="2020-12-31 12:00:00.000000",
            name="foo",
        )
        self.assertNotEqual(param, wrong_type)
        wrong_val = self._make_one(
            range_element_type="DATE", start="2016-08-12", name="foo"
        )
        self.assertNotEqual(param, wrong_val)

    def test___eq___wrong_type(self):
        param = self._make_one(
            range_element_type="DATE", start="2016-08-11", name="foo"
        )
        other = object()
        self.assertNotEqual(param, other)
        self.assertEqual(param, mock.ANY)

    def test___eq___name_mismatch(self):
        param = self._make_one(
            range_element_type="DATE", start="2016-08-11", name="foo"
        )
        other = self._make_one(
            range_element_type="DATE", start="2016-08-11", name="bar"
        )
        self.assertNotEqual(param, other)

    def test___eq___field_type_mismatch(self):
        param = self._make_one(range_element_type="DATE")
        other = self._make_one(range_element_type="DATETIME")
        self.assertNotEqual(param, other)

    def test___eq___value_mismatch(self):
        param = self._make_one(range_element_type="DATE", start="2016-08-11")
        other = self._make_one(range_element_type="DATE", start="2016-08-12")
        self.assertNotEqual(param, other)

    def test___eq___hit(self):
        param = self._make_one(range_element_type="DATE", start="2016-08-12")
        other = self._make_one(range_element_type="DATE", start="2016-08-12")
        self.assertEqual(param, other)

    def test___ne___wrong_type(self):
        param = self._make_one(range_element_type="DATE")
        other = object()
        self.assertNotEqual(param, other)
        self.assertEqual(param, mock.ANY)

    def test___ne___same_value(self):
        param1 = self._make_one(range_element_type="DATE")
        param2 = self._make_one(range_element_type="DATE")
        # unittest ``assertEqual`` uses ``==`` not ``!=``.
        comparison_val = param1 != param2
        self.assertFalse(comparison_val)

    def test___ne___different_values(self):
        param1 = self._make_one(range_element_type="DATE", start="2016-08-12")
        param2 = self._make_one(range_element_type="DATE")
        self.assertNotEqual(param1, param2)

    def test___repr__(self):
        param1 = self._make_one(range_element_type="DATE", start="2016-08-12")
        expected = "RangeQueryParameter(None, {'type': 'RANGE', 'rangeElementType': {'type': 'DATE'}}, '2016-08-12', None)"
        self.assertEqual(repr(param1), expected)


def _make_subparam(name, type_, value):
    from google.cloud.bigquery.query import ScalarQueryParameter

    return ScalarQueryParameter(name, type_, value)


class Test_ArrayQueryParameter(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.query import ArrayQueryParameter

        return ArrayQueryParameter

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_ctor(self):
        param = self._make_one(name="foo", array_type="INT64", values=[1, 2])
        self.assertEqual(param.name, "foo")
        self.assertEqual(param.array_type, "INT64")
        self.assertEqual(param.values, [1, 2])

    def test_ctor_empty_struct_array_wo_type_info(self):
        with self.assertRaisesRegex(ValueError, r"(?i)missing.*struct.*type info.*"):
            self._make_one(name="foo", array_type="STRUCT", values=[])

    def test___eq__(self):
        param = self._make_one(name="foo", array_type="INT64", values=[123])
        self.assertEqual(param, param)
        self.assertNotEqual(param, object())
        alias = self._make_one(name="bar", array_type="INT64", values=[123])
        self.assertNotEqual(param, alias)
        wrong_type = self._make_one(name="foo", array_type="FLOAT64", values=[123.0])
        self.assertNotEqual(param, wrong_type)
        wrong_val = self._make_one(name="foo", array_type="INT64", values=[234])
        self.assertNotEqual(param, wrong_val)

    def test_positional(self):
        klass = self._get_target_class()
        param = klass.positional(array_type="INT64", values=[1, 2])
        self.assertEqual(param.name, None)
        self.assertEqual(param.array_type, "INT64")
        self.assertEqual(param.values, [1, 2])

    def test_from_api_repr_w_name(self):
        RESOURCE = {
            "name": "foo",
            "parameterType": {"type": "ARRAY", "arrayType": {"type": "INT64"}},
            "parameterValue": {"arrayValues": [{"value": "1"}, {"value": "2"}]},
        }
        klass = self._get_target_class()
        param = klass.from_api_repr(RESOURCE)
        self.assertEqual(param.name, "foo")
        self.assertEqual(param.array_type, "INT64")
        self.assertEqual(param.values, [1, 2])

    def test_from_api_repr_wo_name(self):
        RESOURCE = {
            "parameterType": {"type": "ARRAY", "arrayType": {"type": "INT64"}},
            "parameterValue": {"arrayValues": [{"value": "1"}, {"value": "2"}]},
        }
        klass = self._get_target_class()
        param = klass.from_api_repr(RESOURCE)
        self.assertEqual(param.name, None)
        self.assertEqual(param.array_type, "INT64")
        self.assertEqual(param.values, [1, 2])

    def test_from_api_repr_wo_values(self):
        # Back-end may not send back values for empty array params. See #7309
        RESOURCE = {
            "name": "foo",
            "parameterType": {"type": "ARRAY", "arrayType": {"type": "INT64"}},
        }
        klass = self._get_target_class()
        param = klass.from_api_repr(RESOURCE)
        self.assertEqual(param.name, "foo")
        self.assertEqual(param.array_type, "INT64")
        self.assertEqual(param.values, [])

    def test_from_api_repr_w_none_values(self):
        RESOURCE = {
            "parameterType": {"type": "ARRAY", "arrayType": {"type": "INT64"}},
            "parameterValue": {"arrayValues": [{"value": "1"}, {"value": None}]},
        }
        klass = self._get_target_class()
        param = klass.from_api_repr(RESOURCE)
        self.assertEqual(param.array_type, "INT64")
        self.assertEqual(param.values, [1, None])

    def test_from_api_repr_w_struct_type(self):
        from google.cloud.bigquery.query import StructQueryParameter

        RESOURCE = {
            "parameterType": {
                "type": "ARRAY",
                "arrayType": {
                    "type": "STRUCT",
                    "structTypes": [
                        {"name": "name", "type": {"type": "STRING"}},
                        {"name": "age", "type": {"type": "INT64"}},
                    ],
                },
            },
            "parameterValue": {
                "arrayValues": [
                    {
                        "structValues": {
                            "name": {"value": "Phred Phlyntstone"},
                            "age": {"value": "32"},
                        }
                    },
                    {
                        "structValues": {
                            "name": {"value": "Bharney Rhubbyl"},
                            "age": {"value": "31"},
                        }
                    },
                ]
            },
        }

        klass = self._get_target_class()
        param = klass.from_api_repr(RESOURCE)

        phred = StructQueryParameter.positional(
            _make_subparam("name", "STRING", "Phred Phlyntstone"),
            _make_subparam("age", "INT64", 32),
        )
        bharney = StructQueryParameter.positional(
            _make_subparam("name", "STRING", "Bharney Rhubbyl"),
            _make_subparam("age", "INT64", 31),
        )
        self.assertEqual(param.array_type, "STRUCT")
        self.assertEqual(param.values, [phred, bharney])

    def test_to_api_repr_w_name(self):
        EXPECTED = {
            "name": "foo",
            "parameterType": {"type": "ARRAY", "arrayType": {"type": "INT64"}},
            "parameterValue": {"arrayValues": [{"value": "1"}, {"value": "2"}]},
        }
        param = self._make_one(name="foo", array_type="INT64", values=[1, 2])
        self.assertEqual(param.to_api_repr(), EXPECTED)

    def test_to_api_repr_wo_name(self):
        EXPECTED = {
            "parameterType": {"type": "ARRAY", "arrayType": {"type": "INT64"}},
            "parameterValue": {"arrayValues": [{"value": "1"}, {"value": "2"}]},
        }
        klass = self._get_target_class()
        param = klass.positional(array_type="INT64", values=[1, 2])
        self.assertEqual(param.to_api_repr(), EXPECTED)

    def test_to_api_repr_array_type_as_type_instance(self):
        from google.cloud.bigquery.query import ScalarQueryParameterType

        EXPECTED = {
            "parameterType": {"type": "ARRAY", "arrayType": {"type": "BOOLEAN"}},
            "parameterValue": {"arrayValues": [{"value": "true"}, {"value": "false"}]},
        }
        klass = self._get_target_class()
        param = klass.positional(
            array_type=ScalarQueryParameterType("BOOLEAN"),
            values=[True, False],
        )
        self.assertEqual(param.to_api_repr(), EXPECTED)

    def test_to_api_repr_w_unknown_type(self):
        EXPECTED = {
            "parameterType": {"type": "ARRAY", "arrayType": {"type": "UNKNOWN"}},
            "parameterValue": {"arrayValues": [{"value": "unknown"}]},
        }
        klass = self._get_target_class()
        param = klass.positional(array_type="UNKNOWN", values=["unknown"])
        self.assertEqual(param.to_api_repr(), EXPECTED)

    def test_to_api_repr_w_record_type(self):
        from google.cloud.bigquery.query import StructQueryParameter

        EXPECTED = {
            "parameterType": {
                "type": "ARRAY",
                "arrayType": {
                    "type": "STRUCT",
                    "structTypes": [
                        {"name": "foo", "type": {"type": "STRING"}},
                        {"name": "bar", "type": {"type": "INT64"}},
                    ],
                },
            },
            "parameterValue": {
                "arrayValues": [
                    {"structValues": {"foo": {"value": "Foo"}, "bar": {"value": "123"}}}
                ]
            },
        }
        one = _make_subparam("foo", "STRING", "Foo")
        another = _make_subparam("bar", "INT64", 123)
        struct = StructQueryParameter.positional(one, another)
        klass = self._get_target_class()
        param = klass.positional(array_type="RECORD", values=[struct])
        self.assertEqual(param.to_api_repr(), EXPECTED)

    def test_to_api_repr_w_empty_array_of_records_type(self):
        from google.cloud.bigquery.query import ScalarQueryParameterType
        from google.cloud.bigquery.query import StructQueryParameterType

        EXPECTED = {
            "parameterType": {
                "type": "ARRAY",
                "arrayType": {
                    "type": "STRUCT",
                    "structTypes": [
                        {"name": "foo", "type": {"type": "STRING"}},
                        {"name": "bar", "type": {"type": "INT64"}},
                    ],
                },
            },
            "parameterValue": {"arrayValues": []},
        }
        item_type = StructQueryParameterType(
            ScalarQueryParameterType("STRING", name="foo"),
            ScalarQueryParameterType("INT64", name="bar"),
        )
        klass = self._get_target_class()
        param = klass.positional(array_type=item_type, values=[])
        self.assertEqual(param.to_api_repr(), EXPECTED)

    def test___eq___wrong_type(self):
        field = self._make_one("test", "STRING", ["value"])
        other = object()
        self.assertNotEqual(field, other)
        self.assertEqual(field, mock.ANY)

    def test___eq___name_mismatch(self):
        field = self._make_one("field", "STRING", ["value"])
        other = self._make_one("other", "STRING", ["value"])
        self.assertNotEqual(field, other)

    def test___eq___field_type_mismatch(self):
        field = self._make_one("test", "STRING", [])
        other = self._make_one("test", "INT64", [])
        self.assertNotEqual(field, other)

    def test___eq___value_mismatch(self):
        field = self._make_one("test", "STRING", ["hello"])
        other = self._make_one("test", "STRING", ["hello", "world"])
        self.assertNotEqual(field, other)

    def test___eq___hit(self):
        field = self._make_one("test", "STRING", ["gotcha"])
        other = self._make_one("test", "STRING", ["gotcha"])
        self.assertEqual(field, other)

    def test___ne___wrong_type(self):
        field = self._make_one("toast", "INT64", [13])
        other = object()
        self.assertNotEqual(field, other)
        self.assertEqual(field, mock.ANY)

    def test___ne___same_value(self):
        field1 = self._make_one("test", "INT64", [12])
        field2 = self._make_one("test", "INT64", [12])
        # unittest ``assertEqual`` uses ``==`` not ``!=``.
        comparison_val = field1 != field2
        self.assertFalse(comparison_val)

    def test___ne___different_values(self):
        field1 = self._make_one("test", "INT64", [11])
        field2 = self._make_one("test", "INT64", [12])
        self.assertNotEqual(field1, field2)

    def test___repr__array_type_str(self):
        field1 = self._make_one("field1", "STRING", ["value"])
        expected = "ArrayQueryParameter('field1', 'STRING', ['value'])"
        self.assertEqual(repr(field1), expected)

    def test___repr__array_type_scalar_type_instance(self):
        from google.cloud.bigquery.query import ScalarQueryParameterType

        int_items = self._make_one(
            "int_items", ScalarQueryParameterType("INTEGER"), [64]
        )
        expected = "ArrayQueryParameter('int_items', 'INTEGER', [64])"
        self.assertEqual(repr(int_items), expected)

    def test___repr__array_type_struct_type_instance(self):
        from google.cloud.bigquery.query import ScalarQueryParameterType
        from google.cloud.bigquery.query import StructQueryParameterType

        struct_items = self._make_one(
            "struct_items",
            StructQueryParameterType(
                ScalarQueryParameterType("INTEGER", name="age"),
                ScalarQueryParameterType("STRING", name="last_name"),
            ),
            [{"age": 18, "last_name": "Doe"}],
        )
        expected = (
            "ArrayQueryParameter('struct_items', 'STRUCT', "
            "[{'age': 18, 'last_name': 'Doe'}])"
        )
        self.assertEqual(repr(struct_items), expected)


class Test_StructQueryParameter(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.query import StructQueryParameter

        return StructQueryParameter

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_ctor(self):
        sub_1 = _make_subparam("bar", "INT64", 123)
        sub_2 = _make_subparam("baz", "STRING", "abc")
        param = self._make_one("foo", sub_1, sub_2)
        self.assertEqual(param.name, "foo")
        self.assertEqual(param.struct_types, {"bar": "INT64", "baz": "STRING"})
        self.assertEqual(param.struct_values, {"bar": 123, "baz": "abc"})

    def test___eq__(self):
        sub_1 = _make_subparam("bar", "INT64", 123)
        sub_2 = _make_subparam("baz", "STRING", "abc")
        sub_3 = _make_subparam("baz", "STRING", "def")
        sub_1_float = _make_subparam("bar", "FLOAT64", 123.0)
        param = self._make_one("foo", sub_1, sub_2)
        self.assertEqual(param, param)
        self.assertNotEqual(param, object())
        alias = self._make_one("bar", sub_1, sub_2)
        self.assertNotEqual(param, alias)
        wrong_type = self._make_one("foo", sub_1_float, sub_2)
        self.assertNotEqual(param, wrong_type)
        wrong_val = self._make_one("foo", sub_2, sub_3)
        self.assertNotEqual(param, wrong_val)

    def test_positional(self):
        sub_1 = _make_subparam("bar", "INT64", 123)
        sub_2 = _make_subparam("baz", "STRING", "abc")
        klass = self._get_target_class()
        param = klass.positional(sub_1, sub_2)
        self.assertEqual(param.name, None)
        self.assertEqual(param.struct_types, {"bar": "INT64", "baz": "STRING"})
        self.assertEqual(param.struct_values, {"bar": 123, "baz": "abc"})

    def test_from_api_repr_w_name(self):
        RESOURCE = {
            "name": "foo",
            "parameterType": {
                "type": "STRUCT",
                "structTypes": [
                    {"name": "bar", "type": {"type": "INT64"}},
                    {"name": "baz", "type": {"type": "STRING"}},
                ],
            },
            "parameterValue": {
                "structValues": {"bar": {"value": 123}, "baz": {"value": "abc"}}
            },
        }
        klass = self._get_target_class()
        param = klass.from_api_repr(RESOURCE)
        self.assertEqual(param.name, "foo")
        self.assertEqual(param.struct_types, {"bar": "INT64", "baz": "STRING"})
        self.assertEqual(param.struct_values, {"bar": 123, "baz": "abc"})

    def test_from_api_repr_wo_name(self):
        RESOURCE = {
            "parameterType": {
                "type": "STRUCT",
                "structTypes": [
                    {"name": "bar", "type": {"type": "INT64"}},
                    {"name": "baz", "type": {"type": "STRING"}},
                ],
            },
            "parameterValue": {
                "structValues": {"bar": {"value": 123}, "baz": {"value": "abc"}}
            },
        }
        klass = self._get_target_class()
        param = klass.from_api_repr(RESOURCE)
        self.assertEqual(param.name, None)
        self.assertEqual(param.struct_types, {"bar": "INT64", "baz": "STRING"})
        self.assertEqual(param.struct_values, {"bar": 123, "baz": "abc"})

    def test_from_api_repr_w_nested_array(self):
        from google.cloud.bigquery.query import ArrayQueryParameter

        RESOURCE = {
            "name": "foo",
            "parameterType": {
                "type": "STRUCT",
                "structTypes": [
                    {"name": "bar", "type": {"type": "STRING"}},
                    {
                        "name": "baz",
                        "type": {"type": "ARRAY", "arrayType": {"type": "INT64"}},
                    },
                ],
            },
            "parameterValue": {
                "structValues": {
                    "bar": {"value": "abc"},
                    "baz": {"arrayValues": [{"value": "123"}, {"value": "456"}]},
                }
            },
        }
        klass = self._get_target_class()
        param = klass.from_api_repr(RESOURCE)
        self.assertEqual(
            param,
            self._make_one(
                "foo",
                _make_subparam("bar", "STRING", "abc"),
                ArrayQueryParameter("baz", "INT64", [123, 456]),
            ),
        )

    def test_from_api_repr_w_nested_struct(self):
        RESOURCE = {
            "name": "foo",
            "parameterType": {
                "type": "STRUCT",
                "structTypes": [
                    {"name": "bar", "type": {"type": "STRING"}},
                    {
                        "name": "baz",
                        "type": {
                            "type": "STRUCT",
                            "structTypes": [
                                {"name": "qux", "type": {"type": "INT64"}},
                                {"name": "spam", "type": {"type": "BOOL"}},
                            ],
                        },
                    },
                ],
            },
            "parameterValue": {
                "structValues": {
                    "bar": {"value": "abc"},
                    "baz": {
                        "structValues": {
                            "qux": {"value": "123"},
                            "spam": {"value": "true"},
                        }
                    },
                }
            },
        }

        klass = self._get_target_class()
        param = klass.from_api_repr(RESOURCE)

        expected = self._make_one(
            "foo",
            _make_subparam("bar", "STRING", "abc"),
            self._make_one(
                "baz",
                _make_subparam("qux", "INT64", 123),
                _make_subparam("spam", "BOOL", True),
            ),
        )
        self.assertEqual(param.name, "foo")
        self.assertEqual(param.struct_types, expected.struct_types)
        self.assertEqual(param.struct_values, expected.struct_values)

    def test_to_api_repr_w_name(self):
        EXPECTED = {
            "name": "foo",
            "parameterType": {
                "type": "STRUCT",
                "structTypes": [
                    {"name": "bar", "type": {"type": "INT64"}},
                    {"name": "baz", "type": {"type": "STRING"}},
                ],
            },
            "parameterValue": {
                "structValues": {"bar": {"value": "123"}, "baz": {"value": "abc"}}
            },
        }
        sub_1 = _make_subparam("bar", "INT64", 123)
        sub_2 = _make_subparam("baz", "STRING", "abc")
        param = self._make_one("foo", sub_1, sub_2)
        self.assertEqual(param.to_api_repr(), EXPECTED)

    def test_to_api_repr_wo_name(self):
        EXPECTED = {
            "parameterType": {
                "type": "STRUCT",
                "structTypes": [
                    {"name": "bar", "type": {"type": "INT64"}},
                    {"name": "baz", "type": {"type": "STRING"}},
                ],
            },
            "parameterValue": {
                "structValues": {"bar": {"value": "123"}, "baz": {"value": "abc"}}
            },
        }
        sub_1 = _make_subparam("bar", "INT64", 123)
        sub_2 = _make_subparam("baz", "STRING", "abc")
        klass = self._get_target_class()
        param = klass.positional(sub_1, sub_2)
        self.assertEqual(param.to_api_repr(), EXPECTED)

    def test_to_api_repr_w_nested_array(self):
        from google.cloud.bigquery.query import ArrayQueryParameter

        EXPECTED = {
            "name": "foo",
            "parameterType": {
                "type": "STRUCT",
                "structTypes": [
                    {"name": "bar", "type": {"type": "STRING"}},
                    {
                        "name": "baz",
                        "type": {"type": "ARRAY", "arrayType": {"type": "INT64"}},
                    },
                ],
            },
            "parameterValue": {
                "structValues": {
                    "bar": {"value": "abc"},
                    "baz": {"arrayValues": [{"value": "123"}, {"value": "456"}]},
                }
            },
        }
        scalar = _make_subparam("bar", "STRING", "abc")
        array = ArrayQueryParameter("baz", "INT64", [123, 456])
        param = self._make_one("foo", scalar, array)
        self.assertEqual(param.to_api_repr(), EXPECTED)

    def test_to_api_repr_w_nested_struct(self):
        EXPECTED = {
            "name": "foo",
            "parameterType": {
                "type": "STRUCT",
                "structTypes": [
                    {"name": "bar", "type": {"type": "STRING"}},
                    {
                        "name": "baz",
                        "type": {
                            "type": "STRUCT",
                            "structTypes": [
                                {"name": "qux", "type": {"type": "INT64"}},
                                {"name": "spam", "type": {"type": "BOOL"}},
                            ],
                        },
                    },
                ],
            },
            "parameterValue": {
                "structValues": {
                    "bar": {"value": "abc"},
                    "baz": {
                        "structValues": {
                            "qux": {"value": "123"},
                            "spam": {"value": "true"},
                        }
                    },
                }
            },
        }
        scalar_1 = _make_subparam("bar", "STRING", "abc")
        scalar_2 = _make_subparam("qux", "INT64", 123)
        scalar_3 = _make_subparam("spam", "BOOL", True)
        sub = self._make_one("baz", scalar_2, scalar_3)
        param = self._make_one("foo", scalar_1, sub)
        self.assertEqual(param.to_api_repr(), EXPECTED)

    def test_to_api_repr_w_unknown_type(self):
        EXPECTED = {
            "name": "foo",
            "parameterType": {
                "type": "STRUCT",
                "structTypes": [
                    {"name": "bar", "type": {"type": "INT64"}},
                    {"name": "baz", "type": {"type": "UNKNOWN_TYPE"}},
                ],
            },
            "parameterValue": {
                "structValues": {"bar": {"value": "123"}, "baz": {"value": "abc"}}
            },
        }
        sub_1 = _make_subparam("bar", "INT64", 123)
        sub_2 = _make_subparam("baz", "UNKNOWN_TYPE", "abc")
        param = self._make_one("foo", sub_1, sub_2)
        self.assertEqual(param.to_api_repr(), EXPECTED)

    def test___eq___wrong_type(self):
        field = self._make_one("test", _make_subparam("bar", "STRING", "abc"))
        other = object()
        self.assertNotEqual(field, other)
        self.assertEqual(field, mock.ANY)

    def test___eq___name_mismatch(self):
        field = self._make_one("test", _make_subparam("bar", "STRING", "abc"))
        other = self._make_one("other ", _make_subparam("bar", "STRING", "abc"))
        self.assertNotEqual(field, other)

    def test___eq___field_type_mismatch(self):
        field = self._make_one("test", _make_subparam("bar", "STRING", None))
        other = self._make_one("test", _make_subparam("bar", "INT64", None))
        self.assertNotEqual(field, other)

    def test___eq___value_mismatch(self):
        field = self._make_one("test", _make_subparam("bar", "STRING", "hello"))
        other = self._make_one("test", _make_subparam("bar", "STRING", "world"))
        self.assertNotEqual(field, other)

    def test___eq___hit(self):
        field = self._make_one("test", _make_subparam("bar", "STRING", "gotcha"))
        other = self._make_one("test", _make_subparam("bar", "STRING", "gotcha"))
        self.assertEqual(field, other)

    def test___ne___wrong_type(self):
        field = self._make_one("test", _make_subparam("bar", "STRING", "hello"))
        other = object()
        self.assertNotEqual(field, other)
        self.assertEqual(field, mock.ANY)

    def test___ne___same_value(self):
        field1 = self._make_one("test", _make_subparam("bar", "STRING", "hello"))
        field2 = self._make_one("test", _make_subparam("bar", "STRING", "hello"))
        # unittest ``assertEqual`` uses ``==`` not ``!=``.
        comparison_val = field1 != field2
        self.assertFalse(comparison_val)

    def test___ne___different_values(self):
        field1 = self._make_one("test", _make_subparam("bar", "STRING", "hello"))
        field2 = self._make_one("test", _make_subparam("bar", "STRING", "world"))
        self.assertNotEqual(field1, field2)

    def test___repr__(self):
        field1 = self._make_one("test", _make_subparam("field1", "STRING", "hello"))
        got = repr(field1)
        self.assertIn("StructQueryParameter", got)
        self.assertIn("'field1': 'hello'", got)


class Test_QueryResults(unittest.TestCase):
    PROJECT = "project"
    JOB_ID = "test-synchronous-query"
    TOKEN = "TOKEN"

    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.query import _QueryResults

        return _QueryResults

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def _make_resource(self):
        return {"jobReference": {"projectId": self.PROJECT, "jobId": self.JOB_ID}}

    def _verifySchema(self, query, resource):
        from google.cloud.bigquery.schema import SchemaField

        if "schema" in resource:
            fields = resource["schema"]["fields"]
            self.assertEqual(len(query.schema), len(fields))
            for found, expected in zip(query.schema, fields):
                self.assertIsInstance(found, SchemaField)
                self.assertEqual(found.name, expected["name"])
                self.assertEqual(found.field_type, expected["type"])
                self.assertEqual(found.mode, expected["mode"])
                self.assertEqual(found.description, expected.get("description"))
                self.assertEqual(found.fields, expected.get("fields", ()))
        else:
            self.assertEqual(query.schema, [])

    def test_ctor_defaults(self):
        query = self._make_one(self._make_resource())
        self.assertIsNone(query.cache_hit)
        self.assertIsNone(query.complete)
        self.assertIsNone(query.errors)
        self.assertIsNone(query.page_token)
        self.assertEqual(query.project, self.PROJECT)
        self.assertEqual(query.rows, [])
        self.assertEqual(query.schema, [])
        self.assertIsNone(query.total_rows)
        self.assertIsNone(query.total_bytes_processed)

    def test_cache_hit_missing(self):
        query = self._make_one(self._make_resource())
        self.assertIsNone(query.cache_hit)

    def test_cache_hit_present(self):
        resource = self._make_resource()
        resource["cacheHit"] = True
        query = self._make_one(resource)
        self.assertTrue(query.cache_hit)

    def test_complete_missing(self):
        query = self._make_one(self._make_resource())
        self.assertIsNone(query.complete)

    def test_complete_present(self):
        resource = self._make_resource()
        resource["jobComplete"] = True
        query = self._make_one(resource)
        self.assertTrue(query.complete)

    def test_errors_missing(self):
        query = self._make_one(self._make_resource())
        self.assertIsNone(query.errors)

    def test_errors_present(self):
        ERRORS = [{"reason": "testing"}]
        resource = self._make_resource()
        resource["errors"] = ERRORS
        query = self._make_one(resource)
        self.assertEqual(query.errors, ERRORS)

    def test_job_id_missing(self):
        query = self._make_one({})
        self.assertIsNone(query.job_id)

    def test_job_id_broken_job_reference(self):
        resource = {"jobReference": {"bogus": "BOGUS"}}
        query = self._make_one(resource)
        self.assertIsNone(query.job_id)

    def test_job_id_present(self):
        resource = self._make_resource()
        resource["jobReference"]["jobId"] = "custom-job"
        query = self._make_one(resource)
        self.assertEqual(query.job_id, "custom-job")

    def test_location_missing(self):
        query = self._make_one({})
        self.assertIsNone(query.location)

    def test_location_present(self):
        resource = self._make_resource()
        resource["jobReference"]["location"] = "test-location"
        query = self._make_one(resource)
        self.assertEqual(query.location, "test-location")

    def test_page_token_missing(self):
        query = self._make_one(self._make_resource())
        self.assertIsNone(query.page_token)

    def test_page_token_present(self):
        resource = self._make_resource()
        resource["pageToken"] = "TOKEN"
        query = self._make_one(resource)
        self.assertEqual(query.page_token, "TOKEN")

    def test_query_id_missing(self):
        query = self._make_one(self._make_resource())
        self.assertIsNone(query.query_id)

    def test_query_id_present(self):
        resource = self._make_resource()
        resource["queryId"] = "test-query-id"
        query = self._make_one(resource)
        self.assertEqual(query.query_id, "test-query-id")

    def test_total_rows_present_integer(self):
        resource = self._make_resource()
        resource["totalRows"] = 42
        query = self._make_one(resource)
        self.assertEqual(query.total_rows, 42)

    def test_total_rows_present_string(self):
        resource = self._make_resource()
        resource["totalRows"] = "42"
        query = self._make_one(resource)
        self.assertEqual(query.total_rows, 42)

    def test_total_bytes_processed_missing(self):
        query = self._make_one(self._make_resource())
        self.assertIsNone(query.total_bytes_processed)

    def test_total_bytes_processed_present_integer(self):
        resource = self._make_resource()
        resource["totalBytesProcessed"] = 123456
        query = self._make_one(resource)
        self.assertEqual(query.total_bytes_processed, 123456)

    def test_total_bytes_processed_present_string(self):
        resource = self._make_resource()
        resource["totalBytesProcessed"] = "123456"
        query = self._make_one(resource)
        self.assertEqual(query.total_bytes_processed, 123456)

    def test_slot_millis_missing(self):
        query = self._make_one(self._make_resource())
        self.assertIsNone(query.slot_millis)

    def test_slot_millis_present_integer(self):
        resource = self._make_resource()
        resource["totalSlotMs"] = 123456
        query = self._make_one(resource)
        self.assertEqual(query.slot_millis, 123456)

    def test_slot_millis_present_string(self):
        resource = self._make_resource()
        resource["totalSlotMs"] = "123456"
        query = self._make_one(resource)
        self.assertEqual(query.slot_millis, 123456)

    def test_created_missing(self):
        query = self._make_one(self._make_resource())
        self.assertIsNone(query.created)

    def test_created_present_integer(self):
        resource = self._make_resource()
        resource["creationTime"] = 1437767599006
        query = self._make_one(resource)
        self.assertEqual(query.created.timestamp() * 1000, 1437767599006)

    def test_created_present_string(self):
        resource = self._make_resource()
        resource["creationTime"] = "1437767599006"
        query = self._make_one(resource)
        self.assertEqual(query.created.timestamp() * 1000, 1437767599006)

    def test_started_missing(self):
        query = self._make_one(self._make_resource())
        self.assertIsNone(query.started)

    def test_started_present_integer(self):
        resource = self._make_resource()
        resource["startTime"] = 1437767599006
        query = self._make_one(resource)
        self.assertEqual(query.started.timestamp() * 1000, 1437767599006)

    def test_started_present_string(self):
        resource = self._make_resource()
        resource["startTime"] = "1437767599006"
        query = self._make_one(resource)
        self.assertEqual(query.started.timestamp() * 1000, 1437767599006)

    def test_ended_missing(self):
        query = self._make_one(self._make_resource())
        self.assertIsNone(query.ended)

    def test_ended_present_integer(self):
        resource = self._make_resource()
        resource["endTime"] = 1437767599006
        query = self._make_one(resource)
        self.assertEqual(query.ended.timestamp() * 1000, 1437767599006)

    def test_ended_present_string(self):
        resource = self._make_resource()
        resource["endTime"] = "1437767599006"
        query = self._make_one(resource)
        self.assertEqual(query.ended.timestamp() * 1000, 1437767599006)

    def test_num_dml_affected_rows_missing(self):
        query = self._make_one(self._make_resource())
        self.assertIsNone(query.num_dml_affected_rows)

    def test_num_dml_affected_rows_present_integer(self):
        resource = self._make_resource()
        resource["numDmlAffectedRows"] = 123456
        query = self._make_one(resource)
        self.assertEqual(query.num_dml_affected_rows, 123456)

    def test_num_dml_affected_rows_present_string(self):
        resource = self._make_resource()
        resource["numDmlAffectedRows"] = "123456"
        query = self._make_one(resource)
        self.assertEqual(query.num_dml_affected_rows, 123456)

    def test_schema(self):
        query = self._make_one(self._make_resource())
        self._verifySchema(query, self._make_resource())
        resource = self._make_resource()
        resource["schema"] = {
            "fields": [
                {"name": "full_name", "type": "STRING", "mode": "REQURED"},
                {"name": "age", "type": "INTEGER", "mode": "REQURED"},
            ]
        }
        query._set_properties(resource)
        self._verifySchema(query, resource)


class Test__query_param_from_api_repr(unittest.TestCase):
    @staticmethod
    def _call_fut(resource):
        from google.cloud.bigquery.query import _query_param_from_api_repr

        return _query_param_from_api_repr(resource)

    def test_w_scalar(self):
        from google.cloud.bigquery.query import ScalarQueryParameter

        RESOURCE = {
            "name": "foo",
            "parameterType": {"type": "INT64"},
            "parameterValue": {"value": "123"},
        }

        parameter = self._call_fut(RESOURCE)

        self.assertIsInstance(parameter, ScalarQueryParameter)
        self.assertEqual(parameter.name, "foo")
        self.assertEqual(parameter.type_, "INT64")
        self.assertEqual(parameter.value, 123)

    def test_w_scalar_timestamp(self):
        from google.cloud._helpers import UTC
        from google.cloud.bigquery.query import ScalarQueryParameter

        RESOURCE = {
            "name": "zoned",
            "parameterType": {"type": "TIMESTAMP"},
            "parameterValue": {"value": "2012-03-04 05:06:07+00:00"},
        }

        parameter = self._call_fut(RESOURCE)

        self.assertIsInstance(parameter, ScalarQueryParameter)
        self.assertEqual(parameter.name, "zoned")
        self.assertEqual(parameter.type_, "TIMESTAMP")
        self.assertEqual(
            parameter.value, datetime.datetime(2012, 3, 4, 5, 6, 7, tzinfo=UTC)
        )

    def test_w_scalar_timestamp_micros(self):
        from google.cloud._helpers import UTC
        from google.cloud.bigquery.query import ScalarQueryParameter

        RESOURCE = {
            "name": "zoned",
            "parameterType": {"type": "TIMESTAMP"},
            "parameterValue": {"value": "2012-03-04 05:06:07.250000+00:00"},
        }

        parameter = self._call_fut(RESOURCE)

        self.assertIsInstance(parameter, ScalarQueryParameter)
        self.assertEqual(parameter.name, "zoned")
        self.assertEqual(parameter.type_, "TIMESTAMP")
        self.assertEqual(
            parameter.value, datetime.datetime(2012, 3, 4, 5, 6, 7, 250000, tzinfo=UTC)
        )

    def test_w_array(self):
        from google.cloud.bigquery.query import ArrayQueryParameter

        RESOURCE = {
            "name": "foo",
            "parameterType": {"type": "ARRAY", "arrayType": {"type": "INT64"}},
            "parameterValue": {"arrayValues": [{"value": "123"}]},
        }

        parameter = self._call_fut(RESOURCE)

        self.assertIsInstance(parameter, ArrayQueryParameter)
        self.assertEqual(parameter.name, "foo")
        self.assertEqual(parameter.array_type, "INT64")
        self.assertEqual(parameter.values, [123])

    def test_w_struct(self):
        from google.cloud.bigquery.query import StructQueryParameter

        RESOURCE = {
            "name": "foo",
            "parameterType": {
                "type": "STRUCT",
                "structTypes": [
                    {"name": "foo", "type": {"type": "STRING"}},
                    {"name": "bar", "type": {"type": "INT64"}},
                ],
            },
            "parameterValue": {
                "structValues": {"foo": {"value": "Foo"}, "bar": {"value": "123"}}
            },
        }

        parameter = self._call_fut(RESOURCE)

        self.assertIsInstance(parameter, StructQueryParameter)
        self.assertEqual(parameter.name, "foo")
        self.assertEqual(parameter.struct_types, {"foo": "STRING", "bar": "INT64"})
        self.assertEqual(parameter.struct_values, {"foo": "Foo", "bar": 123})
