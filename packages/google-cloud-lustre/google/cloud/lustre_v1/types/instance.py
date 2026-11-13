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
import google.type.date_pb2 as date_pb2  # type: ignore
import google.type.dayofweek_pb2 as dayofweek_pb2  # type: ignore
import google.type.timeofday_pb2 as timeofday_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.lustre.v1",
    manifest={
        "Instance",
        "DynamicTierOptions",
        "AccessRulesOptions",
        "ListInstancesRequest",
        "ListInstancesResponse",
        "GetInstanceRequest",
        "CreateInstanceRequest",
        "UpdateInstanceRequest",
        "DeleteInstanceRequest",
        "OperationMetadata",
        "MaintenancePolicy",
        "MaintenanceSchedule",
        "RescheduleMaintenanceRequest",
    },
)


class Instance(proto.Message):
    r"""A Managed Lustre instance.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The name of the instance.
        filesystem (str):
            Required. Immutable. The filesystem name for
            this instance. This name is used by client-side
            tools, including when mounting the instance.
            Must be eight characters or less and can only
            contain letters and numbers.
        capacity_gib (int):
            Required. The storage capacity of the instance in gibibytes
            (GiB). Allowed values depend on the
            ``perUnitStorageThroughput``. See `Performance
            tiers <https://docs.cloud.google.com/managed-lustre/docs/performance-tiers>`__
            for specific minimums, maximums, and step sizes for each
            performance tier.
        network (str):
            Required. Immutable. The full name of the VPC network to
            which the instance is connected. Must be in the format
            ``projects/{project_id}/global/networks/{network_name}``.
        state (google.cloud.lustre_v1.types.Instance.State):
            Output only. The state of the instance.
        mount_point (str):
            Output only. Mount point of the instance in the format
            ``IP_ADDRESS@tcp:/FILESYSTEM``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the instance was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the instance was
            last updated.
        description (str):
            Optional. A user-readable description of the
            instance.
        labels (MutableMapping[str, str]):
            Optional. Labels as key value pairs.
        per_unit_storage_throughput (int):
            Optional. The throughput of the instance in MBps per TiB.
            Valid values are 0, 125, 250, 500, 1000. See `Performance
            tiers <https://docs.cloud.google.com/managed-lustre/docs/performance-tiers>`__
            for more information.

            If the instance is using the Dynamic tier, this field must
            not be set or must be set to zero.
        gke_support_enabled (bool):
            Optional. Deprecated: No longer required for
            GKE instance creation. Indicates whether you
            want to enable support for GKE clients. By
            default, GKE clients are not supported.
        kms_key (str):
            Optional. Immutable. The Cloud KMS key name to use for data
            encryption. If not set, the instance will use Google-managed
            encryption keys. If set, the instance will use
            customer-managed encryption keys. The key must be in the
            same region as the instance. The key format is:
            projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{key}
        state_reason (str):
            Output only. The reason why the instance is
            in a certain state (e.g. SUSPENDED).
        placement_policy (str):
            Optional. The placement policy name for the instance in the
            format of
            projects/{project}/locations/{location}/resourcePolicies/{resource_policy}
        access_rules_options (google.cloud.lustre_v1.types.AccessRulesOptions):
            Optional. The access rules options for the
            instance.
        uid (str):
            Output only. Unique ID of the resource.
            This is unrelated to the access rules which
            allow specifying the root squash uid.
        maintenance_policy (google.cloud.lustre_v1.types.MaintenancePolicy):
            Optional. The maintenance policy for the
            instance to determine when to allow or exclude
            the instance from maintenance updates.
        upcoming_maintenance_schedule (google.cloud.lustre_v1.types.MaintenanceSchedule):
            Output only. Date and time of upcoming
            maintenance for the instance, if a maintenance
            policy is set.
        dynamic_tier_options (google.cloud.lustre_v1.types.DynamicTierOptions):
            Optional. Immutable. Specifies whether the instance is on
            the Dynamic tier. See `Performance
            tiers <https://docs.cloud.google.com/managed-lustre/docs/performance-tiers>`__
            for more information.
        available_version (str):
            Output only. The available version that this instance can be
            upgraded to. Format: ``Lustre_YYYYMMDD.NN_pXX``

            This field is a member of `oneof`_ ``_available_version``.
        target_version (str):
            Optional. The target version of the instance. Setting this
            field triggers a self-service update to the specified
            version. Format: ``Lustre_YYYYMMDD.NN_pXX`` or ``latest``

            This field is a member of `oneof`_ ``_target_version``.
        effective_version (str):
            Output only. The effective version of the instance. Format:
            ``Lustre_YYYYMMDD.NN_pXX``

            This field is a member of `oneof`_ ``_effective_version``.
    """

    class State(proto.Enum):
        r"""The possible states of an instance.

        Values:
            STATE_UNSPECIFIED (0):
                Not set.
            ACTIVE (1):
                The instance is available for use.
            CREATING (2):
                The instance is being created and is not yet
                ready for use.
            DELETING (3):
                The instance is being deleted.
            UPGRADING (4):
                The instance is being upgraded.
            REPAIRING (5):
                The instance is being repaired.
            STOPPED (6):
                The instance is stopped.
            UPDATING (7):
                The instance is being updated.
            SUSPENDED (8):
                The instance is suspended due to an issue related to Cloud
                KMS. The details are available in
                [state_reason][google.cloud.lustre.v1.Instance.state_reason].
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        CREATING = 2
        DELETING = 3
        UPGRADING = 4
        REPAIRING = 5
        STOPPED = 6
        UPDATING = 7
        SUSPENDED = 8

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filesystem: str = proto.Field(
        proto.STRING,
        number=10,
    )
    capacity_gib: int = proto.Field(
        proto.INT64,
        number=2,
    )
    network: str = proto.Field(
        proto.STRING,
        number=3,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )
    mount_point: str = proto.Field(
        proto.STRING,
        number=5,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    description: str = proto.Field(
        proto.STRING,
        number=8,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=9,
    )
    per_unit_storage_throughput: int = proto.Field(
        proto.INT64,
        number=11,
    )
    gke_support_enabled: bool = proto.Field(
        proto.BOOL,
        number=12,
    )
    kms_key: str = proto.Field(
        proto.STRING,
        number=13,
    )
    state_reason: str = proto.Field(
        proto.STRING,
        number=14,
    )
    placement_policy: str = proto.Field(
        proto.STRING,
        number=17,
    )
    access_rules_options: "AccessRulesOptions" = proto.Field(
        proto.MESSAGE,
        number=18,
        message="AccessRulesOptions",
    )
    uid: str = proto.Field(
        proto.STRING,
        number=19,
    )
    maintenance_policy: "MaintenancePolicy" = proto.Field(
        proto.MESSAGE,
        number=20,
        message="MaintenancePolicy",
    )
    upcoming_maintenance_schedule: "MaintenanceSchedule" = proto.Field(
        proto.MESSAGE,
        number=21,
        message="MaintenanceSchedule",
    )
    dynamic_tier_options: "DynamicTierOptions" = proto.Field(
        proto.MESSAGE,
        number=24,
        message="DynamicTierOptions",
    )
    available_version: str = proto.Field(
        proto.STRING,
        number=33,
        optional=True,
    )
    target_version: str = proto.Field(
        proto.STRING,
        number=34,
        optional=True,
    )
    effective_version: str = proto.Field(
        proto.STRING,
        number=35,
        optional=True,
    )


class DynamicTierOptions(proto.Message):
    r"""Dynamic tier options for a Managed Lustre instance.

    Attributes:
        mode (google.cloud.lustre_v1.types.DynamicTierOptions.Mode):
            Required. Immutable. The dynamic tier mode of
            the instance.
    """

    class Mode(proto.Enum):
        r"""Specifies the Dynamic performance tier for the instance.

        If this field is set to ``DEFAULT_CACHE``,
        ``per_unit_storage_throughput`` must not be set or must be set to
        zero.

        Values:
            MODE_UNSPECIFIED (0):
                Unspecified dynamic tier mode.
            DISABLED (1):
                The dynamic tier is explicitly disabled.
            DEFAULT_CACHE (2):
                The dynamic tier is enabled.
        """

        MODE_UNSPECIFIED = 0
        DISABLED = 1
        DEFAULT_CACHE = 2

    mode: Mode = proto.Field(
        proto.ENUM,
        number=1,
        enum=Mode,
    )


class AccessRulesOptions(proto.Message):
    r"""IP-based access rules for the Managed Lustre instance. These
    options define the root user squash configuration.

    Attributes:
        access_rules (MutableSequence[google.cloud.lustre_v1.types.AccessRulesOptions.AccessRule]):
            Optional. The access rules for the instance.
        default_squash_mode (google.cloud.lustre_v1.types.AccessRulesOptions.SquashMode):
            Required. The squash mode for the default
            access rule.
        default_squash_uid (int):
            Optional. The user squash UID for the default
            access rule. This user squash UID applies to all
            root users connecting from clients that are not
            matched by any of the access rules. If not set,
            the default is 0 (no UID squash).
        default_squash_gid (int):
            Optional. The user squash GID for the default
            access rule. This user squash GID applies to all
            root users connecting from clients that are not
            matched by any of the access rules. If not set,
            the default is 0 (no GID squash).
    """

    class SquashMode(proto.Enum):
        r"""Squash mode for an access rule.

        Values:
            SQUASH_MODE_UNSPECIFIED (0):
                Unspecified squash mode.
            NO_SQUASH (1):
                Squash is disabled.

                If set inside an
                [AccessRule][google.cloud.lustre.v1.AccessRulesOptions.AccessRule],
                root users matching the [ip_ranges][AccessRule.ip_ranges]
                are not squashed.

                If set as the
                [default_squash_mode][google.cloud.lustre.v1.AccessRulesOptions.default_squash_mode],
                root squash is disabled for this instance.

                If the default squash mode is ``NO_SQUASH``, do not set the
                [default_squash_uid][google.cloud.lustre.v1.AccessRulesOptions.default_squash_uid]
                or
                [default_squash_gid][google.cloud.lustre.v1.AccessRulesOptions.default_squash_gid],
                or an ``invalid argument`` error is returned.
            ROOT_SQUASH (2):
                Root user squash is enabled.

                Not supported inside an
                [AccessRule][google.cloud.lustre.v1.AccessRulesOptions.AccessRule].

                If set as the
                [default_squash_mode][google.cloud.lustre.v1.AccessRulesOptions.default_squash_mode],
                root users not matching any of the
                [access_rules][google.cloud.lustre.v1.AccessRulesOptions.access_rules]
                are squashed to the
                [default_squash_uid][google.cloud.lustre.v1.AccessRulesOptions.default_squash_uid]
                and
                [default_squash_gid][google.cloud.lustre.v1.AccessRulesOptions.default_squash_gid].
        """

        SQUASH_MODE_UNSPECIFIED = 0
        NO_SQUASH = 1
        ROOT_SQUASH = 2

    class AccessRule(proto.Message):
        r"""A single policy group with IP-based access rules for the
        Managed Lustre instance.

        Attributes:
            name (str):
                Required. The name of the access rule policy group. Must be
                16 characters or less and include only alphanumeric
                characters or '\_'.
            ip_address_ranges (MutableSequence[str]):
                Required. The IP address ranges to which to apply this
                access rule. Accepts non-overlapping CIDR ranges (e.g.,
                ``192.168.1.0/24``) and IP addresses (e.g.,
                ``192.168.1.0``).
            squash_mode (google.cloud.lustre_v1.types.AccessRulesOptions.SquashMode):
                Required. Squash mode for the access rule.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        ip_address_ranges: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )
        squash_mode: "AccessRulesOptions.SquashMode" = proto.Field(
            proto.ENUM,
            number=6,
            enum="AccessRulesOptions.SquashMode",
        )

    access_rules: MutableSequence[AccessRule] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=AccessRule,
    )
    default_squash_mode: SquashMode = proto.Field(
        proto.ENUM,
        number=2,
        enum=SquashMode,
    )
    default_squash_uid: int = proto.Field(
        proto.INT32,
        number=3,
    )
    default_squash_gid: int = proto.Field(
        proto.INT32,
        number=4,
    )


class ListInstancesRequest(proto.Message):
    r"""Message for requesting list of Instances

    Attributes:
        parent (str):
            Required. The project and location for which to retrieve a
            list of instances, in the format
            ``projects/{projectId}/locations/{location}``.

            To retrieve instance information for all locations, use "-"
            as the value of ``{location}``.
        page_size (int):
            Optional. Requested page size. Server might
            return fewer items than requested. If
            unspecified, the server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filtering results.
        order_by (str):
            Optional. Desired order of results.
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
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListInstancesResponse(proto.Message):
    r"""Message for response to listing Instances

    Attributes:
        instances (MutableSequence[google.cloud.lustre_v1.types.Instance]):
            Response from
            [ListInstances][google.cloud.lustre.v1.Lustre.ListInstances].
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Unordered list. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    instances: MutableSequence["Instance"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Instance",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetInstanceRequest(proto.Message):
    r"""Message for getting a Instance

    Attributes:
        name (str):
            Required. The instance resource name, in the format
            ``projects/{projectId}/locations/{location}/instances/{instanceId}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateInstanceRequest(proto.Message):
    r"""Message for creating a Instance

    Attributes:
        parent (str):
            Required. The instance's project and location, in the format
            ``projects/{project}/locations/{location}``. Locations map
            to Google Cloud zones; for example, ``us-west1-b``.
        instance_id (str):
            Required. The name of the Managed Lustre instance.

            - Must contain only lowercase letters, numbers, and hyphens.
            - Must start with a letter.
            - Must be between 1-63 characters.
            - Must end with a number or a letter.
        instance (google.cloud.lustre_v1.types.Instance):
            Required. The resource being created
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    instance: "Instance" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Instance",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateInstanceRequest(proto.Message):
    r"""Message for updating a Instance

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Specifies the fields to be overwritten in the
            instance resource by the update.

            The fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If no mask is provided then all fields
            present in the request are overwritten.
        instance (google.cloud.lustre_v1.types.Instance):
            Required. The resource name of the instance to update, in
            the format
            ``projects/{projectId}/locations/{location}/instances/{instanceId}``.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    instance: "Instance" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Instance",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteInstanceRequest(proto.Message):
    r"""Message for deleting a Instance

    Attributes:
        name (str):
            Required. The resource name of the instance to delete, in
            the format
            ``projects/{projectId}/locations/{location}/instances/{instanceId}``.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        force (bool):
            Optional. If set to true, any sub-resources
            from this instance will also be deleted.
            Otherwise, the request will only work if the
            instance has no sub-resources.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class OperationMetadata(proto.Message):
    r"""Represents the metadata of a long-running operation.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        target (str):
            Output only. Server-defined resource path for
            the target of the operation.
        verb (str):
            Output only. Name of the verb executed by the
            operation.
        status_message (str):
            Output only. Human-readable status of the
            operation, if any.
        requested_cancellation (bool):
            Output only. Identifies whether the user has requested
            cancellation of the operation. Operations that have been
            cancelled successfully have [Operation.error][] value with a
            [google.rpc.Status.code][google.rpc.Status.code] of 1,
            corresponding to ``Code.CANCELLED``.
        api_version (str):
            Output only. API version used to start the
            operation.
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    target: str = proto.Field(
        proto.STRING,
        number=3,
    )
    verb: str = proto.Field(
        proto.STRING,
        number=4,
    )
    status_message: str = proto.Field(
        proto.STRING,
        number=5,
    )
    requested_cancellation: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    api_version: str = proto.Field(
        proto.STRING,
        number=7,
    )


class MaintenancePolicy(proto.Message):
    r"""Defines a maintenance policy for a resource.

    Attributes:
        weekly_maintenance_windows (MutableSequence[google.cloud.lustre_v1.types.MaintenancePolicy.WeeklyMaintenanceWindow]):
            Required. The weekly maintenance windows for
            the instance. Currently limited to 1 window.
        maintenance_exclusion_window (MutableSequence[google.cloud.lustre_v1.types.MaintenancePolicy.MaintenanceExclusionWindow]):
            Optional. The exclusion windows for the
            instance. Currently limited to 1 window.
    """

    class WeeklyMaintenanceWindow(proto.Message):
        r"""Weekly time window in which maintenance updates may occur.
        Duration of the window is currently fixed at 1 hour. Time zone
        is UTC.

        Attributes:
            day_of_week (google.type.dayofweek_pb2.DayOfWeek):
                Required. Day of the week for the maintenance
                window.
            start_time (google.type.timeofday_pb2.TimeOfDay):
                Required. Start time of the maintenance
                window in UTC time zone.
        """

        day_of_week: dayofweek_pb2.DayOfWeek = proto.Field(
            proto.ENUM,
            number=1,
            enum=dayofweek_pb2.DayOfWeek,
        )
        start_time: timeofday_pb2.TimeOfDay = proto.Field(
            proto.MESSAGE,
            number=2,
            message=timeofday_pb2.TimeOfDay,
        )

    class MaintenanceExclusionWindow(proto.Message):
        r"""Exclusion period when maintenance updates should not occur. An
        exclusion window can be in either of the following two formats:

        - Non-recurring : A full date, with non-zero year, month and day
          values.
        - Recurring : A month and day value, with a zero year. Time zone is
          UTC.

        Attributes:
            start_date (google.type.date_pb2.Date):
                Required. Start date of the exclusion period
                in UTC time zone. This date is inclusive.
            end_date (google.type.date_pb2.Date):
                Required. End date of the exclusion period in
                UTC time zone. This date is inclusive.
            time (google.type.timeofday_pb2.TimeOfDay):
                Required. Time in UTC when the exclusion window starts on
                start_date and ends on end_date. This can be:

                - Full time OR
                - All zeros for 00:00:00 UTC
        """

        start_date: date_pb2.Date = proto.Field(
            proto.MESSAGE,
            number=1,
            message=date_pb2.Date,
        )
        end_date: date_pb2.Date = proto.Field(
            proto.MESSAGE,
            number=2,
            message=date_pb2.Date,
        )
        time: timeofday_pb2.TimeOfDay = proto.Field(
            proto.MESSAGE,
            number=3,
            message=timeofday_pb2.TimeOfDay,
        )

    weekly_maintenance_windows: MutableSequence[WeeklyMaintenanceWindow] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message=WeeklyMaintenanceWindow,
        )
    )
    maintenance_exclusion_window: MutableSequence[MaintenanceExclusionWindow] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message=MaintenanceExclusionWindow,
        )
    )


class MaintenanceSchedule(proto.Message):
    r"""Represents a scheduled maintenance event.

    Attributes:
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The scheduled start time for the
            maintenance.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The scheduled end time for the
            maintenance.
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


class RescheduleMaintenanceRequest(proto.Message):
    r"""Message for requesting to reschedule a maintenance event for
    a specific instance.

    Attributes:
        name (str):
            Required. Format:

            projects/{project}/locations/{location}/instances/{instance}
        reschedule (google.cloud.lustre_v1.types.RescheduleMaintenanceRequest.Reschedule):
            Required. The desired reschedule settings.
        request_id (str):
            Optional. A unique identifier for this request. A random
            UUID is recommended. This request is only idempotent if a
            ``request_id`` is provided.
    """

    class RescheduleType(proto.Enum):
        r"""The type of rescheduling event. More reschedule types may be
        added in the future.

        Values:
            RESCHEDULE_TYPE_UNSPECIFIED (0):
                Unspecified schedule type.
            IMMEDIATE (1):
                Apply update immediately
            NEXT_AVAILABLE_WINDOW (2):
                Reschedule to the next available window.
            BY_TIME (3):
                Reschedule to a specific time.
        """

        RESCHEDULE_TYPE_UNSPECIFIED = 0
        IMMEDIATE = 1
        NEXT_AVAILABLE_WINDOW = 2
        BY_TIME = 3

    class Reschedule(proto.Message):
        r"""The desired reschedule settings.

        Attributes:
            reschedule_type (google.cloud.lustre_v1.types.RescheduleMaintenanceRequest.RescheduleType):
                Required. The type of rescheduling.
            schedule_time (google.protobuf.timestamp_pb2.Timestamp):
                Optional. Required if reschedule_type is BY_TIME. Timestamp
                when the maintenance shall be rescheduled to. This time must
                be within 28 days of the original scheduled maintenance
                start time.
        """

        reschedule_type: "RescheduleMaintenanceRequest.RescheduleType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="RescheduleMaintenanceRequest.RescheduleType",
        )
        schedule_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=2,
            message=timestamp_pb2.Timestamp,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    reschedule: Reschedule = proto.Field(
        proto.MESSAGE,
        number=2,
        message=Reschedule,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
