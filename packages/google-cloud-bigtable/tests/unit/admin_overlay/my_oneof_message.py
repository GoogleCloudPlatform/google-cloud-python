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
import proto

from google.cloud.bigtable_admin_v2.utils import oneof_message

__protobuf__ = proto.module(
    package="test.oneof.v1",
    manifest={
        "MyOneofMessage",
    },
)


# Foo and Bar belong to oneof foobar, and baz is independent.
class MyOneofMessage(oneof_message.OneofMessage):
    foo: int = proto.Field(
        proto.INT32,
        number=1,
        oneof="foobar",
    )

    bar: int = proto.Field(
        proto.INT32,
        number=2,
        oneof="foobar",
    )

    baz: int = proto.Field(
        proto.INT32,
        number=3,
    )
