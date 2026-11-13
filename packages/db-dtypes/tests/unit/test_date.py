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
import operator

import numpy
import numpy.testing
import pandas
import pandas.testing
import pytest
from pandas.errors import OutOfBoundsDatetime

import db_dtypes
from db_dtypes import pandas_backports

VALUE_PARSING_TEST_CASES = [
    # Min/Max values for pandas.Timestamp.
    ("1677-09-22", datetime.date(1677, 9, 22)),
    ("2262-04-11", datetime.date(2262, 4, 11)),
    # Typical "zero" values.
    ("1900-01-01", datetime.date(1900, 1, 1)),
    ("1970-01-01", datetime.date(1970, 1, 1)),
    # Assorted values.
    ("1993-10-31", datetime.date(1993, 10, 31)),
    (datetime.date(1993, 10, 31), datetime.date(1993, 10, 31)),
    ("2012-02-29", datetime.date(2012, 2, 29)),
    (numpy.datetime64("2012-02-29"), datetime.date(2012, 2, 29)),
    ("2021-12-17", datetime.date(2021, 12, 17)),
    (pandas.Timestamp("2021-12-17"), datetime.date(2021, 12, 17)),
    ("2038-01-19", datetime.date(2038, 1, 19)),
]

NULL_VALUE_TEST_CASES = [
    None,
    pandas.NaT,
    float("nan"),
]


def test_box_func():
    input_array = db_dtypes.DateArray([])
    input_datetime = datetime.datetime(2022, 3, 16)
    input_np = numpy.datetime64(input_datetime)

    boxed_value = input_array._box_func(input_np)
    assert boxed_value.year == 2022
    assert boxed_value.month == 3
    assert boxed_value.day == 16

    input_delta = input_datetime - datetime.datetime(1970, 1, 1)
    input_nanoseconds = (
        1_000 * input_delta.microseconds
        + 1_000_000_000 * input_delta.seconds
        + 1_000_000_000 * 60 * 60 * 24 * input_delta.days
    )

    boxed_value = input_array._box_func(input_nanoseconds)
    assert boxed_value.year == 2022
    assert boxed_value.month == 3
    assert boxed_value.day == 16


def test_construct_from_string_with_nonstring():
    with pytest.raises(TypeError):
        db_dtypes.DateDtype.construct_from_string(object())


def test__cmp_method_with_scalar():
    input_array = db_dtypes.DateArray([datetime.date(1900, 1, 1)])
    got = input_array._cmp_method(datetime.date(1900, 1, 1), operator.eq)
    assert got[0]


@pytest.mark.parametrize("value, expected", VALUE_PARSING_TEST_CASES)
def test_date_parsing(value, expected):
    assert pandas.Series([value], dtype="dbdate")[0] == expected


@pytest.mark.parametrize("value", NULL_VALUE_TEST_CASES)
def test_date_parsing_null(value):
    assert pandas.Series([value], dtype="dbdate")[0] is pandas.NaT


@pytest.mark.parametrize("value, expected", VALUE_PARSING_TEST_CASES)
def test_date_set_item(value, expected):
    series = pandas.Series([None], dtype="dbdate")
    series[0] = value
    assert series[0] == expected


@pytest.mark.parametrize("value", NULL_VALUE_TEST_CASES)
def test_date_set_item_null(value):
    series = pandas.Series(["1970-01-01"], dtype="dbdate")
    series[0] = value
    assert series[0] is pandas.NaT


def test_date_set_slice():
    series = pandas.Series([None, None, None], dtype="dbdate")
    series[:] = [
        datetime.date(2022, 3, 21),
        "2011-12-13",
        numpy.datetime64("1998-09-04"),
    ]
    assert series[0] == datetime.date(2022, 3, 21)
    assert series[1] == datetime.date(2011, 12, 13)
    assert series[2] == datetime.date(1998, 9, 4)


def test_date_set_slice_null():
    series = pandas.Series(["1970-01-01"] * len(NULL_VALUE_TEST_CASES), dtype="dbdate")
    series[:] = NULL_VALUE_TEST_CASES
    for row_index in range(len(NULL_VALUE_TEST_CASES)):
        assert series[row_index] is pandas.NaT


@pytest.mark.parametrize(
    "value, error",
    [
        ("thursday", "Bad date string: 'thursday'"),
        ("1-2-thursday", "Bad date string: '1-2-thursday'"),
        ("1-2-3-4", "Bad date string: '1-2-3-4'"),
        ("1-2-3.f", "Bad date string: '1-2-3.f'"),
        ("1-d-3", "Bad date string: '1-d-3'"),
        ("1-3", "Bad date string: '1-3'"),
        ("1", "Bad date string: '1'"),
        ("", "Bad date string: ''"),
        ("2021-2-99", "day is out of range for month|day .* must be in range .*"),
        ("2021-99-1", "month must be in 1[.][.]12"),
        ("10000-1-1", "year 10000 is out of range|year must be in .*"),
    ],
)
def test_date_parsing_errors(value, error):
    with pytest.raises(ValueError, match=error):
        pandas.Series([value], dtype="dbdate")


@pytest.mark.parametrize(
    "value, error",
    [
        # Values that are outside of the min/max values allowed by pandas.Timestamp
        ("0001-01-01", "Out of bounds"),
        ("9999-12-31", "Out of bounds"),
        ("1677-09-21", "Out of bounds"),
        ("2262-04-12", "Out of bounds"),
        (datetime.date(1, 1, 1), "Out of bounds"),
        (datetime.date(9999, 12, 31), "Out of bounds"),
    ],
)
def test_date_parsing_errors_out_of_bounds(value, error):
    with pytest.raises(OutOfBoundsDatetime, match=error):
        pandas.Series([value], dtype="dbdate")


def test_date_max_2d():
    input_array = db_dtypes.DateArray(
        numpy.array(
            [
                [
                    numpy.datetime64("1970-01-01"),
                    numpy.datetime64("1980-02-02"),
                    numpy.datetime64("1990-03-03"),
                ],
                [
                    numpy.datetime64("1971-02-02"),
                    numpy.datetime64("1981-03-03"),
                    numpy.datetime64("1991-04-04"),
                ],
                [
                    numpy.datetime64("1972-03-03"),
                    numpy.datetime64("1982-04-04"),
                    numpy.datetime64("1992-05-05"),
                ],
            ],
            dtype="datetime64[ns]",
        )
    )
    numpy.testing.assert_array_equal(
        input_array.max(axis=0)._ndarray,
        numpy.array(
            [
                numpy.datetime64("1972-03-03"),
                numpy.datetime64("1982-04-04"),
                numpy.datetime64("1992-05-05"),
            ],
            dtype="datetime64[ns]",
        ),
    )
    numpy.testing.assert_array_equal(
        input_array.max(axis=1)._ndarray,
        numpy.array(
            [
                numpy.datetime64("1990-03-03"),
                numpy.datetime64("1991-04-04"),
                numpy.datetime64("1992-05-05"),
            ],
            dtype="datetime64[ns]",
        ),
    )


def test_date_min_2d():
    input_array = db_dtypes.DateArray(
        numpy.array(
            [
                [
                    numpy.datetime64("1970-01-01"),
                    numpy.datetime64("1980-02-02"),
                    numpy.datetime64("1990-03-03"),
                ],
                [
                    numpy.datetime64("1971-02-02"),
                    numpy.datetime64("1981-03-03"),
                    numpy.datetime64("1991-04-04"),
                ],
                [
                    numpy.datetime64("1972-03-03"),
                    numpy.datetime64("1982-04-04"),
                    numpy.datetime64("1992-05-05"),
                ],
            ],
            dtype="datetime64[ns]",
        )
    )
    numpy.testing.assert_array_equal(
        input_array.min(axis=0)._ndarray,
        numpy.array(
            [
                numpy.datetime64("1970-01-01"),
                numpy.datetime64("1980-02-02"),
                numpy.datetime64("1990-03-03"),
            ],
            dtype="datetime64[ns]",
        ),
    )
    numpy.testing.assert_array_equal(
        input_array.min(axis=1)._ndarray,
        numpy.array(
            [
                numpy.datetime64("1970-01-01"),
                numpy.datetime64("1971-02-02"),
                numpy.datetime64("1972-03-03"),
            ],
            dtype="datetime64[ns]",
        ),
    )


@pytest.mark.skipif(
    not hasattr(pandas_backports, "numpy_validate_median"),
    reason="median not available with this version of pandas",
)
@pytest.mark.parametrize(
    "values, expected",
    [
        (["1970-01-01", "1900-01-01", "2000-01-01"], datetime.date(1970, 1, 1)),
        (
            [
                None,
                "1900-01-01",
                pandas.NA if hasattr(pandas, "NA") else None,
                pandas.NaT,
                float("nan"),
            ],
            datetime.date(1900, 1, 1),
        ),
        (["2222-02-01", "2222-02-03"], datetime.date(2222, 2, 2)),
    ],
)
def test_date_median(values, expected):
    series = pandas.Series(values, dtype="dbdate")
    assert series.median() == expected


@pytest.mark.skipif(
    not hasattr(pandas_backports, "numpy_validate_median"),
    reason="median not available with this version of pandas",
)
def test_date_median_2d():
    input_array = db_dtypes.DateArray(
        numpy.array(
            [
                [
                    numpy.datetime64("1970-01-01"),
                    numpy.datetime64("1980-02-02"),
                    numpy.datetime64("1990-03-03"),
                ],
                [
                    numpy.datetime64("1971-02-02"),
                    numpy.datetime64("1981-03-03"),
                    numpy.datetime64("1991-04-04"),
                ],
                [
                    numpy.datetime64("1972-03-03"),
                    numpy.datetime64("1982-04-04"),
                    numpy.datetime64("1992-05-05"),
                ],
            ],
            dtype="datetime64[ns]",
        )
    )
    pandas.testing.assert_extension_array_equal(
        input_array.median(axis=0),
        db_dtypes.DateArray(
            numpy.array(
                [
                    numpy.datetime64("1971-02-02"),
                    numpy.datetime64("1981-03-03"),
                    numpy.datetime64("1991-04-04"),
                ],
                dtype="datetime64[ns]",
            )
        ),
    )
    pandas.testing.assert_extension_array_equal(
        input_array.median(axis=1),
        db_dtypes.DateArray(
            numpy.array(
                [
                    numpy.datetime64("1980-02-02"),
                    numpy.datetime64("1981-03-03"),
                    numpy.datetime64("1982-04-04"),
                ],
                dtype="datetime64[ns]",
            )
        ),
    )


@pytest.mark.parametrize(
    ("search_term", "expected_index"),
    (
        (datetime.date(1899, 12, 31), 0),
        (datetime.date(1900, 1, 1), 0),
        (datetime.date(1920, 2, 2), 1),
        (datetime.date(1930, 3, 3), 1),
        (datetime.date(1950, 5, 5), 2),
        (datetime.date(1990, 9, 9), 3),
        (datetime.date(2012, 12, 12), 3),
        (datetime.date(2022, 3, 24), 4),
    ),
)
def test_date_searchsorted(search_term, expected_index):
    test_series = pandas.Series(
        [
            datetime.date(1900, 1, 1),
            datetime.date(1930, 3, 3),
            datetime.date(1980, 8, 8),
            datetime.date(2012, 12, 12),
        ],
        dtype="dbdate",
    )
    got = test_series.searchsorted(search_term)
    assert got == expected_index
