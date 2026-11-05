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
    package="google.cloud.designcenter.v1",
    manifest={
        "UnregisteredResource",
        "DeployedResource",
    },
)


class UnregisteredResource(proto.Message):
    r"""UnregisteredResource represents a GCP resource that failed to
    register and apphub was not able to discover.

    Attributes:
        deployed_resource (google.cloud.designcenter_v1.types.DeployedResource):
            Output only. The deployed GCP resource that
            failed to register.
        reason (str):
            Output only. The reason for the failure of
            registration.
    """

    deployed_resource: "DeployedResource" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="DeployedResource",
    )
    reason: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeployedResource(proto.Message):
    r"""DeployedResource represents a single deployed GCP resource.

    Attributes:
        resource_id (str):
            Required. The full resource name of the
            deployed GCP resource. Example:
            projects/my-project/locations/us-central1-a/instances/my-instance
        project (str):
            Optional. The project ID of the deployed
            resource.
        location (str):
            Optional. The location of the deployed
            resource.
    """

    resource_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
