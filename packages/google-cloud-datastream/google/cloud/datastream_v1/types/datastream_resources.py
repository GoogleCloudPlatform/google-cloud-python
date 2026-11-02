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
    package="google.cloud.datastream.v1",
    manifest={
        "MongodbJsonMode",
        "PartitioningTimeGranularity",
        "OracleProfile",
        "OracleAsmConfig",
        "MysqlProfile",
        "PostgresqlProfile",
        "SqlServerProfile",
        "SalesforceProfile",
        "MongodbProfile",
        "HostAddress",
        "SpannerProfile",
        "OauthClientCredentials",
        "OauthRefreshTokenCredentials",
        "UserPasswordCredentials",
        "SalesforceMarketingCloudProfile",
        "DataverseProfile",
        "ServiceNowProfile",
        "WorkdayProfile",
        "SrvConnectionFormat",
        "StandardConnectionFormat",
        "GcsProfile",
        "BigQueryProfile",
        "StaticServiceIpConnectivity",
        "ForwardSshTunnelConnectivity",
        "VpcPeeringConfig",
        "PscInterfaceConfig",
        "PrivateConnection",
        "PrivateConnectivity",
        "Route",
        "Secret",
        "MongodbSslConfig",
        "MysqlSslConfig",
        "OracleSslConfig",
        "SqlServerSslConfig",
        "PostgresqlSslConfig",
        "ConnectionProfile",
        "OracleColumn",
        "OracleTable",
        "OracleSchema",
        "OracleRdbms",
        "OracleSourceConfig",
        "PostgresqlColumn",
        "PostgresqlTable",
        "PostgresqlSchema",
        "PostgresqlRdbms",
        "PostgresqlSourceConfig",
        "SqlServerColumn",
        "SqlServerTable",
        "SqlServerSchema",
        "SqlServerRdbms",
        "SqlServerSourceConfig",
        "SqlServerTransactionLogs",
        "SqlServerChangeTables",
        "MysqlColumn",
        "MysqlTable",
        "MysqlDatabase",
        "MysqlRdbms",
        "MysqlSourceConfig",
        "SalesforceSourceConfig",
        "SalesforceOrg",
        "SalesforceObject",
        "SalesforceField",
        "MongodbSourceConfig",
        "MongodbCluster",
        "MongodbDatabase",
        "MongodbCollection",
        "MongodbField",
        "SpannerSourceConfig",
        "SpannerDatabase",
        "SpannerSchema",
        "SpannerTable",
        "SpannerColumn",
        "DataverseSourceConfig",
        "SalesforceMarketingCloudSourceConfig",
        "ServiceNowSourceConfig",
        "WorkdaySourceConfig",
        "SourceCatalog",
        "SourceObject",
        "SourceProperty",
        "SourceConfig",
        "AvroFileFormat",
        "JsonFileFormat",
        "BigQueryClustering",
        "IngestionTimePartition",
        "TimeUnitPartition",
        "IntegerRangePartition",
        "BigQueryPartitioning",
        "GcsDestinationConfig",
        "BigQueryDestinationConfig",
        "DestinationConfig",
        "Stream",
        "StreamObject",
        "SourceObjectIdentifier",
        "BackfillJob",
        "EventFilter",
        "Error",
        "ValidationResult",
        "Validation",
        "ValidationMessage",
        "CdcStrategy",
        "SqlServerLsnPosition",
        "OracleScnPosition",
        "MysqlLogPosition",
        "MysqlGtidPosition",
        "MongodbChangeStreamPosition",
        "SpannerChangeStreamPosition",
    },
)


class MongodbJsonMode(proto.Enum):
    r"""MongoDB JSON mode.

    Values:
        MONGODB_JSON_MODE_UNSPECIFIED (0):
            Unspecified JSON mode.
        STRICT (1):
            Strict JSON mode.
        CANONICAL (2):
            Canonical JSON mode.
    """

    MONGODB_JSON_MODE_UNSPECIFIED = 0
    STRICT = 1
    CANONICAL = 2


class PartitioningTimeGranularity(proto.Enum):
    r"""Partitioning granularity for time partitions.

    Values:
        PARTITIONING_TIME_GRANULARITY_UNSPECIFIED (0):
            Unspecified partitioing interval.
        PARTITIONING_TIME_GRANULARITY_HOUR (1):
            Hourly partitioning.
        PARTITIONING_TIME_GRANULARITY_DAY (2):
            Daily partitioning.
        PARTITIONING_TIME_GRANULARITY_MONTH (3):
            Monthly partitioning.
        PARTITIONING_TIME_GRANULARITY_YEAR (4):
            Yearly partitioning.
    """

    PARTITIONING_TIME_GRANULARITY_UNSPECIFIED = 0
    PARTITIONING_TIME_GRANULARITY_HOUR = 1
    PARTITIONING_TIME_GRANULARITY_DAY = 2
    PARTITIONING_TIME_GRANULARITY_MONTH = 3
    PARTITIONING_TIME_GRANULARITY_YEAR = 4


class OracleProfile(proto.Message):
    r"""Profile for connecting to an Oracle source.

    Attributes:
        hostname (str):
            Required. Hostname for the Oracle connection.
        port (int):
            Port for the Oracle connection, default value
            is 1521.
        username (str):
            Required. Username for the Oracle connection.
        password (str):
            Optional. Password for the Oracle connection. Mutually
            exclusive with the ``secret_manager_stored_password`` field.
        database_service (str):
            Required. Database for the Oracle connection.
        connection_attributes (MutableMapping[str, str]):
            Connection string attributes
        oracle_ssl_config (google.cloud.datastream_v1.types.OracleSslConfig):
            Optional. SSL configuration for the Oracle
            connection.
        oracle_asm_config (google.cloud.datastream_v1.types.OracleAsmConfig):
            Optional. Configuration for Oracle ASM
            connection.
        secret_manager_stored_password (str):
            Optional. A reference to a Secret Manager resource name
            storing the Oracle connection password. Mutually exclusive
            with the ``password`` field.
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
    oracle_ssl_config: "OracleSslConfig" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="OracleSslConfig",
    )
    oracle_asm_config: "OracleAsmConfig" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="OracleAsmConfig",
    )
    secret_manager_stored_password: str = proto.Field(
        proto.STRING,
        number=9,
    )


class OracleAsmConfig(proto.Message):
    r"""Configuration for Oracle Automatic Storage Management (ASM)
    connection.

    Attributes:
        hostname (str):
            Required. Hostname for the Oracle ASM
            connection.
        port (int):
            Required. Port for the Oracle ASM connection.
        username (str):
            Required. Username for the Oracle ASM
            connection.
        password (str):
            Optional. Password for the Oracle ASM connection. Mutually
            exclusive with the ``secret_manager_stored_password`` field.
        asm_service (str):
            Required. ASM service name for the Oracle ASM
            connection.
        connection_attributes (MutableMapping[str, str]):
            Optional. Connection string attributes
        oracle_ssl_config (google.cloud.datastream_v1.types.OracleSslConfig):
            Optional. SSL configuration for the Oracle
            connection.
        secret_manager_stored_password (str):
            Optional. A reference to a Secret Manager resource name
            storing the Oracle ASM connection password. Mutually
            exclusive with the ``password`` field.
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
    asm_service: str = proto.Field(
        proto.STRING,
        number=5,
    )
    connection_attributes: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    oracle_ssl_config: "OracleSslConfig" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="OracleSslConfig",
    )
    secret_manager_stored_password: str = proto.Field(
        proto.STRING,
        number=8,
    )


class MysqlProfile(proto.Message):
    r"""Profile for connecting to a MySQL source.

    Attributes:
        hostname (str):
            Required. Hostname for the MySQL connection.
        port (int):
            Port for the MySQL connection, default value
            is 3306.
        username (str):
            Required. Username for the MySQL connection.
        password (str):
            Optional. Input only. Password for the MySQL connection.
            Mutually exclusive with the
            ``secret_manager_stored_password`` field.
        ssl_config (google.cloud.datastream_v1.types.MysqlSslConfig):
            SSL configuration for the MySQL connection.
        secret_manager_stored_password (str):
            Optional. A reference to a Secret Manager resource name
            storing the MySQL connection password. Mutually exclusive
            with the ``password`` field.
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
    secret_manager_stored_password: str = proto.Field(
        proto.STRING,
        number=6,
    )


class PostgresqlProfile(proto.Message):
    r"""Profile for connecting to a PostgreSQL source.

    Attributes:
        hostname (str):
            Required. Hostname for the PostgreSQL
            connection.
        port (int):
            Port for the PostgreSQL connection, default
            value is 5432.
        username (str):
            Required. Username for the PostgreSQL
            connection.
        password (str):
            Optional. Password for the PostgreSQL connection. Mutually
            exclusive with the ``secret_manager_stored_password`` field.
        database (str):
            Required. Database for the PostgreSQL
            connection.
        secret_manager_stored_password (str):
            Optional. A reference to a Secret Manager resource name
            storing the PostgreSQL connection password. Mutually
            exclusive with the ``password`` field.
        ssl_config (google.cloud.datastream_v1.types.PostgresqlSslConfig):
            Optional. SSL configuration for the PostgreSQL connection.
            In case PostgresqlSslConfig is not set, the connection will
            use the default SSL mode, which is ``prefer`` (i.e. this
            mode will only use encryption if enabled from database side,
            otherwise will use unencrypted communication)
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
    database: str = proto.Field(
        proto.STRING,
        number=5,
    )
    secret_manager_stored_password: str = proto.Field(
        proto.STRING,
        number=6,
    )
    ssl_config: "PostgresqlSslConfig" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="PostgresqlSslConfig",
    )


class SqlServerProfile(proto.Message):
    r"""Profile for connecting to a SQLServer source.

    Attributes:
        hostname (str):
            Required. Hostname for the SQLServer
            connection.
        port (int):
            Port for the SQLServer connection, default
            value is 1433.
        username (str):
            Required. Username for the SQLServer
            connection.
        password (str):
            Optional. Password for the SQLServer connection. Mutually
            exclusive with the ``secret_manager_stored_password`` field.
        database (str):
            Required. Database for the SQLServer
            connection.
        ssl_config (google.cloud.datastream_v1.types.SqlServerSslConfig):
            Optional. SSL configuration for the SQLServer
            connection.
        secret_manager_stored_password (str):
            Optional. A reference to a Secret Manager resource name
            storing the SQLServer connection password. Mutually
            exclusive with the ``password`` field.
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
    database: str = proto.Field(
        proto.STRING,
        number=5,
    )
    ssl_config: "SqlServerSslConfig" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="SqlServerSslConfig",
    )
    secret_manager_stored_password: str = proto.Field(
        proto.STRING,
        number=7,
    )


class SalesforceProfile(proto.Message):
    r"""Profile for connecting to a Salesforce source.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        domain (str):
            Required. Domain endpoint for the Salesforce
            connection.
        user_credentials (google.cloud.datastream_v1.types.SalesforceProfile.UserCredentials):
            Deprecated: Salesforce is retiring Username-Password
            authentication. Use ``oauth2_client_credentials`` instead.

            This field is a member of `oneof`_ ``credentials``.
        oauth2_client_credentials (google.cloud.datastream_v1.types.SalesforceProfile.Oauth2ClientCredentials):
            Connected app authentication.

            This field is a member of `oneof`_ ``credentials``.
    """

    class UserCredentials(proto.Message):
        r"""Deprecated: Salesforce is retiring Username-Password authentication.
        Use ``Oauth2ClientCredentials`` instead.

        Attributes:
            username (str):
                Required. Username for the Salesforce
                connection.
            password (str):
                Optional. Password for the Salesforce connection. Mutually
                exclusive with the ``secret_manager_stored_password`` field.
            security_token (str):
                Optional. Security token for the Salesforce connection.
                Mutually exclusive with the
                ``secret_manager_stored_security_token`` field.
            secret_manager_stored_password (str):
                Optional. A reference to a Secret Manager resource name
                storing the Salesforce connection's password. Mutually
                exclusive with the ``password`` field.
            secret_manager_stored_security_token (str):
                Optional. A reference to a Secret Manager resource name
                storing the Salesforce connection's security token. Mutually
                exclusive with the ``security_token`` field.
        """

        username: str = proto.Field(
            proto.STRING,
            number=1,
        )
        password: str = proto.Field(
            proto.STRING,
            number=2,
        )
        security_token: str = proto.Field(
            proto.STRING,
            number=3,
        )
        secret_manager_stored_password: str = proto.Field(
            proto.STRING,
            number=4,
        )
        secret_manager_stored_security_token: str = proto.Field(
            proto.STRING,
            number=5,
        )

    class Oauth2ClientCredentials(proto.Message):
        r"""OAuth2 Client Credentials.

        Attributes:
            client_id (str):
                Required. Client ID for Salesforce OAuth2
                Client Credentials.
            client_secret (str):
                Optional. Client secret for Salesforce OAuth2 Client
                Credentials. Mutually exclusive with the
                ``secret_manager_stored_client_secret`` field.
            secret_manager_stored_client_secret (str):
                Optional. A reference to a Secret Manager resource name
                storing the Salesforce OAuth2 client_secret. Mutually
                exclusive with the ``client_secret`` field.
        """

        client_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        client_secret: str = proto.Field(
            proto.STRING,
            number=2,
        )
        secret_manager_stored_client_secret: str = proto.Field(
            proto.STRING,
            number=3,
        )

    domain: str = proto.Field(
        proto.STRING,
        number=1,
    )
    user_credentials: UserCredentials = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="credentials",
        message=UserCredentials,
    )
    oauth2_client_credentials: Oauth2ClientCredentials = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="credentials",
        message=Oauth2ClientCredentials,
    )


class MongodbProfile(proto.Message):
    r"""Profile for connecting to a MongoDB source.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        host_addresses (MutableSequence[google.cloud.datastream_v1.types.HostAddress]):
            Required. List of host addresses for a
            MongoDB cluster. For SRV connection format, this
            list must contain exactly one DNS host without a
            port. For Standard connection format, this list
            must contain all the required hosts in the
            cluster with their respective ports.
        replica_set (str):
            Optional. Name of the replica set. Only
            needed for self hosted replica set type MongoDB
            cluster. For SRV connection format, this field
            must be empty. For Standard connection format,
            this field must be specified.
        username (str):
            Required. Username for the MongoDB
            connection.
        password (str):
            Optional. Password for the MongoDB connection. Mutually
            exclusive with the ``secret_manager_stored_password`` field.
        secret_manager_stored_password (str):
            Optional. A reference to a Secret Manager resource name
            storing the SQLServer connection password. Mutually
            exclusive with the ``password`` field.
        ssl_config (google.cloud.datastream_v1.types.MongodbSslConfig):
            Optional. SSL configuration for the MongoDB
            connection.
        srv_connection_format (google.cloud.datastream_v1.types.SrvConnectionFormat):
            Srv connection format.

            This field is a member of `oneof`_ ``mongodb_connection_format``.
        standard_connection_format (google.cloud.datastream_v1.types.StandardConnectionFormat):
            Standard connection format.

            This field is a member of `oneof`_ ``mongodb_connection_format``.
        additional_options (MutableMapping[str, str]):
            Optional. Specifies additional options for the MongoDB
            connection.

            The options should be sent as key-value pairs, for example:
            ``additional_options = {"serverSelectionTimeoutMS": "10000", "directConnection": "true"}``.

            Keys are case-sensitive and should match the official
            MongoDB connection string options:
            https://www.mongodb.com/docs/manual/reference/connection-string-options/

            The server will not modify the values provided by the user.
    """

    host_addresses: MutableSequence["HostAddress"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="HostAddress",
    )
    replica_set: str = proto.Field(
        proto.STRING,
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
    secret_manager_stored_password: str = proto.Field(
        proto.STRING,
        number=5,
    )
    ssl_config: "MongodbSslConfig" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="MongodbSslConfig",
    )
    srv_connection_format: "SrvConnectionFormat" = proto.Field(
        proto.MESSAGE,
        number=101,
        oneof="mongodb_connection_format",
        message="SrvConnectionFormat",
    )
    standard_connection_format: "StandardConnectionFormat" = proto.Field(
        proto.MESSAGE,
        number=102,
        oneof="mongodb_connection_format",
        message="StandardConnectionFormat",
    )
    additional_options: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )


class HostAddress(proto.Message):
    r"""A HostAddress represents a transport end point, which is the
    combination of an IP address or hostname and a port number.

    Attributes:
        hostname (str):
            Required. Hostname for the connection.
        port (int):
            Optional. Port for the connection.
    """

    hostname: str = proto.Field(
        proto.STRING,
        number=1,
    )
    port: int = proto.Field(
        proto.INT32,
        number=2,
    )


class SpannerProfile(proto.Message):
    r"""Profile for connecting to a Spanner source.

    Attributes:
        database (str):
            Required. Immutable. Cloud Spanner database resource. This
            field is immutable. Must be in the format:
            projects/{project}/instances/{instance}/databases/{database_id}.
        host (str):
            Optional. The Spanner endpoint to connect to.
            Defaults to the global endpoint
            (https://spanner.googleapis.com). Must be in the
            format:

            https://spanner.{region}.rep.googleapis.com.
    """

    database: str = proto.Field(
        proto.STRING,
        number=1,
    )
    host: str = proto.Field(
        proto.STRING,
        number=2,
    )


class OauthClientCredentials(proto.Message):
    r"""OAuth Client Credentials.

    Attributes:
        client_id (str):
            Required. Client ID for OAuth Client
            Credentials.
        client_secret (google.cloud.datastream_v1.types.Secret):
            Required. Client secret for OAuth Client
            Credentials.
    """

    client_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    client_secret: "Secret" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Secret",
    )


class OauthRefreshTokenCredentials(proto.Message):
    r"""OAuth Refresh Token Credentials.

    Attributes:
        oauth_client_credentials (google.cloud.datastream_v1.types.OauthClientCredentials):
            Required. Specifies the OAuth Client
            Credentials.
        refresh_token (google.cloud.datastream_v1.types.Secret):
            Required. Specifies the OAuth Refresh Token.
    """

    oauth_client_credentials: "OauthClientCredentials" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="OauthClientCredentials",
    )
    refresh_token: "Secret" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Secret",
    )


class UserPasswordCredentials(proto.Message):
    r"""User-password credentials.

    Attributes:
        username (str):
            Required. Username for the connection.
        password (google.cloud.datastream_v1.types.Secret):
            Required. Password for the connection.
    """

    username: str = proto.Field(
        proto.STRING,
        number=1,
    )
    password: "Secret" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Secret",
    )


class SalesforceMarketingCloudProfile(proto.Message):
    r"""Profile for connecting to a Salesforce Marketing Cloud
    source.

    Attributes:
        subdomain (str):
            Required. Subdomain for the Salesforce Marketing Cloud
            connection. Example: if your specific endpoint is
            ``https://{your-specific-subdomain}.rest.marketingcloudapis.com/``,
            the subdomain is ``{your-specific-subdomain}``. Must be 1-63
            characters, start and end with an alphanumeric character,
            and contain only lowercase letters, numbers, and hyphens
            (-).
        oauth_client_credentials (google.cloud.datastream_v1.types.OauthClientCredentials):
            Required. Input only. Credentials for
            authenticating with the Salesforce Marketing
            Cloud API.
    """

    subdomain: str = proto.Field(
        proto.STRING,
        number=1,
    )
    oauth_client_credentials: "OauthClientCredentials" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="OauthClientCredentials",
    )


class DataverseProfile(proto.Message):
    r"""Profile for connecting to a Dataverse source.

    Attributes:
        tenant_id (str):
            Required. Tenant id of the Microsoft
            Dataverse instance.
        environment_url (str):
            Required. Environment URL of the Microsoft Dataverse
            instance. Example: ``<subdomain>.crm.dynamics.com``
        oauth_client_credentials (google.cloud.datastream_v1.types.OauthClientCredentials):
            Required. Credentials for authenticating with
            the Dataverse API.
    """

    tenant_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    environment_url: str = proto.Field(
        proto.STRING,
        number=5,
    )
    oauth_client_credentials: "OauthClientCredentials" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="OauthClientCredentials",
    )


class ServiceNowProfile(proto.Message):
    r"""Profile for connecting to a ServiceNow source.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        instance (str):
            Required. The instance of the ServiceNow account. This is
            the ``<instance>`` part of the URL
            ``https://<instance>.service-now.com``.
        user_password_credentials (google.cloud.datastream_v1.types.UserPasswordCredentials):
            User-password authentication.

            This field is a member of `oneof`_ ``credentials``.
        oauth_client_credentials (google.cloud.datastream_v1.types.OauthClientCredentials):
            Credentials for authenticating with the
            ServiceNow API.

            This field is a member of `oneof`_ ``credentials``.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    user_password_credentials: "UserPasswordCredentials" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="credentials",
        message="UserPasswordCredentials",
    )
    oauth_client_credentials: "OauthClientCredentials" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="credentials",
        message="OauthClientCredentials",
    )


class WorkdayProfile(proto.Message):
    r"""Profile for connecting to a Workday source.

    Attributes:
        host (str):
            Required. Host for the Workday connection. Must be a valid
            hostname (e.g., ``wd3-impl-services1.workday.com``).
        tenant (str):
            Required. Tenant for the Workday connection (e.g.,
            ``google12``).
        oauth_refresh_token_credentials (google.cloud.datastream_v1.types.OauthRefreshTokenCredentials):
            Required. Credentials for authenticating with
            the Workday API. OAuth Refresh Token credentials
            for authenticating with the Workday API.
    """

    host: str = proto.Field(
        proto.STRING,
        number=1,
    )
    tenant: str = proto.Field(
        proto.STRING,
        number=2,
    )
    oauth_refresh_token_credentials: "OauthRefreshTokenCredentials" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="OauthRefreshTokenCredentials",
    )


class SrvConnectionFormat(proto.Message):
    r"""Srv connection format."""


class StandardConnectionFormat(proto.Message):
    r"""Standard connection format.

    Attributes:
        direct_connection (bool):
            Optional. Deprecated: Use the ``additional_options`` map to
            specify the ``directConnection`` parameter instead. For
            example:
            ``additional_options = {"directConnection": "true"}``.
            Specifies whether the client connects directly to the
            host[:port] in the connection URI.
    """

    direct_connection: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class GcsProfile(proto.Message):
    r"""Profile for connecting to a Cloud Storage destination.

    Attributes:
        bucket (str):
            Required. The Cloud Storage bucket name.
        root_path (str):
            Optional. The root path inside the Cloud
            Storage bucket.
    """

    bucket: str = proto.Field(
        proto.STRING,
        number=1,
    )
    root_path: str = proto.Field(
        proto.STRING,
        number=2,
    )


class BigQueryProfile(proto.Message):
    r"""Profile for connecting to a BigQuery destination."""


class StaticServiceIpConnectivity(proto.Message):
    r"""Static IP address connectivity. Used when the source database
    is configured to allow incoming connections from the Datastream
    public IP addresses for the region specified in the connection
    profile.

    """


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
        vpc (str):
            Required. Fully qualified name of the VPC that Datastream
            will peer to. Format:
            ``projects/{project}/global/{networks}/{name}``
        subnet (str):
            Required. A free subnet for peering. (CIDR of
            /29)
    """

    vpc: str = proto.Field(
        proto.STRING,
        number=1,
    )
    subnet: str = proto.Field(
        proto.STRING,
        number=2,
    )


class PscInterfaceConfig(proto.Message):
    r"""The PSC Interface configuration is used to create PSC
    Interface between Datastream and the consumer's PSC.

    Attributes:
        network_attachment (str):
            Required. Fully qualified name of the Network Attachment
            that Datastream will connect to. Format:
            ``projects/{project}/regions/{region}/networkAttachments/{name}``
    """

    network_attachment: str = proto.Field(
        proto.STRING,
        number=1,
    )


class PrivateConnection(proto.Message):
    r"""The PrivateConnection resource is used to establish private
    connectivity between Datastream and a customer's network.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. Identifier. The resource's name.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The create time of the resource.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The update time of the resource.
        labels (MutableMapping[str, str]):
            Labels.
        display_name (str):
            Required. Display name.
        state (google.cloud.datastream_v1.types.PrivateConnection.State):
            Output only. The state of the Private
            Connection.
        error (google.cloud.datastream_v1.types.Error):
            Output only. In case of error, the details of
            the error in a user-friendly format.
        satisfies_pzs (bool):
            Output only. Reserved for future use.

            This field is a member of `oneof`_ ``_satisfies_pzs``.
        satisfies_pzi (bool):
            Output only. Reserved for future use.

            This field is a member of `oneof`_ ``_satisfies_pzi``.
        vpc_peering_config (google.cloud.datastream_v1.types.VpcPeeringConfig):
            VPC Peering Config.
        psc_interface_config (google.cloud.datastream_v1.types.PscInterfaceConfig):
            PSC Interface Config.
    """

    class State(proto.Enum):
        r"""Private Connection state.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified state.
            CREATING (1):
                The private connection is in creation state -
                creating resources.
            CREATED (2):
                The private connection has been created with
                all of its resources.
            FAILED (3):
                The private connection creation has failed.
            DELETING (4):
                The private connection is being deleted.
            FAILED_TO_DELETE (5):
                Delete request has failed, resource is in
                invalid state.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        CREATED = 2
        FAILED = 3
        DELETING = 4
        FAILED_TO_DELETE = 5

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
    satisfies_pzs: bool = proto.Field(
        proto.BOOL,
        number=8,
        optional=True,
    )
    satisfies_pzi: bool = proto.Field(
        proto.BOOL,
        number=9,
        optional=True,
    )
    vpc_peering_config: "VpcPeeringConfig" = proto.Field(
        proto.MESSAGE,
        number=100,
        message="VpcPeeringConfig",
    )
    psc_interface_config: "PscInterfaceConfig" = proto.Field(
        proto.MESSAGE,
        number=101,
        message="PscInterfaceConfig",
    )


class PrivateConnectivity(proto.Message):
    r"""Private Connectivity

    Attributes:
        private_connection (str):
            Required. A reference to a private connection resource.
            Format:
            ``projects/{project}/locations/{location}/privateConnections/{name}``
    """

    private_connection: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Route(proto.Message):
    r"""The route resource is the child of the private connection
    resource, used for defining a route for a private connection.

    Attributes:
        name (str):
            Output only. Identifier. The resource's name.
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


class Secret(proto.Message):
    r"""A confidential piece of information where the actual value is
    either directly specified in the message as a raw string or
    stored in GCP secret manager.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        raw_value (str):
            Optional. Input only. The actual raw value of
            the secret as plain text.

            This field is a member of `oneof`_ ``value``.
        secret_version (str):
            Optional. A Secret Manager resource name storing the actual
            value of the secret. Supported formats:

            - projects/{project}/locations/{location}/secrets/{secret}/versions/{version}
            - projects/{project}/secrets/{secret}/versions/{version}

            This field is a member of `oneof`_ ``value``.
    """

    raw_value: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="value",
    )
    secret_version: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="value",
    )


class MongodbSslConfig(proto.Message):
    r"""MongoDB SSL configuration information.

    Attributes:
        client_key (str):
            Optional. Input only. PEM-encoded private key associated
            with the Client Certificate. If this field is used then the
            'client_certificate' and the 'ca_certificate' fields are
            mandatory.
        client_key_set (bool):
            Output only. Indicates whether the client_key field is set.
        client_certificate (str):
            Optional. Input only. PEM-encoded certificate that will be
            used by the replica to authenticate against the source
            database server. If this field is used then the 'client_key'
            and the 'ca_certificate' fields are mandatory.
        client_certificate_set (bool):
            Output only. Indicates whether the client_certificate field
            is set.
        ca_certificate (str):
            Optional. Input only. PEM-encoded certificate
            of the CA that signed the source database
            server's certificate.
        ca_certificate_set (bool):
            Output only. Indicates whether the ca_certificate field is
            set.
        secret_manager_stored_client_key (str):
            Optional. Input only. A reference to a Secret Manager
            resource name storing the PEM-encoded private key associated
            with the Client Certificate. If this field is used then the
            'client_certificate' and the 'ca_certificate' fields are
            mandatory. Mutually exclusive with the ``client_key`` field.
    """

    client_key: str = proto.Field(
        proto.STRING,
        number=1,
    )
    client_key_set: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    client_certificate: str = proto.Field(
        proto.STRING,
        number=3,
    )
    client_certificate_set: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    ca_certificate: str = proto.Field(
        proto.STRING,
        number=5,
    )
    ca_certificate_set: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    secret_manager_stored_client_key: str = proto.Field(
        proto.STRING,
        number=7,
    )


class MysqlSslConfig(proto.Message):
    r"""MySQL SSL configuration information.

    Attributes:
        client_key (str):
            Optional. Input only. PEM-encoded private key associated
            with the Client Certificate. If this field is used then the
            'client_certificate' and the 'ca_certificate' fields are
            mandatory.
        client_key_set (bool):
            Output only. Indicates whether the client_key field is set.
        client_certificate (str):
            Optional. Input only. PEM-encoded certificate that will be
            used by the replica to authenticate against the source
            database server. If this field is used then the 'client_key'
            and the 'ca_certificate' fields are mandatory.
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
        number=1,
    )
    client_key_set: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    client_certificate: str = proto.Field(
        proto.STRING,
        number=3,
    )
    client_certificate_set: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    ca_certificate: str = proto.Field(
        proto.STRING,
        number=5,
    )
    ca_certificate_set: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


class OracleSslConfig(proto.Message):
    r"""Oracle SSL configuration information.

    Attributes:
        ca_certificate (str):
            Input only. PEM-encoded certificate of the CA
            that signed the source database server's
            certificate.
        ca_certificate_set (bool):
            Output only. Indicates whether the ca_certificate field has
            been set for this Connection-Profile.
        server_certificate_distinguished_name (str):
            Optional. The distinguished name (DN) mentioned in the
            server certificate. This corresponds to SSL_SERVER_CERT_DN
            sqlnet parameter. Refer
            https://docs.oracle.com/en/database/oracle/oracle-database/19/netrf/local-naming-parameters-in-tns-ora-file.html#GUID-70AB0695-A9AA-4A94-B141-4C605236EEB7
            If this field is not provided, the DN matching is not
            enforced.
    """

    ca_certificate: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ca_certificate_set: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    server_certificate_distinguished_name: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlServerSslConfig(proto.Message):
    r"""SQL Server SSL configuration information.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        encryption_not_enforced (google.cloud.datastream_v1.types.SqlServerSslConfig.EncryptionNotEnforced):
            If set, Datastream will not enforce
            encryption. If the DB server mandates
            encryption, then connection will be encrypted
            but server identity will not be authenticated.

            This field is a member of `oneof`_ ``encryption_setting``.
        basic_encryption (google.cloud.datastream_v1.types.SqlServerSslConfig.BasicEncryption):
            If set, Datastream will enforce encryption
            without authenticating server identity. Server
            certificates will be trusted by default.

            This field is a member of `oneof`_ ``encryption_setting``.
        encryption_and_server_validation (google.cloud.datastream_v1.types.SqlServerSslConfig.EncryptionAndServerValidation):
            If set, Datastream will enforce encryption
            and authenticate server identity.

            This field is a member of `oneof`_ ``encryption_setting``.
    """

    class EncryptionNotEnforced(proto.Message):
        r"""Message to represent the option where encryption is not
        enforced. An empty message right now to allow future
        extensibility.

        """

    class BasicEncryption(proto.Message):
        r"""Message to represent the option where Datastream will enforce
        encryption without authenticating server identity. Server
        certificates will be trusted by default.

        """

    class EncryptionAndServerValidation(proto.Message):
        r"""Message to represent the option where Datastream will enforce
        encryption and authenticate server identity. ca_certificate must be
        set if user selects this option.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            ca_certificate (str):
                Optional. Input only. PEM-encoded certificate
                of the CA that signed the source database
                server's certificate.
            server_certificate_hostname (str):
                Optional. The hostname mentioned in the
                Subject or SAN extension of the server
                certificate. This field is used for bypassing
                the hostname validation while verifying server
                certificate. This is required for scenarios
                where the host name that datastream connects to
                is different from the certificate's subject.
                This specifically happens for private
                connectivity. It could also happen when the
                customer provides a public IP in connection
                profile but the same is not present in the
                server certificate.

                This field is a member of `oneof`_ ``_server_certificate_hostname``.
        """

        ca_certificate: str = proto.Field(
            proto.STRING,
            number=2,
        )
        server_certificate_hostname: str = proto.Field(
            proto.STRING,
            number=3,
            optional=True,
        )

    encryption_not_enforced: EncryptionNotEnforced = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="encryption_setting",
        message=EncryptionNotEnforced,
    )
    basic_encryption: BasicEncryption = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="encryption_setting",
        message=BasicEncryption,
    )
    encryption_and_server_validation: EncryptionAndServerValidation = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="encryption_setting",
        message=EncryptionAndServerValidation,
    )


class PostgresqlSslConfig(proto.Message):
    r"""PostgreSQL SSL configuration information.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        server_verification (google.cloud.datastream_v1.types.PostgresqlSslConfig.ServerVerification):
            If this field is set, the communication will
            be encrypted with TLS  encryption and the server
            identity will be authenticated.

            This field is a member of `oneof`_ ``encryption_setting``.
        server_and_client_verification (google.cloud.datastream_v1.types.PostgresqlSslConfig.ServerAndClientVerification):
            If this field is set, the communication will
            be encrypted with TLS encryption and both the
            server identity and the client identity will be
            authenticated.

            This field is a member of `oneof`_ ``encryption_setting``.
    """

    class ServerVerification(proto.Message):
        r"""Message represents the option where Datastream will enforce the
        encryption and authenticate the server identity. ca_certificate must
        be set if user selects this option.

        Attributes:
            ca_certificate (str):
                Required. Input only. PEM-encoded server root
                CA certificate.
            server_certificate_hostname (str):
                Optional. The hostname mentioned in the
                Subject or SAN extension of the server
                certificate. If this field is not provided, the
                hostname in the server certificate is not
                validated.
        """

        ca_certificate: str = proto.Field(
            proto.STRING,
            number=1,
        )
        server_certificate_hostname: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class ServerAndClientVerification(proto.Message):
        r"""Message represents the option where Datastream will enforce the
        encryption and authenticate the server identity as well as the
        client identity. ca_certificate, client_certificate and client_key
        must be set if user selects this option.

        Attributes:
            client_certificate (str):
                Required. Input only. PEM-encoded certificate
                used by the source database to authenticate the
                client identity (i.e., the Datastream's
                identity). This certificate is signed by either
                a root certificate trusted by the server or one
                or more intermediate certificates (which is
                stored with the leaf certificate) to link the
                this certificate to the trusted root
                certificate.
            client_key (str):
                Optional. Input only. PEM-encoded private key
                associated with the client certificate. This
                value will be used during the SSL/TLS handshake,
                allowing the PostgreSQL server to authenticate
                the client's identity, i.e. identity of the
                Datastream.
            ca_certificate (str):
                Required. Input only. PEM-encoded server root
                CA certificate.
            server_certificate_hostname (str):
                Optional. The hostname mentioned in the
                Subject or SAN extension of the server
                certificate. If this field is not provided, the
                hostname in the server certificate is not
                validated.
        """

        client_certificate: str = proto.Field(
            proto.STRING,
            number=1,
        )
        client_key: str = proto.Field(
            proto.STRING,
            number=2,
        )
        ca_certificate: str = proto.Field(
            proto.STRING,
            number=3,
        )
        server_certificate_hostname: str = proto.Field(
            proto.STRING,
            number=5,
        )

    server_verification: ServerVerification = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="encryption_setting",
        message=ServerVerification,
    )
    server_and_client_verification: ServerAndClientVerification = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="encryption_setting",
        message=ServerAndClientVerification,
    )


class ConnectionProfile(proto.Message):
    r"""A set of reusable connection configurations to be used as a
    source or destination for a stream.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. Identifier. The resource's name.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The create time of the resource.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The update time of the resource.
        labels (MutableMapping[str, str]):
            Labels.
        display_name (str):
            Required. Display name.
        satisfies_pzs (bool):
            Output only. Reserved for future use.

            This field is a member of `oneof`_ ``_satisfies_pzs``.
        satisfies_pzi (bool):
            Output only. Reserved for future use.

            This field is a member of `oneof`_ ``_satisfies_pzi``.
        oracle_profile (google.cloud.datastream_v1.types.OracleProfile):
            Profile for connecting to an Oracle source.

            This field is a member of `oneof`_ ``profile``.
        gcs_profile (google.cloud.datastream_v1.types.GcsProfile):
            Profile for connecting to a Cloud Storage
            destination.

            This field is a member of `oneof`_ ``profile``.
        mysql_profile (google.cloud.datastream_v1.types.MysqlProfile):
            Profile for connecting to a MySQL source.

            This field is a member of `oneof`_ ``profile``.
        bigquery_profile (google.cloud.datastream_v1.types.BigQueryProfile):
            Profile for connecting to a BigQuery
            destination.

            This field is a member of `oneof`_ ``profile``.
        postgresql_profile (google.cloud.datastream_v1.types.PostgresqlProfile):
            Profile for connecting to a PostgreSQL
            source.

            This field is a member of `oneof`_ ``profile``.
        sql_server_profile (google.cloud.datastream_v1.types.SqlServerProfile):
            Profile for connecting to a SQLServer source.

            This field is a member of `oneof`_ ``profile``.
        salesforce_profile (google.cloud.datastream_v1.types.SalesforceProfile):
            Profile for connecting to a Salesforce
            source.

            This field is a member of `oneof`_ ``profile``.
        mongodb_profile (google.cloud.datastream_v1.types.MongodbProfile):
            Profile for connecting to a MongoDB source.

            This field is a member of `oneof`_ ``profile``.
        spanner_profile (google.cloud.datastream_v1.types.SpannerProfile):
            Profile for connecting to a Spanner source.

            This field is a member of `oneof`_ ``profile``.
        dataverse_profile (google.cloud.datastream_v1.types.DataverseProfile):
            Profile for connecting to a Dataverse source.

            This field is a member of `oneof`_ ``profile``.
        salesforce_marketing_cloud_profile (google.cloud.datastream_v1.types.SalesforceMarketingCloudProfile):
            Profile for connecting to a Salesforce
            Marketing Cloud source.

            This field is a member of `oneof`_ ``profile``.
        service_now_profile (google.cloud.datastream_v1.types.ServiceNowProfile):
            Profile for connecting to a ServiceNow
            source.

            This field is a member of `oneof`_ ``profile``.
        workday_profile (google.cloud.datastream_v1.types.WorkdayProfile):
            Optional. Profile for connecting to a Workday
            source.

            This field is a member of `oneof`_ ``profile``.
        static_service_ip_connectivity (google.cloud.datastream_v1.types.StaticServiceIpConnectivity):
            Static Service IP connectivity.

            This field is a member of `oneof`_ ``connectivity``.
        forward_ssh_connectivity (google.cloud.datastream_v1.types.ForwardSshTunnelConnectivity):
            Forward SSH tunnel connectivity.

            This field is a member of `oneof`_ ``connectivity``.
        private_connectivity (google.cloud.datastream_v1.types.PrivateConnectivity):
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
    satisfies_pzs: bool = proto.Field(
        proto.BOOL,
        number=6,
        optional=True,
    )
    satisfies_pzi: bool = proto.Field(
        proto.BOOL,
        number=7,
        optional=True,
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
    bigquery_profile: "BigQueryProfile" = proto.Field(
        proto.MESSAGE,
        number=103,
        oneof="profile",
        message="BigQueryProfile",
    )
    postgresql_profile: "PostgresqlProfile" = proto.Field(
        proto.MESSAGE,
        number=104,
        oneof="profile",
        message="PostgresqlProfile",
    )
    sql_server_profile: "SqlServerProfile" = proto.Field(
        proto.MESSAGE,
        number=105,
        oneof="profile",
        message="SqlServerProfile",
    )
    salesforce_profile: "SalesforceProfile" = proto.Field(
        proto.MESSAGE,
        number=107,
        oneof="profile",
        message="SalesforceProfile",
    )
    mongodb_profile: "MongodbProfile" = proto.Field(
        proto.MESSAGE,
        number=108,
        oneof="profile",
        message="MongodbProfile",
    )
    spanner_profile: "SpannerProfile" = proto.Field(
        proto.MESSAGE,
        number=109,
        oneof="profile",
        message="SpannerProfile",
    )
    dataverse_profile: "DataverseProfile" = proto.Field(
        proto.MESSAGE,
        number=114,
        oneof="profile",
        message="DataverseProfile",
    )
    salesforce_marketing_cloud_profile: "SalesforceMarketingCloudProfile" = proto.Field(
        proto.MESSAGE,
        number=119,
        oneof="profile",
        message="SalesforceMarketingCloudProfile",
    )
    service_now_profile: "ServiceNowProfile" = proto.Field(
        proto.MESSAGE,
        number=120,
        oneof="profile",
        message="ServiceNowProfile",
    )
    workday_profile: "WorkdayProfile" = proto.Field(
        proto.MESSAGE,
        number=121,
        oneof="profile",
        message="WorkdayProfile",
    )
    static_service_ip_connectivity: "StaticServiceIpConnectivity" = proto.Field(
        proto.MESSAGE,
        number=200,
        oneof="connectivity",
        message="StaticServiceIpConnectivity",
    )
    forward_ssh_connectivity: "ForwardSshTunnelConnectivity" = proto.Field(
        proto.MESSAGE,
        number=201,
        oneof="connectivity",
        message="ForwardSshTunnelConnectivity",
    )
    private_connectivity: "PrivateConnectivity" = proto.Field(
        proto.MESSAGE,
        number=202,
        oneof="connectivity",
        message="PrivateConnectivity",
    )


class OracleColumn(proto.Message):
    r"""Oracle Column.

    Attributes:
        column (str):
            The column name.
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

    column: str = proto.Field(
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
        table (str):
            The table name.
        oracle_columns (MutableSequence[google.cloud.datastream_v1.types.OracleColumn]):
            Oracle columns in the schema.
            When unspecified as part of include/exclude
            objects, includes/excludes everything.
    """

    table: str = proto.Field(
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
        schema (str):
            The schema name.
        oracle_tables (MutableSequence[google.cloud.datastream_v1.types.OracleTable]):
            Tables in the schema.
    """

    schema: str = proto.Field(
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
        oracle_schemas (MutableSequence[google.cloud.datastream_v1.types.OracleSchema]):
            Oracle schemas/databases in the database
            server.
    """

    oracle_schemas: MutableSequence["OracleSchema"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="OracleSchema",
    )


class OracleSourceConfig(proto.Message):
    r"""Configuration for syncing data from an Oracle source.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        include_objects (google.cloud.datastream_v1.types.OracleRdbms):
            The Oracle objects to include in the stream.
        exclude_objects (google.cloud.datastream_v1.types.OracleRdbms):
            The Oracle objects to exclude from the
            stream.
        max_concurrent_cdc_tasks (int):
            Maximum number of concurrent CDC tasks. The
            number should be non-negative. If not set (or
            set to 0), the system's default value is used.
        max_concurrent_backfill_tasks (int):
            Maximum number of concurrent backfill tasks.
            The number should be non-negative. If not set
            (or set to 0), the system's default value is
            used.
        drop_large_objects (google.cloud.datastream_v1.types.OracleSourceConfig.DropLargeObjects):
            Drop large object values.

            This field is a member of `oneof`_ ``large_objects_handling``.
        stream_large_objects (google.cloud.datastream_v1.types.OracleSourceConfig.StreamLargeObjects):
            Stream large object values.

            This field is a member of `oneof`_ ``large_objects_handling``.
        log_miner (google.cloud.datastream_v1.types.OracleSourceConfig.LogMiner):
            Use LogMiner.

            This field is a member of `oneof`_ ``cdc_method``.
        binary_log_parser (google.cloud.datastream_v1.types.OracleSourceConfig.BinaryLogParser):
            Use Binary Log Parser.

            This field is a member of `oneof`_ ``cdc_method``.
    """

    class DropLargeObjects(proto.Message):
        r"""Configuration to drop large object values."""

    class StreamLargeObjects(proto.Message):
        r"""Configuration to stream large object values."""

    class LogMiner(proto.Message):
        r"""Configuration to use LogMiner CDC method."""

    class BinaryLogParser(proto.Message):
        r"""Configuration to use Binary Log Parser CDC technique.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            oracle_asm_log_file_access (google.cloud.datastream_v1.types.OracleSourceConfig.BinaryLogParser.OracleAsmLogFileAccess):
                Use Oracle ASM.

                This field is a member of `oneof`_ ``log_file_access``.
            log_file_directories (google.cloud.datastream_v1.types.OracleSourceConfig.BinaryLogParser.LogFileDirectories):
                Use Oracle directories.

                This field is a member of `oneof`_ ``log_file_access``.
        """

        class OracleAsmLogFileAccess(proto.Message):
            r"""Configuration to use Oracle ASM to access the log files."""

        class LogFileDirectories(proto.Message):
            r"""Configuration to specify the Oracle directories to access the
            log files.

            Attributes:
                online_log_directory (str):
                    Required. Oracle directory for online logs.
                archived_log_directory (str):
                    Required. Oracle directory for archived logs.
            """

            online_log_directory: str = proto.Field(
                proto.STRING,
                number=1,
            )
            archived_log_directory: str = proto.Field(
                proto.STRING,
                number=2,
            )

        oracle_asm_log_file_access: "OracleSourceConfig.BinaryLogParser.OracleAsmLogFileAccess" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="log_file_access",
            message="OracleSourceConfig.BinaryLogParser.OracleAsmLogFileAccess",
        )
        log_file_directories: "OracleSourceConfig.BinaryLogParser.LogFileDirectories" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="log_file_access",
            message="OracleSourceConfig.BinaryLogParser.LogFileDirectories",
        )

    include_objects: "OracleRdbms" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="OracleRdbms",
    )
    exclude_objects: "OracleRdbms" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="OracleRdbms",
    )
    max_concurrent_cdc_tasks: int = proto.Field(
        proto.INT32,
        number=3,
    )
    max_concurrent_backfill_tasks: int = proto.Field(
        proto.INT32,
        number=4,
    )
    drop_large_objects: DropLargeObjects = proto.Field(
        proto.MESSAGE,
        number=100,
        oneof="large_objects_handling",
        message=DropLargeObjects,
    )
    stream_large_objects: StreamLargeObjects = proto.Field(
        proto.MESSAGE,
        number=102,
        oneof="large_objects_handling",
        message=StreamLargeObjects,
    )
    log_miner: LogMiner = proto.Field(
        proto.MESSAGE,
        number=103,
        oneof="cdc_method",
        message=LogMiner,
    )
    binary_log_parser: BinaryLogParser = proto.Field(
        proto.MESSAGE,
        number=104,
        oneof="cdc_method",
        message=BinaryLogParser,
    )


class PostgresqlColumn(proto.Message):
    r"""PostgreSQL Column.

    Attributes:
        column (str):
            The column name.
        data_type (str):
            The PostgreSQL data type.
        length (int):
            Column length.
        precision (int):
            Column precision.
        scale (int):
            Column scale.
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

    column: str = proto.Field(
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


class PostgresqlTable(proto.Message):
    r"""PostgreSQL table.

    Attributes:
        table (str):
            The table name.
        postgresql_columns (MutableSequence[google.cloud.datastream_v1.types.PostgresqlColumn]):
            PostgreSQL columns in the schema.
            When unspecified as part of include/exclude
            objects, includes/excludes everything.
    """

    table: str = proto.Field(
        proto.STRING,
        number=1,
    )
    postgresql_columns: MutableSequence["PostgresqlColumn"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="PostgresqlColumn",
    )


class PostgresqlSchema(proto.Message):
    r"""PostgreSQL schema.

    Attributes:
        schema (str):
            The schema name.
        postgresql_tables (MutableSequence[google.cloud.datastream_v1.types.PostgresqlTable]):
            Tables in the schema.
    """

    schema: str = proto.Field(
        proto.STRING,
        number=1,
    )
    postgresql_tables: MutableSequence["PostgresqlTable"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="PostgresqlTable",
    )


class PostgresqlRdbms(proto.Message):
    r"""PostgreSQL database structure.

    Attributes:
        postgresql_schemas (MutableSequence[google.cloud.datastream_v1.types.PostgresqlSchema]):
            PostgreSQL schemas in the database server.
    """

    postgresql_schemas: MutableSequence["PostgresqlSchema"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="PostgresqlSchema",
    )


class PostgresqlSourceConfig(proto.Message):
    r"""Configuration for syncing data from a PostgreSQL source.

    Attributes:
        include_objects (google.cloud.datastream_v1.types.PostgresqlRdbms):
            The PostgreSQL objects to include in the
            stream.
        exclude_objects (google.cloud.datastream_v1.types.PostgresqlRdbms):
            The PostgreSQL objects to exclude from the
            stream.
        replication_slot (str):
            Required. Immutable. The name of the logical
            replication slot that's configured with the
            pgoutput plugin.
        publication (str):
            Required. The name of the publication that includes the set
            of all tables that are defined in the stream's
            include_objects.
        max_concurrent_backfill_tasks (int):
            Maximum number of concurrent backfill tasks.
            The number should be non negative. If not set
            (or set to 0), the system's default value will
            be used.
    """

    include_objects: "PostgresqlRdbms" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="PostgresqlRdbms",
    )
    exclude_objects: "PostgresqlRdbms" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="PostgresqlRdbms",
    )
    replication_slot: str = proto.Field(
        proto.STRING,
        number=3,
    )
    publication: str = proto.Field(
        proto.STRING,
        number=4,
    )
    max_concurrent_backfill_tasks: int = proto.Field(
        proto.INT32,
        number=5,
    )


class SqlServerColumn(proto.Message):
    r"""SQLServer Column.

    Attributes:
        column (str):
            The column name.
        data_type (str):
            The SQLServer data type.
        length (int):
            Column length.
        precision (int):
            Column precision.
        scale (int):
            Column scale.
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

    column: str = proto.Field(
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
    primary_key: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    nullable: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    ordinal_position: int = proto.Field(
        proto.INT32,
        number=8,
    )


class SqlServerTable(proto.Message):
    r"""SQLServer table.

    Attributes:
        table (str):
            The table name.
        columns (MutableSequence[google.cloud.datastream_v1.types.SqlServerColumn]):
            SQLServer columns in the schema.
            When unspecified as part of include/exclude
            objects, includes/excludes everything.
    """

    table: str = proto.Field(
        proto.STRING,
        number=1,
    )
    columns: MutableSequence["SqlServerColumn"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="SqlServerColumn",
    )


class SqlServerSchema(proto.Message):
    r"""SQLServer schema.

    Attributes:
        schema (str):
            The schema name.
        tables (MutableSequence[google.cloud.datastream_v1.types.SqlServerTable]):
            Tables in the schema.
    """

    schema: str = proto.Field(
        proto.STRING,
        number=1,
    )
    tables: MutableSequence["SqlServerTable"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="SqlServerTable",
    )


class SqlServerRdbms(proto.Message):
    r"""SQLServer database structure.

    Attributes:
        schemas (MutableSequence[google.cloud.datastream_v1.types.SqlServerSchema]):
            SQLServer schemas in the database server.
    """

    schemas: MutableSequence["SqlServerSchema"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SqlServerSchema",
    )


class SqlServerSourceConfig(proto.Message):
    r"""Configuration for syncing data from a SQLServer source.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        include_objects (google.cloud.datastream_v1.types.SqlServerRdbms):
            The SQLServer objects to include in the
            stream.
        exclude_objects (google.cloud.datastream_v1.types.SqlServerRdbms):
            The SQLServer objects to exclude from the
            stream.
        max_concurrent_cdc_tasks (int):
            Max concurrent CDC tasks.
        max_concurrent_backfill_tasks (int):
            Max concurrent backfill tasks.
        transaction_logs (google.cloud.datastream_v1.types.SqlServerTransactionLogs):
            CDC reader reads from transaction logs.

            This field is a member of `oneof`_ ``cdc_method``.
        change_tables (google.cloud.datastream_v1.types.SqlServerChangeTables):
            CDC reader reads from change tables.

            This field is a member of `oneof`_ ``cdc_method``.
    """

    include_objects: "SqlServerRdbms" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="SqlServerRdbms",
    )
    exclude_objects: "SqlServerRdbms" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="SqlServerRdbms",
    )
    max_concurrent_cdc_tasks: int = proto.Field(
        proto.INT32,
        number=3,
    )
    max_concurrent_backfill_tasks: int = proto.Field(
        proto.INT32,
        number=4,
    )
    transaction_logs: "SqlServerTransactionLogs" = proto.Field(
        proto.MESSAGE,
        number=101,
        oneof="cdc_method",
        message="SqlServerTransactionLogs",
    )
    change_tables: "SqlServerChangeTables" = proto.Field(
        proto.MESSAGE,
        number=102,
        oneof="cdc_method",
        message="SqlServerChangeTables",
    )


class SqlServerTransactionLogs(proto.Message):
    r"""Configuration to use Transaction Logs CDC read method."""


class SqlServerChangeTables(proto.Message):
    r"""Configuration to use Change Tables CDC read method.

    Attributes:
        ddl_config (google.cloud.datastream_v1.types.SqlServerChangeTables.SqlServerDdlConfig):
            Optional. DDL configuration for change
            tables.
    """

    class SqlServerDdlConfig(proto.Message):
        r"""DDL configuration for change tables.

        Attributes:
            auto_create_new_capture_instance_on_ddl (bool):
                Optional. If set to true, Datastream will
                automatically create a new capture instance when
                DDL is detected on a table.The customer will be
                responsible for deleting it so that the next set
                of DDLs can be handled. The default is false and
                it means that DDL's will not be handled .
            auto_delete_old_capture_instance (bool):
                Optional. If set to true, Datastream will
                automatically delete the old capture instance
                after creating a new one to support a DDL
                change. The default is false and means that the
                customer has to delete the old capture instance
                manually.
        """

        auto_create_new_capture_instance_on_ddl: bool = proto.Field(
            proto.BOOL,
            number=1,
        )
        auto_delete_old_capture_instance: bool = proto.Field(
            proto.BOOL,
            number=2,
        )

    ddl_config: SqlServerDdlConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        message=SqlServerDdlConfig,
    )


class MysqlColumn(proto.Message):
    r"""MySQL Column.

    Attributes:
        column (str):
            The column name.
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
        precision (int):
            Column precision.
        scale (int):
            Column scale.
    """

    column: str = proto.Field(
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
    precision: int = proto.Field(
        proto.INT32,
        number=8,
    )
    scale: int = proto.Field(
        proto.INT32,
        number=9,
    )


class MysqlTable(proto.Message):
    r"""MySQL table.

    Attributes:
        table (str):
            The table name.
        mysql_columns (MutableSequence[google.cloud.datastream_v1.types.MysqlColumn]):
            MySQL columns in the database.
            When unspecified as part of include/exclude
            objects, includes/excludes everything.
    """

    table: str = proto.Field(
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
        database (str):
            The database name.
        mysql_tables (MutableSequence[google.cloud.datastream_v1.types.MysqlTable]):
            Tables in the database.
    """

    database: str = proto.Field(
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
        mysql_databases (MutableSequence[google.cloud.datastream_v1.types.MysqlDatabase]):
            Mysql databases on the server
    """

    mysql_databases: MutableSequence["MysqlDatabase"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="MysqlDatabase",
    )


class MysqlSourceConfig(proto.Message):
    r"""Configuration for syncing data from a MySQL source.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        include_objects (google.cloud.datastream_v1.types.MysqlRdbms):
            The MySQL objects to retrieve from the
            source.
        exclude_objects (google.cloud.datastream_v1.types.MysqlRdbms):
            The MySQL objects to exclude from the stream.
        max_concurrent_cdc_tasks (int):
            Maximum number of concurrent CDC tasks. The
            number should be non negative. If not set (or
            set to 0), the system's default value will be
            used.
        max_concurrent_backfill_tasks (int):
            Maximum number of concurrent backfill tasks.
            The number should be non negative. If not set
            (or set to 0), the system's default value will
            be used.
        binary_log_position (google.cloud.datastream_v1.types.MysqlSourceConfig.BinaryLogPosition):
            Use Binary log position based replication.

            This field is a member of `oneof`_ ``cdc_method``.
        gtid (google.cloud.datastream_v1.types.MysqlSourceConfig.Gtid):
            Use GTID based replication.

            This field is a member of `oneof`_ ``cdc_method``.
    """

    class BinaryLogPosition(proto.Message):
        r"""Use Binary log position based replication."""

    class Gtid(proto.Message):
        r"""Use GTID based replication."""

    include_objects: "MysqlRdbms" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="MysqlRdbms",
    )
    exclude_objects: "MysqlRdbms" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="MysqlRdbms",
    )
    max_concurrent_cdc_tasks: int = proto.Field(
        proto.INT32,
        number=3,
    )
    max_concurrent_backfill_tasks: int = proto.Field(
        proto.INT32,
        number=4,
    )
    binary_log_position: BinaryLogPosition = proto.Field(
        proto.MESSAGE,
        number=101,
        oneof="cdc_method",
        message=BinaryLogPosition,
    )
    gtid: Gtid = proto.Field(
        proto.MESSAGE,
        number=102,
        oneof="cdc_method",
        message=Gtid,
    )


class SalesforceSourceConfig(proto.Message):
    r"""Configuration for syncing data from a Salesforce source.

    Attributes:
        include_objects (google.cloud.datastream_v1.types.SalesforceOrg):
            The Salesforce objects to retrieve from the
            source.
        exclude_objects (google.cloud.datastream_v1.types.SalesforceOrg):
            The Salesforce objects to exclude from the
            stream.
        polling_interval (google.protobuf.duration_pb2.Duration):
            Required. Salesforce objects polling interval. The interval
            at which new changes will be polled for each object. The
            duration must be from ``5 minutes`` to ``24 hours``,
            inclusive.
    """

    include_objects: "SalesforceOrg" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="SalesforceOrg",
    )
    exclude_objects: "SalesforceOrg" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="SalesforceOrg",
    )
    polling_interval: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=3,
        message=duration_pb2.Duration,
    )


class SalesforceOrg(proto.Message):
    r"""Salesforce organization structure.

    Attributes:
        objects (MutableSequence[google.cloud.datastream_v1.types.SalesforceObject]):
            Salesforce objects in the database server.
    """

    objects: MutableSequence["SalesforceObject"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SalesforceObject",
    )


class SalesforceObject(proto.Message):
    r"""Salesforce object.

    Attributes:
        object_name (str):
            The object name.
        fields (MutableSequence[google.cloud.datastream_v1.types.SalesforceField]):
            Salesforce fields.
            When unspecified as part of include objects,
            includes everything, when unspecified as part of
            exclude objects, excludes nothing.
    """

    object_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    fields: MutableSequence["SalesforceField"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="SalesforceField",
    )


class SalesforceField(proto.Message):
    r"""Salesforce field.

    Attributes:
        name (str):
            The field name.
        data_type (str):
            The data type.
        nillable (bool):
            Indicates whether the field can accept nil
            values.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    nillable: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class MongodbSourceConfig(proto.Message):
    r"""Configuration for syncing data from a MongoDB source.

    Attributes:
        include_objects (google.cloud.datastream_v1.types.MongodbCluster):
            The MongoDB collections to include in the
            stream.
        exclude_objects (google.cloud.datastream_v1.types.MongodbCluster):
            The MongoDB collections to exclude from the
            stream.
        max_concurrent_backfill_tasks (int):
            Optional. Maximum number of concurrent
            backfill tasks. The number should be
            non-negative and less than or equal to 50. If
            not set (or set to 0), the system's default
            value is used
        json_mode (google.cloud.datastream_v1.types.MongodbJsonMode):
            Optional. MongoDB JSON mode to use for the
            stream.
    """

    include_objects: "MongodbCluster" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="MongodbCluster",
    )
    exclude_objects: "MongodbCluster" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="MongodbCluster",
    )
    max_concurrent_backfill_tasks: int = proto.Field(
        proto.INT32,
        number=3,
    )
    json_mode: "MongodbJsonMode" = proto.Field(
        proto.ENUM,
        number=4,
        enum="MongodbJsonMode",
    )


class MongodbCluster(proto.Message):
    r"""MongoDB Cluster structure.

    Attributes:
        databases (MutableSequence[google.cloud.datastream_v1.types.MongodbDatabase]):
            MongoDB databases in the cluster.
    """

    databases: MutableSequence["MongodbDatabase"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="MongodbDatabase",
    )


class MongodbDatabase(proto.Message):
    r"""MongoDB Database.

    Attributes:
        database (str):
            The database name.
        collections (MutableSequence[google.cloud.datastream_v1.types.MongodbCollection]):
            Collections in the database.
    """

    database: str = proto.Field(
        proto.STRING,
        number=1,
    )
    collections: MutableSequence["MongodbCollection"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="MongodbCollection",
    )


class MongodbCollection(proto.Message):
    r"""MongoDB Collection.

    Attributes:
        collection (str):
            The collection name.
        fields (MutableSequence[google.cloud.datastream_v1.types.MongodbField]):
            Fields in the collection.
    """

    collection: str = proto.Field(
        proto.STRING,
        number=1,
    )
    fields: MutableSequence["MongodbField"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="MongodbField",
    )


class MongodbField(proto.Message):
    r"""MongoDB Field.

    Attributes:
        field (str):
            The field name.
    """

    field: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SpannerSourceConfig(proto.Message):
    r"""Configuration for syncing data from a Spanner source.

    Attributes:
        change_stream_name (str):
            Required. Immutable. The change stream name
            to use for the stream.
        spanner_rpc_priority (google.cloud.datastream_v1.types.SpannerSourceConfig.SpannerRpcPriority):
            Optional. The RPC priority to use for the
            stream.
        fgac_role (str):
            Optional. The FGAC role to use for the
            stream.
        max_concurrent_cdc_tasks (int):
            Optional. Maximum number of concurrent CDC
            tasks.
        max_concurrent_backfill_tasks (int):
            Optional. Maximum number of concurrent
            backfill tasks.
        include_objects (google.cloud.datastream_v1.types.SpannerDatabase):
            Optional. The Spanner objects to retrieve
            from the data source. If some objects are both
            included and excluded, an error will be thrown.
        exclude_objects (google.cloud.datastream_v1.types.SpannerDatabase):
            Optional. The Spanner objects to avoid
            retrieving. If some objects are both included
            and excluded, an error will be thrown.
        backfill_data_boost_enabled (bool):
            Optional. Whether to use Data Boost for
            Spanner backfills. Defaults to false if not set.
    """

    class SpannerRpcPriority(proto.Enum):
        r"""The RPC priority to use for the stream.

        Values:
            SPANNER_RPC_PRIORITY_UNSPECIFIED (0):
                Unspecified RPC priority.
            LOW (1):
                Low RPC priority.
            MEDIUM (2):
                Medium RPC priority.
            HIGH (3):
                High RPC priority.
        """

        SPANNER_RPC_PRIORITY_UNSPECIFIED = 0
        LOW = 1
        MEDIUM = 2
        HIGH = 3

    change_stream_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    spanner_rpc_priority: SpannerRpcPriority = proto.Field(
        proto.ENUM,
        number=2,
        enum=SpannerRpcPriority,
    )
    fgac_role: str = proto.Field(
        proto.STRING,
        number=3,
    )
    max_concurrent_cdc_tasks: int = proto.Field(
        proto.INT32,
        number=8,
    )
    max_concurrent_backfill_tasks: int = proto.Field(
        proto.INT32,
        number=4,
    )
    include_objects: "SpannerDatabase" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="SpannerDatabase",
    )
    exclude_objects: "SpannerDatabase" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="SpannerDatabase",
    )
    backfill_data_boost_enabled: bool = proto.Field(
        proto.BOOL,
        number=9,
    )


class SpannerDatabase(proto.Message):
    r"""Spanner database structure.

    Attributes:
        schemas (MutableSequence[google.cloud.datastream_v1.types.SpannerSchema]):
            Optional. Spanner schemas in the database.
    """

    schemas: MutableSequence["SpannerSchema"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SpannerSchema",
    )


class SpannerSchema(proto.Message):
    r"""Spanner schema.

    Attributes:
        schema (str):
            Required. The schema name.
        tables (MutableSequence[google.cloud.datastream_v1.types.SpannerTable]):
            Optional. Spanner tables in the schema.
    """

    schema: str = proto.Field(
        proto.STRING,
        number=1,
    )
    tables: MutableSequence["SpannerTable"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="SpannerTable",
    )


class SpannerTable(proto.Message):
    r"""Spanner table.

    Attributes:
        table (str):
            Required. The table name.
        columns (MutableSequence[google.cloud.datastream_v1.types.SpannerColumn]):
            Optional. Spanner columns in the table.
    """

    table: str = proto.Field(
        proto.STRING,
        number=1,
    )
    columns: MutableSequence["SpannerColumn"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="SpannerColumn",
    )


class SpannerColumn(proto.Message):
    r"""Spanner column.

    Attributes:
        column (str):
            Required. The column name.
        data_type (str):
            Optional. Spanner data type.
        is_primary_key (bool):
            Optional. Whether or not the column is a
            primary key.
        ordinal_position (int):
            Optional. The ordinal position of the column
            in the table.
    """

    column: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    is_primary_key: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    ordinal_position: int = proto.Field(
        proto.INT64,
        number=4,
    )


class DataverseSourceConfig(proto.Message):
    r"""Configuration for syncing data from a Dataverse source.

    Attributes:
        include_objects (google.cloud.datastream_v1.types.SourceCatalog):
            Optional. The objects to retrieve from the
            source.
        exclude_objects (google.cloud.datastream_v1.types.SourceCatalog):
            Optional. The objects to exclude from the
            stream.
        polling_interval (google.protobuf.duration_pb2.Duration):
            Required. Incremental sync polling interval for all objects.
            If not set, a default value of ``5 minutes`` is used. The
            duration must be from ``5 minutes`` to ``24 hours``,
            inclusive.
    """

    include_objects: "SourceCatalog" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="SourceCatalog",
    )
    exclude_objects: "SourceCatalog" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="SourceCatalog",
    )
    polling_interval: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=3,
        message=duration_pb2.Duration,
    )


class SalesforceMarketingCloudSourceConfig(proto.Message):
    r"""Configuration for syncing data from a Salesforce Marketing
    Cloud source.

    Attributes:
        include_objects (google.cloud.datastream_v1.types.SourceCatalog):
            Optional. The objects to retrieve from the
            source.
        exclude_objects (google.cloud.datastream_v1.types.SourceCatalog):
            Optional. The objects to exclude from the
            stream.
        polling_interval (google.protobuf.duration_pb2.Duration):
            Required. Incremental sync polling interval for all objects.
            If not set, a default value of ``5 minutes`` is used. The
            duration must be from ``5 minutes`` to ``24 hours``,
            inclusive.
        full_refresh_polling_interval (google.protobuf.duration_pb2.Duration):
            Required. Specifies the polling interval for
            a full refresh of objects that do not support
            incremental sync. If not set, a default value of
            24 hours is used. The duration must be between 1
            and 24 hours, inclusive.
    """

    include_objects: "SourceCatalog" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="SourceCatalog",
    )
    exclude_objects: "SourceCatalog" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="SourceCatalog",
    )
    polling_interval: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=3,
        message=duration_pb2.Duration,
    )
    full_refresh_polling_interval: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=4,
        message=duration_pb2.Duration,
    )


class ServiceNowSourceConfig(proto.Message):
    r"""Configuration for syncing data from a ServiceNow source.

    Attributes:
        include_objects (google.cloud.datastream_v1.types.SourceCatalog):
            Optional. The objects to retrieve from the
            source.
        exclude_objects (google.cloud.datastream_v1.types.SourceCatalog):
            Optional. The objects to exclude from the
            stream.
        polling_interval (google.protobuf.duration_pb2.Duration):
            Required. Incremental sync polling interval for all objects.
            If not set, a default value of ``5 minutes`` is used. The
            duration must be from ``5 minutes`` to ``24 hours``,
            inclusive.
    """

    include_objects: "SourceCatalog" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="SourceCatalog",
    )
    exclude_objects: "SourceCatalog" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="SourceCatalog",
    )
    polling_interval: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=3,
        message=duration_pb2.Duration,
    )


class WorkdaySourceConfig(proto.Message):
    r"""Configuration for syncing data from a Workday source.

    Attributes:
        include_objects (google.cloud.datastream_v1.types.SourceCatalog):
            Optional. The objects to retrieve from the
            source.
        exclude_objects (google.cloud.datastream_v1.types.SourceCatalog):
            Optional. The objects to exclude from the
            stream.
        polling_interval (google.protobuf.duration_pb2.Duration):
            Required. Incremental sync polling interval for all objects.
            If not set, a default value of ``5 minutes`` is used. The
            duration must be from ``5 minutes`` to ``24 hours``,
            inclusive.
    """

    include_objects: "SourceCatalog" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="SourceCatalog",
    )
    exclude_objects: "SourceCatalog" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="SourceCatalog",
    )
    polling_interval: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=3,
        message=duration_pb2.Duration,
    )


class SourceCatalog(proto.Message):
    r"""Source catalog.

    Attributes:
        objects (MutableSequence[google.cloud.datastream_v1.types.SourceObject]):
            Optional. Source objects in the catalog.
    """

    objects: MutableSequence["SourceObject"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SourceObject",
    )


class SourceObject(proto.Message):
    r"""Source object.

    Attributes:
        object_name (str):
            Required. The object name.
        properties (MutableSequence[google.cloud.datastream_v1.types.SourceProperty]):
            Optional. Source properties. When unspecified
            as part of include objects, includes everything,
            when unspecified as part of exclude objects,
            excludes nothing.
    """

    object_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    properties: MutableSequence["SourceProperty"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="SourceProperty",
    )


class SourceProperty(proto.Message):
    r"""Source property.

    Attributes:
        property_name (str):
            Required. The property name.
        properties (MutableSequence[google.cloud.datastream_v1.types.SourceProperty]):
            Optional. Source properties. When specified,
            it means that the current property contains
            nested properties of its own. When unspecified
            as part of include objects, includes everything,
            when unspecified as part of exclude objects,
            excludes nothing.
        primary_key (bool):
            Optional. Whether or not the property is a
            primary key.
    """

    property_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    properties: MutableSequence["SourceProperty"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="SourceProperty",
    )
    primary_key: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class SourceConfig(proto.Message):
    r"""The configuration of the stream source.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        source_connection_profile (str):
            Required. Source connection profile resource. Format:
            ``projects/{project}/locations/{location}/connectionProfiles/{name}``
        oracle_source_config (google.cloud.datastream_v1.types.OracleSourceConfig):
            Oracle data source configuration.

            This field is a member of `oneof`_ ``source_stream_config``.
        mysql_source_config (google.cloud.datastream_v1.types.MysqlSourceConfig):
            MySQL data source configuration.

            This field is a member of `oneof`_ ``source_stream_config``.
        postgresql_source_config (google.cloud.datastream_v1.types.PostgresqlSourceConfig):
            PostgreSQL data source configuration.

            This field is a member of `oneof`_ ``source_stream_config``.
        sql_server_source_config (google.cloud.datastream_v1.types.SqlServerSourceConfig):
            SQLServer data source configuration.

            This field is a member of `oneof`_ ``source_stream_config``.
        salesforce_source_config (google.cloud.datastream_v1.types.SalesforceSourceConfig):
            Salesforce data source configuration.

            This field is a member of `oneof`_ ``source_stream_config``.
        mongodb_source_config (google.cloud.datastream_v1.types.MongodbSourceConfig):
            MongoDB data source configuration.

            This field is a member of `oneof`_ ``source_stream_config``.
        spanner_source_config (google.cloud.datastream_v1.types.SpannerSourceConfig):
            Spanner data source configuration.

            This field is a member of `oneof`_ ``source_stream_config``.
        dataverse_source_config (google.cloud.datastream_v1.types.DataverseSourceConfig):
            Dataverse data source configuration.

            This field is a member of `oneof`_ ``source_stream_config``.
        salesforce_marketing_cloud_source_config (google.cloud.datastream_v1.types.SalesforceMarketingCloudSourceConfig):
            Salesforce Marketing Cloud data source
            configuration.

            This field is a member of `oneof`_ ``source_stream_config``.
        service_now_source_config (google.cloud.datastream_v1.types.ServiceNowSourceConfig):
            ServiceNow data source configuration.

            This field is a member of `oneof`_ ``source_stream_config``.
        workday_source_config (google.cloud.datastream_v1.types.WorkdaySourceConfig):
            Optional. Workday data source configuration.

            This field is a member of `oneof`_ ``source_stream_config``.
    """

    source_connection_profile: str = proto.Field(
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
    postgresql_source_config: "PostgresqlSourceConfig" = proto.Field(
        proto.MESSAGE,
        number=102,
        oneof="source_stream_config",
        message="PostgresqlSourceConfig",
    )
    sql_server_source_config: "SqlServerSourceConfig" = proto.Field(
        proto.MESSAGE,
        number=103,
        oneof="source_stream_config",
        message="SqlServerSourceConfig",
    )
    salesforce_source_config: "SalesforceSourceConfig" = proto.Field(
        proto.MESSAGE,
        number=104,
        oneof="source_stream_config",
        message="SalesforceSourceConfig",
    )
    mongodb_source_config: "MongodbSourceConfig" = proto.Field(
        proto.MESSAGE,
        number=105,
        oneof="source_stream_config",
        message="MongodbSourceConfig",
    )
    spanner_source_config: "SpannerSourceConfig" = proto.Field(
        proto.MESSAGE,
        number=106,
        oneof="source_stream_config",
        message="SpannerSourceConfig",
    )
    dataverse_source_config: "DataverseSourceConfig" = proto.Field(
        proto.MESSAGE,
        number=111,
        oneof="source_stream_config",
        message="DataverseSourceConfig",
    )
    salesforce_marketing_cloud_source_config: "SalesforceMarketingCloudSourceConfig" = (
        proto.Field(
            proto.MESSAGE,
            number=116,
            oneof="source_stream_config",
            message="SalesforceMarketingCloudSourceConfig",
        )
    )
    service_now_source_config: "ServiceNowSourceConfig" = proto.Field(
        proto.MESSAGE,
        number=117,
        oneof="source_stream_config",
        message="ServiceNowSourceConfig",
    )
    workday_source_config: "WorkdaySourceConfig" = proto.Field(
        proto.MESSAGE,
        number=118,
        oneof="source_stream_config",
        message="WorkdaySourceConfig",
    )


class AvroFileFormat(proto.Message):
    r"""AVRO file format configuration."""


class JsonFileFormat(proto.Message):
    r"""JSON file format configuration.

    Attributes:
        schema_file_format (google.cloud.datastream_v1.types.JsonFileFormat.SchemaFileFormat):
            The schema file format along JSON data files.
        compression (google.cloud.datastream_v1.types.JsonFileFormat.JsonCompression):
            Compression of the loaded JSON file.
    """

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

    schema_file_format: SchemaFileFormat = proto.Field(
        proto.ENUM,
        number=1,
        enum=SchemaFileFormat,
    )
    compression: JsonCompression = proto.Field(
        proto.ENUM,
        number=2,
        enum=JsonCompression,
    )


class BigQueryClustering(proto.Message):
    r"""BigQuery clustering configuration.

    Attributes:
        columns (MutableSequence[str]):
            Required. Column names to set as clustering
            columns.
    """

    columns: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class IngestionTimePartition(proto.Message):
    r"""Ingestion time partitioning. see
    https://cloud.google.com/bigquery/docs/partitioned-tables#ingestion_time

    Attributes:
        partitioning_time_granularity (google.cloud.datastream_v1.types.PartitioningTimeGranularity):
            Optional. Partition granularity
    """

    partitioning_time_granularity: "PartitioningTimeGranularity" = proto.Field(
        proto.ENUM,
        number=1,
        enum="PartitioningTimeGranularity",
    )


class TimeUnitPartition(proto.Message):
    r"""Time unit column partitioning. see
    https://cloud.google.com/bigquery/docs/partitioned-tables#date_timestamp_partitioned_tables

    Attributes:
        column (str):
            Required. The partitioning column.
        partitioning_time_granularity (google.cloud.datastream_v1.types.PartitioningTimeGranularity):
            Optional. Partition granularity.
    """

    column: str = proto.Field(
        proto.STRING,
        number=1,
    )
    partitioning_time_granularity: "PartitioningTimeGranularity" = proto.Field(
        proto.ENUM,
        number=2,
        enum="PartitioningTimeGranularity",
    )


class IntegerRangePartition(proto.Message):
    r"""Integer range partitioning. see
    https://cloud.google.com/bigquery/docs/partitioned-tables#integer_range

    Attributes:
        column (str):
            Required. The partitioning column.
        start (int):
            Required. The starting value for range
            partitioning (inclusive).
        end (int):
            Required. The ending value for range
            partitioning (exclusive).
        interval (int):
            Required. The interval of each range within
            the partition.
    """

    column: str = proto.Field(
        proto.STRING,
        number=1,
    )
    start: int = proto.Field(
        proto.INT64,
        number=2,
    )
    end: int = proto.Field(
        proto.INT64,
        number=3,
    )
    interval: int = proto.Field(
        proto.INT64,
        number=4,
    )


class BigQueryPartitioning(proto.Message):
    r"""BigQuery partitioning configuration.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        integer_range_partition (google.cloud.datastream_v1.types.IntegerRangePartition):
            Integer range partitioning.

            This field is a member of `oneof`_ ``partitioning``.
        time_unit_partition (google.cloud.datastream_v1.types.TimeUnitPartition):
            Time unit column partitioning.

            This field is a member of `oneof`_ ``partitioning``.
        ingestion_time_partition (google.cloud.datastream_v1.types.IngestionTimePartition):
            Ingestion time partitioning.

            This field is a member of `oneof`_ ``partitioning``.
        require_partition_filter (bool):
            Optional. If true, queries over the table
            require a partition filter.
    """

    integer_range_partition: "IntegerRangePartition" = proto.Field(
        proto.MESSAGE,
        number=100,
        oneof="partitioning",
        message="IntegerRangePartition",
    )
    time_unit_partition: "TimeUnitPartition" = proto.Field(
        proto.MESSAGE,
        number=101,
        oneof="partitioning",
        message="TimeUnitPartition",
    )
    ingestion_time_partition: "IngestionTimePartition" = proto.Field(
        proto.MESSAGE,
        number=102,
        oneof="partitioning",
        message="IngestionTimePartition",
    )
    require_partition_filter: bool = proto.Field(
        proto.BOOL,
        number=103,
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
        file_rotation_mb (int):
            The maximum file size to be saved in the
            bucket.
        file_rotation_interval (google.protobuf.duration_pb2.Duration):
            The maximum duration for which new events are
            added before a file is closed and a new file is
            created. Values within the range of 15-60
            seconds are allowed.
        avro_file_format (google.cloud.datastream_v1.types.AvroFileFormat):
            AVRO file format configuration.

            This field is a member of `oneof`_ ``file_format``.
        json_file_format (google.cloud.datastream_v1.types.JsonFileFormat):
            JSON file format configuration.

            This field is a member of `oneof`_ ``file_format``.
    """

    path: str = proto.Field(
        proto.STRING,
        number=1,
    )
    file_rotation_mb: int = proto.Field(
        proto.INT32,
        number=2,
    )
    file_rotation_interval: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=3,
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


class BigQueryDestinationConfig(proto.Message):
    r"""BigQuery destination configuration

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        single_target_dataset (google.cloud.datastream_v1.types.BigQueryDestinationConfig.SingleTargetDataset):
            Single destination dataset.

            This field is a member of `oneof`_ ``dataset_config``.
        source_hierarchy_datasets (google.cloud.datastream_v1.types.BigQueryDestinationConfig.SourceHierarchyDatasets):
            Source hierarchy datasets.

            This field is a member of `oneof`_ ``dataset_config``.
        data_freshness (google.protobuf.duration_pb2.Duration):
            The guaranteed data freshness (in seconds)
            when querying tables created by the stream.
            Editing this field will only affect new tables
            created in the future, but existing tables will
            not be impacted. Lower values mean that queries
            will return fresher data, but may result in
            higher cost.
        blmt_config (google.cloud.datastream_v1.types.BigQueryDestinationConfig.BlmtConfig):
            Optional. Big Lake Managed Tables (BLMT)
            configuration.
        merge (google.cloud.datastream_v1.types.BigQueryDestinationConfig.Merge):
            The standard mode

            This field is a member of `oneof`_ ``write_mode``.
        append_only (google.cloud.datastream_v1.types.BigQueryDestinationConfig.AppendOnly):
            Append only mode

            This field is a member of `oneof`_ ``write_mode``.
    """

    class SingleTargetDataset(proto.Message):
        r"""A single target dataset to which all data will be streamed.

        Attributes:
            dataset_id (str):
                The dataset ID of the target dataset.
                DatasetIds allowed characters:

                https://cloud.google.com/bigquery/docs/reference/rest/v2/datasets#datasetreference.
        """

        dataset_id: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class SourceHierarchyDatasets(proto.Message):
        r"""Destination datasets are created so that hierarchy of the
        destination data objects matches the source hierarchy.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            dataset_template (google.cloud.datastream_v1.types.BigQueryDestinationConfig.SourceHierarchyDatasets.DatasetTemplate):
                The dataset template to use for dynamic
                dataset creation.
            project_id (str):
                Optional. The project id of the BigQuery
                dataset. If not specified, the project will be
                inferred from the stream resource.

                This field is a member of `oneof`_ ``_project_id``.
        """

        class DatasetTemplate(proto.Message):
            r"""Dataset template used for dynamic dataset creation.

            Attributes:
                location (str):
                    Required. The geographic location where the
                    dataset should reside. See
                    https://cloud.google.com/bigquery/docs/locations
                    for supported locations.
                dataset_id_prefix (str):
                    If supplied, every created dataset will have its name
                    prefixed by the provided value. The prefix and name will be
                    separated by an underscore. i.e. \_<dataset_name>.
                kms_key_name (str):
                    Describes the Cloud KMS encryption key that will be used to
                    protect destination BigQuery table. The BigQuery Service
                    Account associated with your project requires access to this
                    encryption key. i.e.
                    projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{cryptoKey}.
                    See
                    https://cloud.google.com/bigquery/docs/customer-managed-encryption
                    for more information.
            """

            location: str = proto.Field(
                proto.STRING,
                number=1,
            )
            dataset_id_prefix: str = proto.Field(
                proto.STRING,
                number=2,
            )
            kms_key_name: str = proto.Field(
                proto.STRING,
                number=3,
            )

        dataset_template: "BigQueryDestinationConfig.SourceHierarchyDatasets.DatasetTemplate" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="BigQueryDestinationConfig.SourceHierarchyDatasets.DatasetTemplate",
        )
        project_id: str = proto.Field(
            proto.STRING,
            number=3,
            optional=True,
        )

    class BlmtConfig(proto.Message):
        r"""The configuration for BLMT.

        Attributes:
            bucket (str):
                Required. The Cloud Storage bucket name.
            root_path (str):
                The root path inside the Cloud Storage
                bucket.
            connection_name (str):
                Required. The bigquery connection. Format:
                ``{project}.{location}.{name}``
            file_format (google.cloud.datastream_v1.types.BigQueryDestinationConfig.BlmtConfig.FileFormat):
                Required. The file format.
            table_format (google.cloud.datastream_v1.types.BigQueryDestinationConfig.BlmtConfig.TableFormat):
                Required. The table format.
        """

        class FileFormat(proto.Enum):
            r"""Supported file formats for BigLake managed tables.

            Values:
                FILE_FORMAT_UNSPECIFIED (0):
                    Default value.
                PARQUET (1):
                    Parquet file format.
            """

            FILE_FORMAT_UNSPECIFIED = 0
            PARQUET = 1

        class TableFormat(proto.Enum):
            r"""Supported table formats for BigLake managed tables.

            Values:
                TABLE_FORMAT_UNSPECIFIED (0):
                    Default value.
                ICEBERG (1):
                    Iceberg table format.
            """

            TABLE_FORMAT_UNSPECIFIED = 0
            ICEBERG = 1

        bucket: str = proto.Field(
            proto.STRING,
            number=1,
        )
        root_path: str = proto.Field(
            proto.STRING,
            number=2,
        )
        connection_name: str = proto.Field(
            proto.STRING,
            number=3,
        )
        file_format: "BigQueryDestinationConfig.BlmtConfig.FileFormat" = proto.Field(
            proto.ENUM,
            number=4,
            enum="BigQueryDestinationConfig.BlmtConfig.FileFormat",
        )
        table_format: "BigQueryDestinationConfig.BlmtConfig.TableFormat" = proto.Field(
            proto.ENUM,
            number=5,
            enum="BigQueryDestinationConfig.BlmtConfig.TableFormat",
        )

    class AppendOnly(proto.Message):
        r"""AppendOnly mode defines that all changes to a table will be
        written to the destination table.

        """

    class Merge(proto.Message):
        r"""Merge mode defines that all changes to a table will be merged
        at the destination table.

        """

    single_target_dataset: SingleTargetDataset = proto.Field(
        proto.MESSAGE,
        number=201,
        oneof="dataset_config",
        message=SingleTargetDataset,
    )
    source_hierarchy_datasets: SourceHierarchyDatasets = proto.Field(
        proto.MESSAGE,
        number=202,
        oneof="dataset_config",
        message=SourceHierarchyDatasets,
    )
    data_freshness: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=300,
        message=duration_pb2.Duration,
    )
    blmt_config: BlmtConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        message=BlmtConfig,
    )
    merge: Merge = proto.Field(
        proto.MESSAGE,
        number=301,
        oneof="write_mode",
        message=Merge,
    )
    append_only: AppendOnly = proto.Field(
        proto.MESSAGE,
        number=302,
        oneof="write_mode",
        message=AppendOnly,
    )


class DestinationConfig(proto.Message):
    r"""The configuration of the stream destination.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        destination_connection_profile (str):
            Required. Destination connection profile resource. Format:
            ``projects/{project}/locations/{location}/connectionProfiles/{name}``
        gcs_destination_config (google.cloud.datastream_v1.types.GcsDestinationConfig):
            A configuration for how data should be loaded
            to Cloud Storage.

            This field is a member of `oneof`_ ``destination_stream_config``.
        bigquery_destination_config (google.cloud.datastream_v1.types.BigQueryDestinationConfig):
            BigQuery destination configuration.

            This field is a member of `oneof`_ ``destination_stream_config``.
    """

    destination_connection_profile: str = proto.Field(
        proto.STRING,
        number=1,
    )
    gcs_destination_config: "GcsDestinationConfig" = proto.Field(
        proto.MESSAGE,
        number=100,
        oneof="destination_stream_config",
        message="GcsDestinationConfig",
    )
    bigquery_destination_config: "BigQueryDestinationConfig" = proto.Field(
        proto.MESSAGE,
        number=101,
        oneof="destination_stream_config",
        message="BigQueryDestinationConfig",
    )


class Stream(proto.Message):
    r"""A resource representing streaming data from a source to a
    destination.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. Identifier. The stream's name.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation time of the stream.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last update time of the
            stream.
        labels (MutableMapping[str, str]):
            Labels.
        display_name (str):
            Required. Display name.
        source_config (google.cloud.datastream_v1.types.SourceConfig):
            Required. Source connection profile
            configuration.
        destination_config (google.cloud.datastream_v1.types.DestinationConfig):
            Required. Destination connection profile
            configuration.
        state (google.cloud.datastream_v1.types.Stream.State):
            The state of the stream.
        backfill_all (google.cloud.datastream_v1.types.Stream.BackfillAllStrategy):
            Automatically backfill objects included in
            the stream source configuration. Specific
            objects can be excluded.

            This field is a member of `oneof`_ ``backfill_strategy``.
        backfill_none (google.cloud.datastream_v1.types.Stream.BackfillNoneStrategy):
            Do not automatically backfill any objects.

            This field is a member of `oneof`_ ``backfill_strategy``.
        errors (MutableSequence[google.cloud.datastream_v1.types.Error]):
            Output only. Errors on the Stream.
        customer_managed_encryption_key (str):
            Immutable. A reference to a KMS encryption
            key. If provided, it will be used to encrypt the
            data. If left blank, data will be encrypted
            using an internal Stream-specific encryption key
            provisioned through KMS.

            This field is a member of `oneof`_ ``_customer_managed_encryption_key``.
        last_recovery_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. If the stream was recovered, the
            time of the last recovery. Note: This field is
            currently experimental.
        satisfies_pzs (bool):
            Output only. Reserved for future use.

            This field is a member of `oneof`_ ``_satisfies_pzs``.
        satisfies_pzi (bool):
            Output only. Reserved for future use.

            This field is a member of `oneof`_ ``_satisfies_pzi``.
        rule_sets (MutableSequence[google.cloud.datastream_v1.types.Stream.RuleSet]):
            Optional. Rule sets to apply to the stream.
    """

    class State(proto.Enum):
        r"""Stream state.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified stream state.
            NOT_STARTED (1):
                The stream has been created but has not yet
                started streaming data.
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
        NOT_STARTED = 1
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
            oracle_excluded_objects (google.cloud.datastream_v1.types.OracleRdbms):
                Oracle data source objects to avoid
                backfilling.

                This field is a member of `oneof`_ ``excluded_objects``.
            mysql_excluded_objects (google.cloud.datastream_v1.types.MysqlRdbms):
                MySQL data source objects to avoid
                backfilling.

                This field is a member of `oneof`_ ``excluded_objects``.
            postgresql_excluded_objects (google.cloud.datastream_v1.types.PostgresqlRdbms):
                PostgreSQL data source objects to avoid
                backfilling.

                This field is a member of `oneof`_ ``excluded_objects``.
            sql_server_excluded_objects (google.cloud.datastream_v1.types.SqlServerRdbms):
                SQLServer data source objects to avoid
                backfilling

                This field is a member of `oneof`_ ``excluded_objects``.
            salesforce_excluded_objects (google.cloud.datastream_v1.types.SalesforceOrg):
                Salesforce data source objects to avoid
                backfilling

                This field is a member of `oneof`_ ``excluded_objects``.
            mongodb_excluded_objects (google.cloud.datastream_v1.types.MongodbCluster):
                MongoDB data source objects to avoid
                backfilling

                This field is a member of `oneof`_ ``excluded_objects``.
            spanner_excluded_objects (google.cloud.datastream_v1.types.SpannerDatabase):
                Spanner data source objects to avoid
                backfilling.

                This field is a member of `oneof`_ ``excluded_objects``.
            saas_excluded_objects (google.cloud.datastream_v1.types.SourceCatalog):
                Source catalog data source objects to avoid
                backfilling. This is mainly used to represent
                SaaS applications objects.

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
        postgresql_excluded_objects: "PostgresqlRdbms" = proto.Field(
            proto.MESSAGE,
            number=3,
            oneof="excluded_objects",
            message="PostgresqlRdbms",
        )
        sql_server_excluded_objects: "SqlServerRdbms" = proto.Field(
            proto.MESSAGE,
            number=4,
            oneof="excluded_objects",
            message="SqlServerRdbms",
        )
        salesforce_excluded_objects: "SalesforceOrg" = proto.Field(
            proto.MESSAGE,
            number=5,
            oneof="excluded_objects",
            message="SalesforceOrg",
        )
        mongodb_excluded_objects: "MongodbCluster" = proto.Field(
            proto.MESSAGE,
            number=6,
            oneof="excluded_objects",
            message="MongodbCluster",
        )
        spanner_excluded_objects: "SpannerDatabase" = proto.Field(
            proto.MESSAGE,
            number=7,
            oneof="excluded_objects",
            message="SpannerDatabase",
        )
        saas_excluded_objects: "SourceCatalog" = proto.Field(
            proto.MESSAGE,
            number=9,
            oneof="excluded_objects",
            message="SourceCatalog",
        )

    class BackfillNoneStrategy(proto.Message):
        r"""Backfill strategy to disable automatic backfill for the
        Stream's objects.

        """

    class RuleSet(proto.Message):
        r"""A set of rules to apply to a set of objects.

        Attributes:
            customization_rules (MutableSequence[google.cloud.datastream_v1.types.Stream.RuleSet.CustomizationRule]):
                Required. List of customization rules to
                apply.
            object_filter (google.cloud.datastream_v1.types.Stream.RuleSet.ObjectFilter):
                Required. Object filter to apply the
                customization rules to.
        """

        class ObjectFilter(proto.Message):
            r"""Object filter to apply the rules to.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                source_object_identifier (google.cloud.datastream_v1.types.SourceObjectIdentifier):
                    Specific source object identifier.

                    This field is a member of `oneof`_ ``filter_type``.
            """

            source_object_identifier: "SourceObjectIdentifier" = proto.Field(
                proto.MESSAGE,
                number=1,
                oneof="filter_type",
                message="SourceObjectIdentifier",
            )

        class CustomizationRule(proto.Message):
            r"""A customization rule to apply to a set of objects.

            This message has `oneof`_ fields (mutually exclusive fields).
            For each oneof, at most one member field can be set at the same time.
            Setting any member of the oneof automatically clears all other
            members.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                bigquery_partitioning (google.cloud.datastream_v1.types.BigQueryPartitioning):
                    BigQuery partitioning rule.

                    This field is a member of `oneof`_ ``rule``.
                bigquery_clustering (google.cloud.datastream_v1.types.BigQueryClustering):
                    BigQuery clustering rule.

                    This field is a member of `oneof`_ ``rule``.
            """

            bigquery_partitioning: "BigQueryPartitioning" = proto.Field(
                proto.MESSAGE,
                number=1,
                oneof="rule",
                message="BigQueryPartitioning",
            )
            bigquery_clustering: "BigQueryClustering" = proto.Field(
                proto.MESSAGE,
                number=2,
                oneof="rule",
                message="BigQueryClustering",
            )

        customization_rules: MutableSequence["Stream.RuleSet.CustomizationRule"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message="Stream.RuleSet.CustomizationRule",
            )
        )
        object_filter: "Stream.RuleSet.ObjectFilter" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="Stream.RuleSet.ObjectFilter",
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
    customer_managed_encryption_key: str = proto.Field(
        proto.STRING,
        number=10,
        optional=True,
    )
    last_recovery_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=13,
        message=timestamp_pb2.Timestamp,
    )
    satisfies_pzs: bool = proto.Field(
        proto.BOOL,
        number=15,
        optional=True,
    )
    satisfies_pzi: bool = proto.Field(
        proto.BOOL,
        number=16,
        optional=True,
    )
    rule_sets: MutableSequence[RuleSet] = proto.RepeatedField(
        proto.MESSAGE,
        number=19,
        message=RuleSet,
    )


class StreamObject(proto.Message):
    r"""A specific stream object (e.g a specific DB table).

    Attributes:
        name (str):
            Output only. Identifier. The object
            resource's name.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation time of the object.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last update time of the
            object.
        display_name (str):
            Required. Display name.
        errors (MutableSequence[google.cloud.datastream_v1.types.Error]):
            Output only. Active errors on the object.
        backfill_job (google.cloud.datastream_v1.types.BackfillJob):
            The latest backfill job that was initiated
            for the stream object.
        source_object (google.cloud.datastream_v1.types.SourceObjectIdentifier):
            The object identifier in the data source.
        customization_rules (MutableSequence[google.cloud.datastream_v1.types.Stream.RuleSet.CustomizationRule]):
            Output only. The customization rules for the object. These
            rules are derived from the parent Stream's ``rule_sets`` and
            represent the intended configuration for the object.
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
    display_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    errors: MutableSequence["Error"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="Error",
    )
    backfill_job: "BackfillJob" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="BackfillJob",
    )
    source_object: "SourceObjectIdentifier" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="SourceObjectIdentifier",
    )
    customization_rules: MutableSequence["Stream.RuleSet.CustomizationRule"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=9,
            message="Stream.RuleSet.CustomizationRule",
        )
    )


class SourceObjectIdentifier(proto.Message):
    r"""Represents an identifier of an object in the data source.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        oracle_identifier (google.cloud.datastream_v1.types.SourceObjectIdentifier.OracleObjectIdentifier):
            Oracle data source object identifier.

            This field is a member of `oneof`_ ``source_identifier``.
        mysql_identifier (google.cloud.datastream_v1.types.SourceObjectIdentifier.MysqlObjectIdentifier):
            Mysql data source object identifier.

            This field is a member of `oneof`_ ``source_identifier``.
        postgresql_identifier (google.cloud.datastream_v1.types.SourceObjectIdentifier.PostgresqlObjectIdentifier):
            PostgreSQL data source object identifier.

            This field is a member of `oneof`_ ``source_identifier``.
        sql_server_identifier (google.cloud.datastream_v1.types.SourceObjectIdentifier.SqlServerObjectIdentifier):
            SQLServer data source object identifier.

            This field is a member of `oneof`_ ``source_identifier``.
        salesforce_identifier (google.cloud.datastream_v1.types.SourceObjectIdentifier.SalesforceObjectIdentifier):
            Salesforce data source object identifier.

            This field is a member of `oneof`_ ``source_identifier``.
        mongodb_identifier (google.cloud.datastream_v1.types.SourceObjectIdentifier.MongodbObjectIdentifier):
            MongoDB data source object identifier.

            This field is a member of `oneof`_ ``source_identifier``.
        spanner_identifier (google.cloud.datastream_v1.types.SourceObjectIdentifier.SpannerObjectIdentifier):
            Spanner data source object identifier.

            This field is a member of `oneof`_ ``source_identifier``.
    """

    class OracleObjectIdentifier(proto.Message):
        r"""Oracle data source object identifier.

        Attributes:
            schema (str):
                Required. The schema name.
            table (str):
                Required. The table name.
        """

        schema: str = proto.Field(
            proto.STRING,
            number=1,
        )
        table: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class PostgresqlObjectIdentifier(proto.Message):
        r"""PostgreSQL data source object identifier.

        Attributes:
            schema (str):
                Required. The schema name.
            table (str):
                Required. The table name.
        """

        schema: str = proto.Field(
            proto.STRING,
            number=1,
        )
        table: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class MysqlObjectIdentifier(proto.Message):
        r"""Mysql data source object identifier.

        Attributes:
            database (str):
                Required. The database name.
            table (str):
                Required. The table name.
        """

        database: str = proto.Field(
            proto.STRING,
            number=1,
        )
        table: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class SqlServerObjectIdentifier(proto.Message):
        r"""SQLServer data source object identifier.

        Attributes:
            schema (str):
                Required. The schema name.
            table (str):
                Required. The table name.
        """

        schema: str = proto.Field(
            proto.STRING,
            number=1,
        )
        table: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class SalesforceObjectIdentifier(proto.Message):
        r"""Salesforce data source object identifier.

        Attributes:
            object_name (str):
                Required. The object name.
        """

        object_name: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class MongodbObjectIdentifier(proto.Message):
        r"""MongoDB data source object identifier.

        Attributes:
            database (str):
                Required. The database name.
            collection (str):
                Required. The collection name.
        """

        database: str = proto.Field(
            proto.STRING,
            number=1,
        )
        collection: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class SpannerObjectIdentifier(proto.Message):
        r"""Spanner data source object identifier.

        Attributes:
            schema (str):
                Optional. The schema name.
            table (str):
                Required. The table name.
        """

        schema: str = proto.Field(
            proto.STRING,
            number=1,
        )
        table: str = proto.Field(
            proto.STRING,
            number=2,
        )

    oracle_identifier: OracleObjectIdentifier = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="source_identifier",
        message=OracleObjectIdentifier,
    )
    mysql_identifier: MysqlObjectIdentifier = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="source_identifier",
        message=MysqlObjectIdentifier,
    )
    postgresql_identifier: PostgresqlObjectIdentifier = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="source_identifier",
        message=PostgresqlObjectIdentifier,
    )
    sql_server_identifier: SqlServerObjectIdentifier = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="source_identifier",
        message=SqlServerObjectIdentifier,
    )
    salesforce_identifier: SalesforceObjectIdentifier = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="source_identifier",
        message=SalesforceObjectIdentifier,
    )
    mongodb_identifier: MongodbObjectIdentifier = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="source_identifier",
        message=MongodbObjectIdentifier,
    )
    spanner_identifier: SpannerObjectIdentifier = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="source_identifier",
        message=SpannerObjectIdentifier,
    )


class BackfillJob(proto.Message):
    r"""Represents a backfill job on a specific stream object.

    Attributes:
        state (google.cloud.datastream_v1.types.BackfillJob.State):
            Output only. Backfill job state.
        trigger (google.cloud.datastream_v1.types.BackfillJob.Trigger):
            Backfill job's triggering reason.
        last_start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Backfill job's start time.
        last_end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Backfill job's end time.
        errors (MutableSequence[google.cloud.datastream_v1.types.Error]):
            Output only. Errors which caused the backfill
            job to fail.
        event_filter (google.cloud.datastream_v1.types.EventFilter):
            Output only. The filter for performing a
            partial backfill.
    """

    class State(proto.Enum):
        r"""State of the stream object's backfill job.

        Values:
            STATE_UNSPECIFIED (0):
                Default value.
            NOT_STARTED (1):
                Backfill job was never started for the stream
                object (stream has backfill strategy defined as
                manual or object was explicitly excluded from
                automatic backfill).
            PENDING (2):
                Backfill job will start pending available
                resources.
            ACTIVE (3):
                Backfill job is running.
            STOPPED (4):
                Backfill job stopped (next job run will start
                from beginning).
            FAILED (5):
                Backfill job failed (due to an error).
            COMPLETED (6):
                Backfill completed successfully.
            UNSUPPORTED (7):
                Backfill job failed since the table structure
                is currently unsupported for backfill.
        """

        STATE_UNSPECIFIED = 0
        NOT_STARTED = 1
        PENDING = 2
        ACTIVE = 3
        STOPPED = 4
        FAILED = 5
        COMPLETED = 6
        UNSUPPORTED = 7

    class Trigger(proto.Enum):
        r"""Triggering reason for a backfill job.

        Values:
            TRIGGER_UNSPECIFIED (0):
                Default value.
            AUTOMATIC (1):
                Object backfill job was triggered
                automatically according to the stream's backfill
                strategy.
            MANUAL (2):
                Object backfill job was triggered manually
                using the dedicated API.
        """

        TRIGGER_UNSPECIFIED = 0
        AUTOMATIC = 1
        MANUAL = 2

    state: State = proto.Field(
        proto.ENUM,
        number=1,
        enum=State,
    )
    trigger: Trigger = proto.Field(
        proto.ENUM,
        number=2,
        enum=Trigger,
    )
    last_start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    last_end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    errors: MutableSequence["Error"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="Error",
    )
    event_filter: "EventFilter" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="EventFilter",
    )


class EventFilter(proto.Message):
    r"""Represents a filter for included data on a stream object.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        sql_where_clause (str):
            An SQL-query Where clause selecting which data should be
            included, not including the "WHERE" keyword. e.g.,
            ``t.key1 = 'value1' AND t.key2 = 'value2'``

            This field is a member of `oneof`_ ``filter``.
    """

    sql_where_clause: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="filter",
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
        validations (MutableSequence[google.cloud.datastream_v1.types.Validation]):
            A list of validations (includes both executed
            as well as not executed validations).
    """

    validations: MutableSequence["Validation"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Validation",
    )


class Validation(proto.Message):
    r"""A validation to perform on a stream.

    Attributes:
        description (str):
            A short description of the validation.
        state (google.cloud.datastream_v1.types.Validation.State):
            Output only. Validation execution status.
        message (MutableSequence[google.cloud.datastream_v1.types.ValidationMessage]):
            Messages reflecting the validation results.
        code (str):
            A custom code identifying this validation.
    """

    class State(proto.Enum):
        r"""Validation execution state.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified state.
            NOT_EXECUTED (1):
                Validation did not execute.
            FAILED (2):
                Validation failed.
            PASSED (3):
                Validation passed.
            WARNING (4):
                Validation executed with warnings.
        """

        STATE_UNSPECIFIED = 0
        NOT_EXECUTED = 1
        FAILED = 2
        PASSED = 3
        WARNING = 4

    description: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=2,
        enum=State,
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
        level (google.cloud.datastream_v1.types.ValidationMessage.Level):
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


class CdcStrategy(proto.Message):
    r"""The strategy that the stream uses for CDC replication.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        most_recent_start_position (google.cloud.datastream_v1.types.CdcStrategy.MostRecentStartPosition):
            Optional. Start replicating from the most
            recent position in the source.

            This field is a member of `oneof`_ ``start_position``.
        next_available_start_position (google.cloud.datastream_v1.types.CdcStrategy.NextAvailableStartPosition):
            Optional. Resume replication from the next
            available position in the source.

            This field is a member of `oneof`_ ``start_position``.
        specific_start_position (google.cloud.datastream_v1.types.CdcStrategy.SpecificStartPosition):
            Optional. Start replicating from a specific
            position in the source.

            This field is a member of `oneof`_ ``start_position``.
    """

    class MostRecentStartPosition(proto.Message):
        r"""CDC strategy to start replicating from the most recent
        position in the source.

        """

    class NextAvailableStartPosition(proto.Message):
        r"""CDC strategy to resume replication from the next available
        position in the source.

        """

    class SpecificStartPosition(proto.Message):
        r"""CDC strategy to start replicating from a specific position in
        the source.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            mysql_log_position (google.cloud.datastream_v1.types.MysqlLogPosition):
                MySQL specific log position to start
                replicating from.

                This field is a member of `oneof`_ ``position``.
            oracle_scn_position (google.cloud.datastream_v1.types.OracleScnPosition):
                Oracle SCN to start replicating from.

                This field is a member of `oneof`_ ``position``.
            sql_server_lsn_position (google.cloud.datastream_v1.types.SqlServerLsnPosition):
                SqlServer LSN to start replicating from.

                This field is a member of `oneof`_ ``position``.
            mysql_gtid_position (google.cloud.datastream_v1.types.MysqlGtidPosition):
                MySQL GTID set to start replicating from.

                This field is a member of `oneof`_ ``position``.
            mongodb_change_stream_position (google.cloud.datastream_v1.types.MongodbChangeStreamPosition):
                MongoDB change stream position to start
                replicating from.

                This field is a member of `oneof`_ ``position``.
            spanner_change_stream_position (google.cloud.datastream_v1.types.SpannerChangeStreamPosition):
                Optional. Spanner change stream position to
                start replicating from.

                This field is a member of `oneof`_ ``position``.
        """

        mysql_log_position: "MysqlLogPosition" = proto.Field(
            proto.MESSAGE,
            number=101,
            oneof="position",
            message="MysqlLogPosition",
        )
        oracle_scn_position: "OracleScnPosition" = proto.Field(
            proto.MESSAGE,
            number=102,
            oneof="position",
            message="OracleScnPosition",
        )
        sql_server_lsn_position: "SqlServerLsnPosition" = proto.Field(
            proto.MESSAGE,
            number=103,
            oneof="position",
            message="SqlServerLsnPosition",
        )
        mysql_gtid_position: "MysqlGtidPosition" = proto.Field(
            proto.MESSAGE,
            number=104,
            oneof="position",
            message="MysqlGtidPosition",
        )
        mongodb_change_stream_position: "MongodbChangeStreamPosition" = proto.Field(
            proto.MESSAGE,
            number=105,
            oneof="position",
            message="MongodbChangeStreamPosition",
        )
        spanner_change_stream_position: "SpannerChangeStreamPosition" = proto.Field(
            proto.MESSAGE,
            number=106,
            oneof="position",
            message="SpannerChangeStreamPosition",
        )

    most_recent_start_position: MostRecentStartPosition = proto.Field(
        proto.MESSAGE,
        number=101,
        oneof="start_position",
        message=MostRecentStartPosition,
    )
    next_available_start_position: NextAvailableStartPosition = proto.Field(
        proto.MESSAGE,
        number=102,
        oneof="start_position",
        message=NextAvailableStartPosition,
    )
    specific_start_position: SpecificStartPosition = proto.Field(
        proto.MESSAGE,
        number=103,
        oneof="start_position",
        message=SpecificStartPosition,
    )


class SqlServerLsnPosition(proto.Message):
    r"""SQL Server LSN position

    Attributes:
        lsn (str):
            Required. Log sequence number (LSN) from
            where Logs will be read
    """

    lsn: str = proto.Field(
        proto.STRING,
        number=1,
    )


class OracleScnPosition(proto.Message):
    r"""Oracle SCN position

    Attributes:
        scn (int):
            Required. SCN number from where Logs will be
            read
    """

    scn: int = proto.Field(
        proto.INT64,
        number=1,
    )


class MysqlLogPosition(proto.Message):
    r"""MySQL log position

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        log_file (str):
            Required. The binary log file name.
        log_position (int):
            Optional. The position within the binary log
            file. Default is head of file.

            This field is a member of `oneof`_ ``_log_position``.
    """

    log_file: str = proto.Field(
        proto.STRING,
        number=1,
    )
    log_position: int = proto.Field(
        proto.INT32,
        number=2,
        optional=True,
    )


class MysqlGtidPosition(proto.Message):
    r"""MySQL GTID position

    Attributes:
        gtid_set (str):
            Required. The gtid set to start replication
            from.
    """

    gtid_set: str = proto.Field(
        proto.STRING,
        number=1,
    )


class MongodbChangeStreamPosition(proto.Message):
    r"""MongoDB change stream position

    Attributes:
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Required. The timestamp to start change
            stream from.
    """

    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )


class SpannerChangeStreamPosition(proto.Message):
    r"""Represents a position in a Spanner change stream from which
    to start replicating.

    Attributes:
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Required. The timestamp to start change
            stream queries from. The timestamp must be a
            positive value.
    """

    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
