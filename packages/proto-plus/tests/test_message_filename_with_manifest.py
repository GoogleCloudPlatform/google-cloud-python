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

PACKAGE = "a.test.package.with.manifest"
__protobuf__ = proto.module(
    package=PACKAGE,
    manifest={"ThisFoo", "ThisBar"},
)


class ThisFoo(proto.Message):
    foo = proto.Field(proto.INT32, number=1)


class ThisBar(proto.Message):
    bar = proto.Field(proto.INT32, number=2)


def test_manifest_causes_exclusion_of_classname_salt():
    assert (
        ThisFoo.pb(ThisFoo()).DESCRIPTOR.file.name
        == "test_message_filename_with_manifest.proto"
    )
    assert (
        ThisBar.pb(ThisBar()).DESCRIPTOR.file.name
        == "test_message_filename_with_manifest.proto"
    )
