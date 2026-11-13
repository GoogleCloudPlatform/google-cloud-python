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

from google.cloud.sqladmin_v1.types import cloud_sql_resources

__protobuf__ = proto.module(
    package="google.cloud.sql.v1",
    manifest={
        "SqlOperationsGetRequest",
        "SqlOperationsListRequest",
        "OperationsListResponse",
        "SqlOperationsCancelRequest",
    },
)


class SqlOperationsGetRequest(proto.Message):
    r"""Operations get request.

    Attributes:
        operation (str):
            Required. Instance operation ID.
        project (str):
            Required. Project ID of the project that
            contains the instance.
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    operation: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    location: str = proto.Field(
        proto.STRING,
        number=4,
    )


class SqlOperationsListRequest(proto.Message):
    r"""Operations list request.

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        max_results (int):
            Maximum number of operations per response.
        page_token (str):
            A previously-returned page token representing
            part of the larger set of results to view.
        project (str):
            Project ID of the project that contains the
            instance.
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    max_results: int = proto.Field(
        proto.UINT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    project: str = proto.Field(
        proto.STRING,
        number=4,
    )
    location: str = proto.Field(
        proto.STRING,
        number=6,
    )


class OperationsListResponse(proto.Message):
    r"""Operations list response.

    Attributes:
        kind (str):
            This is always ``sql#operationsList``.
        items (MutableSequence[google.cloud.sqladmin_v1.types.Operation]):
            List of operation resources.
        next_page_token (str):
            The continuation token, used to page through
            large result sets. Provide this value in a
            subsequent request to return the next page of
            results.
    """

    @property
    def raw_page(self):
        return self

    kind: str = proto.Field(
        proto.STRING,
        number=1,
    )
    items: MutableSequence[cloud_sql_resources.Operation] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=cloud_sql_resources.Operation,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlOperationsCancelRequest(proto.Message):
    r"""Operations cancel request.

    Attributes:
        operation (str):
            Instance operation ID.
        project (str):
            Project ID of the project that contains the
            instance.
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    operation: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
