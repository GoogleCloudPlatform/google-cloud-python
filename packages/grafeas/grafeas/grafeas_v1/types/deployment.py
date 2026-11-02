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
    package="grafeas.v1",
    manifest={
        "DeploymentNote",
        "DeploymentOccurrence",
    },
)


class DeploymentNote(proto.Message):
    r"""An artifact that can be deployed in some runtime.

    Attributes:
        resource_uri (MutableSequence[str]):
            Required. Resource URI for the artifact being
            deployed.
    """

    resource_uri: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class DeploymentOccurrence(proto.Message):
    r"""The period during which some deployable was active in a
    runtime.

    Attributes:
        user_email (str):
            Identity of the user that triggered this
            deployment.
        deploy_time (google.protobuf.timestamp_pb2.Timestamp):
            Required. Beginning of the lifetime of this
            deployment.
        undeploy_time (google.protobuf.timestamp_pb2.Timestamp):
            End of the lifetime of this deployment.
        config (str):
            Configuration used to create this deployment.
        address (str):
            Address of the runtime element hosting this
            deployment.
        resource_uri (MutableSequence[str]):
            Output only. Resource URI for the artifact
            being deployed taken from the deployable field
            with the same name.
        platform (grafeas.grafeas_v1.types.DeploymentOccurrence.Platform):
            Platform hosting this deployment.
    """

    class Platform(proto.Enum):
        r"""Types of platforms.

        Values:
            PLATFORM_UNSPECIFIED (0):
                Unknown.
            GKE (1):
                Google Container Engine.
            FLEX (2):
                Google App Engine: Flexible Environment.
            CUSTOM (3):
                Custom user-defined platform.
        """

        PLATFORM_UNSPECIFIED = 0
        GKE = 1
        FLEX = 2
        CUSTOM = 3

    user_email: str = proto.Field(
        proto.STRING,
        number=1,
    )
    deploy_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    undeploy_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    config: str = proto.Field(
        proto.STRING,
        number=4,
    )
    address: str = proto.Field(
        proto.STRING,
        number=5,
    )
    resource_uri: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    platform: Platform = proto.Field(
        proto.ENUM,
        number=7,
        enum=Platform,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
