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
    package="google.cloud.capacityplanner.v1beta",
    manifest={
        "Allocation",
    },
)


class Allocation(proto.Message):
    r"""Repesents Allocation which is part of aggregated
    reservations data response of "QueryReservations".


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        specific_allocation (google.cloud.capacityplanner_v1beta.types.Allocation.SpecificSKUAllocation):
            Reservation for instances with specific
            machine shapes.

            This field is a member of `oneof`_ ``type``.
        id (int):
            The unique identifier for the resource. This
            identifier is defined by the server.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The creation timestamp for this allocation.
        zone (str):
            Zone in which the reservation resides.
        description (str):
            A description while creating reservation.
        allocation (str):
            The reservation resource name.
        owner_project_id (str):

        status (google.cloud.capacityplanner_v1beta.types.Allocation.Status):
            The status of the reservation.
        share_settings (google.cloud.capacityplanner_v1beta.types.Allocation.ShareSettings):
            Specify share-settings to create a shared
            reservation.
        auto_delete_time (google.protobuf.timestamp_pb2.Timestamp):
            Absolute time in future when the reservation
            will be auto-deleted by Compute Engine.
    """

    class Status(proto.Enum):
        r"""The status of the reservation.

        Values:
            STATUS_UNSPECIFIED (0):
                Default value. This value is unused.
            INVALID (1):
                Invalid Reservation
            CREATING (2):
                Resources are being allocated for the
                reservation.
            READY (3):
                Reservation has allocated all its resources.
            DELETING (4):
                Reservation is currently being deleted.
            UPDATING (5):
                Reservation is currently being resized.
        """

        STATUS_UNSPECIFIED = 0
        INVALID = 1
        CREATING = 2
        READY = 3
        DELETING = 4
        UPDATING = 5

    class SpecificSKUAllocation(proto.Message):
        r"""This reservation type allows to pre allocate specific
        instance configuration.

        Attributes:
            instance_properties (google.cloud.capacityplanner_v1beta.types.Allocation.SpecificSKUAllocation.AllocatedInstanceProperties):
                The instance properties for the reservation.
            count (int):
                Specifies the number of resources that are
                allocated.
            used_count (int):
                Indicates how many instances are in use.
            assured_count (int):
                Indicates how many instances are actually
                usable currently.
        """

        class AllocatedInstanceProperties(proto.Message):
            r"""Properties of the SKU instances being reserved.

            Attributes:
                machine_type (str):
                    Specifies type of machine (name only) which has fixed number
                    of vCPUs and fixed amount of memory. This also includes
                    specifying custom machine type following
                    custom-NUMBER_OF_CPUS-AMOUNT_OF_MEMORY pattern.
                guest_accelerator (MutableSequence[google.cloud.capacityplanner_v1beta.types.Allocation.SpecificSKUAllocation.AllocatedInstanceProperties.AcceleratorConfig]):
                    Specifies accelerator type and count.
                min_cpu_platform (str):
                    Minimum cpu platform the reservation.
                local_ssd (MutableSequence[google.cloud.capacityplanner_v1beta.types.Allocation.SpecificSKUAllocation.AllocatedInstanceProperties.AllocatedDisk]):
                    Specifies amount of local ssd to reserve with
                    each instance. The type of disk is local-ssd.
            """

            class AcceleratorConfig(proto.Message):
                r"""A specification of the type and number of accelerator cards
                attached to the instance.

                Attributes:
                    type_ (str):
                        Accelerator name.
                        See
                        https://cloud.google.com/compute/docs/gpus/#introduction
                        for a full list of accelerator types.
                    count (int):
                        The number of the guest accelerator cards
                        exposed to this instance.
                """

                type_: str = proto.Field(
                    proto.STRING,
                    number=1,
                )
                count: int = proto.Field(
                    proto.INT32,
                    number=2,
                )

            class AllocatedDisk(proto.Message):
                r"""A specification of the interface and size of disk attached to
                the instance.

                Attributes:
                    disk_size_gb (int):
                        Specifies the size of the disk in base-2 GB.
                    disk_interface (google.cloud.capacityplanner_v1beta.types.Allocation.SpecificSKUAllocation.AllocatedInstanceProperties.AllocatedDisk.DiskInterface):
                        Specifies the disk interface to use for
                        attaching this disk, which is either SCSI or
                        NVME. The default is SCSI.
                """

                class DiskInterface(proto.Enum):
                    r"""guest device interface options to use for the disk.

                    Values:
                        DISK_INTERFACE_UNSPECIFIED (0):
                            Default value. This value is unused.
                        SCSI (1):
                            SCSI disk interface.
                        NVME (2):
                            NVME disk interface.
                        NVDIMM (3):
                            NVDIMM disk interface.
                        ISCSI (4):
                            ISCSI disk interface.
                    """

                    DISK_INTERFACE_UNSPECIFIED = 0
                    SCSI = 1
                    NVME = 2
                    NVDIMM = 3
                    ISCSI = 4

                disk_size_gb: int = proto.Field(
                    proto.INT64,
                    number=1,
                )
                disk_interface: "Allocation.SpecificSKUAllocation.AllocatedInstanceProperties.AllocatedDisk.DiskInterface" = proto.Field(
                    proto.ENUM,
                    number=2,
                    enum="Allocation.SpecificSKUAllocation.AllocatedInstanceProperties.AllocatedDisk.DiskInterface",
                )

            machine_type: str = proto.Field(
                proto.STRING,
                number=1,
            )
            guest_accelerator: MutableSequence[
                "Allocation.SpecificSKUAllocation.AllocatedInstanceProperties.AcceleratorConfig"
            ] = proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="Allocation.SpecificSKUAllocation.AllocatedInstanceProperties.AcceleratorConfig",
            )
            min_cpu_platform: str = proto.Field(
                proto.STRING,
                number=3,
            )
            local_ssd: MutableSequence[
                "Allocation.SpecificSKUAllocation.AllocatedInstanceProperties.AllocatedDisk"
            ] = proto.RepeatedField(
                proto.MESSAGE,
                number=4,
                message="Allocation.SpecificSKUAllocation.AllocatedInstanceProperties.AllocatedDisk",
            )

        instance_properties: "Allocation.SpecificSKUAllocation.AllocatedInstanceProperties" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="Allocation.SpecificSKUAllocation.AllocatedInstanceProperties",
        )
        count: int = proto.Field(
            proto.INT64,
            number=2,
        )
        used_count: int = proto.Field(
            proto.INT64,
            number=3,
        )
        assured_count: int = proto.Field(
            proto.INT64,
            number=4,
        )

    class ShareSettings(proto.Message):
        r"""The share setting for reservation.

        Attributes:
            share_type (google.cloud.capacityplanner_v1beta.types.Allocation.ShareSettings.ShareType):
                Type of sharing for this shared-reservation
            projects (MutableSequence[str]):
                A List of Project names to specify consumer projects for
                this shared-reservation. This is only valid when
                share_type's value is SPECIFIC_PROJECTS.
        """

        class ShareType(proto.Enum):
            r"""Possible scope in which the reservation can be shared. More
            granularity can be added in future.

            Values:
                SHARE_TYPE_UNSPECIFIED (0):
                    Default value. This value is unused.
                ORGANIZATION (1):
                    Shared-reservation is open to entire
                    Organization
                SPECIFIC_PROJECTS (2):
                    Shared-reservation is open to specific
                    projects
                LOCAL (3):
                    Default value.
                DIRECT_PROJECTS_UNDER_SPECIFIC_FOLDERS (4):
                    Shared-reservation is open to direct child
                    projects of specific folders.
            """

            SHARE_TYPE_UNSPECIFIED = 0
            ORGANIZATION = 1
            SPECIFIC_PROJECTS = 2
            LOCAL = 3
            DIRECT_PROJECTS_UNDER_SPECIFIC_FOLDERS = 4

        share_type: "Allocation.ShareSettings.ShareType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="Allocation.ShareSettings.ShareType",
        )
        projects: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )

    specific_allocation: SpecificSKUAllocation = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="type",
        message=SpecificSKUAllocation,
    )
    id: int = proto.Field(
        proto.INT64,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    zone: str = proto.Field(
        proto.STRING,
        number=3,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    allocation: str = proto.Field(
        proto.STRING,
        number=5,
    )
    owner_project_id: str = proto.Field(
        proto.STRING,
        number=10,
    )
    status: Status = proto.Field(
        proto.ENUM,
        number=7,
        enum=Status,
    )
    share_settings: ShareSettings = proto.Field(
        proto.MESSAGE,
        number=8,
        message=ShareSettings,
    )
    auto_delete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
