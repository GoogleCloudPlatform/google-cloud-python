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
    package="google.cloud.netapp.v1",
    manifest={
        "ServiceLevel",
        "FlexPerformance",
        "EncryptionType",
        "DirectoryServiceType",
        "StoragePoolType",
        "ScaleType",
        "HybridReplicationSchedule",
        "QosType",
        "OsType",
        "LocationMetadata",
        "UserCommands",
    },
)


class ServiceLevel(proto.Enum):
    r"""The service level of a storage pool and its volumes.

    Values:
        SERVICE_LEVEL_UNSPECIFIED (0):
            Unspecified service level.
        PREMIUM (1):
            Premium service level.
        EXTREME (2):
            Extreme service level.
        STANDARD (3):
            Standard service level.
        FLEX (4):
            Flex service level.
    """

    SERVICE_LEVEL_UNSPECIFIED = 0
    PREMIUM = 1
    EXTREME = 2
    STANDARD = 3
    FLEX = 4


class FlexPerformance(proto.Enum):
    r"""Flex Storage Pool performance.

    Values:
        FLEX_PERFORMANCE_UNSPECIFIED (0):
            Unspecified flex performance.
        FLEX_PERFORMANCE_DEFAULT (1):
            Flex Storage Pool with default performance.
        FLEX_PERFORMANCE_CUSTOM (2):
            Flex Storage Pool with custom performance.
    """

    FLEX_PERFORMANCE_UNSPECIFIED = 0
    FLEX_PERFORMANCE_DEFAULT = 1
    FLEX_PERFORMANCE_CUSTOM = 2


class EncryptionType(proto.Enum):
    r"""The volume encryption key source.

    Values:
        ENCRYPTION_TYPE_UNSPECIFIED (0):
            The source of the encryption key is not
            specified.
        SERVICE_MANAGED (1):
            Google managed encryption key.
        CLOUD_KMS (2):
            Customer managed encryption key, which is
            stored in KMS.
    """

    ENCRYPTION_TYPE_UNSPECIFIED = 0
    SERVICE_MANAGED = 1
    CLOUD_KMS = 2


class DirectoryServiceType(proto.Enum):
    r"""Type of directory service

    Values:
        DIRECTORY_SERVICE_TYPE_UNSPECIFIED (0):
            Directory service type is not specified.
        ACTIVE_DIRECTORY (1):
            Active directory policy attached to the
            storage pool.
    """

    DIRECTORY_SERVICE_TYPE_UNSPECIFIED = 0
    ACTIVE_DIRECTORY = 1


class StoragePoolType(proto.Enum):
    r"""Type of storage pool

    Values:
        STORAGE_POOL_TYPE_UNSPECIFIED (0):
            Storage pool type is not specified.
        FILE (1):
            Storage pool type is file.
        UNIFIED (2):
            Storage pool type is unified.
    """

    STORAGE_POOL_TYPE_UNSPECIFIED = 0
    FILE = 1
    UNIFIED = 2


class ScaleType(proto.Enum):
    r"""Defines the scale-type of a UNIFIED Storage Pool.

    Values:
        SCALE_TYPE_UNSPECIFIED (0):
            Unspecified scale type.
        SCALE_TYPE_DEFAULT (1):
            Represents standard capacity and performance
            scale-type. Suitable for general purpose
            workloads.
        SCALE_TYPE_SCALEOUT (2):
            Represents higher capacity and performance
            scale-type. Suitable for more demanding
            workloads.
    """

    SCALE_TYPE_UNSPECIFIED = 0
    SCALE_TYPE_DEFAULT = 1
    SCALE_TYPE_SCALEOUT = 2


class HybridReplicationSchedule(proto.Enum):
    r"""Schedule for Hybrid Replication.
    New enum values may be added in future to support different
    frequency of replication.

    Values:
        HYBRID_REPLICATION_SCHEDULE_UNSPECIFIED (0):
            Unspecified HybridReplicationSchedule
        EVERY_10_MINUTES (1):
            Replication happens once every 10 minutes.
        HOURLY (2):
            Replication happens once every hour.
        DAILY (3):
            Replication happens once every day.
    """

    HYBRID_REPLICATION_SCHEDULE_UNSPECIFIED = 0
    EVERY_10_MINUTES = 1
    HOURLY = 2
    DAILY = 3


class QosType(proto.Enum):
    r"""QoS (Quality of Service) Types of the storage pool

    Values:
        QOS_TYPE_UNSPECIFIED (0):
            Unspecified QoS Type
        AUTO (1):
            QoS Type is Auto
        MANUAL (2):
            QoS Type is Manual
    """

    QOS_TYPE_UNSPECIFIED = 0
    AUTO = 1
    MANUAL = 2


class OsType(proto.Enum):
    r"""OS types for the host group

    Values:
        OS_TYPE_UNSPECIFIED (0):
            Unspecified OS Type
        LINUX (1):
            OS Type is Linux
        WINDOWS (2):
            OS Type is Windows
        ESXI (3):
            OS Type is VMware ESXi
    """

    OS_TYPE_UNSPECIFIED = 0
    LINUX = 1
    WINDOWS = 2
    ESXI = 3


class LocationMetadata(proto.Message):
    r"""Metadata for a given
    [google.cloud.location.Location][google.cloud.location.Location].

    Attributes:
        supported_service_levels (MutableSequence[google.cloud.netapp_v1.types.ServiceLevel]):
            Output only. Supported service levels in a
            location.
        supported_flex_performance (MutableSequence[google.cloud.netapp_v1.types.FlexPerformance]):
            Output only. Supported flex performance in a
            location.
        has_vcp (bool):
            Output only. Indicates if the location has
            VCP support.
        has_ontap_proxy (bool):
            Output only. Indicates if the location has
            ONTAP Proxy support.
        flex_performance_tier (google.cloud.netapp_v1.types.LocationMetadata.FlexPerformanceTier):
            Output only. Indicates the flex performance
            tier of this location.
    """

    class FlexPerformanceTier(proto.Enum):
        r"""The flex performance tier of this location.

        Values:
            FLEX_PERFORMANCE_TIER_UNSPECIFIED (0):
                Unspecified flex performance tier.
            LIMITED (1):
                Flex performance tier is limited.
        """

        FLEX_PERFORMANCE_TIER_UNSPECIFIED = 0
        LIMITED = 1

    supported_service_levels: MutableSequence["ServiceLevel"] = proto.RepeatedField(
        proto.ENUM,
        number=1,
        enum="ServiceLevel",
    )
    supported_flex_performance: MutableSequence["FlexPerformance"] = (
        proto.RepeatedField(
            proto.ENUM,
            number=2,
            enum="FlexPerformance",
        )
    )
    has_vcp: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    has_ontap_proxy: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    flex_performance_tier: FlexPerformanceTier = proto.Field(
        proto.ENUM,
        number=5,
        enum=FlexPerformanceTier,
    )


class UserCommands(proto.Message):
    r"""UserCommands contains the commands to be executed by the
    customer.

    Attributes:
        commands (MutableSequence[str]):
            Output only. List of commands to be executed
            by the customer.
    """

    commands: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
