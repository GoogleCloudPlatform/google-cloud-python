# -*- coding: utf-8 -*-
# Copyright 2025 Google LLC
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
#
import my_oneof_message
import pytest
from google.protobuf import duration_pb2

from google.cloud.bigtable_admin_v2.types import GcRule

# The following proto bytestring was constructed running printproto in
# text-to-binary mode on the following textproto for GcRule:
#
# intersection {
#   rules {
#     max_num_versions: 1234
#   }
#   rules {
#     max_age {
#       seconds: 12345
#     }
#   }
# }
GCRULE_RAW_PROTO_BYTESTRING = b"\x1a\x0c\n\x03\x08\xd2\t\n\x05\x12\x03\x08\xb9`"
INITIAL_VALUE = 123
FINAL_VALUE = 456


@pytest.fixture
def default_msg():
    return my_oneof_message.MyOneofMessage()


@pytest.fixture
def foo_msg():
    return my_oneof_message.MyOneofMessage(foo=INITIAL_VALUE)


def test_oneof_message_setattr_oneof_no_conflict(default_msg):
    default_msg.foo = INITIAL_VALUE
    default_msg.baz = INITIAL_VALUE
    assert default_msg.foo == INITIAL_VALUE
    assert default_msg.baz == INITIAL_VALUE
    assert not default_msg.bar


def test_oneof_message_setattr_conflict(default_msg, foo_msg):
    with pytest.raises(ValueError):
        foo_msg.bar = INITIAL_VALUE
    assert foo_msg.foo == INITIAL_VALUE
    assert not foo_msg.bar

    default_msg.bar = INITIAL_VALUE
    with pytest.raises(ValueError):
        default_msg.foo = INITIAL_VALUE
    assert default_msg.bar == INITIAL_VALUE
    assert not default_msg.foo


def test_oneof_message_setattr_oneof_same_oneof_field(default_msg, foo_msg):
    foo_msg.foo = FINAL_VALUE
    assert foo_msg.foo == FINAL_VALUE
    assert not foo_msg.bar

    default_msg.bar = INITIAL_VALUE
    default_msg.bar = FINAL_VALUE
    assert default_msg.bar == FINAL_VALUE
    assert not default_msg.foo


def test_oneof_message_setattr_oneof_delattr(foo_msg):
    del foo_msg.foo
    foo_msg.bar = INITIAL_VALUE
    assert foo_msg.bar == INITIAL_VALUE
    assert not foo_msg.foo


def test_oneof_message_init_oneof_conflict(foo_msg):
    with pytest.raises(ValueError):
        my_oneof_message.MyOneofMessage(foo=INITIAL_VALUE, bar=INITIAL_VALUE)

    with pytest.raises(ValueError):
        my_oneof_message.MyOneofMessage(
            {
                "foo": INITIAL_VALUE,
                "bar": INITIAL_VALUE,
            }
        )

    with pytest.raises(ValueError):
        my_oneof_message.MyOneofMessage(foo_msg._pb, bar=INITIAL_VALUE)

    with pytest.raises(ValueError):
        my_oneof_message.MyOneofMessage(foo_msg, bar=INITIAL_VALUE)


def test_oneof_message_init_oneof_no_conflict(foo_msg):
    msg = my_oneof_message.MyOneofMessage(foo=INITIAL_VALUE, baz=INITIAL_VALUE)
    assert msg.foo == INITIAL_VALUE
    assert msg.baz == INITIAL_VALUE
    assert not msg.bar

    msg = my_oneof_message.MyOneofMessage(
        {
            "foo": INITIAL_VALUE,
            "baz": INITIAL_VALUE,
        }
    )
    assert msg.foo == INITIAL_VALUE
    assert msg.baz == INITIAL_VALUE
    assert not msg.bar

    msg = my_oneof_message.MyOneofMessage(foo_msg, baz=INITIAL_VALUE)
    assert msg.foo == INITIAL_VALUE
    assert msg.baz == INITIAL_VALUE
    assert not msg.bar

    msg = my_oneof_message.MyOneofMessage(foo_msg._pb, baz=INITIAL_VALUE)
    assert msg.foo == INITIAL_VALUE
    assert msg.baz == INITIAL_VALUE
    assert not msg.bar


def test_oneof_message_init_kwargs_override_same_field_oneof(foo_msg):
    # Kwargs take precedence over mapping, and this should be OK
    msg = my_oneof_message.MyOneofMessage(
        {
            "foo": INITIAL_VALUE,
        },
        foo=FINAL_VALUE,
    )
    assert msg.foo == FINAL_VALUE

    msg = my_oneof_message.MyOneofMessage(foo_msg, foo=FINAL_VALUE)
    assert msg.foo == FINAL_VALUE

    msg = my_oneof_message.MyOneofMessage(foo_msg._pb, foo=FINAL_VALUE)
    assert msg.foo == FINAL_VALUE


def test_gcrule_serialize_deserialize():
    test = GcRule(
        intersection=GcRule.Intersection(
            rules=[
                GcRule(max_num_versions=1234),
                GcRule(max_age=duration_pb2.Duration(seconds=12345)),
            ]
        )
    )
    assert GcRule.serialize(test) == GCRULE_RAW_PROTO_BYTESTRING
    assert GcRule.deserialize(GCRULE_RAW_PROTO_BYTESTRING) == test
