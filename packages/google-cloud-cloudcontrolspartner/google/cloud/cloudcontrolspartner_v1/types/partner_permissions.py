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
    package="google.cloud.cloudcontrolspartner.v1",
    manifest={
        "PartnerPermissions",
        "GetPartnerPermissionsRequest",
    },
)


class PartnerPermissions(proto.Message):
    r"""The permissions granted to the partner for a workload

    Attributes:
        name (str):
            Identifier. Format:
            ``organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}/partnerPermissions``
        partner_permissions (MutableSequence[google.cloud.cloudcontrolspartner_v1.types.PartnerPermissions.Permission]):
            The partner permissions granted for the
            workload
    """

    class Permission(proto.Enum):
        r"""

        Values:
            PERMISSION_UNSPECIFIED (0):
                Unspecified partner permission
            ACCESS_TRANSPARENCY_AND_EMERGENCY_ACCESS_LOGS (1):
                Permission for Access Transparency and
                emergency logs
            ASSURED_WORKLOADS_MONITORING (2):
                Permission for Assured Workloads monitoring
                violations
            ACCESS_APPROVAL_REQUESTS (3):
                Permission for Access Approval requests
            ASSURED_WORKLOADS_EKM_CONNECTION_STATUS (4):
                Permission for External Key Manager
                connection status
            ACCESS_TRANSPARENCY_LOGS_SUPPORT_CASE_VIEWER (5):
                Permission for support case details for
                Access Transparency log entries
        """

        PERMISSION_UNSPECIFIED = 0
        ACCESS_TRANSPARENCY_AND_EMERGENCY_ACCESS_LOGS = 1
        ASSURED_WORKLOADS_MONITORING = 2
        ACCESS_APPROVAL_REQUESTS = 3
        ASSURED_WORKLOADS_EKM_CONNECTION_STATUS = 4
        ACCESS_TRANSPARENCY_LOGS_SUPPORT_CASE_VIEWER = 5

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    partner_permissions: MutableSequence[Permission] = proto.RepeatedField(
        proto.ENUM,
        number=2,
        enum=Permission,
    )


class GetPartnerPermissionsRequest(proto.Message):
    r"""Request for getting the partner permissions granted for a
    workload

    Attributes:
        name (str):
            Required. Name of the resource to get in the format:
            ``organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}/partnerPermissions``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
