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
    package="google.cloud.rapidmigrationassessment.v1",
    manifest={
        "GuestOsScan",
        "VSphereScan",
        "Collector",
        "Annotation",
    },
)


class GuestOsScan(proto.Message):
    r"""Message describing a MC Source of type Guest OS Scan.

    Attributes:
        core_source (str):
            reference to the corresponding Guest OS Scan
            in MC Source.
    """

    core_source: str = proto.Field(
        proto.STRING,
        number=1,
    )


class VSphereScan(proto.Message):
    r"""Message describing a MC Source of type VSphere Scan.

    Attributes:
        core_source (str):
            reference to the corresponding VSphere Scan
            in MC Source.
    """

    core_source: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Collector(proto.Message):
    r"""Message describing Collector object.

    Attributes:
        name (str):
            name of resource.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create time stamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Update time stamp.
        labels (MutableMapping[str, str]):
            Labels as key value pairs.
        display_name (str):
            User specified name of the Collector.
        description (str):
            User specified description of the Collector.
        service_account (str):
            Service Account email used to ingest data to
            this Collector.
        bucket (str):
            Output only. Store cloud storage bucket name
            (which is a guid) created with this Collector.
        expected_asset_count (int):
            User specified expected asset count.
        state (google.cloud.rapidmigrationassessment_v1.types.Collector.State):
            Output only. State of the Collector.
        client_version (str):
            Output only. Client version.
        guest_os_scan (google.cloud.rapidmigrationassessment_v1.types.GuestOsScan):
            Output only. Reference to MC Source Guest Os
            Scan.
        vsphere_scan (google.cloud.rapidmigrationassessment_v1.types.VSphereScan):
            Output only. Reference to MC Source vsphere_scan.
        collection_days (int):
            How many days to collect data.
        eula_uri (str):
            Uri for EULA (End User License Agreement)
            from customer.
    """

    class State(proto.Enum):
        r"""-- Using suggestion from API Linter Analyzer for nesting enum -- --
        https://linter.aip.dev/216/nesting -- State of a Collector
        (server_side). States are used for internal purposes and named to
        keep convention of legacy product:
        https://cloud.google.com/migrate/stratozone/docs/about-stratoprobe.

        Values:
            STATE_UNSPECIFIED (0):
                Collector state is not recognized.
            STATE_INITIALIZING (1):
                Collector started to create, but hasn't been
                completed MC source creation and db object
                creation.
            STATE_READY_TO_USE (2):
                Collector has been created, MC source
                creation and db object creation completed.
            STATE_REGISTERED (3):
                Collector client has been registered with
                client.
            STATE_ACTIVE (4):
                Collector client is actively scanning.
            STATE_PAUSED (5):
                Collector is not actively scanning.
            STATE_DELETING (6):
                Collector is starting background job for
                deletion.
            STATE_DECOMMISSIONED (7):
                Collector completed all tasks for deletion.
            STATE_ERROR (8):
                Collector is in error state.
        """

        STATE_UNSPECIFIED = 0
        STATE_INITIALIZING = 1
        STATE_READY_TO_USE = 2
        STATE_REGISTERED = 3
        STATE_ACTIVE = 4
        STATE_PAUSED = 5
        STATE_DELETING = 6
        STATE_DECOMMISSIONED = 7
        STATE_ERROR = 8

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    description: str = proto.Field(
        proto.STRING,
        number=6,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=7,
    )
    bucket: str = proto.Field(
        proto.STRING,
        number=8,
    )
    expected_asset_count: int = proto.Field(
        proto.INT64,
        number=9,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=10,
        enum=State,
    )
    client_version: str = proto.Field(
        proto.STRING,
        number=11,
    )
    guest_os_scan: "GuestOsScan" = proto.Field(
        proto.MESSAGE,
        number=12,
        message="GuestOsScan",
    )
    vsphere_scan: "VSphereScan" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="VSphereScan",
    )
    collection_days: int = proto.Field(
        proto.INT32,
        number=14,
    )
    eula_uri: str = proto.Field(
        proto.STRING,
        number=15,
    )


class Annotation(proto.Message):
    r"""Message describing an Annotation

    Attributes:
        name (str):
            name of resource.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create time stamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Update time stamp.
        labels (MutableMapping[str, str]):
            Labels as key value pairs.
        type_ (google.cloud.rapidmigrationassessment_v1.types.Annotation.Type):
            Type of an annotation.
    """

    class Type(proto.Enum):
        r"""Types for project level setting.

        Values:
            TYPE_UNSPECIFIED (0):
                Unknown type
            TYPE_LEGACY_EXPORT_CONSENT (1):
                Indicates that this project has opted into
                StratoZone export.
            TYPE_QWIKLAB (2):
                Indicates that this project is created by
                Qwiklab.
        """

        TYPE_UNSPECIFIED = 0
        TYPE_LEGACY_EXPORT_CONSENT = 1
        TYPE_QWIKLAB = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=5,
        enum=Type,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
