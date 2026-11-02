# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest

from proto.marshal.marshal import BaseMarshal
from proto.primitives import ProtoType

INT_32BIT_PLUS_ONE = 0xFFFFFFFF + 1


@pytest.mark.parametrize(
    "pb_type,value,expected",
    [
        (ProtoType.INT64, 0, 0),
        (ProtoType.INT64, INT_32BIT_PLUS_ONE, INT_32BIT_PLUS_ONE),
        (ProtoType.SINT64, -INT_32BIT_PLUS_ONE, -INT_32BIT_PLUS_ONE),
        (ProtoType.INT64, None, None),
        (ProtoType.UINT64, 0, 0),
        (ProtoType.UINT64, INT_32BIT_PLUS_ONE, INT_32BIT_PLUS_ONE),
        (ProtoType.UINT64, None, None),
        (ProtoType.SINT64, 0, 0),
        (ProtoType.SINT64, INT_32BIT_PLUS_ONE, INT_32BIT_PLUS_ONE),
        (ProtoType.SINT64, -INT_32BIT_PLUS_ONE, -INT_32BIT_PLUS_ONE),
        (ProtoType.SINT64, None, None),
        (ProtoType.FIXED64, 0, 0),
        (ProtoType.FIXED64, INT_32BIT_PLUS_ONE, INT_32BIT_PLUS_ONE),
        (ProtoType.FIXED64, -INT_32BIT_PLUS_ONE, -INT_32BIT_PLUS_ONE),
        (ProtoType.FIXED64, None, None),
        (ProtoType.SFIXED64, 0, 0),
        (ProtoType.SFIXED64, INT_32BIT_PLUS_ONE, INT_32BIT_PLUS_ONE),
        (ProtoType.SFIXED64, -INT_32BIT_PLUS_ONE, -INT_32BIT_PLUS_ONE),
        (ProtoType.SFIXED64, None, None),
    ],
)
def test_marshal_to_proto_stringy_numbers(pb_type, value, expected):
    marshal = BaseMarshal()
    assert marshal.to_proto(pb_type, value) == expected
