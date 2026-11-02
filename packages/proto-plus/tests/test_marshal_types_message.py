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

import proto
from proto.marshal.rules.message import MessageRule


def test_to_proto():
    class Foo(proto.Message):
        bar = proto.Field(proto.INT32, number=1)

    message_rule = MessageRule(Foo.pb(), Foo)
    foo_pb2_a = message_rule.to_proto(Foo(bar=42))
    foo_pb2_b = message_rule.to_proto(Foo.pb()(bar=42))
    foo_pb2_c = message_rule.to_proto({"bar": 42})
    assert foo_pb2_a == foo_pb2_b == foo_pb2_c


def test_to_python():
    class Foo(proto.Message):
        bar = proto.Field(proto.INT32, number=1)

    message_rule = MessageRule(Foo.pb(), Foo)
    foo_a = message_rule.to_python(Foo(bar=42))
    foo_b = message_rule.to_python(Foo.pb()(bar=42))
    assert foo_a == foo_b
