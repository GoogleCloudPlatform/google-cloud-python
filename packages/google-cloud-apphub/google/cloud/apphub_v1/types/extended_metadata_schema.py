# -*- coding: utf-8 -*-
# Copyright 2026 Google LLC
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
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.apphub.v1",
    manifest={
        "ExtendedMetadataSchema",
    },
)


class ExtendedMetadataSchema(proto.Message):
    r"""ExtendedMetadataSchema represents a schema for extended
    metadata of a service or workload.

    Attributes:
        name (str):
            Identifier. Resource name of the schema.
            Format:

            projects/<project>/locations/<location>/extendedMetadataSchemas/<schema-id>
        json_schema (str):
            Output only. The JSON schema as a string.
        schema_version (int):
            Output only. The version of the schema. New
            versions are required to be backwards
            compatible.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    json_schema: str = proto.Field(
        proto.STRING,
        number=2,
    )
    schema_version: int = proto.Field(
        proto.INT64,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
