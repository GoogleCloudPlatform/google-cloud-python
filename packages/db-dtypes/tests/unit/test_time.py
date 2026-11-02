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

import datetime

import numpy
import pandas
import pytest

# To register the types.
import db_dtypes  # noqa
from db_dtypes import pandas_backports


def test_box_func():
    input_array = db_dtypes.TimeArray([])
    input_datetime = datetime.datetime(1970, 1, 1, 1, 2, 3, 456789)
    input_np = numpy.datetime64(input_datetime)

    boxed_value = input_array._box_func(input_np)
    assert boxed_value.hour == 1
    assert boxed_value.minute == 2
    assert boxed_value.second == 3
    assert boxed_value.microsecond == 456789

    input_delta = input_datetime - datetime.datetime(1970, 1, 1)
    input_nanoseconds = (
        1_000 * input_delta.microseconds
        + 1_000_000_000 * input_delta.seconds
        + 1_000_000_000 * 60 * 60 * 24 * input_delta.days
    )

    boxed_value = input_array._box_func(input_nanoseconds)
    assert boxed_value.hour == 1
    assert boxed_value.minute == 2
    assert boxed_value.second == 3
    assert boxed_value.microsecond == 456789


@pytest.mark.parametrize(
    "value, expected",
    [
        # Midnight
        ("0", datetime.time(0)),
        ("0:0", datetime.time(0)),
        ("0:0:0", datetime.time(0)),
        ("0:0:0.", datetime.time(0)),
        ("0:0:0.0", datetime.time(0)),
        ("0:0:0.000000", datetime.time(0)),
        ("00:00:00", datetime.time(0, 0, 0)),
        ("  00:00:00  ", datetime.time(0, 0, 0)),
        # Short values
        ("1", datetime.time(1)),
        ("23", datetime.time(23)),
        ("1:2", datetime.time(1, 2)),
        ("23:59", datetime.time(23, 59)),
        ("1:2:3", datetime.time(1, 2, 3)),
        ("23:59:59", datetime.time(23, 59, 59)),
        # Non-octal values.
        ("08:08:08", datetime.time(8, 8, 8)),
        ("09:09:09", datetime.time(9, 9, 9)),
        # Fractional seconds can cause rounding problems if cast to float. See:
        # https://github.com/googleapis/python-db-dtypes-pandas/issues/18
        ("0:0:59.876543", datetime.time(0, 0, 59, 876543)),
        (
            numpy.datetime64("1970-01-01 00:00:59.876543"),
            datetime.time(0, 0, 59, 876543),
        ),
        ("01:01:01.010101", datetime.time(1, 1, 1, 10101)),
        (pandas.Timestamp("1970-01-01 01:01:01.010101"), datetime.time(1, 1, 1, 10101)),
        ("09:09:09.090909", datetime.time(9, 9, 9, 90909)),
        (datetime.time(9, 9, 9, 90909), datetime.time(9, 9, 9, 90909)),
        ("11:11:11.111111", datetime.time(11, 11, 11, 111111)),
        ("19:16:23.987654", datetime.time(19, 16, 23, 987654)),
        # Microsecond precision
        ("00:00:00.000001", datetime.time(0, 0, 0, 1)),
        ("23:59:59.999999", datetime.time(23, 59, 59, 999_999)),
        # TODO: Support nanosecond precision values without truncation.
        # https://github.com/googleapis/python-db-dtypes-pandas/issues/19
        ("0:0:0.000001001", datetime.time(0, 0, 0, 1)),
        ("23:59:59.999999000", datetime.time(23, 59, 59, 999_999)),
        ("23:59:59.999999999", datetime.time(23, 59, 59, 999_999)),
    ],
)
def test_time_parsing(value, expected):
    assert pandas.Series([value], dtype="dbtime")[0] == expected


@pytest.mark.parametrize(
    "value, error",
    [
        ("thursday", "Bad time string: 'thursday'"),
        ("1:2:3thursday", "Bad time string: '1:2:3thursday'"),
        ("1:2:3:4", "Bad time string: '1:2:3:4'"),
        ("1:2:3.f", "Bad time string: '1:2:3.f'"),
        ("1:d:3", "Bad time string: '1:d:3'"),
        ("1:2.3", "Bad time string: '1:2.3'"),
        ("", "Bad time string: ''"),
        ("1:2:99", "second must be in 0[.][.]59"),
        ("1:99", "minute must be in 0[.][.]59"),
        ("99", "hour must be in 0[.][.]23"),
    ],
)
def test_time_parsing_errors(value, error):
    with pytest.raises(ValueError, match=error):
        pandas.Series([value], dtype="dbtime")


@pytest.mark.skipif(
    not hasattr(pandas_backports, "numpy_validate_median"),
    reason="median not available with this version of pandas",
)
@pytest.mark.parametrize(
    "values, expected",
    [
        (
            ["00:00:00", "12:34:56.789101", "23:59:59.999999"],
            datetime.time(12, 34, 56, 789101),
        ),
        (
            [
                None,
                "06:30:00",
                pandas.NA if hasattr(pandas, "NA") else None,
                pandas.NaT,
                float("nan"),
            ],
            datetime.time(6, 30),
        ),
        (["2:22:21.222222", "2:22:23.222222"], datetime.time(2, 22, 22, 222222)),
    ],
)
def test_date_median(values, expected):
    series = pandas.Series(values, dtype="dbtime")
    assert series.median() == expected
