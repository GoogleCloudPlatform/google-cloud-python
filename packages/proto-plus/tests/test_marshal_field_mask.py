# Copyright 2022 Google LLC
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

from google.protobuf import field_mask_pb2

import proto
from proto.marshal.marshal import BaseMarshal


def test_field_mask_read():
    class Foo(proto.Message):
        mask = proto.Field(
            proto.MESSAGE,
            number=1,
            message=field_mask_pb2.FieldMask,
        )

    foo = Foo(mask=field_mask_pb2.FieldMask(paths=["f.b.d", "f.c"]))

    assert isinstance(foo.mask, field_mask_pb2.FieldMask)
    assert foo.mask.paths == ["f.b.d", "f.c"]


def test_field_mask_write_string():
    class Foo(proto.Message):
        mask = proto.Field(
            proto.MESSAGE,
            number=1,
            message=field_mask_pb2.FieldMask,
        )

    foo = Foo()
    foo.mask = "f.b.d,f.c"

    assert isinstance(foo.mask, field_mask_pb2.FieldMask)
    assert foo.mask.paths == ["f.b.d", "f.c"]


def test_field_mask_write_pb2():
    class Foo(proto.Message):
        mask = proto.Field(
            proto.MESSAGE,
            number=1,
            message=field_mask_pb2.FieldMask,
        )

    foo = Foo()
    foo.mask = field_mask_pb2.FieldMask(paths=["f.b.d", "f.c"])

    assert isinstance(foo.mask, field_mask_pb2.FieldMask)
    assert foo.mask.paths == ["f.b.d", "f.c"]


def test_field_mask_absence():
    class Foo(proto.Message):
        mask = proto.Field(
            proto.MESSAGE,
            number=1,
            message=field_mask_pb2.FieldMask,
        )

    foo = Foo()
    assert not foo.mask.paths


def test_timestamp_del():
    class Foo(proto.Message):
        mask = proto.Field(
            proto.MESSAGE,
            number=1,
            message=field_mask_pb2.FieldMask,
        )

    foo = Foo()
    foo.mask = field_mask_pb2.FieldMask(paths=["f.b.d", "f.c"])

    del foo.mask
    assert not foo.mask.paths


def test_timestamp_to_python_idempotent():
    # This path can never run in the current configuration because proto
    # values are the only thing ever saved, and `to_python` is a read method.
    #
    # However, we test idempotency for consistency with `to_proto` and
    # general resiliency.
    marshal = BaseMarshal()
    py_value = "f.b.d,f.c"
    assert marshal.to_python(field_mask_pb2.FieldMask, py_value) is py_value
