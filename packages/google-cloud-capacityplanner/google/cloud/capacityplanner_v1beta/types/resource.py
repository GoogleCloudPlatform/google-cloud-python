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
    package="google.cloud.capacityplanner.v1beta",
    manifest={
        "Unit",
        "ResourceContainer",
        "ResourceIdKey",
        "ResourceIdentifier",
        "ResourceAttribute",
        "ResourceValue",
        "Value",
    },
)


class Unit(proto.Enum):
    r"""

    Values:
        UNIT_UNSPECIFIED (0):
            No description available.
        UNIT_COUNT (1):
            No description available.
        KB (2):
            Kilobytes (10^3 bytes)
        GB (3):
            Gigabytes (10^9 bytes)
        TB (4):
            Terabytes (10^12 bytes)
        MIB (17):
            Mebibytes (2^20 bytes)
        GIB (5):
            Gibibytes (2^30 bytes)
        TIB (6):
            Tebibytes (2^40 bytes)
        QPS (7):
            Queries per second
        MB (8):
            Megabytes (10^6 bytes)
        PIB (9):
            Pebibytes (2^50 bytes)
        TBPS (10):
            Terabits (10^12 bits) per second
        GBPS_BITS (11):
            No description available.
        GIB_BITS (12):
            No description available.
        MBPS_BITS (13):
            No description available.
        MBPS_BYTES (14):
            No description available.
        TBPS_BITS (15):
            No description available.
        TBPS_BYTES (16):
            No description available.
        KOPS (18):
            No description available.
    """

    UNIT_UNSPECIFIED = 0
    UNIT_COUNT = 1
    KB = 2
    GB = 3
    TB = 4
    MIB = 17
    GIB = 5
    TIB = 6
    QPS = 7
    MB = 8
    PIB = 9
    TBPS = 10
    GBPS_BITS = 11
    GIB_BITS = 12
    MBPS_BITS = 13
    MBPS_BYTES = 14
    TBPS_BITS = 15
    TBPS_BYTES = 16
    KOPS = 18


class ResourceContainer(proto.Message):
    r"""The resource container of Google Cloud Platform hierarchy
    such as a project.

    Attributes:
        type_ (google.cloud.capacityplanner_v1beta.types.ResourceContainer.Type):

        id (str):
            Required. Identifier of the resource
            container. For example, project number for
            project type.
    """

    class Type(proto.Enum):
        r"""

        Values:
            TYPE_UNSPECIFIED (0):
                No description available.
            PROJECT (1):
                No description available.
            FOLDER (2):
                No description available.
            ORG (3):
                No description available.
        """

        TYPE_UNSPECIFIED = 0
        PROJECT = 1
        FOLDER = 2
        ORG = 3

    type_: Type = proto.Field(
        proto.ENUM,
        number=1,
        enum=Type,
    )
    id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ResourceIdKey(proto.Message):
    r"""The id for a Google Cloud Platform resource key.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        resource_code (str):
            Required. resource_code for the resource. eg: gce-ram,
            gce-vcpus, gce-gpu, gce-tpu, gce-vm, gce-persistent-disk,
            gce-local-ssd.

            This field is a member of `oneof`_ ``demand_fields``.
        resource_id (google.cloud.capacityplanner_v1beta.types.ResourceIdentifier):
            Required. Id of the resource.
    """

    resource_code: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="demand_fields",
    )
    resource_id: "ResourceIdentifier" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ResourceIdentifier",
    )


class ResourceIdentifier(proto.Message):
    r"""The identifier for a Google Cloud Platform resource.

    Attributes:
        service_name (str):

        resource_name (str):

        resource_attributes (MutableSequence[google.cloud.capacityplanner_v1beta.types.ResourceAttribute]):

    """

    service_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    resource_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    resource_attributes: MutableSequence["ResourceAttribute"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="ResourceAttribute",
    )


class ResourceAttribute(proto.Message):
    r"""An attribute of a Google Cloud Platform resource.

    Attributes:
        key (str):

        value (google.cloud.capacityplanner_v1beta.types.ResourceValue):

    """

    key: str = proto.Field(
        proto.STRING,
        number=1,
    )
    value: "ResourceValue" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ResourceValue",
    )


class ResourceValue(proto.Message):
    r"""

    Attributes:
        unit (google.cloud.capacityplanner_v1beta.types.Unit):

        value (google.cloud.capacityplanner_v1beta.types.Value):

    """

    unit: "Unit" = proto.Field(
        proto.ENUM,
        number=1,
        enum="Unit",
    )
    value: "Value" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Value",
    )


class Value(proto.Message):
    r"""

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        int64_value (int):

            This field is a member of `oneof`_ ``value``.
        string_value (str):

            This field is a member of `oneof`_ ``value``.
        double_value (float):

            This field is a member of `oneof`_ ``value``.
        bool_value (bool):

            This field is a member of `oneof`_ ``value``.
    """

    int64_value: int = proto.Field(
        proto.INT64,
        number=1,
        oneof="value",
    )
    string_value: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="value",
    )
    double_value: float = proto.Field(
        proto.DOUBLE,
        number=3,
        oneof="value",
    )
    bool_value: bool = proto.Field(
        proto.BOOL,
        number=4,
        oneof="value",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
