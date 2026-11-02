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

import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.type.dayofweek_pb2 as dayofweek_pb2  # type: ignore
import google.type.timeofday_pb2 as timeofday_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.redis.v1beta1",
    manifest={
        "NodeInfo",
        "Instance",
        "PersistenceConfig",
        "RescheduleMaintenanceRequest",
        "MaintenancePolicy",
        "WeeklyMaintenanceWindow",
        "MaintenanceSchedule",
        "ListInstancesRequest",
        "ListInstancesResponse",
        "GetInstanceRequest",
        "GetInstanceAuthStringRequest",
        "InstanceAuthString",
        "CreateInstanceRequest",
        "UpdateInstanceRequest",
        "UpgradeInstanceRequest",
        "DeleteInstanceRequest",
        "GcsSource",
        "InputConfig",
        "ImportInstanceRequest",
        "GcsDestination",
        "OutputConfig",
        "ExportInstanceRequest",
        "FailoverInstanceRequest",
        "LocationMetadata",
        "ZoneMetadata",
        "TlsCertificate",
    },
)


class NodeInfo(proto.Message):
    r"""Node specific properties.

    Attributes:
        id (str):
            Output only. Node identifying string. e.g.
            'node-0', 'node-1'
        zone (str):
            Output only. Location of the node.
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    zone: str = proto.Field(
        proto.STRING,
        number=2,
    )


class Instance(proto.Message):
    r"""A Memorystore for Redis instance.

    Attributes:
        name (str):
            Required. Unique name of the resource in this scope
            including project and location using the form:
            ``projects/{project_id}/locations/{location_id}/instances/{instance_id}``

            Note: Redis instances are managed and addressed at regional
            level so location_id here refers to a GCP region; however,
            users may choose which specific zone (or collection of zones
            for cross-zone instances) an instance should be provisioned
            in. Refer to
            [location_id][google.cloud.redis.v1beta1.Instance.location_id]
            and
            [alternative_location_id][google.cloud.redis.v1beta1.Instance.alternative_location_id]
            fields for more details.
        display_name (str):
            An arbitrary and optional user-provided name
            for the instance.
        labels (MutableMapping[str, str]):
            Resource labels to represent user provided
            metadata
        location_id (str):
            Optional. The zone where the instance will be
            provisioned. If not provided, the service will
            choose a zone from the specified region for the
            instance. For standard tier, additional nodes
            will be added across multiple zones for
            protection against zonal failures. If specified,
            at least one node will be provisioned in this
            zone.
        alternative_location_id (str):
            Optional. If specified, at least one node will be
            provisioned in this zone in addition to the zone specified
            in location_id. Only applicable to standard tier. If
            provided, it must be a different zone from the one provided
            in [location_id]. Additional nodes beyond the first 2 will
            be placed in zones selected by the service.
        redis_version (str):
            Optional. The version of Redis software. If not provided,
            latest supported version will be used. Currently, the
            supported values are:

            - ``REDIS_3_2`` for Redis 3.2 compatibility
            - ``REDIS_4_0`` for Redis 4.0 compatibility (default)
            - ``REDIS_5_0`` for Redis 5.0 compatibility
            - ``REDIS_6_X`` for Redis 6.x compatibility
        reserved_ip_range (str):
            Optional. For DIRECT_PEERING mode, the CIDR range of
            internal addresses that are reserved for this instance.
            Range must be unique and non-overlapping with existing
            subnets in an authorized network. For PRIVATE_SERVICE_ACCESS
            mode, the name of one allocated IP address ranges associated
            with this private service access connection. If not
            provided, the service will choose an unused /29 block, for
            example, 10.0.0.0/29 or 192.168.0.0/29. For
            READ_REPLICAS_ENABLED the default block size is /28.
        secondary_ip_range (str):
            Optional. Additional IP range for node placement. Required
            when enabling read replicas on an existing instance. For
            DIRECT_PEERING mode value must be a CIDR range of size /28,
            or "auto". For PRIVATE_SERVICE_ACCESS mode value must be the
            name of an allocated address range associated with the
            private service access connection, or "auto".
        host (str):
            Output only. Hostname or IP address of the
            exposed Redis endpoint used by  clients to
            connect to the service.
        port (int):
            Output only. The port number of the exposed
            Redis endpoint.
        current_location_id (str):
            Output only. The current zone where the Redis primary node
            is located. In basic tier, this will always be the same as
            [location_id]. In standard tier, this can be the zone of any
            node in the instance.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the instance was
            created.
        state (google.cloud.redis_v1beta1.types.Instance.State):
            Output only. The current state of this
            instance.
        status_message (str):
            Output only. Additional information about the
            current status of this instance, if available.
        redis_configs (MutableMapping[str, str]):
            Optional. Redis configuration parameters, according to
            http://redis.io/topics/config. Currently, the only supported
            parameters are:

            Redis version 3.2 and newer:

            - maxmemory-policy
            - notify-keyspace-events

            Redis version 4.0 and newer:

            - activedefrag
            - lfu-decay-time
            - lfu-log-factor
            - maxmemory-gb

            Redis version 5.0 and newer:

            - stream-node-max-bytes
            - stream-node-max-entries
        tier (google.cloud.redis_v1beta1.types.Instance.Tier):
            Required. The service tier of the instance.
        memory_size_gb (int):
            Required. Redis memory size in GiB.
        authorized_network (str):
            Optional. The full name of the Google Compute Engine
            `network <https://cloud.google.com/vpc/docs/vpc>`__ to which
            the instance is connected. If left unspecified, the
            ``default`` network will be used.
        persistence_iam_identity (str):
            Output only. Cloud IAM identity used by import / export
            operations to transfer data to/from Cloud Storage. Format is
            "serviceAccount:<service_account_email>". The value may
            change over time for a given instance so should be checked
            before each import/export operation.
        connect_mode (google.cloud.redis_v1beta1.types.Instance.ConnectMode):
            Optional. The network connect mode of the Redis instance. If
            not provided, the connect mode defaults to DIRECT_PEERING.
        auth_enabled (bool):
            Optional. Indicates whether OSS Redis AUTH is
            enabled for the instance. If set to "true" AUTH
            is enabled on the instance. Default value is
            "false" meaning AUTH is disabled.
        server_ca_certs (MutableSequence[google.cloud.redis_v1beta1.types.TlsCertificate]):
            Output only. List of server CA certificates
            for the instance.
        transit_encryption_mode (google.cloud.redis_v1beta1.types.Instance.TransitEncryptionMode):
            Optional. The TLS mode of the Redis instance.
            If not provided, TLS is disabled for the
            instance.
        maintenance_policy (google.cloud.redis_v1beta1.types.MaintenancePolicy):
            Optional. The maintenance policy for the
            instance. If not provided, maintenance events
            can be performed at any time.
        maintenance_schedule (google.cloud.redis_v1beta1.types.MaintenanceSchedule):
            Output only. Date and time of upcoming
            maintenance events which have been scheduled.
        replica_count (int):
            Optional. The number of replica nodes. The valid range for
            the Standard Tier with read replicas enabled is [1-5] and
            defaults to 2. If read replicas are not enabled for a
            Standard Tier instance, the only valid value is 1 and the
            default is 1. The valid value for basic tier is 0 and the
            default is also 0.
        nodes (MutableSequence[google.cloud.redis_v1beta1.types.NodeInfo]):
            Output only. Info per node.
        read_endpoint (str):
            Output only. Hostname or IP address of the
            exposed readonly Redis endpoint. Standard tier
            only. Targets all healthy replica nodes in
            instance. Replication is asynchronous and
            replica nodes will exhibit some lag behind the
            primary. Write requests must target 'host'.
        read_endpoint_port (int):
            Output only. The port number of the exposed
            readonly redis endpoint. Standard tier only.
            Write requests should target 'port'.
        read_replicas_mode (google.cloud.redis_v1beta1.types.Instance.ReadReplicasMode):
            Optional. Read replicas mode for the instance. Defaults to
            READ_REPLICAS_DISABLED.
        persistence_config (google.cloud.redis_v1beta1.types.PersistenceConfig):
            Optional. Persistence configuration
            parameters
    """

    class State(proto.Enum):
        r"""Represents the different states of a Redis instance.

        Values:
            STATE_UNSPECIFIED (0):
                Not set.
            CREATING (1):
                Redis instance is being created.
            READY (2):
                Redis instance has been created and is fully
                usable.
            UPDATING (3):
                Redis instance configuration is being
                updated. Certain kinds of updates may cause the
                instance to become unusable while the update is
                in progress.
            DELETING (4):
                Redis instance is being deleted.
            REPAIRING (5):
                Redis instance is being repaired and may be
                unusable.
            MAINTENANCE (6):
                Maintenance is being performed on this Redis
                instance.
            IMPORTING (8):
                Redis instance is importing data
                (availability may be affected).
            FAILING_OVER (10):
                Redis instance is failing over (availability
                may be affected).
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        READY = 2
        UPDATING = 3
        DELETING = 4
        REPAIRING = 5
        MAINTENANCE = 6
        IMPORTING = 8
        FAILING_OVER = 10

    class Tier(proto.Enum):
        r"""Available service tiers to choose from

        Values:
            TIER_UNSPECIFIED (0):
                Not set.
            BASIC (1):
                BASIC tier: standalone instance
            STANDARD_HA (3):
                STANDARD_HA tier: highly available primary/replica instances
        """

        TIER_UNSPECIFIED = 0
        BASIC = 1
        STANDARD_HA = 3

    class ConnectMode(proto.Enum):
        r"""Available connection modes.

        Values:
            CONNECT_MODE_UNSPECIFIED (0):
                Not set.
            DIRECT_PEERING (1):
                Connect via direct peering to the Memorystore
                for Redis hosted service.
            PRIVATE_SERVICE_ACCESS (2):
                Connect your Memorystore for Redis instance
                using Private Service Access. Private services
                access provides an IP address range for multiple
                Google Cloud services, including Memorystore.
        """

        CONNECT_MODE_UNSPECIFIED = 0
        DIRECT_PEERING = 1
        PRIVATE_SERVICE_ACCESS = 2

    class TransitEncryptionMode(proto.Enum):
        r"""Available TLS modes.

        Values:
            TRANSIT_ENCRYPTION_MODE_UNSPECIFIED (0):
                Not set.
            SERVER_AUTHENTICATION (1):
                Client to Server traffic encryption enabled
                with server authentication.
            DISABLED (2):
                TLS is disabled for the instance.
        """

        TRANSIT_ENCRYPTION_MODE_UNSPECIFIED = 0
        SERVER_AUTHENTICATION = 1
        DISABLED = 2

    class ReadReplicasMode(proto.Enum):
        r"""Read replicas mode.

        Values:
            READ_REPLICAS_MODE_UNSPECIFIED (0):
                If not set, Memorystore Redis backend will default to
                READ_REPLICAS_DISABLED.
            READ_REPLICAS_DISABLED (1):
                If disabled, read endpoint will not be
                provided and the instance cannot scale up or
                down the number of replicas.
            READ_REPLICAS_ENABLED (2):
                If enabled, read endpoint will be provided
                and the instance can scale up and down the
                number of replicas. Not valid for basic tier.
        """

        READ_REPLICAS_MODE_UNSPECIFIED = 0
        READ_REPLICAS_DISABLED = 1
        READ_REPLICAS_ENABLED = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )
    location_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    alternative_location_id: str = proto.Field(
        proto.STRING,
        number=5,
    )
    redis_version: str = proto.Field(
        proto.STRING,
        number=7,
    )
    reserved_ip_range: str = proto.Field(
        proto.STRING,
        number=9,
    )
    secondary_ip_range: str = proto.Field(
        proto.STRING,
        number=30,
    )
    host: str = proto.Field(
        proto.STRING,
        number=10,
    )
    port: int = proto.Field(
        proto.INT32,
        number=11,
    )
    current_location_id: str = proto.Field(
        proto.STRING,
        number=12,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=13,
        message=timestamp_pb2.Timestamp,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=14,
        enum=State,
    )
    status_message: str = proto.Field(
        proto.STRING,
        number=15,
    )
    redis_configs: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=16,
    )
    tier: Tier = proto.Field(
        proto.ENUM,
        number=17,
        enum=Tier,
    )
    memory_size_gb: int = proto.Field(
        proto.INT32,
        number=18,
    )
    authorized_network: str = proto.Field(
        proto.STRING,
        number=20,
    )
    persistence_iam_identity: str = proto.Field(
        proto.STRING,
        number=21,
    )
    connect_mode: ConnectMode = proto.Field(
        proto.ENUM,
        number=22,
        enum=ConnectMode,
    )
    auth_enabled: bool = proto.Field(
        proto.BOOL,
        number=23,
    )
    server_ca_certs: MutableSequence["TlsCertificate"] = proto.RepeatedField(
        proto.MESSAGE,
        number=25,
        message="TlsCertificate",
    )
    transit_encryption_mode: TransitEncryptionMode = proto.Field(
        proto.ENUM,
        number=26,
        enum=TransitEncryptionMode,
    )
    maintenance_policy: "MaintenancePolicy" = proto.Field(
        proto.MESSAGE,
        number=27,
        message="MaintenancePolicy",
    )
    maintenance_schedule: "MaintenanceSchedule" = proto.Field(
        proto.MESSAGE,
        number=28,
        message="MaintenanceSchedule",
    )
    replica_count: int = proto.Field(
        proto.INT32,
        number=31,
    )
    nodes: MutableSequence["NodeInfo"] = proto.RepeatedField(
        proto.MESSAGE,
        number=32,
        message="NodeInfo",
    )
    read_endpoint: str = proto.Field(
        proto.STRING,
        number=33,
    )
    read_endpoint_port: int = proto.Field(
        proto.INT32,
        number=34,
    )
    read_replicas_mode: ReadReplicasMode = proto.Field(
        proto.ENUM,
        number=35,
        enum=ReadReplicasMode,
    )
    persistence_config: "PersistenceConfig" = proto.Field(
        proto.MESSAGE,
        number=37,
        message="PersistenceConfig",
    )


class PersistenceConfig(proto.Message):
    r"""Configuration of the persistence functionality.

    Attributes:
        persistence_mode (google.cloud.redis_v1beta1.types.PersistenceConfig.PersistenceMode):
            Optional. Controls whether Persistence
            features are enabled. If not provided, the
            existing value will be used.
        rdb_snapshot_period (google.cloud.redis_v1beta1.types.PersistenceConfig.SnapshotPeriod):
            Optional. Period between RDB snapshots. Snapshots will be
            attempted every period starting from the provided snapshot
            start time. For example, a start time of 01/01/2033 06:45
            and SIX_HOURS snapshot period will do nothing until
            01/01/2033, and then trigger snapshots every day at 06:45,
            12:45, 18:45, and 00:45 the next day, and so on. If not
            provided, TWENTY_FOUR_HOURS will be used as default.
        rdb_next_snapshot_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The next time that a snapshot
            attempt is scheduled to occur.
        rdb_snapshot_start_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. Date and time that the first
            snapshot was/will be attempted, and to which
            future snapshots will be aligned. If not
            provided, the current time will be used.
    """

    class PersistenceMode(proto.Enum):
        r"""Available Persistence modes.

        Values:
            PERSISTENCE_MODE_UNSPECIFIED (0):
                Not set.
            DISABLED (1):
                Persistence is disabled for the instance,
                and any existing snapshots are deleted.
            RDB (2):
                RDB based Persistence is enabled.
        """

        PERSISTENCE_MODE_UNSPECIFIED = 0
        DISABLED = 1
        RDB = 2

    class SnapshotPeriod(proto.Enum):
        r"""Available snapshot periods for scheduling.

        Values:
            SNAPSHOT_PERIOD_UNSPECIFIED (0):
                Not set.
            ONE_HOUR (3):
                Snapshot every 1 hour.
            SIX_HOURS (4):
                Snapshot every 6 hours.
            TWELVE_HOURS (5):
                Snapshot every 12 hours.
            TWENTY_FOUR_HOURS (6):
                Snapshot every 24 hours.
        """

        SNAPSHOT_PERIOD_UNSPECIFIED = 0
        ONE_HOUR = 3
        SIX_HOURS = 4
        TWELVE_HOURS = 5
        TWENTY_FOUR_HOURS = 6

    persistence_mode: PersistenceMode = proto.Field(
        proto.ENUM,
        number=1,
        enum=PersistenceMode,
    )
    rdb_snapshot_period: SnapshotPeriod = proto.Field(
        proto.ENUM,
        number=2,
        enum=SnapshotPeriod,
    )
    rdb_next_snapshot_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    rdb_snapshot_start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )


class RescheduleMaintenanceRequest(proto.Message):
    r"""Request for
    [RescheduleMaintenance][google.cloud.redis.v1beta1.CloudRedis.RescheduleMaintenance].

    Attributes:
        name (str):
            Required. Redis instance resource name using the form:
            ``projects/{project_id}/locations/{location_id}/instances/{instance_id}``
            where ``location_id`` refers to a GCP region.
        reschedule_type (google.cloud.redis_v1beta1.types.RescheduleMaintenanceRequest.RescheduleType):
            Required. If reschedule type is SPECIFIC_TIME, must set up
            schedule_time as well.
        schedule_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. Timestamp when the maintenance shall be
            rescheduled to if reschedule_type=SPECIFIC_TIME, in RFC 3339
            format, for example ``2012-11-15T16:19:00.094Z``.
    """

    class RescheduleType(proto.Enum):
        r"""Reschedule options.

        Values:
            RESCHEDULE_TYPE_UNSPECIFIED (0):
                Not set.
            IMMEDIATE (1):
                If the user wants to schedule the maintenance
                to happen now.
            NEXT_AVAILABLE_WINDOW (2):
                If the user wants to use the existing
                maintenance policy to find the next available
                window.
            SPECIFIC_TIME (3):
                If the user wants to reschedule the
                maintenance to a specific time.
        """

        RESCHEDULE_TYPE_UNSPECIFIED = 0
        IMMEDIATE = 1
        NEXT_AVAILABLE_WINDOW = 2
        SPECIFIC_TIME = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    reschedule_type: RescheduleType = proto.Field(
        proto.ENUM,
        number=2,
        enum=RescheduleType,
    )
    schedule_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


class MaintenancePolicy(proto.Message):
    r"""Maintenance policy for an instance.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the policy was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the policy was
            last updated.
        description (str):
            Optional. Description of what this policy is for.
            Create/Update methods return INVALID_ARGUMENT if the length
            is greater than 512.
        weekly_maintenance_window (MutableSequence[google.cloud.redis_v1beta1.types.WeeklyMaintenanceWindow]):
            Optional. Maintenance window that is applied to resources
            covered by this policy. Minimum 1. For the current version,
            the maximum number of weekly_window is expected to be one.
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    weekly_maintenance_window: MutableSequence["WeeklyMaintenanceWindow"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message="WeeklyMaintenanceWindow",
        )
    )


class WeeklyMaintenanceWindow(proto.Message):
    r"""Time window in which disruptive maintenance updates occur.
    Non-disruptive updates can occur inside or outside this window.

    Attributes:
        day (google.type.dayofweek_pb2.DayOfWeek):
            Required. The day of week that maintenance
            updates occur.
        start_time (google.type.timeofday_pb2.TimeOfDay):
            Required. Start time of the window in UTC
            time.
        duration (google.protobuf.duration_pb2.Duration):
            Output only. Duration of the maintenance
            window. The current window is fixed at 1 hour.
    """

    day: dayofweek_pb2.DayOfWeek = proto.Field(
        proto.ENUM,
        number=1,
        enum=dayofweek_pb2.DayOfWeek,
    )
    start_time: timeofday_pb2.TimeOfDay = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timeofday_pb2.TimeOfDay,
    )
    duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=3,
        message=duration_pb2.Duration,
    )


class MaintenanceSchedule(proto.Message):
    r"""Upcoming maintenance schedule. If no maintenance is
    scheduled, fields are not populated.

    Attributes:
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The start time of any upcoming
            scheduled maintenance for this instance.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The end time of any upcoming
            scheduled maintenance for this instance.
        can_reschedule (bool):
            If the scheduled maintenance can be
            rescheduled, default is true.
        schedule_deadline_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The deadline that the
            maintenance schedule start time can not go
            beyond, including reschedule.
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
    can_reschedule: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    schedule_deadline_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )


class ListInstancesRequest(proto.Message):
    r"""Request for
    [ListInstances][google.cloud.redis.v1beta1.CloudRedis.ListInstances].

    Attributes:
        parent (str):
            Required. The resource name of the instance location using
            the form: ``projects/{project_id}/locations/{location_id}``
            where ``location_id`` refers to a GCP region.
        page_size (int):
            The maximum number of items to return.

            If not specified, a default value of 1000 will be used by
            the service. Regardless of the page_size value, the response
            may include a partial list and a caller should only rely on
            response's
            [``next_page_token``][google.cloud.redis.v1beta1.ListInstancesResponse.next_page_token]
            to determine if there are more instances left to be queried.
        page_token (str):
            The ``next_page_token`` value returned from a previous
            [ListInstances][google.cloud.redis.v1beta1.CloudRedis.ListInstances]
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


class ListInstancesResponse(proto.Message):
    r"""Response for
    [ListInstances][google.cloud.redis.v1beta1.CloudRedis.ListInstances].

    Attributes:
        instances (MutableSequence[google.cloud.redis_v1beta1.types.Instance]):
            A list of Redis instances in the project in the specified
            location, or across all locations.

            If the ``location_id`` in the parent field of the request is
            "-", all regions available to the project are queried, and
            the results aggregated. If in such an aggregated query a
            location is unavailable, a placeholder Redis entry is
            included in the response with the ``name`` field set to a
            value of the form
            ``projects/{project_id}/locations/{location_id}/instances/``-
            and the ``status`` field set to ERROR and ``status_message``
            field set to "location not available for ListInstances".
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
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
    r"""Request for
    [GetInstance][google.cloud.redis.v1beta1.CloudRedis.GetInstance].

    Attributes:
        name (str):
            Required. Redis instance resource name using the form:
            ``projects/{project_id}/locations/{location_id}/instances/{instance_id}``
            where ``location_id`` refers to a GCP region.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetInstanceAuthStringRequest(proto.Message):
    r"""Request for
    [GetInstanceAuthString][google.cloud.redis.v1beta1.CloudRedis.GetInstanceAuthString].

    Attributes:
        name (str):
            Required. Redis instance resource name using the form:
            ``projects/{project_id}/locations/{location_id}/instances/{instance_id}``
            where ``location_id`` refers to a GCP region.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class InstanceAuthString(proto.Message):
    r"""Instance AUTH string details.

    Attributes:
        auth_string (str):
            AUTH string set on the instance.
    """

    auth_string: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateInstanceRequest(proto.Message):
    r"""Request for
    [CreateInstance][google.cloud.redis.v1beta1.CloudRedis.CreateInstance].

    Attributes:
        parent (str):
            Required. The resource name of the instance location using
            the form: ``projects/{project_id}/locations/{location_id}``
            where ``location_id`` refers to a GCP region.
        instance_id (str):
            Required. The logical name of the Redis instance in the
            customer project with the following restrictions:

            - Must contain only lowercase letters, numbers, and hyphens.
            - Must start with a letter.
            - Must be between 1-40 characters.
            - Must end with a number or a letter.
            - Must be unique within the customer project / location
        instance (google.cloud.redis_v1beta1.types.Instance):
            Required. A Redis [Instance] resource
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


class UpdateInstanceRequest(proto.Message):
    r"""Request for
    [UpdateInstance][google.cloud.redis.v1beta1.CloudRedis.UpdateInstance].

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Mask of fields to update. At least one path must
            be supplied in this field. The elements of the repeated
            paths field may only include these fields from
            [Instance][google.cloud.redis.v1beta1.Instance]:

            - ``displayName``
            - ``labels``
            - ``memorySizeGb``
            - ``redisConfig``
            - ``replica_count``
        instance (google.cloud.redis_v1beta1.types.Instance):
            Required. Update description. Only fields specified in
            update_mask are updated.
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


class UpgradeInstanceRequest(proto.Message):
    r"""Request for
    [UpgradeInstance][google.cloud.redis.v1beta1.CloudRedis.UpgradeInstance].

    Attributes:
        name (str):
            Required. Redis instance resource name using the form:
            ``projects/{project_id}/locations/{location_id}/instances/{instance_id}``
            where ``location_id`` refers to a GCP region.
        redis_version (str):
            Required. Specifies the target version of
            Redis software to upgrade to.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    redis_version: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteInstanceRequest(proto.Message):
    r"""Request for
    [DeleteInstance][google.cloud.redis.v1beta1.CloudRedis.DeleteInstance].

    Attributes:
        name (str):
            Required. Redis instance resource name using the form:
            ``projects/{project_id}/locations/{location_id}/instances/{instance_id}``
            where ``location_id`` refers to a GCP region.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GcsSource(proto.Message):
    r"""The Cloud Storage location for the input content

    Attributes:
        uri (str):
            Required. Source data URI. (e.g.
            'gs://my_bucket/my_object').
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )


class InputConfig(proto.Message):
    r"""The input content

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_source (google.cloud.redis_v1beta1.types.GcsSource):
            Google Cloud Storage location where input
            content is located.

            This field is a member of `oneof`_ ``source``.
    """

    gcs_source: "GcsSource" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="source",
        message="GcsSource",
    )


class ImportInstanceRequest(proto.Message):
    r"""Request for
    [Import][google.cloud.redis.v1beta1.CloudRedis.ImportInstance].

    Attributes:
        name (str):
            Required. Redis instance resource name using the form:
            ``projects/{project_id}/locations/{location_id}/instances/{instance_id}``
            where ``location_id`` refers to a GCP region.
        input_config (google.cloud.redis_v1beta1.types.InputConfig):
            Required. Specify data to be imported.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    input_config: "InputConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="InputConfig",
    )


class GcsDestination(proto.Message):
    r"""The Cloud Storage location for the output content

    Attributes:
        uri (str):
            Required. Data destination URI (e.g.
            'gs://my_bucket/my_object'). Existing files will be
            overwritten.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )


class OutputConfig(proto.Message):
    r"""The output content

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_destination (google.cloud.redis_v1beta1.types.GcsDestination):
            Google Cloud Storage destination for output
            content.

            This field is a member of `oneof`_ ``destination``.
    """

    gcs_destination: "GcsDestination" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="destination",
        message="GcsDestination",
    )


class ExportInstanceRequest(proto.Message):
    r"""Request for
    [Export][google.cloud.redis.v1beta1.CloudRedis.ExportInstance].

    Attributes:
        name (str):
            Required. Redis instance resource name using the form:
            ``projects/{project_id}/locations/{location_id}/instances/{instance_id}``
            where ``location_id`` refers to a GCP region.
        output_config (google.cloud.redis_v1beta1.types.OutputConfig):
            Required. Specify data to be exported.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    output_config: "OutputConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="OutputConfig",
    )


class FailoverInstanceRequest(proto.Message):
    r"""Request for
    [Failover][google.cloud.redis.v1beta1.CloudRedis.FailoverInstance].

    Attributes:
        name (str):
            Required. Redis instance resource name using the form:
            ``projects/{project_id}/locations/{location_id}/instances/{instance_id}``
            where ``location_id`` refers to a GCP region.
        data_protection_mode (google.cloud.redis_v1beta1.types.FailoverInstanceRequest.DataProtectionMode):
            Optional. Available data protection modes that the user can
            choose. If it's unspecified, data protection mode will be
            LIMITED_DATA_LOSS by default.
    """

    class DataProtectionMode(proto.Enum):
        r"""Specifies different modes of operation in relation to the
        data retention.

        Values:
            DATA_PROTECTION_MODE_UNSPECIFIED (0):
                Defaults to LIMITED_DATA_LOSS if a data protection mode is
                not specified.
            LIMITED_DATA_LOSS (1):
                Instance failover will be protected with data
                loss control. More specifically, the failover
                will only be performed if the current
                replication offset diff between primary and
                replica is under a certain threshold.
            FORCE_DATA_LOSS (2):
                Instance failover will be performed without
                data loss control.
        """

        DATA_PROTECTION_MODE_UNSPECIFIED = 0
        LIMITED_DATA_LOSS = 1
        FORCE_DATA_LOSS = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_protection_mode: DataProtectionMode = proto.Field(
        proto.ENUM,
        number=2,
        enum=DataProtectionMode,
    )


class LocationMetadata(proto.Message):
    r"""This location metadata represents additional configuration options
    for a given location where a Redis instance may be created. All
    fields are output only. It is returned as content of the
    ``google.cloud.location.Location.metadata`` field.

    Attributes:
        available_zones (MutableMapping[str, google.cloud.redis_v1beta1.types.ZoneMetadata]):
            Output only. The set of available zones in the location. The
            map is keyed by the lowercase ID of each zone, as defined by
            GCE. These keys can be specified in ``location_id`` or
            ``alternative_location_id`` fields when creating a Redis
            instance.
    """

    available_zones: MutableMapping[str, "ZoneMetadata"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=1,
        message="ZoneMetadata",
    )


class ZoneMetadata(proto.Message):
    r"""Defines specific information for a particular zone. Currently
    empty and reserved for future use only.

    """


class TlsCertificate(proto.Message):
    r"""TlsCertificate Resource

    Attributes:
        serial_number (str):
            Serial number, as extracted from the
            certificate.
        cert (str):
            PEM representation.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the certificate was created in
            `RFC 3339 <https://tools.ietf.org/html/rfc3339>`__ format,
            for example ``2020-05-18T00:00:00.094Z``.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the certificate expires in `RFC
            3339 <https://tools.ietf.org/html/rfc3339>`__ format, for
            example ``2020-05-18T00:00:00.094Z``.
        sha1_fingerprint (str):
            Sha1 Fingerprint of the certificate.
    """

    serial_number: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cert: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    sha1_fingerprint: str = proto.Field(
        proto.STRING,
        number=5,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
