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

from google.cloud.capacityplanner_v1beta.types import allocation

__protobuf__ = proto.module(
    package="google.cloud.capacityplanner.v1beta",
    manifest={
        "FutureReservation",
    },
)


class FutureReservation(proto.Message):
    r"""Repesents Future Reservation request which is part of
    aggregated reservations data response of "QueryReservations".


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        specific_sku_properties (google.cloud.capacityplanner_v1beta.types.FutureReservation.SpecificSKUProperties):
            Future Reservation configuration to indicate
            instance properties and total count.

            This field is a member of `oneof`_ ``type``.
        id (int):
            A unique identifier for this future
            reservation. The server defines this identifier.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The creation timestamp for this future
            reservation.
        zone (str):
            URL of the Zone where this future reservation
            resides.
        description (str):
            Description of the future reservation
            provided by user.
        future_reservation (str):
            The future reservation resource name.
        owner_project_id (str):

        time_window (google.cloud.capacityplanner_v1beta.types.FutureReservation.TimeWindow):
            Time window for this Future Reservation.
        share_settings (google.cloud.capacityplanner_v1beta.types.Allocation.ShareSettings):
            List of Projects/Folders to share with.
        name_prefix (str):
            Name prefix for the reservations to be
            created at the time of delivery. The name prefix
            must comply with RFC1035. Maximum allowed length
            for name prefix is 20. Automatically created
            reservations name format will be
            <name-prefix>-date-####.
        status (google.cloud.capacityplanner_v1beta.types.FutureReservation.Status):
            Status of the Future Reservation
        auto_created_reservations_delete_time (google.protobuf.timestamp_pb2.Timestamp):
            Future timestamp when the FR auto-created
            reservations will be deleted by Compute Engine.
            Format of this field must be a valid RFC3339
            value.
        auto_delete_auto_created_reservations (bool):
            Setting for enabling or disabling automatic deletion for
            auto-created reservation. If set to true, auto-created
            reservations will be deleted at Future Reservation's end
            time (default) or at user's defined timestamp if any of the
            [auto_created_reservations_delete_time,
            auto_created_reservations_duration] values is specified. For
            keeping auto-created reservation indefinitely, this value
            should be set to false.
    """

    class SpecificSKUProperties(proto.Message):
        r"""Represents specific SKU properties for the Future
        Reservation.

        Attributes:
            instance_properties (google.cloud.capacityplanner_v1beta.types.Allocation.SpecificSKUAllocation.AllocatedInstanceProperties):
                Properties of the SKU instances being
                reserved.
            total_count (int):
                Total number of instances for which capacity
                assurance is requested at a future time period.
        """

        instance_properties: allocation.Allocation.SpecificSKUAllocation.AllocatedInstanceProperties = proto.Field(
            proto.MESSAGE,
            number=1,
            message=allocation.Allocation.SpecificSKUAllocation.AllocatedInstanceProperties,
        )
        total_count: int = proto.Field(
            proto.INT64,
            number=2,
        )

    class TimeWindow(proto.Message):
        r"""Represents time window for the Future Reservation.

        Attributes:
            start_time (google.protobuf.timestamp_pb2.Timestamp):
                Start time of the Future Reservation.
            end_time (google.protobuf.timestamp_pb2.Timestamp):
                End time of the Future Reservation.
        """

        start_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=1,
            message=timestamp_pb2.Timestamp,
        )
        end_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=2,
            message=timestamp_pb2.Timestamp,
        )

    class Status(proto.Message):
        r"""Represents status related to the future reservation.

        Attributes:
            procurement_status (google.cloud.capacityplanner_v1beta.types.FutureReservation.Status.ProcurementStatus):
                Current state of this Future Reservation
            lock_time (google.protobuf.timestamp_pb2.Timestamp):
                Time when Future Reservation would become LOCKED, after
                which no modifications to Future Reservation will be
                allowed. Applicable only after the Future Reservation is in
                the APPROVED state. The lock_time is an RFC3339 string. The
                procurement_status will transition to PROCURING state at
                this time.
            auto_created_reservations (MutableSequence[str]):
                Fully qualified urls of the automatically created
                reservations at start_time.
            fulfilled_count (int):
                This count indicates the fulfilled capacity
                so far. This is set during "PROVISIONING" state.
                This count also includes capacity delivered as
                part of existing matching reservations.
        """

        class ProcurementStatus(proto.Enum):
            r"""Represents procurement status of the Future Reservation.

            Values:
                PROCUREMENT_STATUS_UNSPECIFIED (0):
                    This is unused status value.
                PENDING_APPROVAL (1):
                    Future reservation is pending approval by
                    Google Cloud Platform.
                APPROVED (2):
                    Future reservation is approved by Google
                    Cloud Platform.
                COMMITTED (3):
                    Future reservation is committed by the
                    customer.
                DECLINED (4):
                    Future reservation is rejected by Google
                    Cloud Platform.
                CANCELLED (5):
                    Future reservation is cancelled by the
                    customer.
                PROCURING (6):
                    Future reservation is being procured by
                    Google Cloud Platform. Beyond this point, Future
                    reservation is locked and no further
                    modifications are allowed.
                PROVISIONING (7):
                    Future reservation capacity is being provisioned. This state
                    will be entered after start_time, while reservations are
                    being created to provide total_count reserved instance
                    slots. This state will not persist past start_time + 24h.
                FULFILLED (8):
                    Future reservation is fulfilled completely.
                FAILED (9):
                    Future reservation failed. No additional
                    reservations were provided.
                FAILED_PARTIALLY_FULFILLED (10):
                    Future reservation is partially fulfilled. Additional
                    reservations were provided but did not reach total_count
                    reserved instance slots.
                DRAFTING (11):
                    Related status for PlanningStatus.Draft. Transitions to
                    PENDING_APPROVAL upon user submitting FR.
                PENDING_AMENDMENT_APPROVAL (12):
                    An Amendment to the Future Reservation has
                    been requested. If the Amendment is declined,
                    the Future Reservation will be restored to the
                    last known good state.
            """

            PROCUREMENT_STATUS_UNSPECIFIED = 0
            PENDING_APPROVAL = 1
            APPROVED = 2
            COMMITTED = 3
            DECLINED = 4
            CANCELLED = 5
            PROCURING = 6
            PROVISIONING = 7
            FULFILLED = 8
            FAILED = 9
            FAILED_PARTIALLY_FULFILLED = 10
            DRAFTING = 11
            PENDING_AMENDMENT_APPROVAL = 12

        procurement_status: "FutureReservation.Status.ProcurementStatus" = proto.Field(
            proto.ENUM,
            number=1,
            enum="FutureReservation.Status.ProcurementStatus",
        )
        lock_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=2,
            message=timestamp_pb2.Timestamp,
        )
        auto_created_reservations: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=3,
        )
        fulfilled_count: int = proto.Field(
            proto.INT64,
            number=4,
        )

    specific_sku_properties: SpecificSKUProperties = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="type",
        message=SpecificSKUProperties,
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
        number=5,
    )
    description: str = proto.Field(
        proto.STRING,
        number=6,
    )
    future_reservation: str = proto.Field(
        proto.STRING,
        number=7,
    )
    owner_project_id: str = proto.Field(
        proto.STRING,
        number=15,
    )
    time_window: TimeWindow = proto.Field(
        proto.MESSAGE,
        number=9,
        message=TimeWindow,
    )
    share_settings: allocation.Allocation.ShareSettings = proto.Field(
        proto.MESSAGE,
        number=10,
        message=allocation.Allocation.ShareSettings,
    )
    name_prefix: str = proto.Field(
        proto.STRING,
        number=11,
    )
    status: Status = proto.Field(
        proto.MESSAGE,
        number=12,
        message=Status,
    )
    auto_created_reservations_delete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=13,
        message=timestamp_pb2.Timestamp,
    )
    auto_delete_auto_created_reservations: bool = proto.Field(
        proto.BOOL,
        number=14,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
