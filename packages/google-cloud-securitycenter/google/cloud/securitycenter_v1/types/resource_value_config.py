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

from google.cloud.securitycenter_v1.types import resource

__protobuf__ = proto.module(
    package="google.cloud.securitycenter.v1",
    manifest={
        "ResourceValue",
        "ResourceValueConfig",
    },
)


class ResourceValue(proto.Enum):
    r"""Value enum to map to a resource

    Values:
        RESOURCE_VALUE_UNSPECIFIED (0):
            Unspecific value
        HIGH (1):
            High resource value
        MEDIUM (2):
            Medium resource value
        LOW (3):
            Low resource value
        NONE (4):
            No resource value, e.g. ignore these
            resources
    """

    RESOURCE_VALUE_UNSPECIFIED = 0
    HIGH = 1
    MEDIUM = 2
    LOW = 3
    NONE = 4


class ResourceValueConfig(proto.Message):
    r"""A resource value configuration (RVC) is a mapping
    configuration of user's resources to resource values. Used in
    Attack path simulations.

    Attributes:
        name (str):
            Name for the resource value configuration
        resource_value (google.cloud.securitycenter_v1.types.ResourceValue):
            Required. Resource value level this
            expression represents
        tag_values (MutableSequence[str]):
            Required. Tag values combined with ``AND`` to check against.
            Values in the form "tagValues/123" Example:
            ``[ "tagValues/123", "tagValues/456", "tagValues/789" ]``
            https://cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing
        resource_type (str):
            Apply resource_value only to resources that match
            resource_type. resource_type will be checked with ``AND`` of
            other resources. For example,
            "storage.googleapis.com/Bucket" with resource_value "HIGH"
            will apply "HIGH" value only to
            "storage.googleapis.com/Bucket" resources.
        scope (str):
            Project or folder to scope this configuration to. For
            example, "project/456" would apply this configuration only
            to resources in "project/456" scope will be checked with
            ``AND`` of other resources.
        resource_labels_selector (MutableMapping[str, str]):
            List of resource labels to search for, evaluated with
            ``AND``. For example,
            ``"resource_labels_selector": {"key": "value", "env": "prod"}``
            will match resources with labels "key": "value" ``AND``
            "env": "prod"
            https://cloud.google.com/resource-manager/docs/creating-managing-labels
        description (str):
            Description of the resource value
            configuration.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp this resource value
            configuration was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp this resource value
            configuration was last updated.
        cloud_provider (google.cloud.securitycenter_v1.types.CloudProvider):
            Cloud provider this configuration applies to
        sensitive_data_protection_mapping (google.cloud.securitycenter_v1.types.ResourceValueConfig.SensitiveDataProtectionMapping):
            A mapping of the sensitivity on Sensitive Data Protection
            finding to resource values. This mapping can only be used in
            combination with a resource_type that is related to
            BigQuery, e.g. "bigquery.googleapis.com/Dataset".
    """

    class SensitiveDataProtectionMapping(proto.Message):
        r"""Resource value mapping for Sensitive Data Protection findings. If
        any of these mappings have a resource value that is not unspecified,
        the resource_value field will be ignored when reading this
        configuration.

        Attributes:
            high_sensitivity_mapping (google.cloud.securitycenter_v1.types.ResourceValue):
                Resource value mapping for high-sensitivity
                Sensitive Data Protection findings
            medium_sensitivity_mapping (google.cloud.securitycenter_v1.types.ResourceValue):
                Resource value mapping for medium-sensitivity
                Sensitive Data Protection findings
        """

        high_sensitivity_mapping: "ResourceValue" = proto.Field(
            proto.ENUM,
            number=1,
            enum="ResourceValue",
        )
        medium_sensitivity_mapping: "ResourceValue" = proto.Field(
            proto.ENUM,
            number=2,
            enum="ResourceValue",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    resource_value: "ResourceValue" = proto.Field(
        proto.ENUM,
        number=2,
        enum="ResourceValue",
    )
    tag_values: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    resource_type: str = proto.Field(
        proto.STRING,
        number=4,
    )
    scope: str = proto.Field(
        proto.STRING,
        number=5,
    )
    resource_labels_selector: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    description: str = proto.Field(
        proto.STRING,
        number=7,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    cloud_provider: resource.CloudProvider = proto.Field(
        proto.ENUM,
        number=10,
        enum=resource.CloudProvider,
    )
    sensitive_data_protection_mapping: SensitiveDataProtectionMapping = proto.Field(
        proto.MESSAGE,
        number=11,
        message=SensitiveDataProtectionMapping,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
