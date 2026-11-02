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
    package="google.cloud.memorystore.v1",
    manifest={
        "PscConnectionStatus",
        "ConnectionType",
        "Instance",
        "AclPolicyInfo",
        "StartMigrationRequest",
        "FinishMigrationRequest",
        "SelfManagedSource",
        "MigrationConfig",
        "AclPolicy",
        "AclPolicyRevision",
        "AclPolicyRevisionStatus",
        "InstanceAclPolicyAttachment",
        "AclRule",
        "AutomatedBackupConfig",
        "BackupCollection",
        "Backup",
        "BackupFile",
        "CrossInstanceReplicationConfig",
        "TokenAuthUser",
        "AuthToken",
        "MaintenancePolicy",
        "WeeklyMaintenanceWindow",
        "MaintenanceSchedule",
        "PscAttachmentDetail",
        "PscAutoConnection",
        "PscConnection",
        "DiscoveryEndpoint",
        "PersistenceConfig",
        "NodeConfig",
        "ZoneDistributionConfig",
        "RescheduleMaintenanceRequest",
        "ListAclPoliciesRequest",
        "ListAclPoliciesResponse",
        "ListAclPolicyRevisionsRequest",
        "ListAclPolicyRevisionsResponse",
        "ListInstancesRequest",
        "ListInstancesResponse",
        "GetAclPolicyRequest",
        "GetAclPolicyRevisionRequest",
        "GetInstanceRequest",
        "CreateAclPolicyRequest",
        "CreateInstanceRequest",
        "UpdateAclPolicyRequest",
        "UpdateInstanceRequest",
        "DeleteAclPolicyRequest",
        "DeleteInstanceRequest",
        "ListBackupCollectionsRequest",
        "ListBackupCollectionsResponse",
        "GetBackupCollectionRequest",
        "ListBackupsRequest",
        "ListBackupsResponse",
        "GetBackupRequest",
        "DeleteBackupRequest",
        "ExportBackupRequest",
        "BackupInstanceRequest",
        "GetCertificateAuthorityRequest",
        "ListTokenAuthUsersRequest",
        "ListTokenAuthUsersResponse",
        "GetTokenAuthUserRequest",
        "ListAuthTokensRequest",
        "ListAuthTokensResponse",
        "GetAuthTokenRequest",
        "AddTokenAuthUserRequest",
        "DeleteTokenAuthUserRequest",
        "AddAuthTokenRequest",
        "DeleteAuthTokenRequest",
        "CertificateAuthority",
        "SharedRegionalCertificateAuthority",
        "GetSharedRegionalCertificateAuthorityRequest",
        "OperationMetadata",
        "EncryptionInfo",
    },
)


class PscConnectionStatus(proto.Enum):
    r"""Status of the PSC connection.

    Values:
        PSC_CONNECTION_STATUS_UNSPECIFIED (0):
            PSC connection status is not specified.
        ACTIVE (1):
            The connection is active
        NOT_FOUND (2):
            Connection not found
    """

    PSC_CONNECTION_STATUS_UNSPECIFIED = 0
    ACTIVE = 1
    NOT_FOUND = 2


class ConnectionType(proto.Enum):
    r"""Type of a PSC connection

    Values:
        CONNECTION_TYPE_UNSPECIFIED (0):
            Connection Type is not set
        CONNECTION_TYPE_DISCOVERY (1):
            Connection that will be used for topology
            discovery.
        CONNECTION_TYPE_PRIMARY (2):
            Connection that will be used as primary
            endpoint to access primary.
        CONNECTION_TYPE_READER (3):
            Connection that will be used as reader
            endpoint to access replicas.
    """

    CONNECTION_TYPE_UNSPECIFIED = 0
    CONNECTION_TYPE_DISCOVERY = 1
    CONNECTION_TYPE_PRIMARY = 2
    CONNECTION_TYPE_READER = 3


class Instance(proto.Message):
    r"""A Memorystore instance.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_source (google.cloud.memorystore_v1.types.Instance.GcsBackupSource):
            Optional. Immutable. Backups that stored in
            Cloud Storage buckets. The Cloud Storage buckets
            need to be the same region as the instances.
            Read permission is required to import from the
            provided Cloud Storage Objects.

            This field is a member of `oneof`_ ``import_sources``.
        managed_backup_source (google.cloud.memorystore_v1.types.Instance.ManagedBackupSource):
            Optional. Immutable. Backups that generated
            and managed by memorystore service.

            This field is a member of `oneof`_ ``import_sources``.
        name (str):
            Identifier. Unique name of the instance.
            Format:
            projects/{project}/locations/{location}/instances/{instance}
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Creation timestamp of the
            instance.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Latest update timestamp of the
            instance.
        labels (MutableMapping[str, str]):
            Optional. Labels to represent user-provided
            metadata.
        state (google.cloud.memorystore_v1.types.Instance.State):
            Output only. Current state of the instance.
        state_info (google.cloud.memorystore_v1.types.Instance.StateInfo):
            Output only. Additional information about the
            state of the instance.
        uid (str):
            Output only. System assigned, unique
            identifier for the instance.
        replica_count (int):
            Optional. Number of replica nodes per shard.
            If omitted the default is 0 replicas.

            This field is a member of `oneof`_ ``_replica_count``.
        authorization_mode (google.cloud.memorystore_v1.types.Instance.AuthorizationMode):
            Optional. Immutable. Authorization mode of
            the instance.
        transit_encryption_mode (google.cloud.memorystore_v1.types.Instance.TransitEncryptionMode):
            Optional. Immutable. In-transit encryption
            mode of the instance.
        shard_count (int):
            Optional. Number of shards for the instance.
        discovery_endpoints (MutableSequence[google.cloud.memorystore_v1.types.DiscoveryEndpoint]):
            Output only. Deprecated: The discovery_endpoints parameter
            is deprecated. As a result, it will not be populated if the
            connections are created using endpoints parameter. Instead
            of this parameter, for discovery, use
            endpoints.connections.pscConnection and
            endpoints.connections.pscAutoConnection with connectionType
            CONNECTION_TYPE_DISCOVERY.
        node_type (google.cloud.memorystore_v1.types.Instance.NodeType):
            Optional. Machine type for individual nodes
            of the instance.
        persistence_config (google.cloud.memorystore_v1.types.PersistenceConfig):
            Optional. Persistence configuration of the
            instance.
        engine_version (str):
            Optional. Engine version of the instance.
        engine_configs (MutableMapping[str, str]):
            Optional. User-provided engine configurations
            for the instance.
        node_config (google.cloud.memorystore_v1.types.NodeConfig):
            Output only. Configuration of individual
            nodes of the instance.
        zone_distribution_config (google.cloud.memorystore_v1.types.ZoneDistributionConfig):
            Optional. Immutable. Zone distribution
            configuration of the instance for node
            allocation.
        deletion_protection_enabled (bool):
            Optional. If set to true deletion of the
            instance will fail.

            This field is a member of `oneof`_ ``_deletion_protection_enabled``.
        psc_auto_connections (MutableSequence[google.cloud.memorystore_v1.types.PscAutoConnection]):
            Optional. Immutable. Deprecated: Use the
            endpoints.connections.psc_auto_connection value instead.
        psc_attachment_details (MutableSequence[google.cloud.memorystore_v1.types.PscAttachmentDetail]):
            Output only. Service attachment details to
            configure PSC connections.
        endpoints (MutableSequence[google.cloud.memorystore_v1.types.Instance.InstanceEndpoint]):
            Optional. Endpoints for the instance.
        mode (google.cloud.memorystore_v1.types.Instance.Mode):
            Optional. Immutable. The mode config for the
            instance.
        simulate_maintenance_event (bool):
            Optional. Input only. Simulate a maintenance
            event.

            This field is a member of `oneof`_ ``_simulate_maintenance_event``.
        ondemand_maintenance (bool):
            Optional. Input only. Ondemand maintenance
            for the instance.

            This field is a member of `oneof`_ ``_ondemand_maintenance``.
        satisfies_pzs (bool):
            Optional. Output only. Reserved for future
            use.

            This field is a member of `oneof`_ ``_satisfies_pzs``.
        satisfies_pzi (bool):
            Optional. Output only. Reserved for future
            use.

            This field is a member of `oneof`_ ``_satisfies_pzi``.
        maintenance_policy (google.cloud.memorystore_v1.types.MaintenancePolicy):
            Optional. The maintenance policy for the
            instance. If not provided, the maintenance event
            will be performed based on Memorystore internal
            rollout schedule.
        maintenance_schedule (google.cloud.memorystore_v1.types.MaintenanceSchedule):
            Output only. Published maintenance schedule.
        cross_instance_replication_config (google.cloud.memorystore_v1.types.CrossInstanceReplicationConfig):
            Optional. The config for cross instance
            replication.
        async_instance_endpoints_deletion_enabled (bool):
            Optional. If true, instance endpoints that
            are created and registered by customers can be
            deleted asynchronously. That is, such an
            instance endpoint can be de-registered before
            the forwarding rules in the instance endpoint
            are deleted.

            This field is a member of `oneof`_ ``_async_instance_endpoints_deletion_enabled``.
        kms_key (str):
            Optional. The KMS key used to encrypt the
            at-rest data of the cluster.

            This field is a member of `oneof`_ ``_kms_key``.
        encryption_info (google.cloud.memorystore_v1.types.EncryptionInfo):
            Output only. Encryption information of the
            data at rest of the cluster.
        backup_collection (str):
            Output only. The backup collection full
            resource name. Example:
            projects/{project}/locations/{location}/backupCollections/{collection}

            This field is a member of `oneof`_ ``_backup_collection``.
        automated_backup_config (google.cloud.memorystore_v1.types.AutomatedBackupConfig):
            Optional. The automated backup config for the
            instance.
        maintenance_version (str):
            Optional. This field can be used to trigger self service
            update to indicate the desired maintenance version. The
            input to this field can be determined by the
            available_maintenance_versions field.

            This field is a member of `oneof`_ ``_maintenance_version``.
        effective_maintenance_version (str):
            Output only. This field represents the actual
            maintenance version of the instance.

            This field is a member of `oneof`_ ``_effective_maintenance_version``.
        available_maintenance_versions (MutableSequence[str]):
            Output only. This field is used to determine
            the available maintenance versions for the self
            service update.
        allow_fewer_zones_deployment (bool):
            Optional. Immutable. Deprecated, do not use.
        server_ca_mode (google.cloud.memorystore_v1.types.Instance.ServerCaMode):
            Optional. Immutable. The Server CA mode for
            the instance.

            This field is a member of `oneof`_ ``_server_ca_mode``.
        server_ca_pool (str):
            Optional. Immutable. The customer-managed CA pool for the
            instance. Only applicable if the Server CA mode is
            CUSTOMER_MANAGED_CAS_CA. Format:
            "projects/{project}/locations/{region}/caPools/{ca_pool}".

            This field is a member of `oneof`_ ``_server_ca_pool``.
        rotate_server_certificate (bool):
            Optional. Input only. Rotate the server
            certificates.

            This field is a member of `oneof`_ ``_rotate_server_certificate``.
        migration_config (google.cloud.memorystore_v1.types.MigrationConfig):
            Output only. Migration config for the
            instance.
        acl_policy (str):
            Optional. The ACL policy for the instance. Format:
            projects/{project}/locations/{location}/aclPolicies/{acl_policy}

            This field is a member of `oneof`_ ``_acl_policy``.
        acl_policy_info (google.cloud.memorystore_v1.types.AclPolicyInfo):
            Output only. Details of the applied ACL
            policy.
    """

    class State(proto.Enum):
        r"""Possible states of the instance.

        Values:
            STATE_UNSPECIFIED (0):
                Not set.
            CREATING (1):
                Instance is being created.
            ACTIVE (2):
                Instance has been created and is usable.
            UPDATING (3):
                Instance is being updated.
            DELETING (4):
                Instance is being deleted.
            MIGRATING (6):
                Instance is being migrated.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        UPDATING = 3
        DELETING = 4
        MIGRATING = 6

    class AuthorizationMode(proto.Enum):
        r"""Possible authorization modes of the instance.

        Values:
            AUTHORIZATION_MODE_UNSPECIFIED (0):
                Not set.
            AUTH_DISABLED (1):
                Authorization disabled.
            IAM_AUTH (2):
                IAM basic authorization.
            TOKEN_AUTH (3):
                Token based authorization.
        """

        AUTHORIZATION_MODE_UNSPECIFIED = 0
        AUTH_DISABLED = 1
        IAM_AUTH = 2
        TOKEN_AUTH = 3

    class TransitEncryptionMode(proto.Enum):
        r"""Possible in-transit encryption modes of the instance.

        Values:
            TRANSIT_ENCRYPTION_MODE_UNSPECIFIED (0):
                Not set.
            TRANSIT_ENCRYPTION_DISABLED (1):
                In-transit encryption is disabled.
            SERVER_AUTHENTICATION (2):
                Server-managed encryption is used for
                in-transit encryption.
        """

        TRANSIT_ENCRYPTION_MODE_UNSPECIFIED = 0
        TRANSIT_ENCRYPTION_DISABLED = 1
        SERVER_AUTHENTICATION = 2

    class NodeType(proto.Enum):
        r"""Possible node types of the instance. See
        https://cloud.google.com/memorystore/docs/valkey/instance-node-specification
        for more information.

        Values:
            NODE_TYPE_UNSPECIFIED (0):
                Not set.
            SHARED_CORE_NANO (1):
                Shared core nano.
            HIGHMEM_MEDIUM (2):
                High memory medium.
            HIGHMEM_XLARGE (3):
                High memory extra large.
            STANDARD_SMALL (4):
                Standard small.
            CUSTOM_MICRO (5):
                Custom micro.
            CUSTOM_MINI (6):
                Custom mini.
            HIGHCPU_MEDIUM (7):
                High cpu medium.
            STANDARD_LARGE (8):
                Standard large.
            HIGHMEM_2XLARGE (9):
                High memory 2xlarge.
            CUSTOM_PICO (10):
                Custom pico.
        """

        NODE_TYPE_UNSPECIFIED = 0
        SHARED_CORE_NANO = 1
        HIGHMEM_MEDIUM = 2
        HIGHMEM_XLARGE = 3
        STANDARD_SMALL = 4
        CUSTOM_MICRO = 5
        CUSTOM_MINI = 6
        HIGHCPU_MEDIUM = 7
        STANDARD_LARGE = 8
        HIGHMEM_2XLARGE = 9
        CUSTOM_PICO = 10

    class Mode(proto.Enum):
        r"""The mode config, which is used to enable/disable cluster
        mode.

        Values:
            MODE_UNSPECIFIED (0):
                Mode is not specified.
            STANDALONE (1):
                Deprecated: Use CLUSTER_DISABLED instead.
            CLUSTER (2):
                Instance is in cluster mode.
            CLUSTER_DISABLED (4):
                Cluster mode is disabled for the instance.
        """

        MODE_UNSPECIFIED = 0
        STANDALONE = 1
        CLUSTER = 2
        CLUSTER_DISABLED = 4

    class ServerCaMode(proto.Enum):
        r"""The Server CA mode for the instance.

        Values:
            SERVER_CA_MODE_UNSPECIFIED (0):
                Server CA mode not specified.
            GOOGLE_MANAGED_PER_INSTANCE_CA (1):
                Each instance has its own Google-managed CA.
            GOOGLE_MANAGED_SHARED_CA (2):
                The instance uses a Google-managed shared CA
                for the instance's region.
            CUSTOMER_MANAGED_CAS_CA (3):
                The instance uses a customer-managed CA from
                CAS.
            SERVER_CA_MODE_GOOGLE_MANAGED_PER_INSTANCE_CA (1):
                Deprecated: Use GOOGLE_MANAGED_PER_INSTANCE_CA instead.
            SERVER_CA_MODE_GOOGLE_MANAGED_SHARED_CA (2):
                Deprecated: Use GOOGLE_MANAGED_SHARED_CA instead.
            SERVER_CA_MODE_CUSTOMER_MANAGED_CAS_CA (3):
                Deprecated: Use CUSTOMER_MANAGED_CAS_CA instead.
        """

        _pb_options = {"allow_alias": True}
        SERVER_CA_MODE_UNSPECIFIED = 0
        GOOGLE_MANAGED_PER_INSTANCE_CA = 1
        GOOGLE_MANAGED_SHARED_CA = 2
        CUSTOMER_MANAGED_CAS_CA = 3
        SERVER_CA_MODE_GOOGLE_MANAGED_PER_INSTANCE_CA = 1
        SERVER_CA_MODE_GOOGLE_MANAGED_SHARED_CA = 2
        SERVER_CA_MODE_CUSTOMER_MANAGED_CAS_CA = 3

    class StateInfo(proto.Message):
        r"""Additional information about the state of the instance.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            update_info (google.cloud.memorystore_v1.types.Instance.StateInfo.UpdateInfo):
                Output only. Describes ongoing update when
                instance state is UPDATING.

                This field is a member of `oneof`_ ``info``.
        """

        class UpdateInfo(proto.Message):
            r"""Represents information about instance with state UPDATING.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                target_shard_count (int):
                    Output only. Target number of shards for the
                    instance.

                    This field is a member of `oneof`_ ``_target_shard_count``.
                target_replica_count (int):
                    Output only. Target number of replica nodes
                    per shard for the instance.

                    This field is a member of `oneof`_ ``_target_replica_count``.
                target_engine_version (str):
                    Output only. Target engine version for the
                    instance.

                    This field is a member of `oneof`_ ``_target_engine_version``.
                target_node_type (google.cloud.memorystore_v1.types.Instance.NodeType):
                    Output only. Target node type for the
                    instance.

                    This field is a member of `oneof`_ ``_target_node_type``.
            """

            target_shard_count: int = proto.Field(
                proto.INT32,
                number=1,
                optional=True,
            )
            target_replica_count: int = proto.Field(
                proto.INT32,
                number=2,
                optional=True,
            )
            target_engine_version: str = proto.Field(
                proto.STRING,
                number=3,
                optional=True,
            )
            target_node_type: "Instance.NodeType" = proto.Field(
                proto.ENUM,
                number=4,
                optional=True,
                enum="Instance.NodeType",
            )

        update_info: "Instance.StateInfo.UpdateInfo" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="info",
            message="Instance.StateInfo.UpdateInfo",
        )

    class GcsBackupSource(proto.Message):
        r"""Backups that stored in Cloud Storage buckets.
        The Cloud Storage buckets need to be the same region as the
        instances.

        Attributes:
            uris (MutableSequence[str]):
                Optional. Example: gs://bucket1/object1,
                gs://bucket2/folder2/object2
        """

        uris: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )

    class ManagedBackupSource(proto.Message):
        r"""Backups that generated and managed by memorystore.

        Attributes:
            backup (str):
                Optional. Example:
                //memorystore.googleapis.com/projects/{project}/locations/{location}/backupCollections/{collection}/backups/{backup}
                A shorter version (without the prefix) of the backup name is
                also supported, like
                projects/{project}/locations/{location}/backupCollections/{collection}/backups/{backup_id}
                In this case, it assumes the backup is under
                memorystore.googleapis.com.
        """

        backup: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class InstanceEndpoint(proto.Message):
        r"""InstanceEndpoint consists of PSC connections that are created
        as a group in each VPC network for accessing the instance. In
        each group, there shall be one connection for each service
        attachment in the cluster.

        Attributes:
            connections (MutableSequence[google.cloud.memorystore_v1.types.Instance.ConnectionDetail]):
                Optional. A group of PSC connections. They
                are created in the same VPC network, one for
                each service attachment in the cluster.
        """

        connections: MutableSequence["Instance.ConnectionDetail"] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="Instance.ConnectionDetail",
        )

    class ConnectionDetail(proto.Message):
        r"""Information of each PSC connection.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            psc_auto_connection (google.cloud.memorystore_v1.types.PscAutoConnection):
                Immutable. Detailed information of a PSC
                connection that is created through service
                connectivity automation.

                This field is a member of `oneof`_ ``connection``.
            psc_connection (google.cloud.memorystore_v1.types.PscConnection):
                Detailed information of a PSC connection that
                is created by the user.

                This field is a member of `oneof`_ ``connection``.
        """

        psc_auto_connection: "PscAutoConnection" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="connection",
            message="PscAutoConnection",
        )
        psc_connection: "PscConnection" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="connection",
            message="PscConnection",
        )

    gcs_source: GcsBackupSource = proto.Field(
        proto.MESSAGE,
        number=23,
        oneof="import_sources",
        message=GcsBackupSource,
    )
    managed_backup_source: ManagedBackupSource = proto.Field(
        proto.MESSAGE,
        number=24,
        oneof="import_sources",
        message=ManagedBackupSource,
    )
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
    state: State = proto.Field(
        proto.ENUM,
        number=5,
        enum=State,
    )
    state_info: StateInfo = proto.Field(
        proto.MESSAGE,
        number=6,
        message=StateInfo,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=7,
    )
    replica_count: int = proto.Field(
        proto.INT32,
        number=8,
        optional=True,
    )
    authorization_mode: AuthorizationMode = proto.Field(
        proto.ENUM,
        number=9,
        enum=AuthorizationMode,
    )
    transit_encryption_mode: TransitEncryptionMode = proto.Field(
        proto.ENUM,
        number=10,
        enum=TransitEncryptionMode,
    )
    shard_count: int = proto.Field(
        proto.INT32,
        number=11,
    )
    discovery_endpoints: MutableSequence["DiscoveryEndpoint"] = proto.RepeatedField(
        proto.MESSAGE,
        number=12,
        message="DiscoveryEndpoint",
    )
    node_type: NodeType = proto.Field(
        proto.ENUM,
        number=13,
        enum=NodeType,
    )
    persistence_config: "PersistenceConfig" = proto.Field(
        proto.MESSAGE,
        number=14,
        message="PersistenceConfig",
    )
    engine_version: str = proto.Field(
        proto.STRING,
        number=15,
    )
    engine_configs: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=16,
    )
    node_config: "NodeConfig" = proto.Field(
        proto.MESSAGE,
        number=17,
        message="NodeConfig",
    )
    zone_distribution_config: "ZoneDistributionConfig" = proto.Field(
        proto.MESSAGE,
        number=18,
        message="ZoneDistributionConfig",
    )
    deletion_protection_enabled: bool = proto.Field(
        proto.BOOL,
        number=19,
        optional=True,
    )
    psc_auto_connections: MutableSequence["PscAutoConnection"] = proto.RepeatedField(
        proto.MESSAGE,
        number=20,
        message="PscAutoConnection",
    )
    psc_attachment_details: MutableSequence["PscAttachmentDetail"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=21,
            message="PscAttachmentDetail",
        )
    )
    endpoints: MutableSequence[InstanceEndpoint] = proto.RepeatedField(
        proto.MESSAGE,
        number=25,
        message=InstanceEndpoint,
    )
    mode: Mode = proto.Field(
        proto.ENUM,
        number=26,
        enum=Mode,
    )
    simulate_maintenance_event: bool = proto.Field(
        proto.BOOL,
        number=27,
        optional=True,
    )
    ondemand_maintenance: bool = proto.Field(
        proto.BOOL,
        number=28,
        optional=True,
    )
    satisfies_pzs: bool = proto.Field(
        proto.BOOL,
        number=29,
        optional=True,
    )
    satisfies_pzi: bool = proto.Field(
        proto.BOOL,
        number=30,
        optional=True,
    )
    maintenance_policy: "MaintenancePolicy" = proto.Field(
        proto.MESSAGE,
        number=31,
        message="MaintenancePolicy",
    )
    maintenance_schedule: "MaintenanceSchedule" = proto.Field(
        proto.MESSAGE,
        number=32,
        message="MaintenanceSchedule",
    )
    cross_instance_replication_config: "CrossInstanceReplicationConfig" = proto.Field(
        proto.MESSAGE,
        number=33,
        message="CrossInstanceReplicationConfig",
    )
    async_instance_endpoints_deletion_enabled: bool = proto.Field(
        proto.BOOL,
        number=44,
        optional=True,
    )
    kms_key: str = proto.Field(
        proto.STRING,
        number=45,
        optional=True,
    )
    encryption_info: "EncryptionInfo" = proto.Field(
        proto.MESSAGE,
        number=46,
        message="EncryptionInfo",
    )
    backup_collection: str = proto.Field(
        proto.STRING,
        number=47,
        optional=True,
    )
    automated_backup_config: "AutomatedBackupConfig" = proto.Field(
        proto.MESSAGE,
        number=48,
        message="AutomatedBackupConfig",
    )
    maintenance_version: str = proto.Field(
        proto.STRING,
        number=49,
        optional=True,
    )
    effective_maintenance_version: str = proto.Field(
        proto.STRING,
        number=50,
        optional=True,
    )
    available_maintenance_versions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=51,
    )
    allow_fewer_zones_deployment: bool = proto.Field(
        proto.BOOL,
        number=54,
    )
    server_ca_mode: ServerCaMode = proto.Field(
        proto.ENUM,
        number=56,
        optional=True,
        enum=ServerCaMode,
    )
    server_ca_pool: str = proto.Field(
        proto.STRING,
        number=57,
        optional=True,
    )
    rotate_server_certificate: bool = proto.Field(
        proto.BOOL,
        number=58,
        optional=True,
    )
    migration_config: "MigrationConfig" = proto.Field(
        proto.MESSAGE,
        number=59,
        message="MigrationConfig",
    )
    acl_policy: str = proto.Field(
        proto.STRING,
        number=60,
        optional=True,
    )
    acl_policy_info: "AclPolicyInfo" = proto.Field(
        proto.MESSAGE,
        number=62,
        message="AclPolicyInfo",
    )


class AclPolicyInfo(proto.Message):
    r"""Details of the applied ACL policy.

    Attributes:
        applied_acl_policy (str):
            Output only. The resource name of the applied ACL policy.
            Format:
            "projects/{project}/locations/{location}/aclPolicies/{acl_policy}".
        applied_acl_policy_revision (str):
            Output only. The resource name of the applied ACL policy
            revision. Format:
            "projects/{project}/locations/{location}/aclPolicies/{acl_policy}/revisions/{revision}".
        applied_acl_policy_revision_number (int):
            Output only. The revision number of the
            applied ACL policy revision.
        acl_policy_revision_statuses (MutableSequence[google.cloud.memorystore_v1.types.AclPolicyRevisionStatus]):
            Output only. A list of status for various
            revisions of this ACL policy on the instance.
    """

    applied_acl_policy: str = proto.Field(
        proto.STRING,
        number=1,
    )
    applied_acl_policy_revision: str = proto.Field(
        proto.STRING,
        number=2,
    )
    applied_acl_policy_revision_number: int = proto.Field(
        proto.INT64,
        number=3,
    )
    acl_policy_revision_statuses: MutableSequence["AclPolicyRevisionStatus"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message="AclPolicyRevisionStatus",
        )
    )


class StartMigrationRequest(proto.Message):
    r"""Request for ``StartMigration``.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        self_managed_source (google.cloud.memorystore_v1.types.SelfManagedSource):
            Required. Configuration for migrating from a
            self-managed Valkey/Redis instance

            This field is a member of `oneof`_ ``source``.
        name (str):
            Required. The resource name of the instance
            to start migration on. Format:
            projects/{project}/locations/{location}/instances/{instance}
    """

    self_managed_source: "SelfManagedSource" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="source",
        message="SelfManagedSource",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class FinishMigrationRequest(proto.Message):
    r"""Request for ``FinishMigration``.

    Attributes:
        name (str):
            Required. The resource name of the instance
            to finalize migration on. Format:
            projects/{project}/locations/{location}/instances/{instance}
        force (bool):
            Optional. By default, the ``FinishMigration`` operation
            ensures the target replication offset to catch up to the
            source offset as of the time of the call. Set this field to
            ``true`` to bypass this offset verification check.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class SelfManagedSource(proto.Message):
    r"""Details of the self-managed source instance.

    Attributes:
        ip_address (str):
            Required. The IP address of the source
            instance. This IP address should be a stable IP
            address that can be accessed by the Memorystore
            instance throughout the migration process.
        port (int):
            Required. The port of the source instance.
            This port should be a stable port that can be
            accessed by the Memorystore instance throughout
            the migration process.
        network_attachment (str):
            Required. The resource name of the Private Service Connect
            Network Attachment used to establish connectivity to the
            source instance. This network attachment has the following
            requirements:

            1. It must be in the same project as the Memorystore
               instance.
            2. It must be in the same region as the Memorystore
               instance.
            3. The subnet attached to the network attachment must be in
               the same VPC network as the source instance nodes.

            Format:
            projects/{project}/regions/{region}/networkAttachments/{network_attachment}
    """

    ip_address: str = proto.Field(
        proto.STRING,
        number=1,
    )
    port: int = proto.Field(
        proto.INT32,
        number=2,
    )
    network_attachment: str = proto.Field(
        proto.STRING,
        number=3,
    )


class MigrationConfig(proto.Message):
    r"""Configuration for the migration of an instance.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        self_managed_source (google.cloud.memorystore_v1.types.SelfManagedSource):
            Output only. Configuration for migrating from
            a self-managed Valkey/Redis instance

            This field is a member of `oneof`_ ``source``.
        state (google.cloud.memorystore_v1.types.MigrationConfig.State):
            Output only. Migration state of the instance.
        force_finish_migration (bool):
            Output only. Represents a boolean flag to
            force migration finalization without offset
            catch up validation between source and target
            before stopping replication.
    """

    class State(proto.Enum):
        r"""Migration state of the instance.
        New values may be added in the future.

        Values:
            STATE_UNSPECIFIED (0):
                Instance has no migration related activity.
                This is the initial state.
            ROLLED_BACK (1):
                Instance is not currently migrating. The
                instance underwent a migration attempt that
                failed, and the subsequent rollback was
                successful. The instance is now ready for a new
                migration attempt if desired.
            ROLLING_BACK (5):
                Indicates a previous migration attempt failed. The
                high-level instance state will be ``MIGRATING``. The
                instance is not ready for a new migration attempt. Rollback
                is in progress to restore the instance to its original
                state. The instance will remain in this state until rollback
                is successful.
            REPLICATION_ESTABLISHED (6):
                Instance is in the process of migration.
                Instance has established successful replication
                and is ready for cutover.
            MIGRATED (4):
                Instance is successfully migrated.
        """

        STATE_UNSPECIFIED = 0
        ROLLED_BACK = 1
        ROLLING_BACK = 5
        REPLICATION_ESTABLISHED = 6
        MIGRATED = 4

    self_managed_source: "SelfManagedSource" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="source",
        message="SelfManagedSource",
    )
    state: State = proto.Field(
        proto.ENUM,
        number=1,
        enum=State,
    )
    force_finish_migration: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class AclPolicy(proto.Message):
    r"""The ACL policy resource.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. Full resource path of the ACL
            policy.
        rules (MutableSequence[google.cloud.memorystore_v1.types.AclRule]):
            Required. The ACL rules within the ACL
            policy.
        state (google.cloud.memorystore_v1.types.AclPolicy.State):
            Output only. The state of the ACL policy.
        etag (str):
            Output only. Etag of the ACL policy.

            This field is a member of `oneof`_ ``_etag``.
        instance_acl_policy_attachments (MutableSequence[google.cloud.memorystore_v1.types.InstanceAclPolicyAttachment]):
            Output only. The ACL policy attachment status
            for each attached instance.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp that the ACL
            policy was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp that the ACL
            policy was last updated.
    """

    class State(proto.Enum):
        r"""Represents the different states of an ACL policy.

        Values:
            STATE_UNSPECIFIED (0):
                Not set.
            ACTIVE (1):
                ACL policy has been created and is fully
                usable.
            UPDATING (2):
                ACL policy is being updated.
            DELETING (3):
                ACL policy is being deleted.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        UPDATING = 2
        DELETING = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    rules: MutableSequence["AclRule"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="AclRule",
    )
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    instance_acl_policy_attachments: MutableSequence["InstanceAclPolicyAttachment"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=6,
            message="InstanceAclPolicyAttachment",
        )
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )


class AclPolicyRevision(proto.Message):
    r"""The ACL policy revision resource.

    Attributes:
        name (str):
            Identifier. The name of the ACL policy revision. Format:
            "projects/{project}/locations/{location}/aclPolicies/{acl_policy}/revisions/{revision}".
        revision_number (int):
            Output only. The revision number of the ACL
            policy revision.
        snapshot (google.cloud.memorystore_v1.types.AclPolicy):
            Output only. The snapshot of the ACL policy
            at the time of revision creation.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp that the revision
            was created.
        attached_instances (MutableSequence[str]):
            Output only. A list of instances that are
            attached to this ACL policy revision.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    revision_number: int = proto.Field(
        proto.INT64,
        number=2,
    )
    snapshot: "AclPolicy" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="AclPolicy",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    attached_instances: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )


class AclPolicyRevisionStatus(proto.Message):
    r"""AclPolicyRevisionStatus stores the per-revision status for an
    attached instance.

    Attributes:
        acl_policy_revision (str):
            Output only. The resource name of the ACL policy revision
            this status refers to. Format:
            "projects/{project}/locations/{location}/aclPolicies/{acl_policy}/revisions/{revision}".
        acl_policy_revision_number (int):
            Output only. The revision number of the ACL
            policy revision this status refers to.
        state (google.cloud.memorystore_v1.types.AclPolicyRevisionStatus.State):
            Output only. AclPolicyRevision state.
        error_message (str):
            Output only. Human-readable error message
            providing more details for FAILED states.
    """

    class State(proto.Enum):
        r"""Enum indicating the status of this ACL policy revision on the
        instance.

        Values:
            STATE_UNSPECIFIED (0):
                Not set.
            APPLYING (1):
                The instance is attempting to apply this
                revision.
            APPLIED (2):
                The instance has successfully applied this
                revision.
            FAILED (3):
                The instance failed to apply this revision.
        """

        STATE_UNSPECIFIED = 0
        APPLYING = 1
        APPLIED = 2
        FAILED = 3

    acl_policy_revision: str = proto.Field(
        proto.STRING,
        number=1,
    )
    acl_policy_revision_number: int = proto.Field(
        proto.INT64,
        number=2,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )
    error_message: str = proto.Field(
        proto.STRING,
        number=4,
    )


class InstanceAclPolicyAttachment(proto.Message):
    r"""InstanceAclPolicyAttachment stores the ACL policy status for
    an attached instance for the revisions successfully applied,
    under application or failed.

    Attributes:
        instance (str):
            Output only. The resource name of the
            attached instance. Format:

            "projects/{project}/locations/{location}/instances/{instance}".
        acl_policy_revision_statuses (MutableSequence[google.cloud.memorystore_v1.types.AclPolicyRevisionStatus]):
            Output only. A list of status for various
            revisions of this ACL policy on the instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    acl_policy_revision_statuses: MutableSequence["AclPolicyRevisionStatus"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="AclPolicyRevisionStatus",
        )
    )


class AclRule(proto.Message):
    r"""A single ACL rule which defines the policy for a user.

    Attributes:
        username (str):
            Required. Specifies the IAM user or service
            account to be added to the ACL policy. This
            username will be directly set on the Valkey OSS.
        rule (str):
            Required. The rule to be applied to the username. Ex: "on
            >password123 ~\* +@all" The format of the rule is defined by
            Valkey OSS: https://valkey.io/topics/acl/
    """

    username: str = proto.Field(
        proto.STRING,
        number=1,
    )
    rule: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AutomatedBackupConfig(proto.Message):
    r"""The automated backup config for an instance.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        fixed_frequency_schedule (google.cloud.memorystore_v1.types.AutomatedBackupConfig.FixedFrequencySchedule):
            Optional. Trigger automated backups at a
            fixed frequency.

            This field is a member of `oneof`_ ``schedule``.
        automated_backup_mode (google.cloud.memorystore_v1.types.AutomatedBackupConfig.AutomatedBackupMode):
            Optional. The automated backup mode. If the
            mode is disabled, the other fields will be
            ignored.
        retention (google.protobuf.duration_pb2.Duration):
            Optional. How long to keep automated backups
            before the backups are deleted. The value should
            be between 1 day and 365 days. If not specified,
            the default value is 35 days.
    """

    class AutomatedBackupMode(proto.Enum):
        r"""The automated backup mode.

        Values:
            AUTOMATED_BACKUP_MODE_UNSPECIFIED (0):
                Default value. Automated backup config is not
                specified.
            DISABLED (1):
                Automated backup config disabled.
            ENABLED (2):
                Automated backup config enabled.
        """

        AUTOMATED_BACKUP_MODE_UNSPECIFIED = 0
        DISABLED = 1
        ENABLED = 2

    class FixedFrequencySchedule(proto.Message):
        r"""This schedule allows the backup to be triggered at a fixed
        frequency (currently only daily is supported).

        Attributes:
            start_time (google.type.timeofday_pb2.TimeOfDay):
                Required. The start time of every automated
                backup in UTC. It must be set to the start of an
                hour. This field is required.
        """

        start_time: timeofday_pb2.TimeOfDay = proto.Field(
            proto.MESSAGE,
            number=2,
            message=timeofday_pb2.TimeOfDay,
        )

    fixed_frequency_schedule: FixedFrequencySchedule = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="schedule",
        message=FixedFrequencySchedule,
    )
    automated_backup_mode: AutomatedBackupMode = proto.Field(
        proto.ENUM,
        number=1,
        enum=AutomatedBackupMode,
    )
    retention: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=3,
        message=duration_pb2.Duration,
    )


class BackupCollection(proto.Message):
    r"""BackupCollection of an instance.

    Attributes:
        name (str):
            Identifier. Full resource path of the backup
            collection.
        instance_uid (str):
            Output only. The instance uid of the backup
            collection.
        instance (str):
            Output only. The full resource path of the
            instance the backup collection belongs to.
            Example:

            projects/{project}/locations/{location}/instances/{instance}
        kms_key (str):
            Output only. The KMS key used to encrypt the
            backups under this backup collection.
        uid (str):
            Output only. System assigned unique
            identifier of the backup collection.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the backup
            collection was created.
        total_backup_size_bytes (int):
            Output only. Total size of all backups in the
            backup collection.
        total_backup_count (int):
            Output only. Total number of backups in the
            backup collection.
        last_backup_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last time a backup was
            created in the backup collection.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance_uid: str = proto.Field(
        proto.STRING,
        number=3,
    )
    instance: str = proto.Field(
        proto.STRING,
        number=4,
    )
    kms_key: str = proto.Field(
        proto.STRING,
        number=5,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=6,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    total_backup_size_bytes: int = proto.Field(
        proto.INT64,
        number=8,
    )
    total_backup_count: int = proto.Field(
        proto.INT64,
        number=10,
    )
    last_backup_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )


class Backup(proto.Message):
    r"""Backup of an instance.

    Attributes:
        name (str):
            Identifier. Full resource path of the backup. the last part
            of the name is the backup id with the following format:
            [YYYYMMDDHHMMSS]\_[Shorted Instance UID] OR customer
            specified while backup instance. Example:
            20240515123000_1234
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the backup was
            created.
        instance (str):
            Output only. Instance resource path of this
            backup.
        instance_uid (str):
            Output only. Instance uid of this backup.
        total_size_bytes (int):
            Output only. Total size of the backup in
            bytes.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the backup will
            expire.
        engine_version (str):
            Output only. valkey-7.5/valkey-8.0, etc.
        backup_files (MutableSequence[google.cloud.memorystore_v1.types.BackupFile]):
            Output only. List of backup files of the
            backup.
        node_type (google.cloud.memorystore_v1.types.Instance.NodeType):
            Output only. Node type of the instance.
        replica_count (int):
            Output only. Number of replicas for the
            instance.
        shard_count (int):
            Output only. Number of shards for the
            instance.
        backup_type (google.cloud.memorystore_v1.types.Backup.BackupType):
            Output only. Type of the backup.
        state (google.cloud.memorystore_v1.types.Backup.State):
            Output only. State of the backup.
        encryption_info (google.cloud.memorystore_v1.types.EncryptionInfo):
            Output only. Encryption information of the
            backup.
        uid (str):
            Output only. System assigned unique
            identifier of the backup.
    """

    class BackupType(proto.Enum):
        r"""Type of the backup.

        Values:
            BACKUP_TYPE_UNSPECIFIED (0):
                The default value, not set.
            ON_DEMAND (1):
                On-demand backup.
            AUTOMATED (2):
                Automated backup.
        """

        BACKUP_TYPE_UNSPECIFIED = 0
        ON_DEMAND = 1
        AUTOMATED = 2

    class State(proto.Enum):
        r"""State of the backup.

        Values:
            STATE_UNSPECIFIED (0):
                The default value, not set.
            CREATING (1):
                The backup is being created.
            ACTIVE (2):
                The backup is active to be used.
            DELETING (3):
                The backup is being deleted.
            SUSPENDED (4):
                The backup is currently suspended due to
                reasons like project deletion, billing account
                closure, etc.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        DELETING = 3
        SUSPENDED = 4

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    instance: str = proto.Field(
        proto.STRING,
        number=3,
    )
    instance_uid: str = proto.Field(
        proto.STRING,
        number=4,
    )
    total_size_bytes: int = proto.Field(
        proto.INT64,
        number=5,
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    engine_version: str = proto.Field(
        proto.STRING,
        number=7,
    )
    backup_files: MutableSequence["BackupFile"] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message="BackupFile",
    )
    node_type: "Instance.NodeType" = proto.Field(
        proto.ENUM,
        number=9,
        enum="Instance.NodeType",
    )
    replica_count: int = proto.Field(
        proto.INT32,
        number=10,
    )
    shard_count: int = proto.Field(
        proto.INT32,
        number=11,
    )
    backup_type: BackupType = proto.Field(
        proto.ENUM,
        number=12,
        enum=BackupType,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=13,
        enum=State,
    )
    encryption_info: "EncryptionInfo" = proto.Field(
        proto.MESSAGE,
        number=14,
        message="EncryptionInfo",
    )
    uid: str = proto.Field(
        proto.STRING,
        number=15,
    )


class BackupFile(proto.Message):
    r"""Backup is consisted of multiple backup files.

    Attributes:
        file_name (str):
            Output only. e.g: <shard-id>.rdb
        size_bytes (int):
            Output only. Size of the backup file in
            bytes.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the backup file
            was created.
    """

    file_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    size_bytes: int = proto.Field(
        proto.INT64,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


class CrossInstanceReplicationConfig(proto.Message):
    r"""Cross instance replication config.

    Attributes:
        instance_role (google.cloud.memorystore_v1.types.CrossInstanceReplicationConfig.InstanceRole):
            Required. The role of the instance in cross
            instance replication.
        primary_instance (google.cloud.memorystore_v1.types.CrossInstanceReplicationConfig.RemoteInstance):
            Optional. Details of the primary instance
            that is used as the replication source for this
            secondary instance.

            This field is only set for a secondary instance.
        secondary_instances (MutableSequence[google.cloud.memorystore_v1.types.CrossInstanceReplicationConfig.RemoteInstance]):
            Optional. List of secondary instances that
            are replicating from this primary instance.

            This field is only set for a primary instance.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last time cross instance
            replication config was updated.
        membership (google.cloud.memorystore_v1.types.CrossInstanceReplicationConfig.Membership):
            Output only. An output only view of all the
            member instances participating in the cross
            instance replication. This view will be provided
            by every member instance irrespective of its
            instance role(primary or secondary).

            A primary instance can provide information about
            all the secondary instances replicating from it.
            However, a secondary instance only knows about
            the primary instance from which it is
            replicating. However, for scenarios, where the
            primary instance is unavailable(e.g. regional
            outage), a Getinstance request can be sent to
            any other member instance and this field will
            list all the member instances participating in
            cross instance replication.
    """

    class InstanceRole(proto.Enum):
        r"""The role of the instance in cross instance replication.

        Values:
            INSTANCE_ROLE_UNSPECIFIED (0):
                instance role is not set.
                The behavior is equivalent to NONE.
            NONE (1):
                This instance does not participate in cross
                instance replication. It is an independent
                instance and does not replicate to or from any
                other instances.
            PRIMARY (2):
                A instance that allows both reads and writes.
                Any data written to this instance is also
                replicated to the attached secondary instances.
            SECONDARY (3):
                A instance that allows only reads and
                replicates data from a primary instance.
        """

        INSTANCE_ROLE_UNSPECIFIED = 0
        NONE = 1
        PRIMARY = 2
        SECONDARY = 3

    class RemoteInstance(proto.Message):
        r"""Details of the remote instance associated with this instance
        in a cross instance replication setup.

        Attributes:
            instance (str):
                Optional. The full resource path of the
                remote instance in the format:
                projects/<project>/locations/<region>/instances/<instance-id>
            uid (str):
                Output only. The unique identifier of the
                remote instance.
        """

        instance: str = proto.Field(
            proto.STRING,
            number=1,
        )
        uid: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class Membership(proto.Message):
        r"""An output only view of all the member instances participating
        in the cross instance replication.

        Attributes:
            primary_instance (google.cloud.memorystore_v1.types.CrossInstanceReplicationConfig.RemoteInstance):
                Output only. The primary instance that acts
                as the source of replication for the secondary
                instances.
            secondary_instances (MutableSequence[google.cloud.memorystore_v1.types.CrossInstanceReplicationConfig.RemoteInstance]):
                Output only. The list of secondary instances
                replicating from the primary instance.
        """

        primary_instance: "CrossInstanceReplicationConfig.RemoteInstance" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="CrossInstanceReplicationConfig.RemoteInstance",
        )
        secondary_instances: MutableSequence[
            "CrossInstanceReplicationConfig.RemoteInstance"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="CrossInstanceReplicationConfig.RemoteInstance",
        )

    instance_role: InstanceRole = proto.Field(
        proto.ENUM,
        number=1,
        enum=InstanceRole,
    )
    primary_instance: RemoteInstance = proto.Field(
        proto.MESSAGE,
        number=2,
        message=RemoteInstance,
    )
    secondary_instances: MutableSequence[RemoteInstance] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=RemoteInstance,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    membership: Membership = proto.Field(
        proto.MESSAGE,
        number=5,
        message=Membership,
    )


class TokenAuthUser(proto.Message):
    r"""Token based auth user for the instance.

    Attributes:
        name (str):
            Identifier. Token based auth user name.
        state (google.cloud.memorystore_v1.types.TokenAuthUser.State):
            Output only. The state of the token based
            auth user.
    """

    class State(proto.Enum):
        r"""Represents the different states of a token based auth user.
        New values may be added in the future.

        Values:
            STATE_UNSPECIFIED (0):
                Not set.
            ACTIVE (1):
                The auth user is active.
            CREATING (2):
                The auth user is being created.
            UPDATING (3):
                The auth user is being updated.
            DELETING (4):
                The auth user is being deleted.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        CREATING = 2
        UPDATING = 3
        DELETING = 4

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=2,
        enum=State,
    )


class AuthToken(proto.Message):
    r"""Auth token for the instance.

    Attributes:
        name (str):
            Identifier. Name of the auth token.
        token (str):
            Output only. The auth token.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create time of the auth token.
        state (google.cloud.memorystore_v1.types.AuthToken.State):
            Output only. The state of the auth token.
    """

    class State(proto.Enum):
        r"""Represents the different states of an auth token.
        New values may be added in the future.

        Values:
            STATE_UNSPECIFIED (0):
                Not set.
            ACTIVE (1):
                The auth token is active.
            CREATING (2):
                The auth token is being created.
            DELETING (3):
                The auth token is being deleted.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        CREATING = 2
        DELETING = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )


class MaintenancePolicy(proto.Message):
    r"""Maintenance policy per instance.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the policy was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the policy was
            updated.
        weekly_maintenance_window (MutableSequence[google.cloud.memorystore_v1.types.WeeklyMaintenanceWindow]):
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
    weekly_maintenance_window: MutableSequence["WeeklyMaintenanceWindow"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="WeeklyMaintenanceWindow",
        )
    )


class WeeklyMaintenanceWindow(proto.Message):
    r"""Time window specified for weekly operations.

    Attributes:
        day (google.type.dayofweek_pb2.DayOfWeek):
            Optional. Allows to define schedule that runs
            specified day of the week.
        start_time (google.type.timeofday_pb2.TimeOfDay):
            Optional. Start time of the window in UTC.
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


class MaintenanceSchedule(proto.Message):
    r"""Upcoming maintenance schedule.

    Attributes:
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The start time of any upcoming
            scheduled maintenance for this instance.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The end time of any upcoming
            scheduled maintenance for this instance.
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


class PscAttachmentDetail(proto.Message):
    r"""Configuration of a service attachment of the cluster, for
    creating PSC connections.

    Attributes:
        service_attachment (str):
            Output only. Service attachment URI which
            your self-created PscConnection should use as
            target.
        connection_type (google.cloud.memorystore_v1.types.ConnectionType):
            Output only. Type of Psc endpoint.
    """

    service_attachment: str = proto.Field(
        proto.STRING,
        number=1,
    )
    connection_type: "ConnectionType" = proto.Field(
        proto.ENUM,
        number=4,
        enum="ConnectionType",
    )


class PscAutoConnection(proto.Message):
    r"""Details of consumer resources in a PSC connection.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        port (int):
            Optional. port will only be set for
            Primary/Reader or Discovery endpoint.

            This field is a member of `oneof`_ ``ports``.
        psc_connection_id (str):
            Output only. The PSC connection id of the
            forwarding rule connected to the service
            attachment.
        ip_address (str):
            Output only. The IP allocated on the consumer
            network for the PSC forwarding rule.
        forwarding_rule (str):
            Output only. The URI of the consumer side forwarding rule.
            Format:
            projects/{project}/regions/{region}/forwardingRules/{forwarding_rule}
        project_id (str):
            Required. The consumer project_id where PSC connections are
            established. This should be the same project_id that the
            instance is being created in.
        network (str):
            Required. The network where the PSC endpoints are created,
            in the form of
            projects/{project_id}/global/networks/{network_name}.
        service_attachment (str):
            Output only. The service attachment which is
            the target of the PSC connection, in the form of
            projects/{project-id}/regions/{region}/serviceAttachments/{service-attachment-id}.
        psc_connection_status (google.cloud.memorystore_v1.types.PscConnectionStatus):
            Output only. The status of the PSC
            connection: whether a connection exists and
            ACTIVE or it no longer exists. Please note that
            this value is updated periodically. Please use
            Private Service Connect APIs for the latest
            status.
        connection_type (google.cloud.memorystore_v1.types.ConnectionType):
            Output only. Type of the PSC connection.
    """

    port: int = proto.Field(
        proto.INT32,
        number=9,
        oneof="ports",
    )
    psc_connection_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ip_address: str = proto.Field(
        proto.STRING,
        number=2,
    )
    forwarding_rule: str = proto.Field(
        proto.STRING,
        number=3,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    network: str = proto.Field(
        proto.STRING,
        number=5,
    )
    service_attachment: str = proto.Field(
        proto.STRING,
        number=6,
    )
    psc_connection_status: "PscConnectionStatus" = proto.Field(
        proto.ENUM,
        number=7,
        enum="PscConnectionStatus",
    )
    connection_type: "ConnectionType" = proto.Field(
        proto.ENUM,
        number=8,
        enum="ConnectionType",
    )


class PscConnection(proto.Message):
    r"""User created Psc connection configuration.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        port (int):
            Optional. port will only be set for
            Primary/Reader or Discovery endpoint.

            This field is a member of `oneof`_ ``ports``.
        psc_connection_id (str):
            Required. The PSC connection id of the
            forwarding rule connected to the service
            attachment.
        ip_address (str):
            Required. The IP allocated on the consumer
            network for the PSC forwarding rule.
        forwarding_rule (str):
            Required. The URI of the consumer side forwarding rule.
            Format:
            projects/{project}/regions/{region}/forwardingRules/{forwarding_rule}
        project_id (str):
            Output only. The consumer project_id where the forwarding
            rule is created from.
        network (str):
            Required. The consumer network where the IP address resides,
            in the form of
            projects/{project_id}/global/networks/{network_name}.
        service_attachment (str):
            Required. The service attachment which is the
            target of the PSC connection, in the form of
            projects/{project-id}/regions/{region}/serviceAttachments/{service-attachment-id}.
        psc_connection_status (google.cloud.memorystore_v1.types.PscConnectionStatus):
            Output only. The status of the PSC
            connection: whether a connection exists and
            ACTIVE or it no longer exists. Please note that
            this value is updated periodically. Please use
            Private Service Connect APIs for the latest
            status.
        connection_type (google.cloud.memorystore_v1.types.ConnectionType):
            Output only. Type of the PSC connection.
    """

    port: int = proto.Field(
        proto.INT32,
        number=9,
        oneof="ports",
    )
    psc_connection_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ip_address: str = proto.Field(
        proto.STRING,
        number=2,
    )
    forwarding_rule: str = proto.Field(
        proto.STRING,
        number=3,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    network: str = proto.Field(
        proto.STRING,
        number=5,
    )
    service_attachment: str = proto.Field(
        proto.STRING,
        number=6,
    )
    psc_connection_status: "PscConnectionStatus" = proto.Field(
        proto.ENUM,
        number=7,
        enum="PscConnectionStatus",
    )
    connection_type: "ConnectionType" = proto.Field(
        proto.ENUM,
        number=8,
        enum="ConnectionType",
    )


class DiscoveryEndpoint(proto.Message):
    r"""Represents an endpoint for clients to connect to the
    instance.

    Attributes:
        address (str):
            Output only. IP address of the exposed
            endpoint clients connect to.
        port (int):
            Output only. The port number of the exposed
            endpoint.
        network (str):
            Output only. The network where the IP address of the
            discovery endpoint will be reserved, in the form of
            projects/{network_project}/global/networks/{network_name}.
    """

    address: str = proto.Field(
        proto.STRING,
        number=1,
    )
    port: int = proto.Field(
        proto.INT32,
        number=2,
    )
    network: str = proto.Field(
        proto.STRING,
        number=4,
    )


class PersistenceConfig(proto.Message):
    r"""Represents persistence configuration for a instance.

    Attributes:
        mode (google.cloud.memorystore_v1.types.PersistenceConfig.PersistenceMode):
            Optional. Current persistence mode.
        rdb_config (google.cloud.memorystore_v1.types.PersistenceConfig.RDBConfig):
            Optional. RDB configuration. This field will
            be ignored if mode is not RDB.
        aof_config (google.cloud.memorystore_v1.types.PersistenceConfig.AOFConfig):
            Optional. AOF configuration. This field will
            be ignored if mode is not AOF.
    """

    class PersistenceMode(proto.Enum):
        r"""Possible persistence modes.

        Values:
            PERSISTENCE_MODE_UNSPECIFIED (0):
                Not set.
            DISABLED (1):
                Persistence is disabled, and any snapshot
                data is deleted.
            RDB (2):
                RDB based persistence is enabled.
            AOF (3):
                AOF based persistence is enabled.
        """

        PERSISTENCE_MODE_UNSPECIFIED = 0
        DISABLED = 1
        RDB = 2
        AOF = 3

    class RDBConfig(proto.Message):
        r"""Configuration for RDB based persistence.

        Attributes:
            rdb_snapshot_period (google.cloud.memorystore_v1.types.PersistenceConfig.RDBConfig.SnapshotPeriod):
                Optional. Period between RDB snapshots.
            rdb_snapshot_start_time (google.protobuf.timestamp_pb2.Timestamp):
                Optional. Time that the first snapshot
                was/will be attempted, and to which future
                snapshots will be aligned. If not provided, the
                current time will be used.
        """

        class SnapshotPeriod(proto.Enum):
            r"""Possible snapshot periods.

            Values:
                SNAPSHOT_PERIOD_UNSPECIFIED (0):
                    Not set.
                ONE_HOUR (1):
                    One hour.
                SIX_HOURS (2):
                    Six hours.
                TWELVE_HOURS (3):
                    Twelve hours.
                TWENTY_FOUR_HOURS (4):
                    Twenty four hours.
            """

            SNAPSHOT_PERIOD_UNSPECIFIED = 0
            ONE_HOUR = 1
            SIX_HOURS = 2
            TWELVE_HOURS = 3
            TWENTY_FOUR_HOURS = 4

        rdb_snapshot_period: "PersistenceConfig.RDBConfig.SnapshotPeriod" = proto.Field(
            proto.ENUM,
            number=1,
            enum="PersistenceConfig.RDBConfig.SnapshotPeriod",
        )
        rdb_snapshot_start_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=2,
            message=timestamp_pb2.Timestamp,
        )

    class AOFConfig(proto.Message):
        r"""Configuration for AOF based persistence.

        Attributes:
            append_fsync (google.cloud.memorystore_v1.types.PersistenceConfig.AOFConfig.AppendFsync):
                Optional. The fsync mode.
        """

        class AppendFsync(proto.Enum):
            r"""Possible fsync modes.

            Values:
                APPEND_FSYNC_UNSPECIFIED (0):
                    Not set. Default: EVERY_SEC
                NEVER (1):
                    Never fsync. Normally Linux will flush data
                    every 30 seconds with this configuration, but
                    it's up to the kernel's exact tuning.
                EVERY_SEC (2):
                    Fsync every second. You may lose 1 second of
                    data if there is a disaster.
                ALWAYS (3):
                    Fsync every time new write commands are
                    appended to the AOF. The best data loss
                    protection at the cost of performance.
            """

            APPEND_FSYNC_UNSPECIFIED = 0
            NEVER = 1
            EVERY_SEC = 2
            ALWAYS = 3

        append_fsync: "PersistenceConfig.AOFConfig.AppendFsync" = proto.Field(
            proto.ENUM,
            number=1,
            enum="PersistenceConfig.AOFConfig.AppendFsync",
        )

    mode: PersistenceMode = proto.Field(
        proto.ENUM,
        number=1,
        enum=PersistenceMode,
    )
    rdb_config: RDBConfig = proto.Field(
        proto.MESSAGE,
        number=2,
        message=RDBConfig,
    )
    aof_config: AOFConfig = proto.Field(
        proto.MESSAGE,
        number=3,
        message=AOFConfig,
    )


class NodeConfig(proto.Message):
    r"""Represents configuration for nodes of the instance.

    Attributes:
        size_gb (float):
            Output only. Memory size in GB of the node.
    """

    size_gb: float = proto.Field(
        proto.DOUBLE,
        number=1,
    )


class ZoneDistributionConfig(proto.Message):
    r"""Zone distribution configuration for allocation of instance
    resources.

    Attributes:
        zone (str):
            Optional. Defines zone where all resources will be allocated
            with SINGLE_ZONE mode. Ignored for MULTI_ZONE mode.
        zones (MutableSequence[str]):
            Optional. Specify the zones of a multi-zone
            instance where Memorystore instance allocates
            resources. This flag isn't applicable for
            single-zone instances.
        active_zones (MutableSequence[str]):
            Output only. The exact list of zones where
            the instance currently has active VMs.
        mode (google.cloud.memorystore_v1.types.ZoneDistributionConfig.ZoneDistributionMode):
            Optional. Current zone distribution mode. Defaults to
            MULTI_ZONE.
    """

    class ZoneDistributionMode(proto.Enum):
        r"""Possible zone distribution modes.

        Values:
            ZONE_DISTRIBUTION_MODE_UNSPECIFIED (0):
                Not Set. Default: MULTI_ZONE
            MULTI_ZONE (1):
                Distribute resources across 3 zones picked at
                random within the region.
            SINGLE_ZONE (2):
                Provision resources in a single zone. Zone
                field must be specified.
        """

        ZONE_DISTRIBUTION_MODE_UNSPECIFIED = 0
        MULTI_ZONE = 1
        SINGLE_ZONE = 2

    zone: str = proto.Field(
        proto.STRING,
        number=2,
    )
    zones: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    active_zones: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    mode: ZoneDistributionMode = proto.Field(
        proto.ENUM,
        number=1,
        enum=ZoneDistributionMode,
    )


class RescheduleMaintenanceRequest(proto.Message):
    r"""Request for rescheduling instance maintenance.

    Attributes:
        name (str):
            Required. Name of the instance to reschedule maintenance
            for:
            ``projects/{project}/locations/{location_id}/instances/{instance}``
        reschedule_type (google.cloud.memorystore_v1.types.RescheduleMaintenanceRequest.RescheduleType):
            Required. If reschedule type is SPECIFIC_TIME, schedule_time
            must be set.
        schedule_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. Timestamp when the maintenance shall be
            rescheduled to if reschedule_type=SPECIFIC_TIME, in RFC 3339
            format. Example: ``2012-11-15T16:19:00.094Z``.
    """

    class RescheduleType(proto.Enum):
        r"""Reschedule options.

        Values:
            RESCHEDULE_TYPE_UNSPECIFIED (0):
                Not set.
            IMMEDIATE (1):
                If the user wants to schedule the maintenance
                to happen now.
            SPECIFIC_TIME (3):
                If the user wants to reschedule the
                maintenance to a specific time.
        """

        RESCHEDULE_TYPE_UNSPECIFIED = 0
        IMMEDIATE = 1
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


class ListAclPoliciesRequest(proto.Message):
    r"""Request for ``ListAclPolicies``.

    Attributes:
        parent (str):
            Required. The resource name of the ACL policy location using
            the form: ``projects/{project}/locations/{location}`` where
            ``location`` refers to a Google Cloud region.
        page_size (int):
            Optional. The maximum number of items to return.

            If not specified, a default value of 1000 will be used by
            the service. Regardless of the page_size value, the response
            may include a partial list and a caller should only rely on
            response's ``next_page_token`` to determine if there are
            more ACL policies left to be queried.

            The maximum value is 1000; values above 1000 will be coerced
            to 1000.
        page_token (str):
            Optional. The ``next_page_token`` value returned from a
            previous ``ListAclPolicies`` request, if any.
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


class ListAclPoliciesResponse(proto.Message):
    r"""Response for ``ListAclPolicies``.

    Attributes:
        acl_policies (MutableSequence[google.cloud.memorystore_v1.types.AclPolicy]):
            A list of ACL policies in the project in the specified
            location, or across all locations.

            If the ``location`` in the parent field of the request is
            "-", all regions available to the project are queried, and
            the results aggregated.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
        unreachable (MutableSequence[str]):
            Unordered list. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    acl_policies: MutableSequence["AclPolicy"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AclPolicy",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class ListAclPolicyRevisionsRequest(proto.Message):
    r"""Request for ``ListAclPolicyRevisions``.

    Attributes:
        parent (str):
            Required. The resource name of the ACL policy to list
            revisions for. Format:
            "projects/{project}/locations/{location}/aclPolicies/{acl_policy}".
        page_size (int):
            Optional. The maximum number of items to
            return.
        page_token (str):
            Optional. The ``next_page_token`` value returned from a
            previous ``ListAclPolicyRevisions`` request, if any.
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


class ListAclPolicyRevisionsResponse(proto.Message):
    r"""Response for ``ListAclPolicyRevisions``.

    Attributes:
        acl_policy_revisions (MutableSequence[google.cloud.memorystore_v1.types.AclPolicyRevision]):
            A list of ACL policy revisions.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
        unreachable (MutableSequence[str]):
            Unordered list. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    acl_policy_revisions: MutableSequence["AclPolicyRevision"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AclPolicyRevision",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class ListInstancesRequest(proto.Message):
    r"""Request message for [ListInstances][].

    Attributes:
        parent (str):
            Required. The parent to list instances from.
            Format: projects/{project}/locations/{location}
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Expression for filtering results.
        order_by (str):
            Optional. Sort results by a defined order. Supported values:
            "name", "create_time".
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
    r"""Response message for ``ListInstances``.

    Attributes:
        instances (MutableSequence[google.cloud.memorystore_v1.types.Instance]):
            If the {location} requested was "-" the
            response contains a list of instances from all
            locations. Instances in unreachable locations
            will be omitted.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
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


class GetAclPolicyRequest(proto.Message):
    r"""Request for ``GetAclPolicy``.

    Attributes:
        name (str):
            Required. Memorystore ACL policy resource name using the
            form:
            ``projects/{project}/locations/{location}/aclPolicies/{acl_policy}``
            where ``location`` refers to a Google Cloud region.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetAclPolicyRevisionRequest(proto.Message):
    r"""Request for ``GetAclPolicyRevision``.

    Attributes:
        name (str):
            Required. Memorystore ACL policy revision resource name
            using the form:
            ``projects/{project}/locations/{location}/aclPolicies/{acl_policy}/revisions/{revision}``
            where ``location`` refers to a Google Cloud region.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetInstanceRequest(proto.Message):
    r"""Request message for [GetInstance][].

    Attributes:
        name (str):
            Required. The name of the instance to
            retrieve. Format:
            projects/{project}/locations/{location}/instances/{instance}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateAclPolicyRequest(proto.Message):
    r"""Request for ``CreateAclPolicy``.

    Attributes:
        parent (str):
            Required. The resource name of the ACL policy location using
            the form: ``projects/{project}/locations/{location}`` where
            ``location`` refers to a Google Cloud region.
        acl_policy_id (str):
            Required. The logical name of the ACL policy in the customer
            project with the following restrictions:

            - Must contain only lowercase letters, numbers, and hyphens.
            - Must start with a letter.
            - Must be between 1-63 characters.
            - Must end with a number or a letter.
            - Must be unique within the customer project / location
        acl_policy (google.cloud.memorystore_v1.types.AclPolicy):
            Required. The ACL policy that is to be
            created.
        request_id (str):
            Optional. Idempotent request UUID.
            .
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    acl_policy_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    acl_policy: "AclPolicy" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="AclPolicy",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class CreateInstanceRequest(proto.Message):
    r"""Request message for [CreateInstance][].

    Attributes:
        parent (str):
            Required. The parent resource where this
            instance will be created. Format:
            projects/{project}/locations/{location}
        instance_id (str):
            Required. The ID to use for the instance, which will become
            the final component of the instance's resource name.

            This value is subject to the following restrictions:

            - Must be 4-63 characters in length
            - Must begin with a letter or digit
            - Must contain only lowercase letters, digits, and hyphens
            - Must not end with a hyphen
            - Must be unique within a location
        instance (google.cloud.memorystore_v1.types.Instance):
            Required. The instance to create.
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


class UpdateAclPolicyRequest(proto.Message):
    r"""Request for ``UpdateAclPolicy``.

    Attributes:
        acl_policy (google.cloud.memorystore_v1.types.AclPolicy):
            Required. The ACL policy to be updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Mask of fields to be updated. At least one path
            must be supplied in this field. The elements of the repeated
            paths field may only include these fields from
            ``AclPolicy``:

            - ``rules``
        request_id (str):
            Optional. Idempotent request UUID.
    """

    acl_policy: "AclPolicy" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="AclPolicy",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class UpdateInstanceRequest(proto.Message):
    r"""Request message for [UpdateInstance][].

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to be updated on
            the instance. At least one field must be
            specified.
        instance (google.cloud.memorystore_v1.types.Instance):
            Required. The instance to update.
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


class DeleteAclPolicyRequest(proto.Message):
    r"""Request for ``DeleteAclPolicy``.

    Attributes:
        name (str):
            Required. Memorystore ACL policy resource name using the
            form:
            ``projects/{project}/locations/{location}/aclPolicies/{acl_policy_id}``
            where ``location`` refers to a Google Cloud region.
        request_id (str):
            Optional. Idempotent request UUID.
        etag (str):
            Optional. Etag of the ACL policy. If this is
            different from the server's etag, the request
            will fail with an ABORTED error.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteInstanceRequest(proto.Message):
    r"""Request message for [DeleteInstance][].

    Attributes:
        name (str):
            Required. The name of the instance to delete.
            Format:
            projects/{project}/locations/{location}/instances/{instance}
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
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListBackupCollectionsRequest(proto.Message):
    r"""Request for ``ListBackupCollections``.

    Attributes:
        parent (str):
            Required. The resource name of the backupCollection location
            using the form:
            ``projects/{project_id}/locations/{location_id}`` where
            ``location_id`` refers to a Google Cloud region.
        page_size (int):
            Optional. The maximum number of items to return.

            If not specified, a default value of 1000 will be used by
            the service. Regardless of the page_size value, the response
            may include a partial list and a caller should only rely on
            response's ``next_page_token`` to determine if there are
            more clusters left to be queried.
        page_token (str):
            Optional. The ``next_page_token`` value returned from a
            previous ``ListBackupCollections`` request, if any.
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


class ListBackupCollectionsResponse(proto.Message):
    r"""Response for ``ListBackupCollections``.

    Attributes:
        backup_collections (MutableSequence[google.cloud.memorystore_v1.types.BackupCollection]):
            A list of backupCollections in the project.

            If the ``location_id`` in the parent field of the request is
            "-", all regions available to the project are queried, and
            the results aggregated. If in such an aggregated query a
            location is unavailable, a placeholder backupCollection
            entry is included in the response with the ``name`` field
            set to a value of the form
            ``projects/{project_id}/locations/{location_id}/backupCollections/``-
            and the ``status`` field set to ERROR and ``status_message``
            field set to "location not available for
            ListBackupCollections".
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

    backup_collections: MutableSequence["BackupCollection"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="BackupCollection",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetBackupCollectionRequest(proto.Message):
    r"""Request for ``GetBackupCollection``.

    Attributes:
        name (str):
            Required. Instance backupCollection resource name using the
            form:
            ``projects/{project_id}/locations/{location_id}/backupCollections/{backup_collection_id}``
            where ``location_id`` refers to a Google Cloud region.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListBackupsRequest(proto.Message):
    r"""Request for ``ListBackups``.

    Attributes:
        parent (str):
            Required. The resource name of the backupCollection using
            the form:
            ``projects/{project_id}/locations/{location_id}/backupCollections/{backup_collection_id}``
        page_size (int):
            Optional. The maximum number of items to return.

            If not specified, a default value of 1000 will be used by
            the service. Regardless of the page_size value, the response
            may include a partial list and a caller should only rely on
            response's ``next_page_token`` to determine if there are
            more clusters left to be queried.
        page_token (str):
            Optional. The ``next_page_token`` value returned from a
            previous ``ListBackupCollections`` request, if any.
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


class ListBackupsResponse(proto.Message):
    r"""Response for ``ListBackups``.

    Attributes:
        backups (MutableSequence[google.cloud.memorystore_v1.types.Backup]):
            A list of backups in the project.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
        unreachable (MutableSequence[str]):
            Backups that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    backups: MutableSequence["Backup"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Backup",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetBackupRequest(proto.Message):
    r"""Request for ``GetBackup``.

    Attributes:
        name (str):
            Required. Instance backup resource name using the form:
            ``projects/{project_id}/locations/{location_id}/backupCollections/{backup_collection_id}/backups/{backup_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteBackupRequest(proto.Message):
    r"""Request for ``DeleteBackup``.

    Attributes:
        name (str):
            Required. Instance backup resource name using the form:
            ``projects/{project_id}/locations/{location_id}/backupCollections/{backup_collection_id}/backups/{backup_id}``
        request_id (str):
            Optional. Idempotent request UUID.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ExportBackupRequest(proto.Message):
    r"""Request for ``ExportBackup``.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_bucket (str):
            Google Cloud Storage bucket, like
            "my-bucket".

            This field is a member of `oneof`_ ``destination``.
        name (str):
            Required. Instance backup resource name using the form:
            ``projects/{project_id}/locations/{location_id}/backupCollections/{backup_collection_id}/backups/{backup_id}``
    """

    gcs_bucket: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="destination",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class BackupInstanceRequest(proto.Message):
    r"""Request for ``BackupInstance``.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. Instance resource name using the form:
            ``projects/{project_id}/locations/{location_id}/instances/{instance_id}``
            where ``location_id`` refers to a Google Cloud region.
        ttl (google.protobuf.duration_pb2.Duration):
            Optional. TTL for the backup to expire. Value
            range is 1 day to 100 years. If not specified,
            the default value is 100 years.
        backup_id (str):
            Optional. The id of the backup to be created. If not
            specified, the default value ([YYYYMMDDHHMMSS]\_[Shortened
            Instance UID] is used.

            This field is a member of `oneof`_ ``_backup_id``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ttl: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )
    backup_id: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )


class GetCertificateAuthorityRequest(proto.Message):
    r"""Request message for ``GetCertificateAuthority``.

    Attributes:
        name (str):
            Required. The name of the certificate
            authority. Format:

            projects/{project}/locations/{location}/instances/{instance}/certificateAuthority
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListTokenAuthUsersRequest(proto.Message):
    r"""Request message for ``ListTokenAuthUsers``.

    Attributes:
        parent (str):
            Required. The parent to list token auth users
            from. Format:
            projects/{project}/locations/{location}/instances/{instance}
        page_size (int):
            Optional. The maximum number of items to return. The maximum
            value is 1000; values above 1000 will be coerced to 1000. If
            not specified, a default value of 1000 will be used by the
            service. Regardless of the page_size value, the response may
            include a partial list and a caller should only rely on
            response's ``next_page_token`` to determine if there are
            more token auth users left to be queried.
        page_token (str):
            Optional. The ``next_page_token`` value returned from a
            previous ``ListTokenAuthUsers`` request, if any.
        filter (str):
            Optional. Expression for filtering results.
        order_by (str):
            Optional. Sort results by a defined order.
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


class ListTokenAuthUsersResponse(proto.Message):
    r"""Response message for ``ListTokenAuthUsers``.

    Attributes:
        token_auth_users (MutableSequence[google.cloud.memorystore_v1.types.TokenAuthUser]):
            A list of token auth users in the project.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
        unreachable (MutableSequence[str]):
            Unordered list. Token auth users that could
            not be reached.
    """

    @property
    def raw_page(self):
        return self

    token_auth_users: MutableSequence["TokenAuthUser"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="TokenAuthUser",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetTokenAuthUserRequest(proto.Message):
    r"""Request message for ``GetTokenAuthUser``.

    Attributes:
        name (str):
            Required. The name of token auth user for a basic auth
            enabled instance. Format:
            projects/{project}/locations/{location}/instances/{instance}/tokenAuthUsers/{token_auth_user}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListAuthTokensRequest(proto.Message):
    r"""Request message for ``ListAuthTokens``.

    Attributes:
        parent (str):
            Required. The parent to list auth tokens from. Format:
            projects/{project}/locations/{location}/instances/{instance}/tokenAuthUsers/{token_auth_user}
        page_size (int):
            Optional. The maximum number of items to return. The maximum
            value is 1000; values above 1000 will be coerced to 1000.

            If not specified, a default value of 1000 will be used by
            the service. Regardless of the page_size value, the response
            may include a partial list and a caller should only rely on
            response's ``next_page_token`` to determine if there are
            more auth tokens left to be queried.
        page_token (str):
            Optional. The ``next_page_token`` value returned from a
            previous ``ListAuthTokens`` request, if any.
        filter (str):
            Optional. Expression for filtering results.
        order_by (str):
            Optional. Sort results by a defined order.
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


class ListAuthTokensResponse(proto.Message):
    r"""Response message for ``ListAuthTokens``.

    Attributes:
        auth_tokens (MutableSequence[google.cloud.memorystore_v1.types.AuthToken]):
            A list of auth tokens in the project.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
        unreachable (MutableSequence[str]):
            Unordered list. Auth tokens that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    auth_tokens: MutableSequence["AuthToken"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AuthToken",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetAuthTokenRequest(proto.Message):
    r"""Request message for ``GetAuthToken``.

    Attributes:
        name (str):
            Required. The name of token auth user for a token auth
            enabled instance. Format:
            projects/{project}/locations/{location}/instances/{instance}/tokenAuthUsers/{token_auth_user}/authTokens/{auth_token}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AddTokenAuthUserRequest(proto.Message):
    r"""Request message for ``AddTokenAuthUser``.

    Attributes:
        instance (str):
            Required. The instance resource that this
            token auth user will be added for. Format:
            projects/{project}/locations/{location}/instances/{instance}
        token_auth_user (str):
            Required. The name of the token auth user to
            add.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    token_auth_user: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteTokenAuthUserRequest(proto.Message):
    r"""Request message for ``DeleteTokenAuthUser``.

    Attributes:
        name (str):
            Required. The name of the token auth user to delete. Format:
            projects/{project}/locations/{location}/instances/{instance}/tokenAuthUsers/{token_auth_user}
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
            Optional. If set to true, any auth tokens
            from this user will also be deleted. Otherwise,
            the request will only work if the user has no
            auth tokens.
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


class AddAuthTokenRequest(proto.Message):
    r"""Request message for ``AddAuthToken``.

    Attributes:
        token_auth_user (str):
            Required. The name of the token auth user
            resource that this token will be added for.
        auth_token (google.cloud.memorystore_v1.types.AuthToken):
            Required. The auth token to add.
    """

    token_auth_user: str = proto.Field(
        proto.STRING,
        number=1,
    )
    auth_token: "AuthToken" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="AuthToken",
    )


class DeleteAuthTokenRequest(proto.Message):
    r"""Request message for ``DeleteAuthToken``.

    Attributes:
        name (str):
            Required. The name of the token auth user resource that this
            token will be deleted from. Format:
            projects/{project}/locations/{location}/instances/{instance}/tokenAuthUsers/{token_auth_user}/authTokens/{name}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CertificateAuthority(proto.Message):
    r"""A certificate authority for an instance.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        managed_server_ca (google.cloud.memorystore_v1.types.CertificateAuthority.ManagedCertificateAuthority):
            A managed server certificate authority.

            This field is a member of `oneof`_ ``server_ca``.
        name (str):
            Identifier. Unique name of the certificate
            authority. Format:

            projects/{project}/locations/{location}/instances/{instance}
    """

    class ManagedCertificateAuthority(proto.Message):
        r"""A managed certificate authority.

        Attributes:
            ca_certs (MutableSequence[google.cloud.memorystore_v1.types.CertificateAuthority.ManagedCertificateAuthority.CertChain]):
                PEM encoded CA certificate chains for managed
                server authentication.
        """

        class CertChain(proto.Message):
            r"""A certificate chain.

            Attributes:
                certificates (MutableSequence[str]):
                    The certificates that form the CA chain in
                    order of leaf to root.
            """

            certificates: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=1,
            )

        ca_certs: MutableSequence[
            "CertificateAuthority.ManagedCertificateAuthority.CertChain"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="CertificateAuthority.ManagedCertificateAuthority.CertChain",
        )

    managed_server_ca: ManagedCertificateAuthority = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="server_ca",
        message=ManagedCertificateAuthority,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SharedRegionalCertificateAuthority(proto.Message):
    r"""Shared regional certificate authority for an instance.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        managed_server_ca (google.cloud.memorystore_v1.types.SharedRegionalCertificateAuthority.RegionalManagedCertificateAuthority):
            CA certificate chains for memorystore managed
            server authentication.

            This field is a member of `oneof`_ ``server_ca``.
        name (str):
            Identifier. Unique name of the resource in this scope
            including project and location using the form:
            ``projects/{project}/locations/{location}/sharedRegionalCertificateAuthority``
    """

    class RegionalManagedCertificateAuthority(proto.Message):
        r"""CA certificate chains for memorystore managed server
        authentication.

        Attributes:
            ca_certs (MutableSequence[google.cloud.memorystore_v1.types.SharedRegionalCertificateAuthority.RegionalManagedCertificateAuthority.RegionalCertChain]):
                The PEM encoded CA certificate chains for
                memorystore managed server authentication
        """

        class RegionalCertChain(proto.Message):
            r"""The certificates that form the CA chain, from leaf to root
            order.

            Attributes:
                certificates (MutableSequence[str]):
                    The certificates that form the CA chain, from
                    leaf to root order.
            """

            certificates: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=1,
            )

        ca_certs: MutableSequence[
            "SharedRegionalCertificateAuthority.RegionalManagedCertificateAuthority.RegionalCertChain"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="SharedRegionalCertificateAuthority.RegionalManagedCertificateAuthority.RegionalCertChain",
        )

    managed_server_ca: RegionalManagedCertificateAuthority = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="server_ca",
        message=RegionalManagedCertificateAuthority,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetSharedRegionalCertificateAuthorityRequest(proto.Message):
    r"""Request for ``GetSharedRegionalCertificateAuthority``.

    Attributes:
        name (str):
            Required. Regional certificate authority resource name using
            the form:
            ``projects/{project}/locations/{location}/sharedRegionalCertificateAuthority``
            where ``location_id`` refers to a Google Cloud region.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
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


class EncryptionInfo(proto.Message):
    r"""EncryptionInfo describes the encryption information of a
    cluster.

    Attributes:
        encryption_type (google.cloud.memorystore_v1.types.EncryptionInfo.Type):
            Output only. Type of encryption.
        kms_key_versions (MutableSequence[str]):
            Output only. KMS key versions that are being
            used to protect the data at-rest.
        kms_key_primary_state (google.cloud.memorystore_v1.types.EncryptionInfo.KmsKeyState):
            Output only. The state of the primary version
            of the KMS key perceived by the system. This
            field is not populated in backups.
        last_update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The most recent time when the
            encryption info was updated.
    """

    class Type(proto.Enum):
        r"""Possible encryption types.

        Values:
            TYPE_UNSPECIFIED (0):
                Encryption type not specified. Defaults to
                GOOGLE_DEFAULT_ENCRYPTION.
            GOOGLE_DEFAULT_ENCRYPTION (1):
                The data is encrypted at rest with a key that
                is fully managed by Google. No key version will
                be populated. This is the default state.
            CUSTOMER_MANAGED_ENCRYPTION (2):
                The data is encrypted at rest with a key that
                is managed by the customer. KMS key versions
                will be populated.
        """

        TYPE_UNSPECIFIED = 0
        GOOGLE_DEFAULT_ENCRYPTION = 1
        CUSTOMER_MANAGED_ENCRYPTION = 2

    class KmsKeyState(proto.Enum):
        r"""The state of the KMS key perceived by the system. Refer to
        the public documentation for the impact of each state.

        Values:
            KMS_KEY_STATE_UNSPECIFIED (0):
                The default value. This value is unused.
            ENABLED (1):
                The KMS key is enabled and correctly
                configured.
            PERMISSION_DENIED (2):
                Permission denied on the KMS key.
            DISABLED (3):
                The KMS key is disabled.
            DESTROYED (4):
                The KMS key is destroyed.
            DESTROY_SCHEDULED (5):
                The KMS key is scheduled to be destroyed.
            EKM_KEY_UNREACHABLE_DETECTED (6):
                The EKM key is unreachable.
            BILLING_DISABLED (7):
                Billing is disabled for the project.
            UNKNOWN_FAILURE (8):
                All other unknown failures.
        """

        KMS_KEY_STATE_UNSPECIFIED = 0
        ENABLED = 1
        PERMISSION_DENIED = 2
        DISABLED = 3
        DESTROYED = 4
        DESTROY_SCHEDULED = 5
        EKM_KEY_UNREACHABLE_DETECTED = 6
        BILLING_DISABLED = 7
        UNKNOWN_FAILURE = 8

    encryption_type: Type = proto.Field(
        proto.ENUM,
        number=1,
        enum=Type,
    )
    kms_key_versions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    kms_key_primary_state: KmsKeyState = proto.Field(
        proto.ENUM,
        number=3,
        enum=KmsKeyState,
    )
    last_update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
