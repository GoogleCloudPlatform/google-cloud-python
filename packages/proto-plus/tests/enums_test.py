# Copyright (C) 2021  Google LLC
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

import proto

__protobuf__ = proto.module(
    package="test.proto",
    manifest={
        "Enums",
    },
)


class OneEnum(proto.Enum):
    UNSPECIFIED = 0
    SOME_VALUE = 1


class OtherEnum(proto.Enum):
    UNSPECIFIED = 0
    APPLE = 1
    BANANA = 2
