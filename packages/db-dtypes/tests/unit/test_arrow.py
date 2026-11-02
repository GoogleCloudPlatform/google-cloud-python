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

import datetime as dt
from typing import Optional

import pandas
import pandas.api.extensions
import pandas.testing
import pyarrow
import pytest

import db_dtypes

SECOND_NANOS = 1_000_000_000
MINUTE_NANOS = 60 * SECOND_NANOS
HOUR_NANOS = 60 * MINUTE_NANOS


def types_mapper(
    pyarrow_type: pyarrow.DataType,
) -> Optional[pandas.api.extensions.ExtensionDtype]:
    type_str = str(pyarrow_type)

    if type_str.startswith("date32") or type_str.startswith("date64"):
        return db_dtypes.DateDtype
    elif type_str.startswith("time32") or type_str.startswith("time64"):
        return db_dtypes.TimeDtype
    else:
        # Use default type mapping.
        return None


SERIES_ARRAYS_DEFAULT_TYPES = [
    (pandas.Series([], dtype="dbdate"), pyarrow.array([], type=pyarrow.date32())),
    (
        pandas.Series([None, None, None], dtype="dbdate"),
        pyarrow.array([None, None, None], type=pyarrow.date32()),
    ),
    (
        pandas.Series(
            [dt.date(2021, 9, 27), None, dt.date(2011, 9, 27)], dtype="dbdate"
        ),
        pyarrow.array(
            [dt.date(2021, 9, 27), None, dt.date(2011, 9, 27)],
            type=pyarrow.date32(),
        ),
    ),
    (
        pandas.Series(
            [dt.date(1677, 9, 22), dt.date(1970, 1, 1), dt.date(2262, 4, 11)],
            dtype="dbdate",
        ),
        pyarrow.array(
            [dt.date(1677, 9, 22), dt.date(1970, 1, 1), dt.date(2262, 4, 11)],
            type=pyarrow.date32(),
        ),
    ),
    (
        pandas.Series([], dtype="dbtime"),
        pyarrow.array([], type=pyarrow.time64("ns")),
    ),
    (
        pandas.Series([None, None, None], dtype="dbtime"),
        pyarrow.array([None, None, None], type=pyarrow.time64("ns")),
    ),
    (
        pandas.Series(
            [dt.time(0, 0, 0, 0), None, dt.time(23, 59, 59, 999_999)],
            dtype="dbtime",
        ),
        pyarrow.array(
            [dt.time(0, 0, 0, 0), None, dt.time(23, 59, 59, 999_999)],
            type=pyarrow.time64("ns"),
        ),
    ),
    (
        pandas.Series(
            [
                dt.time(0, 0, 0, 0),
                dt.time(12, 30, 15, 125_000),
                dt.time(23, 59, 59, 999_999),
            ],
            dtype="dbtime",
        ),
        pyarrow.array(
            [
                dt.time(0, 0, 0, 0),
                dt.time(12, 30, 15, 125_000),
                dt.time(23, 59, 59, 999_999),
            ],
            type=pyarrow.time64("ns"),
        ),
    ),
]
SERIES_ARRAYS_CUSTOM_ARROW_TYPES = [
    (pandas.Series([], dtype="dbdate"), pyarrow.array([], type=pyarrow.date64())),
    (
        pandas.Series([None, None, None], dtype="dbdate"),
        pyarrow.array([None, None, None], type=pyarrow.date64()),
    ),
    (
        pandas.Series(
            [dt.date(2021, 9, 27), None, dt.date(2011, 9, 27)], dtype="dbdate"
        ),
        pyarrow.array(
            [dt.date(2021, 9, 27), None, dt.date(2011, 9, 27)],
            type=pyarrow.date64(),
        ),
    ),
    (
        pandas.Series(
            [dt.date(1677, 9, 22), dt.date(1970, 1, 1), dt.date(2262, 4, 11)],
            dtype="dbdate",
        ),
        pyarrow.array(
            [dt.date(1677, 9, 22), dt.date(1970, 1, 1), dt.date(2262, 4, 11)],
            type=pyarrow.date64(),
        ),
    ),
    (
        pandas.Series([], dtype="dbtime"),
        pyarrow.array([], type=pyarrow.time32("ms")),
    ),
    (
        pandas.Series([None, None, None], dtype="dbtime"),
        pyarrow.array([None, None, None], type=pyarrow.time32("ms")),
    ),
    (
        pandas.Series(
            [dt.time(0, 0, 0, 0), None, dt.time(23, 59, 59, 999_000)],
            dtype="dbtime",
        ),
        pyarrow.array(
            [dt.time(0, 0, 0, 0), None, dt.time(23, 59, 59, 999_000)],
            type=pyarrow.time32("ms"),
        ),
    ),
    (
        pandas.Series(
            [
                dt.time(0, 0, 0, 0),
                dt.time(12, 30, 15, 125_000),
                dt.time(23, 59, 59, 999_000),
            ],
            dtype="dbtime",
        ),
        pyarrow.array(
            [
                dt.time(0, 0, 0, 0),
                dt.time(12, 30, 15, 125_000),
                dt.time(23, 59, 59, 999_000),
            ],
            type=pyarrow.time32("ms"),
        ),
    ),
    (
        pandas.Series(
            [dt.time(0, 0, 0, 0), None, dt.time(23, 59, 59, 999_999)],
            dtype="dbtime",
        ),
        pyarrow.array(
            [dt.time(0, 0, 0, 0), None, dt.time(23, 59, 59, 999_999)],
            type=pyarrow.time64("us"),
        ),
    ),
    (
        pandas.Series(
            [
                dt.time(0, 0, 0, 0),
                dt.time(12, 30, 15, 125_000),
                dt.time(23, 59, 59, 999_999),
            ],
            dtype="dbtime",
        ),
        pyarrow.array(
            [
                dt.time(0, 0, 0, 0),
                dt.time(12, 30, 15, 125_000),
                dt.time(23, 59, 59, 999_999),
            ],
            type=pyarrow.time64("us"),
        ),
    ),
    # Only microseconds are supported when reading data. See:
    # https://github.com/googleapis/python-db-dtypes-pandas/issues/19
    # Still, round-trip with pyarrow nanosecond precision scalars
    # is supported.
    pytest.param(
        pandas.Series(
            [
                pyarrow.scalar(0, pyarrow.time64("ns")),
                pyarrow.scalar(
                    12 * HOUR_NANOS
                    + 30 * MINUTE_NANOS
                    + 15 * SECOND_NANOS
                    + 123_456_789,
                    pyarrow.time64("ns"),
                ),
                pyarrow.scalar(
                    23 * HOUR_NANOS
                    + 59 * MINUTE_NANOS
                    + 59 * SECOND_NANOS
                    + 999_999_999,
                    pyarrow.time64("ns"),
                ),
            ],
            dtype="dbtime",
        ),
        pyarrow.array(
            [
                0,
                12 * HOUR_NANOS + 30 * MINUTE_NANOS + 15 * SECOND_NANOS + 123_456_789,
                23 * HOUR_NANOS + 59 * MINUTE_NANOS + 59 * SECOND_NANOS + 999_999_999,
            ],
            type=pyarrow.time64("ns"),
        ),
        id="time-nanoseconds-arrow-round-trip",
    ),
    pytest.param(
        pandas.Series(
            ["0:0:0", "12:30:15.123456789", "23:59:59.999999999"],
            dtype="dbtime",
        ),
        pyarrow.array(
            [
                0,
                12 * HOUR_NANOS + 30 * MINUTE_NANOS + 15 * SECOND_NANOS + 123_456_789,
                23 * HOUR_NANOS + 59 * MINUTE_NANOS + 59 * SECOND_NANOS + 999_999_999,
            ],
            type=pyarrow.time64("ns"),
        ),
        id="time-nanoseconds-arrow-from-string",
    ),
]


@pytest.mark.parametrize(("series", "expected"), SERIES_ARRAYS_DEFAULT_TYPES)
def test_to_arrow(series, expected):
    array = pyarrow.array(series)
    assert array.equals(expected)


@pytest.mark.parametrize(("series", "expected"), SERIES_ARRAYS_CUSTOM_ARROW_TYPES)
def test_to_arrow_w_arrow_type(series, expected):
    array = pyarrow.array(series, type=expected.type)
    assert array.equals(expected)


@pytest.mark.parametrize(
    ["expected", "pyarrow_array"],
    SERIES_ARRAYS_DEFAULT_TYPES + SERIES_ARRAYS_CUSTOM_ARROW_TYPES,
)
def test_series_from_arrow(pyarrow_array: pyarrow.Array, expected: pandas.Series):
    # Convert to RecordBatch because types_mapper argument is ignored when
    # using a pyarrow.Array. https://issues.apache.org/jira/browse/ARROW-9664
    record_batch = pyarrow.RecordBatch.from_arrays([pyarrow_array], ["test_col"])
    dataframe = record_batch.to_pandas(date_as_object=False, types_mapper=types_mapper)
    series = dataframe["test_col"]
    pandas.testing.assert_series_equal(series, expected, check_names=False)


@pytest.mark.parametrize(
    ["expected", "pyarrow_array"],
    SERIES_ARRAYS_DEFAULT_TYPES + SERIES_ARRAYS_CUSTOM_ARROW_TYPES,
)
def test_series_from_arrow_scalars(
    pyarrow_array: pyarrow.Array, expected: pandas.Series
):
    scalars = []
    for scalar in pyarrow_array:
        scalars.append(scalar)
        assert isinstance(scalar, pyarrow.Scalar)
    series = pandas.Series(scalars, dtype=expected.dtype)
    pandas.testing.assert_series_equal(series, expected)


def test_dbtime_series_from_arrow_array():
    """Test to explicitly check Array -> Series conversion."""
    array = pyarrow.array([dt.time(15, 21, 0, 123_456)], type=pyarrow.time64("us"))
    assert isinstance(array, pyarrow.Array)
    assert not isinstance(array, pyarrow.ChunkedArray)
    series = pandas.Series(db_dtypes.TimeDtype.__from_arrow__(array))
    expected = pandas.Series([dt.time(15, 21, 0, 123_456)], dtype="dbtime")
    pandas.testing.assert_series_equal(series, expected)


def test_dbtime_series_from_arrow_chunkedarray():
    """Test to explicitly check ChunkedArray -> Series conversion."""
    array1 = pyarrow.array([dt.time(15, 21, 0, 123_456)], type=pyarrow.time64("us"))
    array2 = pyarrow.array([dt.time(0, 0, 0, 0)], type=pyarrow.time64("us"))
    array = pyarrow.chunked_array([array1, array2])
    assert isinstance(array, pyarrow.ChunkedArray)
    series = pandas.Series(db_dtypes.TimeDtype.__from_arrow__(array))
    expected = pandas.Series(
        [dt.time(15, 21, 0, 123_456), dt.time(0, 0, 0, 0)], dtype="dbtime"
    )
    pandas.testing.assert_series_equal(series, expected)


def test_dataframe_from_arrow():
    record_batch = pyarrow.RecordBatch.from_arrays(
        [
            pyarrow.array(
                [dt.date(2021, 11, 4), dt.date(2038, 1, 20), None, dt.date(1970, 1, 1)],
                type=pyarrow.date32(),
            ),
            pyarrow.array(
                [
                    dt.time(10, 7, 8, 995_325),
                    dt.time(23, 59, 59, 999_999),
                    None,
                    dt.time(0, 0, 0, 0),
                ],
                type=pyarrow.time64("us"),
            ),
            pyarrow.array([1, 2, 3, 4]),
        ],
        ["date_col", "time_col", "int_col"],
    )
    dataframe = record_batch.to_pandas(date_as_object=False, types_mapper=types_mapper)
    expected = pandas.DataFrame(
        {
            "date_col": pandas.Series(
                [dt.date(2021, 11, 4), dt.date(2038, 1, 20), None, dt.date(1970, 1, 1)],
                dtype="dbdate",
            ),
            "time_col": pandas.Series(
                [
                    dt.time(10, 7, 8, 995_325),
                    dt.time(23, 59, 59, 999_999),
                    None,
                    dt.time(0, 0, 0, 0),
                ],
                dtype="dbtime",
            ),
            "int_col": [1, 2, 3, 4],
        },
        columns=["date_col", "time_col", "int_col"],
    )
    pandas.testing.assert_frame_equal(dataframe, expected)
