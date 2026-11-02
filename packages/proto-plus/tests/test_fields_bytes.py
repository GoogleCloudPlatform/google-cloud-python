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

import base64

import proto


def test_bytes_init():
    class Foo(proto.Message):
        bar = proto.Field(proto.BYTES, number=1)
        baz = proto.Field(proto.BYTES, number=2)

    foo = Foo(bar=b"spam")
    assert foo.bar == b"spam"
    assert foo.baz == b""
    assert not foo.baz
    assert Foo.pb(foo).bar == b"spam"
    assert Foo.pb(foo).baz == b""


def test_bytes_rmw():
    class Foo(proto.Message):
        spam = proto.Field(proto.BYTES, number=1)
        eggs = proto.Field(proto.BYTES, number=2)

    foo = Foo(spam=b"bar")
    foo.eggs = b"baz"
    assert foo.spam == b"bar"
    assert foo.eggs == b"baz"
    assert Foo.pb(foo).spam == b"bar"
    assert Foo.pb(foo).eggs == b"baz"
    foo.spam = b"bacon"
    assert foo.spam == b"bacon"
    assert foo.eggs == b"baz"
    assert Foo.pb(foo).spam == b"bacon"
    assert Foo.pb(foo).eggs == b"baz"


def test_bytes_del():
    class Foo(proto.Message):
        bar = proto.Field(proto.BYTES, number=1)

    foo = Foo(bar=b"spam")
    assert foo.bar == b"spam"
    del foo.bar
    assert foo.bar == b""
    assert not foo.bar


def test_bytes_string_distinct():
    class Foo(proto.Message):
        bar = proto.Field(proto.STRING, number=1)
        baz = proto.Field(proto.BYTES, number=2)

    foo = Foo()
    assert foo.bar != foo.baz

    # Since protobuf was written against Python 2, it accepts bytes objects
    # for strings (but not vice versa).
    foo.bar = b"anything"
    assert foo.bar == "anything"

    # We need to permit setting bytes fields from strings,
    # but the marshalling needs to base64 decode the result.
    # This is a requirement for interop with the vanilla protobuf runtime:
    # converting a proto message to a dict base64 encodes the bytes
    # because it may be sent over the network via a protocol like HTTP.
    encoded_swallow: str = base64.urlsafe_b64encode(b"unladen swallow").decode("utf-8")
    assert type(encoded_swallow) is str
    foo.baz = encoded_swallow
    assert foo.baz == b"unladen swallow"


def test_bytes_to_dict_bidi():
    class Foo(proto.Message):
        bar = proto.Field(proto.BYTES, number=1)

    foo = Foo(bar=b"spam")

    foo_dict = Foo.to_dict(foo)
    foo_two = Foo(foo_dict)

    assert foo == foo_two
