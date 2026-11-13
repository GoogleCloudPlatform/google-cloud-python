# Copyright 2018 Google LLC
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
from google.protobuf import empty_pb2

from proto.marshal.marshal import BaseMarshal


def test_registration():
    marshal = BaseMarshal()

    @marshal.register(empty_pb2.Empty)
    class Rule:
        def to_proto(self, value):
            return value

        def to_python(self, value, *, absent=None):
            return value

    assert isinstance(marshal._rules[empty_pb2.Empty], Rule)


def test_invalid_marshal_class():
    marshal = BaseMarshal()
    with pytest.raises(TypeError):

        @marshal.register(empty_pb2.Empty)
        class Marshal:
            pass


def test_invalid_marshal_rule():
    marshal = BaseMarshal()
    with pytest.raises(TypeError):
        marshal.register(empty_pb2.Empty, rule=object())
