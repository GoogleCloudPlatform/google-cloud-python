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
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.devtools.artifactregistry.v1",
    manifest={
        "VPCSCConfig",
        "GetVPCSCConfigRequest",
        "UpdateVPCSCConfigRequest",
    },
)


class VPCSCConfig(proto.Message):
    r"""The Artifact Registry VPC SC config that apply to a Project.

    Attributes:
        name (str):
            The name of the project's VPC SC Config.

            Always of the form:

            projects/{projectID}/locations/{location}/vpcscConfig

            In update request: never set
            In response: always set
        vpcsc_policy (google.cloud.artifactregistry_v1.types.VPCSCConfig.VPCSCPolicy):
            The project per location VPC SC policy that
            defines the VPC SC behavior for the Remote
            Repository (Allow/Deny).
    """

    class VPCSCPolicy(proto.Enum):
        r"""VPCSCPolicy is the VPC SC policy for project and location.

        Values:
            VPCSC_POLICY_UNSPECIFIED (0):
                VPCSC_POLICY_UNSPECIFIED - the VPS SC policy is not defined.
                When VPS SC policy is not defined - the Service will use the
                default behavior (VPCSC_DENY).
            DENY (1):
                VPCSC_DENY - repository will block the requests to the
                Upstreams for the Remote Repositories if the resource is in
                the perimeter.
            ALLOW (2):
                VPCSC_ALLOW - repository will allow the requests to the
                Upstreams for the Remote Repositories if the resource is in
                the perimeter.
        """

        VPCSC_POLICY_UNSPECIFIED = 0
        DENY = 1
        ALLOW = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    vpcsc_policy: VPCSCPolicy = proto.Field(
        proto.ENUM,
        number=2,
        enum=VPCSCPolicy,
    )


class GetVPCSCConfigRequest(proto.Message):
    r"""Gets the VPC SC config for a project.

    Attributes:
        name (str):
            Required. The name of the VPCSCConfig
            resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateVPCSCConfigRequest(proto.Message):
    r"""Sets the VPCSC config of the project.

    Attributes:
        vpcsc_config (google.cloud.artifactregistry_v1.types.VPCSCConfig):
            The project config.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Field mask to support partial updates.
    """

    vpcsc_config: "VPCSCConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="VPCSCConfig",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
