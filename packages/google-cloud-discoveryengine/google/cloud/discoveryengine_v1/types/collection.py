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
    package="google.cloud.discoveryengine.v1",
    manifest={
        "Collection",
    },
)


class Collection(proto.Message):
    r"""Collection is a container for configuring resources and
    access to a set of DataStores.

    Attributes:
        name (str):
            Immutable. The full resource name of the Collection. Format:
            ``projects/{project}/locations/{location}/collections/{collection_id}``.

            This field must be a UTF-8 encoded string with a length
            limit of 1024 characters.
        display_name (str):
            Required. The Collection display name.

            This field must be a UTF-8 encoded string with a length
            limit of 128 characters. Otherwise, an INVALID_ARGUMENT
            error is returned.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp the
            [Collection][google.cloud.discoveryengine.v1.Collection] was
            created at.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
