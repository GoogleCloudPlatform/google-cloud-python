# Copyright 2025 Google LLC
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

import base64
import datetime
import decimal
import json

from dateutil.relativedelta import relativedelta
import pytest

import google.cloud.bigquery.schema


def create_field(mode="NULLABLE", type_="IGNORED", name="test_field", **kwargs):
    return google.cloud.bigquery.schema.SchemaField(name, type_, mode=mode, **kwargs)


@pytest.fixture
def mut():
    from google.cloud.bigquery import _helpers

    return _helpers


@pytest.fixture
def object_under_test(mut):
    return mut.CELL_DATA_PARSER


ALL_TYPES = {
    "BOOL",
    "BOOLEAN",
    "BYTES",
    "INTEGER",
    "INT64",
    "INTERVAL",
    "FLOAT",
    "FLOAT64",
    "NUMERIC",
    "BIGNUMERIC",
    "STRING",
    "GEOGRAPHY",
    "TIMESTAMP",
    "DATETIME",
    "DATE",
    "TIME",
    "RECORD",
    "STRUCT",
    "JSON",
    "RANGE",
}

TYPES_WITH_CLIENT_SIDE_NULL_VALIDATION = ALL_TYPES - {
    "STRING",
    "GEOGRAPHY",
}


@pytest.mark.parametrize(
    "type_",
    list(sorted(ALL_TYPES)),
)
def test_to_py_w_none_nullable(object_under_test, type_):
    assert object_under_test.to_py(None, create_field("NULLABLE", type_)) is None


@pytest.mark.parametrize("type_", list(sorted(TYPES_WITH_CLIENT_SIDE_NULL_VALIDATION)))
def test_to_py_w_none_required(object_under_test, type_):
    with pytest.raises(TypeError):
        object_under_test.to_py(None, create_field("REQUIRED", type_))


def test_interval_to_py_w_invalid_format(object_under_test):
    with pytest.raises(ValueError, match="NOT_AN_INTERVAL"):
        object_under_test.interval_to_py("NOT_AN_INTERVAL", create_field())


@pytest.mark.parametrize(
    ("value", "expected"),
    (
        ("0-0 0 0:0:0", relativedelta()),
        # SELECT INTERVAL X YEAR
        ("-10000-0 0 0:0:0", relativedelta(years=-10000)),
        ("-1-0 0 0:0:0", relativedelta(years=-1)),
        ("1-0 0 0:0:0", relativedelta(years=1)),
        ("10000-0 0 0:0:0", relativedelta(years=10000)),
        # SELECT INTERVAL X MONTH
        ("-0-11 0 0:0:0", relativedelta(months=-11)),
        ("-0-1 0 0:0:0", relativedelta(months=-1)),
        ("0-1 0 0:0:0", relativedelta(months=1)),
        ("0-11 0 0:0:0", relativedelta(months=11)),
        # SELECT INTERVAL X DAY
        ("0-0 -3660000 0:0:0", relativedelta(days=-3660000)),
        ("0-0 -1 0:0:0", relativedelta(days=-1)),
        ("0-0 1 0:0:0", relativedelta(days=1)),
        ("0-0 3660000 0:0:0", relativedelta(days=3660000)),
        # SELECT INTERVAL X HOUR
        ("0-0 0 -87840000:0:0", relativedelta(hours=-87840000)),
        ("0-0 0 -1:0:0", relativedelta(hours=-1)),
        ("0-0 0 1:0:0", relativedelta(hours=1)),
        ("0-0 0 87840000:0:0", relativedelta(hours=87840000)),
        # SELECT INTERVAL X MINUTE
        ("0-0 0 -0:59:0", relativedelta(minutes=-59)),
        ("0-0 0 -0:1:0", relativedelta(minutes=-1)),
        ("0-0 0 0:1:0", relativedelta(minutes=1)),
        ("0-0 0 0:59:0", relativedelta(minutes=59)),
        # SELECT INTERVAL X SECOND
        ("0-0 0 -0:0:59", relativedelta(seconds=-59)),
        ("0-0 0 -0:0:1", relativedelta(seconds=-1)),
        ("0-0 0 0:0:1", relativedelta(seconds=1)),
        ("0-0 0 0:0:59", relativedelta(seconds=59)),
        # SELECT (INTERVAL -1 SECOND) / 1000000
        ("0-0 0 -0:0:0.000001", relativedelta(microseconds=-1)),
        ("0-0 0 -0:0:59.999999", relativedelta(seconds=-59, microseconds=-999999)),
        ("0-0 0 -0:0:59.999", relativedelta(seconds=-59, microseconds=-999000)),
        ("0-0 0 0:0:59.999", relativedelta(seconds=59, microseconds=999000)),
        ("0-0 0 0:0:59.999999", relativedelta(seconds=59, microseconds=999999)),
        # Test with multiple digits in each section.
        (
            "32-11 45 67:16:23.987654",
            relativedelta(
                years=32,
                months=11,
                days=45,
                hours=67,
                minutes=16,
                seconds=23,
                microseconds=987654,
            ),
        ),
        (
            "-32-11 -45 -67:16:23.987654",
            relativedelta(
                years=-32,
                months=-11,
                days=-45,
                hours=-67,
                minutes=-16,
                seconds=-23,
                microseconds=-987654,
            ),
        ),
        # Test with mixed +/- sections.
        (
            "9999-9 -999999 9999999:59:59.999999",
            relativedelta(
                years=9999,
                months=9,
                days=-999999,
                hours=9999999,
                minutes=59,
                seconds=59,
                microseconds=999999,
            ),
        ),
        # Test with fraction that is not microseconds.
        ("0-0 0 0:0:42.", relativedelta(seconds=42)),
        ("0-0 0 0:0:59.1", relativedelta(seconds=59, microseconds=100000)),
        ("0-0 0 0:0:0.12", relativedelta(microseconds=120000)),
        ("0-0 0 0:0:0.123", relativedelta(microseconds=123000)),
        ("0-0 0 0:0:0.1234", relativedelta(microseconds=123400)),
        # Fractional seconds can cause rounding problems if cast to float. See:
        # https://github.com/googleapis/python-db-dtypes-pandas/issues/18
        ("0-0 0 0:0:59.876543", relativedelta(seconds=59, microseconds=876543)),
        (
            "0-0 0 01:01:01.010101",
            relativedelta(hours=1, minutes=1, seconds=1, microseconds=10101),
        ),
        (
            "0-0 0 09:09:09.090909",
            relativedelta(hours=9, minutes=9, seconds=9, microseconds=90909),
        ),
        (
            "0-0 0 11:11:11.111111",
            relativedelta(hours=11, minutes=11, seconds=11, microseconds=111111),
        ),
        (
            "0-0 0 19:16:23.987654",
            relativedelta(hours=19, minutes=16, seconds=23, microseconds=987654),
        ),
        # Nanoseconds are not expected, but should not cause error.
        ("0-0 0 0:0:00.123456789", relativedelta(microseconds=123456)),
        ("0-0 0 0:0:59.87654321", relativedelta(seconds=59, microseconds=876543)),
    ),
)
def test_interval_to_py_w_string_values(object_under_test, value, expected):
    got = object_under_test.interval_to_py(value, create_field())
    assert got == expected


def test_integer_to_py_w_string_value(object_under_test):
    coerced = object_under_test.integer_to_py("42", object())
    assert coerced == 42


def test_integer_to_py_w_float_value(object_under_test):
    coerced = object_under_test.integer_to_py(42.0, object())
    assert coerced == 42


def test_json_to_py_w_json_field(object_under_test):
    data_field = create_field("REQUIRED", "data", "JSON")

    value = json.dumps(
        {"v": {"key": "value"}},
    )

    expected_output = {"v": {"key": "value"}}
    coerced_output = object_under_test.json_to_py(value, data_field)
    assert coerced_output == expected_output


def test_json_to_py_w_string_value(object_under_test):
    coerced = object_under_test.json_to_py('"foo"', create_field())
    assert coerced == "foo"


def test_float_to_py_w_string_value(object_under_test):
    coerced = object_under_test.float_to_py("3.1415", object())
    assert coerced == 3.1415


def test_float_to_py_w_float_value(object_under_test):
    coerced = object_under_test.float_to_py(3.1415, object())
    assert coerced == 3.1415


def test_numeric_to_py_w_string_value(object_under_test):
    coerced = object_under_test.numeric_to_py("3.1415", object())
    assert coerced == decimal.Decimal("3.1415")


def test_numeric_to_py_w_float_value(object_under_test):
    coerced = object_under_test.numeric_to_py(3.1415, object())
    # There is no exact float representation of 3.1415.
    assert coerced == decimal.Decimal(3.1415)


def test_bool_to_py_w_value_t(object_under_test):
    coerced = object_under_test.bool_to_py("T", object())
    assert coerced is True


def test_bool_to_py_w_value_true(object_under_test):
    coerced = object_under_test.bool_to_py("True", object())
    assert coerced is True


def test_bool_to_py_w_value_1(object_under_test):
    coerced = object_under_test.bool_to_py("1", object())
    assert coerced is True


def test_bool_to_py_w_value_other(object_under_test):
    coerced = object_under_test.bool_to_py("f", object())
    assert coerced is False


def test_string_to_py_w_string_value(object_under_test):
    coerced = object_under_test.string_to_py("Wonderful!", object())
    assert coerced == "Wonderful!"


def test_bytes_to_py_w_base64_encoded_bytes(object_under_test):
    expected = b"Wonderful!"
    encoded = base64.standard_b64encode(expected)
    coerced = object_under_test.bytes_to_py(encoded, object())
    assert coerced == expected


def test_bytes_to_py_w_base64_encoded_text(object_under_test):
    expected = b"Wonderful!"
    encoded = base64.standard_b64encode(expected).decode("ascii")
    coerced = object_under_test.bytes_to_py(encoded, object())
    assert coerced == expected


def test_timestamp_to_py_w_string_int_value(object_under_test):
    from google.cloud._helpers import _EPOCH

    coerced = object_under_test.timestamp_to_py("1234567", create_field())
    assert coerced == _EPOCH + datetime.timedelta(seconds=1, microseconds=234567)


def test_timestamp_to_py_w_int_value(object_under_test):
    from google.cloud._helpers import _EPOCH

    coerced = object_under_test.timestamp_to_py(1234567, create_field())
    assert coerced == _EPOCH + datetime.timedelta(seconds=1, microseconds=234567)


def test_timestamp_to_py_w_picosecond_precision(object_under_test):
    from google.cloud.bigquery import enums

    pico_schema = create_field(timestamp_precision=enums.TimestampPrecision.PICOSECOND)
    pico_timestamp = "2025-01-01T00:00:00.123456789012Z"
    coerced = object_under_test.timestamp_to_py(pico_timestamp, pico_schema)
    assert coerced == pico_timestamp


def test_datetime_to_py_w_string_value(object_under_test):
    coerced = object_under_test.datetime_to_py("2016-12-02T18:51:33", object())
    assert coerced == datetime.datetime(2016, 12, 2, 18, 51, 33)


def test_datetime_to_py_w_microseconds(object_under_test):
    coerced = object_under_test.datetime_to_py("2015-05-22T10:11:12.987654", object())
    assert coerced == datetime.datetime(2015, 5, 22, 10, 11, 12, 987654)


def test_date_to_py_w_string_value(object_under_test):
    coerced = object_under_test.date_to_py("1987-09-22", object())
    assert coerced == datetime.date(1987, 9, 22)


def test_time_to_py_w_string_value(object_under_test):
    coerced = object_under_test.time_to_py("12:12:27", object())
    assert coerced == datetime.time(12, 12, 27)


def test_time_to_py_w_subsecond_string_value(object_under_test):
    coerced = object_under_test.time_to_py("12:12:27.123456", object())
    assert coerced == datetime.time(12, 12, 27, 123456)


def test_time_to_py_w_bogus_string_value(object_under_test):
    with pytest.raises(ValueError):
        object_under_test.time_to_py("12:12:27.123", object())


def test_range_to_py_w_wrong_format(object_under_test):
    range_field = create_field(
        "NULLABLE",
        "RANGE",
        range_element_type="DATE",
    )
    with pytest.raises(ValueError):
        object_under_test.range_to_py("[2009-06-172019-06-17)", range_field)


def test_range_to_py_w_wrong_element_type(object_under_test):
    range_field = create_field(
        "NULLABLE",
        "RANGE",
        range_element_type=google.cloud.bigquery.schema.FieldElementType(
            element_type="TIME"
        ),
    )
    with pytest.raises(ValueError):
        object_under_test.range_to_py("[15:31:38, 15:50:38)", range_field)


def test_range_to_py_w_unbounded_value(object_under_test):
    range_field = create_field(
        "NULLABLE",
        "RANGE",
        range_element_type="DATE",
    )
    coerced = object_under_test.range_to_py("[UNBOUNDED, 2019-06-17)", range_field)
    assert coerced == {"start": None, "end": datetime.date(2019, 6, 17)}


def test_range_to_py_w_date_value(object_under_test):
    range_field = create_field(
        "NULLABLE",
        "RANGE",
        range_element_type="DATE",
    )
    coerced = object_under_test.range_to_py("[2009-06-17, 2019-06-17)", range_field)
    assert coerced == {
        "start": datetime.date(2009, 6, 17),
        "end": datetime.date(2019, 6, 17),
    }


def test_range_to_py_w_datetime_value(object_under_test):
    range_field = create_field(
        "NULLABLE",
        "RANGE",
        range_element_type=google.cloud.bigquery.schema.FieldElementType(
            element_type="DATETIME"
        ),
    )
    coerced = object_under_test.range_to_py(
        "[2009-06-17T13:45:30, 2019-06-17T13:45:30)", range_field
    )
    assert coerced == {
        "start": datetime.datetime(2009, 6, 17, 13, 45, 30),
        "end": datetime.datetime(2019, 6, 17, 13, 45, 30),
    }


def test_range_to_py_w_timestamp_value(object_under_test):
    from google.cloud._helpers import _EPOCH

    range_field = create_field(
        "NULLABLE",
        "RANGE",
        range_element_type=google.cloud.bigquery.schema.FieldElementType(
            element_type="TIMESTAMP"
        ),
    )
    coerced = object_under_test.range_to_py("[1234567, 1234789)", range_field)
    assert coerced == {
        "start": _EPOCH + datetime.timedelta(seconds=1, microseconds=234567),
        "end": _EPOCH + datetime.timedelta(seconds=1, microseconds=234789),
    }


def test_record_to_py_w_nullable_subfield_none(object_under_test):
    subfield = create_field("NULLABLE", "INTEGER", name="age")
    field = create_field("REQUIRED", fields=[subfield])
    value = {"f": [{"v": None}]}
    coerced = object_under_test.record_to_py(value, field)
    assert coerced == {"age": None}


def test_record_to_py_w_scalar_subfield(object_under_test):
    subfield = create_field("REQUIRED", "INTEGER", name="age")
    field = create_field("REQUIRED", fields=[subfield])
    value = {"f": [{"v": 42}]}
    coerced = object_under_test.record_to_py(value, field)
    assert coerced == {"age": 42}


def test_record_to_py_w_scalar_subfield_geography(object_under_test):
    subfield = create_field("REQUIRED", "GEOGRAPHY", name="geo")
    field = create_field("REQUIRED", fields=[subfield])
    value = {"f": [{"v": "POINT(1, 2)"}]}
    coerced = object_under_test.record_to_py(value, field)
    assert coerced == {"geo": "POINT(1, 2)"}


def test_record_to_py_w_repeated_subfield(object_under_test):
    subfield = create_field("REPEATED", "STRING", name="color")
    field = create_field("REQUIRED", fields=[subfield])
    value = {"f": [{"v": [{"v": "red"}, {"v": "yellow"}, {"v": "blue"}]}]}
    coerced = object_under_test.record_to_py(value, field)
    assert coerced == {"color": ["red", "yellow", "blue"]}


def test_record_to_py_w_record_subfield(object_under_test):
    full_name = create_field("REQUIRED", "STRING", name="full_name")
    area_code = create_field("REQUIRED", "STRING", name="area_code")
    local_number = create_field("REQUIRED", "STRING", name="local_number")
    rank = create_field("REQUIRED", "INTEGER", name="rank")
    phone = create_field(
        "NULLABLE", "RECORD", name="phone", fields=[area_code, local_number, rank]
    )
    person = create_field(
        "REQUIRED", "RECORD", name="person", fields=[full_name, phone]
    )
    value = {
        "f": [
            {"v": "Phred Phlyntstone"},
            {"v": {"f": [{"v": "800"}, {"v": "555-1212"}, {"v": 1}]}},
        ]
    }
    expected = {
        "full_name": "Phred Phlyntstone",
        "phone": {"area_code": "800", "local_number": "555-1212", "rank": 1},
    }
    coerced = object_under_test.record_to_py(value, person)
    assert coerced == expected
