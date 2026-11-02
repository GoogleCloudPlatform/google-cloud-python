# Copyright 2021 Google LLC All rights reserved.
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

import collections
import datetime
import decimal
import math

from google.api_core import datetime_helpers
from google.cloud._helpers import UTC

from google.cloud import spanner_v1
from google.cloud.spanner_v1.data_types import JsonObject

from .testdata import singer_pb2

TABLE = "contacts"
COLUMNS = ("contact_id", "first_name", "last_name", "email")
ROW_DATA = (
    (1, "Phred", "Phlyntstone", "phred@example.com"),
    (2, "Bharney", "Rhubble", "bharney@example.com"),
    (3, "Wylma", "Phlyntstone", "wylma@example.com"),
)
BATCH_WRITE_ROW_DATA = (
    (1, "Phred", "Phlyntstone", "phred@example.com"),
    (2, "Bharney", "Rhubble", "bharney@example.com"),
    (3, "Wylma", "Phlyntstone", "wylma@example.com"),
    (4, "Pebbles", "Phlyntstone", "pebbles@example.com"),
    (5, "Betty", "Rhubble", "betty@example.com"),
    (6, "Slate", "Stephenson", "slate@example.com"),
)
ALL = spanner_v1.KeySet(all_=True)
SQL = "SELECT * FROM contacts ORDER BY contact_id"

COUNTERS_TABLE = "counters"
COUNTERS_COLUMNS = ("name", "value")

SINGERS_PROTO_TABLE = "singers"
SINGERS_PROTO_COLUMNS = (
    "singer_id",
    "first_name",
    "last_name",
    "singer_info",
    "singer_genre",
)
SINGER_INFO_1 = singer_pb2.SingerInfo()
SINGER_GENRE_1 = singer_pb2.Genre.ROCK
SINGER_INFO_1.singer_id = 1
SINGER_INFO_1.birth_date = "January"
SINGER_INFO_1.nationality = "Country1"
SINGER_INFO_1.genre = SINGER_GENRE_1
SINGER_INFO_2 = singer_pb2.SingerInfo()
SINGER_GENRE_2 = singer_pb2.Genre.FOLK
SINGER_INFO_2.singer_id = 2
SINGER_INFO_2.birth_date = "February"
SINGER_INFO_2.nationality = "Country2"
SINGER_INFO_2.genre = SINGER_GENRE_2
SINGERS_PROTO_ROW_DATA = (
    (1, "Singer1", "Singer1", SINGER_INFO_1, SINGER_GENRE_1),
    (2, "Singer2", "Singer2", SINGER_INFO_2, SINGER_GENRE_2),
)


def _assert_timestamp(value, nano_value):
    assert isinstance(value, datetime.datetime)
    assert value.tzinfo is None
    assert nano_value.tzinfo is UTC

    assert value.year == nano_value.year
    assert value.month == nano_value.month
    assert value.day == nano_value.day
    assert value.hour == nano_value.hour
    assert value.minute == nano_value.minute
    assert value.second == nano_value.second
    assert value.microsecond == nano_value.microsecond

    if isinstance(value, datetime_helpers.DatetimeWithNanoseconds):
        assert value.nanosecond == nano_value.nanosecond
    else:
        assert value.microsecond * 1000 == nano_value.nanosecond


def _check_rows_data(rows_data, expected=ROW_DATA, recurse_into_lists=True):
    assert len(rows_data) == len(expected)

    for row, expected in zip(rows_data, expected):
        _check_row_data(row, expected, recurse_into_lists=recurse_into_lists)


def _check_row_data(row_data, expected, recurse_into_lists=True):
    assert len(row_data) == len(expected)

    for found_cell, expected_cell in zip(row_data, expected):
        _check_cell_data(
            found_cell, expected_cell, recurse_into_lists=recurse_into_lists
        )


def _check_cell_data(found_cell, expected_cell, recurse_into_lists=True):
    if isinstance(found_cell, datetime_helpers.DatetimeWithNanoseconds):
        _assert_timestamp(expected_cell, found_cell)

    elif isinstance(found_cell, float) and math.isnan(found_cell):
        assert math.isnan(expected_cell)

    elif isinstance(found_cell, list) and recurse_into_lists:
        assert len(found_cell) == len(expected_cell)

        for found_item, expected_item in zip(found_cell, expected_cell):
            _check_cell_data(found_item, expected_item)

    elif isinstance(found_cell, float) and not math.isinf(found_cell):
        assert abs(found_cell - expected_cell) < 0.00001

    else:
        assert found_cell == expected_cell


SOME_DATE = datetime.date(2011, 1, 17)
SOME_TIME = datetime.datetime(1989, 1, 17, 17, 59, 12, 345612)
NANO_TIME = datetime_helpers.DatetimeWithNanoseconds(1995, 8, 31, nanosecond=987654321)
BYTES_1 = b"Ymlu"
BYTES_2 = b"Ym9vdHM="
NUMERIC_1 = decimal.Decimal("0.123456789")
NUMERIC_2 = decimal.Decimal("1234567890")
JSON_1 = JsonObject(
    {
        "sample_boolean": True,
        "sample_int": 872163,
        "sample float": 7871.298,
        "sample_null": None,
        "sample_string": "abcdef",
        "sample_array": [23, 76, 19],
    }
)
JSON_2 = JsonObject(
    {"sample_object": {"name": "Anamika", "id": 2635}},
)

ALL_TYPES_TABLE = "all_types"
ALL_TYPES_COLUMNS = (
    "pkey",
    "int_value",
    "int_array",
    "bool_value",
    "bool_array",
    "bytes_value",
    "bytes_array",
    "date_value",
    "date_array",
    "float_value",
    "float_array",
    "string_value",
    "string_array",
    "timestamp_value",
    "timestamp_array",
)

AllTypesRowData = collections.namedtuple("AllTypesRowData", ALL_TYPES_COLUMNS)
AllTypesRowData.__new__.__defaults__ = tuple([None for colum in ALL_TYPES_COLUMNS])

EMULATOR_ALL_TYPES_ROWDATA = (
    # all nulls
    AllTypesRowData(pkey=0),
    # Non-null values
    AllTypesRowData(pkey=101, int_value=123),
    AllTypesRowData(pkey=102, bool_value=False),
    AllTypesRowData(pkey=103, bytes_value=BYTES_1),
    AllTypesRowData(pkey=104, date_value=SOME_DATE),
    AllTypesRowData(pkey=105, float_value=1.4142136),
    AllTypesRowData(pkey=106, string_value="VALUE"),
    AllTypesRowData(pkey=107, timestamp_value=SOME_TIME),
    AllTypesRowData(pkey=108, timestamp_value=NANO_TIME),
    # empty array values
    AllTypesRowData(pkey=201, int_array=[]),
    AllTypesRowData(pkey=202, bool_array=[]),
    AllTypesRowData(pkey=203, bytes_array=[]),
    AllTypesRowData(pkey=204, date_array=[]),
    AllTypesRowData(pkey=205, float_array=[]),
    AllTypesRowData(pkey=206, string_array=[]),
    AllTypesRowData(pkey=207, timestamp_array=[]),
    # non-empty array values, including nulls
    AllTypesRowData(pkey=301, int_array=[123, 456, None]),
    AllTypesRowData(pkey=302, bool_array=[True, False, None]),
    AllTypesRowData(pkey=303, bytes_array=[BYTES_1, BYTES_2, None]),
    AllTypesRowData(pkey=304, date_array=[SOME_DATE, None]),
    AllTypesRowData(pkey=305, float_array=[3.1415926, -2.71828, None]),
    AllTypesRowData(pkey=306, string_array=["One", "Two", None]),
    AllTypesRowData(pkey=307, timestamp_array=[SOME_TIME, NANO_TIME, None]),
)
