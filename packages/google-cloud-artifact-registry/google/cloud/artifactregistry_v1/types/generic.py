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

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.devtools.artifactregistry.v1",
    manifest={
        "GenericArtifact",
    },
)


class GenericArtifact(proto.Message):
    r"""GenericArtifact represents a generic artifact

    Attributes:
        name (str):
            Resource name of the generic artifact. project, location,
            repository, package_id and version_id create a unique
            generic artifact. i.e.
            "projects/test-project/locations/us-west4/repositories/test-repo/
            genericArtifacts/package_id:version_id".
        version (str):
            The version of the generic artifact.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the Generic module
            is created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the Generic module
            is updated.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
