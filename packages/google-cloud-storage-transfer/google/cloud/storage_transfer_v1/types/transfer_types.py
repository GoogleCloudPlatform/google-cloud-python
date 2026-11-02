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
import google.rpc.code_pb2 as code_pb2  # type: ignore
import google.type.date_pb2 as date_pb2  # type: ignore
import google.type.timeofday_pb2 as timeofday_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.storagetransfer.v1",
    manifest={
        "GoogleServiceAccount",
        "AwsAccessKey",
        "AzureCredentials",
        "ObjectConditions",
        "GcsData",
        "AwsS3Data",
        "AzureBlobStorageData",
        "HttpData",
        "PosixFilesystem",
        "HdfsData",
        "AwsS3CompatibleData",
        "S3CompatibleMetadata",
        "AgentPool",
        "TransferOptions",
        "TransferSpec",
        "ReplicationSpec",
        "MetadataOptions",
        "TransferManifest",
        "Schedule",
        "EventStream",
        "TransferJob",
        "ErrorLogEntry",
        "ErrorSummary",
        "TransferCounters",
        "NotificationConfig",
        "LoggingConfig",
        "TransferOperation",
    },
)


class GoogleServiceAccount(proto.Message):
    r"""Google service account

    Attributes:
        account_email (str):
            Email address of the service account.
        subject_id (str):
            Unique identifier for the service account.
    """

    account_email: str = proto.Field(
        proto.STRING,
        number=1,
    )
    subject_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AwsAccessKey(proto.Message):
    r"""AWS access key (see `AWS Security
    Credentials <https://docs.aws.amazon.com/general/latest/gr/aws-security-credentials.html>`__).

    For information on our data retention policy for user credentials,
    see `User
    credentials </storage-transfer/docs/data-retention#user-credentials>`__.

    Attributes:
        access_key_id (str):
            Required. AWS access key ID.
        secret_access_key (str):
            Required. AWS secret access key. This field
            is not returned in RPC responses.
    """

    access_key_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    secret_access_key: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AzureCredentials(proto.Message):
    r"""Azure credentials

    For information on our data retention policy for user credentials,
    see `User
    credentials </storage-transfer/docs/data-retention#user-credentials>`__.

    Attributes:
        sas_token (str):
            Required. Azure shared access signature (SAS).

            For more information about SAS, see `Grant limited access to
            Azure Storage resources using shared access signatures
            (SAS) <https://docs.microsoft.com/en-us/azure/storage/common/storage-sas-overview>`__.
    """

    sas_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ObjectConditions(proto.Message):
    r"""Conditions that determine which objects are transferred. Applies
    only to Cloud Data Sources such as S3, Azure, and Cloud Storage.

    The "last modification time" refers to the time of the last change
    to the object's content or metadata — specifically, this is the
    ``updated`` property of Cloud Storage objects, the ``LastModified``
    field of S3 objects, and the ``Last-Modified`` header of Azure
    blobs.

    For S3 objects, the ``LastModified`` value is the time the object
    begins uploading. If the object meets your "last modification time"
    criteria, but has not finished uploading, the object is not
    transferred. See `Transfer from Amazon S3 to Cloud
    Storage <https://cloud.google.com/storage-transfer/docs/create-transfers/agentless/s3#transfer_options>`__
    for more information.

    Transfers with a
    [PosixFilesystem][google.storagetransfer.v1.PosixFilesystem] source
    or destination don't support ``ObjectConditions``.

    Attributes:
        min_time_elapsed_since_last_modification (google.protobuf.duration_pb2.Duration):
            Ensures that objects are not transferred until a specific
            minimum time has elapsed after the "last modification time".
            When a
            [TransferOperation][google.storagetransfer.v1.TransferOperation]
            begins, objects with a "last modification time" are
            transferred only if the elapsed time between the
            [start_time][google.storagetransfer.v1.TransferOperation.start_time]
            of the ``TransferOperation`` and the "last modification
            time" of the object is equal to or greater than the value of
            min_time_elapsed_since_last_modification\`. Objects that do
            not have a "last modification time" are also transferred.
        max_time_elapsed_since_last_modification (google.protobuf.duration_pb2.Duration):
            Ensures that objects are not transferred if a specific
            maximum time has elapsed since the "last modification time".
            When a
            [TransferOperation][google.storagetransfer.v1.TransferOperation]
            begins, objects with a "last modification time" are
            transferred only if the elapsed time between the
            [start_time][google.storagetransfer.v1.TransferOperation.start_time]
            of the ``TransferOperation``\ and the "last modification
            time" of the object is less than the value of
            max_time_elapsed_since_last_modification\`. Objects that do
            not have a "last modification time" are also transferred.
        include_prefixes (MutableSequence[str]):
            If you specify ``include_prefixes``, Storage Transfer
            Service uses the items in the ``include_prefixes`` array to
            determine which objects to include in a transfer. Objects
            must start with one of the matching ``include_prefixes`` for
            inclusion in the transfer. If
            [exclude_prefixes][google.storagetransfer.v1.ObjectConditions.exclude_prefixes]
            is specified, objects must not start with any of the
            ``exclude_prefixes`` specified for inclusion in the
            transfer.

            The following are requirements of ``include_prefixes``:

            - Each include-prefix can contain any sequence of Unicode
              characters, to a max length of 1024 bytes when
              UTF8-encoded, and must not contain Carriage Return or Line
              Feed characters. Wildcard matching and regular expression
              matching are not supported.

            - Each include-prefix must omit the leading slash. For
              example, to include the object
              ``s3://my-aws-bucket/logs/y=2015/requests.gz``, specify
              the include-prefix as ``logs/y=2015/requests.gz``.

            - None of the include-prefix values can be empty, if
              specified.

            - Each include-prefix must include a distinct portion of the
              object namespace. No include-prefix may be a prefix of
              another include-prefix.

            The max size of ``include_prefixes`` is 1000.

            For more information, see `Filtering objects from
            transfers </storage-transfer/docs/filtering-objects-from-transfers>`__.
        exclude_prefixes (MutableSequence[str]):
            If you specify ``exclude_prefixes``, Storage Transfer
            Service uses the items in the ``exclude_prefixes`` array to
            determine which objects to exclude from a transfer. Objects
            must not start with one of the matching ``exclude_prefixes``
            for inclusion in a transfer.

            The following are requirements of ``exclude_prefixes``:

            - Each exclude-prefix can contain any sequence of Unicode
              characters, to a max length of 1024 bytes when
              UTF8-encoded, and must not contain Carriage Return or Line
              Feed characters. Wildcard matching and regular expression
              matching are not supported.

            - Each exclude-prefix must omit the leading slash. For
              example, to exclude the object
              ``s3://my-aws-bucket/logs/y=2015/requests.gz``, specify
              the exclude-prefix as ``logs/y=2015/requests.gz``.

            - None of the exclude-prefix values can be empty, if
              specified.

            - Each exclude-prefix must exclude a distinct portion of the
              object namespace. No exclude-prefix may be a prefix of
              another exclude-prefix.

            - If
              [include_prefixes][google.storagetransfer.v1.ObjectConditions.include_prefixes]
              is specified, then each exclude-prefix must start with the
              value of a path explicitly included by
              ``include_prefixes``.

            The max size of ``exclude_prefixes`` is 1000.

            For more information, see `Filtering objects from
            transfers </storage-transfer/docs/filtering-objects-from-transfers>`__.
        last_modified_since (google.protobuf.timestamp_pb2.Timestamp):
            If specified, only objects with a "last modification time"
            on or after this timestamp and objects that don't have a
            "last modification time" are transferred.

            The ``last_modified_since`` and ``last_modified_before``
            fields can be used together for chunked data processing. For
            example, consider a script that processes each day's worth
            of data at a time. For that you'd set each of the fields as
            follows:

            - ``last_modified_since`` to the start of the day

            - ``last_modified_before`` to the end of the day
        last_modified_before (google.protobuf.timestamp_pb2.Timestamp):
            If specified, only objects with a "last
            modification time" before this timestamp and
            objects that don't have a "last modification
            time" are transferred.
    """

    min_time_elapsed_since_last_modification: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=1,
        message=duration_pb2.Duration,
    )
    max_time_elapsed_since_last_modification: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )
    include_prefixes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    exclude_prefixes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    last_modified_since: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    last_modified_before: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )


class GcsData(proto.Message):
    r"""In a GcsData resource, an object's name is the Cloud Storage
    object's name and its "last modification time" refers to the
    object's ``updated`` property of Cloud Storage objects, which
    changes when the content or the metadata of the object is updated.

    Attributes:
        bucket_name (str):
            Required. Cloud Storage bucket name. Must meet `Bucket Name
            Requirements </storage/docs/naming#requirements>`__.
        path (str):
            Root path to transfer objects.

            Must be an empty string or full path name that ends with a
            '/'. This field is treated as an object prefix. As such, it
            should generally not begin with a '/'.

            The root path value must meet `Object Name
            Requirements </storage/docs/naming#objectnames>`__.
        managed_folder_transfer_enabled (bool):
            Preview. Enables the transfer of managed folders between
            Cloud Storage buckets. Set this option on the
            gcs_data_source.

            If set to true:

            - Managed folders in the source bucket are transferred to
              the destination bucket.
            - Managed folders in the destination bucket are overwritten.
              Other OVERWRITE options are not supported.

            See `Transfer Cloud Storage managed
            folders </storage-transfer/docs/managed-folders>`__.
    """

    bucket_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    path: str = proto.Field(
        proto.STRING,
        number=3,
    )
    managed_folder_transfer_enabled: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class AwsS3Data(proto.Message):
    r"""An AwsS3Data resource can be a data source, but not a data
    sink. In an AwsS3Data resource, an object's name is the S3
    object's key name.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        bucket_name (str):
            Required. S3 Bucket name (see `Creating a
            bucket <https://docs.aws.amazon.com/AmazonS3/latest/dev/create-bucket-get-location-example.html>`__).
        aws_access_key (google.cloud.storage_transfer_v1.types.AwsAccessKey):
            Input only. AWS access key used to sign the API requests to
            the AWS S3 bucket. Permissions on the bucket must be granted
            to the access ID of the AWS access key.

            For information on our data retention policy for user
            credentials, see `User
            credentials </storage-transfer/docs/data-retention#user-credentials>`__.
        path (str):
            Root path to transfer objects.

            Must be an empty string or full path name that
            ends with a '/'. This field is treated as an
            object prefix. As such, it should generally not
            begin with a '/'.
        role_arn (str):
            The Amazon Resource Name (ARN) of the role to support
            temporary credentials via ``AssumeRoleWithWebIdentity``. For
            more information about ARNs, see `IAM
            ARNs <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns>`__.

            When a role ARN is provided, Transfer Service fetches
            temporary credentials for the session using a
            ``AssumeRoleWithWebIdentity`` call for the provided role
            using the
            [GoogleServiceAccount][google.storagetransfer.v1.GoogleServiceAccount]
            for this project.
        cloudfront_domain (str):
            Optional. The CloudFront distribution domain name pointing
            to this bucket, to use when fetching.

            See `Transfer from S3 via
            CloudFront <https://cloud.google.com/storage-transfer/docs/s3-cloudfront>`__
            for more information.

            Format: ``https://{id}.cloudfront.net`` or any valid custom
            domain. Must begin with ``https://``.
        credentials_secret (str):
            Optional. The Resource name of a secret in Secret Manager.

            AWS credentials must be stored in Secret Manager in JSON
            format:

            { "access_key_id": "ACCESS_KEY_ID", "secret_access_key":
            "SECRET_ACCESS_KEY" }

            [GoogleServiceAccount][google.storagetransfer.v1.GoogleServiceAccount]
            must be granted ``roles/secretmanager.secretAccessor`` for
            the resource.

            See [Configure access to a source: Amazon S3]
            (https://cloud.google.com/storage-transfer/docs/source-amazon-s3#secret_manager)
            for more information.

            If ``credentials_secret`` is specified, do not specify
            [role_arn][google.storagetransfer.v1.AwsS3Data.role_arn] or
            [aws_access_key][google.storagetransfer.v1.AwsS3Data.aws_access_key].

            Format: ``projects/{project_number}/secrets/{secret_name}``
        managed_private_network (bool):
            Egress bytes over a Google-managed private
            network. This network is shared between other
            users of Storage Transfer Service.

            This field is a member of `oneof`_ ``private_network``.
    """

    bucket_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    aws_access_key: "AwsAccessKey" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="AwsAccessKey",
    )
    path: str = proto.Field(
        proto.STRING,
        number=3,
    )
    role_arn: str = proto.Field(
        proto.STRING,
        number=4,
    )
    cloudfront_domain: str = proto.Field(
        proto.STRING,
        number=6,
    )
    credentials_secret: str = proto.Field(
        proto.STRING,
        number=7,
    )
    managed_private_network: bool = proto.Field(
        proto.BOOL,
        number=8,
        oneof="private_network",
    )


class AzureBlobStorageData(proto.Message):
    r"""An AzureBlobStorageData resource can be a data source, but not a
    data sink. An AzureBlobStorageData resource represents one Azure
    container. The storage account determines the `Azure
    endpoint <https://docs.microsoft.com/en-us/azure/storage/common/storage-create-storage-account#storage-account-endpoints>`__.
    In an AzureBlobStorageData resource, a blobs's name is the `Azure
    Blob Storage blob's key
    name <https://docs.microsoft.com/en-us/rest/api/storageservices/naming-and-referencing-containers--blobs--and-metadata#blob-names>`__.

    Attributes:
        storage_account (str):
            Required. The name of the Azure Storage
            account.
        azure_credentials (google.cloud.storage_transfer_v1.types.AzureCredentials):
            Required. Input only. Credentials used to authenticate API
            requests to Azure.

            For information on our data retention policy for user
            credentials, see `User
            credentials </storage-transfer/docs/data-retention#user-credentials>`__.
        container (str):
            Required. The container to transfer from the
            Azure Storage account.
        path (str):
            Root path to transfer objects.

            Must be an empty string or full path name that
            ends with a '/'. This field is treated as an
            object prefix. As such, it should generally not
            begin with a '/'.
        credentials_secret (str):
            Optional. The Resource name of a secret in Secret Manager.

            The Azure SAS token must be stored in Secret Manager in JSON
            format:

            { "sas_token" : "SAS_TOKEN" }

            [GoogleServiceAccount][google.storagetransfer.v1.GoogleServiceAccount]
            must be granted ``roles/secretmanager.secretAccessor`` for
            the resource.

            See [Configure access to a source: Microsoft Azure Blob
            Storage]
            (https://cloud.google.com/storage-transfer/docs/source-microsoft-azure#secret_manager)
            for more information.

            If ``credentials_secret`` is specified, do not specify
            [azure_credentials][google.storagetransfer.v1.AzureBlobStorageData.azure_credentials].

            Format: ``projects/{project_number}/secrets/{secret_name}``
        federated_identity_config (google.cloud.storage_transfer_v1.types.AzureBlobStorageData.FederatedIdentityConfig):
            Optional. Federated identity config of a user registered
            Azure application.

            If ``federated_identity_config`` is specified, do not
            specify
            [azure_credentials][google.storagetransfer.v1.AzureBlobStorageData.azure_credentials]
            or
            [credentials_secret][google.storagetransfer.v1.AzureBlobStorageData.credentials_secret].
    """

    class FederatedIdentityConfig(proto.Message):
        r"""The identity of an Azure application through which Storage Transfer
        Service can authenticate requests using Azure workload identity
        federation.

        Storage Transfer Service can issue requests to Azure Storage through
        registered Azure applications, eliminating the need to pass
        credentials to Storage Transfer Service directly.

        To configure federated identity, see `Configure access to Microsoft
        Azure
        Storage <https://cloud.google.com/storage-transfer/docs/source-microsoft-azure#option_3_authenticate_using_federated_identity>`__.

        Attributes:
            client_id (str):
                Required. The client (application) ID of the
                application with federated credentials.
            tenant_id (str):
                Required. The tenant (directory) ID of the
                application with federated credentials.
        """

        client_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        tenant_id: str = proto.Field(
            proto.STRING,
            number=2,
        )

    storage_account: str = proto.Field(
        proto.STRING,
        number=1,
    )
    azure_credentials: "AzureCredentials" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="AzureCredentials",
    )
    container: str = proto.Field(
        proto.STRING,
        number=4,
    )
    path: str = proto.Field(
        proto.STRING,
        number=5,
    )
    credentials_secret: str = proto.Field(
        proto.STRING,
        number=7,
    )
    federated_identity_config: FederatedIdentityConfig = proto.Field(
        proto.MESSAGE,
        number=8,
        message=FederatedIdentityConfig,
    )


class HttpData(proto.Message):
    r"""An HttpData resource specifies a list of objects on the web to be
    transferred over HTTP. The information of the objects to be
    transferred is contained in a file referenced by a URL. The first
    line in the file must be ``"TsvHttpData-1.0"``, which specifies the
    format of the file. Subsequent lines specify the information of the
    list of objects, one object per list entry. Each entry has the
    following tab-delimited fields:

    - **HTTP URL** — The location of the object.

    - **Length** — The size of the object in bytes.

    - **MD5** — The base64-encoded MD5 hash of the object.

    For an example of a valid TSV file, see `Transferring data from
    URLs <https://cloud.google.com/storage-transfer/docs/create-url-list>`__.

    When transferring data based on a URL list, keep the following in
    mind:

    - When an object located at ``http(s)://hostname:port/<URL-path>``
      is transferred to a data sink, the name of the object at the data
      sink is ``<hostname>/<URL-path>``.

    - If the specified size of an object does not match the actual size
      of the object fetched, the object is not transferred.

    - If the specified MD5 does not match the MD5 computed from the
      transferred bytes, the object transfer fails.

    - Ensure that each URL you specify is publicly accessible. For
      example, in Cloud Storage you can [share an object publicly]
      (/storage/docs/cloud-console#_sharingdata) and get a link to it.

    - Storage Transfer Service obeys ``robots.txt`` rules and requires
      the source HTTP server to support ``Range`` requests and to return
      a ``Content-Length`` header in each response.

    - [ObjectConditions][google.storagetransfer.v1.ObjectConditions]
      have no effect when filtering objects to transfer.

    Attributes:
        list_url (str):
            Required. The URL that points to the file that stores the
            object list entries. This file must allow public access. The
            URL is either an HTTP/HTTPS address (e.g.
            ``https://example.com/urllist.tsv``) or a Cloud Storage path
            (e.g. ``gs://my-bucket/urllist.tsv``).
    """

    list_url: str = proto.Field(
        proto.STRING,
        number=1,
    )


class PosixFilesystem(proto.Message):
    r"""A POSIX filesystem resource.

    Attributes:
        root_directory (str):
            Root directory path to the filesystem.
    """

    root_directory: str = proto.Field(
        proto.STRING,
        number=1,
    )


class HdfsData(proto.Message):
    r"""An HdfsData resource specifies a path within an HDFS entity
    (e.g. a cluster). All cluster-specific settings, such as
    namenodes and ports, are configured on the transfer agents
    servicing requests, so HdfsData only contains the root path to
    the data in our transfer.

    Attributes:
        path (str):
            Root path to transfer files.
    """

    path: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AwsS3CompatibleData(proto.Message):
    r"""An AwsS3CompatibleData resource.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        bucket_name (str):
            Required. Specifies the name of the bucket.
        path (str):
            Specifies the root path to transfer objects.

            Must be an empty string or full path name that
            ends with a '/'. This field is treated as an
            object prefix. As such, it should generally not
            begin with a '/'.
        endpoint (str):
            Required. Specifies the endpoint of the
            storage service.
        region (str):
            Specifies the region to sign requests with.
            This can be left blank if requests should be
            signed with an empty region.
        s3_metadata (google.cloud.storage_transfer_v1.types.S3CompatibleMetadata):
            A S3 compatible metadata.

            This field is a member of `oneof`_ ``data_provider``.
    """

    bucket_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    path: str = proto.Field(
        proto.STRING,
        number=2,
    )
    endpoint: str = proto.Field(
        proto.STRING,
        number=3,
    )
    region: str = proto.Field(
        proto.STRING,
        number=5,
    )
    s3_metadata: "S3CompatibleMetadata" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="data_provider",
        message="S3CompatibleMetadata",
    )


class S3CompatibleMetadata(proto.Message):
    r"""S3CompatibleMetadata contains the metadata fields that apply
    to the basic types of S3-compatible data providers.

    Attributes:
        auth_method (google.cloud.storage_transfer_v1.types.S3CompatibleMetadata.AuthMethod):
            Specifies the authentication and
            authorization method used by the storage
            service. When not specified, Transfer Service
            will attempt to determine right auth method to
            use.
        request_model (google.cloud.storage_transfer_v1.types.S3CompatibleMetadata.RequestModel):
            Specifies the API request model used to call the storage
            service. When not specified, the default value of
            RequestModel REQUEST_MODEL_VIRTUAL_HOSTED_STYLE is used.
        protocol (google.cloud.storage_transfer_v1.types.S3CompatibleMetadata.NetworkProtocol):
            Specifies the network protocol of the agent. When not
            specified, the default value of NetworkProtocol
            NETWORK_PROTOCOL_HTTPS is used.
        list_api (google.cloud.storage_transfer_v1.types.S3CompatibleMetadata.ListApi):
            The Listing API to use for discovering
            objects. When not specified, Transfer Service
            will attempt to determine the right API to use.
    """

    class AuthMethod(proto.Enum):
        r"""The authentication and authorization method used by the
        storage service.

        Values:
            AUTH_METHOD_UNSPECIFIED (0):
                AuthMethod is not specified.
            AUTH_METHOD_AWS_SIGNATURE_V4 (1):
                Auth requests with AWS SigV4.
            AUTH_METHOD_AWS_SIGNATURE_V2 (2):
                Auth requests with AWS SigV2.
        """

        AUTH_METHOD_UNSPECIFIED = 0
        AUTH_METHOD_AWS_SIGNATURE_V4 = 1
        AUTH_METHOD_AWS_SIGNATURE_V2 = 2

    class RequestModel(proto.Enum):
        r"""The request model of the API.

        Values:
            REQUEST_MODEL_UNSPECIFIED (0):
                RequestModel is not specified.
            REQUEST_MODEL_VIRTUAL_HOSTED_STYLE (1):
                Perform requests using Virtual Hosted Style.
                Example:
                https://bucket-name.s3.region.amazonaws.com/key-name
            REQUEST_MODEL_PATH_STYLE (2):
                Perform requests using Path Style.
                Example:
                https://s3.region.amazonaws.com/bucket-name/key-name
        """

        REQUEST_MODEL_UNSPECIFIED = 0
        REQUEST_MODEL_VIRTUAL_HOSTED_STYLE = 1
        REQUEST_MODEL_PATH_STYLE = 2

    class NetworkProtocol(proto.Enum):
        r"""The agent network protocol to access the storage service.

        Values:
            NETWORK_PROTOCOL_UNSPECIFIED (0):
                NetworkProtocol is not specified.
            NETWORK_PROTOCOL_HTTPS (1):
                Perform requests using HTTPS.
            NETWORK_PROTOCOL_HTTP (2):
                Not recommended: This sends data in
                clear-text. This is only appropriate within a
                closed network or for publicly available data.
                Perform requests using HTTP.
        """

        NETWORK_PROTOCOL_UNSPECIFIED = 0
        NETWORK_PROTOCOL_HTTPS = 1
        NETWORK_PROTOCOL_HTTP = 2

    class ListApi(proto.Enum):
        r"""The Listing API to use for discovering objects.

        Values:
            LIST_API_UNSPECIFIED (0):
                ListApi is not specified.
            LIST_OBJECTS_V2 (1):
                Perform listing using ListObjectsV2 API.
            LIST_OBJECTS (2):
                Legacy ListObjects API.
        """

        LIST_API_UNSPECIFIED = 0
        LIST_OBJECTS_V2 = 1
        LIST_OBJECTS = 2

    auth_method: AuthMethod = proto.Field(
        proto.ENUM,
        number=1,
        enum=AuthMethod,
    )
    request_model: RequestModel = proto.Field(
        proto.ENUM,
        number=2,
        enum=RequestModel,
    )
    protocol: NetworkProtocol = proto.Field(
        proto.ENUM,
        number=3,
        enum=NetworkProtocol,
    )
    list_api: ListApi = proto.Field(
        proto.ENUM,
        number=4,
        enum=ListApi,
    )


class AgentPool(proto.Message):
    r"""Represents an agent pool.

    Attributes:
        name (str):
            Required. Specifies a unique string that identifies the
            agent pool.

            Format: ``projects/{project_id}/agentPools/{agent_pool_id}``
        display_name (str):
            Specifies the client-specified AgentPool
            description.
        state (google.cloud.storage_transfer_v1.types.AgentPool.State):
            Output only. Specifies the state of the
            AgentPool.
        bandwidth_limit (google.cloud.storage_transfer_v1.types.AgentPool.BandwidthLimit):
            Specifies the bandwidth limit details. If
            this field is unspecified, the default value is
            set as 'No Limit'.
    """

    class State(proto.Enum):
        r"""The state of an AgentPool.

        Values:
            STATE_UNSPECIFIED (0):
                Default value. This value is unused.
            CREATING (1):
                This is an initialization state. During this
                stage, resources are allocated for the
                AgentPool.
            CREATED (2):
                Determines that the AgentPool is created for
                use. At this state, Agents can join the
                AgentPool and participate in the transfer jobs
                in that pool.
            DELETING (3):
                Determines that the AgentPool deletion has
                been initiated, and all the resources are
                scheduled to be cleaned up and freed.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        CREATED = 2
        DELETING = 3

    class BandwidthLimit(proto.Message):
        r"""Specifies a bandwidth limit for an agent pool.

        Attributes:
            limit_mbps (int):
                Bandwidth rate in megabytes per second,
                distributed across all the agents in the pool.
        """

        limit_mbps: int = proto.Field(
            proto.INT64,
            number=1,
        )

    name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )
    bandwidth_limit: BandwidthLimit = proto.Field(
        proto.MESSAGE,
        number=5,
        message=BandwidthLimit,
    )


class TransferOptions(proto.Message):
    r"""TransferOptions define the actions to be performed on objects
    in a transfer.

    Attributes:
        overwrite_objects_already_existing_in_sink (bool):
            When to overwrite objects that already exist
            in the sink. The default is that only objects
            that are different from the source are
            overwritten. If true, all objects in the sink
            whose name matches an object in the source are
            overwritten with the source object.
        delete_objects_unique_in_sink (bool):
            Whether objects that exist only in the sink should be
            deleted.

            **Note:** This option and
            [delete_objects_from_source_after_transfer][google.storagetransfer.v1.TransferOptions.delete_objects_from_source_after_transfer]
            are mutually exclusive.
        delete_objects_from_source_after_transfer (bool):
            Whether objects should be deleted from the source after they
            are transferred to the sink.

            **Note:** This option and
            [delete_objects_unique_in_sink][google.storagetransfer.v1.TransferOptions.delete_objects_unique_in_sink]
            are mutually exclusive.
        overwrite_when (google.cloud.storage_transfer_v1.types.TransferOptions.OverwriteWhen):
            When to overwrite objects that already exist in the sink. If
            not set, overwrite behavior is determined by
            [overwrite_objects_already_existing_in_sink][google.storagetransfer.v1.TransferOptions.overwrite_objects_already_existing_in_sink].
        metadata_options (google.cloud.storage_transfer_v1.types.MetadataOptions):
            Represents the selected metadata options for
            a transfer job.
    """

    class OverwriteWhen(proto.Enum):
        r"""Specifies when to overwrite an object in the sink when an
        object with matching name is found in the source.

        Values:
            OVERWRITE_WHEN_UNSPECIFIED (0):
                Overwrite behavior is unspecified.
            DIFFERENT (1):
                Overwrites destination objects with the
                source objects, only if the objects have the
                same name but different HTTP ETags or checksum
                values.
            NEVER (2):
                Never overwrites a destination object if a
                source object has the same name. In this case,
                the source object is not transferred.
            ALWAYS (3):
                Always overwrite the destination object with
                the source object, even if the HTTP Etags or
                checksum values are the same.
        """

        OVERWRITE_WHEN_UNSPECIFIED = 0
        DIFFERENT = 1
        NEVER = 2
        ALWAYS = 3

    overwrite_objects_already_existing_in_sink: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    delete_objects_unique_in_sink: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    delete_objects_from_source_after_transfer: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    overwrite_when: OverwriteWhen = proto.Field(
        proto.ENUM,
        number=4,
        enum=OverwriteWhen,
    )
    metadata_options: "MetadataOptions" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="MetadataOptions",
    )


class TransferSpec(proto.Message):
    r"""Configuration for running a transfer.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_data_sink (google.cloud.storage_transfer_v1.types.GcsData):
            A Cloud Storage data sink.

            This field is a member of `oneof`_ ``data_sink``.
        posix_data_sink (google.cloud.storage_transfer_v1.types.PosixFilesystem):
            A POSIX Filesystem data sink.

            This field is a member of `oneof`_ ``data_sink``.
        gcs_data_source (google.cloud.storage_transfer_v1.types.GcsData):
            A Cloud Storage data source.

            This field is a member of `oneof`_ ``data_source``.
        aws_s3_data_source (google.cloud.storage_transfer_v1.types.AwsS3Data):
            An AWS S3 data source.

            This field is a member of `oneof`_ ``data_source``.
        http_data_source (google.cloud.storage_transfer_v1.types.HttpData):
            An HTTP URL data source.

            This field is a member of `oneof`_ ``data_source``.
        posix_data_source (google.cloud.storage_transfer_v1.types.PosixFilesystem):
            A POSIX Filesystem data source.

            This field is a member of `oneof`_ ``data_source``.
        azure_blob_storage_data_source (google.cloud.storage_transfer_v1.types.AzureBlobStorageData):
            An Azure Blob Storage data source.

            This field is a member of `oneof`_ ``data_source``.
        aws_s3_compatible_data_source (google.cloud.storage_transfer_v1.types.AwsS3CompatibleData):
            An AWS S3 compatible data source.

            This field is a member of `oneof`_ ``data_source``.
        hdfs_data_source (google.cloud.storage_transfer_v1.types.HdfsData):
            An HDFS cluster data source.

            This field is a member of `oneof`_ ``data_source``.
        gcs_intermediate_data_location (google.cloud.storage_transfer_v1.types.GcsData):
            For transfers between file systems, specifies a Cloud
            Storage bucket to be used as an intermediate location
            through which to transfer data.

            See `Transfer data between file
            systems <https://cloud.google.com/storage-transfer/docs/file-to-file>`__
            for more information.

            This field is a member of `oneof`_ ``intermediate_data_location``.
        object_conditions (google.cloud.storage_transfer_v1.types.ObjectConditions):
            Only objects that satisfy these object
            conditions are included in the set of data
            source and data sink objects.  Object conditions
            based on objects' "last modification time" do
            not exclude objects in a data sink.
        transfer_options (google.cloud.storage_transfer_v1.types.TransferOptions):
            If the option
            [delete_objects_unique_in_sink][google.storagetransfer.v1.TransferOptions.delete_objects_unique_in_sink]
            is ``true`` and time-based object conditions such as 'last
            modification time' are specified, the request fails with an
            [INVALID_ARGUMENT][google.rpc.Code.INVALID_ARGUMENT] error.
        transfer_manifest (google.cloud.storage_transfer_v1.types.TransferManifest):
            A manifest file provides a list of objects to
            be transferred from the data source. This field
            points to the location of the manifest file.
            Otherwise, the entire source bucket is used.
            ObjectConditions still apply.
        source_agent_pool_name (str):
            Specifies the agent pool name associated with
            the posix data source. When unspecified, the
            default name is used.
        sink_agent_pool_name (str):
            Specifies the agent pool name associated with
            the posix data sink. When unspecified, the
            default name is used.
    """

    gcs_data_sink: "GcsData" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="data_sink",
        message="GcsData",
    )
    posix_data_sink: "PosixFilesystem" = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="data_sink",
        message="PosixFilesystem",
    )
    gcs_data_source: "GcsData" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="data_source",
        message="GcsData",
    )
    aws_s3_data_source: "AwsS3Data" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="data_source",
        message="AwsS3Data",
    )
    http_data_source: "HttpData" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="data_source",
        message="HttpData",
    )
    posix_data_source: "PosixFilesystem" = proto.Field(
        proto.MESSAGE,
        number=14,
        oneof="data_source",
        message="PosixFilesystem",
    )
    azure_blob_storage_data_source: "AzureBlobStorageData" = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="data_source",
        message="AzureBlobStorageData",
    )
    aws_s3_compatible_data_source: "AwsS3CompatibleData" = proto.Field(
        proto.MESSAGE,
        number=19,
        oneof="data_source",
        message="AwsS3CompatibleData",
    )
    hdfs_data_source: "HdfsData" = proto.Field(
        proto.MESSAGE,
        number=20,
        oneof="data_source",
        message="HdfsData",
    )
    gcs_intermediate_data_location: "GcsData" = proto.Field(
        proto.MESSAGE,
        number=16,
        oneof="intermediate_data_location",
        message="GcsData",
    )
    object_conditions: "ObjectConditions" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="ObjectConditions",
    )
    transfer_options: "TransferOptions" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="TransferOptions",
    )
    transfer_manifest: "TransferManifest" = proto.Field(
        proto.MESSAGE,
        number=15,
        message="TransferManifest",
    )
    source_agent_pool_name: str = proto.Field(
        proto.STRING,
        number=17,
    )
    sink_agent_pool_name: str = proto.Field(
        proto.STRING,
        number=18,
    )


class ReplicationSpec(proto.Message):
    r"""Specifies the configuration for a cross-bucket replication
    job. Cross-bucket replication copies new or updated objects from
    a source Cloud Storage bucket to a destination Cloud Storage
    bucket. Existing objects in the source bucket are not copied by
    a new cross-bucket replication job.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_data_source (google.cloud.storage_transfer_v1.types.GcsData):
            The Cloud Storage bucket from which to
            replicate objects.

            This field is a member of `oneof`_ ``data_source``.
        gcs_data_sink (google.cloud.storage_transfer_v1.types.GcsData):
            The Cloud Storage bucket to which to
            replicate objects.

            This field is a member of `oneof`_ ``data_sink``.
        object_conditions (google.cloud.storage_transfer_v1.types.ObjectConditions):
            Object conditions that determine which objects are
            transferred. For replication jobs, only ``include_prefixes``
            and ``exclude_prefixes`` are supported.
        transfer_options (google.cloud.storage_transfer_v1.types.TransferOptions):
            Specifies the metadata options to be applied during
            replication. Delete options are not supported. If a delete
            option is specified, the request fails with an
            [INVALID_ARGUMENT][google.rpc.Code.INVALID_ARGUMENT] error.
    """

    gcs_data_source: "GcsData" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="data_source",
        message="GcsData",
    )
    gcs_data_sink: "GcsData" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="data_sink",
        message="GcsData",
    )
    object_conditions: "ObjectConditions" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ObjectConditions",
    )
    transfer_options: "TransferOptions" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="TransferOptions",
    )


class MetadataOptions(proto.Message):
    r"""Specifies the metadata options for running a transfer.

    Attributes:
        symlink (google.cloud.storage_transfer_v1.types.MetadataOptions.Symlink):
            Specifies how symlinks should be handled by
            the transfer. By default, symlinks are not
            preserved. Only applicable to transfers
            involving POSIX file systems, and ignored for
            other transfers.
        mode (google.cloud.storage_transfer_v1.types.MetadataOptions.Mode):
            Specifies how each file's mode attribute
            should be handled by the transfer. By default,
            mode is not preserved. Only applicable to
            transfers involving POSIX file systems, and
            ignored for other transfers.
        gid (google.cloud.storage_transfer_v1.types.MetadataOptions.GID):
            Specifies how each file's POSIX group ID
            (GID) attribute should be handled by the
            transfer. By default, GID is not preserved. Only
            applicable to transfers involving POSIX file
            systems, and ignored for other transfers.
        uid (google.cloud.storage_transfer_v1.types.MetadataOptions.UID):
            Specifies how each file's POSIX user ID (UID)
            attribute should be handled by the transfer. By
            default, UID is not preserved. Only applicable
            to transfers involving POSIX file systems, and
            ignored for other transfers.
        acl (google.cloud.storage_transfer_v1.types.MetadataOptions.Acl):
            Specifies how each object's ACLs should be preserved for
            transfers between Google Cloud Storage buckets. If
            unspecified, the default behavior is the same as
            ACL_DESTINATION_BUCKET_DEFAULT.
        storage_class (google.cloud.storage_transfer_v1.types.MetadataOptions.StorageClass):
            Specifies the storage class to set on objects being
            transferred to Google Cloud Storage buckets. If unspecified,
            the default behavior is the same as
            [STORAGE_CLASS_DESTINATION_BUCKET_DEFAULT][google.storagetransfer.v1.MetadataOptions.StorageClass.STORAGE_CLASS_DESTINATION_BUCKET_DEFAULT].
        temporary_hold (google.cloud.storage_transfer_v1.types.MetadataOptions.TemporaryHold):
            Specifies how each object's temporary hold status should be
            preserved for transfers between Google Cloud Storage
            buckets. If unspecified, the default behavior is the same as
            [TEMPORARY_HOLD_PRESERVE][google.storagetransfer.v1.MetadataOptions.TemporaryHold.TEMPORARY_HOLD_PRESERVE].
        kms_key (google.cloud.storage_transfer_v1.types.MetadataOptions.KmsKey):
            Specifies how each object's Cloud KMS customer-managed
            encryption key (CMEK) is preserved for transfers between
            Google Cloud Storage buckets. If unspecified, the default
            behavior is the same as
            [KMS_KEY_DESTINATION_BUCKET_DEFAULT][google.storagetransfer.v1.MetadataOptions.KmsKey.KMS_KEY_DESTINATION_BUCKET_DEFAULT].
        time_created (google.cloud.storage_transfer_v1.types.MetadataOptions.TimeCreated):
            Specifies how each object's ``timeCreated`` metadata is
            preserved for transfers. If unspecified, the default
            behavior is the same as
            [TIME_CREATED_SKIP][google.storagetransfer.v1.MetadataOptions.TimeCreated.TIME_CREATED_SKIP].
            This behavior is supported for transfers to Cloud Storage
            buckets from Cloud Storage, Amazon S3, S3-compatible
            storage, and Azure sources.
    """

    class Symlink(proto.Enum):
        r"""Whether symlinks should be skipped or preserved during a
        transfer job.

        Values:
            SYMLINK_UNSPECIFIED (0):
                Symlink behavior is unspecified.
            SYMLINK_SKIP (1):
                Do not preserve symlinks during a transfer
                job.
            SYMLINK_PRESERVE (2):
                Preserve symlinks during a transfer job.
        """

        SYMLINK_UNSPECIFIED = 0
        SYMLINK_SKIP = 1
        SYMLINK_PRESERVE = 2

    class Mode(proto.Enum):
        r"""Options for handling file mode attribute.

        Values:
            MODE_UNSPECIFIED (0):
                Mode behavior is unspecified.
            MODE_SKIP (1):
                Do not preserve mode during a transfer job.
            MODE_PRESERVE (2):
                Preserve mode during a transfer job.
        """

        MODE_UNSPECIFIED = 0
        MODE_SKIP = 1
        MODE_PRESERVE = 2

    class GID(proto.Enum):
        r"""Options for handling file GID attribute.

        Values:
            GID_UNSPECIFIED (0):
                GID behavior is unspecified.
            GID_SKIP (1):
                Do not preserve GID during a transfer job.
            GID_NUMBER (2):
                Preserve GID during a transfer job.
        """

        GID_UNSPECIFIED = 0
        GID_SKIP = 1
        GID_NUMBER = 2

    class UID(proto.Enum):
        r"""Options for handling file UID attribute.

        Values:
            UID_UNSPECIFIED (0):
                UID behavior is unspecified.
            UID_SKIP (1):
                Do not preserve UID during a transfer job.
            UID_NUMBER (2):
                Preserve UID during a transfer job.
        """

        UID_UNSPECIFIED = 0
        UID_SKIP = 1
        UID_NUMBER = 2

    class Acl(proto.Enum):
        r"""Options for handling Cloud Storage object ACLs.

        Values:
            ACL_UNSPECIFIED (0):
                ACL behavior is unspecified.
            ACL_DESTINATION_BUCKET_DEFAULT (1):
                Use the destination bucket's default object
                ACLS, if applicable.
            ACL_PRESERVE (2):
                Preserve the object's original ACLs. This requires the
                service account to have ``storage.objects.getIamPolicy``
                permission for the source object. `Uniform bucket-level
                access <https://cloud.google.com/storage/docs/uniform-bucket-level-access>`__
                must not be enabled on either the source or destination
                buckets.
        """

        ACL_UNSPECIFIED = 0
        ACL_DESTINATION_BUCKET_DEFAULT = 1
        ACL_PRESERVE = 2

    class StorageClass(proto.Enum):
        r"""Options for handling Google Cloud Storage object storage
        class.

        Values:
            STORAGE_CLASS_UNSPECIFIED (0):
                Storage class behavior is unspecified.
            STORAGE_CLASS_DESTINATION_BUCKET_DEFAULT (1):
                Use the destination bucket's default storage
                class.
            STORAGE_CLASS_PRESERVE (2):
                Preserve the object's original storage class. This is only
                supported for transfers from Google Cloud Storage buckets.
                REGIONAL and MULTI_REGIONAL storage classes will be mapped
                to STANDARD to ensure they can be written to the destination
                bucket.
            STORAGE_CLASS_STANDARD (3):
                Set the storage class to STANDARD.
            STORAGE_CLASS_NEARLINE (4):
                Set the storage class to NEARLINE.
            STORAGE_CLASS_COLDLINE (5):
                Set the storage class to COLDLINE.
            STORAGE_CLASS_ARCHIVE (6):
                Set the storage class to ARCHIVE.
        """

        STORAGE_CLASS_UNSPECIFIED = 0
        STORAGE_CLASS_DESTINATION_BUCKET_DEFAULT = 1
        STORAGE_CLASS_PRESERVE = 2
        STORAGE_CLASS_STANDARD = 3
        STORAGE_CLASS_NEARLINE = 4
        STORAGE_CLASS_COLDLINE = 5
        STORAGE_CLASS_ARCHIVE = 6

    class TemporaryHold(proto.Enum):
        r"""Options for handling temporary holds for Google Cloud Storage
        objects.

        Values:
            TEMPORARY_HOLD_UNSPECIFIED (0):
                Temporary hold behavior is unspecified.
            TEMPORARY_HOLD_SKIP (1):
                Do not set a temporary hold on the
                destination object.
            TEMPORARY_HOLD_PRESERVE (2):
                Preserve the object's original temporary hold
                status.
        """

        TEMPORARY_HOLD_UNSPECIFIED = 0
        TEMPORARY_HOLD_SKIP = 1
        TEMPORARY_HOLD_PRESERVE = 2

    class KmsKey(proto.Enum):
        r"""Options for handling the KmsKey setting for Google Cloud
        Storage objects.

        Values:
            KMS_KEY_UNSPECIFIED (0):
                KmsKey behavior is unspecified.
            KMS_KEY_DESTINATION_BUCKET_DEFAULT (1):
                Use the destination bucket's default
                encryption settings.
            KMS_KEY_PRESERVE (2):
                Preserve the object's original Cloud KMS
                customer-managed encryption key (CMEK) if
                present. Objects that do not use a Cloud KMS
                encryption key will be encrypted using the
                destination bucket's encryption settings.
        """

        KMS_KEY_UNSPECIFIED = 0
        KMS_KEY_DESTINATION_BUCKET_DEFAULT = 1
        KMS_KEY_PRESERVE = 2

    class TimeCreated(proto.Enum):
        r"""Options for handling ``timeCreated`` metadata for Google Cloud
        Storage objects.

        Values:
            TIME_CREATED_UNSPECIFIED (0):
                TimeCreated behavior is unspecified.
            TIME_CREATED_SKIP (1):
                Do not preserve the ``timeCreated`` metadata from the source
                object.
            TIME_CREATED_PRESERVE_AS_CUSTOM_TIME (2):
                Preserves the source object's ``timeCreated`` or
                ``lastModified`` metadata in the ``customTime`` field in the
                destination object. Note that any value stored in the source
                object's ``customTime`` field will not be propagated to the
                destination object.
        """

        TIME_CREATED_UNSPECIFIED = 0
        TIME_CREATED_SKIP = 1
        TIME_CREATED_PRESERVE_AS_CUSTOM_TIME = 2

    symlink: Symlink = proto.Field(
        proto.ENUM,
        number=1,
        enum=Symlink,
    )
    mode: Mode = proto.Field(
        proto.ENUM,
        number=2,
        enum=Mode,
    )
    gid: GID = proto.Field(
        proto.ENUM,
        number=3,
        enum=GID,
    )
    uid: UID = proto.Field(
        proto.ENUM,
        number=4,
        enum=UID,
    )
    acl: Acl = proto.Field(
        proto.ENUM,
        number=5,
        enum=Acl,
    )
    storage_class: StorageClass = proto.Field(
        proto.ENUM,
        number=6,
        enum=StorageClass,
    )
    temporary_hold: TemporaryHold = proto.Field(
        proto.ENUM,
        number=7,
        enum=TemporaryHold,
    )
    kms_key: KmsKey = proto.Field(
        proto.ENUM,
        number=8,
        enum=KmsKey,
    )
    time_created: TimeCreated = proto.Field(
        proto.ENUM,
        number=9,
        enum=TimeCreated,
    )


class TransferManifest(proto.Message):
    r"""Specifies where the manifest is located.

    Attributes:
        location (str):
            Specifies the path to the manifest in Cloud Storage. The
            Google-managed service account for the transfer must have
            ``storage.objects.get`` permission for this object. An
            example path is ``gs://bucket_name/path/manifest.csv``.
    """

    location: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Schedule(proto.Message):
    r"""Transfers can be scheduled to recur or to run just once.

    Attributes:
        schedule_start_date (google.type.date_pb2.Date):
            Required. The start date of a transfer. Date boundaries are
            determined relative to UTC time. If ``schedule_start_date``
            and
            [start_time_of_day][google.storagetransfer.v1.Schedule.start_time_of_day]
            are in the past relative to the job's creation time, the
            transfer starts the day after you schedule the transfer
            request.

            **Note:** When starting jobs at or near midnight UTC it is
            possible that a job starts later than expected. For example,
            if you send an outbound request on June 1 one millisecond
            prior to midnight UTC and the Storage Transfer Service
            server receives the request on June 2, then it creates a
            TransferJob with ``schedule_start_date`` set to June 2 and a
            ``start_time_of_day`` set to midnight UTC. The first
            scheduled
            [TransferOperation][google.storagetransfer.v1.TransferOperation]
            takes place on June 3 at midnight UTC.
        schedule_end_date (google.type.date_pb2.Date):
            The last day a transfer runs. Date boundaries are determined
            relative to UTC time. A job runs once per 24 hours within
            the following guidelines:

            - If ``schedule_end_date`` and
              [schedule_start_date][google.storagetransfer.v1.Schedule.schedule_start_date]
              are the same and in the future relative to UTC, the
              transfer is executed only one time.
            - If ``schedule_end_date`` is later than
              ``schedule_start_date`` and ``schedule_end_date`` is in
              the future relative to UTC, the job runs each day at
              [start_time_of_day][google.storagetransfer.v1.Schedule.start_time_of_day]
              through ``schedule_end_date``.
        start_time_of_day (google.type.timeofday_pb2.TimeOfDay):
            The time in UTC that a transfer job is scheduled to run.
            Transfers may start later than this time.

            If ``start_time_of_day`` is not specified:

            - One-time transfers run immediately.
            - Recurring transfers run immediately, and each day at
              midnight UTC, through
              [schedule_end_date][google.storagetransfer.v1.Schedule.schedule_end_date].

            If ``start_time_of_day`` is specified:

            - One-time transfers run at the specified time.
            - Recurring transfers run at the specified time each day,
              through ``schedule_end_date``.
        end_time_of_day (google.type.timeofday_pb2.TimeOfDay):
            The time in UTC that no further transfer operations are
            scheduled. Combined with
            [schedule_end_date][google.storagetransfer.v1.Schedule.schedule_end_date],
            ``end_time_of_day`` specifies the end date and time for
            starting new transfer operations. This field must be greater
            than or equal to the timestamp corresponding to the
            combination of
            [schedule_start_date][google.storagetransfer.v1.Schedule.schedule_start_date]
            and
            [start_time_of_day][google.storagetransfer.v1.Schedule.start_time_of_day],
            and is subject to the following:

            - If ``end_time_of_day`` is not set and
              ``schedule_end_date`` is set, then a default value of
              ``23:59:59`` is used for ``end_time_of_day``.

            - If ``end_time_of_day`` is set and ``schedule_end_date`` is
              not set, then
              [INVALID_ARGUMENT][google.rpc.Code.INVALID_ARGUMENT] is
              returned.
        repeat_interval (google.protobuf.duration_pb2.Duration):
            Interval between the start of each scheduled
            TransferOperation. If unspecified, the default
            value is 24 hours. This value may not be less
            than 1 hour.
    """

    schedule_start_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=1,
        message=date_pb2.Date,
    )
    schedule_end_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=2,
        message=date_pb2.Date,
    )
    start_time_of_day: timeofday_pb2.TimeOfDay = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timeofday_pb2.TimeOfDay,
    )
    end_time_of_day: timeofday_pb2.TimeOfDay = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timeofday_pb2.TimeOfDay,
    )
    repeat_interval: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=5,
        message=duration_pb2.Duration,
    )


class EventStream(proto.Message):
    r"""Specifies the Event-driven transfer options. Event-driven
    transfers listen to an event stream to transfer updated files.

    Attributes:
        name (str):
            Required. Specifies a unique name of the resource such as
            AWS SQS ARN in the form
            'arn:aws:sqs:region:account_id:queue_name', or Pub/Sub
            subscription resource name in the form
            'projects/{project}/subscriptions/{sub}'.
        event_stream_start_time (google.protobuf.timestamp_pb2.Timestamp):
            Specifies the date and time that Storage
            Transfer Service starts listening for events
            from this stream. If no start time is specified
            or start time is in the past, Storage Transfer
            Service starts listening immediately.
        event_stream_expiration_time (google.protobuf.timestamp_pb2.Timestamp):
            Specifies the data and time at which Storage
            Transfer Service stops listening for events from
            this stream. After this time, any transfers in
            progress will complete, but no new transfers are
            initiated.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    event_stream_start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    event_stream_expiration_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


class TransferJob(proto.Message):
    r"""This resource represents the configuration of a transfer job
    that runs periodically.

    Attributes:
        name (str):
            A unique name (within the transfer project) assigned when
            the job is created. If this field is empty in a
            CreateTransferJobRequest, Storage Transfer Service assigns a
            unique name. Otherwise, the specified name is used as the
            unique name for this job.

            If the specified name is in use by a job, the creation
            request fails with an
            [ALREADY_EXISTS][google.rpc.Code.ALREADY_EXISTS] error.

            This name must start with ``"transferJobs/"`` prefix and end
            with a letter or a number, and should be no more than 128
            characters. For transfers involving PosixFilesystem, this
            name must start with ``transferJobs/OPI`` specifically. For
            all other transfer types, this name must not start with
            ``transferJobs/OPI``.

            Non-PosixFilesystem example:
            ``"transferJobs/^(?!OPI)[A-Za-z0-9-._~]*[A-Za-z0-9]$"``

            PosixFilesystem example:
            ``"transferJobs/OPI^[A-Za-z0-9-._~]*[A-Za-z0-9]$"``

            Applications must not rely on the enforcement of naming
            requirements involving OPI.

            Invalid job names fail with an
            [INVALID_ARGUMENT][google.rpc.Code.INVALID_ARGUMENT] error.
        description (str):
            A description provided by the user for the
            job. Its max length is 1024 bytes when
            Unicode-encoded.
        project_id (str):
            The ID of the Google Cloud project that owns
            the job.
        service_account (str):
            Optional. The user-managed service account to which to
            delegate service agent permissions. You can grant Cloud
            Storage bucket permissions to this service account instead
            of to the Transfer Service service agent.

            Format is
            ``projects/-/serviceAccounts/ACCOUNT_EMAIL_OR_UNIQUEID``

            Either the service account email
            (``SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com``)
            or the unique ID (``123456789012345678901``) are accepted in
            the string. The ``-`` wildcard character is required;
            replacing it with a project ID is invalid.

            See
            https://cloud.google.com//storage-transfer/docs/delegate-service-agent-permissions
            for required permissions.
        transfer_spec (google.cloud.storage_transfer_v1.types.TransferSpec):
            Transfer specification.
        replication_spec (google.cloud.storage_transfer_v1.types.ReplicationSpec):
            Replication specification.
        notification_config (google.cloud.storage_transfer_v1.types.NotificationConfig):
            Notification configuration.
        logging_config (google.cloud.storage_transfer_v1.types.LoggingConfig):
            Logging configuration.
        schedule (google.cloud.storage_transfer_v1.types.Schedule):
            Specifies schedule for the transfer job.
            This is an optional field. When the field is not
            set, the job never executes a transfer, unless
            you invoke RunTransferJob or update the job to
            have a non-empty schedule.
        event_stream (google.cloud.storage_transfer_v1.types.EventStream):
            Specifies the event stream for the transfer
            job for event-driven transfers. When EventStream
            is specified, the Schedule fields are ignored.
        status (google.cloud.storage_transfer_v1.types.TransferJob.Status):
            Status of the job. This value MUST be specified for
            ``CreateTransferJobRequests``.

            **Note:** The effect of the new job status takes place
            during a subsequent job run. For example, if you change the
            job status from
            [ENABLED][google.storagetransfer.v1.TransferJob.Status.ENABLED]
            to
            [DISABLED][google.storagetransfer.v1.TransferJob.Status.DISABLED],
            and an operation spawned by the transfer is running, the
            status change would not affect the current operation.
        creation_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time that the transfer job
            was created.
        last_modification_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time that the transfer job
            was last modified.
        deletion_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time that the transfer job
            was deleted.
        latest_operation_name (str):
            The name of the most recently started
            TransferOperation of this JobConfig. Present if
            a TransferOperation has been created for this
            JobConfig.
    """

    class Status(proto.Enum):
        r"""The status of the transfer job.

        Values:
            STATUS_UNSPECIFIED (0):
                Zero is an illegal value.
            ENABLED (1):
                New transfers are performed based on the
                schedule.
            DISABLED (2):
                New transfers are not scheduled.
            DELETED (3):
                This is a soft delete state. After a transfer job is set to
                this state, the job and all the transfer executions are
                subject to garbage collection. Transfer jobs become eligible
                for garbage collection 30 days after their status is set to
                ``DELETED``.
        """

        STATUS_UNSPECIFIED = 0
        ENABLED = 1
        DISABLED = 2
        DELETED = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=18,
    )
    transfer_spec: "TransferSpec" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="TransferSpec",
    )
    replication_spec: "ReplicationSpec" = proto.Field(
        proto.MESSAGE,
        number=17,
        message="ReplicationSpec",
    )
    notification_config: "NotificationConfig" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="NotificationConfig",
    )
    logging_config: "LoggingConfig" = proto.Field(
        proto.MESSAGE,
        number=14,
        message="LoggingConfig",
    )
    schedule: "Schedule" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="Schedule",
    )
    event_stream: "EventStream" = proto.Field(
        proto.MESSAGE,
        number=15,
        message="EventStream",
    )
    status: Status = proto.Field(
        proto.ENUM,
        number=6,
        enum=Status,
    )
    creation_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    last_modification_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    deletion_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    latest_operation_name: str = proto.Field(
        proto.STRING,
        number=12,
    )


class ErrorLogEntry(proto.Message):
    r"""An entry describing an error that has occurred.

    Attributes:
        url (str):
            Required. A URL that refers to the target (a
            data source, a data sink, or an object) with
            which the error is associated.
        error_details (MutableSequence[str]):
            A list of messages that carry the error
            details.
    """

    url: str = proto.Field(
        proto.STRING,
        number=1,
    )
    error_details: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class ErrorSummary(proto.Message):
    r"""A summary of errors by error code, plus a count and sample
    error log entries.

    Attributes:
        error_code (google.rpc.code_pb2.Code):
            Required.
        error_count (int):
            Required. Count of this type of error.
        error_log_entries (MutableSequence[google.cloud.storage_transfer_v1.types.ErrorLogEntry]):
            Error samples.

            At most 5 error log entries are recorded for a
            given error code for a single transfer
            operation.
    """

    error_code: code_pb2.Code = proto.Field(
        proto.ENUM,
        number=1,
        enum=code_pb2.Code,
    )
    error_count: int = proto.Field(
        proto.INT64,
        number=2,
    )
    error_log_entries: MutableSequence["ErrorLogEntry"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="ErrorLogEntry",
    )


class TransferCounters(proto.Message):
    r"""A collection of counters that report the progress of a
    transfer operation.

    Attributes:
        objects_found_from_source (int):
            Objects found in the data source that are
            scheduled to be transferred, excluding any that
            are filtered based on object conditions or
            skipped due to sync.
        bytes_found_from_source (int):
            Bytes found in the data source that are
            scheduled to be transferred, excluding any that
            are filtered based on object conditions or
            skipped due to sync.
        objects_found_only_from_sink (int):
            Objects found only in the data sink that are
            scheduled to be deleted.
        bytes_found_only_from_sink (int):
            Bytes found only in the data sink that are
            scheduled to be deleted.
        objects_from_source_skipped_by_sync (int):
            Objects in the data source that are not
            transferred because they already exist in the
            data sink.
        bytes_from_source_skipped_by_sync (int):
            Bytes in the data source that are not
            transferred because they already exist in the
            data sink.
        objects_copied_to_sink (int):
            Objects that are copied to the data sink.
        bytes_copied_to_sink (int):
            Bytes that are copied to the data sink.
        objects_deleted_from_source (int):
            Objects that are deleted from the data
            source.
        bytes_deleted_from_source (int):
            Bytes that are deleted from the data source.
        objects_deleted_from_sink (int):
            Objects that are deleted from the data sink.
        bytes_deleted_from_sink (int):
            Bytes that are deleted from the data sink.
        objects_from_source_failed (int):
            Objects in the data source that failed to be
            transferred or that failed to be deleted after
            being transferred.
        bytes_from_source_failed (int):
            Bytes in the data source that failed to be
            transferred or that failed to be deleted after
            being transferred.
        objects_failed_to_delete_from_sink (int):
            Objects that failed to be deleted from the
            data sink.
        bytes_failed_to_delete_from_sink (int):
            Bytes that failed to be deleted from the data
            sink.
        directories_found_from_source (int):
            For transfers involving PosixFilesystem only.

            Number of directories found while listing. For example, if
            the root directory of the transfer is ``base/`` and there
            are two other directories, ``a/`` and ``b/`` under this
            directory, the count after listing ``base/``, ``base/a/``
            and ``base/b/`` is 3.
        directories_failed_to_list_from_source (int):
            For transfers involving PosixFilesystem only.

            Number of listing failures for each directory
            found at the source. Potential failures when
            listing a directory include permission failure
            or block failure. If listing a directory fails,
            no files in the directory are transferred.
        directories_successfully_listed_from_source (int):
            For transfers involving PosixFilesystem only.

            Number of successful listings for each directory
            found at the source.
        intermediate_objects_cleaned_up (int):
            Number of successfully cleaned up
            intermediate objects.
        intermediate_objects_failed_cleaned_up (int):
            Number of intermediate objects failed cleaned
            up.
    """

    objects_found_from_source: int = proto.Field(
        proto.INT64,
        number=1,
    )
    bytes_found_from_source: int = proto.Field(
        proto.INT64,
        number=2,
    )
    objects_found_only_from_sink: int = proto.Field(
        proto.INT64,
        number=3,
    )
    bytes_found_only_from_sink: int = proto.Field(
        proto.INT64,
        number=4,
    )
    objects_from_source_skipped_by_sync: int = proto.Field(
        proto.INT64,
        number=5,
    )
    bytes_from_source_skipped_by_sync: int = proto.Field(
        proto.INT64,
        number=6,
    )
    objects_copied_to_sink: int = proto.Field(
        proto.INT64,
        number=7,
    )
    bytes_copied_to_sink: int = proto.Field(
        proto.INT64,
        number=8,
    )
    objects_deleted_from_source: int = proto.Field(
        proto.INT64,
        number=9,
    )
    bytes_deleted_from_source: int = proto.Field(
        proto.INT64,
        number=10,
    )
    objects_deleted_from_sink: int = proto.Field(
        proto.INT64,
        number=11,
    )
    bytes_deleted_from_sink: int = proto.Field(
        proto.INT64,
        number=12,
    )
    objects_from_source_failed: int = proto.Field(
        proto.INT64,
        number=13,
    )
    bytes_from_source_failed: int = proto.Field(
        proto.INT64,
        number=14,
    )
    objects_failed_to_delete_from_sink: int = proto.Field(
        proto.INT64,
        number=15,
    )
    bytes_failed_to_delete_from_sink: int = proto.Field(
        proto.INT64,
        number=16,
    )
    directories_found_from_source: int = proto.Field(
        proto.INT64,
        number=17,
    )
    directories_failed_to_list_from_source: int = proto.Field(
        proto.INT64,
        number=18,
    )
    directories_successfully_listed_from_source: int = proto.Field(
        proto.INT64,
        number=19,
    )
    intermediate_objects_cleaned_up: int = proto.Field(
        proto.INT64,
        number=22,
    )
    intermediate_objects_failed_cleaned_up: int = proto.Field(
        proto.INT64,
        number=23,
    )


class NotificationConfig(proto.Message):
    r"""Specification to configure notifications published to Pub/Sub.
    Notifications are published to the customer-provided topic using the
    following ``PubsubMessage.attributes``:

    - ``"eventType"``: one of the
      [EventType][google.storagetransfer.v1.NotificationConfig.EventType]
      values
    - ``"payloadFormat"``: one of the
      [PayloadFormat][google.storagetransfer.v1.NotificationConfig.PayloadFormat]
      values
    - ``"projectId"``: the
      [project_id][google.storagetransfer.v1.TransferOperation.project_id]
      of the ``TransferOperation``
    - ``"transferJobName"``: the
      [transfer_job_name][google.storagetransfer.v1.TransferOperation.transfer_job_name]
      of the ``TransferOperation``
    - ``"transferOperationName"``: the
      [name][google.storagetransfer.v1.TransferOperation.name] of the
      ``TransferOperation``

    The ``PubsubMessage.data`` contains a
    [TransferOperation][google.storagetransfer.v1.TransferOperation]
    resource formatted according to the specified ``PayloadFormat``.

    Attributes:
        pubsub_topic (str):
            Required. The ``Topic.name`` of the Pub/Sub topic to which
            to publish notifications. Must be of the format:
            ``projects/{project}/topics/{topic}``. Not matching this
            format results in an
            [INVALID_ARGUMENT][google.rpc.Code.INVALID_ARGUMENT] error.
        event_types (MutableSequence[google.cloud.storage_transfer_v1.types.NotificationConfig.EventType]):
            Event types for which a notification is
            desired. If empty, send notifications for all
            event types.
        payload_format (google.cloud.storage_transfer_v1.types.NotificationConfig.PayloadFormat):
            Required. The desired format of the
            notification message payloads.
    """

    class EventType(proto.Enum):
        r"""Enum for specifying event types for which notifications are
        to be published.

        Additional event types may be added in the future. Clients
        should either safely ignore unrecognized event types or
        explicitly specify which event types they are prepared to
        accept.

        Values:
            EVENT_TYPE_UNSPECIFIED (0):
                Illegal value, to avoid allowing a default.
            TRANSFER_OPERATION_SUCCESS (1):
                ``TransferOperation`` completed with status
                [SUCCESS][google.storagetransfer.v1.TransferOperation.Status.SUCCESS].
            TRANSFER_OPERATION_FAILED (2):
                ``TransferOperation`` completed with status
                [FAILED][google.storagetransfer.v1.TransferOperation.Status.FAILED].
            TRANSFER_OPERATION_ABORTED (3):
                ``TransferOperation`` completed with status
                [ABORTED][google.storagetransfer.v1.TransferOperation.Status.ABORTED].
        """

        EVENT_TYPE_UNSPECIFIED = 0
        TRANSFER_OPERATION_SUCCESS = 1
        TRANSFER_OPERATION_FAILED = 2
        TRANSFER_OPERATION_ABORTED = 3

    class PayloadFormat(proto.Enum):
        r"""Enum for specifying the format of a notification message's
        payload.

        Values:
            PAYLOAD_FORMAT_UNSPECIFIED (0):
                Illegal value, to avoid allowing a default.
            NONE (1):
                No payload is included with the notification.
            JSON (2):
                ``TransferOperation`` is `formatted as a JSON
                response <https://developers.google.com/protocol-buffers/docs/proto3#json>`__,
                in application/json.
        """

        PAYLOAD_FORMAT_UNSPECIFIED = 0
        NONE = 1
        JSON = 2

    pubsub_topic: str = proto.Field(
        proto.STRING,
        number=1,
    )
    event_types: MutableSequence[EventType] = proto.RepeatedField(
        proto.ENUM,
        number=2,
        enum=EventType,
    )
    payload_format: PayloadFormat = proto.Field(
        proto.ENUM,
        number=3,
        enum=PayloadFormat,
    )


class LoggingConfig(proto.Message):
    r"""Specifies the logging behavior for transfer operations.

    Logs can be sent to Cloud Logging for all transfer types. See `Read
    transfer
    logs <https://cloud.google.com/storage-transfer/docs/read-transfer-logs>`__
    for details.

    Attributes:
        log_actions (MutableSequence[google.cloud.storage_transfer_v1.types.LoggingConfig.LoggableAction]):
            Specifies the actions to be logged. If empty,
            no logs are generated.
        log_action_states (MutableSequence[google.cloud.storage_transfer_v1.types.LoggingConfig.LoggableActionState]):
            States in which ``log_actions`` are logged. If empty, no
            logs are generated.
        enable_onprem_gcs_transfer_logs (bool):
            For PosixFilesystem transfers, enables `file system transfer
            logs <https://cloud.google.com/storage-transfer/docs/on-prem-transfer-log-format>`__
            instead of, or in addition to, Cloud Logging.

            This option ignores [LoggableAction] and
            [LoggableActionState]. If these are set, Cloud Logging will
            also be enabled for this transfer.
    """

    class LoggableAction(proto.Enum):
        r"""Loggable actions.

        Values:
            LOGGABLE_ACTION_UNSPECIFIED (0):
                Default value. This value is unused.
            FIND (1):
                Listing objects in a bucket.
            DELETE (2):
                Deleting objects at the source or the
                destination.
            COPY (3):
                Copying objects to the destination.
        """

        LOGGABLE_ACTION_UNSPECIFIED = 0
        FIND = 1
        DELETE = 2
        COPY = 3

    class LoggableActionState(proto.Enum):
        r"""Loggable action states.

        Values:
            LOGGABLE_ACTION_STATE_UNSPECIFIED (0):
                Default value. This value is unused.
            SUCCEEDED (1):
                ``LoggableAction`` completed successfully. ``SUCCEEDED``
                actions are logged as
                [INFO][google.logging.type.LogSeverity.INFO].
            FAILED (2):
                ``LoggableAction`` terminated in an error state. ``FAILED``
                actions are logged as
                [ERROR][google.logging.type.LogSeverity.ERROR].
            SKIPPED (3):
                The ``COPY`` action was skipped for this file. Only
                supported for agent-based transfers. ``SKIPPED`` actions are
                logged as [INFO][google.logging.type.LogSeverity.INFO].
        """

        LOGGABLE_ACTION_STATE_UNSPECIFIED = 0
        SUCCEEDED = 1
        FAILED = 2
        SKIPPED = 3

    log_actions: MutableSequence[LoggableAction] = proto.RepeatedField(
        proto.ENUM,
        number=1,
        enum=LoggableAction,
    )
    log_action_states: MutableSequence[LoggableActionState] = proto.RepeatedField(
        proto.ENUM,
        number=2,
        enum=LoggableActionState,
    )
    enable_onprem_gcs_transfer_logs: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class TransferOperation(proto.Message):
    r"""A description of the execution of a transfer.

    Attributes:
        name (str):
            A globally unique ID assigned by the system.
        project_id (str):
            The ID of the Google Cloud project that owns
            the operation.
        transfer_spec (google.cloud.storage_transfer_v1.types.TransferSpec):
            Transfer specification.
        notification_config (google.cloud.storage_transfer_v1.types.NotificationConfig):
            Notification configuration.
        logging_config (google.cloud.storage_transfer_v1.types.LoggingConfig):
            Cloud Logging configuration.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Start time of this transfer execution.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            End time of this transfer execution.
        status (google.cloud.storage_transfer_v1.types.TransferOperation.Status):
            Status of the transfer operation.
        counters (google.cloud.storage_transfer_v1.types.TransferCounters):
            Information about the progress of the
            transfer operation.
        error_breakdowns (MutableSequence[google.cloud.storage_transfer_v1.types.ErrorSummary]):
            Summarizes errors encountered with sample
            error log entries.
        transfer_job_name (str):
            The name of the transfer job that triggers
            this transfer operation.
    """

    class Status(proto.Enum):
        r"""The status of a TransferOperation.

        Values:
            STATUS_UNSPECIFIED (0):
                Zero is an illegal value.
            IN_PROGRESS (1):
                In progress.
            PAUSED (2):
                Paused.
            SUCCESS (3):
                Completed successfully.
            FAILED (4):
                Terminated due to an unrecoverable failure.
            ABORTED (5):
                Aborted by the user.
            QUEUED (6):
                Temporarily delayed by the system. No user
                action is required.
            SUSPENDING (7):
                The operation is suspending and draining the
                ongoing work to completion.
        """

        STATUS_UNSPECIFIED = 0
        IN_PROGRESS = 1
        PAUSED = 2
        SUCCESS = 3
        FAILED = 4
        ABORTED = 5
        QUEUED = 6
        SUSPENDING = 7

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    transfer_spec: "TransferSpec" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="TransferSpec",
    )
    notification_config: "NotificationConfig" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="NotificationConfig",
    )
    logging_config: "LoggingConfig" = proto.Field(
        proto.MESSAGE,
        number=12,
        message="LoggingConfig",
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    status: Status = proto.Field(
        proto.ENUM,
        number=6,
        enum=Status,
    )
    counters: "TransferCounters" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="TransferCounters",
    )
    error_breakdowns: MutableSequence["ErrorSummary"] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message="ErrorSummary",
    )
    transfer_job_name: str = proto.Field(
        proto.STRING,
        number=9,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
