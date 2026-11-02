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
import google.rpc.status_pb2 as status_pb2  # type: ignore
import google.type.date_pb2 as date_pb2  # type: ignore
import google.type.datetime_pb2 as datetime_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.storageinsights.v1",
    manifest={
        "ListReportConfigsRequest",
        "ListReportConfigsResponse",
        "GetReportConfigRequest",
        "CreateReportConfigRequest",
        "UpdateReportConfigRequest",
        "DeleteReportConfigRequest",
        "ReportDetail",
        "ListReportDetailsRequest",
        "ListReportDetailsResponse",
        "GetReportDetailRequest",
        "OperationMetadata",
        "FrequencyOptions",
        "CSVOptions",
        "ParquetOptions",
        "CloudStorageFilters",
        "CloudStorageDestinationOptions",
        "ObjectMetadataReportOptions",
        "ReportConfig",
        "Identity",
        "DatasetConfig",
        "ListDatasetConfigsRequest",
        "ListDatasetConfigsResponse",
        "GetDatasetConfigRequest",
        "CreateDatasetConfigRequest",
        "UpdateDatasetConfigRequest",
        "DeleteDatasetConfigRequest",
        "LinkDatasetRequest",
        "LinkDatasetResponse",
        "UnlinkDatasetRequest",
        "LocationMetadata",
    },
)


class ListReportConfigsRequest(proto.Message):
    r"""Request message for
    [``ListReportConfigs``][google.cloud.storageinsights.v1.StorageInsights.ListReportConfigs]

    Attributes:
        parent (str):
            Required. Parent value for
            ListReportConfigsRequest
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


class ListReportConfigsResponse(proto.Message):
    r"""Message for response to listing ReportConfigs

    Attributes:
        report_configs (MutableSequence[google.cloud.storageinsights_v1.types.ReportConfig]):
            The list of ReportConfig
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    report_configs: MutableSequence["ReportConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ReportConfig",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetReportConfigRequest(proto.Message):
    r"""Message for getting a ReportConfig

    Attributes:
        name (str):
            Required. Name of the resource
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateReportConfigRequest(proto.Message):
    r"""Message for creating a ReportConfig

    Attributes:
        parent (str):
            Required. Value for parent.
        report_config (google.cloud.storageinsights_v1.types.ReportConfig):
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
    report_config: "ReportConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ReportConfig",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateReportConfigRequest(proto.Message):
    r"""Message for updating a ReportConfig

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the ReportConfig resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        report_config (google.cloud.storageinsights_v1.types.ReportConfig):
            Required. The resource being updated
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
    report_config: "ReportConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ReportConfig",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteReportConfigRequest(proto.Message):
    r"""Message for deleting a ReportConfig

    Attributes:
        name (str):
            Required. Name of the resource
        force (bool):
            Optional. If set, all ReportDetails for this
            ReportConfig will be deleted.
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
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ReportDetail(proto.Message):
    r"""Message describing ReportDetail object. ReportDetail
    represents metadata of generated reports for a ReportConfig.
    Next ID: 10

    Attributes:
        name (str):
            Name of resource. It will be of form
            projects/<project>/locations/<location>/reportConfigs/<report-config-id>/reportDetails/<report-detail-id>.
        snapshot_time (google.protobuf.timestamp_pb2.Timestamp):
            The snapshot time.
            All the report data is referenced at this point
            of time.
        report_path_prefix (str):
            Prefix of the object name of each report's shard. This will
            have full prefix except the "extension" and "shard_id". For
            example, if the ``destination_path`` is
            ``{{report-config-id}}/dt={{datetime}}``, the shard object
            name would be
            ``gs://my-insights/1A34-F2E456-12B456-1C3D/dt=2022-05-20T06:35/1A34-F2E456-12B456-1C3D_2022-05-20T06:35_5.csv``
            and the value of ``report_path_prefix`` field would be
            ``gs://my-insights/1A34-F2E456-12B456-1C3D/dt=2022-05-20T06:35/1A34-F2E456-12B456-1C3D_2022-05-20T06:35_``.
        shards_count (int):
            Total shards generated for the report.
        status (google.rpc.status_pb2.Status):
            Status of the ReportDetail.
        labels (MutableMapping[str, str]):
            Labels as key value pairs
        target_datetime (google.type.datetime_pb2.DateTime):
            The date for which report is generated. The time part of
            target_datetime will be zero till we support multiple
            reports per day.
        report_metrics (google.cloud.storageinsights_v1.types.ReportDetail.Metrics):
            Metrics of the report.
    """

    class Metrics(proto.Message):
        r"""Different metrics associated with the generated report.

        Attributes:
            processed_records_count (int):
                Count of Cloud Storage objects which are part
                of the report.
        """

        processed_records_count: int = proto.Field(
            proto.INT64,
            number=1,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    snapshot_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    report_path_prefix: str = proto.Field(
        proto.STRING,
        number=8,
    )
    shards_count: int = proto.Field(
        proto.INT64,
        number=9,
    )
    status: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=4,
        message=status_pb2.Status,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    target_datetime: datetime_pb2.DateTime = proto.Field(
        proto.MESSAGE,
        number=6,
        message=datetime_pb2.DateTime,
    )
    report_metrics: Metrics = proto.Field(
        proto.MESSAGE,
        number=7,
        message=Metrics,
    )


class ListReportDetailsRequest(proto.Message):
    r"""Message for requesting list of ReportDetails

    Attributes:
        parent (str):
            Required. Parent value for
            ListReportDetailsRequest
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


class ListReportDetailsResponse(proto.Message):
    r"""Message for response to listing ReportDetails

    Attributes:
        report_details (MutableSequence[google.cloud.storageinsights_v1.types.ReportDetail]):
            The list of ReportDetail
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    report_details: MutableSequence["ReportDetail"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ReportDetail",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetReportDetailRequest(proto.Message):
    r"""Message for getting a ReportDetail

    Attributes:
        name (str):
            Required. Name of the resource
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class OperationMetadata(proto.Message):
    r"""Represents the metadata of the long-running operation.

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


class FrequencyOptions(proto.Message):
    r"""ReportConfig Resource:

    Options to setup frequency of report generation.

    Attributes:
        frequency (google.cloud.storageinsights_v1.types.FrequencyOptions.Frequency):
            Frequency of report generation.
        start_date (google.type.date_pb2.Date):
            The date from which report generation should
            start. UTC time zone.
        end_date (google.type.date_pb2.Date):
            The date on which report generation should
            stop (Inclusive). UTC time zone.
    """

    class Frequency(proto.Enum):
        r"""This ENUM specifies possible frequencies of report
        generation.

        Values:
            FREQUENCY_UNSPECIFIED (0):
                Unspecified.
            DAILY (1):
                Report will be generated daily.
            WEEKLY (2):
                Report will be generated weekly.
        """

        FREQUENCY_UNSPECIFIED = 0
        DAILY = 1
        WEEKLY = 2

    frequency: Frequency = proto.Field(
        proto.ENUM,
        number=1,
        enum=Frequency,
    )
    start_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=2,
        message=date_pb2.Date,
    )
    end_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=3,
        message=date_pb2.Date,
    )


class CSVOptions(proto.Message):
    r"""Options to configure CSV formatted reports.

    Attributes:
        record_separator (str):
            Record separator characters in CSV.
        delimiter (str):
            Delimiter characters in CSV.
        header_required (bool):
            If set, will include a header row in the CSV
            report.
    """

    record_separator: str = proto.Field(
        proto.STRING,
        number=1,
    )
    delimiter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    header_required: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class ParquetOptions(proto.Message):
    r"""Options to configure Parquet formatted reports."""


class CloudStorageFilters(proto.Message):
    r"""Options to filter data on storage systems.
    Next ID: 2

    Attributes:
        bucket (str):
            Bucket for which the report will be
            generated.
    """

    bucket: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CloudStorageDestinationOptions(proto.Message):
    r"""Options to store reports in storage systems.
    Next ID: 3

    Attributes:
        bucket (str):
            Destination bucket.
        destination_path (str):
            Destination path is the path in the bucket
            where the report should be generated.
    """

    bucket: str = proto.Field(
        proto.STRING,
        number=1,
    )
    destination_path: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ObjectMetadataReportOptions(proto.Message):
    r"""Report specification for exporting object metadata.
    Next ID: 4


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        metadata_fields (MutableSequence[str]):
            Metadata fields to be included in the report.
        storage_filters (google.cloud.storageinsights_v1.types.CloudStorageFilters):
            Cloud Storage as the storage system.

            This field is a member of `oneof`_ ``filter``.
        storage_destination_options (google.cloud.storageinsights_v1.types.CloudStorageDestinationOptions):
            Cloud Storage as the storage system.

            This field is a member of `oneof`_ ``destination_options``.
    """

    metadata_fields: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    storage_filters: "CloudStorageFilters" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="filter",
        message="CloudStorageFilters",
    )
    storage_destination_options: "CloudStorageDestinationOptions" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="destination_options",
        message="CloudStorageDestinationOptions",
    )


class ReportConfig(proto.Message):
    r"""Message describing ReportConfig object. ReportConfig is the
    configuration to generate reports.
    See
    https://cloud.google.com/storage/docs/insights/using-inventory-reports#create-config-rest
    for more details on how to set various fields.
    Next ID: 12

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            name of resource. It will be of form
            projects/<project>/locations/<location>/reportConfigs/<report-config-id>.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Create time stamp
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Update time stamp
        frequency_options (google.cloud.storageinsights_v1.types.FrequencyOptions):
            The frequency of report generation.
        csv_options (google.cloud.storageinsights_v1.types.CSVOptions):
            Options for CSV formatted reports.

            This field is a member of `oneof`_ ``report_format``.
        parquet_options (google.cloud.storageinsights_v1.types.ParquetOptions):
            Options for Parquet formatted reports.

            This field is a member of `oneof`_ ``report_format``.
        object_metadata_report_options (google.cloud.storageinsights_v1.types.ObjectMetadataReportOptions):
            Report for exporting object metadata.

            This field is a member of `oneof`_ ``report_kind``.
        labels (MutableMapping[str, str]):
            Labels as key value pairs
        display_name (str):
            User provided display name which can be empty
            and limited to 256 characters that is editable.
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
    frequency_options: "FrequencyOptions" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="FrequencyOptions",
    )
    csv_options: "CSVOptions" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="report_format",
        message="CSVOptions",
    )
    parquet_options: "ParquetOptions" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="report_format",
        message="ParquetOptions",
    )
    object_metadata_report_options: "ObjectMetadataReportOptions" = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="report_kind",
        message="ObjectMetadataReportOptions",
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=10,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=11,
    )


class Identity(proto.Message):
    r"""Identity lets the user provide the type of identity to use,
    and outputs the identity string that can be used for IAM policy
    changes.

    Attributes:
        name (str):
            Output only. Name of the identity.
        type_ (google.cloud.storageinsights_v1.types.Identity.IdentityType):
            Type of identity to use for the
            datasetConfig.
    """

    class IdentityType(proto.Enum):
        r"""Type of service account to use for the dataset configuration.

        Values:
            IDENTITY_TYPE_UNSPECIFIED (0):
                Default is unspecified and should not be
                used.
            IDENTITY_TYPE_PER_CONFIG (1):
                Google managed service account per resource.
            IDENTITY_TYPE_PER_PROJECT (2):
                Google managed service account per project.
        """

        IDENTITY_TYPE_UNSPECIFIED = 0
        IDENTITY_TYPE_PER_CONFIG = 1
        IDENTITY_TYPE_PER_PROJECT = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: IdentityType = proto.Field(
        proto.ENUM,
        number=2,
        enum=IdentityType,
    )


class DatasetConfig(proto.Message):
    r"""Message describing the dataset configuration properties. For more
    information, see `Dataset configuration
    properties <https://cloud.google.com/storage/docs/insights/datasets#dataset-config>`__.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. name of resource
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The UTC time at which the
            dataset configuration was created. This is
            auto-populated.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The UTC time at which the
            dataset configuration was last updated. This is
            auto-populated.
        labels (MutableMapping[str, str]):
            Labels as key value pairs
        uid (str):
            Output only. System generated unique
            identifier for the resource.
        organization_number (int):
            Optional. Organization resource ID that the
            source projects should belong to. Projects that
            do not belong to the provided organization are
            not considered when creating the dataset.
        source_projects (google.cloud.storageinsights_v1.types.DatasetConfig.SourceProjects):
            Defines the options for providing source
            projects for the dataset.

            This field is a member of `oneof`_ ``source_options``.
        source_folders (google.cloud.storageinsights_v1.types.DatasetConfig.SourceFolders):
            Defines the options for providing source
            folders for the dataset.

            This field is a member of `oneof`_ ``source_options``.
        organization_scope (bool):
            Defines the options for providing a source
            organization for the dataset.

            This field is a member of `oneof`_ ``source_options``.
        cloud_storage_object_path (str):
            Input only. Cloud Storage object path containing a list of
            project or folder numbers to include in the dataset; it
            cannot contain a mix of project and folders.

            The object must be a text file where each line has one of
            the following entries:

            - Project number, formatted as
              ``projects/{project_number}``, for example,
              ``projects/1234567890``.
            - Folder identifier, formatted as
              ``folders/{folder_number}``, for example,
              ``folders/9876543210``. Path must be in the format
              ``gs://{bucket_name}/{object_name}``.

            This field is a member of `oneof`_ ``source_options``.
        include_cloud_storage_locations (google.cloud.storageinsights_v1.types.DatasetConfig.CloudStorageLocations):

            This field is a member of `oneof`_ ``cloud_storage_locations``.
        exclude_cloud_storage_locations (google.cloud.storageinsights_v1.types.DatasetConfig.CloudStorageLocations):

            This field is a member of `oneof`_ ``cloud_storage_locations``.
        include_cloud_storage_buckets (google.cloud.storageinsights_v1.types.DatasetConfig.CloudStorageBuckets):

            This field is a member of `oneof`_ ``cloud_storage_buckets``.
        exclude_cloud_storage_buckets (google.cloud.storageinsights_v1.types.DatasetConfig.CloudStorageBuckets):

            This field is a member of `oneof`_ ``cloud_storage_buckets``.
        include_newly_created_buckets (bool):
            If set to ``true``, the request includes all the newly
            created buckets in the dataset that meet the inclusion and
            exclusion rules.
        skip_verification_and_ingest (bool):
            Optional. If set to ``false``, then all the permission
            checks must be successful before the system can start
            ingesting data. This field can only be updated before the
            system ingests data for the first time. Any attempt to
            modify the field after data ingestion starts results in an
            error.
        retention_period_days (int):
            Number of days of history that must be
            retained.
        link (google.cloud.storageinsights_v1.types.DatasetConfig.Link):
            Details of the linked dataset.
        identity (google.cloud.storageinsights_v1.types.Identity):
            Identity used by this ``datasetConfig``.
        status (google.rpc.status_pb2.Status):
            Output only. Status of the ``datasetConfig``.
        dataset_config_state (google.cloud.storageinsights_v1.types.DatasetConfig.ConfigState):
            Output only. State of the ``datasetConfig``.
        description (str):
            Optional. A user-provided description for the
            dataset configuration.
            Maximum length: 256 characters.
    """

    class ConfigState(proto.Enum):
        r"""State of the configuration.

        Values:
            CONFIG_STATE_UNSPECIFIED (0):
                Unspecified state.
            CONFIG_STATE_ACTIVE (1):
                Active configuration indicates that the
                configuration is actively ingesting data.
            CONFIG_STATE_VERIFICATION_IN_PROGRESS (2):
                In this state, the configuration is being
                verified for various permissions.
            CONFIG_STATE_CREATED (3):
                Configuration is created and further
                processing needs to happen.
            CONFIG_STATE_PROCESSING (4):
                Configuration is under processing
        """

        CONFIG_STATE_UNSPECIFIED = 0
        CONFIG_STATE_ACTIVE = 1
        CONFIG_STATE_VERIFICATION_IN_PROGRESS = 2
        CONFIG_STATE_CREATED = 3
        CONFIG_STATE_PROCESSING = 4

    class SourceProjects(proto.Message):
        r"""Collection of project numbers

        Attributes:
            project_numbers (MutableSequence[int]):

        """

        project_numbers: MutableSequence[int] = proto.RepeatedField(
            proto.INT64,
            number=1,
        )

    class SourceFolders(proto.Message):
        r"""Specifies a set of folders to include in the dataset

        Attributes:
            folder_numbers (MutableSequence[int]):
                Optional. The list of folder numbers to
                include in the dataset.
        """

        folder_numbers: MutableSequence[int] = proto.RepeatedField(
            proto.INT64,
            number=1,
        )

    class CloudStorageLocations(proto.Message):
        r"""Collection of Cloud Storage locations.

        Attributes:
            locations (MutableSequence[str]):

        """

        locations: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )

    class CloudStorageBuckets(proto.Message):
        r"""Collection of Cloud Storage buckets.

        Attributes:
            cloud_storage_buckets (MutableSequence[google.cloud.storageinsights_v1.types.DatasetConfig.CloudStorageBuckets.CloudStorageBucket]):

        """

        class CloudStorageBucket(proto.Message):
            r"""Defines the bucket by its name or a regex pattern to match
            buckets.

            This message has `oneof`_ fields (mutually exclusive fields).
            For each oneof, at most one member field can be set at the same time.
            Setting any member of the oneof automatically clears all other
            members.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                bucket_name (str):
                    Cloud Storage bucket name.

                    This field is a member of `oneof`_ ``cloud_storage_bucket``.
                bucket_prefix_regex (str):
                    A regex pattern for bucket names matching the regex. Regex
                    should follow the syntax specified in ``google/re2`` on
                    GitHub.

                    This field is a member of `oneof`_ ``cloud_storage_bucket``.
            """

            bucket_name: str = proto.Field(
                proto.STRING,
                number=1,
                oneof="cloud_storage_bucket",
            )
            bucket_prefix_regex: str = proto.Field(
                proto.STRING,
                number=2,
                oneof="cloud_storage_bucket",
            )

        cloud_storage_buckets: MutableSequence[
            "DatasetConfig.CloudStorageBuckets.CloudStorageBucket"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="DatasetConfig.CloudStorageBuckets.CloudStorageBucket",
        )

    class Link(proto.Message):
        r"""Defines the details about the linked dataset.

        Attributes:
            dataset (str):
                Output only. Dataset name for linked dataset.
            linked (bool):
                Output only. State of the linked dataset.
        """

        dataset: str = proto.Field(
            proto.STRING,
            number=1,
        )
        linked: bool = proto.Field(
            proto.BOOL,
            number=2,
        )

    class BucketErrors(proto.Message):
        r"""Provides a summary of the bucket level error statistics.

        Attributes:
            validated_count (int):
                Optional. Count of successfully validated
                buckets.
            permission_denied_count (int):
                Optional. Count of buckets with permission
                denied errors.
            permission_denied_bucket_ids (MutableSequence[str]):
                Optional. Subset of bucket names that have
                permission denied.
            non_management_hub_entitled_count (int):
                Optional. Count of buckets that are not
                subscribed to Storage Intelligence.
            internal_error_count (int):
                Optional. Number of buckets that encountered
                internal errors during the validation process.
                These buckets are automatically retried in
                subsequent validation attempts.
            non_storage_intelligence_entitled_count (int):
                Optional. Count of buckets that are not
                subscribed to Storage Intelligence.
            non_storage_intelligence_entitled_bucket_ids (MutableSequence[str]):
                Optional. Subset of bucket names that are not
                subscribed to Storage Intelligence.
        """

        validated_count: int = proto.Field(
            proto.INT64,
            number=1,
        )
        permission_denied_count: int = proto.Field(
            proto.INT64,
            number=2,
        )
        permission_denied_bucket_ids: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=3,
        )
        non_management_hub_entitled_count: int = proto.Field(
            proto.INT64,
            number=5,
        )
        internal_error_count: int = proto.Field(
            proto.INT64,
            number=4,
        )
        non_storage_intelligence_entitled_count: int = proto.Field(
            proto.INT64,
            number=7,
        )
        non_storage_intelligence_entitled_bucket_ids: MutableSequence[str] = (
            proto.RepeatedField(
                proto.STRING,
                number=8,
            )
        )

    class ProjectErrors(proto.Message):
        r"""Provides a summary of the project level error statistics.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            validated_count (int):
                Optional. Count of successfully validated
                projects.

                This field is a member of `oneof`_ ``_validated_count``.
            outside_org_error_count (int):
                Optional. Count of projects which are not in
                the same organization.

                This field is a member of `oneof`_ ``_outside_org_error_count``.
            outside_org_project_numbers (MutableSequence[int]):
                Optional. Subset of project numbers which are
                not in the same organization.
            non_management_hub_entitled_error_count (int):
                Optional. Count of projects that are not
                subscribed to Storage Intelligence.

                This field is a member of `oneof`_ ``_non_management_hub_entitled_error_count``.
            non_management_hub_entitled_project_numbers (MutableSequence[int]):
                Optional. Subset of project numbers that are
                not subscribed to Storage Intelligence.
            non_storage_intelligence_entitled_error_count (int):
                Optional. Count of projects that are not
                subscribed to Storage Intelligence.

                This field is a member of `oneof`_ ``_non_storage_intelligence_entitled_error_count``.
            non_storage_intelligence_entitled_project_numbers (MutableSequence[int]):
                Optional. Subset of project numbers that are
                not subscribed to Storage Intelligence.
            internal_error_count (int):
                Optional. Number of projects that encountered
                internal errors during validation and are
                automatically retried.

                This field is a member of `oneof`_ ``_internal_error_count``.
            destination_project_org_error (bool):
                Optional. Indicates if the destination
                project resides within the same organization as
                the source project.

                This field is a member of `oneof`_ ``destination_project_check_result``.
            destination_project_check_has_internal_error (bool):
                Optional. Indicates whether the destination project check
                failed due to an internal error. If ``true``, the system
                automatically retries the check.

                This field is a member of `oneof`_ ``destination_project_check_result``.
        """

        validated_count: int = proto.Field(
            proto.INT64,
            number=1,
            optional=True,
        )
        outside_org_error_count: int = proto.Field(
            proto.INT64,
            number=2,
            optional=True,
        )
        outside_org_project_numbers: MutableSequence[int] = proto.RepeatedField(
            proto.INT64,
            number=3,
        )
        non_management_hub_entitled_error_count: int = proto.Field(
            proto.INT64,
            number=7,
            optional=True,
        )
        non_management_hub_entitled_project_numbers: MutableSequence[int] = (
            proto.RepeatedField(
                proto.INT64,
                number=8,
            )
        )
        non_storage_intelligence_entitled_error_count: int = proto.Field(
            proto.INT64,
            number=9,
            optional=True,
        )
        non_storage_intelligence_entitled_project_numbers: MutableSequence[int] = (
            proto.RepeatedField(
                proto.INT64,
                number=10,
            )
        )
        internal_error_count: int = proto.Field(
            proto.INT64,
            number=4,
            optional=True,
        )
        destination_project_org_error: bool = proto.Field(
            proto.BOOL,
            number=5,
            oneof="destination_project_check_result",
        )
        destination_project_check_has_internal_error: bool = proto.Field(
            proto.BOOL,
            number=6,
            oneof="destination_project_check_result",
        )

    class ValidationErrorsBeforeIngestion(proto.Message):
        r"""Summary of validation errors that occurred during the
        verification phase.

        Attributes:
            bucket_errors (google.cloud.storageinsights_v1.types.DatasetConfig.BucketErrors):
                Optional. Provides a summary of the bucket
                level error stats.
            project_errors (google.cloud.storageinsights_v1.types.DatasetConfig.ProjectErrors):
                Optional. Provides a summary of the project
                level error stats.
        """

        bucket_errors: "DatasetConfig.BucketErrors" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="DatasetConfig.BucketErrors",
        )
        project_errors: "DatasetConfig.ProjectErrors" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="DatasetConfig.ProjectErrors",
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
    uid: str = proto.Field(
        proto.STRING,
        number=5,
    )
    organization_number: int = proto.Field(
        proto.INT64,
        number=22,
    )
    source_projects: SourceProjects = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="source_options",
        message=SourceProjects,
    )
    source_folders: SourceFolders = proto.Field(
        proto.MESSAGE,
        number=24,
        oneof="source_options",
        message=SourceFolders,
    )
    organization_scope: bool = proto.Field(
        proto.BOOL,
        number=25,
        oneof="source_options",
    )
    cloud_storage_object_path: str = proto.Field(
        proto.STRING,
        number=21,
        oneof="source_options",
    )
    include_cloud_storage_locations: CloudStorageLocations = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="cloud_storage_locations",
        message=CloudStorageLocations,
    )
    exclude_cloud_storage_locations: CloudStorageLocations = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="cloud_storage_locations",
        message=CloudStorageLocations,
    )
    include_cloud_storage_buckets: CloudStorageBuckets = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="cloud_storage_buckets",
        message=CloudStorageBuckets,
    )
    exclude_cloud_storage_buckets: CloudStorageBuckets = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="cloud_storage_buckets",
        message=CloudStorageBuckets,
    )
    include_newly_created_buckets: bool = proto.Field(
        proto.BOOL,
        number=12,
    )
    skip_verification_and_ingest: bool = proto.Field(
        proto.BOOL,
        number=19,
    )
    retention_period_days: int = proto.Field(
        proto.INT32,
        number=14,
    )
    link: Link = proto.Field(
        proto.MESSAGE,
        number=15,
        message=Link,
    )
    identity: "Identity" = proto.Field(
        proto.MESSAGE,
        number=16,
        message="Identity",
    )
    status: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=17,
        message=status_pb2.Status,
    )
    dataset_config_state: ConfigState = proto.Field(
        proto.ENUM,
        number=18,
        enum=ConfigState,
    )
    description: str = proto.Field(
        proto.STRING,
        number=20,
    )


class ListDatasetConfigsRequest(proto.Message):
    r"""Request message for
    [``ListDatasetConfigs``][google.cloud.storageinsights.v1.StorageInsights.ListDatasetConfigs]

    Attributes:
        parent (str):
            Required. Parent value for
            ListDatasetConfigsRequest
        page_size (int):
            Requested page size. Server might return
            fewer items than requested. If unspecified,
            server picks an appropriate default.
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


class ListDatasetConfigsResponse(proto.Message):
    r"""Response message for
    [``ListDatasetConfigs``][google.cloud.storageinsights.v1.StorageInsights.ListDatasetConfigs]

    Attributes:
        dataset_configs (MutableSequence[google.cloud.storageinsights_v1.types.DatasetConfig]):
            The list of ``DatasetConfigs``
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    dataset_configs: MutableSequence["DatasetConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DatasetConfig",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetDatasetConfigRequest(proto.Message):
    r"""Request message for
    [``GetDatasetConfig``][google.cloud.storageinsights.v1.StorageInsights.GetDatasetConfig]

    Attributes:
        name (str):
            Required. Name of the resource
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateDatasetConfigRequest(proto.Message):
    r"""Request message for
    [``CreateDatasetConfig``][google.cloud.storageinsights.v1.StorageInsights.CreateDatasetConfig]

    Attributes:
        parent (str):
            Required. Value for parent.
        dataset_config_id (str):
            Required. ID of the requesting object. If auto-generating ID
            is enabled on the server-side, remove this field and
            ``dataset_config_id`` from the method_signature of Create
            RPC Note: The value should not contain any hyphens.
        dataset_config (google.cloud.storageinsights_v1.types.DatasetConfig):
            Required. The resource being created
        request_id (str):
            Optional. A unique identifier for your
            request. Specify the request ID if you need to
            retry the request. If you retry the request with
            the same ID within 60 minutes, the server
            ignores the request if it has already completed
            the original request.

            For example, if your initial request times out
            and you retry the request using the same request
            ID, the server recognizes the original request
            and does not process the new request.

            The request ID must be a valid UUID and cannot
            be a zero UUID
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    dataset_config_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    dataset_config: "DatasetConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="DatasetConfig",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateDatasetConfigRequest(proto.Message):
    r"""Request message for
    [``UpdateDatasetConfig``][google.cloud.storageinsights.v1.StorageInsights.UpdateDatasetConfig]

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the ``DatasetConfig`` resource by the update.
            The fields specified in the ``update_mask`` are relative to
            the resource, not the full request. A field is overwritten
            if it is in the mask. If the user does not provide a mask
            then it returns an "Invalid Argument" error.
        dataset_config (google.cloud.storageinsights_v1.types.DatasetConfig):
            Required. The resource being updated
        request_id (str):
            Optional. A unique identifier for your
            request. Specify the request ID if you need to
            retry the request. If you retry the request with
            the same ID within 60 minutes, the server
            ignores the request if it has already completed
            the original request.

            For example, if your initial request times out
            and you retry the request using the same request
            ID, the server recognizes the original request
            and does not process the new request.

            The request ID must be a valid UUID and cannot
            be a zero UUID
            (00000000-0000-0000-0000-000000000000).
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    dataset_config: "DatasetConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DatasetConfig",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteDatasetConfigRequest(proto.Message):
    r"""Request message for
    [``DeleteDatasetConfig``][google.cloud.storageinsights.v1.StorageInsights.DeleteDatasetConfig]

    Attributes:
        name (str):
            Required. Name of the resource
        request_id (str):
            Optional. A unique identifier for your
            request. Specify the request ID if you need to
            retry the request. If you retry the request with
            the same ID within 60 minutes, the server
            ignores the request if it has already completed
            the original request.

            For example, if your initial request times out
            and you retry the request using the same request
            ID, the server recognizes the original request
            and does not process the new request.

            The request ID must be a valid UUID and cannot
            be a zero UUID
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


class LinkDatasetRequest(proto.Message):
    r"""Request message for
    [``LinkDataset``][google.cloud.storageinsights.v1.StorageInsights.LinkDataset]

    Attributes:
        name (str):
            Required. Name of the resource
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class LinkDatasetResponse(proto.Message):
    r"""Response message for
    [``LinkDataset``][google.cloud.storageinsights.v1.StorageInsights.LinkDataset]

    """


class UnlinkDatasetRequest(proto.Message):
    r"""Request message for
    [``UnlinkDataset``][google.cloud.storageinsights.v1.StorageInsights.UnlinkDataset]

    Attributes:
        name (str):
            Required. Name of the resource
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class LocationMetadata(proto.Message):
    r"""Metadata that helps discover which resources are available in
    a location.

    Attributes:
        report_config_available (bool):
            If true, ``storageinsights.googleapis.com/ReportConfig``
            resource is available at the location.
        dataset_config_available (bool):
            If true, ``storageinsights.googleapis.com/DatasetConfig``
            resource is available at the location.
    """

    report_config_available: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    dataset_config_available: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
