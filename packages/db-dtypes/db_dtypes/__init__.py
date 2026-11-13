# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Pandas Data Types for SQL systems (BigQuery, Spanner)
"""

import datetime
import re
import warnings
from typing import Optional, Union

import numpy
import pandas
import pandas.api.extensions
import pyarrow
import pyarrow.compute
from pandas.errors import OutOfBoundsDatetime

from db_dtypes import core
from db_dtypes.json import JSONArray, JSONArrowType, JSONDtype  # noqa: F401

date_dtype_name = "dbdate"
time_dtype_name = "dbtime"
_EPOCH = datetime.datetime(1970, 1, 1)
_NPEPOCH = numpy.datetime64(_EPOCH, "ns")
_NP_DTYPE = "datetime64[ns]"

# Numpy converts datetime64 scalars to datetime.datetime only if microsecond or
# smaller precision is used.
#
# TODO(https://github.com/googleapis/python-db-dtypes-pandas/issues/63): Keep
# nanosecond precision when boxing scalars.
_NP_BOX_DTYPE = "datetime64[us]"


@pandas.api.extensions.register_extension_dtype
class TimeDtype(core.BaseDatetimeDtype):
    """
    Extension dtype for time data.
    """

    name = time_dtype_name
    type = datetime.time

    @classmethod
    def construct_array_type(cls):
        return TimeArray

    @staticmethod
    def __from_arrow__(
        array: Union[pyarrow.Array, pyarrow.ChunkedArray],
    ) -> "TimeArray":
        """Convert to dbtime data from an Arrow array.

        See:
        https://pandas.pydata.org/pandas-docs/stable/development/extending.html#compatibility-with-apache-arrow
        """
        # We can't call combine_chunks on an empty array, so short-circuit the
        # rest of the function logic for this special case.
        if len(array) == 0:
            return TimeArray(numpy.array([], dtype="datetime64[ns]"))

        # We can't cast to timestamp("ns"), but time64("ns") has the same
        # memory layout: 64-bit integers representing the number of nanoseconds
        # since the datetime epoch (midnight 1970-01-01).
        array = pyarrow.compute.cast(array, pyarrow.time64("ns"))

        # ChunkedArray has no "view" method, so combine into an Array.
        if isinstance(array, pyarrow.ChunkedArray):
            array = array.combine_chunks()

        array = array.view(pyarrow.timestamp("ns"))
        np_array = array.to_numpy(zero_copy_only=False)
        return TimeArray(np_array)


class TimeArray(core.BaseDatetimeArray):
    """
    Pandas array type containing time data
    """

    # Data are stored as datetime64 values with a date of Jan 1, 1970

    dtype = TimeDtype()

    @classmethod
    def _datetime(
        cls,
        scalar,
        match_fn=re.compile(
            r"\s*(?P<hours>\d+)"
            r"(?::(?P<minutes>\d+)"
            r"(?::(?P<seconds>\d+)"
            r"(?:\.(?P<fraction>\d*))?)?)?\s*$"
        ).match,
    ) -> Optional[numpy.datetime64]:
        if isinstance(scalar, numpy.datetime64):
            return scalar

        # Convert pyarrow values to datetime.time.
        if isinstance(scalar, (pyarrow.Time32Scalar, pyarrow.Time64Scalar)):
            scalar = (
                scalar.cast(pyarrow.time64("ns"))
                .cast(pyarrow.int64())
                .cast(pyarrow.timestamp("ns"))
                .as_py()
            )

        if pandas.isna(scalar):
            return numpy.datetime64("NaT", "ns")
        if isinstance(scalar, datetime.time):
            return pandas.Timestamp(
                year=1970,
                month=1,
                day=1,
                hour=scalar.hour,
                minute=scalar.minute,
                second=scalar.second,
                microsecond=scalar.microsecond,
            ).to_datetime64()
        elif isinstance(scalar, pandas.Timestamp):
            return scalar.to_datetime64()
        elif isinstance(scalar, str):
            # iso string
            parsed = match_fn(scalar)
            if not parsed:
                raise ValueError(f"Bad time string: {repr(scalar)}")

            hour = parsed.group("hours")
            minute = parsed.group("minutes")
            second = parsed.group("seconds")
            fraction = parsed.group("fraction")
            nanosecond = int(fraction.ljust(9, "0")[:9]) if fraction else 0

            return pandas.Timestamp(
                year=1970,
                month=1,
                day=1,
                hour=int(hour),
                minute=int(minute) if minute else 0,
                second=int(second) if second else 0,
                microsecond=nanosecond // 1000,
                nanosecond=nanosecond % 1000,
            ).to_datetime64()
        else:
            raise TypeError("Invalid value type", scalar)

    def _box_func(self, x):
        if pandas.isna(x):
            return pandas.NaT

        try:
            return x.astype(_NP_BOX_DTYPE).item().time()
        except AttributeError:
            x = numpy.datetime64(
                x, "ns"
            )  # Integers are stored with nanosecond precision.
            return x.astype(_NP_BOX_DTYPE).item().time()

    __return_deltas = {"timedelta", "timedelta64", "timedelta64[ns]", "<m8", _NP_DTYPE}

    def astype(self, dtype, copy=True):
        deltas = self._ndarray - _NPEPOCH
        stype = str(dtype)
        if stype in self.__return_deltas:
            return deltas
        elif stype.startswith("timedelta64[") or stype.startswith("<m8["):
            return deltas.astype(dtype, copy=False)
        else:
            return super().astype(dtype, copy=copy)

    def __arrow_array__(self, type=None):
        """Convert to an Arrow array from dbtime data.

        See:
        https://pandas.pydata.org/pandas-docs/stable/development/extending.html#compatibility-with-apache-arrow
        """
        array = pyarrow.array(self._ndarray, type=pyarrow.timestamp("ns"))

        # ChunkedArray has no "view" method, so combine into an Array.
        array = (
            array.combine_chunks() if isinstance(array, pyarrow.ChunkedArray) else array
        )

        # We can't cast to time64("ns"), but timestamp("ns") has the same
        # memory layout: 64-bit integers representing the number of nanoseconds
        # since the datetime epoch (midnight 1970-01-01).
        array = array.view(pyarrow.time64("ns"))
        return pyarrow.compute.cast(
            array,
            type if type is not None else pyarrow.time64("ns"),
        )


@pandas.api.extensions.register_extension_dtype
class DateDtype(core.BaseDatetimeDtype):
    """
    Extension dtype for time data.
    """

    name = date_dtype_name
    type = datetime.date

    @classmethod
    def construct_array_type(cls):
        return DateArray

    @staticmethod
    def __from_arrow__(
        array: Union[pyarrow.Array, pyarrow.ChunkedArray],
    ) -> "DateArray":
        """Convert to dbdate data from an Arrow array.

        See:
        https://pandas.pydata.org/pandas-docs/stable/development/extending.html#compatibility-with-apache-arrow
        """
        array = pyarrow.compute.cast(array, pyarrow.timestamp("ns"))
        np_array = array.to_numpy()
        return DateArray(np_array)


class DateArray(core.BaseDatetimeArray):
    """
    Pandas array type containing date data
    """

    # Data are stored as datetime64 values with a date of Jan 1, 1970

    dtype = DateDtype()

    @staticmethod
    def _datetime(
        scalar,
        match_fn=re.compile(r"\s*(?P<year>\d+)-(?P<month>\d+)-(?P<day>\d+)\s*$").match,
    ) -> Optional[numpy.datetime64]:
        # Convert pyarrow values to datetime.date.
        if isinstance(scalar, (pyarrow.Date32Scalar, pyarrow.Date64Scalar)):
            scalar = scalar.as_py()

        if pandas.isna(scalar):
            return numpy.datetime64("NaT", "D")
        elif isinstance(scalar, numpy.datetime64):
            dateObj = pandas.Timestamp(scalar)
        elif isinstance(scalar, datetime.date):
            dateObj = pandas.Timestamp(
                year=scalar.year, month=scalar.month, day=scalar.day
            )
        elif isinstance(scalar, str):
            match = match_fn(scalar)
            if not match:
                raise ValueError(f"Bad date string: {repr(scalar)}")
            year = int(match.group("year"))
            month = int(match.group("month"))
            day = int(match.group("day"))

            dateObj = pandas.Timestamp(
                year=year,
                month=month,
                day=day,
            )
        else:
            raise TypeError("Invalid value type", scalar)

        # TODO(#64): Support larger ranges with other units.
        if pandas.Timestamp.min < dateObj < pandas.Timestamp.max:
            return dateObj.to_datetime64()
        else:  # pragma: NO COVER
            # TODO(#166): Include these lines in coverage when pandas 2.0 is released.
            raise OutOfBoundsDatetime("Out of bounds", scalar)  # pragma: NO COVER

    def _box_func(self, x):
        if pandas.isna(x):
            return pandas.NaT
        try:
            return x.astype(_NP_BOX_DTYPE).item().date()
        except AttributeError:
            x = numpy.datetime64(
                x, "ns"
            )  # Integers are stored with nanosecond precision.
            return x.astype(_NP_BOX_DTYPE).item().date()

    def astype(self, dtype, copy=True):
        stype = str(dtype)
        if stype.startswith("datetime"):
            if stype == "datetime" or stype == "datetime64":
                dtype = self._ndarray.dtype
            return self._ndarray.astype(dtype, copy=copy)
        elif stype.startswith("<M8"):
            if stype == "<M8":
                dtype = self._ndarray.dtype
            return self._ndarray.astype(dtype, copy=copy)

        return super().astype(dtype, copy=copy)

    def __arrow_array__(self, type=None):
        """Convert to an Arrow array from dbdate data.

        See:
        https://pandas.pydata.org/pandas-docs/stable/development/extending.html#compatibility-with-apache-arrow
        """
        array = pyarrow.array(self._ndarray, type=pyarrow.timestamp("ns"))
        return pyarrow.compute.cast(
            array,
            type if type is not None else pyarrow.date32(),
        )

    def __add__(self, other):
        if isinstance(other, pandas.DateOffset):
            return self.astype("object") + other

        if isinstance(other, TimeArray):
            return (other._ndarray - _NPEPOCH) + self._ndarray

        return super().__add__(other)  # type: ignore[misc]

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, pandas.DateOffset):
            return self.astype("object") - other

        if isinstance(other, self.__class__):
            return self._ndarray - other._ndarray

        return super().__sub__(other)  # type: ignore[misc]


def _check_python_version():
    """Checks the runtime Python version and issues a warning if needed."""
    import sys

    if sys.version_info < (3, 10):
        warnings.warn(
            "The python-bigquery library as well as the python-db-dtypes-pandas library no "
            "longer supports Python 3.7, 3.8, and 3.9. "
            f"Your Python version is {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}. We "
            "recommend that you update soon to ensure ongoing support. For "
            "more details, see: [Google Cloud Client Libraries Supported Python Versions policy](https://cloud.google.com/python/docs/supported-python-versions)",
            FutureWarning,
            stacklevel=2,  # Point warning to the caller of __init__
        )


_check_python_version()

__all__ = [
    "__version__",
    "DateArray",
    "DateDtype",
    "TimeArray",
    "TimeDtype",
    "JSONDtype",
    "JSONArray",
    "JSONArrowType",
]
