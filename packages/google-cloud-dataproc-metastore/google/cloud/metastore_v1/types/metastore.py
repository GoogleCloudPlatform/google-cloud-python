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
import google.protobuf.wrappers_pb2 as wrappers_pb2  # type: ignore
import google.type.dayofweek_pb2 as dayofweek_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.metastore.v1",
    manifest={
        "Service",
        "MaintenanceWindow",
        "HiveMetastoreConfig",
        "KerberosConfig",
        "Secret",
        "EncryptionConfig",
        "AuxiliaryVersionConfig",
        "NetworkConfig",
        "TelemetryConfig",
        "MetadataManagementActivity",
        "MetadataImport",
        "MetadataExport",
        "Backup",
        "Restore",
        "ScalingConfig",
        "ListServicesRequest",
        "ListServicesResponse",
        "GetServiceRequest",
        "CreateServiceRequest",
        "UpdateServiceRequest",
        "DeleteServiceRequest",
        "ListMetadataImportsRequest",
        "ListMetadataImportsResponse",
        "GetMetadataImportRequest",
        "CreateMetadataImportRequest",
        "UpdateMetadataImportRequest",
        "ListBackupsRequest",
        "ListBackupsResponse",
        "GetBackupRequest",
        "CreateBackupRequest",
        "DeleteBackupRequest",
        "ExportMetadataRequest",
        "RestoreServiceRequest",
        "OperationMetadata",
        "LocationMetadata",
        "DatabaseDumpSpec",
        "QueryMetadataRequest",
        "QueryMetadataResponse",
        "ErrorDetails",
        "MoveTableToDatabaseRequest",
        "MoveTableToDatabaseResponse",
        "AlterMetadataResourceLocationRequest",
        "AlterMetadataResourceLocationResponse",
    },
)


class Service(proto.Message):
    r"""A managed metastore service that serves metadata queries.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        hive_metastore_config (google.cloud.metastore_v1.types.HiveMetastoreConfig):
            Configuration information specific to running
            Hive metastore software as the metastore
            service.

            This field is a member of `oneof`_ ``metastore_config``.
        name (str):
            Immutable. The relative resource name of the metastore
            service, in the following format:

            ``projects/{project_number}/locations/{location_id}/services/{service_id}``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the metastore
            service was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the metastore
            service was last updated.
        labels (MutableMapping[str, str]):
            User-defined labels for the metastore
            service.
        network (str):
            Immutable. The relative resource name of the VPC network on
            which the instance can be accessed. It is specified in the
            following form:

            ``projects/{project_number}/global/networks/{network_id}``.
        endpoint_uri (str):
            Output only. The URI of the endpoint used to
            access the metastore service.
        port (int):
            The TCP port at which the metastore service
            is reached. Default: 9083.
        state (google.cloud.metastore_v1.types.Service.State):
            Output only. The current state of the
            metastore service.
        state_message (str):
            Output only. Additional information about the
            current state of the metastore service, if
            available.
        artifact_gcs_uri (str):
            Output only. A Cloud Storage URI (starting with ``gs://``)
            that specifies where artifacts related to the metastore
            service are stored.
        tier (google.cloud.metastore_v1.types.Service.Tier):
            The tier of the service.
        maintenance_window (google.cloud.metastore_v1.types.MaintenanceWindow):
            The one hour maintenance window of the
            metastore service. This specifies when the
            service can be restarted for maintenance
            purposes in UTC time. Maintenance window is not
            needed for services with the SPANNER database
            type.
        uid (str):
            Output only. The globally unique resource
            identifier of the metastore service.
        metadata_management_activity (google.cloud.metastore_v1.types.MetadataManagementActivity):
            Output only. The metadata management
            activities of the metastore service.
        release_channel (google.cloud.metastore_v1.types.Service.ReleaseChannel):
            Immutable. The release channel of the service. If
            unspecified, defaults to ``STABLE``.
        encryption_config (google.cloud.metastore_v1.types.EncryptionConfig):
            Immutable. Information used to configure the
            Dataproc Metastore service to encrypt customer
            data at rest. Cannot be updated.
        network_config (google.cloud.metastore_v1.types.NetworkConfig):
            The configuration specifying the network
            settings for the Dataproc Metastore service.
        database_type (google.cloud.metastore_v1.types.Service.DatabaseType):
            Immutable. The database type that the
            Metastore service stores its data.
        telemetry_config (google.cloud.metastore_v1.types.TelemetryConfig):
            The configuration specifying telemetry settings for the
            Dataproc Metastore service. If unspecified defaults to
            ``JSON``.
        scaling_config (google.cloud.metastore_v1.types.ScalingConfig):
            Scaling configuration of the metastore
            service.
    """

    class State(proto.Enum):
        r"""The current state of the metastore service.

        Values:
            STATE_UNSPECIFIED (0):
                The state of the metastore service is
                unknown.
            CREATING (1):
                The metastore service is in the process of
                being created.
            ACTIVE (2):
                The metastore service is running and ready to
                serve queries.
            SUSPENDING (3):
                The metastore service is entering suspension.
                Its query-serving availability may cease
                unexpectedly.
            SUSPENDED (4):
                The metastore service is suspended and unable
                to serve queries.
            UPDATING (5):
                The metastore service is being updated. It
                remains usable but cannot accept additional
                update requests or be deleted at this time.
            DELETING (6):
                The metastore service is undergoing deletion.
                It cannot be used.
            ERROR (7):
                The metastore service has encountered an
                error and cannot be used. The metastore service
                should be deleted.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        SUSPENDING = 3
        SUSPENDED = 4
        UPDATING = 5
        DELETING = 6
        ERROR = 7

    class Tier(proto.Enum):
        r"""Available service tiers.

        Values:
            TIER_UNSPECIFIED (0):
                The tier is not set.
            DEVELOPER (1):
                The developer tier provides limited
                scalability and no fault tolerance. Good for
                low-cost proof-of-concept.
            ENTERPRISE (3):
                The enterprise tier provides multi-zone high
                availability, and sufficient scalability for
                enterprise-level Dataproc Metastore workloads.
        """

        TIER_UNSPECIFIED = 0
        DEVELOPER = 1
        ENTERPRISE = 3

    class ReleaseChannel(proto.Enum):
        r"""Release channels bundle features of varying levels of
        stability. Newer features may be introduced initially into less
        stable release channels and can be automatically promoted into
        more stable release channels.

        Values:
            RELEASE_CHANNEL_UNSPECIFIED (0):
                Release channel is not specified.
            CANARY (1):
                The ``CANARY`` release channel contains the newest features,
                which may be unstable and subject to unresolved issues with
                no known workarounds. Services using the ``CANARY`` release
                channel are not subject to any SLAs.
            STABLE (2):
                The ``STABLE`` release channel contains features that are
                considered stable and have been validated for production
                use.
        """

        RELEASE_CHANNEL_UNSPECIFIED = 0
        CANARY = 1
        STABLE = 2

    class DatabaseType(proto.Enum):
        r"""The backend database type for the metastore service.

        Values:
            DATABASE_TYPE_UNSPECIFIED (0):
                The DATABASE_TYPE is not set.
            MYSQL (1):
                MySQL is used to persist the metastore data.
            SPANNER (2):
                Spanner is used to persist the metastore
                data.
        """

        DATABASE_TYPE_UNSPECIFIED = 0
        MYSQL = 1
        SPANNER = 2

    hive_metastore_config: "HiveMetastoreConfig" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="metastore_config",
        message="HiveMetastoreConfig",
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
    network: str = proto.Field(
        proto.STRING,
        number=7,
    )
    endpoint_uri: str = proto.Field(
        proto.STRING,
        number=8,
    )
    port: int = proto.Field(
        proto.INT32,
        number=9,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=10,
        enum=State,
    )
    state_message: str = proto.Field(
        proto.STRING,
        number=11,
    )
    artifact_gcs_uri: str = proto.Field(
        proto.STRING,
        number=12,
    )
    tier: Tier = proto.Field(
        proto.ENUM,
        number=13,
        enum=Tier,
    )
    maintenance_window: "MaintenanceWindow" = proto.Field(
        proto.MESSAGE,
        number=15,
        message="MaintenanceWindow",
    )
    uid: str = proto.Field(
        proto.STRING,
        number=16,
    )
    metadata_management_activity: "MetadataManagementActivity" = proto.Field(
        proto.MESSAGE,
        number=17,
        message="MetadataManagementActivity",
    )
    release_channel: ReleaseChannel = proto.Field(
        proto.ENUM,
        number=19,
        enum=ReleaseChannel,
    )
    encryption_config: "EncryptionConfig" = proto.Field(
        proto.MESSAGE,
        number=20,
        message="EncryptionConfig",
    )
    network_config: "NetworkConfig" = proto.Field(
        proto.MESSAGE,
        number=21,
        message="NetworkConfig",
    )
    database_type: DatabaseType = proto.Field(
        proto.ENUM,
        number=22,
        enum=DatabaseType,
    )
    telemetry_config: "TelemetryConfig" = proto.Field(
        proto.MESSAGE,
        number=23,
        message="TelemetryConfig",
    )
    scaling_config: "ScalingConfig" = proto.Field(
        proto.MESSAGE,
        number=24,
        message="ScalingConfig",
    )


class MaintenanceWindow(proto.Message):
    r"""Maintenance window. This specifies when Dataproc Metastore
    may perform system maintenance operation to the service.

    Attributes:
        hour_of_day (google.protobuf.wrappers_pb2.Int32Value):
            The hour of day (0-23) when the window
            starts.
        day_of_week (google.type.dayofweek_pb2.DayOfWeek):
            The day of week, when the window starts.
    """

    hour_of_day: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=1,
        message=wrappers_pb2.Int32Value,
    )
    day_of_week: dayofweek_pb2.DayOfWeek = proto.Field(
        proto.ENUM,
        number=2,
        enum=dayofweek_pb2.DayOfWeek,
    )


class HiveMetastoreConfig(proto.Message):
    r"""Specifies configuration information specific to running Hive
    metastore software as the metastore service.

    Attributes:
        version (str):
            Immutable. The Hive metastore schema version.
        config_overrides (MutableMapping[str, str]):
            A mapping of Hive metastore configuration key-value pairs to
            apply to the Hive metastore (configured in
            ``hive-site.xml``). The mappings override system defaults
            (some keys cannot be overridden). These overrides are also
            applied to auxiliary versions and can be further customized
            in the auxiliary version's ``AuxiliaryVersionConfig``.
        kerberos_config (google.cloud.metastore_v1.types.KerberosConfig):
            Information used to configure the Hive metastore service as
            a service principal in a Kerberos realm. To disable
            Kerberos, use the ``UpdateService`` method and specify this
            field's path (``hive_metastore_config.kerberos_config``) in
            the request's ``update_mask`` while omitting this field from
            the request's ``service``.
        endpoint_protocol (google.cloud.metastore_v1.types.HiveMetastoreConfig.EndpointProtocol):
            The protocol to use for the metastore service endpoint. If
            unspecified, defaults to ``THRIFT``.
        auxiliary_versions (MutableMapping[str, google.cloud.metastore_v1.types.AuxiliaryVersionConfig]):
            A mapping of Hive metastore version to the auxiliary version
            configuration. When specified, a secondary Hive metastore
            service is created along with the primary service. All
            auxiliary versions must be less than the service's primary
            version. The key is the auxiliary service name and it must
            match the regular expression `a-z <[-a-z0-9]*[a-z0-9]>`__?.
            This means that the first character must be a lowercase
            letter, and all the following characters must be hyphens,
            lowercase letters, or digits, except the last character,
            which cannot be a hyphen.
    """

    class EndpointProtocol(proto.Enum):
        r"""Protocols available for serving the metastore service
        endpoint.

        Values:
            ENDPOINT_PROTOCOL_UNSPECIFIED (0):
                The protocol is not set.
            THRIFT (1):
                Use the legacy Apache Thrift protocol for the
                metastore service endpoint.
            GRPC (2):
                Use the modernized gRPC protocol for the
                metastore service endpoint.
        """

        ENDPOINT_PROTOCOL_UNSPECIFIED = 0
        THRIFT = 1
        GRPC = 2

    version: str = proto.Field(
        proto.STRING,
        number=1,
    )
    config_overrides: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )
    kerberos_config: "KerberosConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="KerberosConfig",
    )
    endpoint_protocol: EndpointProtocol = proto.Field(
        proto.ENUM,
        number=4,
        enum=EndpointProtocol,
    )
    auxiliary_versions: MutableMapping[str, "AuxiliaryVersionConfig"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=5,
        message="AuxiliaryVersionConfig",
    )


class KerberosConfig(proto.Message):
    r"""Configuration information for a Kerberos principal.

    Attributes:
        keytab (google.cloud.metastore_v1.types.Secret):
            A Kerberos keytab file that can be used to
            authenticate a service principal with a Kerberos
            Key Distribution Center (KDC).
        principal (str):
            A Kerberos principal that exists in the both the keytab the
            KDC to authenticate as. A typical principal is of the form
            ``primary/instance@REALM``, but there is no exact format.
        krb5_config_gcs_uri (str):
            A Cloud Storage URI that specifies the path to a krb5.conf
            file. It is of the form
            ``gs://{bucket_name}/path/to/krb5.conf``, although the file
            does not need to be named krb5.conf explicitly.
    """

    keytab: "Secret" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Secret",
    )
    principal: str = proto.Field(
        proto.STRING,
        number=2,
    )
    krb5_config_gcs_uri: str = proto.Field(
        proto.STRING,
        number=3,
    )


class Secret(proto.Message):
    r"""A securely stored value.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        cloud_secret (str):
            The relative resource name of a Secret Manager secret
            version, in the following form:

            ``projects/{project_number}/secrets/{secret_id}/versions/{version_id}``.

            This field is a member of `oneof`_ ``value``.
    """

    cloud_secret: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="value",
    )


class EncryptionConfig(proto.Message):
    r"""Encryption settings for the service.

    Attributes:
        kms_key (str):
            The fully qualified customer provided Cloud KMS key name to
            use for customer data encryption, in the following form:

            ``projects/{project_number}/locations/{location_id}/keyRings/{key_ring_id}/cryptoKeys/{crypto_key_id}``.
    """

    kms_key: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AuxiliaryVersionConfig(proto.Message):
    r"""Configuration information for the auxiliary service versions.

    Attributes:
        version (str):
            The Hive metastore version of the auxiliary
            service. It must be less than the primary Hive
            metastore service's version.
        config_overrides (MutableMapping[str, str]):
            A mapping of Hive metastore configuration key-value pairs to
            apply to the auxiliary Hive metastore (configured in
            ``hive-site.xml``) in addition to the primary version's
            overrides. If keys are present in both the auxiliary
            version's overrides and the primary version's overrides, the
            value from the auxiliary version's overrides takes
            precedence.
        network_config (google.cloud.metastore_v1.types.NetworkConfig):
            Output only. The network configuration
            contains the endpoint URI(s) of the auxiliary
            Hive metastore service.
    """

    version: str = proto.Field(
        proto.STRING,
        number=1,
    )
    config_overrides: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )
    network_config: "NetworkConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="NetworkConfig",
    )


class NetworkConfig(proto.Message):
    r"""Network configuration for the Dataproc Metastore service.

    Next available ID: 4

    Attributes:
        consumers (MutableSequence[google.cloud.metastore_v1.types.NetworkConfig.Consumer]):
            Immutable. The consumer-side network
            configuration for the Dataproc Metastore
            instance.
    """

    class Consumer(proto.Message):
        r"""Contains information of the customer's network
        configurations.
        Next available ID: 5


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            subnetwork (str):
                Immutable. The subnetwork of the customer project from which
                an IP address is reserved and used as the Dataproc Metastore
                service's endpoint. It is accessible to hosts in the subnet
                and to all hosts in a subnet in the same region and same
                network. There must be at least one IP address available in
                the subnet's primary range. The subnet is specified in the
                following form:

                ``projects/{project_number}/regions/{region_id}/subnetworks/{subnetwork_id}``

                This field is a member of `oneof`_ ``vpc_resource``.
            endpoint_uri (str):
                Output only. The URI of the endpoint used to
                access the metastore service.
            endpoint_location (str):
                Output only. The location of the endpoint URI. Format:
                ``projects/{project}/locations/{location}``.
        """

        subnetwork: str = proto.Field(
            proto.STRING,
            number=1,
            oneof="vpc_resource",
        )
        endpoint_uri: str = proto.Field(
            proto.STRING,
            number=3,
        )
        endpoint_location: str = proto.Field(
            proto.STRING,
            number=4,
        )

    consumers: MutableSequence[Consumer] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=Consumer,
    )


class TelemetryConfig(proto.Message):
    r"""Telemetry Configuration for the Dataproc Metastore service.

    Attributes:
        log_format (google.cloud.metastore_v1.types.TelemetryConfig.LogFormat):
            The output format of the Dataproc Metastore
            service's logs.
    """

    class LogFormat(proto.Enum):
        r"""

        Values:
            LOG_FORMAT_UNSPECIFIED (0):
                The LOG_FORMAT is not set.
            LEGACY (1):
                Logging output uses the legacy ``textPayload`` format.
            JSON (2):
                Logging output uses the ``jsonPayload`` format.
        """

        LOG_FORMAT_UNSPECIFIED = 0
        LEGACY = 1
        JSON = 2

    log_format: LogFormat = proto.Field(
        proto.ENUM,
        number=1,
        enum=LogFormat,
    )


class MetadataManagementActivity(proto.Message):
    r"""The metadata management activities of the metastore service.

    Attributes:
        metadata_exports (MutableSequence[google.cloud.metastore_v1.types.MetadataExport]):
            Output only. The latest metadata exports of
            the metastore service.
        restores (MutableSequence[google.cloud.metastore_v1.types.Restore]):
            Output only. The latest restores of the
            metastore service.
    """

    metadata_exports: MutableSequence["MetadataExport"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="MetadataExport",
    )
    restores: MutableSequence["Restore"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Restore",
    )


class MetadataImport(proto.Message):
    r"""A metastore resource that imports metadata.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        database_dump (google.cloud.metastore_v1.types.MetadataImport.DatabaseDump):
            Immutable. A database dump from a
            pre-existing metastore's database.

            This field is a member of `oneof`_ ``metadata``.
        name (str):
            Immutable. The relative resource name of the metadata
            import, of the form:

            ``projects/{project_number}/locations/{location_id}/services/{service_id}/metadataImports/{metadata_import_id}``.
        description (str):
            The description of the metadata import.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the metadata
            import was started.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the metadata
            import was last updated.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the metadata
            import finished.
        state (google.cloud.metastore_v1.types.MetadataImport.State):
            Output only. The current state of the
            metadata import.
    """

    class State(proto.Enum):
        r"""The current state of the metadata import.

        Values:
            STATE_UNSPECIFIED (0):
                The state of the metadata import is unknown.
            RUNNING (1):
                The metadata import is running.
            SUCCEEDED (2):
                The metadata import completed successfully.
            UPDATING (3):
                The metadata import is being updated.
            FAILED (4):
                The metadata import failed, and attempted
                metadata changes were rolled back.
        """

        STATE_UNSPECIFIED = 0
        RUNNING = 1
        SUCCEEDED = 2
        UPDATING = 3
        FAILED = 4

    class DatabaseDump(proto.Message):
        r"""A specification of the location of and metadata about a
        database dump from a relational database management system.

        Attributes:
            database_type (google.cloud.metastore_v1.types.MetadataImport.DatabaseDump.DatabaseType):
                The type of the database.
            gcs_uri (str):
                A Cloud Storage object or folder URI that specifies the
                source from which to import metadata. It must begin with
                ``gs://``.
            source_database (str):
                The name of the source database.
            type_ (google.cloud.metastore_v1.types.DatabaseDumpSpec.Type):
                Optional. The type of the database dump. If unspecified,
                defaults to ``MYSQL``.
        """

        class DatabaseType(proto.Enum):
            r"""The type of the database.

            Values:
                DATABASE_TYPE_UNSPECIFIED (0):
                    The type of the source database is unknown.
                MYSQL (1):
                    The type of the source database is MySQL.
            """

            DATABASE_TYPE_UNSPECIFIED = 0
            MYSQL = 1

        database_type: "MetadataImport.DatabaseDump.DatabaseType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="MetadataImport.DatabaseDump.DatabaseType",
        )
        gcs_uri: str = proto.Field(
            proto.STRING,
            number=2,
        )
        source_database: str = proto.Field(
            proto.STRING,
            number=3,
        )
        type_: "DatabaseDumpSpec.Type" = proto.Field(
            proto.ENUM,
            number=4,
            enum="DatabaseDumpSpec.Type",
        )

    database_dump: DatabaseDump = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="metadata",
        message=DatabaseDump,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=5,
        enum=State,
    )


class MetadataExport(proto.Message):
    r"""The details of a metadata export operation.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        destination_gcs_uri (str):
            Output only. A Cloud Storage URI of a folder that metadata
            are exported to, in the form of
            ``gs://<bucket_name>/<path_inside_bucket>/<export_folder>``,
            where ``<export_folder>`` is automatically generated.

            This field is a member of `oneof`_ ``destination``.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the export
            started.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the export ended.
        state (google.cloud.metastore_v1.types.MetadataExport.State):
            Output only. The current state of the export.
        database_dump_type (google.cloud.metastore_v1.types.DatabaseDumpSpec.Type):
            Output only. The type of the database dump.
    """

    class State(proto.Enum):
        r"""The current state of the metadata export.

        Values:
            STATE_UNSPECIFIED (0):
                The state of the metadata export is unknown.
            RUNNING (1):
                The metadata export is running.
            SUCCEEDED (2):
                The metadata export completed successfully.
            FAILED (3):
                The metadata export failed.
            CANCELLED (4):
                The metadata export is cancelled.
        """

        STATE_UNSPECIFIED = 0
        RUNNING = 1
        SUCCEEDED = 2
        FAILED = 3
        CANCELLED = 4

    destination_gcs_uri: str = proto.Field(
        proto.STRING,
        number=4,
        oneof="destination",
    )
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
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )
    database_dump_type: "DatabaseDumpSpec.Type" = proto.Field(
        proto.ENUM,
        number=5,
        enum="DatabaseDumpSpec.Type",
    )


class Backup(proto.Message):
    r"""The details of a backup resource.

    Attributes:
        name (str):
            Immutable. The relative resource name of the backup, in the
            following form:

            ``projects/{project_number}/locations/{location_id}/services/{service_id}/backups/{backup_id}``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the backup was
            started.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the backup
            finished creating.
        state (google.cloud.metastore_v1.types.Backup.State):
            Output only. The current state of the backup.
        service_revision (google.cloud.metastore_v1.types.Service):
            Output only. The revision of the service at
            the time of backup.
        description (str):
            The description of the backup.
        restoring_services (MutableSequence[str]):
            Output only. Services that are restoring from
            the backup.
    """

    class State(proto.Enum):
        r"""The current state of the backup.

        Values:
            STATE_UNSPECIFIED (0):
                The state of the backup is unknown.
            CREATING (1):
                The backup is being created.
            DELETING (2):
                The backup is being deleted.
            ACTIVE (3):
                The backup is active and ready to use.
            FAILED (4):
                The backup failed.
            RESTORING (5):
                The backup is being restored.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        DELETING = 2
        ACTIVE = 3
        FAILED = 4
        RESTORING = 5

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )
    service_revision: "Service" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="Service",
    )
    description: str = proto.Field(
        proto.STRING,
        number=6,
    )
    restoring_services: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )


class Restore(proto.Message):
    r"""The details of a metadata restore operation.

    Attributes:
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the restore
            started.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the restore ended.
        state (google.cloud.metastore_v1.types.Restore.State):
            Output only. The current state of the
            restore.
        backup (str):
            Output only. The relative resource name of the metastore
            service backup to restore from, in the following form:

            ``projects/{project_id}/locations/{location_id}/services/{service_id}/backups/{backup_id}``.
        type_ (google.cloud.metastore_v1.types.Restore.RestoreType):
            Output only. The type of restore.
        details (str):
            Output only. The restore details containing
            the revision of the service to be restored to,
            in format of JSON.
    """

    class State(proto.Enum):
        r"""The current state of the restore.

        Values:
            STATE_UNSPECIFIED (0):
                The state of the metadata restore is unknown.
            RUNNING (1):
                The metadata restore is running.
            SUCCEEDED (2):
                The metadata restore completed successfully.
            FAILED (3):
                The metadata restore failed.
            CANCELLED (4):
                The metadata restore is cancelled.
        """

        STATE_UNSPECIFIED = 0
        RUNNING = 1
        SUCCEEDED = 2
        FAILED = 3
        CANCELLED = 4

    class RestoreType(proto.Enum):
        r"""The type of restore. If unspecified, defaults to ``METADATA_ONLY``.

        Values:
            RESTORE_TYPE_UNSPECIFIED (0):
                The restore type is unknown.
            FULL (1):
                The service's metadata and configuration are
                restored.
            METADATA_ONLY (2):
                Only the service's metadata is restored.
        """

        RESTORE_TYPE_UNSPECIFIED = 0
        FULL = 1
        METADATA_ONLY = 2

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
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )
    backup: str = proto.Field(
        proto.STRING,
        number=4,
    )
    type_: RestoreType = proto.Field(
        proto.ENUM,
        number=5,
        enum=RestoreType,
    )
    details: str = proto.Field(
        proto.STRING,
        number=6,
    )


class ScalingConfig(proto.Message):
    r"""Represents the scaling configuration of a metastore service.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        instance_size (google.cloud.metastore_v1.types.ScalingConfig.InstanceSize):
            An enum of readable instance sizes, with each instance size
            mapping to a float value (e.g. InstanceSize.EXTRA_SMALL =
            scaling_factor(0.1))

            This field is a member of `oneof`_ ``scaling_model``.
        scaling_factor (float):
            Scaling factor, increments of 0.1 for values
            less than 1.0, and increments of 1.0 for values
            greater than 1.0.

            This field is a member of `oneof`_ ``scaling_model``.
    """

    class InstanceSize(proto.Enum):
        r"""Metastore instance sizes.

        Values:
            INSTANCE_SIZE_UNSPECIFIED (0):
                Unspecified instance size
            EXTRA_SMALL (1):
                Extra small instance size, maps to a scaling
                factor of 0.1.
            SMALL (2):
                Small instance size, maps to a scaling factor
                of 0.5.
            MEDIUM (3):
                Medium instance size, maps to a scaling
                factor of 1.0.
            LARGE (4):
                Large instance size, maps to a scaling factor
                of 3.0.
            EXTRA_LARGE (5):
                Extra large instance size, maps to a scaling
                factor of 6.0.
        """

        INSTANCE_SIZE_UNSPECIFIED = 0
        EXTRA_SMALL = 1
        SMALL = 2
        MEDIUM = 3
        LARGE = 4
        EXTRA_LARGE = 5

    instance_size: InstanceSize = proto.Field(
        proto.ENUM,
        number=1,
        oneof="scaling_model",
        enum=InstanceSize,
    )
    scaling_factor: float = proto.Field(
        proto.FLOAT,
        number=2,
        oneof="scaling_model",
    )


class ListServicesRequest(proto.Message):
    r"""Request message for
    [DataprocMetastore.ListServices][google.cloud.metastore.v1.DataprocMetastore.ListServices].

    Attributes:
        parent (str):
            Required. The relative resource name of the location of
            metastore services to list, in the following form:

            ``projects/{project_number}/locations/{location_id}``.
        page_size (int):
            Optional. The maximum number of services to
            return. The response may contain less than the
            maximum number. If unspecified, no more than 500
            services are returned. The maximum value is
            1000; values above 1000 are changed to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            [DataprocMetastore.ListServices][google.cloud.metastore.v1.DataprocMetastore.ListServices]
            call. Provide this token to retrieve the subsequent page.

            To retrieve the first page, supply an empty page token.

            When paginating, other parameters provided to
            [DataprocMetastore.ListServices][google.cloud.metastore.v1.DataprocMetastore.ListServices]
            must match the call that provided the page token.
        filter (str):
            Optional. The filter to apply to list
            results.
        order_by (str):
            Optional. Specify the ordering of results as described in
            `Sorting
            Order <https://cloud.google.com/apis/design/design_patterns#sorting_order>`__.
            If not specified, the results will be sorted in the default
            order.
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


class ListServicesResponse(proto.Message):
    r"""Response message for
    [DataprocMetastore.ListServices][google.cloud.metastore.v1.DataprocMetastore.ListServices].

    Attributes:
        services (MutableSequence[google.cloud.metastore_v1.types.Service]):
            The services in the specified location.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    services: MutableSequence["Service"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Service",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetServiceRequest(proto.Message):
    r"""Request message for
    [DataprocMetastore.GetService][google.cloud.metastore.v1.DataprocMetastore.GetService].

    Attributes:
        name (str):
            Required. The relative resource name of the metastore
            service to retrieve, in the following form:

            ``projects/{project_number}/locations/{location_id}/services/{service_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateServiceRequest(proto.Message):
    r"""Request message for
    [DataprocMetastore.CreateService][google.cloud.metastore.v1.DataprocMetastore.CreateService].

    Attributes:
        parent (str):
            Required. The relative resource name of the location in
            which to create a metastore service, in the following form:

            ``projects/{project_number}/locations/{location_id}``.
        service_id (str):
            Required. The ID of the metastore service,
            which is used as the final component of the
            metastore service's name.

            This value must be between 2 and 63 characters
            long inclusive, begin with a letter, end with a
            letter or number, and consist of alpha-numeric
            ASCII characters or hyphens.
        service (google.cloud.metastore_v1.types.Service):
            Required. The Metastore service to create. The ``name``
            field is ignored. The ID of the created metastore service
            must be provided in the request's ``service_id`` field.
        request_id (str):
            Optional. A request ID. Specify a unique request ID to allow
            the server to ignore the request if it has completed. The
            server will ignore subsequent requests that provide a
            duplicate request ID for at least 60 minutes after the first
            request.

            For example, if an initial request times out, followed by
            another request with the same request ID, the server ignores
            the second request to prevent the creation of duplicate
            commitments.

            The request ID must be a valid
            `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier#Format>`__
            A zero UUID (00000000-0000-0000-0000-000000000000) is not
            supported.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    service_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    service: "Service" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Service",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateServiceRequest(proto.Message):
    r"""Request message for
    [DataprocMetastore.UpdateService][google.cloud.metastore.v1.DataprocMetastore.UpdateService].

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. A field mask used to specify the fields to be
            overwritten in the metastore service resource by the update.
            Fields specified in the ``update_mask`` are relative to the
            resource (not to the full request). A field is overwritten
            if it is in the mask.
        service (google.cloud.metastore_v1.types.Service):
            Required. The metastore service to update. The server only
            merges fields in the service if they are specified in
            ``update_mask``.

            The metastore service's ``name`` field is used to identify
            the metastore service to be updated.
        request_id (str):
            Optional. A request ID. Specify a unique request ID to allow
            the server to ignore the request if it has completed. The
            server will ignore subsequent requests that provide a
            duplicate request ID for at least 60 minutes after the first
            request.

            For example, if an initial request times out, followed by
            another request with the same request ID, the server ignores
            the second request to prevent the creation of duplicate
            commitments.

            The request ID must be a valid
            `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier#Format>`__
            A zero UUID (00000000-0000-0000-0000-000000000000) is not
            supported.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    service: "Service" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Service",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteServiceRequest(proto.Message):
    r"""Request message for
    [DataprocMetastore.DeleteService][google.cloud.metastore.v1.DataprocMetastore.DeleteService].

    Attributes:
        name (str):
            Required. The relative resource name of the metastore
            service to delete, in the following form:

            ``projects/{project_number}/locations/{location_id}/services/{service_id}``.
        request_id (str):
            Optional. A request ID. Specify a unique request ID to allow
            the server to ignore the request if it has completed. The
            server will ignore subsequent requests that provide a
            duplicate request ID for at least 60 minutes after the first
            request.

            For example, if an initial request times out, followed by
            another request with the same request ID, the server ignores
            the second request to prevent the creation of duplicate
            commitments.

            The request ID must be a valid
            `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier#Format>`__
            A zero UUID (00000000-0000-0000-0000-000000000000) is not
            supported.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListMetadataImportsRequest(proto.Message):
    r"""Request message for
    [DataprocMetastore.ListMetadataImports][google.cloud.metastore.v1.DataprocMetastore.ListMetadataImports].

    Attributes:
        parent (str):
            Required. The relative resource name of the service whose
            metadata imports to list, in the following form:

            ``projects/{project_number}/locations/{location_id}/services/{service_id}/metadataImports``.
        page_size (int):
            Optional. The maximum number of imports to
            return. The response may contain less than the
            maximum number. If unspecified, no more than 500
            imports are returned. The maximum value is 1000;
            values above 1000 are changed to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            [DataprocMetastore.ListServices][google.cloud.metastore.v1.DataprocMetastore.ListServices]
            call. Provide this token to retrieve the subsequent page.

            To retrieve the first page, supply an empty page token.

            When paginating, other parameters provided to
            [DataprocMetastore.ListServices][google.cloud.metastore.v1.DataprocMetastore.ListServices]
            must match the call that provided the page token.
        filter (str):
            Optional. The filter to apply to list
            results.
        order_by (str):
            Optional. Specify the ordering of results as described in
            `Sorting
            Order <https://cloud.google.com/apis/design/design_patterns#sorting_order>`__.
            If not specified, the results will be sorted in the default
            order.
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


class ListMetadataImportsResponse(proto.Message):
    r"""Response message for
    [DataprocMetastore.ListMetadataImports][google.cloud.metastore.v1.DataprocMetastore.ListMetadataImports].

    Attributes:
        metadata_imports (MutableSequence[google.cloud.metastore_v1.types.MetadataImport]):
            The imports in the specified service.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    metadata_imports: MutableSequence["MetadataImport"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="MetadataImport",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetMetadataImportRequest(proto.Message):
    r"""Request message for
    [DataprocMetastore.GetMetadataImport][google.cloud.metastore.v1.DataprocMetastore.GetMetadataImport].

    Attributes:
        name (str):
            Required. The relative resource name of the metadata import
            to retrieve, in the following form:

            ``projects/{project_number}/locations/{location_id}/services/{service_id}/metadataImports/{import_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateMetadataImportRequest(proto.Message):
    r"""Request message for
    [DataprocMetastore.CreateMetadataImport][google.cloud.metastore.v1.DataprocMetastore.CreateMetadataImport].

    Attributes:
        parent (str):
            Required. The relative resource name of the service in which
            to create a metastore import, in the following form:

            ``projects/{project_number}/locations/{location_id}/services/{service_id}``.
        metadata_import_id (str):
            Required. The ID of the metadata import,
            which is used as the final component of the
            metadata import's name.

            This value must be between 1 and 64 characters
            long, begin with a letter, end with a letter or
            number, and consist of alpha-numeric ASCII
            characters or hyphens.
        metadata_import (google.cloud.metastore_v1.types.MetadataImport):
            Required. The metadata import to create. The ``name`` field
            is ignored. The ID of the created metadata import must be
            provided in the request's ``metadata_import_id`` field.
        request_id (str):
            Optional. A request ID. Specify a unique request ID to allow
            the server to ignore the request if it has completed. The
            server will ignore subsequent requests that provide a
            duplicate request ID for at least 60 minutes after the first
            request.

            For example, if an initial request times out, followed by
            another request with the same request ID, the server ignores
            the second request to prevent the creation of duplicate
            commitments.

            The request ID must be a valid
            `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier#Format>`__
            A zero UUID (00000000-0000-0000-0000-000000000000) is not
            supported.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    metadata_import_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    metadata_import: "MetadataImport" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="MetadataImport",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateMetadataImportRequest(proto.Message):
    r"""Request message for
    [DataprocMetastore.UpdateMetadataImport][google.cloud.metastore.v1.DataprocMetastore.UpdateMetadataImport].

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. A field mask used to specify the fields to be
            overwritten in the metadata import resource by the update.
            Fields specified in the ``update_mask`` are relative to the
            resource (not to the full request). A field is overwritten
            if it is in the mask.
        metadata_import (google.cloud.metastore_v1.types.MetadataImport):
            Required. The metadata import to update. The server only
            merges fields in the import if they are specified in
            ``update_mask``.

            The metadata import's ``name`` field is used to identify the
            metastore import to be updated.
        request_id (str):
            Optional. A request ID. Specify a unique request ID to allow
            the server to ignore the request if it has completed. The
            server will ignore subsequent requests that provide a
            duplicate request ID for at least 60 minutes after the first
            request.

            For example, if an initial request times out, followed by
            another request with the same request ID, the server ignores
            the second request to prevent the creation of duplicate
            commitments.

            The request ID must be a valid
            `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier#Format>`__
            A zero UUID (00000000-0000-0000-0000-000000000000) is not
            supported.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    metadata_import: "MetadataImport" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="MetadataImport",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListBackupsRequest(proto.Message):
    r"""Request message for
    [DataprocMetastore.ListBackups][google.cloud.metastore.v1.DataprocMetastore.ListBackups].

    Attributes:
        parent (str):
            Required. The relative resource name of the service whose
            backups to list, in the following form:

            ``projects/{project_number}/locations/{location_id}/services/{service_id}/backups``.
        page_size (int):
            Optional. The maximum number of backups to
            return. The response may contain less than the
            maximum number. If unspecified, no more than 500
            backups are returned. The maximum value is 1000;
            values above 1000 are changed to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            [DataprocMetastore.ListBackups][google.cloud.metastore.v1.DataprocMetastore.ListBackups]
            call. Provide this token to retrieve the subsequent page.

            To retrieve the first page, supply an empty page token.

            When paginating, other parameters provided to
            [DataprocMetastore.ListBackups][google.cloud.metastore.v1.DataprocMetastore.ListBackups]
            must match the call that provided the page token.
        filter (str):
            Optional. The filter to apply to list
            results.
        order_by (str):
            Optional. Specify the ordering of results as described in
            `Sorting
            Order <https://cloud.google.com/apis/design/design_patterns#sorting_order>`__.
            If not specified, the results will be sorted in the default
            order.
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


class ListBackupsResponse(proto.Message):
    r"""Response message for
    [DataprocMetastore.ListBackups][google.cloud.metastore.v1.DataprocMetastore.ListBackups].

    Attributes:
        backups (MutableSequence[google.cloud.metastore_v1.types.Backup]):
            The backups of the specified service.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
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
    r"""Request message for
    [DataprocMetastore.GetBackup][google.cloud.metastore.v1.DataprocMetastore.GetBackup].

    Attributes:
        name (str):
            Required. The relative resource name of the backup to
            retrieve, in the following form:

            ``projects/{project_number}/locations/{location_id}/services/{service_id}/backups/{backup_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateBackupRequest(proto.Message):
    r"""Request message for
    [DataprocMetastore.CreateBackup][google.cloud.metastore.v1.DataprocMetastore.CreateBackup].

    Attributes:
        parent (str):
            Required. The relative resource name of the service in which
            to create a backup of the following form:

            ``projects/{project_number}/locations/{location_id}/services/{service_id}``.
        backup_id (str):
            Required. The ID of the backup, which is used
            as the final component of the backup's name.

            This value must be between 1 and 64 characters
            long, begin with a letter, end with a letter or
            number, and consist of alpha-numeric ASCII
            characters or hyphens.
        backup (google.cloud.metastore_v1.types.Backup):
            Required. The backup to create. The ``name`` field is
            ignored. The ID of the created backup must be provided in
            the request's ``backup_id`` field.
        request_id (str):
            Optional. A request ID. Specify a unique request ID to allow
            the server to ignore the request if it has completed. The
            server will ignore subsequent requests that provide a
            duplicate request ID for at least 60 minutes after the first
            request.

            For example, if an initial request times out, followed by
            another request with the same request ID, the server ignores
            the second request to prevent the creation of duplicate
            commitments.

            The request ID must be a valid
            `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier#Format>`__
            A zero UUID (00000000-0000-0000-0000-000000000000) is not
            supported.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    backup_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    backup: "Backup" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Backup",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteBackupRequest(proto.Message):
    r"""Request message for
    [DataprocMetastore.DeleteBackup][google.cloud.metastore.v1.DataprocMetastore.DeleteBackup].

    Attributes:
        name (str):
            Required. The relative resource name of the backup to
            delete, in the following form:

            ``projects/{project_number}/locations/{location_id}/services/{service_id}/backups/{backup_id}``.
        request_id (str):
            Optional. A request ID. Specify a unique request ID to allow
            the server to ignore the request if it has completed. The
            server will ignore subsequent requests that provide a
            duplicate request ID for at least 60 minutes after the first
            request.

            For example, if an initial request times out, followed by
            another request with the same request ID, the server ignores
            the second request to prevent the creation of duplicate
            commitments.

            The request ID must be a valid
            `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier#Format>`__
            A zero UUID (00000000-0000-0000-0000-000000000000) is not
            supported.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ExportMetadataRequest(proto.Message):
    r"""Request message for
    [DataprocMetastore.ExportMetadata][google.cloud.metastore.v1.DataprocMetastore.ExportMetadata].


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        destination_gcs_folder (str):
            A Cloud Storage URI of a folder, in the format
            ``gs://<bucket_name>/<path_inside_bucket>``. A sub-folder
            ``<export_folder>`` containing exported files will be
            created below it.

            This field is a member of `oneof`_ ``destination``.
        service (str):
            Required. The relative resource name of the metastore
            service to run export, in the following form:

            ``projects/{project_id}/locations/{location_id}/services/{service_id}``.
        request_id (str):
            Optional. A request ID. Specify a unique request ID to allow
            the server to ignore the request if it has completed. The
            server will ignore subsequent requests that provide a
            duplicate request ID for at least 60 minutes after the first
            request.

            For example, if an initial request times out, followed by
            another request with the same request ID, the server ignores
            the second request to prevent the creation of duplicate
            commitments.

            The request ID must be a valid
            `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier#Format>`__.
            A zero UUID (00000000-0000-0000-0000-000000000000) is not
            supported.
        database_dump_type (google.cloud.metastore_v1.types.DatabaseDumpSpec.Type):
            Optional. The type of the database dump. If unspecified,
            defaults to ``MYSQL``.
    """

    destination_gcs_folder: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="destination",
    )
    service: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    database_dump_type: "DatabaseDumpSpec.Type" = proto.Field(
        proto.ENUM,
        number=4,
        enum="DatabaseDumpSpec.Type",
    )


class RestoreServiceRequest(proto.Message):
    r"""Request message for [DataprocMetastore.Restore][].

    Attributes:
        service (str):
            Required. The relative resource name of the metastore
            service to run restore, in the following form:

            ``projects/{project_id}/locations/{location_id}/services/{service_id}``.
        backup (str):
            Required. The relative resource name of the metastore
            service backup to restore from, in the following form:

            ``projects/{project_id}/locations/{location_id}/services/{service_id}/backups/{backup_id}``.
        restore_type (google.cloud.metastore_v1.types.Restore.RestoreType):
            Optional. The type of restore. If unspecified, defaults to
            ``METADATA_ONLY``.
        request_id (str):
            Optional. A request ID. Specify a unique request ID to allow
            the server to ignore the request if it has completed. The
            server will ignore subsequent requests that provide a
            duplicate request ID for at least 60 minutes after the first
            request.

            For example, if an initial request times out, followed by
            another request with the same request ID, the server ignores
            the second request to prevent the creation of duplicate
            commitments.

            The request ID must be a valid
            `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier#Format>`__.
            A zero UUID (00000000-0000-0000-0000-000000000000) is not
            supported.
    """

    service: str = proto.Field(
        proto.STRING,
        number=1,
    )
    backup: str = proto.Field(
        proto.STRING,
        number=2,
    )
    restore_type: "Restore.RestoreType" = proto.Field(
        proto.ENUM,
        number=3,
        enum="Restore.RestoreType",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
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
            Output only. Identifies whether the caller has requested
            cancellation of the operation. Operations that have
            successfully been cancelled have [Operation.error][] value
            with a [google.rpc.Status.code][google.rpc.Status.code] of
            1, corresponding to ``Code.CANCELLED``.
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


class LocationMetadata(proto.Message):
    r"""Metadata about the service in a location.

    Attributes:
        supported_hive_metastore_versions (MutableSequence[google.cloud.metastore_v1.types.LocationMetadata.HiveMetastoreVersion]):
            The versions of Hive Metastore that can be used when
            creating a new metastore service in this location. The
            server guarantees that exactly one ``HiveMetastoreVersion``
            in the list will set ``is_default``.
    """

    class HiveMetastoreVersion(proto.Message):
        r"""A specification of a supported version of the Hive Metastore
        software.

        Attributes:
            version (str):
                The semantic version of the Hive Metastore
                software.
            is_default (bool):
                Whether ``version`` will be chosen by the server if a
                metastore service is created with a ``HiveMetastoreConfig``
                that omits the ``version``.
        """

        version: str = proto.Field(
            proto.STRING,
            number=1,
        )
        is_default: bool = proto.Field(
            proto.BOOL,
            number=2,
        )

    supported_hive_metastore_versions: MutableSequence[HiveMetastoreVersion] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=HiveMetastoreVersion,
        )
    )


class DatabaseDumpSpec(proto.Message):
    r"""The specification of database dump to import from or export
    to.

    """

    class Type(proto.Enum):
        r"""The type of the database dump.

        Values:
            TYPE_UNSPECIFIED (0):
                The type of the database dump is unknown.
            MYSQL (1):
                Database dump is a MySQL dump file.
            AVRO (2):
                Database dump contains Avro files.
        """

        TYPE_UNSPECIFIED = 0
        MYSQL = 1
        AVRO = 2


class QueryMetadataRequest(proto.Message):
    r"""Request message for
    [DataprocMetastore.QueryMetadata][google.cloud.metastore.v1.DataprocMetastore.QueryMetadata].

    Attributes:
        service (str):
            Required. The relative resource name of the metastore
            service to query metadata, in the following format:

            ``projects/{project_id}/locations/{location_id}/services/{service_id}``.
        query (str):
            Required. A read-only SQL query to execute
            against the metadata database. The query cannot
            change or mutate the data.
    """

    service: str = proto.Field(
        proto.STRING,
        number=1,
    )
    query: str = proto.Field(
        proto.STRING,
        number=2,
    )


class QueryMetadataResponse(proto.Message):
    r"""Response message for
    [DataprocMetastore.QueryMetadata][google.cloud.metastore.v1.DataprocMetastore.QueryMetadata].

    Attributes:
        result_manifest_uri (str):
            The manifest URI  is link to a JSON instance
            in Cloud Storage. This instance manifests
            immediately along with QueryMetadataResponse.
            The content of the URI is not retriable until
            the long-running operation query against the
            metadata finishes.
    """

    result_manifest_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ErrorDetails(proto.Message):
    r"""Error details in public error message for
    [DataprocMetastore.QueryMetadata][google.cloud.metastore.v1.DataprocMetastore.QueryMetadata].

    Attributes:
        details (MutableMapping[str, str]):
            Additional structured details about this
            error.
            Keys define the failure items.
            Value describes the exception or details of the
            item.
    """

    details: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=1,
    )


class MoveTableToDatabaseRequest(proto.Message):
    r"""Request message for
    [DataprocMetastore.MoveTableToDatabase][google.cloud.metastore.v1.DataprocMetastore.MoveTableToDatabase].

    Attributes:
        service (str):
            Required. The relative resource name of the metastore
            service to mutate metadata, in the following format:

            ``projects/{project_id}/locations/{location_id}/services/{service_id}``.
        table_name (str):
            Required. The name of the table to be moved.
        db_name (str):
            Required. The name of the database where the
            table resides.
        destination_db_name (str):
            Required. The name of the database where the
            table should be moved.
    """

    service: str = proto.Field(
        proto.STRING,
        number=1,
    )
    table_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    db_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    destination_db_name: str = proto.Field(
        proto.STRING,
        number=4,
    )


class MoveTableToDatabaseResponse(proto.Message):
    r"""Response message for
    [DataprocMetastore.MoveTableToDatabase][google.cloud.metastore.v1.DataprocMetastore.MoveTableToDatabase].

    """


class AlterMetadataResourceLocationRequest(proto.Message):
    r"""Request message for
    [DataprocMetastore.AlterMetadataResourceLocation][google.cloud.metastore.v1.DataprocMetastore.AlterMetadataResourceLocation].

    Attributes:
        service (str):
            Required. The relative resource name of the metastore
            service to mutate metadata, in the following format:

            ``projects/{project_id}/locations/{location_id}/services/{service_id}``.
        resource_name (str):
            Required. The relative metadata resource name in the
            following format.

            ``databases/{database_id}`` or
            ``databases/{database_id}/tables/{table_id}`` or
            ``databases/{database_id}/tables/{table_id}/partitions/{partition_id}``
        location_uri (str):
            Required. The new location URI for the
            metadata resource.
    """

    service: str = proto.Field(
        proto.STRING,
        number=1,
    )
    resource_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    location_uri: str = proto.Field(
        proto.STRING,
        number=3,
    )


class AlterMetadataResourceLocationResponse(proto.Message):
    r"""Response message for
    [DataprocMetastore.AlterMetadataResourceLocation][google.cloud.metastore.v1.DataprocMetastore.AlterMetadataResourceLocation].

    """


__all__ = tuple(sorted(__protobuf__.manifest))
