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
import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.alloydb_v1.types import data_model, resources

__protobuf__ = proto.module(
    package="google.cloud.alloydb.v1",
    manifest={
        "ListClustersRequest",
        "ListClustersResponse",
        "GetClusterRequest",
        "CreateSecondaryClusterRequest",
        "CreateClusterRequest",
        "UpdateClusterRequest",
        "GcsDestination",
        "ExportClusterRequest",
        "ExportClusterResponse",
        "ImportClusterRequest",
        "ImportClusterResponse",
        "UpgradeClusterRequest",
        "UpgradeClusterResponse",
        "DeleteClusterRequest",
        "SwitchoverClusterRequest",
        "PromoteClusterRequest",
        "RestoreClusterRequest",
        "ListInstancesRequest",
        "ListInstancesResponse",
        "GetInstanceRequest",
        "CreateInstanceRequest",
        "CreateSecondaryInstanceRequest",
        "CreateInstanceRequests",
        "BatchCreateInstancesRequest",
        "BatchCreateInstancesResponse",
        "BatchCreateInstancesMetadata",
        "BatchCreateInstanceStatus",
        "UpdateInstanceRequest",
        "DeleteInstanceRequest",
        "FailoverInstanceRequest",
        "InjectFaultRequest",
        "RestartInstanceRequest",
        "ExecuteSqlRequest",
        "ExecuteSqlResponse",
        "ExecuteSqlMetadata",
        "ListBackupsRequest",
        "ListBackupsResponse",
        "GetBackupRequest",
        "CreateBackupRequest",
        "UpdateBackupRequest",
        "DeleteBackupRequest",
        "ListSupportedDatabaseFlagsRequest",
        "ListSupportedDatabaseFlagsResponse",
        "GenerateClientCertificateRequest",
        "GenerateClientCertificateResponse",
        "GetConnectionInfoRequest",
        "OperationMetadata",
        "UpgradeClusterStatus",
        "ListUsersRequest",
        "ListUsersResponse",
        "GetUserRequest",
        "CreateUserRequest",
        "UpdateUserRequest",
        "DeleteUserRequest",
        "ListDatabasesRequest",
        "ListDatabasesResponse",
    },
)


class ListClustersRequest(proto.Message):
    r"""Message for requesting list of Clusters

    Attributes:
        parent (str):
            Required. The name of the parent resource. For the required
            format, see the comment on the Cluster.name field.
            Additionally, you can perform an aggregated list operation
            by specifying a value with the following format:

            - projects/{project}/locations/-
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            A token identifying a page of results the
            server should return.
        filter (str):
            Optional. Filtering results
        order_by (str):
            Optional. Hint for how to order the results
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


class ListClustersResponse(proto.Message):
    r"""Message for response to listing Clusters

    Attributes:
        clusters (MutableSequence[google.cloud.alloydb_v1.types.Cluster]):
            The list of Cluster
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    clusters: MutableSequence[resources.Cluster] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Cluster,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetClusterRequest(proto.Message):
    r"""Message for getting a Cluster

    Attributes:
        name (str):
            Required. The name of the resource. For the
            required format, see the comment on the
            Cluster.name field.
        view (google.cloud.alloydb_v1.types.ClusterView):
            Optional. The view of the cluster to return.
            Returns all default fields if not set.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: resources.ClusterView = proto.Field(
        proto.ENUM,
        number=2,
        enum=resources.ClusterView,
    )


class CreateSecondaryClusterRequest(proto.Message):
    r"""

    Attributes:
        parent (str):
            Required. The location of the new cluster.
            For the required format, see the comment on the
            Cluster.name field.
        cluster_id (str):
            Required. ID of the requesting object (the
            secondary cluster).
        cluster (google.cloud.alloydb_v1.types.Cluster):
            Required. Configuration of the requesting
            object (the secondary cluster).
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server ignores
            the request if it has already been completed.
            The server guarantees that for at least 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if the original
            operation with the same request ID was received,
            and if so, ignores the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        validate_only (bool):
            Optional. If set, performs request
            validation, for example, permission checks and
            any other type of validation, but does not
            actually execute the create request.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cluster_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    cluster: resources.Cluster = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.Cluster,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=5,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


class CreateClusterRequest(proto.Message):
    r"""Message for creating a Cluster

    Attributes:
        parent (str):
            Required. The location of the new cluster.
            For the required format, see the comment on the
            Cluster.name field.
        cluster_id (str):
            Required. ID of the requesting object.
        cluster (google.cloud.alloydb_v1.types.Cluster):
            Required. The resource being created
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server ignores
            the request if it has already been completed.
            The server guarantees that for at least 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if the original
            operation with the same request ID was received,
            and if so, ignores the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        validate_only (bool):
            Optional. If set, performs request
            validation, for example, permission checks and
            any other type of validation, but does not
            actually execute the create request.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cluster_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    cluster: resources.Cluster = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.Cluster,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class UpdateClusterRequest(proto.Message):
    r"""Message for updating a Cluster

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the Cluster resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        cluster (google.cloud.alloydb_v1.types.Cluster):
            Required. The resource being updated
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server ignores
            the request if it has already been completed.
            The server guarantees that for at least 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if the original
            operation with the same request ID was received,
            and if so, ignores the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        validate_only (bool):
            Optional. If set, performs request
            validation, for example, permission checks and
            any other type of validation, but does not
            actually execute the create request.
        allow_missing (bool):
            Optional. If set to true, update succeeds even if cluster is
            not found. In that case, a new cluster is created and
            ``update_mask`` is ignored.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    cluster: resources.Cluster = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.Cluster,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class GcsDestination(proto.Message):
    r"""Destination for Export. Export will be done to cloud storage.

    Attributes:
        uri (str):
            Required. The path to the file in Google Cloud Storage where
            the export will be stored. The URI is in the form
            ``gs://bucketName/fileName``.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ExportClusterRequest(proto.Message):
    r"""Export cluster request.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_destination (google.cloud.alloydb_v1.types.GcsDestination):
            Required. Option to export data to cloud
            storage.

            This field is a member of `oneof`_ ``destination``.
        csv_export_options (google.cloud.alloydb_v1.types.ExportClusterRequest.CsvExportOptions):
            Options for exporting data in CSV format.
            Required field to be set for CSV file type.

            This field is a member of `oneof`_ ``export_options``.
        sql_export_options (google.cloud.alloydb_v1.types.ExportClusterRequest.SqlExportOptions):
            Options for exporting data in SQL format.
            Required field to be set for SQL file type.

            This field is a member of `oneof`_ ``export_options``.
        name (str):
            Required. The resource name of the cluster.
        database (str):
            Required. Name of the database where the export command will
            be executed. Note - Value provided should be the same as
            expected from ``SELECT current_database();`` and NOT as a
            resource reference.
    """

    class CsvExportOptions(proto.Message):
        r"""Options for exporting data in CSV format.

        Attributes:
            select_query (str):
                Required. The SELECT query used to extract
                the data.
            field_delimiter (str):
                Optional. Specifies the character that
                separates columns within each row (line) of the
                file. The default is comma. The value of this
                argument has to be a character in Hex ASCII
                Code.
            quote_character (str):
                Optional. Specifies the quoting character to
                be used when a data value is quoted. The default
                is double-quote. The value of this argument has
                to be a character in Hex ASCII Code.
            escape_character (str):
                Optional. Specifies the character that should
                appear before a data character that needs to be
                escaped. The default is the same as quote
                character. The value of this argument has to be
                a character in Hex ASCII Code.
        """

        select_query: str = proto.Field(
            proto.STRING,
            number=1,
        )
        field_delimiter: str = proto.Field(
            proto.STRING,
            number=2,
        )
        quote_character: str = proto.Field(
            proto.STRING,
            number=3,
        )
        escape_character: str = proto.Field(
            proto.STRING,
            number=4,
        )

    class SqlExportOptions(proto.Message):
        r"""Options for exporting data in SQL format.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            tables (MutableSequence[str]):
                Optional. Tables to export from.
            schema_only (bool):
                Optional. If true, only export the schema.

                This field is a member of `oneof`_ ``_schema_only``.
            clean_target_objects (bool):
                Optional. If true, output commands to DROP
                all the dumped database objects prior to
                outputting the commands for creating them.

                This field is a member of `oneof`_ ``_clean_target_objects``.
            if_exist_target_objects (bool):
                Optional. If true, use DROP ... IF EXISTS commands to check
                for the object's existence before dropping it in
                clean_target_objects mode.

                This field is a member of `oneof`_ ``_if_exist_target_objects``.
        """

        tables: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        schema_only: bool = proto.Field(
            proto.BOOL,
            number=2,
            optional=True,
        )
        clean_target_objects: bool = proto.Field(
            proto.BOOL,
            number=3,
            optional=True,
        )
        if_exist_target_objects: bool = proto.Field(
            proto.BOOL,
            number=4,
            optional=True,
        )

    gcs_destination: "GcsDestination" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="destination",
        message="GcsDestination",
    )
    csv_export_options: CsvExportOptions = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="export_options",
        message=CsvExportOptions,
    )
    sql_export_options: SqlExportOptions = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="export_options",
        message=SqlExportOptions,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    database: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ExportClusterResponse(proto.Message):
    r"""Response of export cluster rpc.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_destination (google.cloud.alloydb_v1.types.GcsDestination):
            Required. Option to export data to cloud
            storage.

            This field is a member of `oneof`_ ``destination``.
    """

    gcs_destination: "GcsDestination" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="destination",
        message="GcsDestination",
    )


class ImportClusterRequest(proto.Message):
    r"""Import cluster request.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        sql_import_options (google.cloud.alloydb_v1.types.ImportClusterRequest.SqlImportOptions):
            Options for importing data in SQL format.

            This field is a member of `oneof`_ ``import_options``.
        csv_import_options (google.cloud.alloydb_v1.types.ImportClusterRequest.CsvImportOptions):
            Options for importing data in CSV format.

            This field is a member of `oneof`_ ``import_options``.
        name (str):
            Required. The resource name of the cluster.
        gcs_uri (str):
            Required. The path to the file in Google Cloud Storage where
            the source file for import will be stored. The URI is in the
            form ``gs://bucketName/fileName``.
        database (str):
            Optional. Name of the database to which the import will be
            done. For import from SQL file, this is required only if the
            file does not specify a database. Note - Value provided
            should be the same as expected from
            ``SELECT current_database();`` and NOT as a resource
            reference.
        user (str):
            Optional. Database user to be used for importing the data.
            Note - Value provided should be the same as expected from
            ``SELECT current_user;`` and NOT as a resource reference.
    """

    class SqlImportOptions(proto.Message):
        r"""Options for importing data in SQL format."""

    class CsvImportOptions(proto.Message):
        r"""Options for importing data in CSV format.

        Attributes:
            table (str):
                Required. The database table to import CSV
                file into.
            columns (MutableSequence[str]):
                Optional. The columns to which CSV data is
                imported. If not specified, all columns of the
                database table are loaded with CSV data.
            field_delimiter (str):
                Optional. Specifies the character that
                separates columns within each row (line) of the
                file. The default is comma. The value of this
                argument has to be a character in Hex ASCII
                Code.
            quote_character (str):
                Optional. Specifies the quoting character to
                be used when a data value is quoted. The default
                is double-quote. The value of this argument has
                to be a character in Hex ASCII Code.
            escape_character (str):
                Optional. Specifies the character that should
                appear before a data character that needs to be
                escaped. The default is same as quote character.
                The value of this argument has to be a character
                in Hex ASCII Code.
        """

        table: str = proto.Field(
            proto.STRING,
            number=1,
        )
        columns: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )
        field_delimiter: str = proto.Field(
            proto.STRING,
            number=3,
        )
        quote_character: str = proto.Field(
            proto.STRING,
            number=4,
        )
        escape_character: str = proto.Field(
            proto.STRING,
            number=5,
        )

    sql_import_options: SqlImportOptions = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="import_options",
        message=SqlImportOptions,
    )
    csv_import_options: CsvImportOptions = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="import_options",
        message=CsvImportOptions,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    gcs_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    database: str = proto.Field(
        proto.STRING,
        number=3,
    )
    user: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ImportClusterResponse(proto.Message):
    r"""Response of import rpc.

    Attributes:
        bytes_downloaded (int):
            Required. Size of the object downloaded from
            Google Cloud Storage in bytes.
    """

    bytes_downloaded: int = proto.Field(
        proto.INT64,
        number=1,
    )


class UpgradeClusterRequest(proto.Message):
    r"""Upgrades a cluster.

    Attributes:
        name (str):
            Required. The resource name of the cluster.
        version (google.cloud.alloydb_v1.types.DatabaseVersion):
            Required. The version the cluster is going to
            be upgraded to.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server ignores
            the request if it has already been completed.
            The server guarantees that for at least 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if the original
            operation with the same request ID was received,
            and if so, ignores the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        validate_only (bool):
            Optional. If set, performs request
            validation, for example, permission checks and
            any other type of validation, but does not
            actually execute the create request.
        etag (str):
            Optional. The current etag of the Cluster.
            If an etag is provided and does not match the
            current etag of the Cluster, upgrade will be
            blocked and an ABORTED error will be returned.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    version: resources.DatabaseVersion = proto.Field(
        proto.ENUM,
        number=2,
        enum=resources.DatabaseVersion,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=5,
    )


class UpgradeClusterResponse(proto.Message):
    r"""UpgradeClusterResponse contains the response for upgrade
    cluster operation.

    Attributes:
        status (google.cloud.alloydb_v1.types.UpgradeClusterResponse.Status):
            Status of upgrade operation.
        message (str):
            A user friendly message summarising the
            upgrade operation details and the next steps for
            the user if there is any.
        cluster_upgrade_details (MutableSequence[google.cloud.alloydb_v1.types.UpgradeClusterResponse.ClusterUpgradeDetails]):
            Array of upgrade details for the current
            cluster and all the secondary clusters
            associated with this cluster.
    """

    class Status(proto.Enum):
        r"""Status of upgrade operation.

        Values:
            STATUS_UNSPECIFIED (0):
                Unspecified status.
            NOT_STARTED (4):
                Not started.
            IN_PROGRESS (5):
                In progress.
            SUCCESS (1):
                Operation succeeded.
            FAILED (2):
                Operation failed.
            PARTIAL_SUCCESS (3):
                Operation partially succeeded.
            CANCEL_IN_PROGRESS (6):
                Cancel is in progress.
            CANCELLED (7):
                Cancellation complete.
        """

        STATUS_UNSPECIFIED = 0
        NOT_STARTED = 4
        IN_PROGRESS = 5
        SUCCESS = 1
        FAILED = 2
        PARTIAL_SUCCESS = 3
        CANCEL_IN_PROGRESS = 6
        CANCELLED = 7

    class Stage(proto.Enum):
        r"""Stage in the upgrade.

        Values:
            STAGE_UNSPECIFIED (0):
                Unspecified stage.
            ALLOYDB_PRECHECK (1):
                Pre-upgrade custom checks, not covered by pg_upgrade.
            PG_UPGRADE_CHECK (2):
                Pre-upgrade pg_upgrade checks.
            PREPARE_FOR_UPGRADE (5):
                Clone the original cluster.
            PRIMARY_INSTANCE_UPGRADE (3):
                Upgrade the primary instance(downtime).
            READ_POOL_INSTANCES_UPGRADE (4):
                This stage is read pool upgrade.
            ROLLBACK (6):
                Rollback in case of critical failures.
            CLEANUP (7):
                Cleanup.
        """

        STAGE_UNSPECIFIED = 0
        ALLOYDB_PRECHECK = 1
        PG_UPGRADE_CHECK = 2
        PREPARE_FOR_UPGRADE = 5
        PRIMARY_INSTANCE_UPGRADE = 3
        READ_POOL_INSTANCES_UPGRADE = 4
        ROLLBACK = 6
        CLEANUP = 7

    class StageInfo(proto.Message):
        r"""Stage information for different stages in the upgrade
        process.

        Attributes:
            stage (google.cloud.alloydb_v1.types.UpgradeClusterResponse.Stage):
                The stage.
            status (google.cloud.alloydb_v1.types.UpgradeClusterResponse.Status):
                Status of the stage.
            logs_url (str):
                logs_url is the URL for the logs associated with a stage if
                that stage has logs. Right now, only three stages have logs:
                ALLOYDB_PRECHECK, PG_UPGRADE_CHECK,
                PRIMARY_INSTANCE_UPGRADE.
        """

        stage: "UpgradeClusterResponse.Stage" = proto.Field(
            proto.ENUM,
            number=1,
            enum="UpgradeClusterResponse.Stage",
        )
        status: "UpgradeClusterResponse.Status" = proto.Field(
            proto.ENUM,
            number=2,
            enum="UpgradeClusterResponse.Status",
        )
        logs_url: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class InstanceUpgradeDetails(proto.Message):
        r"""Details regarding the upgrade of instances associated with a
        cluster.

        Attributes:
            name (str):
                Normalized name of the instance.
            upgrade_status (google.cloud.alloydb_v1.types.UpgradeClusterResponse.Status):
                Upgrade status of the instance.
            instance_type (google.cloud.alloydb_v1.types.Instance.InstanceType):
                Instance type.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        upgrade_status: "UpgradeClusterResponse.Status" = proto.Field(
            proto.ENUM,
            number=2,
            enum="UpgradeClusterResponse.Status",
        )
        instance_type: resources.Instance.InstanceType = proto.Field(
            proto.ENUM,
            number=3,
            enum=resources.Instance.InstanceType,
        )

    class ClusterUpgradeDetails(proto.Message):
        r"""Upgrade details of a cluster. This cluster can be primary or
        secondary.

        Attributes:
            name (str):
                Normalized name of the cluster
            upgrade_status (google.cloud.alloydb_v1.types.UpgradeClusterResponse.Status):
                Upgrade status of the cluster.
            cluster_type (google.cloud.alloydb_v1.types.Cluster.ClusterType):
                Cluster type which can either be primary or
                secondary.
            database_version (google.cloud.alloydb_v1.types.DatabaseVersion):
                Database version of the cluster after the
                upgrade operation. This will be the target
                version if the upgrade was successful otherwise
                it remains the same as that before the upgrade
                operation.
            stage_info (MutableSequence[google.cloud.alloydb_v1.types.UpgradeClusterResponse.StageInfo]):
                Array containing stage info associated with
                this cluster.
            instance_upgrade_details (MutableSequence[google.cloud.alloydb_v1.types.UpgradeClusterResponse.InstanceUpgradeDetails]):
                Upgrade details of the instances directly
                associated with this cluster.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        upgrade_status: "UpgradeClusterResponse.Status" = proto.Field(
            proto.ENUM,
            number=2,
            enum="UpgradeClusterResponse.Status",
        )
        cluster_type: resources.Cluster.ClusterType = proto.Field(
            proto.ENUM,
            number=3,
            enum=resources.Cluster.ClusterType,
        )
        database_version: resources.DatabaseVersion = proto.Field(
            proto.ENUM,
            number=4,
            enum=resources.DatabaseVersion,
        )
        stage_info: MutableSequence["UpgradeClusterResponse.StageInfo"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=5,
                message="UpgradeClusterResponse.StageInfo",
            )
        )
        instance_upgrade_details: MutableSequence[
            "UpgradeClusterResponse.InstanceUpgradeDetails"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=6,
            message="UpgradeClusterResponse.InstanceUpgradeDetails",
        )

    status: Status = proto.Field(
        proto.ENUM,
        number=1,
        enum=Status,
    )
    message: str = proto.Field(
        proto.STRING,
        number=2,
    )
    cluster_upgrade_details: MutableSequence[ClusterUpgradeDetails] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message=ClusterUpgradeDetails,
        )
    )


class DeleteClusterRequest(proto.Message):
    r"""Message for deleting a Cluster

    Attributes:
        name (str):
            Required. The name of the resource. For the
            required format, see the comment on the
            Cluster.name field.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server ignores
            the request if it has already been completed.
            The server guarantees that for at least 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if the original
            operation with the same request ID was received,
            and if so, ignores the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        etag (str):
            Optional. The current etag of the Cluster.
            If an etag is provided and does not match the
            current etag of the Cluster, deletion will be
            blocked and an ABORTED error will be returned.
        validate_only (bool):
            Optional. If set, performs request
            validation, for example, permission checks and
            any other type of validation, but does not
            actually execute the create request.
        force (bool):
            Optional. Whether to cascade delete child
            instances for given cluster.
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
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class SwitchoverClusterRequest(proto.Message):
    r"""Message for switching over to a cluster

    Attributes:
        name (str):
            Required. The name of the resource. For the
            required format, see the comment on the
            Cluster.name field
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server ignores
            the request if it has already been completed.
            The server guarantees that for at least 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if the original
            operation with the same request ID was received,
            and if so, ignores the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        validate_only (bool):
            Optional. If set, performs request
            validation, for example, permission checks and
            any other type of validation, but does not
            actually execute the create request.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class PromoteClusterRequest(proto.Message):
    r"""Message for promoting a Cluster

    Attributes:
        name (str):
            Required. The name of the resource. For the
            required format, see the comment on the
            Cluster.name field
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server ignores
            the request if it has already been completed.
            The server guarantees that for at least 60
            minutes since the first request.

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
        etag (str):
            Optional. The current etag of the Cluster.
            If an etag is provided and does not match the
            current etag of the Cluster, deletion will be
            blocked and an ABORTED error will be returned.
        validate_only (bool):
            Optional. If set, performs request
            validation, for example, permission checks and
            any other type of validation, but does not
            actually execute the create request.
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
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class RestoreClusterRequest(proto.Message):
    r"""Message for restoring a Cluster from a backup or another cluster at
    a given point in time. NEXT_ID: 11

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        backup_source (google.cloud.alloydb_v1.types.BackupSource):
            Backup source.

            This field is a member of `oneof`_ ``source``.
        continuous_backup_source (google.cloud.alloydb_v1.types.ContinuousBackupSource):
            ContinuousBackup source. Continuous backup
            needs to be enabled in the source cluster for
            this operation to succeed.

            This field is a member of `oneof`_ ``source``.
        parent (str):
            Required. The name of the parent resource.
            For the required format, see the comment on the
            Cluster.name field.
        cluster_id (str):
            Required. ID of the requesting object.
        cluster (google.cloud.alloydb_v1.types.Cluster):
            Required. The resource being created
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server ignores
            the request if it has already been completed.
            The server guarantees that for at least 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if the original
            operation with the same request ID was received,
            and if so, ignores the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        validate_only (bool):
            Optional. If set, performs request
            validation, for example, permission checks and
            any other type of validation, but does not
            actually execute the create request.
    """

    backup_source: resources.BackupSource = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="source",
        message=resources.BackupSource,
    )
    continuous_backup_source: resources.ContinuousBackupSource = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="source",
        message=resources.ContinuousBackupSource,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cluster_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    cluster: resources.Cluster = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.Cluster,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=5,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


class ListInstancesRequest(proto.Message):
    r"""Message for requesting list of Instances

    Attributes:
        parent (str):
            Required. The name of the parent resource. For the required
            format, see the comment on the Instance.name field.
            Additionally, you can perform an aggregated list operation
            by specifying a value with one of the following formats:

            - projects/{project}/locations/-/clusters/-
            - projects/{project}/locations/{region}/clusters/-
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            A token identifying a page of results the
            server should return.
        filter (str):
            Optional. Filtering results
        order_by (str):
            Optional. Hint for how to order the results
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
        instances (MutableSequence[google.cloud.alloydb_v1.types.Instance]):
            The list of Instance
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    instances: MutableSequence[resources.Instance] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Instance,
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
            Required. The name of the resource. For the
            required format, see the comment on the
            Instance.name field.
        view (google.cloud.alloydb_v1.types.InstanceView):
            The view of the instance to return.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: resources.InstanceView = proto.Field(
        proto.ENUM,
        number=2,
        enum=resources.InstanceView,
    )


class CreateInstanceRequest(proto.Message):
    r"""Message for creating a Instance

    Attributes:
        parent (str):
            Required. The name of the parent resource.
            For the required format, see the comment on the
            Instance.name field.
        instance_id (str):
            Required. ID of the requesting object.
        instance (google.cloud.alloydb_v1.types.Instance):
            Required. The resource being created
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server ignores
            the request if it has already been completed.
            The server guarantees that for at least 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if the original
            operation with the same request ID was received,
            and if so, ignores the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        validate_only (bool):
            Optional. If set, performs request
            validation, for example, permission checks and
            any other type of validation, but does not
            actually execute the create request.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    instance: resources.Instance = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.Instance,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class CreateSecondaryInstanceRequest(proto.Message):
    r"""Message for creating a Secondary Instance

    Attributes:
        parent (str):
            Required. The name of the parent resource.
            For the required format, see the comment on the
            Instance.name field.
        instance_id (str):
            Required. ID of the requesting object.
        instance (google.cloud.alloydb_v1.types.Instance):
            Required. The resource being created
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server ignores
            the request if it has already been completed.
            The server guarantees that for at least 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if the original
            operation with the same request ID was received,
            and if so, ignores the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        validate_only (bool):
            Optional. If set, performs request
            validation, for example, permission checks and
            any other type of validation, but does not
            actually execute the create request.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    instance: resources.Instance = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.Instance,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class CreateInstanceRequests(proto.Message):
    r"""See usage below for notes.

    Attributes:
        create_instance_requests (MutableSequence[google.cloud.alloydb_v1.types.CreateInstanceRequest]):
            Required. Primary and read replica instances
            to be created. This list should not be empty.
    """

    create_instance_requests: MutableSequence["CreateInstanceRequest"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="CreateInstanceRequest",
        )
    )


class BatchCreateInstancesRequest(proto.Message):
    r"""Message for creating a batch of instances under the specified
    cluster.

    Attributes:
        parent (str):
            Required. The name of the parent resource.
        requests (google.cloud.alloydb_v1.types.CreateInstanceRequests):
            Required. Resources being created.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server ignores
            the request if it has already been completed.
            The server guarantees that for at least 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if the original
            operation with the same request ID was received,
            and if so, ignores the second request. This
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
    requests: "CreateInstanceRequests" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="CreateInstanceRequests",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class BatchCreateInstancesResponse(proto.Message):
    r"""Message for creating batches of instances in a cluster.

    Attributes:
        instances (MutableSequence[google.cloud.alloydb_v1.types.Instance]):
            Created instances.
    """

    instances: MutableSequence[resources.Instance] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Instance,
    )


class BatchCreateInstancesMetadata(proto.Message):
    r"""Message for metadata that is specific to BatchCreateInstances API.
    NEXT_ID: 3

    Attributes:
        instance_targets (MutableSequence[str]):
            The instances being created in the API call.
            Each string in this list is the server defined
            resource path for target instances in the
            request and for the format of each string, see
            the comment on the Instance.name field.
        instance_statuses (MutableMapping[str, google.cloud.alloydb_v1.types.BatchCreateInstanceStatus]):
            A map representing state of the instances involved in the
            BatchCreateInstances operation during the operation
            execution. The instance state will be in STATE_UNSPECIFIED
            state if the instance has not yet been picked up for
            processing. The key of the map is the name of the instance
            resource. For the format, see the comment on the
            Instance.name field.
    """

    instance_targets: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    instance_statuses: MutableMapping[str, "BatchCreateInstanceStatus"] = (
        proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=2,
            message="BatchCreateInstanceStatus",
        )
    )


class BatchCreateInstanceStatus(proto.Message):
    r"""Message for current status of an instance in the
    BatchCreateInstances operation. For example, lets say a
    BatchCreateInstances workflow has 4 instances, Instance1 through
    Instance4. Lets also assume that 2 instances succeeded but the third
    failed to create and the 4th was never picked up for creation
    because of failure of the previous one. Then, resulting states would
    look something like:

    1. Instance1 = ROLLED_BACK
    2. Instance2 = ROLLED_BACK
    3. Instance3 = FAILED
    4. Instance4 = FAILED

    However, while the operation is running, the instance might be in
    other states including PENDING_CREATE, ACTIVE, DELETING and
    CREATING. The states / do not get further updated once the operation
    is done.

    Attributes:
        state (google.cloud.alloydb_v1.types.BatchCreateInstanceStatus.State):
            The current state of an instance involved in the batch
            create operation. Once the operation is complete, the final
            state of the instances in the LRO can be one of:

            1. ACTIVE, indicating that instances were created
               successfully
            2. FAILED, indicating that a particular instance failed
               creation
            3. ROLLED_BACK indicating that although the instance was
               created successfully, it had to be rolled back and
               deleted due to failure in other steps of the workflow.
        error_msg (str):
            DEPRECATED - Use the error field instead.
            Error, if any error occurred and is available,
            during instance creation.
        error (google.rpc.status_pb2.Status):
            The RPC status of the instance creation
            operation. This field will be present if an
            error happened during the instance creation.
        type_ (google.cloud.alloydb_v1.types.Instance.InstanceType):

    """

    class State(proto.Enum):
        r"""State contains all valid instance states for the
        BatchCreateInstances operation. This is mainly used for status
        reporting through the LRO metadata.

        Values:
            STATE_UNSPECIFIED (0):
                The state of the instance is unknown.
            PENDING_CREATE (1):
                Instance is pending creation and has not yet
                been picked up for processing in the backend.
            READY (2):
                The instance is active and running.
            CREATING (3):
                The instance is being created.
            DELETING (4):
                The instance is being deleted.
            FAILED (5):
                The creation of the instance failed or a
                fatal error occurred during an operation on the
                instance or a batch of instances.
            ROLLED_BACK (6):
                The instance was created successfully, but
                was rolled back and deleted due to some other
                failure during BatchCreateInstances operation.
        """

        STATE_UNSPECIFIED = 0
        PENDING_CREATE = 1
        READY = 2
        CREATING = 3
        DELETING = 4
        FAILED = 5
        ROLLED_BACK = 6

    state: State = proto.Field(
        proto.ENUM,
        number=1,
        enum=State,
    )
    error_msg: str = proto.Field(
        proto.STRING,
        number=2,
    )
    error: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=4,
        message=status_pb2.Status,
    )
    type_: resources.Instance.InstanceType = proto.Field(
        proto.ENUM,
        number=3,
        enum=resources.Instance.InstanceType,
    )


class UpdateInstanceRequest(proto.Message):
    r"""Message for updating a Instance

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the Instance resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        instance (google.cloud.alloydb_v1.types.Instance):
            Required. The resource being updated
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server ignores
            the request if it has already been completed.
            The server guarantees that for at least 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if the original
            operation with the same request ID was received,
            and if so, ignores the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        validate_only (bool):
            Optional. If set, performs request
            validation, for example, permission checks and
            any other type of validation, but does not
            actually execute the create request.
        allow_missing (bool):
            Optional. If set to true, update succeeds even if instance
            is not found. In that case, a new instance is created and
            ``update_mask`` is ignored.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    instance: resources.Instance = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.Instance,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class DeleteInstanceRequest(proto.Message):
    r"""Message for deleting a Instance

    Attributes:
        name (str):
            Required. The name of the resource. For the
            required format, see the comment on the
            Instance.name field.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server ignores
            the request if it has already been completed.
            The server guarantees that for at least 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if the original
            operation with the same request ID was received,
            and if so, ignores the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        etag (str):
            Optional. The current etag of the Instance.
            If an etag is provided and does not match the
            current etag of the Instance, deletion will be
            blocked and an ABORTED error will be returned.
        validate_only (bool):
            Optional. If set, performs request
            validation, for example, permission checks and
            any other type of validation, but does not
            actually execute the create request.
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
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class FailoverInstanceRequest(proto.Message):
    r"""Message for triggering failover on an Instance

    Attributes:
        name (str):
            Required. The name of the resource. For the
            required format, see the comment on the
            Instance.name field.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server ignores
            the request if it has already been completed.
            The server guarantees that for at least 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if the original
            operation with the same request ID was received,
            and if so, ignores the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        validate_only (bool):
            Optional. If set, performs request
            validation, for example, permission checks and
            any other type of validation, but does not
            actually execute the create request.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class InjectFaultRequest(proto.Message):
    r"""Message for triggering fault injection on an instance

    Attributes:
        fault_type (google.cloud.alloydb_v1.types.InjectFaultRequest.FaultType):
            Required. The type of fault to be injected in
            an instance.
        name (str):
            Required. The name of the resource. For the
            required format, see the comment on the
            Instance.name field.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server ignores
            the request if it has already been completed.
            The server guarantees that for at least 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if the original
            operation with the same request ID was received,
            and if so, ignores the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        validate_only (bool):
            Optional. If set, performs request
            validation, for example, permission checks and
            any other type of validation, but does not
            actually execute the create request.
    """

    class FaultType(proto.Enum):
        r"""FaultType contains all valid types of faults that can be
        injected to an instance.

        Values:
            FAULT_TYPE_UNSPECIFIED (0):
                The fault type is unknown.
            STOP_VM (1):
                Stop the VM
        """

        FAULT_TYPE_UNSPECIFIED = 0
        STOP_VM = 1

    fault_type: FaultType = proto.Field(
        proto.ENUM,
        number=1,
        enum=FaultType,
    )
    name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class RestartInstanceRequest(proto.Message):
    r"""

    Attributes:
        name (str):
            Required. The name of the resource. For the
            required format, see the comment on the
            Instance.name field.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server ignores
            the request if it has already been completed.
            The server guarantees that for at least 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if the original
            operation with the same request ID was received,
            and if so, ignores the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        validate_only (bool):
            Optional. If set, performs request
            validation, for example, permission checks and
            any other type of validation, but does not
            actually execute the create request.
        node_ids (MutableSequence[str]):
            Optional. Full name of the nodes as obtained from
            INSTANCE_VIEW_FULL to restart upon. Applicable only to read
            instances.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    node_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )


class ExecuteSqlRequest(proto.Message):
    r"""Request for ExecuteSql rpc.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        password (str):
            Optional. The database native user’s
            password.

            This field is a member of `oneof`_ ``user_credential``.
        instance (str):
            Required. The instance where the SQL will be
            executed. For the required format, see the
            comment on the Instance.name field.
        database (str):
            Required. Name of the database where the query will be
            executed. Note - Value provided should be the same as
            expected from ``SELECT current_database();`` and NOT as a
            resource reference.
        user (str):
            Required. Database user to be used for executing the SQL.
            Note - Value provided should be the same as expected from
            ``SELECT current_user;`` and NOT as a resource reference.
        sql_statement (str):
            Required. SQL statement to execute on
            database. Any valid statement is permitted,
            including DDL, DML, DQL statements.
        validate_only (bool):
            Optional. If set, validates the sql statement
            by performing syntax and semantic validation and
            doesn't execute the query.
    """

    password: str = proto.Field(
        proto.STRING,
        number=5,
        oneof="user_credential",
    )
    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    database: str = proto.Field(
        proto.STRING,
        number=2,
    )
    user: str = proto.Field(
        proto.STRING,
        number=3,
    )
    sql_statement: str = proto.Field(
        proto.STRING,
        number=4,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


class ExecuteSqlResponse(proto.Message):
    r"""Execute a SQL statement response.

    Attributes:
        sql_results (MutableSequence[google.cloud.alloydb_v1.types.SqlResult]):
            SqlResult represents the results for the
            execution of sql statements.
        metadata (google.cloud.alloydb_v1.types.ExecuteSqlMetadata):
            Any additional metadata information regarding
            the execution of the sql statement.
    """

    sql_results: MutableSequence[data_model.SqlResult] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=data_model.SqlResult,
    )
    metadata: "ExecuteSqlMetadata" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ExecuteSqlMetadata",
    )


class ExecuteSqlMetadata(proto.Message):
    r"""Any additional metadata information regarding the execution
    of the SQL

    Attributes:
        message (str):
            Message related to SQL execution. Marked as
            core content since it can potentially contain
            details related to the query or result set. This
            field can be used to convey messages such as
            "when the SQL result set exceeds the acceptable
            response size limits.".
        partial_result (bool):
            Set to true if SQL returned a result set
            larger than the acceptable response size limits
            and the result was truncated.
        sql_statement_execution_duration (google.protobuf.duration_pb2.Duration):
            The time duration taken to execute the sql
            statement.
        status (google.cloud.alloydb_v1.types.ExecuteSqlMetadata.Status):
            Status of SQL execution.
    """

    class Status(proto.Enum):
        r"""Status contains all valid Status a SQL execution can end up
        in.

        Values:
            STATUS_UNSPECIFIED (0):
                The status is unknown.
            OK (1):
                No error during SQL execution i.e. All SQL
                statements ran to completion. The "message" will
                be empty.
            PARTIAL (2):
                Same as OK, except indicates that only
                partial results were returned. The "message"
                field will contain details on why results were
                truncated.
            ERROR (3):
                Error during SQL execution. Atleast 1 SQL
                statement execution resulted in a error. Side
                effects of other statements are rolled back.
                The "message" field will contain human readable
                error given by Postgres of the first bad SQL
                statement. SQL execution errors don't constitute
                API errors as defined in
                https://google.aip.dev/193 but will be returned
                as part of this message.
        """

        STATUS_UNSPECIFIED = 0
        OK = 1
        PARTIAL = 2
        ERROR = 3

    message: str = proto.Field(
        proto.STRING,
        number=1,
    )
    partial_result: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    sql_statement_execution_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=3,
        message=duration_pb2.Duration,
    )
    status: Status = proto.Field(
        proto.ENUM,
        number=4,
        enum=Status,
    )


class ListBackupsRequest(proto.Message):
    r"""Message for requesting list of Backups

    Attributes:
        parent (str):
            Required. Parent value for ListBackupsRequest
        page_size (int):
            Requested page size. Server may return fewer
            items than requested. If unspecified, server
            will pick an appropriate default.
        page_token (str):
            A token identifying a page of results the
            server should return.
        filter (str):
            Filtering results
        order_by (str):
            Hint for how to order the results
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
    r"""Message for response to listing Backups

    Attributes:
        backups (MutableSequence[google.cloud.alloydb_v1.types.Backup]):
            The list of Backup
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    backups: MutableSequence[resources.Backup] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Backup,
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
    r"""Message for getting a Backup

    Attributes:
        name (str):
            Required. Name of the resource
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateBackupRequest(proto.Message):
    r"""Message for creating a Backup

    Attributes:
        parent (str):
            Required. Value for parent.
        backup_id (str):
            Required. ID of the requesting object.
        backup (google.cloud.alloydb_v1.types.Backup):
            Required. The resource being created
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server ignores
            the request if it has already been completed.
            The server guarantees that for at least 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if the original
            operation with the same request ID was received,
            and if so, ignores the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        validate_only (bool):
            Optional. If set, the backend validates the
            request, but doesn't actually execute it.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    backup_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    backup: resources.Backup = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.Backup,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class UpdateBackupRequest(proto.Message):
    r"""Message for updating a Backup

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the Backup resource by the update. The fields
            specified in the update_mask are relative to the resource,
            not the full request. A field will be overwritten if it is
            in the mask. If the user does not provide a mask then all
            fields will be overwritten.
        backup (google.cloud.alloydb_v1.types.Backup):
            Required. The resource being updated
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server ignores
            the request if it has already been completed.
            The server guarantees that for at least 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if the original
            operation with the same request ID was received,
            and if so, ignores the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        validate_only (bool):
            Optional. If set, the backend validates the
            request, but doesn't actually execute it.
        allow_missing (bool):
            Optional. If set to true, update succeeds even if instance
            is not found. In that case, a new backup is created and
            ``update_mask`` is ignored.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    backup: resources.Backup = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.Backup,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class DeleteBackupRequest(proto.Message):
    r"""Message for deleting a Backup

    Attributes:
        name (str):
            Required. Name of the resource. For the
            required format, see the comment on the
            Backup.name field.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server ignores
            the request if it has already been completed.
            The server guarantees that for at least 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if the original
            operation with the same request ID was received,
            and if so, ignores the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        validate_only (bool):
            Optional. If set, the backend validates the
            request, but doesn't actually execute it.
        etag (str):
            Optional. The current etag of the Backup.
            If an etag is provided and does not match the
            current etag of the Backup, deletion will be
            blocked and an ABORTED error will be returned.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListSupportedDatabaseFlagsRequest(proto.Message):
    r"""Message for listing the information about the supported
    Database flags.

    Attributes:
        parent (str):
            Required. The name of the parent resource. The required
            format is:

            - projects/{project}/locations/{location}

            Regardless of the parent specified here, as long it is
            contains a valid project and location, the service will
            return a static list of supported flags resources. Note that
            we do not yet support region-specific flags.
        page_size (int):
            Requested page size. Server may return fewer
            items than requested. If unspecified, server
            will pick an appropriate default.
        page_token (str):
            A token identifying a page of results the
            server should return.
        scope (google.cloud.alloydb_v1.types.SupportedDatabaseFlag.Scope):
            Optional. The scope for which supported flags
            are requested. If not specified, default is
            DATABASE.
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
    scope: resources.SupportedDatabaseFlag.Scope = proto.Field(
        proto.ENUM,
        number=6,
        enum=resources.SupportedDatabaseFlag.Scope,
    )


class ListSupportedDatabaseFlagsResponse(proto.Message):
    r"""Message for response to listing SupportedDatabaseFlags.

    Attributes:
        supported_database_flags (MutableSequence[google.cloud.alloydb_v1.types.SupportedDatabaseFlag]):
            The list of SupportedDatabaseFlags.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
    """

    @property
    def raw_page(self):
        return self

    supported_database_flags: MutableSequence[resources.SupportedDatabaseFlag] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=resources.SupportedDatabaseFlag,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GenerateClientCertificateRequest(proto.Message):
    r"""Message for requests to generate a client certificate signed
    by the Cluster CA.

    Attributes:
        parent (str):
            Required. The name of the parent resource. The required
            format is:

            - projects/{project}/locations/{location}/clusters/{cluster}
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server ignores
            the request if it has already been completed.
            The server guarantees that for at least 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if the original
            operation with the same request ID was received,
            and if so, ignores the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        cert_duration (google.protobuf.duration_pb2.Duration):
            Optional. An optional hint to the endpoint to
            generate the client certificate with the
            requested duration. The duration can be from 1
            hour to 24 hours. The endpoint may or may not
            honor the hint. If the hint is left unspecified
            or is not honored, then the endpoint will pick
            an appropriate default duration.
        public_key (str):
            Optional. The public key from the client.
        use_metadata_exchange (bool):
            Optional. An optional hint to the endpoint to
            generate a client certificate that can be used
            by AlloyDB connectors to exchange additional
            metadata with the server after TLS handshake.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    cert_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=4,
        message=duration_pb2.Duration,
    )
    public_key: str = proto.Field(
        proto.STRING,
        number=5,
    )
    use_metadata_exchange: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


class GenerateClientCertificateResponse(proto.Message):
    r"""Message returned by a GenerateClientCertificate operation.

    Attributes:
        pem_certificate_chain (MutableSequence[str]):
            Output only. The pem-encoded chain that may
            be used to verify the X.509 certificate.
            Expected to be in issuer-to-root order according
            to RFC 5246.
        ca_cert (str):
            Optional. The pem-encoded cluster ca X.509
            certificate.
    """

    pem_certificate_chain: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    ca_cert: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GetConnectionInfoRequest(proto.Message):
    r"""Request message for GetConnectionInfo.

    Attributes:
        parent (str):
            Required. The name of the parent resource.
            The required format is:
            projects/{project}/locations/{location}/clusters/{cluster}/instances/{instance}
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server ignores
            the request if it has already been completed.
            The server guarantees that for at least 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if the original
            operation with the same request ID was received,
            and if so, ignores the second request. This
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
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class OperationMetadata(proto.Message):
    r"""Represents the metadata of the long-running operation.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        batch_create_instances_metadata (google.cloud.alloydb_v1.types.BatchCreateInstancesMetadata):
            Output only. BatchCreateInstances related
            metadata.

            This field is a member of `oneof`_ ``request_specific``.
        upgrade_cluster_status (google.cloud.alloydb_v1.types.UpgradeClusterStatus):
            Output only. UpgradeClusterStatus related
            metadata.

            This field is a member of `oneof`_ ``request_specific``.
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
            cancellation of the operation. Operations that have
            successfully been cancelled have
            [google.longrunning.Operation.error][google.longrunning.Operation.error]
            value with a
            [google.rpc.Status.code][google.rpc.Status.code] of 1,
            corresponding to ``Code.CANCELLED``.
        api_version (str):
            Output only. API version used to start the
            operation.
    """

    batch_create_instances_metadata: "BatchCreateInstancesMetadata" = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="request_specific",
        message="BatchCreateInstancesMetadata",
    )
    upgrade_cluster_status: "UpgradeClusterStatus" = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="request_specific",
        message="UpgradeClusterStatus",
    )
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


class UpgradeClusterStatus(proto.Message):
    r"""Message for current status of the Major Version Upgrade
    operation.

    Attributes:
        state (google.cloud.alloydb_v1.types.UpgradeClusterResponse.Status):
            Cluster Major Version Upgrade state.
        cancellable (bool):
            Whether the operation is cancellable.
        source_version (google.cloud.alloydb_v1.types.DatabaseVersion):
            Source database major version.
        target_version (google.cloud.alloydb_v1.types.DatabaseVersion):
            Target database major version.
        stages (MutableSequence[google.cloud.alloydb_v1.types.UpgradeClusterStatus.StageStatus]):
            Status of all upgrade stages.
    """

    class StageStatus(proto.Message):
        r"""Status of an upgrade stage.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            read_pool_instances_upgrade (google.cloud.alloydb_v1.types.UpgradeClusterStatus.ReadPoolInstancesUpgradeStageStatus):
                Read pool instances upgrade metadata.

                This field is a member of `oneof`_ ``stage_specific_status``.
            stage (google.cloud.alloydb_v1.types.UpgradeClusterResponse.Stage):
                Upgrade stage.
            state (google.cloud.alloydb_v1.types.UpgradeClusterResponse.Status):
                State of this stage.
            schedule (google.cloud.alloydb_v1.types.UpgradeClusterStatus.StageStatus.StageSchedule):
                Output only. Timing information for the stage
                execution.
        """

        class StageSchedule(proto.Message):
            r"""Timing information for the stage execution.

            Attributes:
                estimated_start_time (google.protobuf.timestamp_pb2.Timestamp):
                    When the stage is expected to start. Set only
                    if the stage has not started yet.
                actual_start_time (google.protobuf.timestamp_pb2.Timestamp):
                    Actual start time of the stage. Set only if
                    the stage has started.
                estimated_end_time (google.protobuf.timestamp_pb2.Timestamp):
                    When the stage is expected to end. Set only
                    if the stage has not completed yet.
                actual_end_time (google.protobuf.timestamp_pb2.Timestamp):
                    Actual end time of the stage. Set only if the
                    stage has completed.
            """

            estimated_start_time: timestamp_pb2.Timestamp = proto.Field(
                proto.MESSAGE,
                number=1,
                message=timestamp_pb2.Timestamp,
            )
            actual_start_time: timestamp_pb2.Timestamp = proto.Field(
                proto.MESSAGE,
                number=2,
                message=timestamp_pb2.Timestamp,
            )
            estimated_end_time: timestamp_pb2.Timestamp = proto.Field(
                proto.MESSAGE,
                number=3,
                message=timestamp_pb2.Timestamp,
            )
            actual_end_time: timestamp_pb2.Timestamp = proto.Field(
                proto.MESSAGE,
                number=4,
                message=timestamp_pb2.Timestamp,
            )

        read_pool_instances_upgrade: "UpgradeClusterStatus.ReadPoolInstancesUpgradeStageStatus" = proto.Field(
            proto.MESSAGE,
            number=11,
            oneof="stage_specific_status",
            message="UpgradeClusterStatus.ReadPoolInstancesUpgradeStageStatus",
        )
        stage: "UpgradeClusterResponse.Stage" = proto.Field(
            proto.ENUM,
            number=1,
            enum="UpgradeClusterResponse.Stage",
        )
        state: "UpgradeClusterResponse.Status" = proto.Field(
            proto.ENUM,
            number=2,
            enum="UpgradeClusterResponse.Status",
        )
        schedule: "UpgradeClusterStatus.StageStatus.StageSchedule" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="UpgradeClusterStatus.StageStatus.StageSchedule",
        )

    class ReadPoolInstancesUpgradeStageStatus(proto.Message):
        r"""Read pool instances upgrade specific status.

        Attributes:
            upgrade_stats (google.cloud.alloydb_v1.types.UpgradeClusterStatus.ReadPoolInstancesUpgradeStageStatus.Stats):
                Read pool instances upgrade statistics.
        """

        class Stats(proto.Message):
            r"""Upgrade stats for read pool instances.

            Attributes:
                not_started (int):
                    Number of read pool instances for which
                    upgrade has not started.
                ongoing (int):
                    Number of read pool instances undergoing
                    upgrade.
                success (int):
                    Number of read pool instances successfully
                    upgraded.
                failed (int):
                    Number of read pool instances which failed to
                    upgrade.
            """

            not_started: int = proto.Field(
                proto.INT32,
                number=1,
            )
            ongoing: int = proto.Field(
                proto.INT32,
                number=2,
            )
            success: int = proto.Field(
                proto.INT32,
                number=3,
            )
            failed: int = proto.Field(
                proto.INT32,
                number=4,
            )

        upgrade_stats: "UpgradeClusterStatus.ReadPoolInstancesUpgradeStageStatus.Stats" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="UpgradeClusterStatus.ReadPoolInstancesUpgradeStageStatus.Stats",
        )

    state: "UpgradeClusterResponse.Status" = proto.Field(
        proto.ENUM,
        number=1,
        enum="UpgradeClusterResponse.Status",
    )
    cancellable: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    source_version: resources.DatabaseVersion = proto.Field(
        proto.ENUM,
        number=3,
        enum=resources.DatabaseVersion,
    )
    target_version: resources.DatabaseVersion = proto.Field(
        proto.ENUM,
        number=4,
        enum=resources.DatabaseVersion,
    )
    stages: MutableSequence[StageStatus] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=StageStatus,
    )


class ListUsersRequest(proto.Message):
    r"""Message for requesting list of Users

    Attributes:
        parent (str):
            Required. Parent value for ListUsersRequest
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filtering results
        order_by (str):
            Optional. Hint for how to order the results
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


class ListUsersResponse(proto.Message):
    r"""Message for response to listing Users

    Attributes:
        users (MutableSequence[google.cloud.alloydb_v1.types.User]):
            The list of User
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    users: MutableSequence[resources.User] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.User,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetUserRequest(proto.Message):
    r"""Message for getting a User

    Attributes:
        name (str):
            Required. The name of the resource. For the
            required format, see the comment on the
            User.name field.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateUserRequest(proto.Message):
    r"""Message for creating a User

    Attributes:
        parent (str):
            Required. Value for parent.
        user_id (str):
            Required. ID of the requesting object.
        user (google.cloud.alloydb_v1.types.User):
            Required. The resource being created
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server ignores
            the request if it has already been completed.
            The server guarantees that for at least 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if the original
            operation with the same request ID was received,
            and if so, ignores the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        validate_only (bool):
            Optional. If set, the backend validates the
            request, but doesn't actually execute it.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    user_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    user: resources.User = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.User,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class UpdateUserRequest(proto.Message):
    r"""Message for updating a User

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the User resource by the update. The fields
            specified in the update_mask are relative to the resource,
            not the full request. A field will be overwritten if it is
            in the mask. If the user does not provide a mask then all
            fields will be overwritten.
        user (google.cloud.alloydb_v1.types.User):
            Required. The resource being updated
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server ignores
            the request if it has already been completed.
            The server guarantees that for at least 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if the original
            operation with the same request ID was received,
            and if so, ignores the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        validate_only (bool):
            Optional. If set, the backend validates the
            request, but doesn't actually execute it.
        allow_missing (bool):
            Optional. Allow missing fields in the update
            mask.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    user: resources.User = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.User,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class DeleteUserRequest(proto.Message):
    r"""Message for deleting a User

    Attributes:
        name (str):
            Required. The name of the resource. For the
            required format, see the comment on the
            User.name field.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server ignores
            the request if it has already been completed.
            The server guarantees that for at least 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if the original
            operation with the same request ID was received,
            and if so, ignores the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        validate_only (bool):
            Optional. If set, the backend validates the
            request, but doesn't actually execute it.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class ListDatabasesRequest(proto.Message):
    r"""Message for ListDatabases request.

    Attributes:
        parent (str):
            Required. Parent value for
            ListDatabasesRequest.
        page_size (int):
            Optional. The maximum number of databases to return. The
            service may return fewer than this value. If unspecified,
            2000 is the default page_size. The max value of page_size
            will be 4000, values above max will be coerced to max.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListDatabases`` call. This should be provided to retrieve
            the subsequent page. This field is currently not supported,
            its value will be ignored if passed.
        filter (str):
            Optional. Filtering results.
            This field is currently not supported, its value
            will be ignored if passed.
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


class ListDatabasesResponse(proto.Message):
    r"""Message for ListDatabases response.

    Attributes:
        databases (MutableSequence[google.cloud.alloydb_v1.types.Database]):
            The list of databases.
        next_page_token (str):
            A token identifying the next page of results
            the server should return. If this field is
            omitted, there are no subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    databases: MutableSequence[resources.Database] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Database,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
