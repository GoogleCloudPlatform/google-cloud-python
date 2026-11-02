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

__protobuf__ = proto.module(
    package="google.cloud.networksecurity.v1",
    manifest={
        "AddressGroup",
        "ListAddressGroupsRequest",
        "ListAddressGroupsResponse",
        "GetAddressGroupRequest",
        "CreateAddressGroupRequest",
        "UpdateAddressGroupRequest",
        "DeleteAddressGroupRequest",
        "AddAddressGroupItemsRequest",
        "RemoveAddressGroupItemsRequest",
        "CloneAddressGroupItemsRequest",
        "ListAddressGroupReferencesRequest",
        "ListAddressGroupReferencesResponse",
    },
)


class AddressGroup(proto.Message):
    r"""AddressGroup is a resource that specifies how a collection of
    IP/DNS used in Firewall Policy.

    Attributes:
        name (str):
            Required. Name of the AddressGroup resource. It matches
            pattern
            ``projects/*/locations/{location}/addressGroups/<address_group>``.
        description (str):
            Optional. Free-text description of the
            resource.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was updated.
        labels (MutableMapping[str, str]):
            Optional. Set of label tags associated with
            the AddressGroup resource.
        type_ (google.cloud.network_security_v1.types.AddressGroup.Type):
            Required. The type of the Address Group.
            Possible values are "IPv4" or "IPV6".
        items (MutableSequence[str]):
            Optional. List of items.
        capacity (int):
            Required. Capacity of the Address Group
        self_link (str):
            Output only. Server-defined fully-qualified
            URL for this resource.
        purpose (MutableSequence[google.cloud.network_security_v1.types.AddressGroup.Purpose]):
            Optional. List of supported purposes of the
            Address Group.
    """

    class Type(proto.Enum):
        r"""Possible type of the Address Group.

        Values:
            TYPE_UNSPECIFIED (0):
                Default value.
            IPV4 (1):
                IP v4 ranges.
            IPV6 (2):
                IP v6 ranges.
        """

        TYPE_UNSPECIFIED = 0
        IPV4 = 1
        IPV6 = 2

    class Purpose(proto.Enum):
        r"""Purpose of the Address Group.

        Values:
            PURPOSE_UNSPECIFIED (0):
                Default value. Should never happen.
            DEFAULT (1):
                Address Group is distributed to VMC, and is
                usable in Firewall Policies and other systems
                that rely on VMC.
            CLOUD_ARMOR (2):
                Address Group is usable in Cloud Armor.
        """

        PURPOSE_UNSPECIFIED = 0
        DEFAULT = 1
        CLOUD_ARMOR = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
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
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=6,
        enum=Type,
    )
    items: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    capacity: int = proto.Field(
        proto.INT32,
        number=8,
    )
    self_link: str = proto.Field(
        proto.STRING,
        number=9,
    )
    purpose: MutableSequence[Purpose] = proto.RepeatedField(
        proto.ENUM,
        number=10,
        enum=Purpose,
    )


class ListAddressGroupsRequest(proto.Message):
    r"""Request used with the ListAddressGroups method.

    Attributes:
        parent (str):
            Required. The project and location from which the
            AddressGroups should be listed, specified in the format
            ``projects/*/locations/{location}``.
        page_size (int):
            Maximum number of AddressGroups to return per
            call.
        page_token (str):
            The value returned by the last ``ListAddressGroupsResponse``
            Indicates that this is a continuation of a prior
            ``ListAddressGroups`` call, and that the system should
            return the next page of data.
        return_partial_success (bool):
            Optional. If true, allow partial responses
            for multi-regional Aggregated List requests.
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
    return_partial_success: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class ListAddressGroupsResponse(proto.Message):
    r"""Response returned by the ListAddressGroups method.

    Attributes:
        address_groups (MutableSequence[google.cloud.network_security_v1.types.AddressGroup]):
            List of AddressGroups resources.
        next_page_token (str):
            If there might be more results than those appearing in this
            response, then ``next_page_token`` is included. To get the
            next set of results, call this method again using the value
            of ``next_page_token`` as ``page_token``.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    address_groups: MutableSequence["AddressGroup"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AddressGroup",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetAddressGroupRequest(proto.Message):
    r"""Request used by the GetAddressGroup method.

    Attributes:
        name (str):
            Required. A name of the AddressGroup to get. Must be in the
            format ``projects/*/locations/{location}/addressGroups/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateAddressGroupRequest(proto.Message):
    r"""Request used by the CreateAddressGroup method.

    Attributes:
        parent (str):
            Required. The parent resource of the AddressGroup. Must be
            in the format ``projects/*/locations/{location}``.
        address_group_id (str):
            Required. Short name of the AddressGroup resource to be
            created. This value should be 1-63 characters long,
            containing only letters, numbers, hyphens, and underscores,
            and should not start with a number. E.g. "authz_policy".
        address_group (google.cloud.network_security_v1.types.AddressGroup):
            Required. AddressGroup resource to be
            created.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    address_group_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    address_group: "AddressGroup" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="AddressGroup",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateAddressGroupRequest(proto.Message):
    r"""Request used by the UpdateAddressGroup method.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the AddressGroup resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        address_group (google.cloud.network_security_v1.types.AddressGroup):
            Required. Updated AddressGroup resource.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    address_group: "AddressGroup" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="AddressGroup",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteAddressGroupRequest(proto.Message):
    r"""Request used by the DeleteAddressGroup method.

    Attributes:
        name (str):
            Required. A name of the AddressGroup to delete. Must be in
            the format
            ``projects/*/locations/{location}/addressGroups/*``.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AddAddressGroupItemsRequest(proto.Message):
    r"""Request used by the AddAddressGroupItems method.

    Attributes:
        address_group (str):
            Required. A name of the AddressGroup to add items to. Must
            be in the format
            ``projects|organization/*/locations/{location}/addressGroups/*``.
        items (MutableSequence[str]):
            Required. List of items to add.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    address_group: str = proto.Field(
        proto.STRING,
        number=1,
    )
    items: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class RemoveAddressGroupItemsRequest(proto.Message):
    r"""Request used by the RemoveAddressGroupItems method.

    Attributes:
        address_group (str):
            Required. A name of the AddressGroup to remove items from.
            Must be in the format
            ``projects|organization/*/locations/{location}/addressGroups/*``.
        items (MutableSequence[str]):
            Required. List of items to remove.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    address_group: str = proto.Field(
        proto.STRING,
        number=1,
    )
    items: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class CloneAddressGroupItemsRequest(proto.Message):
    r"""Request used by the CloneAddressGroupItems method.

    Attributes:
        address_group (str):
            Required. A name of the AddressGroup to clone items to. Must
            be in the format
            ``projects|organization/*/locations/{location}/addressGroups/*``.
        source_address_group (str):
            Required. Source address group to clone items
            from.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    address_group: str = proto.Field(
        proto.STRING,
        number=1,
    )
    source_address_group: str = proto.Field(
        proto.STRING,
        number=2,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListAddressGroupReferencesRequest(proto.Message):
    r"""Request used by the ListAddressGroupReferences method.

    Attributes:
        address_group (str):
            Required. A name of the AddressGroup to clone items to. Must
            be in the format
            ``projects|organization/*/locations/{location}/addressGroups/*``.
        page_size (int):
            The maximum number of references to return. If unspecified,
            server will pick an appropriate default. Server may return
            fewer items than requested. A caller should only rely on
            response's
            [next_page_token][google.cloud.networksecurity.v1.ListAddressGroupReferencesResponse.next_page_token]
            to determine if there are more AddressGroupUsers left to be
            queried.
        page_token (str):
            The next_page_token value returned from a previous List
            request, if any.
    """

    address_group: str = proto.Field(
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


class ListAddressGroupReferencesResponse(proto.Message):
    r"""Response of the ListAddressGroupReferences method.

    Attributes:
        address_group_references (MutableSequence[google.cloud.network_security_v1.types.ListAddressGroupReferencesResponse.AddressGroupReference]):
            A list of references that matches the
            specified filter in the request.
        next_page_token (str):
            If there might be more results than those appearing in this
            response, then ``next_page_token`` is included. To get the
            next set of results, call this method again using the value
            of ``next_page_token`` as ``page_token``.
    """

    class AddressGroupReference(proto.Message):
        r"""The Reference of AddressGroup.

        Attributes:
            firewall_policy (str):
                FirewallPolicy that is using the Address
                Group.
            security_policy (str):
                Cloud Armor SecurityPolicy that is using the
                Address Group.
            rule_priority (int):
                Rule priority of the FirewallPolicy that is
                using the Address Group.
        """

        firewall_policy: str = proto.Field(
            proto.STRING,
            number=1,
        )
        security_policy: str = proto.Field(
            proto.STRING,
            number=4,
        )
        rule_priority: int = proto.Field(
            proto.INT32,
            number=2,
        )

    @property
    def raw_page(self):
        return self

    address_group_references: MutableSequence[AddressGroupReference] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=AddressGroupReference,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
