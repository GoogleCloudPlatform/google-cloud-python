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
import json
import os
import warnings
import pytest
import packaging
import unittest
from unittest import mock

import google.api_core
from google.cloud.bigquery._helpers import _isinstance_or_raise


@pytest.mark.skipif(
    packaging.version.parse(getattr(google.api_core, "__version__", "0.0.0"))
    < packaging.version.Version("2.15.0"),
    reason="universe_domain not supported with google-api-core < 2.15.0",
)
class Test_get_client_universe(unittest.TestCase):
    def test_with_none(self):
        from google.cloud.bigquery._helpers import _get_client_universe

        self.assertEqual("googleapis.com", _get_client_universe(None))

    def test_with_dict(self):
        from google.cloud.bigquery._helpers import _get_client_universe

        options = {"universe_domain": "foo.com"}
        self.assertEqual("foo.com", _get_client_universe(options))

    def test_with_dict_empty(self):
        from google.cloud.bigquery._helpers import _get_client_universe

        options = {"universe_domain": ""}
        self.assertEqual("googleapis.com", _get_client_universe(options))

    def test_with_client_options(self):
        from google.cloud.bigquery._helpers import _get_client_universe
        from google.api_core import client_options

        options = client_options.from_dict({"universe_domain": "foo.com"})
        self.assertEqual("foo.com", _get_client_universe(options))

    @mock.patch.dict(os.environ, {"GOOGLE_CLOUD_UNIVERSE_DOMAIN": "foo.com"})
    def test_with_environ(self):
        from google.cloud.bigquery._helpers import _get_client_universe

        self.assertEqual("foo.com", _get_client_universe(None))

    @mock.patch.dict(os.environ, {"GOOGLE_CLOUD_UNIVERSE_DOMAIN": "foo.com"})
    def test_with_environ_and_dict(self):
        from google.cloud.bigquery._helpers import _get_client_universe

        options = ({"credentials_file": "file.json"},)
        self.assertEqual("foo.com", _get_client_universe(options))

    @mock.patch.dict(os.environ, {"GOOGLE_CLOUD_UNIVERSE_DOMAIN": "foo.com"})
    def test_with_environ_and_empty_options(self):
        from google.cloud.bigquery._helpers import _get_client_universe
        from google.api_core import client_options

        options = client_options.from_dict({})
        self.assertEqual("foo.com", _get_client_universe(options))

    @mock.patch.dict(os.environ, {"GOOGLE_CLOUD_UNIVERSE_DOMAIN": ""})
    def test_with_environ_empty(self):
        from google.cloud.bigquery._helpers import _get_client_universe

        self.assertEqual("googleapis.com", _get_client_universe(None))


class Test_validate_universe(unittest.TestCase):
    def test_with_none(self):
        from google.cloud.bigquery._helpers import _validate_universe

        # should not raise
        _validate_universe("googleapis.com", None)

    def test_with_no_universe_creds(self):
        from google.cloud.bigquery._helpers import _validate_universe
        from .helpers import make_creds

        creds = make_creds(None)
        # should not raise
        _validate_universe("googleapis.com", creds)

    def test_with_matched_universe_creds(self):
        from google.cloud.bigquery._helpers import _validate_universe
        from .helpers import make_creds

        creds = make_creds("googleapis.com")
        # should not raise
        _validate_universe("googleapis.com", creds)

    def test_with_mismatched_universe_creds(self):
        from google.cloud.bigquery._helpers import _validate_universe
        from .helpers import make_creds

        creds = make_creds("foo.com")
        with self.assertRaises(ValueError):
            _validate_universe("googleapis.com", creds)


class Test_not_null(unittest.TestCase):
    def _call_fut(self, value, field):
        from google.cloud.bigquery._helpers import _not_null

        return _not_null(value, field)

    def test_w_none_nullable(self):
        self.assertFalse(self._call_fut(None, _Field("NULLABLE")))

    def test_w_none_required(self):
        self.assertTrue(self._call_fut(None, _Field("REQUIRED")))

    def test_w_value(self):
        self.assertTrue(self._call_fut(object(), object()))


class Test_field_to_index_mapping(unittest.TestCase):
    def _call_fut(self, schema):
        from google.cloud.bigquery._helpers import _field_to_index_mapping

        return _field_to_index_mapping(schema)

    def test_w_empty_schema(self):
        self.assertEqual(self._call_fut([]), {})

    def test_w_non_empty_schema(self):
        schema = [
            _Field("REPEATED", "first", "INTEGER"),
            _Field("REQUIRED", "second", "INTEGER"),
            _Field("REPEATED", "third", "INTEGER"),
        ]
        self.assertEqual(self._call_fut(schema), {"first": 0, "second": 1, "third": 2})


class Test_row_tuple_from_json(unittest.TestCase):
    def _call_fut(self, row, schema):
        from google.cloud.bigquery._helpers import _row_tuple_from_json

        with _field_isinstance_patcher():
            return _row_tuple_from_json(row, schema)

    def test_w_single_scalar_column(self):
        # SELECT 1 AS col
        col = _Field("REQUIRED", "col", "INTEGER")
        row = {"f": [{"v": "1"}]}
        self.assertEqual(self._call_fut(row, schema=[col]), (1,))

    def test_w_unknown_type(self):
        # SELECT 1 AS col
        col = _Field("REQUIRED", "col", "UNKNOWN")
        row = {"f": [{"v": "1"}]}
        with warnings.catch_warnings(record=True) as warned:
            self.assertEqual(self._call_fut(row, schema=[col]), ("1",))
        self.assertEqual(len(warned), 1)
        warning = warned[0]
        self.assertTrue("UNKNOWN" in str(warning))
        self.assertTrue("col" in str(warning))

    def test_w_single_scalar_geography_column(self):
        # SELECT 1 AS col
        col = _Field("REQUIRED", "geo", "GEOGRAPHY")
        row = {"f": [{"v": "POINT(1, 2)"}]}
        self.assertEqual(self._call_fut(row, schema=[col]), ("POINT(1, 2)",))

    def test_w_single_struct_column(self):
        # SELECT (1, 2) AS col
        sub_1 = _Field("REQUIRED", "sub_1", "INTEGER")
        sub_2 = _Field("REQUIRED", "sub_2", "INTEGER")
        col = _Field("REQUIRED", "col", "RECORD", fields=[sub_1, sub_2])
        row = {"f": [{"v": {"f": [{"v": "1"}, {"v": "2"}]}}]}
        self.assertEqual(self._call_fut(row, schema=[col]), ({"sub_1": 1, "sub_2": 2},))

    def test_w_single_array_column(self):
        # SELECT [1, 2, 3] as col
        col = _Field("REPEATED", "col", "INTEGER")
        row = {"f": [{"v": [{"v": "1"}, {"v": "2"}, {"v": "3"}]}]}
        self.assertEqual(self._call_fut(row, schema=[col]), ([1, 2, 3],))

    def test_w_unknown_type_repeated(self):
        # SELECT 1 AS col
        col = _Field("REPEATED", "col", "UNKNOWN")
        row = {"f": [{"v": [{"v": "1"}, {"v": "2"}, {"v": "3"}]}]}
        with warnings.catch_warnings(record=True) as warned:
            self.assertEqual(self._call_fut(row, schema=[col]), (["1", "2", "3"],))
        self.assertEqual(len(warned), 1)
        warning = warned[0]
        self.assertTrue("UNKNOWN" in str(warning))
        self.assertTrue("col" in str(warning))

    def test_w_struct_w_nested_array_column(self):
        # SELECT ([1, 2], 3, [4, 5]) as col
        first = _Field("REPEATED", "first", "INTEGER")
        second = _Field("REQUIRED", "second", "INTEGER")
        third = _Field("REPEATED", "third", "INTEGER")
        col = _Field("REQUIRED", "col", "RECORD", fields=[first, second, third])
        row = {
            "f": [
                {
                    "v": {
                        "f": [
                            {"v": [{"v": "1"}, {"v": "2"}]},
                            {"v": "3"},
                            {"v": [{"v": "4"}, {"v": "5"}]},
                        ]
                    }
                }
            ]
        }
        self.assertEqual(
            self._call_fut(row, schema=[col]),
            ({"first": [1, 2], "second": 3, "third": [4, 5]},),
        )

    def test_w_unknown_type_subfield(self):
        # SELECT [(1, 2, 3), (4, 5, 6)] as col
        first = _Field("REPEATED", "first", "UNKNOWN1")
        second = _Field("REQUIRED", "second", "UNKNOWN2")
        third = _Field("REPEATED", "third", "INTEGER")
        col = _Field("REQUIRED", "col", "RECORD", fields=[first, second, third])
        row = {
            "f": [
                {
                    "v": {
                        "f": [
                            {"v": [{"v": "1"}, {"v": "2"}]},
                            {"v": "3"},
                            {"v": [{"v": "4"}, {"v": "5"}]},
                        ]
                    }
                }
            ]
        }
        with warnings.catch_warnings(record=True) as warned:
            self.assertEqual(
                self._call_fut(row, schema=[col]),
                ({"first": ["1", "2"], "second": "3", "third": [4, 5]},),
            )
        self.assertEqual(len(warned), 2)  # 1 warning per unknown field.
        warned = [str(warning) for warning in warned]
        self.assertTrue(
            any(["first" in warning and "UNKNOWN1" in warning for warning in warned])
        )
        self.assertTrue(
            any(["second" in warning and "UNKNOWN2" in warning for warning in warned])
        )

    def test_w_array_of_struct(self):
        # SELECT [(1, 2, 3), (4, 5, 6)] as col
        first = _Field("REQUIRED", "first", "INTEGER")
        second = _Field("REQUIRED", "second", "INTEGER")
        third = _Field("REQUIRED", "third", "INTEGER")
        col = _Field("REPEATED", "col", "RECORD", fields=[first, second, third])
        row = {
            "f": [
                {
                    "v": [
                        {"v": {"f": [{"v": "1"}, {"v": "2"}, {"v": "3"}]}},
                        {"v": {"f": [{"v": "4"}, {"v": "5"}, {"v": "6"}]}},
                    ]
                }
            ]
        }
        self.assertEqual(
            self._call_fut(row, schema=[col]),
            (
                [
                    {"first": 1, "second": 2, "third": 3},
                    {"first": 4, "second": 5, "third": 6},
                ],
            ),
        )

    def test_w_array_of_struct_w_array(self):
        # SELECT [([1, 2, 3], 4), ([5, 6], 7)]
        first = _Field("REPEATED", "first", "INTEGER")
        second = _Field("REQUIRED", "second", "INTEGER")
        col = _Field("REPEATED", "col", "RECORD", fields=[first, second])
        row = {
            "f": [
                {
                    "v": [
                        {
                            "v": {
                                "f": [
                                    {"v": [{"v": "1"}, {"v": "2"}, {"v": "3"}]},
                                    {"v": "4"},
                                ]
                            }
                        },
                        {"v": {"f": [{"v": [{"v": "5"}, {"v": "6"}]}, {"v": "7"}]}},
                    ]
                }
            ]
        }
        self.assertEqual(
            self._call_fut(row, schema=[col]),
            ([{"first": [1, 2, 3], "second": 4}, {"first": [5, 6], "second": 7}],),
        )


class Test_rows_from_json(unittest.TestCase):
    def _call_fut(self, rows, schema):
        from google.cloud.bigquery._helpers import _rows_from_json

        with _field_isinstance_patcher():
            return _rows_from_json(rows, schema)

    def test_w_record_subfield(self):
        from google.cloud.bigquery.table import Row

        full_name = _Field("REQUIRED", "full_name", "STRING")
        area_code = _Field("REQUIRED", "area_code", "STRING")
        local_number = _Field("REQUIRED", "local_number", "STRING")
        rank = _Field("REQUIRED", "rank", "INTEGER")
        phone = _Field(
            "NULLABLE", "phone", "RECORD", fields=[area_code, local_number, rank]
        )
        color = _Field("REPEATED", "color", "STRING")
        schema = [full_name, phone, color]
        rows = [
            {
                "f": [
                    {"v": "Phred Phlyntstone"},
                    {"v": {"f": [{"v": "800"}, {"v": "555-1212"}, {"v": 1}]}},
                    {"v": [{"v": "orange"}, {"v": "black"}]},
                ]
            },
            {
                "f": [
                    {"v": "Bharney Rhubble"},
                    {"v": {"f": [{"v": "877"}, {"v": "768-5309"}, {"v": 2}]}},
                    {"v": [{"v": "brown"}]},
                ]
            },
            {"f": [{"v": "Wylma Phlyntstone"}, {"v": None}, {"v": []}]},
        ]
        phred_phone = {"area_code": "800", "local_number": "555-1212", "rank": 1}
        bharney_phone = {"area_code": "877", "local_number": "768-5309", "rank": 2}
        f2i = {"full_name": 0, "phone": 1, "color": 2}
        expected = [
            Row(("Phred Phlyntstone", phred_phone, ["orange", "black"]), f2i),
            Row(("Bharney Rhubble", bharney_phone, ["brown"]), f2i),
            Row(("Wylma Phlyntstone", None, []), f2i),
        ]
        coerced = self._call_fut(rows, schema)
        self.assertEqual(coerced, expected)

    def test_w_int64_float64_bool(self):
        from google.cloud.bigquery.table import Row

        # "Standard" SQL dialect uses 'INT64', 'FLOAT64', 'BOOL'.
        candidate = _Field("REQUIRED", "candidate", "STRING")
        votes = _Field("REQUIRED", "votes", "INT64")
        percentage = _Field("REQUIRED", "percentage", "FLOAT64")
        incumbent = _Field("REQUIRED", "incumbent", "BOOL")
        schema = [candidate, votes, percentage, incumbent]
        rows = [
            {"f": [{"v": "Phred Phlyntstone"}, {"v": 8}, {"v": 0.25}, {"v": "true"}]},
            {"f": [{"v": "Bharney Rhubble"}, {"v": 4}, {"v": 0.125}, {"v": "false"}]},
            {
                "f": [
                    {"v": "Wylma Phlyntstone"},
                    {"v": 20},
                    {"v": 0.625},
                    {"v": "false"},
                ]
            },
        ]
        f2i = {"candidate": 0, "votes": 1, "percentage": 2, "incumbent": 3}
        expected = [
            Row(("Phred Phlyntstone", 8, 0.25, True), f2i),
            Row(("Bharney Rhubble", 4, 0.125, False), f2i),
            Row(("Wylma Phlyntstone", 20, 0.625, False), f2i),
        ]
        coerced = self._call_fut(rows, schema)
        self.assertEqual(coerced, expected)


class Test_int_to_json(unittest.TestCase):
    def _call_fut(self, value):
        from google.cloud.bigquery._helpers import _int_to_json

        return _int_to_json(value)

    def test_w_int(self):
        self.assertEqual(self._call_fut(123), "123")

    def test_w_string(self):
        self.assertEqual(self._call_fut("123"), "123")


class Test_float_to_json(unittest.TestCase):
    def _call_fut(self, value):
        from google.cloud.bigquery._helpers import _float_to_json

        return _float_to_json(value)

    def test_w_none(self):
        self.assertEqual(self._call_fut(None), None)

    def test_w_non_numeric(self):
        with self.assertRaises(TypeError):
            self._call_fut(object())

    def test_w_integer(self):
        result = self._call_fut(123)
        self.assertIsInstance(result, float)
        self.assertEqual(result, 123.0)

    def test_w_float(self):
        self.assertEqual(self._call_fut(1.23), 1.23)

    def test_w_float_as_string(self):
        self.assertEqual(self._call_fut("1.23"), 1.23)

    def test_w_nan(self):
        result = self._call_fut(float("nan"))
        self.assertEqual(result.lower(), "nan")

    def test_w_nan_as_string(self):
        result = self._call_fut("NaN")
        self.assertEqual(result.lower(), "nan")

    def test_w_infinity(self):
        result = self._call_fut(float("inf"))
        self.assertEqual(result.lower(), "inf")

    def test_w_infinity_as_string(self):
        result = self._call_fut("inf")
        self.assertEqual(result.lower(), "inf")

    def test_w_negative_infinity(self):
        result = self._call_fut(float("-inf"))
        self.assertEqual(result.lower(), "-inf")

    def test_w_negative_infinity_as_string(self):
        result = self._call_fut("-inf")
        self.assertEqual(result.lower(), "-inf")


class Test_decimal_to_json(unittest.TestCase):
    def _call_fut(self, value):
        from google.cloud.bigquery._helpers import _decimal_to_json

        return _decimal_to_json(value)

    def test_w_float(self):
        self.assertEqual(self._call_fut(1.23), 1.23)

    def test_w_string(self):
        self.assertEqual(self._call_fut("1.23"), "1.23")

    def test_w_decimal(self):
        self.assertEqual(self._call_fut(decimal.Decimal("1.23")), "1.23")


class Test_bool_to_json(unittest.TestCase):
    def _call_fut(self, value):
        from google.cloud.bigquery._helpers import _bool_to_json

        return _bool_to_json(value)

    def test_w_true(self):
        self.assertEqual(self._call_fut(True), "true")

    def test_w_false(self):
        self.assertEqual(self._call_fut(False), "false")

    def test_w_string(self):
        self.assertEqual(self._call_fut("false"), "false")


class Test_bytes_to_json(unittest.TestCase):
    def _call_fut(self, value):
        from google.cloud.bigquery._helpers import _bytes_to_json

        return _bytes_to_json(value)

    def test_w_non_bytes(self):
        non_bytes = object()
        self.assertIs(self._call_fut(non_bytes), non_bytes)

    def test_w_bytes(self):
        source = b"source"
        expected = "c291cmNl"
        converted = self._call_fut(source)
        self.assertEqual(converted, expected)


class Test_timestamp_to_json_parameter(unittest.TestCase):
    def _call_fut(self, value):
        from google.cloud.bigquery._helpers import _timestamp_to_json_parameter

        return _timestamp_to_json_parameter(value)

    def test_w_float(self):
        self.assertEqual(self._call_fut(1.234567), 1.234567)

    def test_w_string(self):
        ZULU = "2016-12-20 15:58:27.339328+00:00"
        self.assertEqual(self._call_fut(ZULU), ZULU)

    def test_w_datetime_wo_zone(self):
        ZULU = "2016-12-20 15:58:27.339328+00:00"
        when = datetime.datetime(2016, 12, 20, 15, 58, 27, 339328)
        self.assertEqual(self._call_fut(when), ZULU)

    def test_w_datetime_w_non_utc_zone(self):
        class _Zone(datetime.tzinfo):
            def utcoffset(self, _):
                return datetime.timedelta(minutes=-240)

        ZULU = "2016-12-20 19:58:27.339328+00:00"
        when = datetime.datetime(2016, 12, 20, 15, 58, 27, 339328, tzinfo=_Zone())
        self.assertEqual(self._call_fut(when), ZULU)

    def test_w_datetime_w_utc_zone(self):
        from google.cloud._helpers import UTC

        ZULU = "2016-12-20 15:58:27.339328+00:00"
        when = datetime.datetime(2016, 12, 20, 15, 58, 27, 339328, tzinfo=UTC)
        self.assertEqual(self._call_fut(when), ZULU)


class Test_timestamp_to_json_row(unittest.TestCase):
    def _call_fut(self, value):
        from google.cloud.bigquery._helpers import _timestamp_to_json_row

        return _timestamp_to_json_row(value)

    def test_w_float(self):
        self.assertEqual(self._call_fut(1.234567), 1.234567)

    def test_w_string(self):
        ZULU = "2016-12-20 15:58:27.339328+00:00"
        self.assertEqual(self._call_fut(ZULU), ZULU)

    def test_w_datetime_no_zone(self):
        when = datetime.datetime(2016, 12, 20, 15, 58, 27, 339328)
        self.assertEqual(self._call_fut(when), "2016-12-20T15:58:27.339328Z")

    def test_w_datetime_w_utc_zone(self):
        from google.cloud._helpers import UTC

        when = datetime.datetime(2020, 11, 17, 1, 6, 52, 353795, tzinfo=UTC)
        self.assertEqual(self._call_fut(when), "2020-11-17T01:06:52.353795Z")

    def test_w_datetime_w_non_utc_zone(self):
        class EstZone(datetime.tzinfo):
            def utcoffset(self, _):
                return datetime.timedelta(minutes=-300)

        when = datetime.datetime(2020, 11, 17, 1, 6, 52, 353795, tzinfo=EstZone())
        self.assertEqual(self._call_fut(when), "2020-11-17T06:06:52.353795Z")


class Test_datetime_to_json(unittest.TestCase):
    def _call_fut(self, value):
        from google.cloud.bigquery._helpers import _datetime_to_json

        return _datetime_to_json(value)

    def test_w_string(self):
        RFC3339 = "2016-12-03T14:14:51Z"
        self.assertEqual(self._call_fut(RFC3339), RFC3339)

    def test_w_datetime(self):
        from google.cloud._helpers import UTC

        when = datetime.datetime(2016, 12, 3, 14, 11, 27, 123456, tzinfo=UTC)
        self.assertEqual(self._call_fut(when), "2016-12-03T14:11:27.123456")

    def test_w_datetime_w_non_utc_zone(self):
        class EstZone(datetime.tzinfo):
            def utcoffset(self, _):
                return datetime.timedelta(minutes=-300)

        when = datetime.datetime(2016, 12, 3, 14, 11, 27, 123456, tzinfo=EstZone())
        self.assertEqual(self._call_fut(when), "2016-12-03T19:11:27.123456")


class Test_date_to_json(unittest.TestCase):
    def _call_fut(self, value):
        from google.cloud.bigquery._helpers import _date_to_json

        return _date_to_json(value)

    def test_w_string(self):
        RFC3339 = "2016-12-03"
        self.assertEqual(self._call_fut(RFC3339), RFC3339)

    def test_w_datetime(self):
        when = datetime.date(2016, 12, 3)
        self.assertEqual(self._call_fut(when), "2016-12-03")


class Test_time_to_json(unittest.TestCase):
    def _call_fut(self, value):
        from google.cloud.bigquery._helpers import _time_to_json

        return _time_to_json(value)

    def test_w_string(self):
        RFC3339 = "12:13:41"
        self.assertEqual(self._call_fut(RFC3339), RFC3339)

    def test_w_datetime(self):
        when = datetime.time(12, 13, 41)
        self.assertEqual(self._call_fut(when), "12:13:41")


def _make_field(
    field_type,
    mode="NULLABLE",
    name="testing",
    fields=(),
    range_element_type=None,
):
    from google.cloud.bigquery.schema import SchemaField

    return SchemaField(
        name=name,
        field_type=field_type,
        mode=mode,
        fields=fields,
        range_element_type=range_element_type,
    )


class Test_scalar_field_to_json(unittest.TestCase):
    def _call_fut(self, field, value):
        from google.cloud.bigquery._helpers import _scalar_field_to_json

        return _scalar_field_to_json(field, value)

    def test_w_unknown_field_type(self):
        field = _make_field("UNKNOWN")
        original = object()
        with warnings.catch_warnings(record=True) as warned:
            converted = self._call_fut(field, original)
        self.assertIs(converted, original)
        self.assertEqual(len(warned), 1)
        warning = warned[0]
        self.assertTrue("UNKNOWN" in str(warning))

    def test_w_known_field_type(self):
        field = _make_field("INT64")
        original = 42
        converted = self._call_fut(field, original)
        self.assertEqual(converted, str(original))

    def test_w_scalar_none(self):
        import google.cloud.bigquery._helpers as module_under_test

        scalar_types = module_under_test._SCALAR_VALUE_TO_JSON_ROW.keys()
        for type_ in scalar_types:
            field = _make_field(type_)
            original = None
            converted = self._call_fut(field, original)
            self.assertIsNone(converted, msg=f"{type_} did not return None")


class Test_single_field_to_json(unittest.TestCase):
    def _call_fut(self, field, value):
        from google.cloud.bigquery._helpers import _single_field_to_json

        return _single_field_to_json(field, value)

    def test_w_none(self):
        field = _make_field("INT64")
        original = None
        converted = self._call_fut(field, original)
        self.assertIsNone(converted)

    def test_w_record(self):
        subfields = [
            _make_field("INT64", name="one"),
            _make_field("STRING", name="two"),
        ]
        field = _make_field("RECORD", fields=subfields)
        original = {"one": 42, "two": "two"}
        converted = self._call_fut(field, original)
        self.assertEqual(converted, {"one": "42", "two": "two"})

    def test_w_scalar(self):
        field = _make_field("INT64")
        original = 42
        converted = self._call_fut(field, original)
        self.assertEqual(converted, str(original))

    def test_w_scalar_ignores_mode(self):
        field = _make_field("STRING", mode="REPEATED")
        original = "hello world"
        converted = self._call_fut(field, original)
        self.assertEqual(converted, original)

    def test_w_scalar_json(self):
        field = _make_field("JSON")
        original = {"alpha": "abc", "num": [1, 2, 3]}
        converted = self._call_fut(field, original)
        self.assertEqual(converted, json.dumps(original))


class Test_repeated_field_to_json(unittest.TestCase):
    def _call_fut(self, field, value):
        from google.cloud.bigquery._helpers import _repeated_field_to_json

        return _repeated_field_to_json(field, value)

    def test_w_empty(self):
        field = _make_field("INT64", mode="REPEATED")
        original = []
        converted = self._call_fut(field, original)
        self.assertEqual(converted, original)
        self.assertEqual(field.mode, "REPEATED")

    def test_w_non_empty(self):
        field = _make_field("INT64", mode="REPEATED")
        original = [42]
        converted = self._call_fut(field, original)
        self.assertEqual(converted, [str(value) for value in original])
        self.assertEqual(field.mode, "REPEATED")


class Test_record_field_to_json(unittest.TestCase):
    def _call_fut(self, field, value):
        from google.cloud.bigquery._helpers import _record_field_to_json

        return _record_field_to_json(field, value)

    def test_w_empty(self):
        fields = []
        original = []
        converted = self._call_fut(fields, original)
        self.assertEqual(converted, {})

    def test_w_non_empty_list(self):
        fields = [
            _make_field("INT64", name="one", mode="NULLABLE"),
            _make_field("STRING", name="two", mode="NULLABLE"),
        ]
        original = [42, "two"]
        converted = self._call_fut(fields, original)
        self.assertEqual(converted, {"one": "42", "two": "two"})

    def test_w_list_missing_fields(self):
        fields = [
            _make_field("INT64", name="one", mode="NULLABLE"),
            _make_field("STRING", name="two", mode="NULLABLE"),
        ]
        original = [42]

        with self.assertRaisesRegex(ValueError, r".*not match schema length.*"):
            self._call_fut(fields, original)

    def test_w_list_too_many_fields(self):
        fields = [
            _make_field("INT64", name="one", mode="NULLABLE"),
            _make_field("STRING", name="two", mode="NULLABLE"),
        ]
        original = [42, "two", "three"]

        with self.assertRaisesRegex(ValueError, r".*not match schema length.*"):
            self._call_fut(fields, original)

    def test_w_non_empty_dict(self):
        fields = [
            _make_field("INT64", name="one", mode="NULLABLE"),
            _make_field("STRING", name="two", mode="NULLABLE"),
        ]
        original = {"one": 42, "two": "two"}
        converted = self._call_fut(fields, original)
        self.assertEqual(converted, {"one": "42", "two": "two"})

    def test_w_some_missing_nullables(self):
        fields = [
            _make_field("INT64", name="one", mode="NULLABLE"),
            _make_field("STRING", name="two", mode="NULLABLE"),
        ]
        original = {"one": 42}
        converted = self._call_fut(fields, original)

        # missing fields should not be converted to an explicit None
        self.assertEqual(converted, {"one": "42"})

    def test_w_all_missing_nullables(self):
        fields = [
            _make_field("INT64", name="one", mode="NULLABLE"),
            _make_field("STRING", name="two", mode="NULLABLE"),
        ]
        original = {}
        converted = self._call_fut(fields, original)

        # we should get an empty dict, not None
        self.assertEqual(converted, {})

    def test_w_explicit_none_value(self):
        fields = [
            _make_field("INT64", name="one", mode="NULLABLE"),
            _make_field("STRING", name="two", mode="NULLABLE"),
            _make_field("BOOL", name="three", mode="REPEATED"),
        ]
        original = {"three": None, "one": 42, "two": None}
        converted = self._call_fut(fields, original)

        # None values should be dropped regardless of the field type
        self.assertEqual(converted, {"one": "42"})

    def test_w_dict_unknown_fields(self):
        fields = [
            _make_field("INT64", name="one", mode="NULLABLE"),
            _make_field("STRING", name="two", mode="NULLABLE"),
        ]
        original = {
            "whoami": datetime.date(2020, 7, 20),
            "one": 111,
            "two": "222",
            "void": None,
        }

        converted = self._call_fut(fields, original)

        # Unknown fields should be included (if not None), but converted as strings.
        self.assertEqual(
            converted,
            {"whoami": "2020-07-20", "one": "111", "two": "222"},
        )


class Test_range_field_to_json(unittest.TestCase):
    def _call_fut(self, field, value):
        from google.cloud.bigquery._helpers import _range_field_to_json

        return _range_field_to_json(field, value)

    def test_w_date(self):
        field = _make_field("RANGE", range_element_type="DATE")
        start = datetime.date(2016, 12, 3)
        original = {"start": start}
        converted = self._call_fut(field.range_element_type, original)
        expected = {"start": "2016-12-03", "end": None}
        self.assertEqual(converted, expected)

    def test_w_date_string(self):
        field = _make_field("RANGE", range_element_type="DATE")
        original = {"start": "2016-12-03"}
        converted = self._call_fut(field.range_element_type, original)
        expected = {"start": "2016-12-03", "end": None}
        self.assertEqual(converted, expected)

    def test_w_datetime(self):
        field = _make_field("RANGE", range_element_type="DATETIME")
        start = datetime.datetime(2016, 12, 3, 14, 11, 27, 123456)
        original = {"start": start}
        converted = self._call_fut(field.range_element_type, original)
        expected = {"start": "2016-12-03T14:11:27.123456", "end": None}
        self.assertEqual(converted, expected)

    def test_w_datetime_string(self):
        field = _make_field("RANGE", range_element_type="DATETIME")
        original = {"start": "2016-12-03T14:11:27.123456"}
        converted = self._call_fut(field.range_element_type, original)
        expected = {"start": "2016-12-03T14:11:27.123456", "end": None}
        self.assertEqual(converted, expected)

    def test_w_timestamp(self):
        from google.cloud._helpers import UTC

        field = _make_field("RANGE", range_element_type="TIMESTAMP")
        start = datetime.datetime(2016, 12, 3, 14, 11, 27, 123456, tzinfo=UTC)
        original = {"start": start}
        converted = self._call_fut(field.range_element_type, original)
        expected = {"start": "2016-12-03T14:11:27.123456Z", "end": None}
        self.assertEqual(converted, expected)

    def test_w_timestamp_string(self):
        field = _make_field("RANGE", range_element_type="TIMESTAMP")
        original = {"start": "2016-12-03T14:11:27.123456Z"}
        converted = self._call_fut(field.range_element_type, original)
        expected = {"start": "2016-12-03T14:11:27.123456Z", "end": None}
        self.assertEqual(converted, expected)

    def test_w_timestamp_float(self):
        field = _make_field("RANGE", range_element_type="TIMESTAMP")
        original = {"start": 12.34567}
        converted = self._call_fut(field.range_element_type, original)
        expected = {"start": 12.34567, "end": None}
        self.assertEqual(converted, expected)

    def test_w_string_literal(self):
        field = _make_field("RANGE", range_element_type="DATE")
        original = "[2016-12-03, UNBOUNDED)"
        converted = self._call_fut(field.range_element_type, original)
        expected = {"start": "2016-12-03", "end": None}
        self.assertEqual(converted, expected)

    def test_w_unsupported_range_element_type(self):
        field = _make_field("RANGE", range_element_type="TIME")
        with self.assertRaises(ValueError):
            self._call_fut(
                field.range_element_type,
                {"start": datetime.time(12, 13, 41)},
            )

    def test_w_no_range_element_type(self):
        field = _make_field("RANGE")
        with self.assertRaises(ValueError):
            self._call_fut(field.range_element_type, "2016-12-03")

    def test_w_incorrect_literal_format(self):
        field = _make_field("RANGE", range_element_type="DATE")
        original = "[2016-12-03, UNBOUNDED]"
        with self.assertRaises(ValueError):
            self._call_fut(field.range_element_type, original)

    def test_w_unsupported_representation(self):
        field = _make_field("RANGE", range_element_type="DATE")
        with self.assertRaises(ValueError):
            self._call_fut(field.range_element_type, object())


class Test_field_to_json(unittest.TestCase):
    def _call_fut(self, field, value):
        from google.cloud.bigquery._helpers import _field_to_json

        return _field_to_json(field, value)

    def test_w_none(self):
        field = _make_field("INT64")
        original = None
        converted = self._call_fut(field, original)
        self.assertIsNone(converted)

    def test_w_repeated(self):
        field = _make_field("INT64", mode="REPEATED")
        original = [42, 17]
        converted = self._call_fut(field, original)
        self.assertEqual(converted, [str(value) for value in original])

    def test_w_record(self):
        subfields = [
            _make_field("INT64", name="one"),
            _make_field("STRING", name="two"),
        ]
        field = _make_field("RECORD", fields=subfields)
        original = {"one": 42, "two": "two"}
        converted = self._call_fut(field, original)
        self.assertEqual(converted, {"one": "42", "two": "two"})

    def test_w_scalar(self):
        field = _make_field("INT64")
        original = 42
        converted = self._call_fut(field, original)
        self.assertEqual(converted, str(original))

    def test_w_range(self):
        field = _make_field("RANGE", range_element_type="DATE")
        original = {"start": "2016-12-03", "end": "2024-12-03"}
        converted = self._call_fut(field, original)
        self.assertEqual(converted, original)


class Test_snake_to_camel_case(unittest.TestCase):
    def _call_fut(self, value):
        from google.cloud.bigquery._helpers import _snake_to_camel_case

        return _snake_to_camel_case(value)

    def test_w_snake_case_string(self):
        self.assertEqual(self._call_fut("friendly_name"), "friendlyName")

    def test_w_camel_case_string(self):
        self.assertEqual(self._call_fut("friendlyName"), "friendlyName")


class Test__get_sub_prop(unittest.TestCase):
    def _call_fut(self, container, keys, **kw):
        from google.cloud.bigquery._helpers import _get_sub_prop

        return _get_sub_prop(container, keys, **kw)

    def test_w_empty_container_default_default(self):
        self.assertIsNone(self._call_fut({}, ["key1"]))

    def test_w_missing_key_explicit_default(self):
        self.assertEqual(self._call_fut({"key2": 2}, ["key1"], default=1), 1)

    def test_w_matching_single_key_in_sequence(self):
        self.assertEqual(self._call_fut({"key1": 1}, ["key1"]), 1)

    def test_w_matching_single_string_key(self):
        data = {"k": {"e": {"y": "foo"}}, "key": "bar"}
        self.assertEqual(self._call_fut(data, "key"), "bar")

    def test_w_matching_first_key_missing_second_key(self):
        self.assertIsNone(self._call_fut({"key1": {"key3": 3}}, ["key1", "key2"]))

    def test_w_matching_first_key_matching_second_key(self):
        self.assertEqual(self._call_fut({"key1": {"key2": 2}}, ["key1", "key2"]), 2)


class Test__set_sub_prop(unittest.TestCase):
    def _call_fut(self, container, keys, value):
        from google.cloud.bigquery._helpers import _set_sub_prop

        return _set_sub_prop(container, keys, value)

    def test_w_empty_container_single_key_in_sequence(self):
        container = {}
        self._call_fut(container, ["key1"], "value")
        self.assertEqual(container, {"key1": "value"})

    def test_w_empty_container_single_string_key(self):
        container = {}
        self._call_fut(container, "key", "value")
        self.assertEqual(container, {"key": "value"})

    def test_w_empty_container_nested_keys(self):
        container = {}
        self._call_fut(container, ["key1", "key2", "key3"], "value")
        self.assertEqual(container, {"key1": {"key2": {"key3": "value"}}})

    def test_w_existing_value(self):
        container = {"key1": "before"}
        self._call_fut(container, ["key1"], "after")
        self.assertEqual(container, {"key1": "after"})

    def test_w_nested_keys_existing_value(self):
        container = {"key1": {"key2": {"key3": "before"}}}
        self._call_fut(container, ["key1", "key2", "key3"], "after")
        self.assertEqual(container, {"key1": {"key2": {"key3": "after"}}})


class Test__del_sub_prop(unittest.TestCase):
    def _call_fut(self, container, keys):
        from google.cloud.bigquery._helpers import _del_sub_prop

        return _del_sub_prop(container, keys)

    def test_w_single_key(self):
        container = {"key1": "value"}
        self._call_fut(container, ["key1"])
        self.assertEqual(container, {})

    def test_w_empty_container_nested_keys(self):
        container = {}
        self._call_fut(container, ["key1", "key2", "key3"])
        self.assertEqual(container, {"key1": {"key2": {}}})

    def test_w_existing_value_nested_keys(self):
        container = {"key1": {"key2": {"key3": "value"}}}
        self._call_fut(container, ["key1", "key2", "key3"])
        self.assertEqual(container, {"key1": {"key2": {}}})


class Test__int_or_none(unittest.TestCase):
    def _call_fut(self, value):
        from google.cloud.bigquery._helpers import _int_or_none

        return _int_or_none(value)

    def test_w_num_string(self):
        self.assertEqual(self._call_fut("123"), 123)

    def test_w_none(self):
        self.assertIsNone(self._call_fut(None))

    def test_w_int(self):
        self.assertEqual(self._call_fut(123), 123)

    def test_w_non_num_string(self):
        with self.assertRaises(ValueError):
            self._call_fut("ham")


class Test__str_or_none(unittest.TestCase):
    def _call_fut(self, value):
        from google.cloud.bigquery._helpers import _str_or_none

        return _str_or_none(value)

    def test_w_int(self):
        self.assertEqual(self._call_fut(123), "123")

    def test_w_none(self):
        self.assertIsNone(self._call_fut(None))

    def test_w_str(self):
        self.assertEqual(self._call_fut("ham"), "ham")


class _Field(object):
    def __init__(
        self,
        mode,
        name="unknown",
        field_type="UNKNOWN",
        fields=(),
        range_element_type=None,
        element_type=None,
    ):
        self.mode = mode
        self.name = name
        self.field_type = field_type
        self.fields = fields
        self.range_element_type = range_element_type
        self.element_type = element_type


def _field_isinstance_patcher():
    """A patcher thank makes _Field instances seem like SchemaField instances."""
    from google.cloud.bigquery.schema import SchemaField

    def fake_isinstance(instance, target_class):
        if instance.__class__.__name__ != "_Field":
            return isinstance(instance, target_class)  # pragma: NO COVER

        # pretend that _Field() instances are actually instances of SchemaField
        return target_class is SchemaField or (
            isinstance(target_class, tuple) and SchemaField in target_class
        )

    patcher = mock.patch(
        "google.cloud.bigquery.schema.isinstance", side_effect=fake_isinstance
    )
    return patcher


def test_decimal_as_float_api_repr():
    """Make sure decimals get converted to float."""
    import google.cloud.bigquery.query
    from decimal import Decimal

    param = google.cloud.bigquery.query.ScalarQueryParameter(
        "x", "FLOAT64", Decimal(42)
    )
    assert param.to_api_repr() == {
        "parameterType": {"type": "FLOAT64"},
        "parameterValue": {"value": 42.0},
        "name": "x",
    }


class Test__get_bigquery_host(unittest.TestCase):
    @staticmethod
    def _call_fut():
        from google.cloud.bigquery._helpers import _get_bigquery_host

        return _get_bigquery_host()

    def test_wo_env_var(self):
        from google.cloud.bigquery._helpers import _DEFAULT_HOST

        with mock.patch("os.environ", {}):
            host = self._call_fut()

        self.assertEqual(host, _DEFAULT_HOST)

    def test_w_env_var(self):
        from google.cloud.bigquery._helpers import BIGQUERY_EMULATOR_HOST

        HOST = "https://api.example.com"

        with mock.patch("os.environ", {BIGQUERY_EMULATOR_HOST: HOST}):
            host = self._call_fut()

        self.assertEqual(host, HOST)


class Test__isinstance_or_raise:
    @pytest.mark.parametrize(
        "value,dtype,none_allowed,expected",
        [
            (None, str, True, None),
            ("hello world.uri", str, True, "hello world.uri"),
            ("hello world.uri", str, False, "hello world.uri"),
            (None, (str, float), True, None),
            ("hello world.uri", (str, float), True, "hello world.uri"),
            ("hello world.uri", (str, float), False, "hello world.uri"),
        ],
    )
    def test__valid_isinstance_or_raise(self, value, dtype, none_allowed, expected):
        result = _isinstance_or_raise(value, dtype, none_allowed=none_allowed)
        assert result == expected

    @pytest.mark.parametrize(
        "value,dtype,none_allowed,expected",
        [
            (None, str, False, pytest.raises(TypeError)),
            ({"key": "value"}, str, True, pytest.raises(TypeError)),
            ({"key": "value"}, str, False, pytest.raises(TypeError)),
            ({"key": "value"}, (str, float), True, pytest.raises(TypeError)),
            ({"key": "value"}, (str, float), False, pytest.raises(TypeError)),
        ],
    )
    def test__invalid_isinstance_or_raise(self, value, dtype, none_allowed, expected):
        with expected:
            _isinstance_or_raise(value, dtype, none_allowed=none_allowed)
