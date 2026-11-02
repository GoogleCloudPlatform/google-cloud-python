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

from db_dtypes import DateArray, DateDtype


@pytest.fixture(params=["data", "data_missing"])
def all_data(request, data, data_missing):
    """Parametrized fixture giving 'data' and 'data_missing'"""
    if request.param == "data":
        return data
    elif request.param == "data_missing":
        return data_missing


@pytest.fixture
def data():
    return DateArray(
        numpy.arange(
            datetime.datetime(1900, 1, 1),
            datetime.datetime(2099, 12, 31),
            datetime.timedelta(days=731),
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
    return DateArray(
        [
            datetime.date(1980, 1, 27),
            datetime.date(1980, 1, 27),
            None,
            None,
            datetime.date(1969, 12, 30),
            datetime.date(1969, 12, 30),
            datetime.date(1980, 1, 27),
            datetime.date(2022, 3, 18),
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
    return DateArray(
        [
            datetime.date(1980, 1, 27),
            datetime.date(2022, 3, 18),
            datetime.date(1969, 12, 30),
        ]
    )


@pytest.fixture
def data_missing():
    """Length-2 array with [NA, Valid]

    See:
    https://github.com/pandas-dev/pandas/blob/main/pandas/tests/extension/conftest.py
    """
    return DateArray([None, datetime.date(2022, 1, 27)])


@pytest.fixture
def data_missing_for_sorting():
    """
    Length-3 array with a known sort order.

    This should be three items [B, NA, A] with
    A < B and NA missing.

    See:
    https://github.com/pandas-dev/pandas/blob/main/pandas/tests/extension/conftest.py
    """
    return DateArray([datetime.date(1980, 1, 27), None, datetime.date(1969, 12, 30)])


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
    return DateDtype()
