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

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.netapp_v1.types import common

__protobuf__ = proto.module(
    package="google.cloud.netapp.v1",
    manifest={
        "ListHostGroupsRequest",
        "ListHostGroupsResponse",
        "GetHostGroupRequest",
        "CreateHostGroupRequest",
        "UpdateHostGroupRequest",
        "DeleteHostGroupRequest",
        "HostGroup",
    },
)


class ListHostGroupsRequest(proto.Message):
    r"""ListHostGroupsRequest for listing host groups.

    Attributes:
        parent (str):
            Required. Parent value for
            ListHostGroupsRequest
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, the server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filter to apply to the request.
        order_by (str):
            Optional. Hint for how to order the results
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
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListHostGroupsResponse(proto.Message):
    r"""ListHostGroupsResponse is the response to a
    ListHostGroupsRequest.

    Attributes:
        host_groups (MutableSequence[google.cloud.netapp_v1.types.HostGroup]):
            The list of host groups.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    host_groups: MutableSequence["HostGroup"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="HostGroup",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetHostGroupRequest(proto.Message):
    r"""GetHostGroupRequest for getting a host group.

    Attributes:
        name (str):
            Required. The resource name of the host group. Format:
            ``projects/{project_number}/locations/{location_id}/hostGroups/{host_group_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateHostGroupRequest(proto.Message):
    r"""CreateHostGroupRequest for creating a host group.

    Attributes:
        parent (str):
            Required. Parent value for
            CreateHostGroupRequest
        host_group (google.cloud.netapp_v1.types.HostGroup):
            Required. Fields of the host group to create.
        host_group_id (str):
            Required. ID of the host group to create.
            Must be unique within the parent resource. Must
            contain only letters, numbers, and hyphen, with
            the first character a letter or underscore, the
            last a letter or underscore or a number, and a
            63 character maximum.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    host_group: "HostGroup" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="HostGroup",
    )
    host_group_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class UpdateHostGroupRequest(proto.Message):
    r"""UpdateHostGroupRequest for updating a host group.

    Attributes:
        host_group (google.cloud.netapp_v1.types.HostGroup):
            Required. The host group to update. The host group's
            ``name`` field is used to identify the host group. Format:
            ``projects/{project_number}/locations/{location_id}/hostGroups/{host_group_id}``.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    host_group: "HostGroup" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="HostGroup",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteHostGroupRequest(proto.Message):
    r"""DeleteHostGroupRequest for deleting a single host group.

    Attributes:
        name (str):
            Required. The resource name of the host group. Format:
            ``projects/{project_number}/locations/{location_id}/hostGroups/{host_group_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class HostGroup(proto.Message):
    r"""Host group is a collection of hosts that can be used for
    accessing a Block Volume.

    Attributes:
        name (str):
            Identifier. The resource name of the host group. Format:
            ``projects/{project_number}/locations/{location_id}/hostGroups/{host_group_id}``.
        type_ (google.cloud.netapp_v1.types.HostGroup.Type):
            Required. Type of the host group.
        state (google.cloud.netapp_v1.types.HostGroup.State):
            Output only. State of the host group.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create time of the host group.
        hosts (MutableSequence[str]):
            Required. The list of hosts associated with
            the host group.
        os_type (google.cloud.netapp_v1.types.OsType):
            Required. The OS type of the host group. It
            indicates the type of operating system used by
            all of the hosts in the HostGroup. All hosts in
            a HostGroup must be of the same OS type. This
            can be set only when creating a HostGroup.
        description (str):
            Optional. Description of the host group.
        labels (MutableMapping[str, str]):
            Optional. Labels of the host group.
    """

    class Type(proto.Enum):
        r"""Types of host group.

        Values:
            TYPE_UNSPECIFIED (0):
                Unspecified type for host group.
            ISCSI_INITIATOR (1):
                iSCSI initiator host group.
        """

        TYPE_UNSPECIFIED = 0
        ISCSI_INITIATOR = 1

    class State(proto.Enum):
        r"""Host group states.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified state for host group.
            CREATING (1):
                Host group is creating.
            READY (2):
                Host group is ready.
            UPDATING (3):
                Host group is updating.
            DELETING (4):
                Host group is deleting.
            DISABLED (5):
                Host group is disabled.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        READY = 2
        UPDATING = 3
        DELETING = 4
        DISABLED = 5

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=2,
        enum=Type,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    hosts: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    os_type: common.OsType = proto.Field(
        proto.ENUM,
        number=6,
        enum=common.OsType,
    )
    description: str = proto.Field(
        proto.STRING,
        number=7,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=8,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
