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
        "DeleteCollectionRequest",
        "DeleteCollectionMetadata",
    },
)


class DeleteCollectionRequest(proto.Message):
    r"""Request message for
    [CollectionService.DeleteCollection][google.cloud.discoveryengine.v1.CollectionService.DeleteCollection]
    method.

    Attributes:
        name (str):
            Required. The full resource name of the Collection, in the
            format of
            ``projects/{project}/locations/{location}/collections/{collection}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteCollectionMetadata(proto.Message):
    r"""Metadata related to the progress of the
    [CollectionService.UpdateCollection][] operation. This will be
    returned by the google.longrunning.Operation.metadata field.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Operation create time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Operation last update time. If the operation
            is done, this is also the finish time.
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
