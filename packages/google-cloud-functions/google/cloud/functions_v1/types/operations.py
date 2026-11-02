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

import google.protobuf.any_pb2 as any_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.functions.v1",
    manifest={
        "OperationType",
        "OperationMetadataV1",
    },
)


class OperationType(proto.Enum):
    r"""A type of an operation.

    Values:
        OPERATION_UNSPECIFIED (0):
            Unknown operation type.
        CREATE_FUNCTION (1):
            Triggered by CreateFunction call
        UPDATE_FUNCTION (2):
            Triggered by UpdateFunction call
        DELETE_FUNCTION (3):
            Triggered by DeleteFunction call.
    """

    OPERATION_UNSPECIFIED = 0
    CREATE_FUNCTION = 1
    UPDATE_FUNCTION = 2
    DELETE_FUNCTION = 3


class OperationMetadataV1(proto.Message):
    r"""Metadata describing an [Operation][google.longrunning.Operation]

    Attributes:
        target (str):
            Target of the operation - for example
            ``projects/project-1/locations/region-1/functions/function-1``
        type_ (google.cloud.functions_v1.types.OperationType):
            Type of operation.
        request (google.protobuf.any_pb2.Any):
            The original request that started the
            operation.
        version_id (int):
            Version id of the function created or updated
            by an API call. This field is only populated for
            Create and Update operations.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            The last update timestamp of the operation.
        build_id (str):
            The Cloud Build ID of the function created or
            updated by an API call. This field is only
            populated for Create and Update operations.
        source_token (str):
            An identifier for Firebase function sources.
            Disclaimer: This field is only supported for
            Firebase function deployments.
        build_name (str):
            The Cloud Build Name of the function deployment. This field
            is only populated for Create and Update operations.
            ``projects/<project-number>/locations/<region>/builds/<build-id>``.
    """

    target: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: "OperationType" = proto.Field(
        proto.ENUM,
        number=2,
        enum="OperationType",
    )
    request: any_pb2.Any = proto.Field(
        proto.MESSAGE,
        number=3,
        message=any_pb2.Any,
    )
    version_id: int = proto.Field(
        proto.INT64,
        number=4,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    build_id: str = proto.Field(
        proto.STRING,
        number=6,
    )
    source_token: str = proto.Field(
        proto.STRING,
        number=7,
    )
    build_name: str = proto.Field(
        proto.STRING,
        number=8,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
