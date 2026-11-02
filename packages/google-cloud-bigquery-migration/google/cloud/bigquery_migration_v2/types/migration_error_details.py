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

import google.rpc.error_details_pb2 as error_details_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.bigquery.migration.v2",
    manifest={
        "ResourceErrorDetail",
        "ErrorDetail",
        "ErrorLocation",
    },
)


class ResourceErrorDetail(proto.Message):
    r"""Provides details for errors and the corresponding resources.

    Attributes:
        resource_info (google.rpc.error_details_pb2.ResourceInfo):
            Required. Information about the resource
            where the error is located.
        error_details (MutableSequence[google.cloud.bigquery_migration_v2.types.ErrorDetail]):
            Required. The error details for the resource.
        error_count (int):
            Required. How many errors there are in total for the
            resource. Truncation can be indicated by having an
            ``error_count`` that is higher than the size of
            ``error_details``.
    """

    resource_info: error_details_pb2.ResourceInfo = proto.Field(
        proto.MESSAGE,
        number=1,
        message=error_details_pb2.ResourceInfo,
    )
    error_details: MutableSequence["ErrorDetail"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="ErrorDetail",
    )
    error_count: int = proto.Field(
        proto.INT32,
        number=3,
    )


class ErrorDetail(proto.Message):
    r"""Provides details for errors, e.g. issues that where
    encountered when processing a subtask.

    Attributes:
        location (google.cloud.bigquery_migration_v2.types.ErrorLocation):
            Optional. The exact location within the
            resource (if applicable).
        error_info (google.rpc.error_details_pb2.ErrorInfo):
            Required. Describes the cause of the error
            with structured detail.
    """

    location: "ErrorLocation" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ErrorLocation",
    )
    error_info: error_details_pb2.ErrorInfo = proto.Field(
        proto.MESSAGE,
        number=2,
        message=error_details_pb2.ErrorInfo,
    )


class ErrorLocation(proto.Message):
    r"""Holds information about where the error is located.

    Attributes:
        line (int):
            Optional. If applicable, denotes the line
            where the error occurred. A zero value means
            that there is no line information.
        column (int):
            Optional. If applicable, denotes the column
            where the error occurred. A zero value means
            that there is no columns information.
    """

    line: int = proto.Field(
        proto.INT32,
        number=1,
    )
    column: int = proto.Field(
        proto.INT32,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
