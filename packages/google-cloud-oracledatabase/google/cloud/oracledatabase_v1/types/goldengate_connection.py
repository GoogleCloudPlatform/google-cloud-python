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
    package="google.cloud.oracledatabase.v1",
    manifest={
        "GoldengateConnection",
        "GoldengateConnectionProperties",
        "GoldengateOracleConnectionProperties",
        "GoldengateGoldengateConnectionProperties",
        "GoldengateGenericConnectionProperties",
        "GoldengateGoogleCloudStorageConnectionProperties",
        "GoldengateGoogleBigQueryConnectionProperties",
        "GoldengateMysqlConnectionProperties",
        "GoldengateKafkaConnectionProperties",
        "GoldengateKafkaSchemaRegistryConnectionProperties",
        "GoldengateOciObjectStorageConnectionProperties",
        "GoldengateAzureDataLakeStorageConnectionProperties",
        "GoldengateAzureSynapseAnalyticsConnectionProperties",
        "GoldengatePostgresqlConnectionProperties",
        "GoldengateMicrosoftSqlserverConnectionProperties",
        "GoldengateAmazonS3ConnectionProperties",
        "GoldengateHdfsConnectionProperties",
        "GoldengateJavaMessageServiceConnectionProperties",
        "GoldengateMongodbConnectionProperties",
        "GoldengateOracleNosqlConnectionProperties",
        "GoldengateSnowflakeConnectionProperties",
        "GoldengateAmazonRedshiftConnectionProperties",
        "GoldengateElasticsearchConnectionProperties",
        "GoldengateAmazonKinesisConnectionProperties",
        "GoldengateDb2ConnectionProperties",
        "GoldengateRedisConnectionProperties",
        "GoldengateDatabricksConnectionProperties",
        "GoldengateGooglePubsubConnectionProperties",
        "GoldengateMicrosoftFabricConnectionProperties",
        "GoldengateOracleAIDataPlatformConnectionProperties",
        "GlueIcebergCatalog",
        "NessieIcebergCatalog",
        "PolarisIcebergCatalog",
        "RestIcebergCatalog",
        "IcebergCatalog",
        "AmazonS3IcebergStorage",
        "GoogleCloudStorageIcebergStorage",
        "AzureDataLakeStorageIcebergStorage",
        "IcebergStorage",
        "GoldengateIcebergConnectionProperties",
        "CreateGoldengateConnectionRequest",
        "DeleteGoldengateConnectionRequest",
        "GetGoldengateConnectionRequest",
        "ListGoldengateConnectionsRequest",
        "ListGoldengateConnectionsResponse",
        "NameValuePair",
        "KafkaBootstrapServer",
    },
)


class GoldengateConnection(proto.Message):
    r"""Details of the GoldengateConnection resource.

    Attributes:
        name (str):
            Identifier. The name of the GoldengateConnection resource in
            the following format:
            projects/{project}/locations/{region}/goldengateConnections/{goldengate_connection}
        properties (google.cloud.oracledatabase_v1.types.GoldengateConnectionProperties):
            Required. The properties of the
            GoldengateConnection.
        gcp_oracle_zone (str):
            Optional. The GCP Oracle zone where Oracle
            GoldengateConnection is hosted. Example:
            us-east4-b-r2. If not specified, the system will
            pick a zone based on availability.
        labels (MutableMapping[str, str]):
            Optional. The labels or tags associated with
            the GoldengateConnection.
        odb_network (str):
            Optional. The name of the OdbNetwork associated with the
            GoldengateConnection. The format is
            projects/{project}/locations/{location}/odbNetworks/{odb_network}.
            It is optional but if specified, this should match the
            parent ODBNetwork of the OdbSubnet.
        odb_subnet (str):
            Optional. The name of the OdbSubnet associated with the
            GoldengateConnection for IP allocation. Format:
            projects/{project}/locations/{location}/odbNetworks/{odb_network}/odbSubnets/{odb_subnet}
        entitlement_id (str):
            Output only. The ID of the subscription
            entitlement associated with the
            GoldengateConnection.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The date and time that the
            GoldengateConnection was created.
        oci_url (str):
            Output only. HTTPS link to OCI resources
            exposed to Customer via UI Interface.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    properties: "GoldengateConnectionProperties" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="GoldengateConnectionProperties",
    )
    gcp_oracle_zone: str = proto.Field(
        proto.STRING,
        number=3,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    odb_network: str = proto.Field(
        proto.STRING,
        number=5,
    )
    odb_subnet: str = proto.Field(
        proto.STRING,
        number=6,
    )
    entitlement_id: str = proto.Field(
        proto.STRING,
        number=7,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    oci_url: str = proto.Field(
        proto.STRING,
        number=9,
    )


class GoldengateConnectionProperties(proto.Message):
    r"""The properties of a GoldengateConnection.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        oracle_connection_properties (google.cloud.oracledatabase_v1.types.GoldengateOracleConnectionProperties):
            Properties for an Oracle Database Connection.

            This field is a member of `oneof`_ ``connection_details``.
        goldengate_connection_properties (google.cloud.oracledatabase_v1.types.GoldengateGoldengateConnectionProperties):
            Properties for a Goldengate Connection.

            This field is a member of `oneof`_ ``connection_details``.
        generic_connection_properties (google.cloud.oracledatabase_v1.types.GoldengateGenericConnectionProperties):
            Properties for a Generic Connection.

            This field is a member of `oneof`_ ``connection_details``.
        google_cloud_storage_connection_properties (google.cloud.oracledatabase_v1.types.GoldengateGoogleCloudStorageConnectionProperties):
            Properties for a Google Cloud Storage
            Connection.

            This field is a member of `oneof`_ ``connection_details``.
        google_big_query_connection_properties (google.cloud.oracledatabase_v1.types.GoldengateGoogleBigQueryConnectionProperties):
            Properties for a Google BigQuery Connection.

            This field is a member of `oneof`_ ``connection_details``.
        mysql_connection_properties (google.cloud.oracledatabase_v1.types.GoldengateMysqlConnectionProperties):
            Properties for a Mysql Connection.

            This field is a member of `oneof`_ ``connection_details``.
        kafka_connection_properties (google.cloud.oracledatabase_v1.types.GoldengateKafkaConnectionProperties):
            Properties for a Kafka Connection.

            This field is a member of `oneof`_ ``connection_details``.
        kafka_schema_registry_connection_properties (google.cloud.oracledatabase_v1.types.GoldengateKafkaSchemaRegistryConnectionProperties):
            Properties for a Kafka Schema Registry
            Connection.

            This field is a member of `oneof`_ ``connection_details``.
        oci_object_storage_connection_properties (google.cloud.oracledatabase_v1.types.GoldengateOciObjectStorageConnectionProperties):
            Properties for an OCI Object Storage
            Connection.

            This field is a member of `oneof`_ ``connection_details``.
        azure_data_lake_storage_connection_properties (google.cloud.oracledatabase_v1.types.GoldengateAzureDataLakeStorageConnectionProperties):
            Properties for an Azure Data Lake Storage
            Connection.

            This field is a member of `oneof`_ ``connection_details``.
        azure_synapse_analytics_connection_properties (google.cloud.oracledatabase_v1.types.GoldengateAzureSynapseAnalyticsConnectionProperties):
            Properties for an Azure Synapse Analytics
            connection.

            This field is a member of `oneof`_ ``connection_details``.
        postgresql_connection_properties (google.cloud.oracledatabase_v1.types.GoldengatePostgresqlConnectionProperties):
            Properties for a PostgreSQL connection.

            This field is a member of `oneof`_ ``connection_details``.
        microsoft_sqlserver_connection_properties (google.cloud.oracledatabase_v1.types.GoldengateMicrosoftSqlserverConnectionProperties):
            Properties for a Microsoft SQL Server
            connection.

            This field is a member of `oneof`_ ``connection_details``.
        amazon_s3_connection_properties (google.cloud.oracledatabase_v1.types.GoldengateAmazonS3ConnectionProperties):
            Properties for an Amazon S3 connection.

            This field is a member of `oneof`_ ``connection_details``.
        hdfs_connection_properties (google.cloud.oracledatabase_v1.types.GoldengateHdfsConnectionProperties):
            Properties for an HDFS connection.

            This field is a member of `oneof`_ ``connection_details``.
        java_message_service_connection_properties (google.cloud.oracledatabase_v1.types.GoldengateJavaMessageServiceConnectionProperties):
            Properties for a Java Message Service
            connection.

            This field is a member of `oneof`_ ``connection_details``.
        mongodb_connection_properties (google.cloud.oracledatabase_v1.types.GoldengateMongodbConnectionProperties):
            Properties for a MongoDB connection.

            This field is a member of `oneof`_ ``connection_details``.
        oracle_nosql_connection_properties (google.cloud.oracledatabase_v1.types.GoldengateOracleNosqlConnectionProperties):
            Properties for an Oracle NoSQL connection.

            This field is a member of `oneof`_ ``connection_details``.
        snowflake_connection_properties (google.cloud.oracledatabase_v1.types.GoldengateSnowflakeConnectionProperties):
            Properties for a Snowflake connection.

            This field is a member of `oneof`_ ``connection_details``.
        amazon_redshift_connection_properties (google.cloud.oracledatabase_v1.types.GoldengateAmazonRedshiftConnectionProperties):
            Properties for an Amazon Redshift connection.

            This field is a member of `oneof`_ ``connection_details``.
        elasticsearch_connection_properties (google.cloud.oracledatabase_v1.types.GoldengateElasticsearchConnectionProperties):
            Properties for an Elasticsearch connection.

            This field is a member of `oneof`_ ``connection_details``.
        amazon_kinesis_connection_properties (google.cloud.oracledatabase_v1.types.GoldengateAmazonKinesisConnectionProperties):
            Properties for an Amazon Kinesis connection.

            This field is a member of `oneof`_ ``connection_details``.
        db2_connection_properties (google.cloud.oracledatabase_v1.types.GoldengateDb2ConnectionProperties):
            Properties for a DB2 connection.

            This field is a member of `oneof`_ ``connection_details``.
        redis_connection_properties (google.cloud.oracledatabase_v1.types.GoldengateRedisConnectionProperties):
            Properties for a Redis connection.

            This field is a member of `oneof`_ ``connection_details``.
        databricks_connection_properties (google.cloud.oracledatabase_v1.types.GoldengateDatabricksConnectionProperties):
            Properties for a Databricks connection.

            This field is a member of `oneof`_ ``connection_details``.
        google_pubsub_connection_properties (google.cloud.oracledatabase_v1.types.GoldengateGooglePubsubConnectionProperties):
            Properties for a Google Pub/Sub connection.

            This field is a member of `oneof`_ ``connection_details``.
        microsoft_fabric_connection_properties (google.cloud.oracledatabase_v1.types.GoldengateMicrosoftFabricConnectionProperties):
            Properties for a Microsoft Fabric connection.

            This field is a member of `oneof`_ ``connection_details``.
        oracle_ai_data_platform_connection_properties (google.cloud.oracledatabase_v1.types.GoldengateOracleAIDataPlatformConnectionProperties):
            Properties for an Oracle AI Data Platform
            connection.

            This field is a member of `oneof`_ ``connection_details``.
        iceberg_connection_properties (google.cloud.oracledatabase_v1.types.GoldengateIcebergConnectionProperties):
            Properties for an Iceberg connection.

            This field is a member of `oneof`_ ``connection_details``.
        connection_type (google.cloud.oracledatabase_v1.types.GoldengateConnectionProperties.GoldengateConnectionType):
            Required. The connection type.
        ocid (str):
            Output only. The [OCID] of the connection being referenced.
        display_name (str):
            Required. An object's Display Name.
        description (str):
            Optional. Metadata about this specific
            object.
        lifecycle_state (google.cloud.oracledatabase_v1.types.GoldengateConnectionProperties.GoldengateConnectionLifecycleState):
            Output only. The lifecycle state of the
            connection.
        lifecycle_details (str):
            Output only. Describes the object's current
            state in detail. For example, it can be used to
            provide actionable information for a resource in
            a Failed state.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the resource was last
            updated.
        routing_method (google.cloud.oracledatabase_v1.types.GoldengateConnectionProperties.GoldengateConnectionRoutingMethod):
            Optional. The routing method for the
            GoldengateConnection.
        ingress_ip_addresses (MutableSequence[str]):
            Output only. The Ingress IPs of the
            GoldengateConnection.
    """

    class GoldengateConnectionType(proto.Enum):
        r"""Enum for Connection type.

        Values:
            GOLDENGATE_CONNECTION_TYPE_UNSPECIFIED (0):
                Connection type unspecified.
            GOLDENGATE (1):
                Goldengate connection type.
            KAFKA (2):
                Kafka connection type.
            KAFKA_SCHEMA_REGISTRY (3):
                Kafka schema registry connection type.
            MYSQL (4):
                MySQL connection type.
            JAVA_MESSAGE_SERVICE (5):
                Java message service connection type.
            MICROSOFT_SQLSERVER (6):
                Microsoft SQL Server connection type.
            OCI_OBJECT_STORAGE (7):
                OCI object storage connection type.
            ORACLE (8):
                Oracle connection type.
            AZURE_DATA_LAKE_STORAGE (9):
                Azure data lake storage connection type.
            POSTGRESQL (10):
                PostgreSQL connection type.
            AZURE_SYNAPSE_ANALYTICS (11):
                Azure synapse analytics connection type.
            SNOWFLAKE (12):
                Snowflake connection type.
            AMAZON_S3 (13):
                Amazon S3 connection type.
            HDFS (14):
                HDFS connection type.
            ORACLE_AI_DATA_PLATFORM (15):
                Oracle AI data platform connection type.
            ORACLE_NOSQL (16):
                Oracle NoSQL connection type.
            MONGODB (17):
                MongoDB connection type.
            AMAZON_KINESIS (18):
                Amazon Kinesis connection type.
            AMAZON_REDSHIFT (19):
                Amazon Redshift connection type.
            DB2 (20):
                DB2 connection type.
            REDIS (21):
                Redis connection type.
            ELASTICSEARCH (22):
                Elasticsearch connection type.
            GENERIC (23):
                Generic connection type.
            GOOGLE_CLOUD_STORAGE (24):
                Google Cloud Storage connection type.
            GOOGLE_BIGQUERY (25):
                Google BigQuery connection type.
            DATABRICKS (26):
                Databricks connection type.
            GOOGLE_PUBSUB (27):
                Google Pub/Sub connection type.
            MICROSOFT_FABRIC (28):
                Microsoft Fabric connection type.
            ICEBERG (29):
                Iceberg connection type.
        """

        GOLDENGATE_CONNECTION_TYPE_UNSPECIFIED = 0
        GOLDENGATE = 1
        KAFKA = 2
        KAFKA_SCHEMA_REGISTRY = 3
        MYSQL = 4
        JAVA_MESSAGE_SERVICE = 5
        MICROSOFT_SQLSERVER = 6
        OCI_OBJECT_STORAGE = 7
        ORACLE = 8
        AZURE_DATA_LAKE_STORAGE = 9
        POSTGRESQL = 10
        AZURE_SYNAPSE_ANALYTICS = 11
        SNOWFLAKE = 12
        AMAZON_S3 = 13
        HDFS = 14
        ORACLE_AI_DATA_PLATFORM = 15
        ORACLE_NOSQL = 16
        MONGODB = 17
        AMAZON_KINESIS = 18
        AMAZON_REDSHIFT = 19
        DB2 = 20
        REDIS = 21
        ELASTICSEARCH = 22
        GENERIC = 23
        GOOGLE_CLOUD_STORAGE = 24
        GOOGLE_BIGQUERY = 25
        DATABRICKS = 26
        GOOGLE_PUBSUB = 27
        MICROSOFT_FABRIC = 28
        ICEBERG = 29

    class GoldengateConnectionLifecycleState(proto.Enum):
        r"""Possible lifecycle states for connection.

        Values:
            GOLDENGATE_CONNECTION_LIFECYCLE_STATE_UNSPECIFIED (0):
                Default unspecified value.
            CREATING (1):
                Indicates that the resource is in
                provisioning state.
            ACTIVE (2):
                Indicates that the resource is in active
                state.
            UPDATING (3):
                Indicates that the resource is in updating
                state.
            DELETING (4):
                Indicates that the resource is in deleting
                state.
            DELETED (5):
                Indicates that the resource is in deleted
                state.
            FAILED (6):
                Indicates that the resource is in failed
                state.
        """

        GOLDENGATE_CONNECTION_LIFECYCLE_STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        UPDATING = 3
        DELETING = 4
        DELETED = 5
        FAILED = 6

    class GoldengateConnectionRoutingMethod(proto.Enum):
        r"""The various routing methods of the GoldengateConnection.

        Values:
            GOLDENGATE_CONNECTION_ROUTING_METHOD_UNSPECIFIED (0):
                Default unspecified value.
            SHARED_DEPLOYMENT_ENDPOINT (1):
                Network traffic flows from the assigned
                deployment's private endpoint through the
                deployment's subnet.
            DEDICATED_ENDPOINT (2):
                A dedicated private endpoint is created in
                the target VCN subnet for the connection.
        """

        GOLDENGATE_CONNECTION_ROUTING_METHOD_UNSPECIFIED = 0
        SHARED_DEPLOYMENT_ENDPOINT = 1
        DEDICATED_ENDPOINT = 2

    oracle_connection_properties: "GoldengateOracleConnectionProperties" = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="connection_details",
        message="GoldengateOracleConnectionProperties",
    )
    goldengate_connection_properties: "GoldengateGoldengateConnectionProperties" = (
        proto.Field(
            proto.MESSAGE,
            number=10,
            oneof="connection_details",
            message="GoldengateGoldengateConnectionProperties",
        )
    )
    generic_connection_properties: "GoldengateGenericConnectionProperties" = (
        proto.Field(
            proto.MESSAGE,
            number=11,
            oneof="connection_details",
            message="GoldengateGenericConnectionProperties",
        )
    )
    google_cloud_storage_connection_properties: "GoldengateGoogleCloudStorageConnectionProperties" = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="connection_details",
        message="GoldengateGoogleCloudStorageConnectionProperties",
    )
    google_big_query_connection_properties: "GoldengateGoogleBigQueryConnectionProperties" = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="connection_details",
        message="GoldengateGoogleBigQueryConnectionProperties",
    )
    mysql_connection_properties: "GoldengateMysqlConnectionProperties" = proto.Field(
        proto.MESSAGE,
        number=14,
        oneof="connection_details",
        message="GoldengateMysqlConnectionProperties",
    )
    kafka_connection_properties: "GoldengateKafkaConnectionProperties" = proto.Field(
        proto.MESSAGE,
        number=15,
        oneof="connection_details",
        message="GoldengateKafkaConnectionProperties",
    )
    kafka_schema_registry_connection_properties: "GoldengateKafkaSchemaRegistryConnectionProperties" = proto.Field(
        proto.MESSAGE,
        number=16,
        oneof="connection_details",
        message="GoldengateKafkaSchemaRegistryConnectionProperties",
    )
    oci_object_storage_connection_properties: "GoldengateOciObjectStorageConnectionProperties" = proto.Field(
        proto.MESSAGE,
        number=17,
        oneof="connection_details",
        message="GoldengateOciObjectStorageConnectionProperties",
    )
    azure_data_lake_storage_connection_properties: "GoldengateAzureDataLakeStorageConnectionProperties" = proto.Field(
        proto.MESSAGE,
        number=18,
        oneof="connection_details",
        message="GoldengateAzureDataLakeStorageConnectionProperties",
    )
    azure_synapse_analytics_connection_properties: "GoldengateAzureSynapseAnalyticsConnectionProperties" = proto.Field(
        proto.MESSAGE,
        number=19,
        oneof="connection_details",
        message="GoldengateAzureSynapseAnalyticsConnectionProperties",
    )
    postgresql_connection_properties: "GoldengatePostgresqlConnectionProperties" = (
        proto.Field(
            proto.MESSAGE,
            number=20,
            oneof="connection_details",
            message="GoldengatePostgresqlConnectionProperties",
        )
    )
    microsoft_sqlserver_connection_properties: "GoldengateMicrosoftSqlserverConnectionProperties" = proto.Field(
        proto.MESSAGE,
        number=21,
        oneof="connection_details",
        message="GoldengateMicrosoftSqlserverConnectionProperties",
    )
    amazon_s3_connection_properties: "GoldengateAmazonS3ConnectionProperties" = (
        proto.Field(
            proto.MESSAGE,
            number=22,
            oneof="connection_details",
            message="GoldengateAmazonS3ConnectionProperties",
        )
    )
    hdfs_connection_properties: "GoldengateHdfsConnectionProperties" = proto.Field(
        proto.MESSAGE,
        number=23,
        oneof="connection_details",
        message="GoldengateHdfsConnectionProperties",
    )
    java_message_service_connection_properties: "GoldengateJavaMessageServiceConnectionProperties" = proto.Field(
        proto.MESSAGE,
        number=24,
        oneof="connection_details",
        message="GoldengateJavaMessageServiceConnectionProperties",
    )
    mongodb_connection_properties: "GoldengateMongodbConnectionProperties" = (
        proto.Field(
            proto.MESSAGE,
            number=25,
            oneof="connection_details",
            message="GoldengateMongodbConnectionProperties",
        )
    )
    oracle_nosql_connection_properties: "GoldengateOracleNosqlConnectionProperties" = (
        proto.Field(
            proto.MESSAGE,
            number=26,
            oneof="connection_details",
            message="GoldengateOracleNosqlConnectionProperties",
        )
    )
    snowflake_connection_properties: "GoldengateSnowflakeConnectionProperties" = (
        proto.Field(
            proto.MESSAGE,
            number=27,
            oneof="connection_details",
            message="GoldengateSnowflakeConnectionProperties",
        )
    )
    amazon_redshift_connection_properties: "GoldengateAmazonRedshiftConnectionProperties" = proto.Field(
        proto.MESSAGE,
        number=28,
        oneof="connection_details",
        message="GoldengateAmazonRedshiftConnectionProperties",
    )
    elasticsearch_connection_properties: "GoldengateElasticsearchConnectionProperties" = proto.Field(
        proto.MESSAGE,
        number=29,
        oneof="connection_details",
        message="GoldengateElasticsearchConnectionProperties",
    )
    amazon_kinesis_connection_properties: "GoldengateAmazonKinesisConnectionProperties" = proto.Field(
        proto.MESSAGE,
        number=31,
        oneof="connection_details",
        message="GoldengateAmazonKinesisConnectionProperties",
    )
    db2_connection_properties: "GoldengateDb2ConnectionProperties" = proto.Field(
        proto.MESSAGE,
        number=32,
        oneof="connection_details",
        message="GoldengateDb2ConnectionProperties",
    )
    redis_connection_properties: "GoldengateRedisConnectionProperties" = proto.Field(
        proto.MESSAGE,
        number=33,
        oneof="connection_details",
        message="GoldengateRedisConnectionProperties",
    )
    databricks_connection_properties: "GoldengateDatabricksConnectionProperties" = (
        proto.Field(
            proto.MESSAGE,
            number=34,
            oneof="connection_details",
            message="GoldengateDatabricksConnectionProperties",
        )
    )
    google_pubsub_connection_properties: "GoldengateGooglePubsubConnectionProperties" = proto.Field(
        proto.MESSAGE,
        number=35,
        oneof="connection_details",
        message="GoldengateGooglePubsubConnectionProperties",
    )
    microsoft_fabric_connection_properties: "GoldengateMicrosoftFabricConnectionProperties" = proto.Field(
        proto.MESSAGE,
        number=36,
        oneof="connection_details",
        message="GoldengateMicrosoftFabricConnectionProperties",
    )
    oracle_ai_data_platform_connection_properties: "GoldengateOracleAIDataPlatformConnectionProperties" = proto.Field(
        proto.MESSAGE,
        number=37,
        oneof="connection_details",
        message="GoldengateOracleAIDataPlatformConnectionProperties",
    )
    iceberg_connection_properties: "GoldengateIcebergConnectionProperties" = (
        proto.Field(
            proto.MESSAGE,
            number=38,
            oneof="connection_details",
            message="GoldengateIcebergConnectionProperties",
        )
    )
    connection_type: GoldengateConnectionType = proto.Field(
        proto.ENUM,
        number=1,
        enum=GoldengateConnectionType,
    )
    ocid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    lifecycle_state: GoldengateConnectionLifecycleState = proto.Field(
        proto.ENUM,
        number=5,
        enum=GoldengateConnectionLifecycleState,
    )
    lifecycle_details: str = proto.Field(
        proto.STRING,
        number=6,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    routing_method: GoldengateConnectionRoutingMethod = proto.Field(
        proto.ENUM,
        number=8,
        enum=GoldengateConnectionRoutingMethod,
    )
    ingress_ip_addresses: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=39,
    )


class GoldengateOracleConnectionProperties(proto.Message):
    r"""The properties of Goldengate Oracle Database Connection.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        password (str):
            Optional. Input only. The password Oracle
            Goldengate uses in plain text.

            This field is a member of `oneof`_ ``connection_password_options``.
        password_secret_version (str):
            Optional. Input only. The resource name of a
            secret version in Secret Manager which contains
            the password Oracle Goldengate uses. Format:

            projects/{project}/secrets/{secret}/versions/{version}.

            This field is a member of `oneof`_ ``connection_password_options``.
        technology_type (str):
            Optional. The technology type.
        username (str):
            Optional. The username Oracle Goldengate uses
            to connect.
        authentication_mode (google.cloud.oracledatabase_v1.types.GoldengateOracleConnectionProperties.OracleAuthenticationMode):
            Optional. Authentication mode.
        connection_string (str):
            Optional. Connect descriptor or Easy Connect
            Naming method used to connect to a database.
        session_mode (google.cloud.oracledatabase_v1.types.GoldengateOracleConnectionProperties.SessionMode):
            Optional. The mode of the database connection
            session to be established by the data client.
        gcp_oracle_database_id (str):
            Optional. Autonomous AI Database instance id of database in
            Oracle Database @ Google Cloud. If gcp_oracle_database_id is
            provided, connection_string must be empty. Format:
            projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}
        wallet_file (str):
            Optional. The wallet contents Oracle
            Goldengate uses to make connections to a
            database. This attribute is expected to be
            base64 encoded.
    """

    class OracleAuthenticationMode(proto.Enum):
        r"""Enum for Authentication mode.

        Values:
            ORACLE_AUTHENTICATION_MODE_UNSPECIFIED (0):
                Authentication mode not specified.
            TLS (1):
                TLS authentication mode.
            MTLS (2):
                MTLS authentication mode.
        """

        ORACLE_AUTHENTICATION_MODE_UNSPECIFIED = 0
        TLS = 1
        MTLS = 2

    class SessionMode(proto.Enum):
        r"""The various session modes of the GoldengateConnection.

        Values:
            SESSION_MODE_UNSPECIFIED (0):
                Default unspecified value.
            DIRECT (1):
                Indicates that the resource is using direct
                session mode.
            REDIRECT (2):
                Indicates that the resource is using redirect
                session mode.
        """

        SESSION_MODE_UNSPECIFIED = 0
        DIRECT = 1
        REDIRECT = 2

    password: str = proto.Field(
        proto.STRING,
        number=10,
        oneof="connection_password_options",
    )
    password_secret_version: str = proto.Field(
        proto.STRING,
        number=11,
        oneof="connection_password_options",
    )
    technology_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    username: str = proto.Field(
        proto.STRING,
        number=2,
    )
    authentication_mode: OracleAuthenticationMode = proto.Field(
        proto.ENUM,
        number=3,
        enum=OracleAuthenticationMode,
    )
    connection_string: str = proto.Field(
        proto.STRING,
        number=4,
    )
    session_mode: SessionMode = proto.Field(
        proto.ENUM,
        number=5,
        enum=SessionMode,
    )
    gcp_oracle_database_id: str = proto.Field(
        proto.STRING,
        number=6,
    )
    wallet_file: str = proto.Field(
        proto.STRING,
        number=9,
    )


class GoldengateGoldengateConnectionProperties(proto.Message):
    r"""The properties of GoldengateGoldengateConnectionProperties.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        password (str):
            Optional. Input only. The password used to
            connect to the Oracle Goldengate in plain text.

            This field is a member of `oneof`_ ``connection_password_options``.
        password_secret_version (str):
            Optional. Input only. The resource name of a
            secret version in Secret Manager which contains
            the password used to connect to the Oracle
            Goldengate. Format:

            projects/{project}/secrets/{secret}/versions/{version}.

            This field is a member of `oneof`_ ``connection_password_options``.
        technology_type (str):
            Optional. The technology type.
        goldengate_deployment_id (str):
            Optional. The name of the GoldengateDeployment associated
            with the GoldengateConnection. Format:
            projects/{project}/locations/{location}/goldengateDeployments/{goldengate_deployment}
        host (str):
            Optional. The host of the
            GoldengateConnection.
        port (int):
            Optional. The port of the
            GoldengateConnection.
        username (str):
            Optional. The username credential.
    """

    password: str = proto.Field(
        proto.STRING,
        number=7,
        oneof="connection_password_options",
    )
    password_secret_version: str = proto.Field(
        proto.STRING,
        number=8,
        oneof="connection_password_options",
    )
    technology_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    goldengate_deployment_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    host: str = proto.Field(
        proto.STRING,
        number=3,
    )
    port: int = proto.Field(
        proto.INT32,
        number=4,
    )
    username: str = proto.Field(
        proto.STRING,
        number=5,
    )


class GoldengateGenericConnectionProperties(proto.Message):
    r"""The properties of GoldengateGenericConnectionProperties.

    Attributes:
        technology_type (str):
            Optional. The technology type.
        host (str):
            Optional. The host of the GenericConnection.
    """

    technology_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    host: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GoldengateGoogleCloudStorageConnectionProperties(proto.Message):
    r"""The properties of
    GoldengateGoogleCloudStorageConnectionProperties.

    Attributes:
        technology_type (str):
            Optional. The technology type.
        service_account_key_file (str):
            Optional. The base64 encoded content of the
            service account key file containing the
            credentials required to use Google Cloud
            Storage.
    """

    technology_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    service_account_key_file: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GoldengateGoogleBigQueryConnectionProperties(proto.Message):
    r"""The properties of
    GoldengateGoogleBigQueryConnectionProperties.

    Attributes:
        technology_type (str):
            Optional. The technology type.
        service_account_key_file (str):
            Optional. The base64 encoded content of the
            service account key file containing the
            credentials required to use Google BigQuery.
    """

    technology_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    service_account_key_file: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GoldengateMysqlConnectionProperties(proto.Message):
    r"""Properties of GoldengateMysqlConnection.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        password (str):
            Optional. Input only. The password Oracle
            Goldengate uses to connect to MySQL in plain
            text.

            This field is a member of `oneof`_ ``connection_password_options``.
        password_secret_version (str):
            Optional. Input only. The resource name of a
            secret version in Secret Manager which contains
            the password Oracle Goldengate uses to connect
            to MySQL. Format:
            projects/{project}/secrets/{secret}/versions/{version}.

            This field is a member of `oneof`_ ``connection_password_options``.
        technology_type (str):
            Optional. The technology type of
            MysqlConnection.
        username (str):
            Optional. The username Oracle Goldengate uses
            to connect the associated system of the given
            technology.
        host (str):
            Optional. The name or address of a host.
        port (int):
            Optional. The port of an endpoint usually
            specified for a connection.
        database (str):
            Optional. The name of the database.
        security_protocol (google.cloud.oracledatabase_v1.types.GoldengateMysqlConnectionProperties.MysqlSecurityProtocol):
            Optional. Security Type for MySQL.
        ssl_mode (google.cloud.oracledatabase_v1.types.GoldengateMysqlConnectionProperties.SSLMode):
            Optional. SSL modes for MySQL.
        ssl_ca_file (str):
            Optional. Database Certificate - The base64
            encoded content of a .pem or .crt file
            containing the server public key (for 1 and
            2-way SSL).
        ssl_crl_file (str):
            Optional. The base64 encoded list of
            certificates revoked by the trusted certificate
            authorities (Trusted CA).
        ssl_cert_file (str):
            Optional. Client Certificate - The base64
            encoded content of a .pem or .crt file
            containing the client public key (for 2-way
            SSL).
        ssl_key_file (str):
            Optional. Client Key - The base64 encoded
            content of a .pem or .crt file containing the
            client private key (for 2-way SSL).
        additional_attributes (MutableSequence[google.cloud.oracledatabase_v1.types.NameValuePair]):
            Optional. An array of name-value pair
            attribute entries. Used as additional parameters
            in connection string.
        db_system_id (str):
            Optional. The OCID of the database system
            being referenced.
    """

    class MysqlSecurityProtocol(proto.Enum):
        r"""Enum for Security Type for MySQL.

        Values:
            MYSQL_SECURITY_PROTOCOL_UNSPECIFIED (0):
                Security type not specified.
            PLAIN (1):
                Plain text communication.
            TLS (2):
                Transport Layer Security.
            MTLS (3):
                Mutual Transport Layer Security.
        """

        MYSQL_SECURITY_PROTOCOL_UNSPECIFIED = 0
        PLAIN = 1
        TLS = 2
        MTLS = 3

    class SSLMode(proto.Enum):
        r"""Enum for SSL modes for MySQL.

        Values:
            SSL_MODE_UNSPECIFIED (0):
                SSL mode not specified.
            DISABLED (1):
                SSL is disabled.
            PREFERRED (2):
                SSL is preferred.
            REQUIRED (3):
                SSL is required.
            VERIFY_CA (4):
                SSL is required and certificate is verified.
            VERIFY_IDENTITY (5):
                SSL is required and certificate and hostname
                are verified.
        """

        SSL_MODE_UNSPECIFIED = 0
        DISABLED = 1
        PREFERRED = 2
        REQUIRED = 3
        VERIFY_CA = 4
        VERIFY_IDENTITY = 5

    password: str = proto.Field(
        proto.STRING,
        number=15,
        oneof="connection_password_options",
    )
    password_secret_version: str = proto.Field(
        proto.STRING,
        number=16,
        oneof="connection_password_options",
    )
    technology_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    username: str = proto.Field(
        proto.STRING,
        number=2,
    )
    host: str = proto.Field(
        proto.STRING,
        number=4,
    )
    port: int = proto.Field(
        proto.INT32,
        number=5,
    )
    database: str = proto.Field(
        proto.STRING,
        number=6,
    )
    security_protocol: MysqlSecurityProtocol = proto.Field(
        proto.ENUM,
        number=7,
        enum=MysqlSecurityProtocol,
    )
    ssl_mode: SSLMode = proto.Field(
        proto.ENUM,
        number=8,
        enum=SSLMode,
    )
    ssl_ca_file: str = proto.Field(
        proto.STRING,
        number=9,
    )
    ssl_crl_file: str = proto.Field(
        proto.STRING,
        number=10,
    )
    ssl_cert_file: str = proto.Field(
        proto.STRING,
        number=11,
    )
    ssl_key_file: str = proto.Field(
        proto.STRING,
        number=12,
    )
    additional_attributes: MutableSequence["NameValuePair"] = proto.RepeatedField(
        proto.MESSAGE,
        number=13,
        message="NameValuePair",
    )
    db_system_id: str = proto.Field(
        proto.STRING,
        number=14,
    )


class GoldengateKafkaConnectionProperties(proto.Message):
    r"""The properties of GoldengateKafkaConnection.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        password (str):
            Optional. Input only. The password for Kafka
            basic/SASL auth in plain text.

            This field is a member of `oneof`_ ``connection_password_options``.
        password_secret_version (str):
            Optional. Input only. The resource name of a
            secret version in Secret Manager which contains
            the password for Kafka basic/SASL auth. Format:

            projects/{project}/secrets/{secret}/versions/{version}.

            This field is a member of `oneof`_ ``connection_password_options``.
        trust_store_password (str):
            Optional. Input only. The TrustStore password
            in plain text.

            This field is a member of `oneof`_ ``trust_store_password_options``.
        trust_store_password_secret_version (str):
            Optional. Input only. The resource name of a
            secret version in Secret Manager which contains
            the TrustStore password. Format:

            projects/{project}/secrets/{secret}/versions/{version}.

            This field is a member of `oneof`_ ``trust_store_password_options``.
        key_store_password (str):
            Optional. Input only. The KeyStore password
            in plain text.

            This field is a member of `oneof`_ ``key_store_password_options``.
        key_store_password_secret_version (str):
            Optional. Input only. The resource name of a
            secret version in Secret Manager which contains
            the KeyStore password. Format:

            projects/{project}/secrets/{secret}/versions/{version}.

            This field is a member of `oneof`_ ``key_store_password_options``.
        ssl_key_password (str):
            Optional. Input only. The password for the
            cert inside of the KeyStore in plain text.

            This field is a member of `oneof`_ ``ssl_key_password_options``.
        ssl_key_password_secret_version (str):
            Optional. Input only. The resource name of a
            secret version in Secret Manager which contains
            the password for the cert inside of the
            KeyStore. Format:
            projects/{project}/secrets/{secret}/versions/{version}.

            This field is a member of `oneof`_ ``ssl_key_password_options``.
        technology_type (str):
            Optional. The technology type of
            KafkaConnection.
        stream_pool_id (str):
            Optional. The OCID of the stream pool being
            referenced.
        cluster_id (str):
            Optional. The OCID of the Kafka cluster being
            referenced from OCI Streaming with Apache Kafka.
        bootstrap_servers (MutableSequence[google.cloud.oracledatabase_v1.types.KafkaBootstrapServer]):
            Optional. Kafka bootstrap. Equivalent of
            bootstrap.servers configuration property in
            Kafka: list of KafkaBootstrapServer objects
            specified by host/port. Used for establishing
            the initial connection to the Kafka cluster.
            Example:
            "server1.example.com:9092,server2.example.com:9092".
        security_protocol (google.cloud.oracledatabase_v1.types.GoldengateKafkaConnectionProperties.KafkaSecurityProtocol):
            Optional. Security Type for Kafka.
        username (str):
            Optional. The username Oracle Goldengate uses
            to connect the associated system of the given
            technology.
        trust_store_file (str):
            Optional. The base64 encoded content of the
            TrustStore file.
        key_store_file (str):
            Optional. The base64 encoded content of the
            KeyStore file.
        consumer_properties_file (str):
            Optional. The base64 encoded content of the
            consumer.properties file.
        producer_properties_file (str):
            Optional. The base64 encoded content of the
            producer.properties file.
        use_resource_principal (bool):
            Optional. Specifies that the user intends to
            authenticate to the instance using a resource
            principal. Applicable only for OCI Streaming
            connections.
    """

    class KafkaSecurityProtocol(proto.Enum):
        r"""Enum for Security Type for Kafka.

        Values:
            KAFKA_SECURITY_PROTOCOL_UNSPECIFIED (0):
                Security type not specified.
            SSL (1):
                SSL security protocol.
            SASL_SSL (2):
                SASL SSL security protocol.
            PLAINTEXT (3):
                Plaintext security protocol.
            SASL_PLAINTEXT (4):
                SASL Plaintext security protocol.
        """

        KAFKA_SECURITY_PROTOCOL_UNSPECIFIED = 0
        SSL = 1
        SASL_SSL = 2
        PLAINTEXT = 3
        SASL_PLAINTEXT = 4

    password: str = proto.Field(
        proto.STRING,
        number=16,
        oneof="connection_password_options",
    )
    password_secret_version: str = proto.Field(
        proto.STRING,
        number=20,
        oneof="connection_password_options",
    )
    trust_store_password: str = proto.Field(
        proto.STRING,
        number=17,
        oneof="trust_store_password_options",
    )
    trust_store_password_secret_version: str = proto.Field(
        proto.STRING,
        number=21,
        oneof="trust_store_password_options",
    )
    key_store_password: str = proto.Field(
        proto.STRING,
        number=18,
        oneof="key_store_password_options",
    )
    key_store_password_secret_version: str = proto.Field(
        proto.STRING,
        number=22,
        oneof="key_store_password_options",
    )
    ssl_key_password: str = proto.Field(
        proto.STRING,
        number=19,
        oneof="ssl_key_password_options",
    )
    ssl_key_password_secret_version: str = proto.Field(
        proto.STRING,
        number=23,
        oneof="ssl_key_password_options",
    )
    technology_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    stream_pool_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    cluster_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    bootstrap_servers: MutableSequence["KafkaBootstrapServer"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="KafkaBootstrapServer",
    )
    security_protocol: KafkaSecurityProtocol = proto.Field(
        proto.ENUM,
        number=5,
        enum=KafkaSecurityProtocol,
    )
    username: str = proto.Field(
        proto.STRING,
        number=6,
    )
    trust_store_file: str = proto.Field(
        proto.STRING,
        number=8,
    )
    key_store_file: str = proto.Field(
        proto.STRING,
        number=10,
    )
    consumer_properties_file: str = proto.Field(
        proto.STRING,
        number=13,
    )
    producer_properties_file: str = proto.Field(
        proto.STRING,
        number=14,
    )
    use_resource_principal: bool = proto.Field(
        proto.BOOL,
        number=15,
    )


class GoldengateKafkaSchemaRegistryConnectionProperties(proto.Message):
    r"""The properties of GoldengateKafkaSchemaRegistryConnection.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        password (str):
            Optional. Input only. The password to access
            Schema Registry in plain text.

            This field is a member of `oneof`_ ``connection_password_options``.
        password_secret_version (str):
            Optional. Input only. The resource name of a
            secret version in Secret Manager which contains
            the password to access Schema Registry using
            basic authentication. Format:

            projects/{project}/secrets/{secret}/versions/{version}.

            This field is a member of `oneof`_ ``connection_password_options``.
        trust_store_password (str):
            Optional. Input only. The TrustStore password
            in plain text.

            This field is a member of `oneof`_ ``trust_store_password_options``.
        trust_store_password_secret_version (str):
            Optional. Input only. The resource name of a
            secret version in Secret Manager which contains
            the TrustStore password. Format:

            projects/{project}/secrets/{secret}/versions/{version}.

            This field is a member of `oneof`_ ``trust_store_password_options``.
        key_store_password (str):
            Optional. Input only. The KeyStore password
            in plain text.

            This field is a member of `oneof`_ ``key_store_password_options``.
        key_store_password_secret_version (str):
            Optional. Input only. The resource name of a
            secret version in Secret Manager which contains
            the KeyStore password. Format:

            projects/{project}/secrets/{secret}/versions/{version}.

            This field is a member of `oneof`_ ``key_store_password_options``.
        ssl_key_password (str):
            Optional. Input only. The password for the
            cert inside the KeyStore in plain text.

            This field is a member of `oneof`_ ``ssl_key_password_options``.
        ssl_key_password_secret_version (str):
            Optional. Input only. The resource name of a
            secret version in Secret Manager which contains
            the password for the cert inside the KeyStore.
            Format:
            projects/{project}/secrets/{secret}/versions/{version}.

            This field is a member of `oneof`_ ``ssl_key_password_options``.
        technology_type (str):
            Optional. The technology type of
            KafkaSchemaRegistryConnection.
        url (str):
            Optional. Kafka Schema Registry URL.
            e.g.: 'https://server1.us.oracle.com:8081'
        authentication_type (google.cloud.oracledatabase_v1.types.GoldengateKafkaSchemaRegistryConnectionProperties.AuthenticationType):
            Optional. Used authentication mechanism to
            access Schema Registry.
        username (str):
            Optional. The username to access Schema
            Registry using basic authentication. This value
            is injected into
            'schema.registry.basic.auth.user.info=user:password'
            configuration property.
        trust_store_file (str):
            Optional. The base64 encoded content of the
            TrustStore file.
        key_store_file (str):
            Optional. The base64 encoded content of the
            KeyStore file.
    """

    class AuthenticationType(proto.Enum):
        r"""Enum for authentication mechanism to access Schema Registry.

        Values:
            AUTHENTICATION_TYPE_UNSPECIFIED (0):
                Authentication type not specified.
            NONE (1):
                No authentication.
            BASIC (2):
                Basic authentication.
            MUTUAL (3):
                Mutual authentication.
        """

        AUTHENTICATION_TYPE_UNSPECIFIED = 0
        NONE = 1
        BASIC = 2
        MUTUAL = 3

    password: str = proto.Field(
        proto.STRING,
        number=11,
        oneof="connection_password_options",
    )
    password_secret_version: str = proto.Field(
        proto.STRING,
        number=15,
        oneof="connection_password_options",
    )
    trust_store_password: str = proto.Field(
        proto.STRING,
        number=12,
        oneof="trust_store_password_options",
    )
    trust_store_password_secret_version: str = proto.Field(
        proto.STRING,
        number=16,
        oneof="trust_store_password_options",
    )
    key_store_password: str = proto.Field(
        proto.STRING,
        number=13,
        oneof="key_store_password_options",
    )
    key_store_password_secret_version: str = proto.Field(
        proto.STRING,
        number=17,
        oneof="key_store_password_options",
    )
    ssl_key_password: str = proto.Field(
        proto.STRING,
        number=14,
        oneof="ssl_key_password_options",
    )
    ssl_key_password_secret_version: str = proto.Field(
        proto.STRING,
        number=18,
        oneof="ssl_key_password_options",
    )
    technology_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    url: str = proto.Field(
        proto.STRING,
        number=2,
    )
    authentication_type: AuthenticationType = proto.Field(
        proto.ENUM,
        number=3,
        enum=AuthenticationType,
    )
    username: str = proto.Field(
        proto.STRING,
        number=4,
    )
    trust_store_file: str = proto.Field(
        proto.STRING,
        number=6,
    )
    key_store_file: str = proto.Field(
        proto.STRING,
        number=8,
    )


class GoldengateOciObjectStorageConnectionProperties(proto.Message):
    r"""The properties of GoldengateOciObjectStorageConnection.

    Attributes:
        technology_type (str):
            Optional. The technology type of
            OciObjectStorageConnection.
        tenancy_id (str):
            Optional. The OCID of the related OCI
            tenancy.
        region (str):
            Optional. The name of the region of OCI
            Object Storage. e.g.: us-ashburn-1 If the region
            is not provided, backend will default to the
            default region.
        user_id (str):
            Optional. The OCID of the OCI user who will
            access the Object Storage. The user must have
            write access to the bucket they want to connect
            to.
        private_key_file (str):
            Optional. The content of the private key file
            (PEM file) corresponding to the API key of the
            fingerprint.
        private_key_passphrase_secret (str):
            Optional. The passphrase of the private key.
        public_key_fingerprint (str):
            Optional. The fingerprint of the API Key of
            the user specified by the userId.
        use_resource_principal (bool):
            Optional. Specifies that the user intends to
            authenticate to the instance using a resource
            principal.
    """

    technology_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    tenancy_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    region: str = proto.Field(
        proto.STRING,
        number=3,
    )
    user_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    private_key_file: str = proto.Field(
        proto.STRING,
        number=5,
    )
    private_key_passphrase_secret: str = proto.Field(
        proto.STRING,
        number=6,
    )
    public_key_fingerprint: str = proto.Field(
        proto.STRING,
        number=7,
    )
    use_resource_principal: bool = proto.Field(
        proto.BOOL,
        number=8,
    )


class GoldengateAzureDataLakeStorageConnectionProperties(proto.Message):
    r"""The properties of GoldengateAzureDataLakeStorageConnection.

    Attributes:
        technology_type (str):
            Optional. The technology type of
            AzureDataLakeStorageConnection.
        authentication_type (google.cloud.oracledatabase_v1.types.GoldengateAzureDataLakeStorageConnectionProperties.AuthenticationType):
            Optional. Authentication mechanism to access
            Azure Data Lake Storage.
        account (str):
            Optional. Sets the Azure storage account
            name.
        account_key_secret (str):
            Optional. Azure storage account key. This property is
            required when 'authentication_type' is set to 'SHARED_KEY'.
        sas_token_secret (str):
            Optional. Credential that uses a shared
            access signature (SAS) to authenticate to an
            Azure Service.
        azure_tenant_id (str):
            Optional. Azure tenant ID of the application. This property
            is required when 'authentication_type' is set to
            'AZURE_ACTIVE_DIRECTORY'.
        client_id (str):
            Optional. Azure client ID of the application. This property
            is required when 'authentication_type' is set to
            'AZURE_ACTIVE_DIRECTORY'.
        client_secret (str):
            Optional. Azure client secret (aka
            application password) for authentication.
        endpoint (str):
            Optional. Azure Storage service endpoint.
            e.g: https://test.blob.core.windows.net
        azure_authority_host (str):
            Optional. The endpoint used for
            authentication with Microsoft Entra ID (formerly
            Azure Active Directory). Default value:

            https://login.microsoftonline.com
    """

    class AuthenticationType(proto.Enum):
        r"""Enum for authentication mechanism to access Azure Data Lake
        Storage.

        Values:
            AUTHENTICATION_TYPE_UNSPECIFIED (0):
                Authentication type not specified.
            SHARED_KEY (1):
                Shared key authentication.
            SHARED_ACCESS_SIGNATURE (2):
                Shared access signature authentication.
            AZURE_ACTIVE_DIRECTORY (3):
                Azure active directory authentication.
        """

        AUTHENTICATION_TYPE_UNSPECIFIED = 0
        SHARED_KEY = 1
        SHARED_ACCESS_SIGNATURE = 2
        AZURE_ACTIVE_DIRECTORY = 3

    technology_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    authentication_type: AuthenticationType = proto.Field(
        proto.ENUM,
        number=2,
        enum=AuthenticationType,
    )
    account: str = proto.Field(
        proto.STRING,
        number=3,
    )
    account_key_secret: str = proto.Field(
        proto.STRING,
        number=4,
    )
    sas_token_secret: str = proto.Field(
        proto.STRING,
        number=5,
    )
    azure_tenant_id: str = proto.Field(
        proto.STRING,
        number=6,
    )
    client_id: str = proto.Field(
        proto.STRING,
        number=7,
    )
    client_secret: str = proto.Field(
        proto.STRING,
        number=8,
    )
    endpoint: str = proto.Field(
        proto.STRING,
        number=9,
    )
    azure_authority_host: str = proto.Field(
        proto.STRING,
        number=10,
    )


class GoldengateAzureSynapseAnalyticsConnectionProperties(proto.Message):
    r"""The properties of GoldengateAzureSynapseAnalyticsConnection.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        password (str):
            Optional. Input only. The password Oracle
            Goldengate uses for Azure Synapse Analytics
            connection in plain text.

            This field is a member of `oneof`_ ``connection_password_options``.
        password_secret_version (str):
            Optional. Input only. The resource name of a
            secret version in Secret Manager which contains
            the password Oracle Goldengate uses for Azure
            Synapse Analytics connection. Format:

            projects/{project}/secrets/{secret}/versions/{version}.

            This field is a member of `oneof`_ ``connection_password_options``.
        technology_type (str):
            Optional. The technology type of
            AzureSynapseAnalyticsConnection.
        connection_string (str):
            Optional. JDBC connection string. e.g.:
            'jdbc:sqlserver://.sql.azuresynapse.net:1433;database=;encrypt=true;trustServerCertificate=false;hostNameInCertificate=\*.sql.azuresynapse.net;loginTimeout=300;'
        username (str):
            Optional. The username Oracle Goldengate uses
            to connect the associated system of the given
            technology.
    """

    password: str = proto.Field(
        proto.STRING,
        number=5,
        oneof="connection_password_options",
    )
    password_secret_version: str = proto.Field(
        proto.STRING,
        number=6,
        oneof="connection_password_options",
    )
    technology_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    connection_string: str = proto.Field(
        proto.STRING,
        number=2,
    )
    username: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GoldengatePostgresqlConnectionProperties(proto.Message):
    r"""The properties of GoldengatePostgresqlConnection.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        password (str):
            Optional. Input only. The password Oracle
            Goldengate uses for PostgreSQL connection in
            plain text.

            This field is a member of `oneof`_ ``connection_password_options``.
        password_secret_version (str):
            Optional. Input only. The resource name of a
            secret version in Secret Manager which contains
            the password Oracle Goldengate uses for
            PostgreSQL connection. Format:

            projects/{project}/secrets/{secret}/versions/{version}.

            This field is a member of `oneof`_ ``connection_password_options``.
        technology_type (str):
            Optional. The technology type of
            PostgresqlConnection.
        database (str):
            Optional. The name of the database.
        host (str):
            Optional. The name or address of a host.
        port (int):
            Optional. The port of an endpoint usually
            specified for a connection.
        username (str):
            Optional. The username Oracle Goldengate uses
            to connect the associated system of the given
            technology.
        additional_attributes (MutableSequence[google.cloud.oracledatabase_v1.types.NameValuePair]):
            Optional. An array of name-value pair
            attribute entries. Used as additional parameters
            in connection string.
        security_protocol (google.cloud.oracledatabase_v1.types.GoldengatePostgresqlConnectionProperties.PostgresqlSecurityProtocol):
            Optional. Security protocol for PostgreSQL.
        ssl_mode (google.cloud.oracledatabase_v1.types.GoldengatePostgresqlConnectionProperties.PostgresqlSslMode):
            Optional. SSL modes for PostgreSQL.
        ssl_ca_file (str):
            Optional. The base64 encoded certificate of
            the trusted certificate authorities (Trusted CA)
            for PostgreSQL.
        ssl_crl_file (str):
            Optional. The base64 encoded list of
            certificates revoked by the trusted certificate
            authorities (Trusted CA).
        ssl_cert_file (str):
            Optional. The base64 encoded certificate of
            the PostgreSQL server.
        ssl_key_file (str):
            Optional. The base64 encoded private key of
            the PostgreSQL server.
        db_system_id (str):
            Optional. The OCID of the database system
            being referenced.
    """

    class PostgresqlSecurityProtocol(proto.Enum):
        r"""Enum for Security protocol for PostgreSQL.

        Values:
            POSTGRESQL_SECURITY_PROTOCOL_UNSPECIFIED (0):
                Security protocol not specified.
            PLAIN (1):
                Plain text communication.
            TLS (2):
                Transport Layer Security.
            MTLS (3):
                Mutual Transport Layer Security.
        """

        POSTGRESQL_SECURITY_PROTOCOL_UNSPECIFIED = 0
        PLAIN = 1
        TLS = 2
        MTLS = 3

    class PostgresqlSslMode(proto.Enum):
        r"""Enum for SSL modes for PostgreSQL.

        Values:
            POSTGRESQL_SSL_MODE_UNSPECIFIED (0):
                SSL mode not specified.
            PREFER (1):
                Prefer SSL.
            REQUIRE (2):
                Require SSL.
            VERIFY_CA (3):
                Verify Certificate Authority.
            VERIFY_FULL (4):
                Verify Full.
        """

        POSTGRESQL_SSL_MODE_UNSPECIFIED = 0
        PREFER = 1
        REQUIRE = 2
        VERIFY_CA = 3
        VERIFY_FULL = 4

    password: str = proto.Field(
        proto.STRING,
        number=15,
        oneof="connection_password_options",
    )
    password_secret_version: str = proto.Field(
        proto.STRING,
        number=16,
        oneof="connection_password_options",
    )
    technology_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    database: str = proto.Field(
        proto.STRING,
        number=2,
    )
    host: str = proto.Field(
        proto.STRING,
        number=3,
    )
    port: int = proto.Field(
        proto.INT32,
        number=4,
    )
    username: str = proto.Field(
        proto.STRING,
        number=5,
    )
    additional_attributes: MutableSequence["NameValuePair"] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="NameValuePair",
    )
    security_protocol: PostgresqlSecurityProtocol = proto.Field(
        proto.ENUM,
        number=8,
        enum=PostgresqlSecurityProtocol,
    )
    ssl_mode: PostgresqlSslMode = proto.Field(
        proto.ENUM,
        number=9,
        enum=PostgresqlSslMode,
    )
    ssl_ca_file: str = proto.Field(
        proto.STRING,
        number=10,
    )
    ssl_crl_file: str = proto.Field(
        proto.STRING,
        number=11,
    )
    ssl_cert_file: str = proto.Field(
        proto.STRING,
        number=12,
    )
    ssl_key_file: str = proto.Field(
        proto.STRING,
        number=13,
    )
    db_system_id: str = proto.Field(
        proto.STRING,
        number=14,
    )


class GoldengateMicrosoftSqlserverConnectionProperties(proto.Message):
    r"""The properties of GoldengateMicrosoftSqlserverConnection.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        password (str):
            Optional. Input only. The password Oracle
            Goldengate uses for Microsoft SQL Server
            connection in plain text.

            This field is a member of `oneof`_ ``connection_password_options``.
        password_secret_version (str):
            Optional. Input only. The resource name of a
            secret version in Secret Manager which contains
            the password Oracle Goldengate uses for
            Microsoft SQL Server connection. Format:

            projects/{project}/secrets/{secret}/versions/{version}.

            This field is a member of `oneof`_ ``connection_password_options``.
        technology_type (str):
            Optional. The technology type of
            MicrosoftSqlserverConnection.
        database (str):
            Optional. The name of the database.
        host (str):
            Optional. The name or address of a host.
        port (int):
            Optional. The port of an endpoint usually
            specified for a connection.
        username (str):
            Optional. The username Oracle Goldengate uses
            to connect to the Microsoft SQL Server.
        additional_attributes (MutableSequence[google.cloud.oracledatabase_v1.types.NameValuePair]):
            Optional. An array of name-value pair
            attribute entries. Used as additional parameters
            in connection string.
        security_protocol (google.cloud.oracledatabase_v1.types.GoldengateMicrosoftSqlserverConnectionProperties.MicrosoftSqlserverSecurityProtocol):
            Optional. Security Type for Microsoft SQL
            Server.
        ssl_ca_file (str):
            Optional. Database Certificate - The base64
            encoded content of a .pem or .crt file
            containing the server public key (for 1-way
            SSL).
        server_certificate_validation_required (bool):
            Optional. If set to true, the driver
            validates the certificate that is sent by the
            database server.
    """

    class MicrosoftSqlserverSecurityProtocol(proto.Enum):
        r"""Enum for Security Type for Microsoft SQL Server.

        Values:
            MICROSOFT_SQLSERVER_SECURITY_PROTOCOL_UNSPECIFIED (0):
                Security type not specified.
            PLAIN (1):
                Plain text communication.
            TLS (2):
                Transport Layer Security.
        """

        MICROSOFT_SQLSERVER_SECURITY_PROTOCOL_UNSPECIFIED = 0
        PLAIN = 1
        TLS = 2

    password: str = proto.Field(
        proto.STRING,
        number=11,
        oneof="connection_password_options",
    )
    password_secret_version: str = proto.Field(
        proto.STRING,
        number=12,
        oneof="connection_password_options",
    )
    technology_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    database: str = proto.Field(
        proto.STRING,
        number=2,
    )
    host: str = proto.Field(
        proto.STRING,
        number=3,
    )
    port: int = proto.Field(
        proto.INT32,
        number=4,
    )
    username: str = proto.Field(
        proto.STRING,
        number=5,
    )
    additional_attributes: MutableSequence["NameValuePair"] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="NameValuePair",
    )
    security_protocol: MicrosoftSqlserverSecurityProtocol = proto.Field(
        proto.ENUM,
        number=8,
        enum=MicrosoftSqlserverSecurityProtocol,
    )
    ssl_ca_file: str = proto.Field(
        proto.STRING,
        number=9,
    )
    server_certificate_validation_required: bool = proto.Field(
        proto.BOOL,
        number=10,
    )


class GoldengateAmazonS3ConnectionProperties(proto.Message):
    r"""The properties of GoldengateAmazonS3Connection.

    Attributes:
        technology_type (str):
            Optional. The technology type of
            AmazonS3Connection.
        access_key_id (str):
            Optional. Access key ID to access the Amazon
            S3 bucket.
        secret_access_key_secret (str):
            Optional. Secret access key to access the
            Amazon S3 bucket.
        endpoint (str):
            Optional. The Amazon Endpoint for S3.
        region (str):
            Optional. The name of the AWS region where
            the bucket is created.
    """

    technology_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    access_key_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    secret_access_key_secret: str = proto.Field(
        proto.STRING,
        number=3,
    )
    endpoint: str = proto.Field(
        proto.STRING,
        number=4,
    )
    region: str = proto.Field(
        proto.STRING,
        number=5,
    )


class GoldengateHdfsConnectionProperties(proto.Message):
    r"""The properties of GoldengateHdfsConnection.

    Attributes:
        technology_type (str):
            Optional. The technology type of
            HdfsConnection.
        core_site_xml (str):
            Optional. The content of the Hadoop
            Distributed File System configuration file
            (core-site.xml).
    """

    technology_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    core_site_xml: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GoldengateJavaMessageServiceConnectionProperties(proto.Message):
    r"""The properties of GoldengateJavaMessageServiceConnection.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        password (str):
            Optional. Input only. The password Oracle
            Goldengate uses to connect the Java Message
            Service in plain text.

            This field is a member of `oneof`_ ``connection_password_options``.
        password_secret_version (str):
            Optional. Input only. The resource name of a
            secret version in Secret Manager which contains
            the password Oracle Goldengate uses to connect
            the associated Java Message Service. Format:

            projects/{project}/secrets/{secret}/versions/{version}.

            This field is a member of `oneof`_ ``connection_password_options``.
        trust_store_password (str):
            Optional. Input only. The TrustStore password
            in plain text.

            This field is a member of `oneof`_ ``trust_store_password_options``.
        trust_store_password_secret_version (str):
            Optional. Input only. The resource name of a
            secret version in Secret Manager which contains
            the TrustStore password. Format:

            projects/{project}/secrets/{secret}/versions/{version}.

            This field is a member of `oneof`_ ``trust_store_password_options``.
        key_store_password (str):
            Optional. Input only. The KeyStore password
            in plain text.

            This field is a member of `oneof`_ ``key_store_password_options``.
        key_store_password_secret_version (str):
            Optional. Input only. The resource name of a
            secret version in Secret Manager which contains
            the KeyStore password. Format:

            projects/{project}/secrets/{secret}/versions/{version}.

            This field is a member of `oneof`_ ``key_store_password_options``.
        ssl_key_password (str):
            Optional. Input only. The password for the
            cert inside of the KeyStore in plain text.

            This field is a member of `oneof`_ ``ssl_key_password_options``.
        ssl_key_password_secret_version (str):
            Optional. Input only. The resource name of a
            secret version in Secret Manager which contains
            the password for the cert inside of the
            KeyStore. Format:
            projects/{project}/secrets/{secret}/versions/{version}.

            This field is a member of `oneof`_ ``ssl_key_password_options``.
        technology_type (str):
            Optional. The technology type of
            JavaMessageServiceConnection.
        use_jndi (bool):
            Optional. If set to true, Java Naming and
            Directory Interface (JNDI) properties should be
            provided.
        jndi_connection_factory (str):
            Optional. The Connection Factory can be
            looked up using this name. e.g.:
            'ConnectionFactory'
        jndi_provider_url (str):
            Optional. The URL that Java Message Service
            will use to contact the JNDI provider. e.g.:
            'tcp://myjms.host.domain:61616?jms.prefetchPolicy.all=1000'
        jndi_initial_context_factory (str):
            Optional. The implementation of
            javax.naming.spi.InitialContextFactory interface
            used to obtain initial naming context.
        jndi_security_principal (str):
            Optional. Specifies the identity of the
            principal (user) to be authenticated.
        jndi_security_credentials_secret (str):
            Optional. The password associated to the
            principal.
        connection_url (str):
            Optional. Connection URL of the Java Message
            Service, specifying the protocol, host, and
            port. e.g.: 'mq://myjms.host.domain:7676'
        connection_factory (str):
            Optional. The Java class implementing
            javax.jms.ConnectionFactory interface supplied
            by the JMS provider.
        username (str):
            Optional. The username Oracle Goldengate uses
            to connect to the Java Message Service.
        security_protocol (google.cloud.oracledatabase_v1.types.GoldengateJavaMessageServiceConnectionProperties.JmsSecurityProtocol):
            Optional. Security protocol for Java Message
            Service.
        authentication_type (google.cloud.oracledatabase_v1.types.GoldengateJavaMessageServiceConnectionProperties.JmsAuthenticationType):
            Optional. Authentication type for Java
            Message Service.
        trust_store_file (str):
            Optional. The base64 encoded content of the
            TrustStore file.
        key_store_file (str):
            Optional. The base64 encoded content of the
            KeyStore file.
    """

    class JmsSecurityProtocol(proto.Enum):
        r"""Enum for Security protocol for Java Message Service.

        Values:
            JMS_SECURITY_PROTOCOL_UNSPECIFIED (0):
                Security protocol not specified.
            PLAIN (1):
                Plain text communication.
            TLS (2):
                Transport Layer Security.
            MTLS (3):
                Mutual Transport Layer Security.
        """

        JMS_SECURITY_PROTOCOL_UNSPECIFIED = 0
        PLAIN = 1
        TLS = 2
        MTLS = 3

    class JmsAuthenticationType(proto.Enum):
        r"""Enum for Authentication type for Java Message Service.

        Values:
            JMS_AUTHENTICATION_TYPE_UNSPECIFIED (0):
                Authentication type not specified.
            NONE (1):
                No authentication.
            BASIC (2):
                Basic authentication.
        """

        JMS_AUTHENTICATION_TYPE_UNSPECIFIED = 0
        NONE = 1
        BASIC = 2

    password: str = proto.Field(
        proto.STRING,
        number=19,
        oneof="connection_password_options",
    )
    password_secret_version: str = proto.Field(
        proto.STRING,
        number=23,
        oneof="connection_password_options",
    )
    trust_store_password: str = proto.Field(
        proto.STRING,
        number=20,
        oneof="trust_store_password_options",
    )
    trust_store_password_secret_version: str = proto.Field(
        proto.STRING,
        number=24,
        oneof="trust_store_password_options",
    )
    key_store_password: str = proto.Field(
        proto.STRING,
        number=21,
        oneof="key_store_password_options",
    )
    key_store_password_secret_version: str = proto.Field(
        proto.STRING,
        number=25,
        oneof="key_store_password_options",
    )
    ssl_key_password: str = proto.Field(
        proto.STRING,
        number=22,
        oneof="ssl_key_password_options",
    )
    ssl_key_password_secret_version: str = proto.Field(
        proto.STRING,
        number=26,
        oneof="ssl_key_password_options",
    )
    technology_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    use_jndi: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    jndi_connection_factory: str = proto.Field(
        proto.STRING,
        number=3,
    )
    jndi_provider_url: str = proto.Field(
        proto.STRING,
        number=4,
    )
    jndi_initial_context_factory: str = proto.Field(
        proto.STRING,
        number=5,
    )
    jndi_security_principal: str = proto.Field(
        proto.STRING,
        number=6,
    )
    jndi_security_credentials_secret: str = proto.Field(
        proto.STRING,
        number=7,
    )
    connection_url: str = proto.Field(
        proto.STRING,
        number=8,
    )
    connection_factory: str = proto.Field(
        proto.STRING,
        number=9,
    )
    username: str = proto.Field(
        proto.STRING,
        number=10,
    )
    security_protocol: JmsSecurityProtocol = proto.Field(
        proto.ENUM,
        number=12,
        enum=JmsSecurityProtocol,
    )
    authentication_type: JmsAuthenticationType = proto.Field(
        proto.ENUM,
        number=13,
        enum=JmsAuthenticationType,
    )
    trust_store_file: str = proto.Field(
        proto.STRING,
        number=14,
    )
    key_store_file: str = proto.Field(
        proto.STRING,
        number=16,
    )


class GoldengateMongodbConnectionProperties(proto.Message):
    r"""The properties of GoldengateMongodbConnection.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        password (str):
            Optional. Input only. The password Oracle
            Goldengate uses to connect the Mongodb
            connection in plain text.

            This field is a member of `oneof`_ ``connection_password_options``.
        password_secret_version (str):
            Optional. Input only. The resource name of a
            secret version in Secret Manager which contains
            the password Oracle Goldengate uses to connect
            the Mongodb connection. Format:

            projects/{project}/secrets/{secret}/versions/{version}.

            This field is a member of `oneof`_ ``connection_password_options``.
        tls_certificate_key_file_password (str):
            Optional. Input only. The Client Certificate
            key file password in plain text.

            This field is a member of `oneof`_ ``tls_certificate_key_file_password_options``.
        tls_certificate_key_file_password_secret_version (str):
            Optional. Input only. The resource name of a
            secret version in Secret Manager which contains
            the Client Certificate key file password in
            Secret Manager. Format:
            projects/{project}/secrets/{secret}/versions/{version}.

            This field is a member of `oneof`_ ``tls_certificate_key_file_password_options``.
        technology_type (str):
            Optional. The technology type of
            MongodbConnection.
        connection_string (str):
            Optional. MongoDB connection string.
            e.g.:
            'mongodb://mongodb0.example.com:27017/recordsrecords'
        username (str):
            Optional. The username Oracle Goldengate uses
            to connect to the database.
        database_id (str):
            Optional. The OCID of the Oracle Autonomous
            Json Database.
        security_protocol (google.cloud.oracledatabase_v1.types.GoldengateMongodbConnectionProperties.MongodbSecurityProtocol):
            Optional. Security Type for MongoDB.
        tls_ca_file (str):
            Optional. Database Certificate - The base64
            encoded content of a .pem file, containing the
            server public key (for 1 and 2-way SSL).
        tls_certificate_key_file (str):
            Optional. Client Certificate - The base64
            encoded content of a .pem file, containing the
            client public key (for 2-way SSL).
    """

    class MongodbSecurityProtocol(proto.Enum):
        r"""Enum for Security Type for MongoDB.

        Values:
            MONGODB_SECURITY_PROTOCOL_UNSPECIFIED (0):
                Security type not specified.
            PLAIN (1):
                Plain text communication.
            TLS (2):
                Transport Layer Security.
            MTLS (3):
                Mutual Transport Layer Security.
        """

        MONGODB_SECURITY_PROTOCOL_UNSPECIFIED = 0
        PLAIN = 1
        TLS = 2
        MTLS = 3

    password: str = proto.Field(
        proto.STRING,
        number=10,
        oneof="connection_password_options",
    )
    password_secret_version: str = proto.Field(
        proto.STRING,
        number=12,
        oneof="connection_password_options",
    )
    tls_certificate_key_file_password: str = proto.Field(
        proto.STRING,
        number=11,
        oneof="tls_certificate_key_file_password_options",
    )
    tls_certificate_key_file_password_secret_version: str = proto.Field(
        proto.STRING,
        number=13,
        oneof="tls_certificate_key_file_password_options",
    )
    technology_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    connection_string: str = proto.Field(
        proto.STRING,
        number=2,
    )
    username: str = proto.Field(
        proto.STRING,
        number=3,
    )
    database_id: str = proto.Field(
        proto.STRING,
        number=5,
    )
    security_protocol: MongodbSecurityProtocol = proto.Field(
        proto.ENUM,
        number=6,
        enum=MongodbSecurityProtocol,
    )
    tls_ca_file: str = proto.Field(
        proto.STRING,
        number=7,
    )
    tls_certificate_key_file: str = proto.Field(
        proto.STRING,
        number=8,
    )


class GoldengateOracleNosqlConnectionProperties(proto.Message):
    r"""The properties of GoldengateOracleNosqlConnection.

    Attributes:
        technology_type (str):
            Optional. The technology type of
            OracleNosqlConnection.
        tenancy_id (str):
            Optional. The OCID of the OCI tenancy.
        region (str):
            Optional. The name of the region. e.g.:
            us-ashburn-1
        user_id (str):
            Optional. The OCID of the OCI user who will
            access the Oracle NoSQL database.
        private_key_file (str):
            Optional. The content of the private key file
            (PEM file) corresponding to the API key of the
            fingerprint.
        private_key_passphrase_secret (str):
            Optional. The passphrase of the private key.
        public_key_fingerprint (str):
            Optional. The fingerprint of the API Key of
            the user specified by the userId.
        use_resource_principal (bool):
            Optional. Specifies that the user intends to
            authenticate to the instance using a resource
            principal.
    """

    technology_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    tenancy_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    region: str = proto.Field(
        proto.STRING,
        number=3,
    )
    user_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    private_key_file: str = proto.Field(
        proto.STRING,
        number=5,
    )
    private_key_passphrase_secret: str = proto.Field(
        proto.STRING,
        number=6,
    )
    public_key_fingerprint: str = proto.Field(
        proto.STRING,
        number=7,
    )
    use_resource_principal: bool = proto.Field(
        proto.BOOL,
        number=8,
    )


class GoldengateSnowflakeConnectionProperties(proto.Message):
    r"""The properties of GoldengateSnowflakeConnection.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        password (str):
            Optional. Input only. The password Oracle
            Goldengate uses to connect to Snowflake platform
            in plain text.

            This field is a member of `oneof`_ ``connection_password_options``.
        password_secret_version (str):
            Optional. Input only. The resource name of a
            secret version in Secret Manager which contains
            the password Oracle Goldengate uses to connect
            to Snowflake platform. Format:

            projects/{project}/secrets/{secret}/versions/{version}.

            This field is a member of `oneof`_ ``connection_password_options``.
        technology_type (str):
            Optional. The technology type of
            SnowflakeConnection.
        connection_url (str):
            Optional. JDBC connection URL. e.g.:
            'jdbc:snowflake://<account_name>.snowflakecomputing.com/?warehouse=&db='
        authentication_type (google.cloud.oracledatabase_v1.types.GoldengateSnowflakeConnectionProperties.AuthenticationType):
            Optional. Used authentication mechanism to
            access Snowflake.
        username (str):
            Optional. The username Oracle Goldengate uses
            to connect to Snowflake.
        private_key_file (str):
            Optional. The content of private key file in
            PEM format.
        private_key_passphrase_secret (str):
            Optional. Password if the private key file is
            encrypted.
    """

    class AuthenticationType(proto.Enum):
        r"""Enum for authentication mechanism to access Snowflake.

        Values:
            AUTHENTICATION_TYPE_UNSPECIFIED (0):
                Authentication type not specified.
            BASIC (1):
                Basic authentication.
            KEY_PAIR (2):
                Key pair authentication.
        """

        AUTHENTICATION_TYPE_UNSPECIFIED = 0
        BASIC = 1
        KEY_PAIR = 2

    password: str = proto.Field(
        proto.STRING,
        number=8,
        oneof="connection_password_options",
    )
    password_secret_version: str = proto.Field(
        proto.STRING,
        number=9,
        oneof="connection_password_options",
    )
    technology_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    connection_url: str = proto.Field(
        proto.STRING,
        number=2,
    )
    authentication_type: AuthenticationType = proto.Field(
        proto.ENUM,
        number=3,
        enum=AuthenticationType,
    )
    username: str = proto.Field(
        proto.STRING,
        number=4,
    )
    private_key_file: str = proto.Field(
        proto.STRING,
        number=6,
    )
    private_key_passphrase_secret: str = proto.Field(
        proto.STRING,
        number=7,
    )


class GoldengateAmazonRedshiftConnectionProperties(proto.Message):
    r"""The properties of GoldengateAmazonRedshiftConnection.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        password (str):
            Optional. Input only. The password Oracle
            Goldengate uses for Amazon Redshift connection
            in plain text.

            This field is a member of `oneof`_ ``connection_password_options``.
        password_secret_version (str):
            Optional. Input only. The resource name of a
            secret version in Secret Manager which contains
            the password Oracle Goldengate uses for Amazon
            Redshift connection. Format:

            projects/{project}/secrets/{secret}/versions/{version}.

            This field is a member of `oneof`_ ``connection_password_options``.
        technology_type (str):
            Optional. The technology type of
            AmazonRedshiftConnection.
        connection_url (str):
            Optional. Connection URL.
            e.g.:

            'jdbc:redshift://aws-redshift-instance.aaaaaaaaaaaa.us-east-2.redshift.amazonaws.com:5439/mydb'
        username (str):
            Optional. The username Oracle Goldengate uses
            to connect the associated system of the given
            technology.
    """

    password: str = proto.Field(
        proto.STRING,
        number=5,
        oneof="connection_password_options",
    )
    password_secret_version: str = proto.Field(
        proto.STRING,
        number=6,
        oneof="connection_password_options",
    )
    technology_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    connection_url: str = proto.Field(
        proto.STRING,
        number=2,
    )
    username: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GoldengateElasticsearchConnectionProperties(proto.Message):
    r"""The properties of GoldengateElasticsearchConnection.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        password (str):
            Optional. Input only. The password Oracle
            Goldengate uses for Elastic Search connection in
            plain text.

            This field is a member of `oneof`_ ``connection_password_options``.
        password_secret_version (str):
            Optional. Input only. The resource name of a
            secret version in Secret Manager which contains
            the password Oracle Goldengate uses for Elastic
            Search connection. Format:

            projects/{project}/secrets/{secret}/versions/{version}.

            This field is a member of `oneof`_ ``connection_password_options``.
        technology_type (str):
            Optional. The technology type of
            ElasticsearchConnection.
        servers (str):
            Optional. Comma separated list of
            Elasticsearch server addresses, specified as
            host:port entries, where :port is optional. If
            port is not specified, it defaults to 9200.
            Example:

            "server1.example.com:4000,server2.example.com:4000".
        security_protocol (google.cloud.oracledatabase_v1.types.GoldengateElasticsearchConnectionProperties.ElasticsearchSecurityProtocol):
            Optional. Security protocol for
            Elasticsearch.
        authentication_type (google.cloud.oracledatabase_v1.types.GoldengateElasticsearchConnectionProperties.ElasticsearchAuthenticationType):
            Optional. Authentication type for
            Elasticsearch.
        username (str):
            Optional. The username Oracle Goldengate uses
            to connect the associated system of the given
            technology.
        fingerprint (str):
            Optional. Fingerprint required by TLS
            security protocol. Eg.:
            '6152b2dfbff200f973c5074a5b91d06ab3b472c07c09a1ea57bb7fd406cdce9c'
    """

    class ElasticsearchSecurityProtocol(proto.Enum):
        r"""Enum for Security protocol for Elasticsearch.

        Values:
            ELASTICSEARCH_SECURITY_PROTOCOL_UNSPECIFIED (0):
                Security protocol not specified.
            PLAIN (1):
                Plain text communication.
            TLS (2):
                Transport Layer Security.
        """

        ELASTICSEARCH_SECURITY_PROTOCOL_UNSPECIFIED = 0
        PLAIN = 1
        TLS = 2

    class ElasticsearchAuthenticationType(proto.Enum):
        r"""Enum for Authentication type for Elasticsearch.

        Values:
            ELASTICSEARCH_AUTHENTICATION_TYPE_UNSPECIFIED (0):
                Authentication type not specified.
            NONE (1):
                No authentication.
            BASIC (2):
                Basic authentication.
        """

        ELASTICSEARCH_AUTHENTICATION_TYPE_UNSPECIFIED = 0
        NONE = 1
        BASIC = 2

    password: str = proto.Field(
        proto.STRING,
        number=8,
        oneof="connection_password_options",
    )
    password_secret_version: str = proto.Field(
        proto.STRING,
        number=9,
        oneof="connection_password_options",
    )
    technology_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    servers: str = proto.Field(
        proto.STRING,
        number=2,
    )
    security_protocol: ElasticsearchSecurityProtocol = proto.Field(
        proto.ENUM,
        number=3,
        enum=ElasticsearchSecurityProtocol,
    )
    authentication_type: ElasticsearchAuthenticationType = proto.Field(
        proto.ENUM,
        number=4,
        enum=ElasticsearchAuthenticationType,
    )
    username: str = proto.Field(
        proto.STRING,
        number=5,
    )
    fingerprint: str = proto.Field(
        proto.STRING,
        number=7,
    )


class GoldengateAmazonKinesisConnectionProperties(proto.Message):
    r"""The properties of GoldengateAmazonKinesisConnection.

    Attributes:
        technology_type (str):
            Optional. The technology type of
            AmazonKinesisConnection.
        access_key_id (str):
            Optional. Access key ID to access the Amazon
            Kinesis.
        secret_access_key_secret (str):
            Optional. Secret access key to access the
            Amazon Kinesis.
        endpoint (str):
            Optional. The endpoint URL of the Amazon
            Kinesis service. e.g.:
            'https://kinesis.us-east-1.amazonaws.com' If not
            provided, Goldengate will default to
            'https://kinesis.<region>.amazonaws.com'.
        aws_region (str):
            Optional. The name of the AWS region.
            If not provided, Goldengate will default to
            'us-west-1'.
    """

    technology_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    access_key_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    secret_access_key_secret: str = proto.Field(
        proto.STRING,
        number=3,
    )
    endpoint: str = proto.Field(
        proto.STRING,
        number=4,
    )
    aws_region: str = proto.Field(
        proto.STRING,
        number=5,
    )


class GoldengateDb2ConnectionProperties(proto.Message):
    r"""The properties of GoldengateDb2Connection.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        password (str):
            Optional. Input only. The password Oracle
            Goldengate uses for Db2 connection in plain
            text.

            This field is a member of `oneof`_ ``connection_password_options``.
        password_secret_version (str):
            Optional. Input only. The resource name of a
            secret version in Secret Manager which contains
            the password Oracle Goldengate uses for Db2
            connection. Format:

            projects/{project}/secrets/{secret}/versions/{version}.

            This field is a member of `oneof`_ ``connection_password_options``.
        technology_type (str):
            Optional. The technology type of
            Db2Connection.
        host (str):
            Optional. The name or address of a host.
        port (int):
            Optional. The port of an endpoint usually
            specified for a connection.
        database (str):
            Optional. The name of the database.
        username (str):
            Optional. The username Oracle Goldengate uses
            to connect to the DB2 database.
        security_protocol (google.cloud.oracledatabase_v1.types.GoldengateDb2ConnectionProperties.Db2SecurityProtocol):
            Optional. Security protocol for the DB2
            database.
        additional_attributes (MutableSequence[google.cloud.oracledatabase_v1.types.NameValuePair]):
            Optional. An array of name-value pair
            attribute entries. Used as additional parameters
            in connection string.
        ssl_client_keystoredb_file (str):
            Optional. The keystore file created at the
            client containing the server certificate / CA
            root certificate. Not supported for IBM Db2 for
            i.
        ssl_client_keystash_file (str):
            Optional. The keystash file which contains
            the encrypted password to the key database file.
            Not supported for IBM Db2 for i.
        ssl_server_certificate_file (str):
            Optional. The file which contains the
            self-signed server certificate / Certificate
            Authority (CA) certificate.
    """

    class Db2SecurityProtocol(proto.Enum):
        r"""Enum for Security protocol for the DB2 database.

        Values:
            DB2_SECURITY_PROTOCOL_UNSPECIFIED (0):
                Security protocol not specified.
            PLAIN (1):
                Plain text communication.
            TLS (2):
                Transport Layer Security.
        """

        DB2_SECURITY_PROTOCOL_UNSPECIFIED = 0
        PLAIN = 1
        TLS = 2

    password: str = proto.Field(
        proto.STRING,
        number=12,
        oneof="connection_password_options",
    )
    password_secret_version: str = proto.Field(
        proto.STRING,
        number=13,
        oneof="connection_password_options",
    )
    technology_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    host: str = proto.Field(
        proto.STRING,
        number=2,
    )
    port: int = proto.Field(
        proto.INT32,
        number=3,
    )
    database: str = proto.Field(
        proto.STRING,
        number=4,
    )
    username: str = proto.Field(
        proto.STRING,
        number=5,
    )
    security_protocol: Db2SecurityProtocol = proto.Field(
        proto.ENUM,
        number=6,
        enum=Db2SecurityProtocol,
    )
    additional_attributes: MutableSequence["NameValuePair"] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message="NameValuePair",
    )
    ssl_client_keystoredb_file: str = proto.Field(
        proto.STRING,
        number=9,
    )
    ssl_client_keystash_file: str = proto.Field(
        proto.STRING,
        number=10,
    )
    ssl_server_certificate_file: str = proto.Field(
        proto.STRING,
        number=11,
    )


class GoldengateRedisConnectionProperties(proto.Message):
    r"""The properties of GoldengateRedisConnection.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        password (str):
            Optional. Input only. The password Oracle
            Goldengate uses for Redis connection in plain
            text.

            This field is a member of `oneof`_ ``connection_password_options``.
        password_secret_version (str):
            Optional. Input only. The resource name of a
            secret version in Secret Manager which contains
            the password Oracle Goldengate uses for Redis
            connection. Format:

            projects/{project}/secrets/{secret}/versions/{version}.

            This field is a member of `oneof`_ ``connection_password_options``.
        trust_store_password (str):
            Optional. Input only. The TrustStore password
            in plain text.

            This field is a member of `oneof`_ ``trust_store_password_options``.
        trust_store_password_secret_version (str):
            Optional. Input only. The resource name of a
            secret version in Secret Manager which contains
            the TrustStore password. Format:

            projects/{project}/secrets/{secret}/versions/{version}.

            This field is a member of `oneof`_ ``trust_store_password_options``.
        key_store_password (str):
            Optional. Input only. The KeyStore password
            in plain text.

            This field is a member of `oneof`_ ``key_store_password_options``.
        key_store_password_secret_version (str):
            Optional. Input only. The resource name of a
            secret version in Secret Manager which contains
            the KeyStore password. Format:

            projects/{project}/secrets/{secret}/versions/{version}.

            This field is a member of `oneof`_ ``key_store_password_options``.
        technology_type (str):
            Optional. The technology type of
            RedisConnection.
        servers (str):
            Optional. Comma separated list of Redis
            server addresses, specified as host:port
            entries, where :port is optional. If port is not
            specified, it defaults to 6379. Example:

            "server1.example.com:6379,server2.example.com:6379".
        security_protocol (google.cloud.oracledatabase_v1.types.GoldengateRedisConnectionProperties.RedisSecurityProtocol):
            Optional. Security protocol for Redis.
        authentication_type (google.cloud.oracledatabase_v1.types.GoldengateRedisConnectionProperties.RedisAuthenticationType):
            Optional. Authentication type for Redis.
        username (str):
            Optional. The username Oracle Goldengate uses
            to connect the associated system of the given
            technology.
        redis_cluster_id (str):
            Optional. The OCID of the Redis cluster.
        trust_store_file (str):
            Optional. The base64 encoded content of the
            TrustStore file.
        key_store_file (str):
            Optional. The base64 encoded content of the
            KeyStore file.
    """

    class RedisSecurityProtocol(proto.Enum):
        r"""Enum for Security protocol for Redis.

        Values:
            REDIS_SECURITY_PROTOCOL_UNSPECIFIED (0):
                Security protocol not specified.
            PLAIN (1):
                Plain text communication.
            TLS (2):
                Transport Layer Security.
            MTLS (3):
                Mutual Transport Layer Security.
        """

        REDIS_SECURITY_PROTOCOL_UNSPECIFIED = 0
        PLAIN = 1
        TLS = 2
        MTLS = 3

    class RedisAuthenticationType(proto.Enum):
        r"""Enum for Authentication type for Redis.

        Values:
            REDIS_AUTHENTICATION_TYPE_UNSPECIFIED (0):
                Authentication type not specified.
            NONE (1):
                No authentication.
            BASIC (2):
                Basic authentication.
        """

        REDIS_AUTHENTICATION_TYPE_UNSPECIFIED = 0
        NONE = 1
        BASIC = 2

    password: str = proto.Field(
        proto.STRING,
        number=12,
        oneof="connection_password_options",
    )
    password_secret_version: str = proto.Field(
        proto.STRING,
        number=15,
        oneof="connection_password_options",
    )
    trust_store_password: str = proto.Field(
        proto.STRING,
        number=13,
        oneof="trust_store_password_options",
    )
    trust_store_password_secret_version: str = proto.Field(
        proto.STRING,
        number=16,
        oneof="trust_store_password_options",
    )
    key_store_password: str = proto.Field(
        proto.STRING,
        number=14,
        oneof="key_store_password_options",
    )
    key_store_password_secret_version: str = proto.Field(
        proto.STRING,
        number=17,
        oneof="key_store_password_options",
    )
    technology_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    servers: str = proto.Field(
        proto.STRING,
        number=2,
    )
    security_protocol: RedisSecurityProtocol = proto.Field(
        proto.ENUM,
        number=3,
        enum=RedisSecurityProtocol,
    )
    authentication_type: RedisAuthenticationType = proto.Field(
        proto.ENUM,
        number=4,
        enum=RedisAuthenticationType,
    )
    username: str = proto.Field(
        proto.STRING,
        number=5,
    )
    redis_cluster_id: str = proto.Field(
        proto.STRING,
        number=7,
    )
    trust_store_file: str = proto.Field(
        proto.STRING,
        number=8,
    )
    key_store_file: str = proto.Field(
        proto.STRING,
        number=10,
    )


class GoldengateDatabricksConnectionProperties(proto.Message):
    r"""The properties of GoldengateDatabricksConnection.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        password (str):
            Optional. Input only. The password used to
            connect to Databricks in plain text.

            This field is a member of `oneof`_ ``connection_password_options``.
        password_secret_version (str):
            Optional. Input only. The resource name of a
            secret version in Secret Manager which contains
            the password used to connect to Databricks.
            Format:
            projects/{project}/secrets/{secret}/versions/{version}.

            This field is a member of `oneof`_ ``connection_password_options``.
        technology_type (str):
            Optional. The technology type of
            DatabricksConnection.
        authentication_type (google.cloud.oracledatabase_v1.types.GoldengateDatabricksConnectionProperties.DatabricksAuthenticationType):
            Optional. Authentication type for Databricks.
        connection_url (str):
            Optional. Connection URL.
            e.g.:

            'jdbc:databricks://adb-33934.4.azuredatabricks.net:443/default;transportMode=http;ssl=1;httpPath=sql/protocolv1/o/3393########44/0##3-7-hlrb'
        client_id (str):
            Optional. OAuth client id, only applicable for
            authentication_type == OAUTH_M2M
        client_secret (str):
            Optional. OAuth client secret, only applicable for
            authentication_type == OAUTH_M2M
        storage_credential (str):
            Optional. External storage credential name to
            access files on object storage such as ADLS
            Gen2, S3 or Cloud Storage.
    """

    class DatabricksAuthenticationType(proto.Enum):
        r"""Enum for authentication type for Databricks.

        Values:
            DATABRICKS_AUTHENTICATION_TYPE_UNSPECIFIED (0):
                Authentication type not specified.
            PERSONAL_ACCESS_TOKEN (1):
                Personal access token authentication.
            OAUTH_M2M (2):
                OAuth M2M authentication.
        """

        DATABRICKS_AUTHENTICATION_TYPE_UNSPECIFIED = 0
        PERSONAL_ACCESS_TOKEN = 1
        OAUTH_M2M = 2

    password: str = proto.Field(
        proto.STRING,
        number=8,
        oneof="connection_password_options",
    )
    password_secret_version: str = proto.Field(
        proto.STRING,
        number=9,
        oneof="connection_password_options",
    )
    technology_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    authentication_type: DatabricksAuthenticationType = proto.Field(
        proto.ENUM,
        number=2,
        enum=DatabricksAuthenticationType,
    )
    connection_url: str = proto.Field(
        proto.STRING,
        number=3,
    )
    client_id: str = proto.Field(
        proto.STRING,
        number=5,
    )
    client_secret: str = proto.Field(
        proto.STRING,
        number=6,
    )
    storage_credential: str = proto.Field(
        proto.STRING,
        number=7,
    )


class GoldengateGooglePubsubConnectionProperties(proto.Message):
    r"""The properties of GoldengateGooglePubsubConnection.

    Attributes:
        technology_type (str):
            Optional. The technology type of
            GooglePubsubConnection.
        service_account_key_file (str):
            Optional. The base64 encoded content of the
            service account key file containing the
            credentials required to use Google Pub/Sub.
    """

    technology_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    service_account_key_file: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GoldengateMicrosoftFabricConnectionProperties(proto.Message):
    r"""The properties of GoldengateMicrosoftFabricConnection.

    Attributes:
        technology_type (str):
            Optional. The technology type of
            MicrosoftFabricConnection.
        tenant_id (str):
            Optional. Azure tenant ID of the application.
        client_id (str):
            Optional. Azure client ID of the application.
        client_secret (str):
            Optional. Client secret associated with the
            client id.
        endpoint (str):
            Optional. Optional Microsoft Fabric service
            endpoint. Default value:
            https://onelake.dfs.fabric.microsoft.com
    """

    technology_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    tenant_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    client_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    client_secret: str = proto.Field(
        proto.STRING,
        number=4,
    )
    endpoint: str = proto.Field(
        proto.STRING,
        number=5,
    )


class GoldengateOracleAIDataPlatformConnectionProperties(proto.Message):
    r"""The properties of GoldengateOracleAIDataPlatformConnection.

    Attributes:
        technology_type (str):
            Optional. The technology type of
            OracleAiDataPlatformConnection.
        connection_url (str):
            Optional. Connection URL. It must start with
            'jdbc:spark://'
        tenancy_id (str):
            Optional. The OCID of the related OCI
            tenancy.
        region (str):
            Optional. The name of the region. e.g.:
            us-ashburn-1
        user_id (str):
            Optional. The OCID of the OCI user who will
            access.
        private_key_file (str):
            Optional. The content of the private key file
            (PEM file) corresponding to the API key of the
            fingerprint.
        private_key_passphrase_secret (str):
            Optional. The passphrase of the private key.
        public_key_fingerprint (str):
            Optional. The fingerprint of the API Key of the user
            specified by the user_id.
        use_resource_principal (bool):
            Optional. Specifies that the user intends to
            authenticate to the instance using a resource
            principal.
    """

    technology_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    connection_url: str = proto.Field(
        proto.STRING,
        number=2,
    )
    tenancy_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    region: str = proto.Field(
        proto.STRING,
        number=4,
    )
    user_id: str = proto.Field(
        proto.STRING,
        number=5,
    )
    private_key_file: str = proto.Field(
        proto.STRING,
        number=6,
    )
    private_key_passphrase_secret: str = proto.Field(
        proto.STRING,
        number=7,
    )
    public_key_fingerprint: str = proto.Field(
        proto.STRING,
        number=8,
    )
    use_resource_principal: bool = proto.Field(
        proto.BOOL,
        number=9,
    )


class GlueIcebergCatalog(proto.Message):
    r"""The Glue Iceberg catalog.

    Attributes:
        glue_id (str):
            Required. The catalog ID of Glue.
    """

    glue_id: str = proto.Field(
        proto.STRING,
        number=1,
    )


class NessieIcebergCatalog(proto.Message):
    r"""The Nessie Iceberg catalog.

    Attributes:
        uri (str):
            Required. The Nessie uri.
        branch (str):
            Required. The Nessie branch.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    branch: str = proto.Field(
        proto.STRING,
        number=2,
    )


class PolarisIcebergCatalog(proto.Message):
    r"""The Polaris Iceberg catalog.

    Attributes:
        uri (str):
            Required. The Polaris uri.
        polaris_catalog (str):
            Required. The catalog name within Polaris.
        client_id (str):
            Required. The Polaris client ID.
        principal_role (str):
            Required. The Polaris principal role.
        client_secret (str):
            Optional. The Polaris client secret.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    polaris_catalog: str = proto.Field(
        proto.STRING,
        number=2,
    )
    client_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    principal_role: str = proto.Field(
        proto.STRING,
        number=4,
    )
    client_secret: str = proto.Field(
        proto.STRING,
        number=5,
    )


class RestIcebergCatalog(proto.Message):
    r"""The REST Iceberg catalog.

    Attributes:
        uri (str):
            Required. The REST uri.
        properties (str):
            Optional. The base64 encoded content of the
            configuration file containing additional
            properties for the REST catalog.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    properties: str = proto.Field(
        proto.STRING,
        number=2,
    )


class IcebergCatalog(proto.Message):
    r"""The Iceberg catalog details.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        glue_iceberg_catalog (google.cloud.oracledatabase_v1.types.GlueIcebergCatalog):
            The Glue Iceberg catalog.

            This field is a member of `oneof`_ ``catalog_details``.
        nessie_iceberg_catalog (google.cloud.oracledatabase_v1.types.NessieIcebergCatalog):
            The Nessie Iceberg catalog.

            This field is a member of `oneof`_ ``catalog_details``.
        polaris_iceberg_catalog (google.cloud.oracledatabase_v1.types.PolarisIcebergCatalog):
            The Polaris Iceberg catalog.

            This field is a member of `oneof`_ ``catalog_details``.
        rest_iceberg_catalog (google.cloud.oracledatabase_v1.types.RestIcebergCatalog):
            The REST Iceberg catalog.

            This field is a member of `oneof`_ ``catalog_details``.
        catalog_type (google.cloud.oracledatabase_v1.types.IcebergCatalog.CatalogType):
            Required. The type of Iceberg catalog.
    """

    class CatalogType(proto.Enum):
        r"""The type of Iceberg catalog.

        Values:
            CATALOG_TYPE_UNSPECIFIED (0):
                Catalog type not specified.
            GLUE (1):
                Glue catalog.
            HADOOP (2):
                Hadoop catalog.
            NESSIE (3):
                Nessie catalog.
            POLARIS (4):
                Polaris catalog.
            REST (5):
                REST catalog.
        """

        CATALOG_TYPE_UNSPECIFIED = 0
        GLUE = 1
        HADOOP = 2
        NESSIE = 3
        POLARIS = 4
        REST = 5

    glue_iceberg_catalog: "GlueIcebergCatalog" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="catalog_details",
        message="GlueIcebergCatalog",
    )
    nessie_iceberg_catalog: "NessieIcebergCatalog" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="catalog_details",
        message="NessieIcebergCatalog",
    )
    polaris_iceberg_catalog: "PolarisIcebergCatalog" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="catalog_details",
        message="PolarisIcebergCatalog",
    )
    rest_iceberg_catalog: "RestIcebergCatalog" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="catalog_details",
        message="RestIcebergCatalog",
    )
    catalog_type: CatalogType = proto.Field(
        proto.ENUM,
        number=6,
        enum=CatalogType,
    )


class AmazonS3IcebergStorage(proto.Message):
    r"""The Amazon S3 Iceberg storage.

    Attributes:
        scheme_type (google.cloud.oracledatabase_v1.types.AmazonS3IcebergStorage.SchemeType):
            Required. The scheme type of Amazon S3.
        access_key_id (str):
            Required. The access key ID of Amazon S3.
        region (str):
            Required. The region of Amazon S3.
        bucket (str):
            Required. The bucket of Amazon S3.
        endpoint (str):
            Optional. The endpoint of Amazon S3.
        secret_access_key_secret (str):
            Optional. The secret access key of Amazon S3.
    """

    class SchemeType(proto.Enum):
        r"""Enum for scheme type of Amazon S3.

        Values:
            SCHEME_TYPE_UNSPECIFIED (0):
                Scheme type not specified.
            S3 (1):
                S3 scheme.
            S3A (2):
                S3A scheme.
        """

        SCHEME_TYPE_UNSPECIFIED = 0
        S3 = 1
        S3A = 2

    scheme_type: SchemeType = proto.Field(
        proto.ENUM,
        number=1,
        enum=SchemeType,
    )
    access_key_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    region: str = proto.Field(
        proto.STRING,
        number=3,
    )
    bucket: str = proto.Field(
        proto.STRING,
        number=4,
    )
    endpoint: str = proto.Field(
        proto.STRING,
        number=5,
    )
    secret_access_key_secret: str = proto.Field(
        proto.STRING,
        number=6,
    )


class GoogleCloudStorageIcebergStorage(proto.Message):
    r"""The Google Cloud Storage Iceberg storage.

    Attributes:
        bucket (str):
            Required. The bucket of Google Cloud Storage.
        project_id (str):
            Required. The project ID of Google Cloud
            Storage.
        service_account_key_file (str):
            Optional. The base64 encoded content of the
            service account key file of Google Cloud
            Storage.
    """

    bucket: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    service_account_key_file: str = proto.Field(
        proto.STRING,
        number=3,
    )


class AzureDataLakeStorageIcebergStorage(proto.Message):
    r"""The Azure Data Lake Storage Iceberg storage.

    Attributes:
        azure_account (str):
            Required. The account of Azure Data Lake
            Storage.
        container (str):
            Required. The container of Azure Data Lake
            Storage.
        account_key_secret (str):
            Optional. The account key of Azure Data Lake
            Storage.
        endpoint (str):
            Optional. The endpoint of Azure Data Lake
            Storage.
    """

    azure_account: str = proto.Field(
        proto.STRING,
        number=1,
    )
    container: str = proto.Field(
        proto.STRING,
        number=2,
    )
    account_key_secret: str = proto.Field(
        proto.STRING,
        number=3,
    )
    endpoint: str = proto.Field(
        proto.STRING,
        number=4,
    )


class IcebergStorage(proto.Message):
    r"""The Iceberg storage details.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        amazon_s3_iceberg_storage (google.cloud.oracledatabase_v1.types.AmazonS3IcebergStorage):
            The Amazon S3 Iceberg storage.

            This field is a member of `oneof`_ ``storage_details``.
        google_cloud_storage_iceberg_storage (google.cloud.oracledatabase_v1.types.GoogleCloudStorageIcebergStorage):
            The Google Cloud Storage Iceberg storage.

            This field is a member of `oneof`_ ``storage_details``.
        azure_data_lake_storage_iceberg_storage (google.cloud.oracledatabase_v1.types.AzureDataLakeStorageIcebergStorage):
            The Azure Data Lake Storage Iceberg storage.

            This field is a member of `oneof`_ ``storage_details``.
        storage_type (google.cloud.oracledatabase_v1.types.IcebergStorage.StorageType):
            Required. The type of Iceberg storage.
    """

    class StorageType(proto.Enum):
        r"""The type of Iceberg storage.

        Values:
            STORAGE_TYPE_UNSPECIFIED (0):
                Storage type not specified.
            AMAZON_S3 (1):
                Amazon S3 storage.
            GOOGLE_CLOUD_STORAGE (2):
                Google Cloud Storage storage.
            AZURE_DATA_LAKE_STORAGE (3):
                Azure Data Lake Storage storage.
        """

        STORAGE_TYPE_UNSPECIFIED = 0
        AMAZON_S3 = 1
        GOOGLE_CLOUD_STORAGE = 2
        AZURE_DATA_LAKE_STORAGE = 3

    amazon_s3_iceberg_storage: "AmazonS3IcebergStorage" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="storage_details",
        message="AmazonS3IcebergStorage",
    )
    google_cloud_storage_iceberg_storage: "GoogleCloudStorageIcebergStorage" = (
        proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="storage_details",
            message="GoogleCloudStorageIcebergStorage",
        )
    )
    azure_data_lake_storage_iceberg_storage: "AzureDataLakeStorageIcebergStorage" = (
        proto.Field(
            proto.MESSAGE,
            number=3,
            oneof="storage_details",
            message="AzureDataLakeStorageIcebergStorage",
        )
    )
    storage_type: StorageType = proto.Field(
        proto.ENUM,
        number=4,
        enum=StorageType,
    )


class GoldengateIcebergConnectionProperties(proto.Message):
    r"""The properties of GoldengateIcebergConnection.

    Attributes:
        technology_type (str):
            Required. The technology type of Iceberg
            connection.
        catalog (google.cloud.oracledatabase_v1.types.IcebergCatalog):
            Required. The Iceberg catalog.
        storage (google.cloud.oracledatabase_v1.types.IcebergStorage):
            Required. The Iceberg storage.
    """

    technology_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    catalog: "IcebergCatalog" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="IcebergCatalog",
    )
    storage: "IcebergStorage" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="IcebergStorage",
    )


class CreateGoldengateConnectionRequest(proto.Message):
    r"""The request for ``GoldengateConnection.Create``.

    Attributes:
        parent (str):
            Required. The value for parent of the
            GoldengateConnection in the following format:
            projects/{project}/locations/{location}.
        goldengate_connection_id (str):
            Required. The ID of the GoldengateConnection to create. This
            value is restricted to
            (^\ `a-z <[a-z0-9-]{0,61}[a-z0-9]>`__?$) and must be a
            maximum of 63 characters in length. The value must start
            with a letter and end with a letter or a number.
        goldengate_connection (google.cloud.oracledatabase_v1.types.GoldengateConnection):
            Required. The resource being created.
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
    goldengate_connection_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    goldengate_connection: "GoldengateConnection" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="GoldengateConnection",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteGoldengateConnectionRequest(proto.Message):
    r"""The request for ``GoldengateConnection.Delete``.

    Attributes:
        name (str):
            Required. The name of the GoldengateConnection in the
            following format:
            projects/{project}/locations/{location}/goldengateConnections/{goldengate_connection}.
        request_id (str):
            Optional. An optional ID to identify the
            request. This value is used to identify
            duplicate requests. If you make a request with
            the same request ID and the original request is
            still in progress or completed, the server
            ignores the second request. This prevents
            clients from accidentally creating duplicate
            commitments.

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


class GetGoldengateConnectionRequest(proto.Message):
    r"""The request for ``GoldengateConnection.Get``.

    Attributes:
        name (str):
            Required. The name of the GoldengateConnection in the
            following format:
            projects/{project}/locations/{location}/goldengateConnections/{goldengate_connection}.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListGoldengateConnectionsRequest(proto.Message):
    r"""The request for ``GoldengateConnection.List``.

    Attributes:
        parent (str):
            Required. The parent value for
            GoldengateConnections in the following format:
            projects/{project}/locations/{location}.
        page_size (int):
            Optional. The maximum number of items to
            return. If unspecified, at most 50
            GoldengateConnections will be returned. The
            maximum value is 1000; values above 1000 will be
            coerced to 1000.
        page_token (str):
            Optional. A page token, received from a
            previous ListGoldengateConnections call. Provide
            this to retrieve the subsequent page.
        filter (str):
            Optional. An expression for filtering the
            results of the request.
        order_by (str):
            Optional. An expression for ordering the
            results of the request.
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


class ListGoldengateConnectionsResponse(proto.Message):
    r"""The response for ``GoldengateConnection.List``.

    Attributes:
        goldengate_connections (MutableSequence[google.cloud.oracledatabase_v1.types.GoldengateConnection]):
            The list of GoldengateConnections.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Optional. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    goldengate_connections: MutableSequence["GoldengateConnection"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="GoldengateConnection",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class NameValuePair(proto.Message):
    r"""A name-value pair representing an attribute entry usable in a
    list of attributes.

    Attributes:
        key (str):
            Required. The name of the property entry.
        value (str):
            Required. The value of the property entry.
    """

    key: str = proto.Field(
        proto.STRING,
        number=1,
    )
    value: str = proto.Field(
        proto.STRING,
        number=2,
    )


class KafkaBootstrapServer(proto.Message):
    r"""Represents a Kafka bootstrap server with host name, optional
    port defaults to 9092, and an optional private ip.

    Attributes:
        host (str):
            Required. The name or address of a host.
        port (int):
            Optional. The port of an endpoint usually
            specified for a connection.
        private_ip_address (str):
            Optional. The private IP address of the
            connection's endpoint in the customer's VCN,
            typically a database endpoint or a big data
            endpoint (e.g. Kafka bootstrap server). In case
            the privateIp is provided, the subnetId must
            also be provided. In case the privateIp (and the
            subnetId) is not provided it is assumed the
            datasource is publicly accessible. In case the
            connection is accessible only privately, the
            lack of privateIp will result in not being able
            to access the connection.
    """

    host: str = proto.Field(
        proto.STRING,
        number=1,
    )
    port: int = proto.Field(
        proto.INT32,
        number=2,
    )
    private_ip_address: str = proto.Field(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
