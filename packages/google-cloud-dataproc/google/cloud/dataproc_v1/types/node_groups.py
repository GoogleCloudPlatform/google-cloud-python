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

import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.dataproc_v1.types import clusters

__protobuf__ = proto.module(
    package="google.cloud.dataproc.v1",
    manifest={
        "CreateNodeGroupRequest",
        "ResizeNodeGroupRequest",
        "GetNodeGroupRequest",
    },
)


class CreateNodeGroupRequest(proto.Message):
    r"""A request to create a node group.

    Attributes:
        parent (str):
            Required. The parent resource where this node group will be
            created. Format:
            ``projects/{project}/regions/{region}/clusters/{cluster}``
        node_group (google.cloud.dataproc_v1.types.NodeGroup):
            Required. The node group to create.
        node_group_id (str):
            Optional. An optional node group ID. Generated if not
            specified.

            The ID must contain only letters (a-z, A-Z), numbers (0-9),
            underscores (\_), and hyphens (-). Cannot begin or end with
            underscore or hyphen. Must consist of from 3 to 33
            characters.
        request_id (str):
            Optional. A unique ID used to identify the request. If the
            server receives two
            `CreateNodeGroupRequest <https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#google.cloud.dataproc.v1.CreateNodeGroupRequests>`__
            with the same ID, the second request is ignored and the
            first
            [google.longrunning.Operation][google.longrunning.Operation]
            created and stored in the backend is returned.

            Recommendation: Set this value to a
            `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier>`__.

            The ID must contain only letters (a-z, A-Z), numbers (0-9),
            underscores (\_), and hyphens (-). The maximum length is 40
            characters.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    node_group: clusters.NodeGroup = proto.Field(
        proto.MESSAGE,
        number=2,
        message=clusters.NodeGroup,
    )
    node_group_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ResizeNodeGroupRequest(proto.Message):
    r"""A request to resize a node group.

    Attributes:
        name (str):
            Required. The name of the node group to resize. Format:
            ``projects/{project}/regions/{region}/clusters/{cluster}/nodeGroups/{nodeGroup}``
        size (int):
            Required. The number of running instances for
            the node group to maintain. The group adds or
            removes instances to maintain the number of
            instances specified by this parameter.
        request_id (str):
            Optional. A unique ID used to identify the request. If the
            server receives two
            `ResizeNodeGroupRequest <https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#google.cloud.dataproc.v1.ResizeNodeGroupRequests>`__
            with the same ID, the second request is ignored and the
            first
            [google.longrunning.Operation][google.longrunning.Operation]
            created and stored in the backend is returned.

            Recommendation: Set this value to a
            `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier>`__.

            The ID must contain only letters (a-z, A-Z), numbers (0-9),
            underscores (\_), and hyphens (-). The maximum length is 40
            characters.
        graceful_decommission_timeout (google.protobuf.duration_pb2.Duration):
            Optional. Timeout for graceful YARN decommissioning.
            [Graceful decommissioning]
            (https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/scaling-clusters#graceful_decommissioning)
            allows the removal of nodes from the Compute Engine node
            group without interrupting jobs in progress. This timeout
            specifies how long to wait for jobs in progress to finish
            before forcefully removing nodes (and potentially
            interrupting jobs). Default timeout is 0 (for forceful
            decommission), and the maximum allowed timeout is 1 day.
            (see JSON representation of
            `Duration <https://developers.google.com/protocol-buffers/docs/proto3#json>`__).

            Only supported on Dataproc image versions 1.2 and higher.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    graceful_decommission_timeout: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=4,
        message=duration_pb2.Duration,
    )


class GetNodeGroupRequest(proto.Message):
    r"""A request to get a node group .

    Attributes:
        name (str):
            Required. The name of the node group to retrieve. Format:
            ``projects/{project}/regions/{region}/clusters/{cluster}/nodeGroups/{nodeGroup}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
