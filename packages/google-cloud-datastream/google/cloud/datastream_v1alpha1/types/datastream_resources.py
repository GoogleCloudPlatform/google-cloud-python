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
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.datastream.v1alpha1",
    manifest={
        "GcsFileFormat",
        "SchemaFileFormat",
        "OracleProfile",
        "MysqlProfile",
        "GcsProfile",
        "NoConnectivitySettings",
        "StaticServiceIpConnectivity",
        "ForwardSshTunnelConnectivity",
        "VpcPeeringConfig",
        "PrivateConnection",
        "PrivateConnectivity",
        "Route",
        "MysqlSslConfig",
        "ConnectionProfile",
        "OracleColumn",
        "OracleTable",
        "OracleSchema",
        "OracleRdbms",
        "OracleSourceConfig",
        "MysqlColumn",
        "MysqlTable",
        "MysqlDatabase",
        "MysqlRdbms",
        "MysqlSourceConfig",
        "SourceConfig",
        "AvroFileFormat",
        "JsonFileFormat",
        "GcsDestinationConfig",
        "DestinationConfig",
        "Stream",
        "Error",
        "ValidationResult",
        "Validation",
        "ValidationMessage",
    },
)


class GcsFileFormat(proto.Enum):
    r"""File format in Cloud Storage.

    Values:
        GCS_FILE_FORMAT_UNSPECIFIED (0):
            Unspecified Cloud Storage file format.
        AVRO (1):
            Avro file format
    """

    _pb_options = {"deprecated": True}
    GCS_FILE_FORMAT_UNSPECIFIED = 0
    AVRO = 1


class SchemaFileFormat(proto.Enum):
    r"""Schema file format.

    Values:
        SCHEMA_FILE_FORMAT_UNSPECIFIED (0):
            Unspecified schema file format.
        NO_SCHEMA_FILE (1):
            Do not attach schema file.
        AVRO_SCHEMA_FILE (2):
            Avro schema format.
    """

    SCHEMA_FILE_FORMAT_UNSPECIFIED = 0
    NO_SCHEMA_FILE = 1
    AVRO_SCHEMA_FILE = 2


class OracleProfile(proto.Message):
    r"""Oracle database profile.

    Attributes:
        hostname (str):
            Required. Hostname for the Oracle connection.
        port (int):
            Port for the Oracle connection, default value
            is 1521.
        username (str):
            Required. Username for the Oracle connection.
        password (str):
            Required. Password for the Oracle connection.
        database_service (str):
            Required. Database for the Oracle connection.
        connection_attributes (MutableMapping[str, str]):
            Connection string attributes
    """

    hostname: str = proto.Field(
        proto.STRING,
        number=1,
    )
    port: int = proto.Field(
        proto.INT32,
        number=2,
    )
    username: str = proto.Field(
        proto.STRING,
        number=3,
    )
    password: str = proto.Field(
        proto.STRING,
        number=4,
    )
    database_service: str = proto.Field(
        proto.STRING,
        number=5,
    )
    connection_attributes: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )


class MysqlProfile(proto.Message):
    r"""MySQL database profile.

    Attributes:
        hostname (str):
            Required. Hostname for the MySQL connection.
        port (int):
            Port for the MySQL connection, default value
            is 3306.
        username (str):
            Required. Username for the MySQL connection.
        password (str):
            Required. Input only. Password for the MySQL
            connection.
        ssl_config (google.cloud.datastream_v1alpha1.types.MysqlSslConfig):
            SSL configuration for the MySQL connection.
    """

    hostname: str = proto.Field(
        proto.STRING,
        number=1,
    )
    port: int = proto.Field(
        proto.INT32,
        number=2,
    )
    username: str = proto.Field(
        proto.STRING,
        number=3,
    )
    password: str = proto.Field(
        proto.STRING,
        number=4,
    )
    ssl_config: "MysqlSslConfig" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="MysqlSslConfig",
    )


class GcsProfile(proto.Message):
    r"""Cloud Storage bucket profile.

    Attributes:
        bucket_name (str):
            Required. The full project and resource path
            for Cloud Storage bucket including the name.
        root_path (str):
            The root path inside the Cloud Storage
            bucket.
    """

    bucket_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    root_path: str = proto.Field(
        proto.STRING,
        number=2,
    )


class NoConnectivitySettings(proto.Message):
    r"""No connectivity settings."""


class StaticServiceIpConnectivity(proto.Message):
    r"""Static IP address connectivity."""


class ForwardSshTunnelConnectivity(proto.Message):
    r"""Forward SSH Tunnel connectivity.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        hostname (str):
            Required. Hostname for the SSH tunnel.
        username (str):
            Required. Username for the SSH tunnel.
        port (int):
            Port for the SSH tunnel, default value is 22.
        password (str):
            Input only. SSH password.

            This field is a member of `oneof`_ ``authentication_method``.
        private_key (str):
            Input only. SSH private key.

            This field is a member of `oneof`_ ``authentication_method``.
    """

    hostname: str = proto.Field(
        proto.STRING,
        number=1,
    )
    username: str = proto.Field(
        proto.STRING,
        number=2,
    )
    port: int = proto.Field(
        proto.INT32,
        number=3,
    )
    password: str = proto.Field(
        proto.STRING,
        number=100,
        oneof="authentication_method",
    )
    private_key: str = proto.Field(
        proto.STRING,
        number=101,
        oneof="authentication_method",
    )


class VpcPeeringConfig(proto.Message):
    r"""The VPC Peering configuration is used to create VPC peering
    between Datastream and the consumer's VPC.

    Attributes:
        vpc_name (str):
            Required. fully qualified name of the VPC
            Datastream will peer to.
        subnet (str):
            Required. A free subnet for peering. (CIDR of
            /29)
    """

    vpc_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    subnet: str = proto.Field(
        proto.STRING,
        number=2,
    )


class PrivateConnection(proto.Message):
    r"""The PrivateConnection resource is used to establish private
    connectivity between Datastream and a customer's network.

    Attributes:
        name (str):
            Output only. The resource's name.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The create time of the resource.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The update time of the resource.
        labels (MutableMapping[str, str]):
            Labels.
        display_name (str):
            Required. Display name.
        state (google.cloud.datastream_v1alpha1.types.PrivateConnection.State):
            Output only. The state of the Private
            Connection.
        error (google.cloud.datastream_v1alpha1.types.Error):
            Output only. In case of error, the details of
            the error in a user-friendly format.
        vpc_peering_config (google.cloud.datastream_v1alpha1.types.VpcPeeringConfig):
            VPC Peering Config
    """

    class State(proto.Enum):
        r"""Private Connection state.

        Values:
            STATE_UNSPECIFIED (0):
                No description available.
            CREATING (1):
                The private connection is in creation state -
                creating resources.
            CREATED (2):
                The private connection has been created with
                all of it's resources.
            FAILED (3):
                The private connection creation has failed.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        CREATED = 2
        FAILED = 3

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
    state: State = proto.Field(
        proto.ENUM,
        number=6,
        enum=State,
    )
    error: "Error" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="Error",
    )
    vpc_peering_config: "VpcPeeringConfig" = proto.Field(
        proto.MESSAGE,
        number=100,
        message="VpcPeeringConfig",
    )


class PrivateConnectivity(proto.Message):
    r"""Private Connectivity

    Attributes:
        private_connection_name (str):

    """

    private_connection_name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Route(proto.Message):
    r"""The Route resource is the child of the PrivateConnection
    resource. It used to define a route for a PrivateConnection
    setup.

    Attributes:
        name (str):
            Output only. The resource's name.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The create time of the resource.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The update time of the resource.
        labels (MutableMapping[str, str]):
            Labels.
        display_name (str):
            Required. Display name.
        destination_address (str):
            Required. Destination address for connection
        destination_port (int):
            Destination port for connection
    """

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
    destination_address: str = proto.Field(
        proto.STRING,
        number=6,
    )
    destination_port: int = proto.Field(
        proto.INT32,
        number=7,
    )


class MysqlSslConfig(proto.Message):
    r"""MySQL SSL configuration information.

    Attributes:
        client_key (str):
            Input only. PEM-encoded private key associated with the
            Client Certificate. If this field is used then the
            'client_certificate' and the 'ca_certificate' fields are
            mandatory.
        client_key_set (bool):
            Output only. Indicates whether the client_key field is set.
        client_certificate (str):
            Input only. PEM-encoded certificate that will be used by the
            replica to authenticate against the source database server.
            If this field is used then the 'client_key' and the
            'ca_certificate' fields are mandatory.
        client_certificate_set (bool):
            Output only. Indicates whether the client_certificate field
            is set.
        ca_certificate (str):
            Input only. PEM-encoded certificate of the CA
            that signed the source database server's
            certificate.
        ca_certificate_set (bool):
            Output only. Indicates whether the ca_certificate field is
            set.
    """

    client_key: str = proto.Field(
        proto.STRING,
        number=11,
    )
    client_key_set: bool = proto.Field(
        proto.BOOL,
        number=12,
    )
    client_certificate: str = proto.Field(
        proto.STRING,
        number=13,
    )
    client_certificate_set: bool = proto.Field(
        proto.BOOL,
        number=14,
    )
    ca_certificate: str = proto.Field(
        proto.STRING,
        number=15,
    )
    ca_certificate_set: bool = proto.Field(
        proto.BOOL,
        number=16,
    )


class ConnectionProfile(proto.Message):
    r"""

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. The resource's name.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The create time of the resource.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The update time of the resource.
        labels (MutableMapping[str, str]):
            Labels.
        display_name (str):
            Required. Display name.
        oracle_profile (google.cloud.datastream_v1alpha1.types.OracleProfile):
            Oracle ConnectionProfile configuration.

            This field is a member of `oneof`_ ``profile``.
        gcs_profile (google.cloud.datastream_v1alpha1.types.GcsProfile):
            Cloud Storage ConnectionProfile
            configuration.

            This field is a member of `oneof`_ ``profile``.
        mysql_profile (google.cloud.datastream_v1alpha1.types.MysqlProfile):
            MySQL ConnectionProfile configuration.

            This field is a member of `oneof`_ ``profile``.
        no_connectivity (google.cloud.datastream_v1alpha1.types.NoConnectivitySettings):
            No connectivity option chosen.

            This field is a member of `oneof`_ ``connectivity``.
        static_service_ip_connectivity (google.cloud.datastream_v1alpha1.types.StaticServiceIpConnectivity):
            Static Service IP connectivity.

            This field is a member of `oneof`_ ``connectivity``.
        forward_ssh_connectivity (google.cloud.datastream_v1alpha1.types.ForwardSshTunnelConnectivity):
            Forward SSH tunnel connectivity.

            This field is a member of `oneof`_ ``connectivity``.
        private_connectivity (google.cloud.datastream_v1alpha1.types.PrivateConnectivity):
            Private connectivity.

            This field is a member of `oneof`_ ``connectivity``.
    """

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
    oracle_profile: "OracleProfile" = proto.Field(
        proto.MESSAGE,
        number=100,
        oneof="profile",
        message="OracleProfile",
    )
    gcs_profile: "GcsProfile" = proto.Field(
        proto.MESSAGE,
        number=101,
        oneof="profile",
        message="GcsProfile",
    )
    mysql_profile: "MysqlProfile" = proto.Field(
        proto.MESSAGE,
        number=102,
        oneof="profile",
        message="MysqlProfile",
    )
    no_connectivity: "NoConnectivitySettings" = proto.Field(
        proto.MESSAGE,
        number=200,
        oneof="connectivity",
        message="NoConnectivitySettings",
    )
    static_service_ip_connectivity: "StaticServiceIpConnectivity" = proto.Field(
        proto.MESSAGE,
        number=201,
        oneof="connectivity",
        message="StaticServiceIpConnectivity",
    )
    forward_ssh_connectivity: "ForwardSshTunnelConnectivity" = proto.Field(
        proto.MESSAGE,
        number=202,
        oneof="connectivity",
        message="ForwardSshTunnelConnectivity",
    )
    private_connectivity: "PrivateConnectivity" = proto.Field(
        proto.MESSAGE,
        number=203,
        oneof="connectivity",
        message="PrivateConnectivity",
    )


class OracleColumn(proto.Message):
    r"""Oracle Column.

    Attributes:
        column_name (str):
            Column name.
        data_type (str):
            The Oracle data type.
        length (int):
            Column length.
        precision (int):
            Column precision.
        scale (int):
            Column scale.
        encoding (str):
            Column encoding.
        primary_key (bool):
            Whether or not the column represents a
            primary key.
        nullable (bool):
            Whether or not the column can accept a null
            value.
        ordinal_position (int):
            The ordinal position of the column in the
            table.
    """

    column_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    length: int = proto.Field(
        proto.INT32,
        number=3,
    )
    precision: int = proto.Field(
        proto.INT32,
        number=4,
    )
    scale: int = proto.Field(
        proto.INT32,
        number=5,
    )
    encoding: str = proto.Field(
        proto.STRING,
        number=6,
    )
    primary_key: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    nullable: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    ordinal_position: int = proto.Field(
        proto.INT32,
        number=9,
    )


class OracleTable(proto.Message):
    r"""Oracle table.

    Attributes:
        table_name (str):
            Table name.
        oracle_columns (MutableSequence[google.cloud.datastream_v1alpha1.types.OracleColumn]):
            Oracle columns in the schema.
            When unspecified as part of inclue/exclude
            lists, includes/excludes everything.
    """

    table_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    oracle_columns: MutableSequence["OracleColumn"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="OracleColumn",
    )


class OracleSchema(proto.Message):
    r"""Oracle schema.

    Attributes:
        schema_name (str):
            Schema name.
        oracle_tables (MutableSequence[google.cloud.datastream_v1alpha1.types.OracleTable]):
            Tables in the schema.
    """

    schema_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    oracle_tables: MutableSequence["OracleTable"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="OracleTable",
    )


class OracleRdbms(proto.Message):
    r"""Oracle database structure.

    Attributes:
        oracle_schemas (MutableSequence[google.cloud.datastream_v1alpha1.types.OracleSchema]):
            Oracle schemas/databases in the database
            server.
    """

    oracle_schemas: MutableSequence["OracleSchema"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="OracleSchema",
    )


class OracleSourceConfig(proto.Message):
    r"""Oracle data source configuration

    Attributes:
        allowlist (google.cloud.datastream_v1alpha1.types.OracleRdbms):
            Oracle objects to include in the stream.
        rejectlist (google.cloud.datastream_v1alpha1.types.OracleRdbms):
            Oracle objects to exclude from the stream.
    """

    allowlist: "OracleRdbms" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="OracleRdbms",
    )
    rejectlist: "OracleRdbms" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="OracleRdbms",
    )


class MysqlColumn(proto.Message):
    r"""MySQL Column.

    Attributes:
        column_name (str):
            Column name.
        data_type (str):
            The MySQL data type. Full data types list can
            be found here:
            https://dev.mysql.com/doc/refman/8.0/en/data-types.html
        length (int):
            Column length.
        collation (str):
            Column collation.
        primary_key (bool):
            Whether or not the column represents a
            primary key.
        nullable (bool):
            Whether or not the column can accept a null
            value.
        ordinal_position (int):
            The ordinal position of the column in the
            table.
    """

    column_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    length: int = proto.Field(
        proto.INT32,
        number=3,
    )
    collation: str = proto.Field(
        proto.STRING,
        number=4,
    )
    primary_key: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    nullable: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    ordinal_position: int = proto.Field(
        proto.INT32,
        number=7,
    )


class MysqlTable(proto.Message):
    r"""MySQL table.

    Attributes:
        table_name (str):
            Table name.
        mysql_columns (MutableSequence[google.cloud.datastream_v1alpha1.types.MysqlColumn]):
            MySQL columns in the database.
            When unspecified as part of include/exclude
            lists, includes/excludes everything.
    """

    table_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    mysql_columns: MutableSequence["MysqlColumn"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="MysqlColumn",
    )


class MysqlDatabase(proto.Message):
    r"""MySQL database.

    Attributes:
        database_name (str):
            Database name.
        mysql_tables (MutableSequence[google.cloud.datastream_v1alpha1.types.MysqlTable]):
            Tables in the database.
    """

    database_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    mysql_tables: MutableSequence["MysqlTable"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="MysqlTable",
    )


class MysqlRdbms(proto.Message):
    r"""MySQL database structure

    Attributes:
        mysql_databases (MutableSequence[google.cloud.datastream_v1alpha1.types.MysqlDatabase]):
            Mysql databases on the server
    """

    mysql_databases: MutableSequence["MysqlDatabase"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="MysqlDatabase",
    )


class MysqlSourceConfig(proto.Message):
    r"""MySQL source configuration

    Attributes:
        allowlist (google.cloud.datastream_v1alpha1.types.MysqlRdbms):
            MySQL objects to retrieve from the source.
        rejectlist (google.cloud.datastream_v1alpha1.types.MysqlRdbms):
            MySQL objects to exclude from the stream.
    """

    allowlist: "MysqlRdbms" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="MysqlRdbms",
    )
    rejectlist: "MysqlRdbms" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="MysqlRdbms",
    )


class SourceConfig(proto.Message):
    r"""The configuration of the stream source.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        source_connection_profile_name (str):
            Required. Source connection profile
            identifier.
        oracle_source_config (google.cloud.datastream_v1alpha1.types.OracleSourceConfig):
            Oracle data source configuration

            This field is a member of `oneof`_ ``source_stream_config``.
        mysql_source_config (google.cloud.datastream_v1alpha1.types.MysqlSourceConfig):
            MySQL data source configuration

            This field is a member of `oneof`_ ``source_stream_config``.
    """

    source_connection_profile_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    oracle_source_config: "OracleSourceConfig" = proto.Field(
        proto.MESSAGE,
        number=100,
        oneof="source_stream_config",
        message="OracleSourceConfig",
    )
    mysql_source_config: "MysqlSourceConfig" = proto.Field(
        proto.MESSAGE,
        number=101,
        oneof="source_stream_config",
        message="MysqlSourceConfig",
    )


class AvroFileFormat(proto.Message):
    r"""AVRO file format configuration."""


class JsonFileFormat(proto.Message):
    r"""JSON file format configuration.

    Attributes:
        schema_file_format (google.cloud.datastream_v1alpha1.types.SchemaFileFormat):
            The schema file format along JSON data files.
        compression (google.cloud.datastream_v1alpha1.types.JsonFileFormat.JsonCompression):
            Compression of the loaded JSON file.
    """

    class JsonCompression(proto.Enum):
        r"""Json file compression.

        Values:
            JSON_COMPRESSION_UNSPECIFIED (0):
                Unspecified json file compression.
            NO_COMPRESSION (1):
                Do not compress JSON file.
            GZIP (2):
                Gzip compression.
        """

        JSON_COMPRESSION_UNSPECIFIED = 0
        NO_COMPRESSION = 1
        GZIP = 2

    schema_file_format: "SchemaFileFormat" = proto.Field(
        proto.ENUM,
        number=1,
        enum="SchemaFileFormat",
    )
    compression: JsonCompression = proto.Field(
        proto.ENUM,
        number=2,
        enum=JsonCompression,
    )


class GcsDestinationConfig(proto.Message):
    r"""Google Cloud Storage destination configuration

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        path (str):
            Path inside the Cloud Storage bucket to write
            data to.
        gcs_file_format (google.cloud.datastream_v1alpha1.types.GcsFileFormat):
            File format that data should be written in. Deprecated field
            - use file_format instead.
        file_rotation_mb (int):
            The maximum file size to be saved in the
            bucket.
        file_rotation_interval (google.protobuf.duration_pb2.Duration):
            The maximum duration for which new events are
            added before a file is closed and a new file is
            created.
        avro_file_format (google.cloud.datastream_v1alpha1.types.AvroFileFormat):
            AVRO file format configuration.

            This field is a member of `oneof`_ ``file_format``.
        json_file_format (google.cloud.datastream_v1alpha1.types.JsonFileFormat):
            JSON file format configuration.

            This field is a member of `oneof`_ ``file_format``.
    """

    path: str = proto.Field(
        proto.STRING,
        number=1,
    )
    gcs_file_format: "GcsFileFormat" = proto.Field(
        proto.ENUM,
        number=2,
        enum="GcsFileFormat",
    )
    file_rotation_mb: int = proto.Field(
        proto.INT32,
        number=3,
    )
    file_rotation_interval: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=4,
        message=duration_pb2.Duration,
    )
    avro_file_format: "AvroFileFormat" = proto.Field(
        proto.MESSAGE,
        number=100,
        oneof="file_format",
        message="AvroFileFormat",
    )
    json_file_format: "JsonFileFormat" = proto.Field(
        proto.MESSAGE,
        number=101,
        oneof="file_format",
        message="JsonFileFormat",
    )


class DestinationConfig(proto.Message):
    r"""The configuration of the stream destination.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        destination_connection_profile_name (str):
            Required. Destination connection profile
            identifier.
        gcs_destination_config (google.cloud.datastream_v1alpha1.types.GcsDestinationConfig):

            This field is a member of `oneof`_ ``destination_stream_config``.
    """

    destination_connection_profile_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    gcs_destination_config: "GcsDestinationConfig" = proto.Field(
        proto.MESSAGE,
        number=100,
        oneof="destination_stream_config",
        message="GcsDestinationConfig",
    )


class Stream(proto.Message):
    r"""

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. The stream's name.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation time of the stream.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last update time of the
            stream.
        labels (MutableMapping[str, str]):
            Labels.
        display_name (str):
            Required. Display name.
        source_config (google.cloud.datastream_v1alpha1.types.SourceConfig):
            Required. Source connection profile
            configuration.
        destination_config (google.cloud.datastream_v1alpha1.types.DestinationConfig):
            Required. Destination connection profile
            configuration.
        state (google.cloud.datastream_v1alpha1.types.Stream.State):
            The state of the stream.
        backfill_all (google.cloud.datastream_v1alpha1.types.Stream.BackfillAllStrategy):
            Automatically backfill objects included in
            the stream source configuration. Specific
            objects can be excluded.

            This field is a member of `oneof`_ ``backfill_strategy``.
        backfill_none (google.cloud.datastream_v1alpha1.types.Stream.BackfillNoneStrategy):
            Do not automatically backfill any objects.

            This field is a member of `oneof`_ ``backfill_strategy``.
        errors (MutableSequence[google.cloud.datastream_v1alpha1.types.Error]):
            Output only. Errors on the Stream.
    """

    class State(proto.Enum):
        r"""Stream state.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified stream state.
            CREATED (1):
                The stream has been created.
            RUNNING (2):
                The stream is running.
            PAUSED (3):
                The stream is paused.
            MAINTENANCE (4):
                The stream is in maintenance mode.

                Updates are rejected on the resource in this
                state.
            FAILED (5):
                The stream is experiencing an error that is
                preventing data from being streamed.
            FAILED_PERMANENTLY (6):
                The stream has experienced a terminal
                failure.
            STARTING (7):
                The stream is starting, but not yet running.
            DRAINING (8):
                The Stream is no longer reading new events,
                but still writing events in the buffer.
        """

        STATE_UNSPECIFIED = 0
        CREATED = 1
        RUNNING = 2
        PAUSED = 3
        MAINTENANCE = 4
        FAILED = 5
        FAILED_PERMANENTLY = 6
        STARTING = 7
        DRAINING = 8

    class BackfillAllStrategy(proto.Message):
        r"""Backfill strategy to automatically backfill the Stream's
        objects. Specific objects can be excluded.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            oracle_excluded_objects (google.cloud.datastream_v1alpha1.types.OracleRdbms):
                Oracle data source objects to avoid
                backfilling.

                This field is a member of `oneof`_ ``excluded_objects``.
            mysql_excluded_objects (google.cloud.datastream_v1alpha1.types.MysqlRdbms):
                MySQL data source objects to avoid
                backfilling.

                This field is a member of `oneof`_ ``excluded_objects``.
        """

        oracle_excluded_objects: "OracleRdbms" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="excluded_objects",
            message="OracleRdbms",
        )
        mysql_excluded_objects: "MysqlRdbms" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="excluded_objects",
            message="MysqlRdbms",
        )

    class BackfillNoneStrategy(proto.Message):
        r"""Backfill strategy to disable automatic backfill for the
        Stream's objects.

        """

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
    source_config: "SourceConfig" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="SourceConfig",
    )
    destination_config: "DestinationConfig" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="DestinationConfig",
    )
    state: State = proto.Field(
        proto.ENUM,
        number=8,
        enum=State,
    )
    backfill_all: BackfillAllStrategy = proto.Field(
        proto.MESSAGE,
        number=101,
        oneof="backfill_strategy",
        message=BackfillAllStrategy,
    )
    backfill_none: BackfillNoneStrategy = proto.Field(
        proto.MESSAGE,
        number=102,
        oneof="backfill_strategy",
        message=BackfillNoneStrategy,
    )
    errors: MutableSequence["Error"] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="Error",
    )


class Error(proto.Message):
    r"""Represent a user-facing Error.

    Attributes:
        reason (str):
            A title that explains the reason for the
            error.
        error_uuid (str):
            A unique identifier for this specific error,
            allowing it to be traced throughout the system
            in logs and API responses.
        message (str):
            A message containing more information about
            the error that occurred.
        error_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the error occurred.
        details (MutableMapping[str, str]):
            Additional information about the error.
    """

    reason: str = proto.Field(
        proto.STRING,
        number=1,
    )
    error_uuid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    message: str = proto.Field(
        proto.STRING,
        number=3,
    )
    error_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    details: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )


class ValidationResult(proto.Message):
    r"""Contains the current validation results.

    Attributes:
        validations (MutableSequence[google.cloud.datastream_v1alpha1.types.Validation]):
            A list of validations (includes both executed
            as well as not executed validations).
    """

    validations: MutableSequence["Validation"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Validation",
    )


class Validation(proto.Message):
    r"""

    Attributes:
        description (str):
            A short description of the validation.
        status (google.cloud.datastream_v1alpha1.types.Validation.Status):
            Validation execution status.
        message (MutableSequence[google.cloud.datastream_v1alpha1.types.ValidationMessage]):
            Messages reflecting the validation results.
        code (str):
            A custom code identifying this validation.
    """

    class Status(proto.Enum):
        r"""Validation execution status.

        Values:
            STATUS_UNSPECIFIED (0):
                Unspecified status.
            NOT_EXECUTED (1):
                Validation did not execute.
            FAILED (2):
                Validation failed.
            PASSED (3):
                Validation passed.
        """

        STATUS_UNSPECIFIED = 0
        NOT_EXECUTED = 1
        FAILED = 2
        PASSED = 3

    description: str = proto.Field(
        proto.STRING,
        number=1,
    )
    status: Status = proto.Field(
        proto.ENUM,
        number=2,
        enum=Status,
    )
    message: MutableSequence["ValidationMessage"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="ValidationMessage",
    )
    code: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ValidationMessage(proto.Message):
    r"""Represent user-facing validation result message.

    Attributes:
        message (str):
            The result of the validation.
        level (google.cloud.datastream_v1alpha1.types.ValidationMessage.Level):
            Message severity level (warning or error).
        metadata (MutableMapping[str, str]):
            Additional metadata related to the result.
        code (str):
            A custom code identifying this specific
            message.
    """

    class Level(proto.Enum):
        r"""Validation message level.

        Values:
            LEVEL_UNSPECIFIED (0):
                Unspecified level.
            WARNING (1):
                Potentially cause issues with the Stream.
            ERROR (2):
                Definitely cause issues with the Stream.
        """

        LEVEL_UNSPECIFIED = 0
        WARNING = 1
        ERROR = 2

    message: str = proto.Field(
        proto.STRING,
        number=1,
    )
    level: Level = proto.Field(
        proto.ENUM,
        number=2,
        enum=Level,
    )
    metadata: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )
    code: str = proto.Field(
        proto.STRING,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
