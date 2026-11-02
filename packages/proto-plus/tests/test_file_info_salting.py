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


import collections

from google.protobuf import descriptor_pb2

import proto
from proto import _file_info, _package_info


def sample_file_info(name):
    filename = name + ".proto"

    # Get the essential information about the proto package, and where
    # this component belongs within the file.
    package, marshal = _package_info.compile(name, {})

    # Get or create the information about the file, including the
    # descriptor to which the new message descriptor shall be added.
    return _file_info._FileInfo.registry.setdefault(
        filename,
        _file_info._FileInfo(
            descriptor=descriptor_pb2.FileDescriptorProto(
                name=filename,
                package=package,
                syntax="proto3",
            ),
            enums=collections.OrderedDict(),
            messages=collections.OrderedDict(),
            name=filename,
            nested={},
            nested_enum={},
        ),
    )


def test_fallback_salt_is_appended_to_filename():
    # given
    class Foo(proto.Message):
        bar = proto.Field(proto.INT32, number=1)

    name = "my-fileinfo"
    fallback_salt = "my-fallback_salt"
    file_info = sample_file_info(name)

    # when
    file_info.generate_file_pb(new_class=Foo, fallback_salt=fallback_salt)

    # then
    assert file_info.descriptor.name == name + "_" + fallback_salt + ".proto"


def test_none_fallback_salt_is_appended_to_filename_as_empty():
    # given

    class Foo(proto.Message):
        bar = proto.Field(proto.INT32, number=1)

    name = "my-fileinfo"
    none_fallback_salt = None
    file_info = sample_file_info(name)

    # when
    file_info.generate_file_pb(new_class=Foo, fallback_salt=none_fallback_salt)

    # then
    assert file_info.descriptor.name == name + ".proto"
