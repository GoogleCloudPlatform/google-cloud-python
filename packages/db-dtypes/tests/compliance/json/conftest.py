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


import json
import random

import numpy as np
import pandas as pd
import pytest

from db_dtypes import JSONArray, JSONDtype


def make_data():
    # Since the `np.array` constructor needs a consistent shape after the first
    # dimension, the samples data in this instance doesn't include the array type.
    samples = [
        True,  # Boolean
        100,  # Int
        0.98,  # Float
        "str",  # String
        {"bool_value": True},  # Dict with a boolean
        {"float_num": 3.14159},  # Dict with a float
        {"date": "2024-07-16"},  # Dict with a date (as strings)
        {"null_field": None},  # Dict with a null
        {"list_data": [10, 20, 30]},  # Dict with a list
        {"person": {"name": "Alice", "age": 35}},  # Dict with nested objects
        {"address": {"street": "123 Main St", "city": "Anytown"}},
        {"order": {"items": ["book", "pen"], "total": 15.99}},
    ]
    data = np.random.default_rng(2).choice(samples, size=100)
    # This replaces a single data item with an array. We are skipping the first two
    # items to avoid some `setitem` tests failed, because setting with a list is
    # ambiguity in this context.
    id = random.randint(3, 99)
    data[id] = [0.1, 0.2]  # Array
    return data


@pytest.fixture
def dtype():
    return JSONDtype()


@pytest.fixture
def data():
    """Length-100 PeriodArray for semantics test."""
    data = make_data()

    return JSONArray._from_sequence(data)


@pytest.fixture
def data_for_twos(dtype):
    """
    Length-100 array in which all the elements are two.

    Call pytest.skip in your fixture if the dtype does not support divmod.
    """
    pytest.skip(f"{dtype} is not a numeric dtype")


@pytest.fixture
def data_missing():
    """Length 2 array with [NA, Valid]"""
    return JSONArray._from_sequence([None, {"a": 10}])


@pytest.fixture
def data_missing_for_sorting():
    return JSONArray._from_sequence([json.dumps({"b": 1}), None, json.dumps({"a": 4})])


@pytest.fixture
def data_for_sorting():
    return JSONArray._from_sequence(
        [json.dumps({"b": 1}), json.dumps({"c": 4}), json.dumps({"a": 2})]
    )


@pytest.fixture
def na_cmp():
    """
    Binary operator for comparing NA values.

    Should return a function of two arguments that returns
    True if both arguments are (scalar) NA for your type.

    By default, uses ``operator.is_``
    """

    def cmp(a, b):
        return lambda left, right: pd.isna(left) and pd.isna(right)

    return cmp


@pytest.fixture
def data_repeated(data):
    """
    Generate many datasets.

    Parameters
    ----------
    data : fixture implementing `data`

    Returns
    -------
    Callable[[int], Generator]:
        A callable that takes a `count` argument and
        returns a generator yielding `count` datasets.
    """

    def gen(count):
        for _ in range(count):
            yield data

    return gen


_all_numeric_accumulations = ["cumsum", "cumprod", "cummin", "cummax"]


@pytest.fixture(params=_all_numeric_accumulations)
def all_numeric_accumulations(request):
    """
    Fixture for numeric accumulation names
    """
    return request.param


_all_boolean_reductions = ["all", "any"]


@pytest.fixture(params=_all_boolean_reductions)
def all_boolean_reductions(request):
    """
    Fixture for boolean reduction names.
    """
    return request.param


_all_numeric_reductions = [
    "count",
    "sum",
    "max",
    "min",
    "mean",
    "prod",
    "std",
    "var",
    "median",
    "kurt",
    "skew",
    "sem",
]


@pytest.fixture(params=_all_numeric_reductions)
def all_numeric_reductions(request):
    """
    Fixture for numeric reduction names.
    """
    return request.param


@pytest.fixture(params=["data", "data_missing"])
def all_data(request, data, data_missing):
    """Parametrized fixture returning 'data' or 'data_missing' integer arrays.

    Used to test dtype conversion with and without missing values.
    """
    if request.param == "data":
        return data
    elif request.param == "data_missing":
        return data_missing
