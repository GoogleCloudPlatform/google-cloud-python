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
    package="google.cloud.apigeeconnect.v1",
    manifest={
        "ListConnectionsRequest",
        "ListConnectionsResponse",
        "Connection",
        "Cluster",
    },
)


class ListConnectionsRequest(proto.Message):
    r"""The request for [ListConnections][Management.ListConnections].

    Attributes:
        parent (str):
            Required. Parent name of the form:
            ``projects/{project_number or project_id}/endpoints/{endpoint}``.
        page_size (int):
            The maximum number of connections to return.
            The service may return fewer than this value. If
            unspecified, at most 100 connections will be
            returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            A page token, received from a previous ``ListConnections``
            call. Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListConnections`` must match the call that provided the
            page token.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListConnectionsResponse(proto.Message):
    r"""The response for [ListConnections][Management.ListConnections].

    Attributes:
        connections (MutableSequence[google.cloud.apigeeconnect_v1.types.Connection]):
            A list of clients.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    connections: MutableSequence["Connection"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Connection",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class Connection(proto.Message):
    r"""

    Attributes:
        endpoint (str):
            The endpoint that the connection is made against. Format:
            ``projects/{project_number}/endpoints/{endpoint}``
        cluster (google.cloud.apigeeconnect_v1.types.Cluster):
            Cluster information.
        stream_count (int):
            The count of streams.
    """

    endpoint: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cluster: "Cluster" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Cluster",
    )
    stream_count: int = proto.Field(
        proto.INT32,
        number=3,
    )


class Cluster(proto.Message):
    r"""

    Attributes:
        name (str):
            The name of the cluster.
        region (str):
            The region of the cluster.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    region: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
