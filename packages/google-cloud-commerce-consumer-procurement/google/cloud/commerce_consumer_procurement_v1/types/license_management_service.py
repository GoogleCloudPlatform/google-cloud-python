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
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.commerce.consumer.procurement.v1",
    manifest={
        "AssignmentProtocol",
        "LicensePool",
        "GetLicensePoolRequest",
        "UpdateLicensePoolRequest",
        "AssignRequest",
        "AssignResponse",
        "UnassignRequest",
        "UnassignResponse",
        "EnumerateLicensedUsersRequest",
        "LicensedUser",
        "EnumerateLicensedUsersResponse",
    },
)


class AssignmentProtocol(proto.Message):
    r"""Assignment protocol for a license pool.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        manual_assignment_type (google.cloud.commerce_consumer_procurement_v1.types.AssignmentProtocol.ManualAssignmentType):
            Allow manual assignments triggered by
            administrative operations only.

            This field is a member of `oneof`_ ``assignment_type``.
        auto_assignment_type (google.cloud.commerce_consumer_procurement_v1.types.AssignmentProtocol.AutoAssignmentType):
            Allow automatic assignments triggered by data
            plane operations.

            This field is a member of `oneof`_ ``assignment_type``.
    """

    class ManualAssignmentType(proto.Message):
        r"""Allow manual assignments triggered by administrative
        operations only.

        """

    class AutoAssignmentType(proto.Message):
        r"""Configuration for automatic assignments handled by data plane
        operations.

        Attributes:
            inactive_license_ttl (google.protobuf.duration_pb2.Duration):
                Optional. The time to live for an inactive
                license. After this time has passed, the license
                will be automatically unassigned from the user.
                Must be at least 7 days, if set. If unset, the
                license will never expire.
        """

        inactive_license_ttl: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=1,
            message=duration_pb2.Duration,
        )

    manual_assignment_type: ManualAssignmentType = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="assignment_type",
        message=ManualAssignmentType,
    )
    auto_assignment_type: AutoAssignmentType = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="assignment_type",
        message=AutoAssignmentType,
    )


class LicensePool(proto.Message):
    r"""A license pool represents a pool of licenses that can be
    assigned to users.

    Attributes:
        name (str):
            Identifier. Format:
            ``billingAccounts/{billing_account}/orders/{order}/licensePool``
        license_assignment_protocol (google.cloud.commerce_consumer_procurement_v1.types.AssignmentProtocol):
            Required. Assignment protocol for the license
            pool.
        available_license_count (int):
            Output only. Licenses count that are
            available to be assigned.
        total_license_count (int):
            Output only. Total number of licenses in the
            pool.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    license_assignment_protocol: "AssignmentProtocol" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="AssignmentProtocol",
    )
    available_license_count: int = proto.Field(
        proto.INT32,
        number=3,
    )
    total_license_count: int = proto.Field(
        proto.INT32,
        number=4,
    )


class GetLicensePoolRequest(proto.Message):
    r"""Request message for getting a license pool.

    Attributes:
        name (str):
            Required. The name of the license pool to get. Format:
            ``billingAccounts/{billing_account}/orders/{order}/licensePool``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateLicensePoolRequest(proto.Message):
    r"""Request message for updating a license pool.

    Attributes:
        license_pool (google.cloud.commerce_consumer_procurement_v1.types.LicensePool):
            Required. The license pool to update.

            The license pool's name field is used to identify the
            license pool to update. Format:
            ``billingAccounts/{billing_account}/orders/{order}/licensePool``.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to update.
    """

    license_pool: "LicensePool" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="LicensePool",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class AssignRequest(proto.Message):
    r"""Request message for
    [LicenseManagementService.Assign][google.cloud.commerce.consumer.procurement.v1.LicenseManagementService.Assign].

    Attributes:
        parent (str):
            Required. License pool name.
        usernames (MutableSequence[str]):
            Required. Username. Format: ``name@domain.com``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    usernames: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class AssignResponse(proto.Message):
    r"""Response message for
    [LicenseManagementService.Assign][google.cloud.commerce.consumer.procurement.v1.LicenseManagementService.Assign].

    """


class UnassignRequest(proto.Message):
    r"""Request message for
    [LicenseManagementService.Unassign][google.cloud.commerce.consumer.procurement.v1.LicenseManagementService.Unassign].

    Attributes:
        parent (str):
            Required. License pool name.
        usernames (MutableSequence[str]):
            Required. Username. Format: ``name@domain.com``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    usernames: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class UnassignResponse(proto.Message):
    r"""Response message for
    [LicenseManagementService.Unassign][google.cloud.commerce.consumer.procurement.v1.LicenseManagementService.Unassign].

    """


class EnumerateLicensedUsersRequest(proto.Message):
    r"""Request message for
    [LicenseManagementService.EnumerateLicensedUsers][google.cloud.commerce.consumer.procurement.v1.LicenseManagementService.EnumerateLicensedUsers].

    Attributes:
        parent (str):
            Required. License pool name.
        page_size (int):
            Optional. The maximum number of users to
            return. The service may return fewer than this
            value.
        page_token (str):
            Optional. A page token, received from a previous
            ``EnumerateLicensedUsers`` call. Provide this to retrieve
            the subsequent page.
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


class LicensedUser(proto.Message):
    r"""A licensed user.

    Attributes:
        username (str):
            Username. Format: ``name@domain.com``.
        assign_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the license was
            assigned.
        recent_usage_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the license was
            recently used. This may not be the most recent
            usage time, and will be updated regularly
            (within 24 hours).
    """

    username: str = proto.Field(
        proto.STRING,
        number=1,
    )
    assign_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    recent_usage_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


class EnumerateLicensedUsersResponse(proto.Message):
    r"""Response message for
    [LicenseManagementService.EnumerateLicensedUsers][google.cloud.commerce.consumer.procurement.v1.LicenseManagementService.EnumerateLicensedUsers].

    Attributes:
        licensed_users (MutableSequence[google.cloud.commerce_consumer_procurement_v1.types.LicensedUser]):
            The list of licensed users.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    licensed_users: MutableSequence["LicensedUser"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="LicensedUser",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
