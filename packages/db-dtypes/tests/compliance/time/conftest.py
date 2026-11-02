# Copyright 2022 Google LLC
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
import pytest

from db_dtypes import TimeArray, TimeDtype


@pytest.fixture(params=["data", "data_missing"])
def all_data(request, data, data_missing):
    """Parametrized fixture giving 'data' and 'data_missing'"""
    if request.param == "data":
        return data
    elif request.param == "data_missing":
        return data_missing


@pytest.fixture
def data():
    return TimeArray(
        numpy.arange(
            datetime.datetime(1970, 1, 1),
            datetime.datetime(1970, 1, 2),
            datetime.timedelta(microseconds=864_123_456),
            dtype="datetime64[ns]",
        )
    )


@pytest.fixture
def data_for_grouping():
    """
    Data for factorization, grouping, and unique tests.

    Expected to be like [B, B, NA, NA, A, A, B, C]

    Where A < B < C and NA is missing

    See:
    https://github.com/pandas-dev/pandas/blob/main/pandas/tests/extension/conftest.py
    """
    return TimeArray(
        [
            datetime.time(11, 45, 29, 987_654),
            datetime.time(11, 45, 29, 987_654),
            None,
            None,
            datetime.time(0, 1, 2, 345_678),
            datetime.time(0, 1, 2, 345_678),
            datetime.time(11, 45, 29, 987_654),
            datetime.time(23, 59, 59, 999_999),
        ]
    )


@pytest.fixture
def data_for_sorting():
    """
    Length-3 array with a known sort order.

    This should be three items [B, C, A] with
    A < B < C

    See:
    https://github.com/pandas-dev/pandas/blob/main/pandas/tests/extension/conftest.py
    """
    return TimeArray(
        [
            datetime.time(11, 45, 29, 987_654),
            datetime.time(23, 59, 59, 999_999),
            datetime.time(0, 1, 2, 345_678),
        ]
    )


@pytest.fixture
def data_missing():
    """Length-2 array with [NA, Valid]

    See:
    https://github.com/pandas-dev/pandas/blob/main/pandas/tests/extension/conftest.py
    """
    return TimeArray([None, datetime.time(13, 7, 42, 123_456)])


@pytest.fixture
def data_missing_for_sorting():
    """
    Length-3 array with a known sort order.

    This should be three items [B, NA, A] with
    A < B and NA missing.

    See:
    https://github.com/pandas-dev/pandas/blob/main/pandas/tests/extension/conftest.py
    """
    return TimeArray(
        [datetime.time(13, 7, 42, 123_456), None, datetime.time(1, 2, 3, 456_789)]
    )


@pytest.fixture
def data_repeated(data):
    """
    Generate many datasets.

    See:
    https://github.com/pandas-dev/pandas/blob/main/pandas/tests/extension/conftest.py
    """

    def gen(count):
        for _ in range(count):
            yield data

    return gen


@pytest.fixture
def dtype():
    return TimeDtype()
