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
    package="google.cloud.ces.v1beta",
    manifest={
        "SecuritySettings",
        "EndpointControlPolicy",
    },
)


class SecuritySettings(proto.Message):
    r"""Project/Location level security settings for CES.

    Attributes:
        name (str):
            Identifier. The unique identifier of the security settings.
            Format:
            ``projects/{project}/locations/{location}/securitySettings``
        endpoint_control_policy (google.cloud.ces_v1beta.types.EndpointControlPolicy):
            Optional. Endpoint control related settings.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create time of the security
            settings.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Last update time of the security
            settings.
        etag (str):
            Output only. Etag of the security settings.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    endpoint_control_policy: "EndpointControlPolicy" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="EndpointControlPolicy",
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
    etag: str = proto.Field(
        proto.STRING,
        number=5,
    )


class EndpointControlPolicy(proto.Message):
    r"""Defines project/location level endpoint control policy.

    Attributes:
        enforcement_scope (google.cloud.ces_v1beta.types.EndpointControlPolicy.EnforcementScope):
            Optional. The scope in which this policy's allowed_origins
            list is enforced.
        allowed_origins (MutableSequence[str]):
            Optional. The allowed HTTP(s) origins that tools in the App
            are able to directly call. The enforcement depends on the
            value of enforcement_scope and the VPC-SC status of the
            project. If a port number is not provided, all ports will be
            allowed. Otherwise, the port number must match exactly. For
            example, "https://example.com" will match
            "https://example.com:443" and any other port.
            "https://example.com:443" will only match
            "https://example.com:443".
    """

    class EnforcementScope(proto.Enum):
        r"""Defines the scope in which this policy's allowed_origins list is
        enforced.

        Values:
            ENFORCEMENT_SCOPE_UNSPECIFIED (0):
                Unspecified. This policy will be treated as VPCSC_ONLY.
            VPCSC_ONLY (1):
                This policy applies only when VPC-SC is
                active.
            ALWAYS (2):
                This policy ALWAYS applies, regardless of
                VPC-SC status.
        """

        ENFORCEMENT_SCOPE_UNSPECIFIED = 0
        VPCSC_ONLY = 1
        ALWAYS = 2

    enforcement_scope: EnforcementScope = proto.Field(
        proto.ENUM,
        number=1,
        enum=EnforcementScope,
    )
    allowed_origins: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
