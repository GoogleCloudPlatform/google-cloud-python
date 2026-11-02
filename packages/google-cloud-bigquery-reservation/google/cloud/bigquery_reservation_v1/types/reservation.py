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

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
import google.type.expr_pb2 as expr_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.bigquery.reservation.v1",
    manifest={
        "Edition",
        "FailoverMode",
        "Reservation",
        "SchedulingPolicy",
        "ReservationGroup",
        "CapacityCommitment",
        "CreateReservationRequest",
        "ListReservationsRequest",
        "ListReservationsResponse",
        "GetReservationRequest",
        "DeleteReservationRequest",
        "UpdateReservationRequest",
        "FailoverReservationRequest",
        "CreateReservationGroupRequest",
        "GetReservationGroupRequest",
        "ListReservationGroupsRequest",
        "ListReservationGroupsResponse",
        "DeleteReservationGroupRequest",
        "UpdateReservationGroupRequest",
        "CreateCapacityCommitmentRequest",
        "ListCapacityCommitmentsRequest",
        "ListCapacityCommitmentsResponse",
        "GetCapacityCommitmentRequest",
        "DeleteCapacityCommitmentRequest",
        "UpdateCapacityCommitmentRequest",
        "SplitCapacityCommitmentRequest",
        "SplitCapacityCommitmentResponse",
        "MergeCapacityCommitmentsRequest",
        "Assignment",
        "CreateAssignmentRequest",
        "ListAssignmentsRequest",
        "ListAssignmentsResponse",
        "DeleteAssignmentRequest",
        "SearchAssignmentsRequest",
        "SearchAllAssignmentsRequest",
        "SearchAssignmentsResponse",
        "SearchAllAssignmentsResponse",
        "MoveAssignmentRequest",
        "UpdateAssignmentRequest",
        "TableReference",
        "BiReservation",
        "GetBiReservationRequest",
        "UpdateBiReservationRequest",
    },
)


class Edition(proto.Enum):
    r"""The type of editions.
    Different features and behaviors are provided to different
    editions Capacity commitments and reservations are linked to
    editions.

    Values:
        EDITION_UNSPECIFIED (0):
            Default value, which will be treated as
            ENTERPRISE.
        STANDARD (1):
            Standard edition.
        ENTERPRISE (2):
            Enterprise edition.
        ENTERPRISE_PLUS (3):
            Enterprise Plus edition.
    """

    EDITION_UNSPECIFIED = 0
    STANDARD = 1
    ENTERPRISE = 2
    ENTERPRISE_PLUS = 3


class FailoverMode(proto.Enum):
    r"""The failover mode when a user initiates a failover on a
    reservation determines how writes that are pending replication
    are handled after the failover is initiated.

    Values:
        FAILOVER_MODE_UNSPECIFIED (0):
            Invalid value.
        SOFT (1):
            When customers initiate a soft failover,
            BigQuery will wait until all committed writes
            are replicated to the secondary. This mode
            requires both regions to be available for the
            failover to succeed and prevents data loss.
        HARD (2):
            When customers initiate a hard failover,
            BigQuery will not wait until all committed
            writes are replicated to the secondary. There
            can be data loss for hard failover.
    """

    FAILOVER_MODE_UNSPECIFIED = 0
    SOFT = 1
    HARD = 2


class Reservation(proto.Message):
    r"""A reservation is a mechanism used to guarantee slots to
    users.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the reservation, e.g.,
            ``projects/*/locations/*/reservations/team1-prod``. The
            reservation_id must only contain lower case alphanumeric
            characters or dashes. It must start with a letter and must
            not end with a dash. Its maximum length is 64 characters.
        slot_capacity (int):
            Optional. Baseline slots available to this reservation. A
            slot is a unit of computational power in BigQuery, and
            serves as the unit of parallelism.

            Queries using this reservation might use more slots during
            runtime if ignore_idle_slots is set to false, or autoscaling
            is enabled.

            The total slot_capacity of the reservation and its siblings
            may exceed the total slot_count of capacity commitments. In
            that case, the exceeding slots will be charged with the
            autoscale SKU. You can increase the number of baseline slots
            in a reservation every few minutes. If you want to decrease
            your baseline slots, you are limited to once an hour if you
            have recently changed your baseline slot capacity and your
            baseline slots exceed your committed slots. Otherwise, you
            can decrease your baseline slots every few minutes.
        ignore_idle_slots (bool):
            Optional. If false, any query or pipeline job using this
            reservation will use idle slots from other reservations
            within the same admin project. If true, a query or pipeline
            job using this reservation will execute with the slot
            capacity specified in the slot_capacity field at most.
        autoscale (google.cloud.bigquery_reservation_v1.types.Reservation.Autoscale):
            Optional. The configuration parameters for
            the auto scaling feature.
        concurrency (int):
            Optional. Job concurrency target which sets a
            soft upper bound on the number of jobs that can
            run concurrently in this reservation. This is a
            soft target due to asynchronous nature of the
            system and various optimizations for small
            queries. Default value is 0 which means that
            concurrency target will be automatically
            computed by the system. NOTE: this field is
            exposed as target job concurrency in the
            Information Schema, DDL and BigQuery CLI.
        creation_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Creation time of the
            reservation.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Last update time of the
            reservation.
        multi_region_auxiliary (bool):
            Applicable only for reservations located
            within one of the BigQuery multi-regions (US or
            EU).

            If set to true, this reservation is placed in
            the organization's secondary region which is
            designated for disaster recovery purposes. If
            false, this reservation is placed in the
            organization's default region.

            NOTE: this is a preview feature. Project must be
            allow-listed in order to set this field.
        edition (google.cloud.bigquery_reservation_v1.types.Edition):
            Optional. Edition of the reservation.
        primary_location (str):
            Output only. The current location of the
            reservation's primary replica. This field is
            only set for reservations using the managed
            disaster recovery feature.
        secondary_location (str):
            Optional. The current location of the
            reservation's secondary replica. This field is
            only set for reservations using the managed
            disaster recovery feature. Users can set this in
            create reservation calls to create a failover
            reservation or in update reservation calls to
            convert a non-failover reservation to a failover
            reservation(or vice versa).
        original_primary_location (str):
            Output only. The location where the
            reservation was originally created. This is set
            only during the failover reservation's creation.
            All billing charges for the failover reservation
            will be applied to this location.
        max_slots (int):
            Optional. The overall max slots for the reservation,
            covering slot_capacity (baseline), idle slots (if
            ignore_idle_slots is false) and scaled slots. If present,
            the reservation won't use more than the specified number of
            slots, even if there is demand and supply (from idle slots).
            NOTE: capping a reservation's idle slot usage is best effort
            and its usage may exceed the max_slots value. However, in
            terms of autoscale.current_slots (which accounts for the
            additional added slots), it will never exceed the max_slots
            - baseline.

            This field must be set together with the scaling_mode enum
            value, otherwise the request will be rejected with error
            code ``google.rpc.Code.INVALID_ARGUMENT``.

            If the max_slots and scaling_mode are set, the autoscale or
            autoscale.max_slots field must be unset. Otherwise the
            request will be rejected with error code
            ``google.rpc.Code.INVALID_ARGUMENT``. However, the autoscale
            field may still be in the output. The autopscale.max_slots
            will always show as 0 and the autoscaler.current_slots will
            represent the current slots from autoscaler excluding idle
            slots. For example, if the max_slots is 1000 and
            scaling_mode is AUTOSCALE_ONLY, then in the output, the
            autoscaler.max_slots will be 0 and the
            autoscaler.current_slots may be any value between 0 and
            1000.

            If the max_slots is 1000, scaling_mode is ALL_SLOTS, the
            baseline is 100 and idle slots usage is 200, then in the
            output, the autoscaler.max_slots will be 0 and the
            autoscaler.current_slots will not be higher than 700.

            If the max_slots is 1000, scaling_mode is IDLE_SLOTS_ONLY,
            then in the output, the autoscaler field will be null.

            If the max_slots and scaling_mode are set, then the
            ignore_idle_slots field must be aligned with the
            scaling_mode enum value.(See details in ScalingMode
            comments). Otherwise the request will be rejected with error
            code ``google.rpc.Code.INVALID_ARGUMENT``.

            Please note, the max_slots is for user to manage the part of
            slots greater than the baseline. Therefore, we don't allow
            users to set max_slots smaller or equal to the baseline as
            it will not be meaningful. If the field is present and
            slot_capacity>=max_slots, requests will be rejected with
            error code ``google.rpc.Code.INVALID_ARGUMENT``.

            Please note that if max_slots is set to 0, we will treat it
            as unset. Customers can set max_slots to 0 and set
            scaling_mode to SCALING_MODE_UNSPECIFIED to disable the
            max_slots feature.

            This field is a member of `oneof`_ ``_max_slots``.
        scaling_mode (google.cloud.bigquery_reservation_v1.types.Reservation.ScalingMode):
            Optional. The scaling mode for the reservation. If the field
            is present but max_slots is not present, requests will be
            rejected with error code
            ``google.rpc.Code.INVALID_ARGUMENT``.
        labels (MutableMapping[str, str]):
            Optional. The labels associated with this
            reservation. You can use these to organize and
            group your reservations. You can set this
            property when you create or update a
            reservation.
        reservation_group (str):
            Optional. The reservation group that this reservation
            belongs to. You can set this property when you create or
            update a reservation. Reservations do not need to belong to
            a reservation group. Format:
            projects/{project}/locations/{location}/reservationGroups/{reservation_group}
            or just {reservation_group}
        replication_status (google.cloud.bigquery_reservation_v1.types.Reservation.ReplicationStatus):
            Output only. The Disaster Recovery(DR)
            replication status of the reservation. This is
            only available for the primary replicas of
            DR/failover reservations and provides
            information about the both the staleness of the
            secondary and the last error encountered while
            trying to replicate changes from the primary to
            the secondary. If this field is blank, it means
            that the reservation is either not a DR
            reservation or the reservation is a DR secondary
            or that any replication operations on the
            reservation have succeeded.
        scheduling_policy (google.cloud.bigquery_reservation_v1.types.SchedulingPolicy):
            Optional. The scheduling policy to use for
            jobs and queries running under this reservation.
            The scheduling policy controls how the
            reservation's resources are distributed.

            This feature is not yet generally available.
        reservation_group_path (MutableSequence[str]):
            Output only. The reservation group path of the reservation
            from root to leaf. The order of elements matters: the first
            element is the top level group and the last element is the
            direct parent reservation group. For example, if a
            reservation is under group-1 -> group-2 -> group-3, then the
            reservation group path is ["group-1", "group-2", "group-3"].
    """

    class ScalingMode(proto.Enum):
        r"""The scaling mode for the reservation. This enum determines
        how the reservation scales up and down.

        Values:
            SCALING_MODE_UNSPECIFIED (0):
                Default value of ScalingMode.
            AUTOSCALE_ONLY (1):
                The reservation will scale up only using slots from
                autoscaling. It will not use any idle slots even if there
                may be some available. The upper limit that autoscaling can
                scale up to will be max_slots - baseline. For example, if
                max_slots is 1000, baseline is 200 and customer sets
                ScalingMode to AUTOSCALE_ONLY, then autoscalerg will scale
                up to 800 slots and no idle slots will be used.

                Please note, in this mode, the ignore_idle_slots field must
                be set to true. Otherwise the request will be rejected with
                error code ``google.rpc.Code.INVALID_ARGUMENT``.
            IDLE_SLOTS_ONLY (2):
                The reservation will scale up using only idle slots
                contributed by other reservations or from unassigned
                commitments. If no idle slots are available it will not
                scale up further. If the idle slots which it is using are
                reclaimed by the contributing reservation(s) it may be
                forced to scale down. The max idle slots the reservation can
                be max_slots - baseline capacity. For example, if max_slots
                is 1000, baseline is 200 and customer sets ScalingMode to
                IDLE_SLOTS_ONLY,

                1. if there are 1000 idle slots available in other
                   reservations, the reservation will scale up to 1000 slots
                   with 200 baseline and 800 idle slots.
                2. if there are 500 idle slots available in other
                   reservations, the reservation will scale up to 700 slots
                   with 200 baseline and 500 idle slots. Please note, in
                   this mode, the reservation might not be able to scale up
                   to max_slots.

                Please note, in this mode, the ignore_idle_slots field must
                be set to false. Otherwise the request will be rejected with
                error code ``google.rpc.Code.INVALID_ARGUMENT``.
            ALL_SLOTS (3):
                The reservation will scale up using all slots available to
                it. It will use idle slots contributed by other reservations
                or from unassigned commitments first. If no idle slots are
                available it will scale up using autoscaling. For example,
                if max_slots is 1000, baseline is 200 and customer sets
                ScalingMode to ALL_SLOTS,

                1. if there are 800 idle slots available in other
                   reservations, the reservation will scale up to 1000 slots
                   with 200 baseline and 800 idle slots.
                2. if there are 500 idle slots available in other
                   reservations, the reservation will scale up to 1000 slots
                   with 200 baseline, 500 idle slots and 300 autoscaling
                   slots.
                3. if there are no idle slots available in other
                   reservations, it will scale up to 1000 slots with 200
                   baseline and 800 autoscaling slots.

                Please note, in this mode, the ignore_idle_slots field must
                be set to false. Otherwise the request will be rejected with
                error code ``google.rpc.Code.INVALID_ARGUMENT``.
        """

        SCALING_MODE_UNSPECIFIED = 0
        AUTOSCALE_ONLY = 1
        IDLE_SLOTS_ONLY = 2
        ALL_SLOTS = 3

    class Autoscale(proto.Message):
        r"""Auto scaling settings.

        Attributes:
            current_slots (int):
                Output only. The slot capacity added to this reservation
                when autoscale happens. Will be between [0, max_slots].
                Note: after users reduce max_slots, it may take a while
                before it can be propagated, so current_slots may stay in
                the original value and could be larger than max_slots for
                that brief period (less than one minute)
            max_slots (int):
                Optional. Number of slots to be scaled when
                needed.
        """

        current_slots: int = proto.Field(
            proto.INT64,
            number=1,
        )
        max_slots: int = proto.Field(
            proto.INT64,
            number=2,
        )

    class ReplicationStatus(proto.Message):
        r"""Disaster Recovery(DR) replication status of the reservation.

        Attributes:
            error (google.rpc.status_pb2.Status):
                Output only. The last error encountered while
                trying to replicate changes from the primary to
                the secondary. This field is only available if
                the replication has not succeeded since.
            last_error_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. The time at which the last error
                was encountered while trying to replicate
                changes from the primary to the secondary. This
                field is only available if the replication has
                not succeeded since.
            last_replication_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. A timestamp corresponding to the
                last change on the primary that was successfully
                replicated to the secondary.
            soft_failover_start_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. The time at which a soft
                failover for the reservation and its associated
                datasets was initiated. After this field is set,
                all subsequent changes to the reservation will
                be rejected unless a hard failover overrides
                this operation. This field will be cleared once
                the failover is complete.
        """

        error: status_pb2.Status = proto.Field(
            proto.MESSAGE,
            number=1,
            message=status_pb2.Status,
        )
        last_error_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=2,
            message=timestamp_pb2.Timestamp,
        )
        last_replication_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=3,
            message=timestamp_pb2.Timestamp,
        )
        soft_failover_start_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=4,
            message=timestamp_pb2.Timestamp,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    slot_capacity: int = proto.Field(
        proto.INT64,
        number=2,
    )
    ignore_idle_slots: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    autoscale: Autoscale = proto.Field(
        proto.MESSAGE,
        number=7,
        message=Autoscale,
    )
    concurrency: int = proto.Field(
        proto.INT64,
        number=16,
    )
    creation_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    multi_region_auxiliary: bool = proto.Field(
        proto.BOOL,
        number=14,
    )
    edition: "Edition" = proto.Field(
        proto.ENUM,
        number=17,
        enum="Edition",
    )
    primary_location: str = proto.Field(
        proto.STRING,
        number=18,
    )
    secondary_location: str = proto.Field(
        proto.STRING,
        number=19,
    )
    original_primary_location: str = proto.Field(
        proto.STRING,
        number=20,
    )
    max_slots: int = proto.Field(
        proto.INT64,
        number=21,
        optional=True,
    )
    scaling_mode: ScalingMode = proto.Field(
        proto.ENUM,
        number=22,
        enum=ScalingMode,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=23,
    )
    reservation_group: str = proto.Field(
        proto.STRING,
        number=25,
    )
    replication_status: ReplicationStatus = proto.Field(
        proto.MESSAGE,
        number=24,
        message=ReplicationStatus,
    )
    scheduling_policy: "SchedulingPolicy" = proto.Field(
        proto.MESSAGE,
        number=27,
        message="SchedulingPolicy",
    )
    reservation_group_path: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=28,
    )


class SchedulingPolicy(proto.Message):
    r"""The scheduling policy controls how a reservation's resources
    are distributed.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        concurrency (int):
            Optional. If present and > 0, the reservation
            will attempt to limit the concurrency of jobs
            running for any particular project within it to
            the given value.

            This feature is not yet generally available.

            This field is a member of `oneof`_ ``_concurrency``.
        max_slots (int):
            Optional. If present and > 0, the reservation
            will attempt to limit the slot consumption of
            queries running for any particular project
            within it to the given value.

            This feature is not yet generally available.

            This field is a member of `oneof`_ ``_max_slots``.
    """

    concurrency: int = proto.Field(
        proto.INT64,
        number=1,
        optional=True,
    )
    max_slots: int = proto.Field(
        proto.INT64,
        number=2,
        optional=True,
    )


class ReservationGroup(proto.Message):
    r"""A reservation group is a container for reservations.

    Attributes:
        name (str):
            Identifier. The resource name of the reservation group,
            e.g.,
            ``projects/*/locations/*/reservationGroups/team1-prod``. The
            reservation_group_id must only contain lower case
            alphanumeric characters or dashes. It must start with a
            letter and must not end with a dash. Its maximum length is
            64 characters.
        parent_group (str):
            Optional. The parent reservation group of the reservation
            group. Format:
            ``projects/*/locations/*/reservationGroups/team1-prod`` for
            non-root reservation groups, or ``projects/*/locations/*``
            for root reservation groups.
        creation_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Creation time of the reservation
            group.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Last update time of the
            reservation group via a user operation. This
            timestamp is updated only when an update
            operation explicitly targets this reservation
            group directly. It is not updated when parent or
            child groups are created, updated, or deleted.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    parent_group: str = proto.Field(
        proto.STRING,
        number=2,
    )
    creation_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


class CapacityCommitment(proto.Message):
    r"""Capacity commitment is a way to purchase compute capacity for
    BigQuery jobs (in the form of slots) with some committed period
    of usage. Annual commitments renew by default. Commitments can
    be removed after their commitment end time passes.

    In order to remove annual commitment, its plan needs to be
    changed to monthly or flex first.

    A capacity commitment resource exists as a child resource of the
    admin project.

    Attributes:
        name (str):
            Output only. The resource name of the capacity commitment,
            e.g.,
            ``projects/myproject/locations/US/capacityCommitments/123``
            The commitment_id must only contain lower case alphanumeric
            characters or dashes. It must start with a letter and must
            not end with a dash. Its maximum length is 64 characters.
        slot_count (int):
            Optional. Number of slots in this commitment.
        plan (google.cloud.bigquery_reservation_v1.types.CapacityCommitment.CommitmentPlan):
            Optional. Capacity commitment commitment
            plan.
        state (google.cloud.bigquery_reservation_v1.types.CapacityCommitment.State):
            Output only. State of the commitment.
        commitment_start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The start of the current commitment period. It
            is applicable only for ACTIVE capacity commitments. Note
            after the commitment is renewed, commitment_start_time won't
            be changed. It refers to the start time of the original
            commitment.
        commitment_end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The end of the current commitment period. It is
            applicable only for ACTIVE capacity commitments. Note after
            renewal, commitment_end_time is the time the renewed
            commitment expires. So itwould be at a time after
            commitment_start_time + committed period, because we don't
            change commitment_start_time ,
        failure_status (google.rpc.status_pb2.Status):
            Output only. For FAILED commitment plan,
            provides the reason of failure.
        renewal_plan (google.cloud.bigquery_reservation_v1.types.CapacityCommitment.CommitmentPlan):
            Optional. The plan this capacity commitment is converted to
            after commitment_end_time passes. Once the plan is changed,
            committed period is extended according to commitment plan.
            Only applicable for ANNUAL and TRIAL commitments.
        multi_region_auxiliary (bool):
            Applicable only for commitments located
            within one of the BigQuery multi-regions (US or
            EU).

            If set to true, this commitment is placed in the
            organization's secondary region which is
            designated for disaster recovery purposes. If
            false, this commitment is placed in the
            organization's default region.

            NOTE: this is a preview feature. Project must be
            allow-listed in order to set this field.
        edition (google.cloud.bigquery_reservation_v1.types.Edition):
            Optional. Edition of the capacity commitment.
        is_flat_rate (bool):
            Output only. If true, the commitment is a
            flat-rate commitment, otherwise, it's an edition
            commitment.
    """

    class CommitmentPlan(proto.Enum):
        r"""Commitment plan defines the current committed period.
        Capacity commitment cannot be deleted during it's committed
        period.

        Values:
            COMMITMENT_PLAN_UNSPECIFIED (0):
                Invalid plan value. Requests with this value will be
                rejected with error code
                ``google.rpc.Code.INVALID_ARGUMENT``.
            FLEX (3):
                Deprecated: Flex commitments are deprecated.
                Please use Edition-based capacity commitments.
                Flex commitments have committed period of 1
                minute after becoming ACTIVE. After that, they
                are not in a committed period anymore and can be
                removed any time.
            FLEX_FLAT_RATE (7):
                Same as FLEX, should only be used if
                flat-rate commitments are still available.
            TRIAL (5):
                Trial commitments have a committed period of 182 days after
                becoming ACTIVE. After that, they are converted to a new
                commitment based on the ``renewal_plan``. Default
                ``renewal_plan`` for Trial commitment is Flex so that it can
                be deleted right after committed period ends.
            MONTHLY (2):
                Monthly commitments have a committed period
                of 30 days after becoming ACTIVE. After that,
                they are not in a committed period anymore and
                can be removed any time.
            MONTHLY_FLAT_RATE (8):
                Same as MONTHLY, should only be used if
                flat-rate commitments are still available.
            ANNUAL (4):
                Annual commitments have a committed period of 365 days after
                becoming ACTIVE. After that they are converted to a new
                commitment based on the renewal_plan.
            ANNUAL_FLAT_RATE (9):
                Same as ANNUAL, should only be used if
                flat-rate commitments are still available.
            THREE_YEAR (10):
                3-year commitments have a committed period of 1095(3 \* 365)
                days after becoming ACTIVE. After that they are converted to
                a new commitment based on the renewal_plan.
            NONE (6):
                Should only be used for ``renewal_plan`` and is only
                meaningful if edition is specified to values other than
                EDITION_UNSPECIFIED. Otherwise
                CreateCapacityCommitmentRequest or
                UpdateCapacityCommitmentRequest will be rejected with error
                code ``google.rpc.Code.INVALID_ARGUMENT``. If the
                renewal_plan is NONE, capacity commitment will be removed at
                the end of its commitment period.
        """

        COMMITMENT_PLAN_UNSPECIFIED = 0
        FLEX = 3
        FLEX_FLAT_RATE = 7
        TRIAL = 5
        MONTHLY = 2
        MONTHLY_FLAT_RATE = 8
        ANNUAL = 4
        ANNUAL_FLAT_RATE = 9
        THREE_YEAR = 10
        NONE = 6

    class State(proto.Enum):
        r"""Capacity commitment can either become ACTIVE right away or
        transition from PENDING to ACTIVE or FAILED.

        Values:
            STATE_UNSPECIFIED (0):
                Invalid state value.
            PENDING (1):
                Capacity commitment is pending provisioning. Pending
                capacity commitment does not contribute to the project's
                slot_capacity.
            ACTIVE (2):
                Once slots are provisioned, capacity commitment becomes
                active. slot_count is added to the project's slot_capacity.
            FAILED (3):
                Capacity commitment is failed to be activated
                by the backend.
        """

        STATE_UNSPECIFIED = 0
        PENDING = 1
        ACTIVE = 2
        FAILED = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    slot_count: int = proto.Field(
        proto.INT64,
        number=2,
    )
    plan: CommitmentPlan = proto.Field(
        proto.ENUM,
        number=3,
        enum=CommitmentPlan,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )
    commitment_start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    commitment_end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    failure_status: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=7,
        message=status_pb2.Status,
    )
    renewal_plan: CommitmentPlan = proto.Field(
        proto.ENUM,
        number=8,
        enum=CommitmentPlan,
    )
    multi_region_auxiliary: bool = proto.Field(
        proto.BOOL,
        number=10,
    )
    edition: "Edition" = proto.Field(
        proto.ENUM,
        number=12,
        enum="Edition",
    )
    is_flat_rate: bool = proto.Field(
        proto.BOOL,
        number=14,
    )


class CreateReservationRequest(proto.Message):
    r"""The request for
    [ReservationService.CreateReservation][google.cloud.bigquery.reservation.v1.ReservationService.CreateReservation].

    Attributes:
        parent (str):
            Required. Project, location. E.g.,
            ``projects/myproject/locations/US``
        reservation_id (str):
            The reservation ID. It must only contain
            lower case alphanumeric characters or dashes. It
            must start with a letter and must not end with a
            dash. Its maximum length is 64 characters.
        reservation (google.cloud.bigquery_reservation_v1.types.Reservation):
            Definition of the new reservation to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    reservation_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    reservation: "Reservation" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Reservation",
    )


class ListReservationsRequest(proto.Message):
    r"""The request for
    [ReservationService.ListReservations][google.cloud.bigquery.reservation.v1.ReservationService.ListReservations].

    Attributes:
        parent (str):
            Required. The parent resource name containing project and
            location, e.g.: ``projects/myproject/locations/US``
        page_size (int):
            The maximum number of items to return per
            page.
        page_token (str):
            The next_page_token value returned from a previous List
            request, if any.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListReservationsResponse(proto.Message):
    r"""The response for
    [ReservationService.ListReservations][google.cloud.bigquery.reservation.v1.ReservationService.ListReservations].

    Attributes:
        reservations (MutableSequence[google.cloud.bigquery_reservation_v1.types.Reservation]):
            List of reservations visible to the user.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    reservations: MutableSequence["Reservation"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Reservation",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetReservationRequest(proto.Message):
    r"""The request for
    [ReservationService.GetReservation][google.cloud.bigquery.reservation.v1.ReservationService.GetReservation].

    Attributes:
        name (str):
            Required. Resource name of the reservation to retrieve.
            E.g.,
            ``projects/myproject/locations/US/reservations/team1-prod``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteReservationRequest(proto.Message):
    r"""The request for
    [ReservationService.DeleteReservation][google.cloud.bigquery.reservation.v1.ReservationService.DeleteReservation].

    Attributes:
        name (str):
            Required. Resource name of the reservation to retrieve.
            E.g.,
            ``projects/myproject/locations/US/reservations/team1-prod``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateReservationRequest(proto.Message):
    r"""The request for
    [ReservationService.UpdateReservation][google.cloud.bigquery.reservation.v1.ReservationService.UpdateReservation].

    Attributes:
        reservation (google.cloud.bigquery_reservation_v1.types.Reservation):
            Content of the reservation to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Standard field mask for the set of fields to
            be updated.
    """

    reservation: "Reservation" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Reservation",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class FailoverReservationRequest(proto.Message):
    r"""The request for ReservationService.FailoverReservation.

    Attributes:
        name (str):
            Required. Resource name of the reservation to failover.
            E.g.,
            ``projects/myproject/locations/US/reservations/team1-prod``
        failover_mode (google.cloud.bigquery_reservation_v1.types.FailoverMode):
            Optional. A parameter that determines how
            writes that are pending replication are handled
            after a failover is initiated. If not specified,
            HARD failover mode is used by default.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    failover_mode: "FailoverMode" = proto.Field(
        proto.ENUM,
        number=2,
        enum="FailoverMode",
    )


class CreateReservationGroupRequest(proto.Message):
    r"""The request for
    [ReservationService.CreateReservationGroup][google.cloud.bigquery.reservation.v1.ReservationService.CreateReservationGroup].

    Attributes:
        parent (str):
            Required. Project, location. E.g.,
            ``projects/myproject/locations/US``
        reservation_group_id (str):
            Required. The reservation group ID. It must
            only contain lower case alphanumeric characters
            or dashes. It must start with a letter and must
            not end with a dash. Its maximum length is 64
            characters.
        reservation_group (google.cloud.bigquery_reservation_v1.types.ReservationGroup):
            Required. New Reservation Group to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    reservation_group_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    reservation_group: "ReservationGroup" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ReservationGroup",
    )


class GetReservationGroupRequest(proto.Message):
    r"""The request for
    [ReservationService.GetReservationGroup][google.cloud.bigquery.reservation.v1.ReservationService.GetReservationGroup].

    Attributes:
        name (str):
            Required. Resource name of the reservation group to
            retrieve. E.g.,
            ``projects/myproject/locations/US/reservationGroups/team1-prod``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListReservationGroupsRequest(proto.Message):
    r"""The request for
    [ReservationService.ListReservationGroups][google.cloud.bigquery.reservation.v1.ReservationService.ListReservationGroups].

    Attributes:
        parent (str):
            Required. The parent resource name containing project and
            location, e.g.: ``projects/myproject/locations/US``
        page_size (int):
            The maximum number of items to return per
            page.
        page_token (str):
            The next_page_token value returned from a previous List
            request, if any.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListReservationGroupsResponse(proto.Message):
    r"""The response for
    [ReservationService.ListReservationGroups][google.cloud.bigquery.reservation.v1.ReservationService.ListReservationGroups].

    Attributes:
        reservation_groups (MutableSequence[google.cloud.bigquery_reservation_v1.types.ReservationGroup]):
            List of reservations visible to the user.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    reservation_groups: MutableSequence["ReservationGroup"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ReservationGroup",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteReservationGroupRequest(proto.Message):
    r"""The request for
    [ReservationService.DeleteReservationGroup][google.cloud.bigquery.reservation.v1.ReservationService.DeleteReservationGroup].

    Attributes:
        name (str):
            Required. Resource name of the reservation group to
            retrieve. E.g.,
            ``projects/myproject/locations/US/reservationGroups/team1-prod``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateReservationGroupRequest(proto.Message):
    r"""The request for
    [ReservationService.UpdateReservationGroup][google.cloud.bigquery.reservation.v1.ReservationService.UpdateReservationGroup].

    Attributes:
        reservation_group (google.cloud.bigquery_reservation_v1.types.ReservationGroup):
            Required. Content of the reservation group to
            update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Standard field mask for the set of
            fields to be updated.
    """

    reservation_group: "ReservationGroup" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ReservationGroup",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class CreateCapacityCommitmentRequest(proto.Message):
    r"""The request for
    [ReservationService.CreateCapacityCommitment][google.cloud.bigquery.reservation.v1.ReservationService.CreateCapacityCommitment].

    Attributes:
        parent (str):
            Required. Resource name of the parent reservation. E.g.,
            ``projects/myproject/locations/US``
        capacity_commitment (google.cloud.bigquery_reservation_v1.types.CapacityCommitment):
            Content of the capacity commitment to create.
        enforce_single_admin_project_per_org (bool):
            If true, fail the request if another project
            in the organization has a capacity commitment.
        capacity_commitment_id (str):
            The optional capacity commitment ID. Capacity
            commitment name will be generated automatically
            if this field is empty. This field must only
            contain lower case alphanumeric characters or
            dashes. The first and last character cannot be a
            dash. Max length is 64 characters. NOTE: this ID
            won't be kept if the capacity commitment is
            split or merged.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    capacity_commitment: "CapacityCommitment" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="CapacityCommitment",
    )
    enforce_single_admin_project_per_org: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    capacity_commitment_id: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListCapacityCommitmentsRequest(proto.Message):
    r"""The request for
    [ReservationService.ListCapacityCommitments][google.cloud.bigquery.reservation.v1.ReservationService.ListCapacityCommitments].

    Attributes:
        parent (str):
            Required. Resource name of the parent reservation. E.g.,
            ``projects/myproject/locations/US``
        page_size (int):
            The maximum number of items to return.
        page_token (str):
            The next_page_token value returned from a previous List
            request, if any.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListCapacityCommitmentsResponse(proto.Message):
    r"""The response for
    [ReservationService.ListCapacityCommitments][google.cloud.bigquery.reservation.v1.ReservationService.ListCapacityCommitments].

    Attributes:
        capacity_commitments (MutableSequence[google.cloud.bigquery_reservation_v1.types.CapacityCommitment]):
            List of capacity commitments visible to the
            user.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    capacity_commitments: MutableSequence["CapacityCommitment"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="CapacityCommitment",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetCapacityCommitmentRequest(proto.Message):
    r"""The request for
    [ReservationService.GetCapacityCommitment][google.cloud.bigquery.reservation.v1.ReservationService.GetCapacityCommitment].

    Attributes:
        name (str):
            Required. Resource name of the capacity commitment to
            retrieve. E.g.,
            ``projects/myproject/locations/US/capacityCommitments/123``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteCapacityCommitmentRequest(proto.Message):
    r"""The request for
    [ReservationService.DeleteCapacityCommitment][google.cloud.bigquery.reservation.v1.ReservationService.DeleteCapacityCommitment].

    Attributes:
        name (str):
            Required. Resource name of the capacity commitment to
            delete. E.g.,
            ``projects/myproject/locations/US/capacityCommitments/123``
        force (bool):
            Can be used to force delete commitments even
            if assignments exist. Deleting commitments with
            assignments may cause queries to fail if they no
            longer have access to slots.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class UpdateCapacityCommitmentRequest(proto.Message):
    r"""The request for
    [ReservationService.UpdateCapacityCommitment][google.cloud.bigquery.reservation.v1.ReservationService.UpdateCapacityCommitment].

    Attributes:
        capacity_commitment (google.cloud.bigquery_reservation_v1.types.CapacityCommitment):
            Content of the capacity commitment to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Standard field mask for the set of fields to
            be updated.
    """

    capacity_commitment: "CapacityCommitment" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="CapacityCommitment",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class SplitCapacityCommitmentRequest(proto.Message):
    r"""The request for
    [ReservationService.SplitCapacityCommitment][google.cloud.bigquery.reservation.v1.ReservationService.SplitCapacityCommitment].

    Attributes:
        name (str):
            Required. The resource name e.g.,:
            ``projects/myproject/locations/US/capacityCommitments/123``
        slot_count (int):
            Number of slots in the capacity commitment
            after the split.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    slot_count: int = proto.Field(
        proto.INT64,
        number=2,
    )


class SplitCapacityCommitmentResponse(proto.Message):
    r"""The response for
    [ReservationService.SplitCapacityCommitment][google.cloud.bigquery.reservation.v1.ReservationService.SplitCapacityCommitment].

    Attributes:
        first (google.cloud.bigquery_reservation_v1.types.CapacityCommitment):
            First capacity commitment, result of a split.
        second (google.cloud.bigquery_reservation_v1.types.CapacityCommitment):
            Second capacity commitment, result of a
            split.
    """

    first: "CapacityCommitment" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="CapacityCommitment",
    )
    second: "CapacityCommitment" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="CapacityCommitment",
    )


class MergeCapacityCommitmentsRequest(proto.Message):
    r"""The request for
    [ReservationService.MergeCapacityCommitments][google.cloud.bigquery.reservation.v1.ReservationService.MergeCapacityCommitments].

    Attributes:
        parent (str):
            Parent resource that identifies admin project and location
            e.g., ``projects/myproject/locations/us``
        capacity_commitment_ids (MutableSequence[str]):
            Ids of capacity commitments to merge.
            These capacity commitments must exist under
            admin project and location specified in the
            parent.
            ID is the last portion of capacity commitment
            name e.g., 'abc' for
            projects/myproject/locations/US/capacityCommitments/abc
        capacity_commitment_id (str):
            Optional. The optional resulting capacity
            commitment ID. Capacity commitment name will be
            generated automatically if this field is empty.
            This field must only contain lower case
            alphanumeric characters or dashes. The first and
            last character cannot be a dash. Max length is
            64 characters.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    capacity_commitment_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    capacity_commitment_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class Assignment(proto.Message):
    r"""An assignment allows a project to submit jobs
    of a certain type using slots from the specified reservation.

    Attributes:
        name (str):
            Output only. Name of the resource. E.g.:
            ``projects/myproject/locations/US/reservations/team1-prod/assignments/123``.
            The assignment_id must only contain lower case alphanumeric
            characters or dashes and the max length is 64 characters.
        assignee (str):
            Optional. The resource which will use the reservation. E.g.
            ``projects/myproject``, ``folders/123``, or
            ``organizations/456``.
        job_type (google.cloud.bigquery_reservation_v1.types.Assignment.JobType):
            Optional. Which type of jobs will use the
            reservation.
        state (google.cloud.bigquery_reservation_v1.types.Assignment.State):
            Output only. State of the assignment.
        enable_gemini_in_bigquery (bool):
            Optional. Deprecated: "Gemini in BigQuery" is
            now available by default for all BigQuery
            editions and should not be explicitly set.
            Controls if "Gemini in BigQuery"
            (https://cloud.google.com/gemini/docs/bigquery/overview)
            features should be enabled for this reservation
            assignment.
        scheduling_policy (google.cloud.bigquery_reservation_v1.types.SchedulingPolicy):
            Optional. The scheduling policy to use for
            jobs and queries of this assignee when running
            under the associated reservation. The scheduling
            policy controls how the reservation's resources
            are distributed. This overrides the default
            scheduling policy specified on the reservation.

            This feature is not yet generally available.
        principal (str):
            Optional. Represents the principal for this assignment. If
            not empty, jobs run by this principal utilize the associated
            reservation. Otherwise, jobs fall back to using the
            reservation assigned to the project, folder, or
            organization, in that order. If no reservation is assigned
            at any of these levels, on-demand capacity is used.

            The supported formats are:

            - ``principal://goog/subject/USER_EMAIL_ADDRESS`` for users,
            - ``principal://iam.googleapis.com/projects/-/serviceAccounts/SA_EMAIL_ADDRESS``
              for service accounts,
            - ``principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/SUBJECT_ID``
              for workload identity pool identities.
            - The special value ``unknown_or_deleted_user`` represents
              principals which cannot be read from the user info
              service, for example, deleted users.
        precedence (int):
            Optional. Specifies the priority precedence
            for this assignment. Used to resolve ambiguity
            when multiple assignments match a single job.
            Higher numerical values represent higher
            priority (e.g., 20 is higher than 10). If
            unspecified, it defaults to 0. Multiple
            assignments can share the same precedence, but
            it is recommended to use unique precedence
            values for assignments within the same assignee
            scope.
        condition (google.type.expr_pb2.Expr):
            Optional. Common Expression Language (CEL)
            condition that defines the matching criteria for
            this assignment. The condition must resolve to a
            boolean value. Supported variables will be added
            later.
    """

    class JobType(proto.Enum):
        r"""Types of job, which could be specified when using the
        reservation.

        Values:
            JOB_TYPE_UNSPECIFIED (0):
                Invalid type. Requests with this value will be rejected with
                error code ``google.rpc.Code.INVALID_ARGUMENT``.
            PIPELINE (1):
                Pipeline (load/export) jobs from the project
                will use the reservation.
            QUERY (2):
                Query jobs from the project will use the
                reservation.
            ML_EXTERNAL (3):
                BigQuery ML jobs that use services external
                to BigQuery for model training. These jobs will
                not utilize idle slots from other reservations.
            BACKGROUND (4):
                Background jobs that BigQuery runs for the
                customers in the background.
            CONTINUOUS (6):
                Continuous SQL jobs will use this
                reservation. Reservations with continuous
                assignments cannot be mixed with non-continuous
                assignments.
            BACKGROUND_CHANGE_DATA_CAPTURE (7):
                Finer granularity background jobs for
                capturing changes in a source database and
                streaming them into BigQuery. Reservations with
                this job type take priority over a default
                BACKGROUND reservation assignment (if it
                exists).
            BACKGROUND_COLUMN_METADATA_INDEX (8):
                Finer granularity background jobs for
                refreshing cached metadata for BigQuery tables.
                Reservations with this job type take priority
                over a default BACKGROUND reservation assignment
                (if it exists).
            BACKGROUND_SEARCH_INDEX_REFRESH (9):
                Finer granularity background jobs for
                refreshing search indexes upon BigQuery table
                columns. Reservations with this job type take
                priority over a default BACKGROUND reservation
                assignment (if it exists).
            AUTOMATIC_MATERIALIZED_VIEW_REFRESH (10):
                Automated materialized view refresh jobs will
                use the reservation. Reservations with this job
                type will take priority over a default QUERY
                reservation assignment (if it exists).
        """

        JOB_TYPE_UNSPECIFIED = 0
        PIPELINE = 1
        QUERY = 2
        ML_EXTERNAL = 3
        BACKGROUND = 4
        CONTINUOUS = 6
        BACKGROUND_CHANGE_DATA_CAPTURE = 7
        BACKGROUND_COLUMN_METADATA_INDEX = 8
        BACKGROUND_SEARCH_INDEX_REFRESH = 9
        AUTOMATIC_MATERIALIZED_VIEW_REFRESH = 10

    class State(proto.Enum):
        r"""Assignment will remain in PENDING state if no active capacity
        commitment is present. It will become ACTIVE when some capacity
        commitment becomes active.

        Values:
            STATE_UNSPECIFIED (0):
                Invalid state value.
            PENDING (1):
                Queries from assignee will be executed as
                on-demand, if related assignment is pending.
            ACTIVE (2):
                Assignment is ready.
        """

        STATE_UNSPECIFIED = 0
        PENDING = 1
        ACTIVE = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    assignee: str = proto.Field(
        proto.STRING,
        number=4,
    )
    job_type: JobType = proto.Field(
        proto.ENUM,
        number=3,
        enum=JobType,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=6,
        enum=State,
    )
    enable_gemini_in_bigquery: bool = proto.Field(
        proto.BOOL,
        number=10,
    )
    scheduling_policy: "SchedulingPolicy" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="SchedulingPolicy",
    )
    principal: str = proto.Field(
        proto.STRING,
        number=12,
    )
    precedence: int = proto.Field(
        proto.INT64,
        number=13,
    )
    condition: expr_pb2.Expr = proto.Field(
        proto.MESSAGE,
        number=14,
        message=expr_pb2.Expr,
    )


class CreateAssignmentRequest(proto.Message):
    r"""The request for
    [ReservationService.CreateAssignment][google.cloud.bigquery.reservation.v1.ReservationService.CreateAssignment].
    Note: "bigquery.reservationAssignments.create" permission is
    required on the related assignee.

    Attributes:
        parent (str):
            Required. The parent resource name of the assignment E.g.
            ``projects/myproject/locations/US/reservations/team1-prod``
        assignment (google.cloud.bigquery_reservation_v1.types.Assignment):
            Assignment resource to create.
        assignment_id (str):
            The optional assignment ID. Assignment name
            will be generated automatically if this field is
            empty. This field must only contain lower case
            alphanumeric characters or dashes. Max length is
            64 characters.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    assignment: "Assignment" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Assignment",
    )
    assignment_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListAssignmentsRequest(proto.Message):
    r"""The request for
    [ReservationService.ListAssignments][google.cloud.bigquery.reservation.v1.ReservationService.ListAssignments].

    Attributes:
        parent (str):
            Required. The parent resource name e.g.:

            ``projects/myproject/locations/US/reservations/team1-prod``

            Or:

            ``projects/myproject/locations/US/reservations/-``
        page_size (int):
            The maximum number of items to return per
            page.
        page_token (str):
            The next_page_token value returned from a previous List
            request, if any.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListAssignmentsResponse(proto.Message):
    r"""The response for
    [ReservationService.ListAssignments][google.cloud.bigquery.reservation.v1.ReservationService.ListAssignments].

    Attributes:
        assignments (MutableSequence[google.cloud.bigquery_reservation_v1.types.Assignment]):
            List of assignments visible to the user.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    assignments: MutableSequence["Assignment"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Assignment",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteAssignmentRequest(proto.Message):
    r"""The request for
    [ReservationService.DeleteAssignment][google.cloud.bigquery.reservation.v1.ReservationService.DeleteAssignment].
    Note: "bigquery.reservationAssignments.delete" permission is
    required on the related assignee.

    Attributes:
        name (str):
            Required. Name of the resource, e.g.
            ``projects/myproject/locations/US/reservations/team1-prod/assignments/123``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SearchAssignmentsRequest(proto.Message):
    r"""The request for
    [ReservationService.SearchAssignments][google.cloud.bigquery.reservation.v1.ReservationService.SearchAssignments].
    Note: "bigquery.reservationAssignments.search" permission is
    required on the related assignee.

    Attributes:
        parent (str):
            Required. The resource name of the admin project(containing
            project and location), e.g.:
            ``projects/myproject/locations/US``.
        query (str):
            Please specify resource name as assignee in the query.

            Examples:

            - ``assignee=projects/myproject``
            - ``assignee=folders/123``
            - ``assignee=organizations/456``
        page_size (int):
            The maximum number of items to return per
            page.
        page_token (str):
            The next_page_token value returned from a previous List
            request, if any.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    query: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class SearchAllAssignmentsRequest(proto.Message):
    r"""The request for
    [ReservationService.SearchAllAssignments][google.cloud.bigquery.reservation.v1.ReservationService.SearchAllAssignments].
    Note: "bigquery.reservationAssignments.search" permission is
    required on the related assignee.

    Attributes:
        parent (str):
            Required. The resource name with location (project name
            could be the wildcard '-'), e.g.:
            ``projects/-/locations/US``.
        query (str):
            Please specify resource name as assignee in the query.

            Examples:

            - ``assignee=projects/myproject``
            - ``assignee=folders/123``
            - ``assignee=organizations/456``
        page_size (int):
            The maximum number of items to return per
            page.
        page_token (str):
            The next_page_token value returned from a previous List
            request, if any.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    query: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class SearchAssignmentsResponse(proto.Message):
    r"""The response for
    [ReservationService.SearchAssignments][google.cloud.bigquery.reservation.v1.ReservationService.SearchAssignments].

    Attributes:
        assignments (MutableSequence[google.cloud.bigquery_reservation_v1.types.Assignment]):
            List of assignments visible to the user.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    assignments: MutableSequence["Assignment"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Assignment",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SearchAllAssignmentsResponse(proto.Message):
    r"""The response for
    [ReservationService.SearchAllAssignments][google.cloud.bigquery.reservation.v1.ReservationService.SearchAllAssignments].

    Attributes:
        assignments (MutableSequence[google.cloud.bigquery_reservation_v1.types.Assignment]):
            List of assignments visible to the user.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    assignments: MutableSequence["Assignment"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Assignment",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class MoveAssignmentRequest(proto.Message):
    r"""The request for
    [ReservationService.MoveAssignment][google.cloud.bigquery.reservation.v1.ReservationService.MoveAssignment].

    **Note**: "bigquery.reservationAssignments.create" permission is
    required on the destination_id.

    **Note**: "bigquery.reservationAssignments.create" and
    "bigquery.reservationAssignments.delete" permission are required on
    the related assignee.

    Attributes:
        name (str):
            Required. The resource name of the assignment, e.g.
            ``projects/myproject/locations/US/reservations/team1-prod/assignments/123``
        destination_id (str):
            The new reservation ID, e.g.:
            ``projects/myotherproject/locations/US/reservations/team2-prod``
        assignment_id (str):
            The optional assignment ID. A new assignment
            name is generated if this field is empty.

            This field can contain only lowercase
            alphanumeric characters or dashes. Max length is
            64 characters.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    destination_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    assignment_id: str = proto.Field(
        proto.STRING,
        number=5,
    )


class UpdateAssignmentRequest(proto.Message):
    r"""The request for
    [ReservationService.UpdateAssignment][google.cloud.bigquery.reservation.v1.ReservationService.UpdateAssignment].

    Attributes:
        assignment (google.cloud.bigquery_reservation_v1.types.Assignment):
            Content of the assignment to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Standard field mask for the set of fields to
            be updated.
    """

    assignment: "Assignment" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Assignment",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class TableReference(proto.Message):
    r"""Fully qualified reference to BigQuery table.
    Internally stored as google.cloud.bi.v1.BqTableReference.

    Attributes:
        project_id (str):
            Optional. The assigned project ID of the
            project.
        dataset_id (str):
            Optional. The ID of the dataset in the above
            project.
        table_id (str):
            Optional. The ID of the table in the above
            dataset.
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    dataset_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    table_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class BiReservation(proto.Message):
    r"""Represents a BI Reservation.

    Attributes:
        name (str):
            Identifier. The resource name of the singleton BI
            reservation. Reservation names have the form
            ``projects/{project_id}/locations/{location_id}/biReservation``.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last update timestamp of a
            reservation.
        size (int):
            Optional. Size of a reservation, in bytes.
        preferred_tables (MutableSequence[google.cloud.bigquery_reservation_v1.types.TableReference]):
            Optional. Preferred tables to use BI capacity
            for.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    size: int = proto.Field(
        proto.INT64,
        number=4,
    )
    preferred_tables: MutableSequence["TableReference"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="TableReference",
    )


class GetBiReservationRequest(proto.Message):
    r"""A request to get a singleton BI reservation.

    Attributes:
        name (str):
            Required. Name of the requested reservation, for example:
            ``projects/{project_id}/locations/{location_id}/biReservation``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateBiReservationRequest(proto.Message):
    r"""A request to update a BI reservation.

    Attributes:
        bi_reservation (google.cloud.bigquery_reservation_v1.types.BiReservation):
            A reservation to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            A list of fields to be updated in this
            request.
    """

    bi_reservation: "BiReservation" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="BiReservation",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
