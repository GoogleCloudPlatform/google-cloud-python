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
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.bigquery.connection.v1",
    manifest={
        "CreateConnectionRequest",
        "GetConnectionRequest",
        "ListConnectionsRequest",
        "ListConnectionsResponse",
        "UpdateConnectionRequest",
        "DeleteConnectionRequest",
        "Connection",
        "CloudSqlProperties",
        "CloudSqlCredential",
        "CloudSpannerProperties",
        "AwsProperties",
        "AwsCrossAccountRole",
        "AwsAccessRole",
        "AzureProperties",
        "CloudResourceProperties",
        "MetastoreServiceConfig",
        "SparkHistoryServerConfig",
        "SparkProperties",
        "SalesforceDataCloudProperties",
    },
)


class CreateConnectionRequest(proto.Message):
    r"""The request for
    [ConnectionService.CreateConnection][google.cloud.bigquery.connection.v1.ConnectionService.CreateConnection].

    Attributes:
        parent (str):
            Required. Parent resource name. Must be in the format
            ``projects/{project_id}/locations/{location_id}``
        connection_id (str):
            Optional. Connection id that should be
            assigned to the created connection.
        connection (google.cloud.bigquery_connection_v1.types.Connection):
            Required. Connection to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    connection_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    connection: "Connection" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Connection",
    )


class GetConnectionRequest(proto.Message):
    r"""The request for
    [ConnectionService.GetConnection][google.cloud.bigquery.connection.v1.ConnectionService.GetConnection].

    Attributes:
        name (str):
            Required. Name of the requested connection, for example:
            ``projects/{project_id}/locations/{location_id}/connections/{connection_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListConnectionsRequest(proto.Message):
    r"""The request for
    [ConnectionService.ListConnections][google.cloud.bigquery.connection.v1.ConnectionService.ListConnections].

    Attributes:
        parent (str):
            Required. Parent resource name. Must be in the form:
            ``projects/{project_id}/locations/{location_id}``
        page_size (int):
            Required. Page size.
        page_token (str):
            Page token.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=4,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListConnectionsResponse(proto.Message):
    r"""The response for
    [ConnectionService.ListConnections][google.cloud.bigquery.connection.v1.ConnectionService.ListConnections].

    Attributes:
        next_page_token (str):
            Next page token.
        connections (MutableSequence[google.cloud.bigquery_connection_v1.types.Connection]):
            List of connections.
    """

    @property
    def raw_page(self):
        return self

    next_page_token: str = proto.Field(
        proto.STRING,
        number=1,
    )
    connections: MutableSequence["Connection"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Connection",
    )


class UpdateConnectionRequest(proto.Message):
    r"""The request for
    [ConnectionService.UpdateConnection][google.cloud.bigquery.connection.v1.ConnectionService.UpdateConnection].

    Attributes:
        name (str):
            Required. Name of the connection to update, for example:
            ``projects/{project_id}/locations/{location_id}/connections/{connection_id}``
        connection (google.cloud.bigquery_connection_v1.types.Connection):
            Required. Connection containing the updated
            fields.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Update mask for the connection
            fields to be updated.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    connection: "Connection" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Connection",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=3,
        message=field_mask_pb2.FieldMask,
    )


class DeleteConnectionRequest(proto.Message):
    r"""The request for [ConnectionService.DeleteConnectionRequest][].

    Attributes:
        name (str):
            Required. Name of the deleted connection, for example:
            ``projects/{project_id}/locations/{location_id}/connections/{connection_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Connection(proto.Message):
    r"""Configuration parameters to establish connection with an
    external data source, except the credential attributes.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            The resource name of the connection in the form of:
            ``projects/{project_id}/locations/{location_id}/connections/{connection_id}``
        friendly_name (str):
            User provided display name for the
            connection.
        description (str):
            User provided description.
        cloud_sql (google.cloud.bigquery_connection_v1.types.CloudSqlProperties):
            Cloud SQL properties.

            This field is a member of `oneof`_ ``properties``.
        aws (google.cloud.bigquery_connection_v1.types.AwsProperties):
            Amazon Web Services (AWS) properties.

            This field is a member of `oneof`_ ``properties``.
        azure (google.cloud.bigquery_connection_v1.types.AzureProperties):
            Azure properties.

            This field is a member of `oneof`_ ``properties``.
        cloud_spanner (google.cloud.bigquery_connection_v1.types.CloudSpannerProperties):
            Cloud Spanner properties.

            This field is a member of `oneof`_ ``properties``.
        cloud_resource (google.cloud.bigquery_connection_v1.types.CloudResourceProperties):
            Cloud Resource properties.

            This field is a member of `oneof`_ ``properties``.
        spark (google.cloud.bigquery_connection_v1.types.SparkProperties):
            Spark properties.

            This field is a member of `oneof`_ ``properties``.
        salesforce_data_cloud (google.cloud.bigquery_connection_v1.types.SalesforceDataCloudProperties):
            Optional. Salesforce DataCloud properties.
            This field is intended for use only by
            Salesforce partner projects. This field contains
            properties for your Salesforce DataCloud
            connection.

            This field is a member of `oneof`_ ``properties``.
        creation_time (int):
            Output only. The creation timestamp of the
            connection.
        last_modified_time (int):
            Output only. The last update timestamp of the
            connection.
        has_credential (bool):
            Output only. True, if credential is
            configured for this connection.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    friendly_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    cloud_sql: "CloudSqlProperties" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="properties",
        message="CloudSqlProperties",
    )
    aws: "AwsProperties" = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="properties",
        message="AwsProperties",
    )
    azure: "AzureProperties" = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="properties",
        message="AzureProperties",
    )
    cloud_spanner: "CloudSpannerProperties" = proto.Field(
        proto.MESSAGE,
        number=21,
        oneof="properties",
        message="CloudSpannerProperties",
    )
    cloud_resource: "CloudResourceProperties" = proto.Field(
        proto.MESSAGE,
        number=22,
        oneof="properties",
        message="CloudResourceProperties",
    )
    spark: "SparkProperties" = proto.Field(
        proto.MESSAGE,
        number=23,
        oneof="properties",
        message="SparkProperties",
    )
    salesforce_data_cloud: "SalesforceDataCloudProperties" = proto.Field(
        proto.MESSAGE,
        number=24,
        oneof="properties",
        message="SalesforceDataCloudProperties",
    )
    creation_time: int = proto.Field(
        proto.INT64,
        number=5,
    )
    last_modified_time: int = proto.Field(
        proto.INT64,
        number=6,
    )
    has_credential: bool = proto.Field(
        proto.BOOL,
        number=7,
    )


class CloudSqlProperties(proto.Message):
    r"""Connection properties specific to the Cloud SQL.

    Attributes:
        instance_id (str):
            Cloud SQL instance ID in the form
            ``project:location:instance``.
        database (str):
            Database name.
        type_ (google.cloud.bigquery_connection_v1.types.CloudSqlProperties.DatabaseType):
            Type of the Cloud SQL database.
        credential (google.cloud.bigquery_connection_v1.types.CloudSqlCredential):
            Input only. Cloud SQL credential.
        service_account_id (str):
            Output only. The account ID of the service
            used for the purpose of this connection.

            When the connection is used in the context of an
            operation in BigQuery, this service account will
            serve as the identity being used for connecting
            to the CloudSQL instance specified in this
            connection.
    """

    class DatabaseType(proto.Enum):
        r"""Supported Cloud SQL database types.

        Values:
            DATABASE_TYPE_UNSPECIFIED (0):
                Unspecified database type.
            POSTGRES (1):
                Cloud SQL for PostgreSQL.
            MYSQL (2):
                Cloud SQL for MySQL.
        """

        DATABASE_TYPE_UNSPECIFIED = 0
        POSTGRES = 1
        MYSQL = 2

    instance_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    database: str = proto.Field(
        proto.STRING,
        number=2,
    )
    type_: DatabaseType = proto.Field(
        proto.ENUM,
        number=3,
        enum=DatabaseType,
    )
    credential: "CloudSqlCredential" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="CloudSqlCredential",
    )
    service_account_id: str = proto.Field(
        proto.STRING,
        number=5,
    )


class CloudSqlCredential(proto.Message):
    r"""Credential info for the Cloud SQL.

    Attributes:
        username (str):
            The username for the credential.
        password (str):
            The password for the credential.
    """

    username: str = proto.Field(
        proto.STRING,
        number=1,
    )
    password: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CloudSpannerProperties(proto.Message):
    r"""Connection properties specific to Cloud Spanner.

    Attributes:
        database (str):
            Cloud Spanner database in the form
            \`project/instance/database'
        use_parallelism (bool):
            If parallelism should be used when reading
            from Cloud Spanner
        max_parallelism (int):
            Allows setting max parallelism per query when executing on
            Spanner independent compute resources. If unspecified,
            default values of parallelism are chosen that are dependent
            on the Cloud Spanner instance configuration.

            REQUIRES: ``use_parallelism`` must be set. REQUIRES: Either
            ``use_data_boost`` or ``use_serverless_analytics`` must be
            set.
        use_serverless_analytics (bool):
            If the serverless analytics service should be used to read
            data from Cloud Spanner. Note: ``use_parallelism`` must be
            set when using serverless analytics.
        use_data_boost (bool):
            If set, the request will be executed via Spanner independent
            compute resources. REQUIRES: ``use_parallelism`` must be
            set.

            NOTE: ``use_serverless_analytics`` will be deprecated.
            Prefer ``use_data_boost`` over ``use_serverless_analytics``.
        database_role (str):
            Optional. Cloud Spanner database role for fine-grained
            access control. The Cloud Spanner admin should have
            provisioned the database role with appropriate permissions,
            such as ``SELECT`` and ``INSERT``. Other users should only
            use roles provided by their Cloud Spanner admins.

            For more details, see [About fine-grained access control]
            (https://cloud.google.com/spanner/docs/fgac-about).

            REQUIRES: The database role name must start with a letter,
            and can only contain letters, numbers, and underscores.
    """

    database: str = proto.Field(
        proto.STRING,
        number=1,
    )
    use_parallelism: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    max_parallelism: int = proto.Field(
        proto.INT32,
        number=5,
    )
    use_serverless_analytics: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    use_data_boost: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    database_role: str = proto.Field(
        proto.STRING,
        number=4,
    )


class AwsProperties(proto.Message):
    r"""Connection properties specific to Amazon Web Services (AWS).

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        cross_account_role (google.cloud.bigquery_connection_v1.types.AwsCrossAccountRole):
            Authentication using Google owned AWS IAM
            user's access key to assume into customer's AWS
            IAM Role. Deprecated, do not use.

            This field is a member of `oneof`_ ``authentication_method``.
        access_role (google.cloud.bigquery_connection_v1.types.AwsAccessRole):
            Authentication using Google owned service
            account to assume into customer's AWS IAM Role.

            This field is a member of `oneof`_ ``authentication_method``.
    """

    cross_account_role: "AwsCrossAccountRole" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="authentication_method",
        message="AwsCrossAccountRole",
    )
    access_role: "AwsAccessRole" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="authentication_method",
        message="AwsAccessRole",
    )


class AwsCrossAccountRole(proto.Message):
    r"""Authentication method for Amazon Web Services (AWS) that uses
    Google owned AWS IAM user's access key to assume into customer's
    AWS IAM Role.

    Attributes:
        iam_role_id (str):
            The user’s AWS IAM Role that trusts the
            Google-owned AWS IAM user Connection.
        iam_user_id (str):
            Output only. Google-owned AWS IAM User for a
            Connection.
        external_id (str):
            Output only. A Google-generated id for representing
            Connection’s identity in AWS. External Id is also used for
            preventing the Confused Deputy Problem. See
            https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html
    """

    iam_role_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    iam_user_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    external_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class AwsAccessRole(proto.Message):
    r"""Authentication method for Amazon Web Services (AWS) that uses
    Google owned Google service account to assume into customer's
    AWS IAM Role.

    Attributes:
        iam_role_id (str):
            The user’s AWS IAM Role that trusts the
            Google-owned AWS IAM user Connection.
        identity (str):
            A unique Google-owned and Google-generated
            identity for the Connection. This identity will
            be used to access the user's AWS IAM Role.
    """

    iam_role_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    identity: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AzureProperties(proto.Message):
    r"""Container for connection properties specific to Azure.

    Attributes:
        application (str):
            Output only. The name of the Azure Active
            Directory Application.
        client_id (str):
            Output only. The client id of the Azure
            Active Directory Application.
        object_id (str):
            Output only. The object id of the Azure
            Active Directory Application.
        customer_tenant_id (str):
            The id of customer's directory that host the
            data.
        redirect_uri (str):
            The URL user will be redirected to after
            granting consent during connection setup.
        federated_application_client_id (str):
            The client ID of the user's Azure Active
            Directory Application used for a federated
            connection.
        identity (str):
            Output only. A unique Google-owned and
            Google-generated identity for the Connection.
            This identity will be used to access the user's
            Azure Active Directory Application.
    """

    application: str = proto.Field(
        proto.STRING,
        number=1,
    )
    client_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    object_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    customer_tenant_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    redirect_uri: str = proto.Field(
        proto.STRING,
        number=5,
    )
    federated_application_client_id: str = proto.Field(
        proto.STRING,
        number=6,
    )
    identity: str = proto.Field(
        proto.STRING,
        number=7,
    )


class CloudResourceProperties(proto.Message):
    r"""Container for connection properties for delegation of access
    to GCP resources.

    Attributes:
        service_account_id (str):
            Output only. The account ID of the service
            created for the purpose of this connection.

            The service account does not have any
            permissions associated with it when it is
            created. After creation, customers delegate
            permissions to the service account. When the
            connection is used in the context of an
            operation in BigQuery, the service account will
            be used to connect to the desired resources in
            GCP.

            The account ID is in the form of:

            <service-1234>@gcp-sa-bigquery-cloudresource.iam.gserviceaccount.com
    """

    service_account_id: str = proto.Field(
        proto.STRING,
        number=1,
    )


class MetastoreServiceConfig(proto.Message):
    r"""Configuration of the Dataproc Metastore Service.

    Attributes:
        metastore_service (str):
            Optional. Resource name of an existing Dataproc Metastore
            service.

            Example:

            - ``projects/[project_id]/locations/[region]/services/[service_id]``
    """

    metastore_service: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SparkHistoryServerConfig(proto.Message):
    r"""Configuration of the Spark History Server.

    Attributes:
        dataproc_cluster (str):
            Optional. Resource name of an existing Dataproc Cluster to
            act as a Spark History Server for the connection.

            Example:

            - ``projects/[project_id]/regions/[region]/clusters/[cluster_name]``
    """

    dataproc_cluster: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SparkProperties(proto.Message):
    r"""Container for connection properties to execute stored
    procedures for Apache Spark.

    Attributes:
        service_account_id (str):
            Output only. The account ID of the service
            created for the purpose of this connection.

            The service account does not have any
            permissions associated with it when it is
            created. After creation, customers delegate
            permissions to the service account. When the
            connection is used in the context of a stored
            procedure for Apache Spark in BigQuery, the
            service account is used to connect to the
            desired resources in Google Cloud.

            The account ID is in the form of:

            bqcx-<projectnumber>-<uniqueid>@gcp-sa-bigquery-consp.iam.gserviceaccount.com
        metastore_service_config (google.cloud.bigquery_connection_v1.types.MetastoreServiceConfig):
            Optional. Dataproc Metastore Service
            configuration for the connection.
        spark_history_server_config (google.cloud.bigquery_connection_v1.types.SparkHistoryServerConfig):
            Optional. Spark History Server configuration
            for the connection.
    """

    service_account_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    metastore_service_config: "MetastoreServiceConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="MetastoreServiceConfig",
    )
    spark_history_server_config: "SparkHistoryServerConfig" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="SparkHistoryServerConfig",
    )


class SalesforceDataCloudProperties(proto.Message):
    r"""Connection properties specific to Salesforce DataCloud. This
    is intended for use only by Salesforce partner projects.

    Attributes:
        instance_uri (str):
            The URL to the user's Salesforce DataCloud
            instance.
        identity (str):
            Output only. A unique Google-owned and
            Google-generated service account identity for
            the connection.
        tenant_id (str):
            The ID of the user's Salesforce tenant.
    """

    instance_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    identity: str = proto.Field(
        proto.STRING,
        number=2,
    )
    tenant_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
