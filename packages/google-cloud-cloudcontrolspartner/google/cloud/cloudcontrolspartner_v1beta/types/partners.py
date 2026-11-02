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
    package="google.cloud.cloudcontrolspartner.v1beta",
    manifest={
        "Partner",
        "GetPartnerRequest",
        "Sku",
        "EkmMetadata",
    },
)


class Partner(proto.Message):
    r"""Message describing Partner resource

    Attributes:
        name (str):
            Identifier. The resource name of the partner. Format:
            ``organizations/{organization}/locations/{location}/partner``
            Example:
            "organizations/123456/locations/us-central1/partner".
        skus (MutableSequence[google.cloud.cloudcontrolspartner_v1beta.types.Sku]):
            List of SKUs the partner is offering
        ekm_solutions (MutableSequence[google.cloud.cloudcontrolspartner_v1beta.types.EkmMetadata]):
            List of Google Cloud supported EKM partners
            supported by the partner
        operated_cloud_regions (MutableSequence[str]):
            List of Google Cloud regions that the partner
            sells services to customers. Valid Google Cloud
            regions found here:

            https://cloud.google.com/compute/docs/regions-zones
        partner_project_id (str):
            Google Cloud project ID in the partner's
            Google Cloud organization for receiving enhanced
            Logs for Partners.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time the resource was created
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last time the resource was
            updated
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    skus: MutableSequence["Sku"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="Sku",
    )
    ekm_solutions: MutableSequence["EkmMetadata"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="EkmMetadata",
    )
    operated_cloud_regions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    partner_project_id: str = proto.Field(
        proto.STRING,
        number=7,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )


class GetPartnerRequest(proto.Message):
    r"""Message for getting a Partner

    Attributes:
        name (str):
            Required. Format:
            ``organizations/{organization}/locations/{location}/partner``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Sku(proto.Message):
    r"""Represents the SKU a partner owns inside Google Cloud to sell
    to customers.

    Attributes:
        id (str):
            Argentum product SKU, that is associated with
            the partner offerings to customers used by
            Syntro for billing purposes. SKUs can represent
            resold Google products or support services.
        display_name (str):
            Display name of the product identified by the
            SKU. A partner may want to show partner branded
            names for their offerings such as local
            sovereign cloud solutions.
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class EkmMetadata(proto.Message):
    r"""Holds information needed by Mudbray to use partner EKMs for
    workloads.

    Attributes:
        ekm_solution (google.cloud.cloudcontrolspartner_v1beta.types.EkmMetadata.EkmSolution):
            The Cloud EKM partner.
        ekm_endpoint_uri (str):
            Endpoint for sending requests to the EKM for
            key provisioning during Assured Workload
            creation.
    """

    class EkmSolution(proto.Enum):
        r"""Represents Google Cloud supported external key management partners
        `Google Cloud EKM partners
        docs <https://cloud.google.com/kms/docs/ekm#supported_partners>`__.

        Values:
            EKM_SOLUTION_UNSPECIFIED (0):
                Unspecified EKM solution
            FORTANIX (1):
                EKM Partner Fortanix
            FUTUREX (2):
                EKM Partner FutureX
            THALES (3):
                EKM Partner Thales
            VIRTRU (4):
                This enum value is never used.
        """

        EKM_SOLUTION_UNSPECIFIED = 0
        FORTANIX = 1
        FUTUREX = 2
        THALES = 3
        VIRTRU = 4

    ekm_solution: EkmSolution = proto.Field(
        proto.ENUM,
        number=1,
        enum=EkmSolution,
    )
    ekm_endpoint_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
