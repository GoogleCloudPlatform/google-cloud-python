# Copyright 2021, Google LLC
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

import enums_test
import pytest


def test_total_ordering_w_same_enum_type():
    to_compare = enums_test.OneEnum.SOME_VALUE

    for item in enums_test.OneEnum:
        if item.value < to_compare.value:
            assert not to_compare == item
            assert to_compare != item
            assert not to_compare < item
            assert not to_compare <= item
            assert to_compare > item
            assert to_compare >= item
        elif item.value > to_compare.value:
            assert not to_compare == item
            assert to_compare != item
            assert to_compare < item
            assert to_compare <= item
            assert not to_compare > item
            assert not to_compare >= item
        else:  # item.value == to_compare.value:
            assert to_compare == item
            assert not to_compare != item
            assert not to_compare < item
            assert to_compare <= item
            assert not to_compare > item
            assert to_compare >= item


def test_total_ordering_w_other_enum_type():
    to_compare = enums_test.OneEnum.SOME_VALUE

    for item in enums_test.OtherEnum:
        assert not to_compare == item
        assert type(to_compare).SOME_VALUE != item
        try:
            assert to_compare.SOME_VALUE != item
        except AttributeError:  # Python 3.11.0b3
            pass
        with pytest.raises(TypeError):
            assert not to_compare < item
        with pytest.raises(TypeError):
            assert not to_compare <= item
        with pytest.raises(TypeError):
            assert not to_compare > item
        with pytest.raises(TypeError):
            assert not to_compare >= item


@pytest.mark.parametrize("int_val", range(-1, 3))
def test_total_ordering_w_int(int_val):
    to_compare = enums_test.OneEnum.SOME_VALUE

    if int_val < to_compare.value:
        assert not to_compare == int_val
        assert to_compare != int_val
        assert not to_compare < int_val
        assert not to_compare <= int_val
        assert to_compare > int_val
        assert to_compare >= int_val
    elif int_val > to_compare.value:
        assert not to_compare == int_val
        assert to_compare != int_val
        assert to_compare < int_val
        assert to_compare <= int_val
        assert not to_compare > int_val
        assert not to_compare >= int_val
    else:  # int_val == to_compare.value:
        assert to_compare == int_val
        assert not to_compare != int_val
        assert not to_compare < int_val
        assert to_compare <= int_val
        assert not to_compare > int_val
        assert to_compare >= int_val


def test_hashing():
    to_hash = enums_test.OneEnum.SOME_VALUE

    {to_hash: "testing"}  # no raise
