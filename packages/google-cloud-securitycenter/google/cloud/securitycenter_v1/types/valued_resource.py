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
    package="google.cloud.securitycenter.v1",
    manifest={
        "ValuedResource",
        "ResourceValueConfigMetadata",
    },
)


class ValuedResource(proto.Message):
    r"""A resource that is determined to have value to a user's
    system

    Attributes:
        name (str):
            Valued resource name, for example, e.g.:
            ``organizations/123/simulations/456/valuedResources/789``
        resource (str):
            The `full resource
            name <https://cloud.google.com/apis/design/resource_names#full_resource_name>`__
            of the valued resource.
        resource_type (str):
            The `resource
            type <https://cloud.google.com/asset-inventory/docs/supported-asset-types>`__
            of the valued resource.
        display_name (str):
            Human-readable name of the valued resource.
        resource_value (google.cloud.securitycenter_v1.types.ValuedResource.ResourceValue):
            How valuable this resource is.
        exposed_score (float):
            Exposed score for this valued resource. A
            value of 0 means no exposure was detected
            exposure.
        resource_value_configs_used (MutableSequence[google.cloud.securitycenter_v1.types.ResourceValueConfigMetadata]):
            List of resource value configurations'
            metadata used to determine the value of this
            resource. Maximum of 100.
    """

    class ResourceValue(proto.Enum):
        r"""How valuable the resource is.

        Values:
            RESOURCE_VALUE_UNSPECIFIED (0):
                The resource value isn't specified.
            RESOURCE_VALUE_LOW (1):
                This is a low-value resource.
            RESOURCE_VALUE_MEDIUM (2):
                This is a medium-value resource.
            RESOURCE_VALUE_HIGH (3):
                This is a high-value resource.
        """

        RESOURCE_VALUE_UNSPECIFIED = 0
        RESOURCE_VALUE_LOW = 1
        RESOURCE_VALUE_MEDIUM = 2
        RESOURCE_VALUE_HIGH = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    resource: str = proto.Field(
        proto.STRING,
        number=2,
    )
    resource_type: str = proto.Field(
        proto.STRING,
        number=3,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    resource_value: ResourceValue = proto.Field(
        proto.ENUM,
        number=5,
        enum=ResourceValue,
    )
    exposed_score: float = proto.Field(
        proto.DOUBLE,
        number=6,
    )
    resource_value_configs_used: MutableSequence["ResourceValueConfigMetadata"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=7,
            message="ResourceValueConfigMetadata",
        )
    )


class ResourceValueConfigMetadata(proto.Message):
    r"""Metadata about a ResourceValueConfig. For example, id and
    name.

    Attributes:
        name (str):
            Resource value config name
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
