# Copyright 2017 Google LLC All rights reserved.
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

import pytest


def _make_value_list(*args, **kwargs):
    from google.cloud.firestore_v1.transforms import _ValueList

    return _ValueList(*args, **kwargs)


def test__valuelist_ctor_w_non_list_non_tuple():
    invalid_values = (None, "phred", b"DEADBEEF", 123, {}, object())
    for invalid_value in invalid_values:
        with pytest.raises(ValueError):
            _make_value_list(invalid_value)


def test__valuelist_ctor_w_empty():
    with pytest.raises(ValueError):
        _make_value_list([])


def test__valuelist_ctor_w_non_empty_list():
    values = ["phred", "bharney"]
    inst = _make_value_list(values)
    assert inst.values == values


def test__valuelist_ctor_w_non_empty_tuple():
    values = ("phred", "bharney")
    inst = _make_value_list(values)
    assert inst.values == list(values)


def test__valuelist___eq___other_type():
    values = ("phred", "bharney")
    inst = _make_value_list(values)
    other = object()
    assert not (inst == other)


def test__valuelist___eq___different_values():
    values = ("phred", "bharney")
    other_values = ("wylma", "bhetty")
    inst = _make_value_list(values)
    other = _make_value_list(other_values)
    assert not (inst == other)


def test__valuelist___eq___same_values():
    values = ("phred", "bharney")
    inst = _make_value_list(values)
    other = _make_value_list(values)
    assert inst == other


def _make_numeric_value(*args, **kwargs):
    from google.cloud.firestore_v1.transforms import _NumericValue

    return _NumericValue(*args, **kwargs)


@pytest.mark.parametrize(
    "invalid_value",
    [(None, "phred", b"DEADBEEF", [], {}, object())],
)
def test__numericvalue_ctor_w_invalid_types(invalid_value):
    with pytest.raises(ValueError):
        _make_numeric_value(invalid_value)


@pytest.mark.parametrize("value", [-10, -1, 0, 1, 10])
def test__numericvalue_ctor_w_int(value):
    inst = _make_numeric_value(value)
    assert inst.value == value


@pytest.mark.parametrize("value", [-10.0, -1.0, 0.0, 1.0, 10.0])
def test__numericvalue_ctor_w_float(value):
    inst = _make_numeric_value(value)
    assert inst.value == value


def test__numericvalue___eq___other_type():
    value = 3.1415926
    inst = _make_numeric_value(value)
    other = object()
    assert not (inst == other)


def test__numericvalue___eq___different_value():
    value = 3.1415926
    other_value = 2.71828
    inst = _make_numeric_value(value)
    other = _make_numeric_value(other_value)
    assert not (inst == other)


def test__numericvalue___eq___same_value():
    value = 3.1415926
    inst = _make_numeric_value(value)
    other = _make_numeric_value(value)
    assert inst == other


def test__server_timestamp_is_same_after_copy():
    import copy

    from google.cloud.firestore_v1.transforms import SERVER_TIMESTAMP

    value = SERVER_TIMESTAMP

    value_copy = copy.copy(value)
    assert value_copy is value


def test__server_timestamp_is_same_after_deepcopy():
    import copy

    from google.cloud.firestore_v1.transforms import SERVER_TIMESTAMP

    value = SERVER_TIMESTAMP

    value_copy = copy.deepcopy(value)
    assert value_copy is value
