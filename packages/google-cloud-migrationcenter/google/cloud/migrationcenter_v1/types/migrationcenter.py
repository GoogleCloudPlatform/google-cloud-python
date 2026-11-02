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
import google.type.date_pb2 as date_pb2  # type: ignore
import google.type.money_pb2 as money_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.migrationcenter.v1",
    manifest={
        "AssetView",
        "OperatingSystemFamily",
        "ImportJobFormat",
        "ImportJobView",
        "ErrorFrameView",
        "PersistentDiskType",
        "LicenseType",
        "SizingOptimizationStrategy",
        "CommitmentPlan",
        "ComputeMigrationTargetProduct",
        "ReportView",
        "Asset",
        "PreferenceSet",
        "ImportJob",
        "ImportDataFile",
        "Group",
        "ErrorFrame",
        "Source",
        "ReportConfig",
        "Report",
        "OperationMetadata",
        "ListAssetsRequest",
        "ListAssetsResponse",
        "GetAssetRequest",
        "UpdateAssetRequest",
        "BatchUpdateAssetsRequest",
        "BatchUpdateAssetsResponse",
        "DeleteAssetRequest",
        "BatchDeleteAssetsRequest",
        "ReportAssetFramesRequest",
        "ReportAssetFramesResponse",
        "AggregateAssetsValuesRequest",
        "AggregateAssetsValuesResponse",
        "CreateImportJobRequest",
        "ListImportJobsRequest",
        "ListImportJobsResponse",
        "GetImportJobRequest",
        "DeleteImportJobRequest",
        "UpdateImportJobRequest",
        "ValidateImportJobRequest",
        "RunImportJobRequest",
        "GetImportDataFileRequest",
        "ListImportDataFilesRequest",
        "ListImportDataFilesResponse",
        "CreateImportDataFileRequest",
        "DeleteImportDataFileRequest",
        "ListGroupsRequest",
        "ListGroupsResponse",
        "GetGroupRequest",
        "CreateGroupRequest",
        "UpdateGroupRequest",
        "DeleteGroupRequest",
        "AddAssetsToGroupRequest",
        "RemoveAssetsFromGroupRequest",
        "ListErrorFramesRequest",
        "ListErrorFramesResponse",
        "GetErrorFrameRequest",
        "ListSourcesRequest",
        "ListSourcesResponse",
        "GetSourceRequest",
        "CreateSourceRequest",
        "UpdateSourceRequest",
        "DeleteSourceRequest",
        "ListPreferenceSetsRequest",
        "ListPreferenceSetsResponse",
        "GetPreferenceSetRequest",
        "CreatePreferenceSetRequest",
        "UpdatePreferenceSetRequest",
        "DeletePreferenceSetRequest",
        "GetSettingsRequest",
        "UpdateSettingsRequest",
        "CreateReportConfigRequest",
        "DeleteReportConfigRequest",
        "GetReportRequest",
        "ListReportsRequest",
        "ListReportsResponse",
        "DeleteReportRequest",
        "GetReportConfigRequest",
        "ListReportConfigsRequest",
        "ListReportConfigsResponse",
        "CreateReportRequest",
        "Frames",
        "AssetFrame",
        "MachineDetails",
        "MachineArchitectureDetails",
        "BiosDetails",
        "MachineNetworkDetails",
        "NetworkAdapterList",
        "NetworkAdapterDetails",
        "NetworkAddressList",
        "NetworkAddress",
        "MachineDiskDetails",
        "DiskEntryList",
        "DiskEntry",
        "DiskPartitionList",
        "DiskPartition",
        "VmwareDiskConfig",
        "GuestOsDetails",
        "GuestConfigDetails",
        "FstabEntryList",
        "FstabEntry",
        "HostsEntryList",
        "HostsEntry",
        "NfsExportList",
        "NfsExport",
        "GuestRuntimeDetails",
        "RunningServiceList",
        "RunningService",
        "RunningProcessList",
        "RunningProcess",
        "RuntimeNetworkInfo",
        "NetworkConnectionList",
        "NetworkConnection",
        "GuestInstalledApplicationList",
        "GuestInstalledApplication",
        "OpenFileList",
        "OpenFileDetails",
        "PlatformDetails",
        "VmwarePlatformDetails",
        "AwsEc2PlatformDetails",
        "AzureVmPlatformDetails",
        "GenericPlatformDetails",
        "PhysicalPlatformDetails",
        "MemoryUsageSample",
        "CpuUsageSample",
        "NetworkUsageSample",
        "DiskUsageSample",
        "PerformanceSample",
        "AssetPerformanceData",
        "DailyResourceUsageAggregation",
        "InsightList",
        "Insight",
        "GenericInsight",
        "MigrationInsight",
        "ComputeEngineMigrationTarget",
        "ComputeEngineShapeDescriptor",
        "ComputeStorageDescriptor",
        "FitDescriptor",
        "Aggregation",
        "AggregationResult",
        "FileValidationReport",
        "ValidationReport",
        "ExecutionReport",
        "ImportError",
        "ImportRowError",
        "UploadFileInfo",
        "AssetList",
        "FrameViolationEntry",
        "VirtualMachinePreferences",
        "ComputeEnginePreferences",
        "MachinePreferences",
        "MachineSeries",
        "VmwareEnginePreferences",
        "SoleTenancyPreferences",
        "SoleTenantNodeType",
        "RegionPreferences",
        "Settings",
        "ReportSummary",
    },
)


class AssetView(proto.Enum):
    r"""Specifies the types of asset views that provide complete or
    partial details of an asset.

    Values:
        ASSET_VIEW_UNSPECIFIED (0):
            The asset view is not specified. The API
            displays the basic view by default.
        ASSET_VIEW_BASIC (1):
            The asset view includes only basic metadata
            of the asset.
        ASSET_VIEW_FULL (2):
            The asset view includes all the metadata of
            an asset and performance data.
    """

    ASSET_VIEW_UNSPECIFIED = 0
    ASSET_VIEW_BASIC = 1
    ASSET_VIEW_FULL = 2


class OperatingSystemFamily(proto.Enum):
    r"""Known categories of operating systems.

    Values:
        OS_FAMILY_UNKNOWN (0):
            No description available.
        OS_FAMILY_WINDOWS (1):
            Microsoft Windows Server and Desktop.
        OS_FAMILY_LINUX (2):
            Various Linux flavors.
        OS_FAMILY_UNIX (3):
            Non-Linux Unix flavors.
    """

    OS_FAMILY_UNKNOWN = 0
    OS_FAMILY_WINDOWS = 1
    OS_FAMILY_LINUX = 2
    OS_FAMILY_UNIX = 3


class ImportJobFormat(proto.Enum):
    r"""Specifies the data formats supported by Migration Center.

    Values:
        IMPORT_JOB_FORMAT_UNSPECIFIED (0):
            Default value.
        IMPORT_JOB_FORMAT_RVTOOLS_XLSX (1):
            RVTools format (XLSX).
        IMPORT_JOB_FORMAT_RVTOOLS_CSV (2):
            RVTools format (CSV).
        IMPORT_JOB_FORMAT_EXPORTED_AWS_CSV (4):
            CSV format exported from AWS using the [AWS collection
            script][https://github.com/GoogleCloudPlatform/aws-to-stratozone-export].
        IMPORT_JOB_FORMAT_EXPORTED_AZURE_CSV (5):
            CSV format exported from Azure using the [Azure collection
            script][https://github.com/GoogleCloudPlatform/azure-to-stratozone-export].
        IMPORT_JOB_FORMAT_STRATOZONE_CSV (6):
            CSV format created manually and following the StratoZone
            format. For more information, see [Manually create and
            upload data
            tables][https://cloud.google.com/migrate/stratozone/docs/import-data-portal].
    """

    IMPORT_JOB_FORMAT_UNSPECIFIED = 0
    IMPORT_JOB_FORMAT_RVTOOLS_XLSX = 1
    IMPORT_JOB_FORMAT_RVTOOLS_CSV = 2
    IMPORT_JOB_FORMAT_EXPORTED_AWS_CSV = 4
    IMPORT_JOB_FORMAT_EXPORTED_AZURE_CSV = 5
    IMPORT_JOB_FORMAT_STRATOZONE_CSV = 6


class ImportJobView(proto.Enum):
    r"""Specifies the types of import job views that provide complete
    or partial details of an import job.

    Values:
        IMPORT_JOB_VIEW_UNSPECIFIED (0):
            The import job view is not specified. The API
            displays the basic view by default.
        IMPORT_JOB_VIEW_BASIC (1):
            The import job view includes basic metadata
            of an import job. This view does not include
            payload information.
        IMPORT_JOB_VIEW_FULL (2):
            The import job view includes all metadata of
            an import job.
    """

    IMPORT_JOB_VIEW_UNSPECIFIED = 0
    IMPORT_JOB_VIEW_BASIC = 1
    IMPORT_JOB_VIEW_FULL = 2


class ErrorFrameView(proto.Enum):
    r"""ErrorFrameView can be specified in ErrorFrames List and Get
    requests to control the level of details that is returned for
    the original frame.

    Values:
        ERROR_FRAME_VIEW_UNSPECIFIED (0):
            Value is unset. The system will fallback to
            the default value.
        ERROR_FRAME_VIEW_BASIC (1):
            Include basic frame data, but not the full
            contents.
        ERROR_FRAME_VIEW_FULL (2):
            Include everything.
    """

    ERROR_FRAME_VIEW_UNSPECIFIED = 0
    ERROR_FRAME_VIEW_BASIC = 1
    ERROR_FRAME_VIEW_FULL = 2


class PersistentDiskType(proto.Enum):
    r"""The persistent disk (PD) types of Compute Engine virtual
    machines.

    Values:
        PERSISTENT_DISK_TYPE_UNSPECIFIED (0):
            Unspecified (default value).
            Selecting this value allows the system to use
            any disk type according to reported usage. This
            a good value to start with.
        PERSISTENT_DISK_TYPE_STANDARD (1):
            Standard HDD Persistent Disk.
        PERSISTENT_DISK_TYPE_BALANCED (2):
            Balanced Persistent Disk.
        PERSISTENT_DISK_TYPE_SSD (3):
            SSD Persistent Disk.
    """

    PERSISTENT_DISK_TYPE_UNSPECIFIED = 0
    PERSISTENT_DISK_TYPE_STANDARD = 1
    PERSISTENT_DISK_TYPE_BALANCED = 2
    PERSISTENT_DISK_TYPE_SSD = 3


class LicenseType(proto.Enum):
    r"""The License type for premium images (RHEL, RHEL for SAP,
    SLES, SLES for SAP, Windows Server).

    Values:
        LICENSE_TYPE_UNSPECIFIED (0):
            Unspecified (default value).
        LICENSE_TYPE_DEFAULT (1):
            Default Google Cloud licensing plan.
            Licensing is charged per usage. This a good
            value to start with.
        LICENSE_TYPE_BRING_YOUR_OWN_LICENSE (2):
            Bring-your-own-license (BYOL) plan. User
            provides the OS license.
    """

    LICENSE_TYPE_UNSPECIFIED = 0
    LICENSE_TYPE_DEFAULT = 1
    LICENSE_TYPE_BRING_YOUR_OWN_LICENSE = 2


class SizingOptimizationStrategy(proto.Enum):
    r"""The sizing optimization strategy preferences of a virtual
    machine. This strategy, in addition to actual usage data of the
    virtual machine, can help determine the recommended shape on the
    target platform.

    Values:
        SIZING_OPTIMIZATION_STRATEGY_UNSPECIFIED (0):
            Unspecified (default value).
        SIZING_OPTIMIZATION_STRATEGY_SAME_AS_SOURCE (1):
            No optimization applied. Virtual machine
            sizing matches as closely as possible the
            machine shape on the source site, not
            considering any actual performance data.
        SIZING_OPTIMIZATION_STRATEGY_MODERATE (2):
            Virtual machine sizing will match the
            reported usage and shape, with some slack. This
            a good value to start with.
        SIZING_OPTIMIZATION_STRATEGY_AGGRESSIVE (3):
            Virtual machine sizing will match the
            reported usage, with little slack. Using this
            option can help reduce costs.
    """

    SIZING_OPTIMIZATION_STRATEGY_UNSPECIFIED = 0
    SIZING_OPTIMIZATION_STRATEGY_SAME_AS_SOURCE = 1
    SIZING_OPTIMIZATION_STRATEGY_MODERATE = 2
    SIZING_OPTIMIZATION_STRATEGY_AGGRESSIVE = 3


class CommitmentPlan(proto.Enum):
    r"""The plan of commitments for VM resource-based committed use
    discount (CUD).

    Values:
        COMMITMENT_PLAN_UNSPECIFIED (0):
            Unspecified commitment plan.
        COMMITMENT_PLAN_NONE (1):
            No commitment plan.
        COMMITMENT_PLAN_ONE_YEAR (2):
            1 year commitment.
        COMMITMENT_PLAN_THREE_YEARS (3):
            3 years commitment.
    """

    COMMITMENT_PLAN_UNSPECIFIED = 0
    COMMITMENT_PLAN_NONE = 1
    COMMITMENT_PLAN_ONE_YEAR = 2
    COMMITMENT_PLAN_THREE_YEARS = 3


class ComputeMigrationTargetProduct(proto.Enum):
    r"""The preference for a specific Google Cloud product platform.

    Values:
        COMPUTE_MIGRATION_TARGET_PRODUCT_UNSPECIFIED (0):
            Unspecified (default value).
        COMPUTE_MIGRATION_TARGET_PRODUCT_COMPUTE_ENGINE (1):
            Prefer to migrate to Google Cloud Compute
            Engine.
        COMPUTE_MIGRATION_TARGET_PRODUCT_VMWARE_ENGINE (2):
            Prefer to migrate to Google Cloud VMware
            Engine.
        COMPUTE_MIGRATION_TARGET_PRODUCT_SOLE_TENANCY (3):
            Prefer to migrate to Google Cloud Sole Tenant
            Nodes.
    """

    COMPUTE_MIGRATION_TARGET_PRODUCT_UNSPECIFIED = 0
    COMPUTE_MIGRATION_TARGET_PRODUCT_COMPUTE_ENGINE = 1
    COMPUTE_MIGRATION_TARGET_PRODUCT_VMWARE_ENGINE = 2
    COMPUTE_MIGRATION_TARGET_PRODUCT_SOLE_TENANCY = 3


class ReportView(proto.Enum):
    r"""Specifies the types of views that provide complete or partial
    details of a Report.

    Values:
        REPORT_VIEW_UNSPECIFIED (0):
            The report view is not specified. The API
            displays the basic view by default.
        REPORT_VIEW_BASIC (1):
            The report view includes only basic metadata
            of the Report. Useful for list views.
        REPORT_VIEW_FULL (2):
            The report view includes all the metadata of
            the Report. Useful for preview.
        REPORT_VIEW_STANDARD (3):
            The report view includes the standard
            metadata of an report. Useful for detail view.
    """

    REPORT_VIEW_UNSPECIFIED = 0
    REPORT_VIEW_BASIC = 1
    REPORT_VIEW_FULL = 2
    REPORT_VIEW_STANDARD = 3


class Asset(proto.Message):
    r"""An asset represents a resource in your environment. Asset
    types include virtual machines and databases.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. The full name of the asset.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the asset was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the asset was
            last updated.
        labels (MutableMapping[str, str]):
            Labels as key value pairs.
        attributes (MutableMapping[str, str]):
            Generic asset attributes.
        machine_details (google.cloud.migrationcenter_v1.types.MachineDetails):
            Output only. Asset information specific for
            virtual and physical machines.

            This field is a member of `oneof`_ ``AssetDetails``.
        insight_list (google.cloud.migrationcenter_v1.types.InsightList):
            Output only. The list of insights associated
            with the asset.
        performance_data (google.cloud.migrationcenter_v1.types.AssetPerformanceData):
            Output only. Performance data for the asset.
        sources (MutableSequence[str]):
            Output only. The list of sources contributing
            to the asset.
        assigned_groups (MutableSequence[str]):
            Output only. The list of groups that the
            asset is assigned to.
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
    attributes: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    machine_details: "MachineDetails" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="AssetDetails",
        message="MachineDetails",
    )
    insight_list: "InsightList" = proto.Field(
        proto.MESSAGE,
        number=20,
        message="InsightList",
    )
    performance_data: "AssetPerformanceData" = proto.Field(
        proto.MESSAGE,
        number=21,
        message="AssetPerformanceData",
    )
    sources: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=22,
    )
    assigned_groups: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=23,
    )


class PreferenceSet(proto.Message):
    r"""The preferences that apply to all assets in a given context.

    Attributes:
        name (str):
            Output only. Name of the preference set.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the
            preference set was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the
            preference set was last updated.
        display_name (str):
            User-friendly display name. Maximum length is
            63 characters.
        description (str):
            A description of the preference set.
        virtual_machine_preferences (google.cloud.migrationcenter_v1.types.VirtualMachinePreferences):
            A set of preferences that applies to all
            virtual machines in the context.
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
        number=4,
    )
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    virtual_machine_preferences: "VirtualMachinePreferences" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="VirtualMachinePreferences",
    )


class ImportJob(proto.Message):
    r"""A resource that represents the background job that imports
    asset frames.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. The full name of the import job.
        display_name (str):
            User-friendly display name. Maximum length is
            63 characters.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the import
            job was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the import
            job was last updated.
        complete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the import
            job was completed.
        state (google.cloud.migrationcenter_v1.types.ImportJob.ImportJobState):
            Output only. The state of the import job.
        labels (MutableMapping[str, str]):
            Labels as key value pairs.
        asset_source (str):
            Required. Reference to a source.
        validation_report (google.cloud.migrationcenter_v1.types.ValidationReport):
            Output only. The report with the validation
            results of the import job.

            This field is a member of `oneof`_ ``report``.
        execution_report (google.cloud.migrationcenter_v1.types.ExecutionReport):
            Output only. The report with the results of
            running the import job.

            This field is a member of `oneof`_ ``report``.
    """

    class ImportJobState(proto.Enum):
        r"""Enumerates possible states of an import job.

        Values:
            IMPORT_JOB_STATE_UNSPECIFIED (0):
                Default value.
            IMPORT_JOB_STATE_PENDING (1):
                The import job is pending.
            IMPORT_JOB_STATE_RUNNING (2):
                The processing of the import job is ongoing.
            IMPORT_JOB_STATE_COMPLETED (3):
                The import job processing has completed.
            IMPORT_JOB_STATE_FAILED (4):
                The import job failed to be processed.
            IMPORT_JOB_STATE_VALIDATING (5):
                The import job is being validated.
            IMPORT_JOB_STATE_FAILED_VALIDATION (6):
                The import job contains blocking errors.
            IMPORT_JOB_STATE_READY (7):
                The validation of the job completed with no
                blocking errors.
        """

        IMPORT_JOB_STATE_UNSPECIFIED = 0
        IMPORT_JOB_STATE_PENDING = 1
        IMPORT_JOB_STATE_RUNNING = 2
        IMPORT_JOB_STATE_COMPLETED = 3
        IMPORT_JOB_STATE_FAILED = 4
        IMPORT_JOB_STATE_VALIDATING = 5
        IMPORT_JOB_STATE_FAILED_VALIDATION = 6
        IMPORT_JOB_STATE_READY = 7

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
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
    complete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    state: ImportJobState = proto.Field(
        proto.ENUM,
        number=6,
        enum=ImportJobState,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    asset_source: str = proto.Field(
        proto.STRING,
        number=8,
    )
    validation_report: "ValidationReport" = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="report",
        message="ValidationReport",
    )
    execution_report: "ExecutionReport" = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="report",
        message="ExecutionReport",
    )


class ImportDataFile(proto.Message):
    r"""A resource that represents a payload file in an import job.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. The name of the file.
        display_name (str):
            User-friendly display name. Maximum length is
            63 characters.
        format_ (google.cloud.migrationcenter_v1.types.ImportJobFormat):
            Required. The payload format.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the file was
            created.
        state (google.cloud.migrationcenter_v1.types.ImportDataFile.State):
            Output only. The state of the import data
            file.
        upload_file_info (google.cloud.migrationcenter_v1.types.UploadFileInfo):
            Information about a file that is uploaded to
            a storage service.

            This field is a member of `oneof`_ ``file_info``.
    """

    class State(proto.Enum):
        r"""Enumerates possible states of an import data file.

        Values:
            STATE_UNSPECIFIED (0):
                Default value.
            CREATING (1):
                The data file is being created.
            ACTIVE (2):
                The data file completed initialization.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=6,
    )
    format_: "ImportJobFormat" = proto.Field(
        proto.ENUM,
        number=2,
        enum="ImportJobFormat",
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
    upload_file_info: "UploadFileInfo" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="file_info",
        message="UploadFileInfo",
    )


class Group(proto.Message):
    r"""A resource that represents an asset group.
    The purpose of an asset group is to bundle a set of assets that
    have something in common, while allowing users to add
    annotations to the group. An asset can belong to multiple
    groups.

    Attributes:
        name (str):
            Output only. The name of the group.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the group was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the group was
            last updated.
        labels (MutableMapping[str, str]):
            Labels as key value pairs.
        display_name (str):
            User-friendly display name.
        description (str):
            The description of the resource.
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
    description: str = proto.Field(
        proto.STRING,
        number=6,
    )


class ErrorFrame(proto.Message):
    r"""Message representing a frame which failed to be processed due
    to an error.

    Attributes:
        name (str):
            Output only. The identifier of the
            ErrorFrame.
        violations (MutableSequence[google.cloud.migrationcenter_v1.types.FrameViolationEntry]):
            Output only. All the violations that were
            detected for the frame.
        original_frame (google.cloud.migrationcenter_v1.types.AssetFrame):
            Output only. The frame that was originally
            reported.
        ingestion_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Frame ingestion time.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    violations: MutableSequence["FrameViolationEntry"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="FrameViolationEntry",
    )
    original_frame: "AssetFrame" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="AssetFrame",
    )
    ingestion_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


class Source(proto.Message):
    r"""Source represents an object from which asset information is
    streamed to Migration Center.

    Attributes:
        name (str):
            Output only. The full name of the source.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the source
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the source
            was last updated.
        display_name (str):
            User-friendly display name.
        description (str):
            Free-text description.
        type_ (google.cloud.migrationcenter_v1.types.Source.SourceType):
            Data source type.
        priority (int):
            The information confidence of the source.
            The higher the value, the higher the confidence.
        managed (bool):
            If ``true``, the source is managed by other service(s).
        pending_frame_count (int):
            Output only. Number of frames that are still
            being processed.
        error_frame_count (int):
            Output only. The number of frames that were
            reported by the source and contained errors.
        state (google.cloud.migrationcenter_v1.types.Source.State):
            Output only. The state of the source.
    """

    class SourceType(proto.Enum):
        r"""

        Values:
            SOURCE_TYPE_UNKNOWN (0):
                Unspecified
            SOURCE_TYPE_UPLOAD (1):
                Manually uploaded file (e.g. CSV)
            SOURCE_TYPE_GUEST_OS_SCAN (2):
                Guest-level info
            SOURCE_TYPE_INVENTORY_SCAN (3):
                Inventory-level scan
            SOURCE_TYPE_CUSTOM (4):
                Third-party owned sources.
        """

        SOURCE_TYPE_UNKNOWN = 0
        SOURCE_TYPE_UPLOAD = 1
        SOURCE_TYPE_GUEST_OS_SCAN = 2
        SOURCE_TYPE_INVENTORY_SCAN = 3
        SOURCE_TYPE_CUSTOM = 4

    class State(proto.Enum):
        r"""Enumerates possible states of a source.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified.
            ACTIVE (1):
                The source is active and ready to be used.
            DELETING (2):
                In the process of being deleted.
            INVALID (3):
                Source is in an invalid state. Asset frames
                reported to it will be ignored.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        DELETING = 2
        INVALID = 3

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
        number=4,
    )
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    type_: SourceType = proto.Field(
        proto.ENUM,
        number=6,
        enum=SourceType,
    )
    priority: int = proto.Field(
        proto.INT32,
        number=7,
    )
    managed: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    pending_frame_count: int = proto.Field(
        proto.INT32,
        number=9,
    )
    error_frame_count: int = proto.Field(
        proto.INT32,
        number=10,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=11,
        enum=State,
    )


class ReportConfig(proto.Message):
    r"""The groups and associated preference sets on which
    we can generate reports.

    Attributes:
        name (str):
            Output only. Name of resource.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was last updated.
        display_name (str):
            User-friendly display name. Maximum length is
            63 characters.
        description (str):
            Free-text description.
        group_preferenceset_assignments (MutableSequence[google.cloud.migrationcenter_v1.types.ReportConfig.GroupPreferenceSetAssignment]):
            Required. Collection of combinations of
            groups and preference sets.
    """

    class GroupPreferenceSetAssignment(proto.Message):
        r"""Represents a combination of a group with a preference set.

        Attributes:
            group (str):
                Required. Name of the group.
            preference_set (str):
                Required. Name of the Preference Set.
        """

        group: str = proto.Field(
            proto.STRING,
            number=1,
        )
        preference_set: str = proto.Field(
            proto.STRING,
            number=2,
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
    display_name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    group_preferenceset_assignments: MutableSequence[GroupPreferenceSetAssignment] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=6,
            message=GroupPreferenceSetAssignment,
        )
    )


class Report(proto.Message):
    r"""Report represents a point-in-time rendering of the
    ReportConfig results.

    Attributes:
        name (str):
            Output only. Name of resource.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Creation timestamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Last update timestamp.
        display_name (str):
            User-friendly display name. Maximum length is
            63 characters.
        description (str):
            Free-text description.
        type_ (google.cloud.migrationcenter_v1.types.Report.Type):
            Report type.
        state (google.cloud.migrationcenter_v1.types.Report.State):
            Report creation state.
        summary (google.cloud.migrationcenter_v1.types.ReportSummary):
            Output only. Summary view of the Report.
    """

    class Type(proto.Enum):
        r"""Report type.

        Values:
            TYPE_UNSPECIFIED (0):
                Default Report type.
            TOTAL_COST_OF_OWNERSHIP (1):
                Total cost of ownership Report type.
        """

        TYPE_UNSPECIFIED = 0
        TOTAL_COST_OF_OWNERSHIP = 1

    class State(proto.Enum):
        r"""Report creation state.

        Values:
            STATE_UNSPECIFIED (0):
                Default Report creation state.
            PENDING (1):
                Creating Report.
            SUCCEEDED (2):
                Successfully created Report.
            FAILED (3):
                Failed to create Report.
        """

        STATE_UNSPECIFIED = 0
        PENDING = 1
        SUCCEEDED = 2
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
    display_name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=6,
        enum=Type,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=7,
        enum=State,
    )
    summary: "ReportSummary" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="ReportSummary",
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


class ListAssetsRequest(proto.Message):
    r"""Message for requesting a list of assets.

    Attributes:
        parent (str):
            Required. Parent value for ``ListAssetsRequest``.
        page_size (int):
            Requested page size. Server may return fewer
            items than requested. If unspecified, server
            will pick an appropriate default.
        page_token (str):
            A token identifying a page of results the
            server should return.
        filter (str):
            Filtering results.
        order_by (str):
            Field to sort by. See
            https://google.aip.dev/132#ordering for more
            details.
        view (google.cloud.migrationcenter_v1.types.AssetView):
            View of the assets. Defaults to BASIC.
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
    view: "AssetView" = proto.Field(
        proto.ENUM,
        number=6,
        enum="AssetView",
    )


class ListAssetsResponse(proto.Message):
    r"""Response message for listing assets.

    Attributes:
        assets (MutableSequence[google.cloud.migrationcenter_v1.types.Asset]):
            A list of assets.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    assets: MutableSequence["Asset"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Asset",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetAssetRequest(proto.Message):
    r"""Message for getting a Asset.

    Attributes:
        name (str):
            Required. Name of the resource.
        view (google.cloud.migrationcenter_v1.types.AssetView):
            View of the assets. Defaults to BASIC.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: "AssetView" = proto.Field(
        proto.ENUM,
        number=2,
        enum="AssetView",
    )


class UpdateAssetRequest(proto.Message):
    r"""A request to update an asset.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the ``Asset`` resource by the update. The
            values specified in the ``update_mask`` field are relative
            to the resource, not the full request. A field will be
            overwritten if it is in the mask. A single \* value in the
            mask lets you to overwrite all fields.
        asset (google.cloud.migrationcenter_v1.types.Asset):
            Required. The resource being updated.
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
    asset: "Asset" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Asset",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class BatchUpdateAssetsRequest(proto.Message):
    r"""A request to update a list of assets.

    Attributes:
        parent (str):
            Required. Parent value for batch asset
            update.
        requests (MutableSequence[google.cloud.migrationcenter_v1.types.UpdateAssetRequest]):
            Required. The request message specifying the
            resources to update. A maximum of 1000 assets
            can be modified in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["UpdateAssetRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="UpdateAssetRequest",
    )


class BatchUpdateAssetsResponse(proto.Message):
    r"""Response for updating a list of assets.

    Attributes:
        assets (MutableSequence[google.cloud.migrationcenter_v1.types.Asset]):
            Update asset content.
            The content only includes values after field
            mask being applied.
    """

    assets: MutableSequence["Asset"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Asset",
    )


class DeleteAssetRequest(proto.Message):
    r"""A request to delete an asset.

    Attributes:
        name (str):
            Required. Name of the resource.
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


class BatchDeleteAssetsRequest(proto.Message):
    r"""A request to delete a list of  asset.

    Attributes:
        parent (str):
            Required. Parent value for batch asset
            delete.
        names (MutableSequence[str]):
            Required. The IDs of the assets to delete.
            A maximum of 1000 assets can be deleted in a
            batch. Format:
            projects/{project}/locations/{location}/assets/{name}.
        allow_missing (bool):
            Optional. When this value is set to ``true`` the request is
            a no-op for non-existing assets. See
            https://google.aip.dev/135#delete-if-existing for additional
            details. Default value is ``false``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class ReportAssetFramesRequest(proto.Message):
    r"""A request to report a set of asset frames.

    Attributes:
        parent (str):
            Required. Parent of the resource.
        frames (google.cloud.migrationcenter_v1.types.Frames):
            Collection of frames data.
        source (str):
            Required. Reference to a source.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    frames: "Frames" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Frames",
    )
    source: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ReportAssetFramesResponse(proto.Message):
    r"""A response to a call to ``ReportAssetFrame``."""


class AggregateAssetsValuesRequest(proto.Message):
    r"""A request to aggregate one or more values.

    Attributes:
        parent (str):
            Required. Parent value for ``AggregateAssetsValuesRequest``.
        aggregations (MutableSequence[google.cloud.migrationcenter_v1.types.Aggregation]):
            Array of aggregations to perform.
            Up to 25 aggregations can be defined.
        filter (str):
            The aggregation will be performed on assets
            that match the provided filter.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    aggregations: MutableSequence["Aggregation"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Aggregation",
    )
    filter: str = proto.Field(
        proto.STRING,
        number=3,
    )


class AggregateAssetsValuesResponse(proto.Message):
    r"""A response to a request to aggregated assets values.

    Attributes:
        results (MutableSequence[google.cloud.migrationcenter_v1.types.AggregationResult]):
            The aggregation results.
    """

    results: MutableSequence["AggregationResult"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AggregationResult",
    )


class CreateImportJobRequest(proto.Message):
    r"""A request to create an import job.

    Attributes:
        parent (str):
            Required. Value for parent.
        import_job_id (str):
            Required. ID of the import job.
        import_job (google.cloud.migrationcenter_v1.types.ImportJob):
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
    import_job_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    import_job: "ImportJob" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ImportJob",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListImportJobsRequest(proto.Message):
    r"""A request to list import jobs.

    Attributes:
        parent (str):
            Required. Parent value for ``ListImportJobsRequest``.
        page_size (int):
            Requested page size. Server may return fewer
            items than requested. If unspecified, server
            will pick an appropriate default.
        page_token (str):
            A token identifying a page of results the
            server should return.
        filter (str):
            Filtering results.
        order_by (str):
            Field to sort by. See
            https://google.aip.dev/132#ordering for more
            details.
        view (google.cloud.migrationcenter_v1.types.ImportJobView):
            Optional. The level of details of each import
            job. Default value is BASIC.
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
    view: "ImportJobView" = proto.Field(
        proto.ENUM,
        number=6,
        enum="ImportJobView",
    )


class ListImportJobsResponse(proto.Message):
    r"""A response for listing import jobs.

    Attributes:
        import_jobs (MutableSequence[google.cloud.migrationcenter_v1.types.ImportJob]):
            The list of import jobs.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    import_jobs: MutableSequence["ImportJob"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ImportJob",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetImportJobRequest(proto.Message):
    r"""A request to get an import job.

    Attributes:
        name (str):
            Required. Name of the resource.
        view (google.cloud.migrationcenter_v1.types.ImportJobView):
            Optional. The level of details of the import
            job. Default value is FULL.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: "ImportJobView" = proto.Field(
        proto.ENUM,
        number=2,
        enum="ImportJobView",
    )


class DeleteImportJobRequest(proto.Message):
    r"""A request to delete an import job.

    Attributes:
        name (str):
            Required. Name of the resource.
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
            Optional. If set to ``true``, any ``ImportDataFiles`` of
            this job will also be deleted If set to ``false``, the
            request only works if the job has no data files.
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


class UpdateImportJobRequest(proto.Message):
    r"""A request to update an import job.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the ``Asset`` resource by the update. The
            values specified in the ``update_mask`` field are relative
            to the resource, not the full request. A field will be
            overwritten if it is in the mask. A single \* value in the
            mask lets you to overwrite all fields.
        import_job (google.cloud.migrationcenter_v1.types.ImportJob):
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
    import_job: "ImportJob" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ImportJob",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ValidateImportJobRequest(proto.Message):
    r"""A request to validate an import job.

    Attributes:
        name (str):
            Required. The name of the import job to
            validate.
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


class RunImportJobRequest(proto.Message):
    r"""A request to run an import job.

    Attributes:
        name (str):
            Required. The name of the import job to run.
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


class GetImportDataFileRequest(proto.Message):
    r"""A request to get an import data file.

    Attributes:
        name (str):
            Required. Name of the ImportDataFile.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListImportDataFilesRequest(proto.Message):
    r"""A request to list import data files of an import job.

    Attributes:
        parent (str):
            Required. Name of the parent of the ``ImportDataFiles``
            resource.
        page_size (int):
            The maximum number of data files to return.
            The service may return fewer than this value. If
            unspecified, at most 500 data files will be
            returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            A page token, received from a previous
            ``ListImportDataFiles`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListImportDataFiles`` must match the call that provided
            the page token.
        filter (str):
            Filtering results.
        order_by (str):
            Field to sort by. See
            https://google.aip.dev/132#ordering for more
            details.
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


class ListImportDataFilesResponse(proto.Message):
    r"""Response for listing payload files of an import job.

    Attributes:
        import_data_files (MutableSequence[google.cloud.migrationcenter_v1.types.ImportDataFile]):
            The list of import data files.
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

    import_data_files: MutableSequence["ImportDataFile"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ImportDataFile",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class CreateImportDataFileRequest(proto.Message):
    r"""A request to create an ``ImportDataFile`` resource.

    Attributes:
        parent (str):
            Required. Name of the parent of the
            ImportDataFile.
        import_data_file_id (str):
            Required. The ID of the new data file.
        import_data_file (google.cloud.migrationcenter_v1.types.ImportDataFile):
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
    import_data_file_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    import_data_file: "ImportDataFile" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ImportDataFile",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteImportDataFileRequest(proto.Message):
    r"""A request to delete an ``ImportDataFile`` resource.

    Attributes:
        name (str):
            Required. Name of the ImportDataFile to
            delete.
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


class ListGroupsRequest(proto.Message):
    r"""A request to list groups.

    Attributes:
        parent (str):
            Required. Parent value for ``ListGroupsRequest``.
        page_size (int):
            Requested page size. Server may return fewer
            items than requested. If unspecified, server
            will pick an appropriate default.
        page_token (str):
            A token identifying a page of results the
            server should return.
        filter (str):
            Filtering results.
        order_by (str):
            Field to sort by. See
            https://google.aip.dev/132#ordering for more
            details.
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


class ListGroupsResponse(proto.Message):
    r"""A response for listing groups.

    Attributes:
        groups (MutableSequence[google.cloud.migrationcenter_v1.types.Group]):
            The list of Group
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    groups: MutableSequence["Group"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Group",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetGroupRequest(proto.Message):
    r"""A request to get a group.

    Attributes:
        name (str):
            Required. Name of the resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateGroupRequest(proto.Message):
    r"""A request to create a group.

    Attributes:
        parent (str):
            Required. Value for parent.
        group_id (str):
            Required. User specified ID for the group. It will become
            the last component of the group name. The ID must be unique
            within the project, must conform with RFC-1034, is
            restricted to lower-cased letters, and has a maximum length
            of 63 characters. The ID must match the regular expression:
            ``[a-z]([a-z0-9-]{0,61}[a-z0-9])?``.
        group (google.cloud.migrationcenter_v1.types.Group):
            Required. The group resource being created.
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
    group_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    group: "Group" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Group",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateGroupRequest(proto.Message):
    r"""A request to update a group.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the ``Group`` resource by the update. The
            values specified in the ``update_mask`` are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. A single \* value in the mask lets you
            to overwrite all fields.
        group (google.cloud.migrationcenter_v1.types.Group):
            Required. The group resource being updated.
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
    group: "Group" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Group",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteGroupRequest(proto.Message):
    r"""A request to delete a group.

    Attributes:
        name (str):
            Required. Name of the group resource.
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


class AddAssetsToGroupRequest(proto.Message):
    r"""A request to add assets to a group.

    Attributes:
        group (str):
            Required. Group reference.
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
        assets (google.cloud.migrationcenter_v1.types.AssetList):
            Required. List of assets to be added.
            The maximum number of assets that can be added
            in a single request is 1000.
        allow_existing (bool):
            Optional. When this value is set to ``false`` and one of the
            given assets is already an existing member of the group, the
            operation fails with an ``Already Exists`` error. When set
            to ``true`` this situation is silently ignored by the
            server.

            Default value is ``false``.
    """

    group: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    assets: "AssetList" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="AssetList",
    )
    allow_existing: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class RemoveAssetsFromGroupRequest(proto.Message):
    r"""A request to remove assets from a group.

    Attributes:
        group (str):
            Required. Group reference.
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
        assets (google.cloud.migrationcenter_v1.types.AssetList):
            Required. List of assets to be removed.
            The maximum number of assets that can be removed
            in a single request is 1000.
        allow_missing (bool):
            Optional. When this value is set to ``false`` and one of the
            given assets is not an existing member of the group, the
            operation fails with a ``Not Found`` error. When set to
            ``true`` this situation is silently ignored by the server.

            Default value is ``false``.
    """

    group: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    assets: "AssetList" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="AssetList",
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class ListErrorFramesRequest(proto.Message):
    r"""A request to list error frames for a source.

    Attributes:
        parent (str):
            Required. Parent value (the source) for
            ``ListErrorFramesRequest``.
        page_size (int):
            Requested page size. Server may return fewer
            items than requested. If unspecified, server
            will pick an appropriate default.
        page_token (str):
            A token identifying a page of results the
            server should return.
        view (google.cloud.migrationcenter_v1.types.ErrorFrameView):
            Optional. An optional view mode to control
            the level of details of each error frame. The
            default is a BASIC frame view.
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
    view: "ErrorFrameView" = proto.Field(
        proto.ENUM,
        number=4,
        enum="ErrorFrameView",
    )


class ListErrorFramesResponse(proto.Message):
    r"""A response for listing error frames.

    Attributes:
        error_frames (MutableSequence[google.cloud.migrationcenter_v1.types.ErrorFrame]):
            The list of error frames.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    error_frames: MutableSequence["ErrorFrame"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ErrorFrame",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetErrorFrameRequest(proto.Message):
    r"""

    Attributes:
        name (str):
            Required. The name of the frame to retrieve. Format:
            projects/{project}/locations/{location}/sources/{source}/errorFrames/{error_frame}
        view (google.cloud.migrationcenter_v1.types.ErrorFrameView):
            Optional. An optional view mode to control
            the level of details for the frame. The default
            is a basic frame view.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: "ErrorFrameView" = proto.Field(
        proto.ENUM,
        number=2,
        enum="ErrorFrameView",
    )


class ListSourcesRequest(proto.Message):
    r"""A request for a list of sources.

    Attributes:
        parent (str):
            Required. Parent value for ``ListSourcesRequest``.
        page_size (int):
            Requested page size. The server may return
            fewer items than requested. If unspecified, the
            server will pick an appropriate default value.
        page_token (str):
            A token identifying a page of results that
            the server should return.
        filter (str):
            Filtering results.
        order_by (str):
            Field to sort by. See
            https://google.aip.dev/132#ordering for more
            details.
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


class ListSourcesResponse(proto.Message):
    r"""Response message for listing sources.

    Attributes:
        sources (MutableSequence[google.cloud.migrationcenter_v1.types.Source]):
            The list of sources.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    sources: MutableSequence["Source"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Source",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetSourceRequest(proto.Message):
    r"""A request to get a source.

    Attributes:
        name (str):
            Required. Name of the resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateSourceRequest(proto.Message):
    r"""A request to create a source.

    Attributes:
        parent (str):
            Required. Value for parent.
        source_id (str):
            Required. User specified ID for the source. It will become
            the last component of the source name. The ID must be unique
            within the project, must conform with RFC-1034, is
            restricted to lower-cased letters, and has a maximum length
            of 63 characters. The ID must match the regular expression:
            ``[a-z]([a-z0-9-]{0,61}[a-z0-9])?``.
        source (google.cloud.migrationcenter_v1.types.Source):
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
    source_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    source: "Source" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Source",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateSourceRequest(proto.Message):
    r"""A request to update a source.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the ``Source`` resource by the update. The
            values specified in the ``update_mask`` field are relative
            to the resource, not the full request. A field will be
            overwritten if it is in the mask. A single \* value in the
            mask lets you to overwrite all fields.
        source (google.cloud.migrationcenter_v1.types.Source):
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
    source: "Source" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Source",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteSourceRequest(proto.Message):
    r"""A request to delete a source.

    Attributes:
        name (str):
            Required. Name of the resource.
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


class ListPreferenceSetsRequest(proto.Message):
    r"""Request for listing preference sets.

    Attributes:
        parent (str):
            Required. Parent value for ``ListPreferenceSetsRequest``.
        page_size (int):
            Requested page size. Server may return fewer
            items than requested. If unspecified, at most
            500 preference sets will be returned. The
            maximum value is 1000; values above 1000 will be
            coerced to 1000.
        page_token (str):
            A token identifying a page of results the
            server should return.
        order_by (str):
            Field to sort by. See
            https://google.aip.dev/132#ordering for more
            details.
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
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListPreferenceSetsResponse(proto.Message):
    r"""Response message for listing preference sets.

    Attributes:
        preference_sets (MutableSequence[google.cloud.migrationcenter_v1.types.PreferenceSet]):
            The list of PreferenceSets
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    preference_sets: MutableSequence["PreferenceSet"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="PreferenceSet",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetPreferenceSetRequest(proto.Message):
    r"""A request to get a preference set.

    Attributes:
        name (str):
            Required. Name of the resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreatePreferenceSetRequest(proto.Message):
    r"""A request to create a preference set.

    Attributes:
        parent (str):
            Required. Value for parent.
        preference_set_id (str):
            Required. User specified ID for the preference set. It will
            become the last component of the preference set name. The ID
            must be unique within the project, must conform with
            RFC-1034, is restricted to lower-cased letters, and has a
            maximum length of 63 characters. The ID must match the
            regular expression ``[a-z]([a-z0-9-]{0,61}[a-z0-9])?``.
        preference_set (google.cloud.migrationcenter_v1.types.PreferenceSet):
            Required. The preference set resource being
            created.
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
    preference_set_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    preference_set: "PreferenceSet" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="PreferenceSet",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdatePreferenceSetRequest(proto.Message):
    r"""A request to update a preference set.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the ``PreferenceSet`` resource by the update.
            The values specified in the ``update_mask`` field are
            relative to the resource, not the full request. A field will
            be overwritten if it is in the mask. A single \* value in
            the mask lets you to overwrite all fields.
        preference_set (google.cloud.migrationcenter_v1.types.PreferenceSet):
            Required. The preference set resource being
            updated.
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
    preference_set: "PreferenceSet" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="PreferenceSet",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeletePreferenceSetRequest(proto.Message):
    r"""A request to delete a preference set.

    Attributes:
        name (str):
            Required. Name of the group resource.
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


class GetSettingsRequest(proto.Message):
    r"""A request to get the settings.

    Attributes:
        name (str):
            Required. Name of the resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateSettingsRequest(proto.Message):
    r"""A request to update the settings.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the ``Settings`` resource by the update. The
            values specified in the ``update_mask`` field are relative
            to the resource, not the full request. A field will be
            overwritten if it is in the mask. A single \* value in the
            mask lets you to overwrite all fields.
        settings (google.cloud.migrationcenter_v1.types.Settings):
            Required. The project settings resource being
            updated.
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
    settings: "Settings" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Settings",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class CreateReportConfigRequest(proto.Message):
    r"""A request to create a ``ReportConfig`` resource.

    Attributes:
        parent (str):
            Required. Value for parent.
        report_config_id (str):
            Required. User specified ID for the report config. It will
            become the last component of the report config name. The ID
            must be unique within the project, must conform with
            RFC-1034, is restricted to lower-cased letters, and has a
            maximum length of 63 characters. The ID must match the
            regular expression: `a-z <[a-z0-9-]{0,61}[a-z0-9]>`__?.
        report_config (google.cloud.migrationcenter_v1.types.ReportConfig):
            Required. The report config set resource
            being created.
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
    report_config_id: str = proto.Field(
        proto.STRING,
        number=2,
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


class DeleteReportConfigRequest(proto.Message):
    r"""A request to delete a ReportConfig.

    Attributes:
        name (str):
            Required. Name of the resource.
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
            Optional. If set to ``true``, any child ``Reports`` of this
            entity will also be deleted. If set to ``false``, the
            request only works if the resource has no children.
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


class GetReportRequest(proto.Message):
    r"""A request to get a Report.

    Attributes:
        name (str):
            Required. Name of the resource.
        view (google.cloud.migrationcenter_v1.types.ReportView):
            Determines what information to retrieve for
            the Report.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: "ReportView" = proto.Field(
        proto.ENUM,
        number=6,
        enum="ReportView",
    )


class ListReportsRequest(proto.Message):
    r"""A request for a list of Reports.

    Attributes:
        parent (str):
            Required. Parent value for ``ListReportsRequest``.
        page_size (int):
            Requested page size. The server may return
            fewer items than requested. If unspecified, the
            server will pick an appropriate default value.
        page_token (str):
            A token identifying a page of results that
            the server should return.
        filter (str):
            Filtering results.
        order_by (str):
            Field to sort by. See
            https://google.aip.dev/132#ordering for more
            details.
        view (google.cloud.migrationcenter_v1.types.ReportView):
            Determines what information to retrieve for
            each Report.
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
    view: "ReportView" = proto.Field(
        proto.ENUM,
        number=6,
        enum="ReportView",
    )


class ListReportsResponse(proto.Message):
    r"""Response message for listing Reports.

    Attributes:
        reports (MutableSequence[google.cloud.migrationcenter_v1.types.Report]):
            The list of Reports.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    reports: MutableSequence["Report"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Report",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class DeleteReportRequest(proto.Message):
    r"""A request to delete a Report.

    Attributes:
        name (str):
            Required. Name of the resource.
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


class GetReportConfigRequest(proto.Message):
    r"""A request to get a ``ReportConfig`` resource.

    Attributes:
        name (str):
            Required. Name of the resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListReportConfigsRequest(proto.Message):
    r"""A request to get a list of ``ReportConfig`` resources.

    Attributes:
        parent (str):
            Required. Parent value for ``ListReportConfigsRequest``.
        page_size (int):
            Requested page size. Server may return fewer
            items than requested. If unspecified, server
            will pick an appropriate default.
        page_token (str):
            A token identifying a page of results the
            server should return.
        filter (str):
            Filtering results.
        order_by (str):
            Field to sort by. See
            https://google.aip.dev/132#ordering for more
            details.
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
    r"""Response message for listing report configs.

    Attributes:
        report_configs (MutableSequence[google.cloud.migrationcenter_v1.types.ReportConfig]):
            A list of report configs.
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


class CreateReportRequest(proto.Message):
    r"""Message for creating a Report.

    Attributes:
        parent (str):
            Required. Value for parent.
        report_id (str):
            Required. User specified id for the report. It will become
            the last component of the report name. The id must be unique
            within the project, must conform with RFC-1034, is
            restricted to lower-cased letters, and has a maximum length
            of 63 characters. The id must match the regular expression:
            `a-z <[a-z0-9-]{0,61}[a-z0-9]>`__?.
        report (google.cloud.migrationcenter_v1.types.Report):
            Required. The report resource being created.
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
    report_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    report: "Report" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Report",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class Frames(proto.Message):
    r"""Collection of frame data.

    Attributes:
        frames_data (MutableSequence[google.cloud.migrationcenter_v1.types.AssetFrame]):
            A repeated field of asset data.
    """

    frames_data: MutableSequence["AssetFrame"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AssetFrame",
    )


class AssetFrame(proto.Message):
    r"""Contains data reported from an inventory source on an asset.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        machine_details (google.cloud.migrationcenter_v1.types.MachineDetails):
            Asset information specific for virtual
            machines.

            This field is a member of `oneof`_ ``FrameData``.
        report_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the data was reported.
        labels (MutableMapping[str, str]):
            Labels as key value pairs.
        attributes (MutableMapping[str, str]):
            Generic asset attributes.
        performance_samples (MutableSequence[google.cloud.migrationcenter_v1.types.PerformanceSample]):
            Asset performance data samples.
            Samples that are from more than 40 days ago or
            after tomorrow are ignored.
        trace_token (str):
            Optional. Trace token is optionally provided
            to assist with debugging and traceability.
    """

    machine_details: "MachineDetails" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="FrameData",
        message="MachineDetails",
    )
    report_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=11,
    )
    attributes: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=12,
    )
    performance_samples: MutableSequence["PerformanceSample"] = proto.RepeatedField(
        proto.MESSAGE,
        number=13,
        message="PerformanceSample",
    )
    trace_token: str = proto.Field(
        proto.STRING,
        number=14,
    )


class MachineDetails(proto.Message):
    r"""Details of a machine.

    Attributes:
        uuid (str):
            Machine unique identifier.
        machine_name (str):
            Machine name.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Machine creation time.
        core_count (int):
            Number of CPU cores in the machine. Must be
            non-negative.
        memory_mb (int):
            The amount of memory in the machine. Must be
            non-negative.
        power_state (google.cloud.migrationcenter_v1.types.MachineDetails.PowerState):
            Power state of the machine.
        architecture (google.cloud.migrationcenter_v1.types.MachineArchitectureDetails):
            Architecture details (vendor, CPU
            architecture).
        guest_os (google.cloud.migrationcenter_v1.types.GuestOsDetails):
            Guest OS information.
        network (google.cloud.migrationcenter_v1.types.MachineNetworkDetails):
            Network details.
        disks (google.cloud.migrationcenter_v1.types.MachineDiskDetails):
            Disk details.
        platform (google.cloud.migrationcenter_v1.types.PlatformDetails):
            Platform specific information.
    """

    class PowerState(proto.Enum):
        r"""Machine power state.

        Values:
            POWER_STATE_UNSPECIFIED (0):
                Power state is unknown.
            PENDING (1):
                The machine is preparing to enter the ACTIVE
                state. An instance may enter the PENDING state
                when it launches for the first time, or when it
                is started after being in the SUSPENDED state.
            ACTIVE (2):
                The machine is active.
            SUSPENDING (3):
                The machine is being turned off.
            SUSPENDED (4):
                The machine is off.
            DELETING (5):
                The machine is being deleted from the hosting
                platform.
            DELETED (6):
                The machine is deleted from the hosting
                platform.
        """

        POWER_STATE_UNSPECIFIED = 0
        PENDING = 1
        ACTIVE = 2
        SUSPENDING = 3
        SUSPENDED = 4
        DELETING = 5
        DELETED = 6

    uuid: str = proto.Field(
        proto.STRING,
        number=1,
    )
    machine_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    core_count: int = proto.Field(
        proto.INT32,
        number=4,
    )
    memory_mb: int = proto.Field(
        proto.INT32,
        number=5,
    )
    power_state: PowerState = proto.Field(
        proto.ENUM,
        number=6,
        enum=PowerState,
    )
    architecture: "MachineArchitectureDetails" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="MachineArchitectureDetails",
    )
    guest_os: "GuestOsDetails" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="GuestOsDetails",
    )
    network: "MachineNetworkDetails" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="MachineNetworkDetails",
    )
    disks: "MachineDiskDetails" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="MachineDiskDetails",
    )
    platform: "PlatformDetails" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="PlatformDetails",
    )


class MachineArchitectureDetails(proto.Message):
    r"""Details of the machine architecture.

    Attributes:
        cpu_architecture (str):
            CPU architecture, e.g., "x64-based PC", "x86_64", "i686"
            etc.
        cpu_name (str):
            CPU name, e.g., "Intel Xeon E5-2690", "AMD
            EPYC 7571" etc.
        vendor (str):
            Hardware vendor.
        cpu_thread_count (int):
            Number of CPU threads allocated to the
            machine.
        cpu_socket_count (int):
            Number of processor sockets allocated to the
            machine.
        bios (google.cloud.migrationcenter_v1.types.BiosDetails):
            BIOS Details.
        firmware_type (google.cloud.migrationcenter_v1.types.MachineArchitectureDetails.FirmwareType):
            Firmware type.
        hyperthreading (google.cloud.migrationcenter_v1.types.MachineArchitectureDetails.CpuHyperThreading):
            CPU hyper-threading support.
    """

    class FirmwareType(proto.Enum):
        r"""Firmware type.

        Values:
            FIRMWARE_TYPE_UNSPECIFIED (0):
                Unspecified or unknown.
            BIOS (1):
                BIOS firmware.
            EFI (2):
                EFI firmware.
        """

        FIRMWARE_TYPE_UNSPECIFIED = 0
        BIOS = 1
        EFI = 2

    class CpuHyperThreading(proto.Enum):
        r"""CPU hyper-threading support.

        Values:
            CPU_HYPER_THREADING_UNSPECIFIED (0):
                Unspecified or unknown.
            DISABLED (1):
                Hyper-threading is disabled.
            ENABLED (2):
                Hyper-threading is enabled.
        """

        CPU_HYPER_THREADING_UNSPECIFIED = 0
        DISABLED = 1
        ENABLED = 2

    cpu_architecture: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cpu_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    vendor: str = proto.Field(
        proto.STRING,
        number=3,
    )
    cpu_thread_count: int = proto.Field(
        proto.INT32,
        number=4,
    )
    cpu_socket_count: int = proto.Field(
        proto.INT32,
        number=5,
    )
    bios: "BiosDetails" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="BiosDetails",
    )
    firmware_type: FirmwareType = proto.Field(
        proto.ENUM,
        number=7,
        enum=FirmwareType,
    )
    hyperthreading: CpuHyperThreading = proto.Field(
        proto.ENUM,
        number=8,
        enum=CpuHyperThreading,
    )


class BiosDetails(proto.Message):
    r"""Details about the BIOS.

    Attributes:
        bios_name (str):
            BIOS name. This fields is deprecated. Please use the ``id``
            field instead.
        id (str):
            BIOS ID.
        manufacturer (str):
            BIOS manufacturer.
        version (str):
            BIOS version.
        release_date (google.type.date_pb2.Date):
            BIOS release date.
        smbios_uuid (str):
            SMBIOS UUID.
    """

    bios_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    manufacturer: str = proto.Field(
        proto.STRING,
        number=3,
    )
    version: str = proto.Field(
        proto.STRING,
        number=4,
    )
    release_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=5,
        message=date_pb2.Date,
    )
    smbios_uuid: str = proto.Field(
        proto.STRING,
        number=6,
    )


class MachineNetworkDetails(proto.Message):
    r"""Details of network adapters and settings.

    Attributes:
        primary_ip_address (str):
            The primary IP address of the machine.
        public_ip_address (str):
            The public IP address of the machine.
        primary_mac_address (str):
            MAC address of the machine.
            This property is used to uniqly identify the
            machine.
        adapters (google.cloud.migrationcenter_v1.types.NetworkAdapterList):
            List of network adapters.
    """

    primary_ip_address: str = proto.Field(
        proto.STRING,
        number=1,
    )
    public_ip_address: str = proto.Field(
        proto.STRING,
        number=2,
    )
    primary_mac_address: str = proto.Field(
        proto.STRING,
        number=3,
    )
    adapters: "NetworkAdapterList" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="NetworkAdapterList",
    )


class NetworkAdapterList(proto.Message):
    r"""List of network adapters.

    Attributes:
        entries (MutableSequence[google.cloud.migrationcenter_v1.types.NetworkAdapterDetails]):
            Network adapter entries.
    """

    entries: MutableSequence["NetworkAdapterDetails"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="NetworkAdapterDetails",
    )


class NetworkAdapterDetails(proto.Message):
    r"""Details of network adapter.

    Attributes:
        adapter_type (str):
            Network adapter type (e.g. VMXNET3).
        mac_address (str):
            MAC address.
        addresses (google.cloud.migrationcenter_v1.types.NetworkAddressList):
            NetworkAddressList
    """

    adapter_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    mac_address: str = proto.Field(
        proto.STRING,
        number=2,
    )
    addresses: "NetworkAddressList" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="NetworkAddressList",
    )


class NetworkAddressList(proto.Message):
    r"""List of allocated/assigned network addresses.

    Attributes:
        entries (MutableSequence[google.cloud.migrationcenter_v1.types.NetworkAddress]):
            Network address entries.
    """

    entries: MutableSequence["NetworkAddress"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="NetworkAddress",
    )


class NetworkAddress(proto.Message):
    r"""Details of network address.

    Attributes:
        ip_address (str):
            Assigned or configured IP Address.
        subnet_mask (str):
            Subnet mask.
        bcast (str):
            Broadcast address.
        fqdn (str):
            Fully qualified domain name.
        assignment (google.cloud.migrationcenter_v1.types.NetworkAddress.AddressAssignment):
            Whether DHCP is used to assign addresses.
    """

    class AddressAssignment(proto.Enum):
        r"""Network address assignment.

        Values:
            ADDRESS_ASSIGNMENT_UNSPECIFIED (0):
                Unknown (default value).
            ADDRESS_ASSIGNMENT_STATIC (1):
                Staticly assigned IP.
            ADDRESS_ASSIGNMENT_DHCP (2):
                Dynamically assigned IP (DHCP).
        """

        ADDRESS_ASSIGNMENT_UNSPECIFIED = 0
        ADDRESS_ASSIGNMENT_STATIC = 1
        ADDRESS_ASSIGNMENT_DHCP = 2

    ip_address: str = proto.Field(
        proto.STRING,
        number=1,
    )
    subnet_mask: str = proto.Field(
        proto.STRING,
        number=2,
    )
    bcast: str = proto.Field(
        proto.STRING,
        number=3,
    )
    fqdn: str = proto.Field(
        proto.STRING,
        number=4,
    )
    assignment: AddressAssignment = proto.Field(
        proto.ENUM,
        number=5,
        enum=AddressAssignment,
    )


class MachineDiskDetails(proto.Message):
    r"""Details of machine disks.

    Attributes:
        total_capacity_bytes (int):
            Disk total Capacity.
        total_free_bytes (int):
            Total disk free space.
        disks (google.cloud.migrationcenter_v1.types.DiskEntryList):
            List of disks.
    """

    total_capacity_bytes: int = proto.Field(
        proto.INT64,
        number=1,
    )
    total_free_bytes: int = proto.Field(
        proto.INT64,
        number=2,
    )
    disks: "DiskEntryList" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="DiskEntryList",
    )


class DiskEntryList(proto.Message):
    r"""VM disks.

    Attributes:
        entries (MutableSequence[google.cloud.migrationcenter_v1.types.DiskEntry]):
            Disk entries.
    """

    entries: MutableSequence["DiskEntry"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DiskEntry",
    )


class DiskEntry(proto.Message):
    r"""Single disk entry.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        capacity_bytes (int):
            Disk capacity.
        free_bytes (int):
            Disk free space.
        disk_label (str):
            Disk label.
        disk_label_type (str):
            Disk label type (e.g. BIOS/GPT)
        interface_type (google.cloud.migrationcenter_v1.types.DiskEntry.InterfaceType):
            Disks interface type.
        partitions (google.cloud.migrationcenter_v1.types.DiskPartitionList):
            Partition layout.
        hw_address (str):
            Disk hardware address (e.g. 0:1 for SCSI).
        vmware (google.cloud.migrationcenter_v1.types.VmwareDiskConfig):
            VMware disk details.

            This field is a member of `oneof`_ ``platform_specific``.
    """

    class InterfaceType(proto.Enum):
        r"""Disks interface type.

        Values:
            INTERFACE_TYPE_UNSPECIFIED (0):
                Interface type unknown or unspecified.
            IDE (1):
                IDE interface type.
            SATA (2):
                SATA interface type.
            SAS (3):
                SAS interface type.
            SCSI (4):
                SCSI interface type.
            NVME (5):
                NVME interface type.
            FC (6):
                FC interface type.
            ISCSI (7):
                iSCSI interface type.
        """

        INTERFACE_TYPE_UNSPECIFIED = 0
        IDE = 1
        SATA = 2
        SAS = 3
        SCSI = 4
        NVME = 5
        FC = 6
        ISCSI = 7

    capacity_bytes: int = proto.Field(
        proto.INT64,
        number=1,
    )
    free_bytes: int = proto.Field(
        proto.INT64,
        number=2,
    )
    disk_label: str = proto.Field(
        proto.STRING,
        number=3,
    )
    disk_label_type: str = proto.Field(
        proto.STRING,
        number=4,
    )
    interface_type: InterfaceType = proto.Field(
        proto.ENUM,
        number=5,
        enum=InterfaceType,
    )
    partitions: "DiskPartitionList" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="DiskPartitionList",
    )
    hw_address: str = proto.Field(
        proto.STRING,
        number=7,
    )
    vmware: "VmwareDiskConfig" = proto.Field(
        proto.MESSAGE,
        number=20,
        oneof="platform_specific",
        message="VmwareDiskConfig",
    )


class DiskPartitionList(proto.Message):
    r"""Disk partition list.

    Attributes:
        entries (MutableSequence[google.cloud.migrationcenter_v1.types.DiskPartition]):
            Partition entries.
    """

    entries: MutableSequence["DiskPartition"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DiskPartition",
    )


class DiskPartition(proto.Message):
    r"""Disk Partition details.

    Attributes:
        type_ (str):
            Partition type.
        file_system (str):
            Partition file system.
        mount_point (str):
            Mount pount (Linux/Windows) or drive letter
            (Windows).
        capacity_bytes (int):
            Partition capacity.
        free_bytes (int):
            Partition free space.
        uuid (str):
            Partition UUID.
        sub_partitions (google.cloud.migrationcenter_v1.types.DiskPartitionList):
            Sub-partitions.
    """

    type_: str = proto.Field(
        proto.STRING,
        number=1,
    )
    file_system: str = proto.Field(
        proto.STRING,
        number=2,
    )
    mount_point: str = proto.Field(
        proto.STRING,
        number=3,
    )
    capacity_bytes: int = proto.Field(
        proto.INT64,
        number=4,
    )
    free_bytes: int = proto.Field(
        proto.INT64,
        number=5,
    )
    uuid: str = proto.Field(
        proto.STRING,
        number=6,
    )
    sub_partitions: "DiskPartitionList" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="DiskPartitionList",
    )


class VmwareDiskConfig(proto.Message):
    r"""VMware disk config details.

    Attributes:
        backing_type (google.cloud.migrationcenter_v1.types.VmwareDiskConfig.BackingType):
            VMDK backing type.
        shared (bool):
            Is VMDK shared with other VMs.
        vmdk_mode (google.cloud.migrationcenter_v1.types.VmwareDiskConfig.VmdkMode):
            VMDK disk mode.
        rdm_compatibility (google.cloud.migrationcenter_v1.types.VmwareDiskConfig.RdmCompatibility):
            RDM compatibility mode.
    """

    class BackingType(proto.Enum):
        r"""VMDK backing type possible values.

        Values:
            BACKING_TYPE_UNSPECIFIED (0):
                Default value.
            BACKING_TYPE_FLAT_V1 (1):
                Flat v1.
            BACKING_TYPE_FLAT_V2 (2):
                Flat v2.
            BACKING_TYPE_PMEM (3):
                Persistent memory, also known as Non-Volatile
                Memory (NVM).
            BACKING_TYPE_RDM_V1 (4):
                Raw Disk Memory v1.
            BACKING_TYPE_RDM_V2 (5):
                Raw Disk Memory v2.
            BACKING_TYPE_SESPARSE (6):
                SEsparse is a snapshot format introduced in
                vSphere 5.5 for large disks.
            BACKING_TYPE_SESPARSE_V1 (7):
                SEsparse v1.
            BACKING_TYPE_SESPARSE_V2 (8):
                SEsparse v1.
        """

        BACKING_TYPE_UNSPECIFIED = 0
        BACKING_TYPE_FLAT_V1 = 1
        BACKING_TYPE_FLAT_V2 = 2
        BACKING_TYPE_PMEM = 3
        BACKING_TYPE_RDM_V1 = 4
        BACKING_TYPE_RDM_V2 = 5
        BACKING_TYPE_SESPARSE = 6
        BACKING_TYPE_SESPARSE_V1 = 7
        BACKING_TYPE_SESPARSE_V2 = 8

    class VmdkMode(proto.Enum):
        r"""VMDK disk mode.

        Values:
            VMDK_MODE_UNSPECIFIED (0):
                VMDK disk mode unspecified or unknown.
            DEPENDENT (1):
                Dependent disk mode.
            INDEPENDENT_PERSISTENT (2):
                Independent - Persistent disk mode.
            INDEPENDENT_NONPERSISTENT (3):
                Independent - Nonpersistent disk mode.
        """

        VMDK_MODE_UNSPECIFIED = 0
        DEPENDENT = 1
        INDEPENDENT_PERSISTENT = 2
        INDEPENDENT_NONPERSISTENT = 3

    class RdmCompatibility(proto.Enum):
        r"""RDM compatibility mode.

        Values:
            RDM_COMPATIBILITY_UNSPECIFIED (0):
                Compatibility mode unspecified or unknown.
            PHYSICAL_COMPATIBILITY (1):
                Physical compatibility mode.
            VIRTUAL_COMPATIBILITY (2):
                Virtual compatibility mode.
        """

        RDM_COMPATIBILITY_UNSPECIFIED = 0
        PHYSICAL_COMPATIBILITY = 1
        VIRTUAL_COMPATIBILITY = 2

    backing_type: BackingType = proto.Field(
        proto.ENUM,
        number=1,
        enum=BackingType,
    )
    shared: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    vmdk_mode: VmdkMode = proto.Field(
        proto.ENUM,
        number=3,
        enum=VmdkMode,
    )
    rdm_compatibility: RdmCompatibility = proto.Field(
        proto.ENUM,
        number=4,
        enum=RdmCompatibility,
    )


class GuestOsDetails(proto.Message):
    r"""Information from Guest-level collections.

    Attributes:
        os_name (str):
            The name of the operating system.
        family (google.cloud.migrationcenter_v1.types.OperatingSystemFamily):
            What family the OS belong to, if known.
        version (str):
            The version of the operating system.
        config (google.cloud.migrationcenter_v1.types.GuestConfigDetails):
            OS and app configuration.
        runtime (google.cloud.migrationcenter_v1.types.GuestRuntimeDetails):
            Runtime information.
    """

    os_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    family: "OperatingSystemFamily" = proto.Field(
        proto.ENUM,
        number=2,
        enum="OperatingSystemFamily",
    )
    version: str = proto.Field(
        proto.STRING,
        number=3,
    )
    config: "GuestConfigDetails" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="GuestConfigDetails",
    )
    runtime: "GuestRuntimeDetails" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="GuestRuntimeDetails",
    )


class GuestConfigDetails(proto.Message):
    r"""Guest OS config information.

    Attributes:
        issue (str):
            OS issue (typically /etc/issue in Linux).
        fstab (google.cloud.migrationcenter_v1.types.FstabEntryList):
            Mount list (Linux fstab).
        hosts (google.cloud.migrationcenter_v1.types.HostsEntryList):
            Hosts file (/etc/hosts).
        nfs_exports (google.cloud.migrationcenter_v1.types.NfsExportList):
            NFS exports.
        selinux_mode (google.cloud.migrationcenter_v1.types.GuestConfigDetails.SeLinuxMode):
            Security-Enhanced Linux (SELinux) mode.
    """

    class SeLinuxMode(proto.Enum):
        r"""Security-Enhanced Linux (SELinux) mode.

        Values:
            SE_LINUX_MODE_UNSPECIFIED (0):
                SELinux mode unknown or unspecified.
            SE_LINUX_MODE_DISABLED (1):
                SELinux is disabled.
            SE_LINUX_MODE_PERMISSIVE (2):
                SELinux permissive mode.
            SE_LINUX_MODE_ENFORCING (3):
                SELinux enforcing mode.
        """

        SE_LINUX_MODE_UNSPECIFIED = 0
        SE_LINUX_MODE_DISABLED = 1
        SE_LINUX_MODE_PERMISSIVE = 2
        SE_LINUX_MODE_ENFORCING = 3

    issue: str = proto.Field(
        proto.STRING,
        number=1,
    )
    fstab: "FstabEntryList" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="FstabEntryList",
    )
    hosts: "HostsEntryList" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="HostsEntryList",
    )
    nfs_exports: "NfsExportList" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="NfsExportList",
    )
    selinux_mode: SeLinuxMode = proto.Field(
        proto.ENUM,
        number=5,
        enum=SeLinuxMode,
    )


class FstabEntryList(proto.Message):
    r"""Fstab content.

    Attributes:
        entries (MutableSequence[google.cloud.migrationcenter_v1.types.FstabEntry]):
            Fstab entries.
    """

    entries: MutableSequence["FstabEntry"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="FstabEntry",
    )


class FstabEntry(proto.Message):
    r"""Single fstab entry.

    Attributes:
        spec (str):
            The block special device or remote filesystem
            to be mounted.
        file (str):
            The mount point for the filesystem.
        vfstype (str):
            The type of the filesystem.
        mntops (str):
            Mount options associated with the filesystem.
        freq (int):
            Used by dump to determine which filesystems
            need to be dumped.
        passno (int):
            Used by the fsck(8) program to determine the
            order in which filesystem checks are done at
            reboot time.
    """

    spec: str = proto.Field(
        proto.STRING,
        number=1,
    )
    file: str = proto.Field(
        proto.STRING,
        number=2,
    )
    vfstype: str = proto.Field(
        proto.STRING,
        number=3,
    )
    mntops: str = proto.Field(
        proto.STRING,
        number=4,
    )
    freq: int = proto.Field(
        proto.INT32,
        number=5,
    )
    passno: int = proto.Field(
        proto.INT32,
        number=6,
    )


class HostsEntryList(proto.Message):
    r"""Hosts content.

    Attributes:
        entries (MutableSequence[google.cloud.migrationcenter_v1.types.HostsEntry]):
            Hosts entries.
    """

    entries: MutableSequence["HostsEntry"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="HostsEntry",
    )


class HostsEntry(proto.Message):
    r"""Single /etc/hosts entry.

    Attributes:
        ip (str):
            IP (raw, IPv4/6 agnostic).
        host_names (MutableSequence[str]):
            List of host names / aliases.
    """

    ip: str = proto.Field(
        proto.STRING,
        number=1,
    )
    host_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class NfsExportList(proto.Message):
    r"""NFS exports.

    Attributes:
        entries (MutableSequence[google.cloud.migrationcenter_v1.types.NfsExport]):
            NFS export entries.
    """

    entries: MutableSequence["NfsExport"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="NfsExport",
    )


class NfsExport(proto.Message):
    r"""NFS export.

    Attributes:
        export_directory (str):
            The directory being exported.
        hosts (MutableSequence[str]):
            The hosts or networks to which the export is
            being shared.
    """

    export_directory: str = proto.Field(
        proto.STRING,
        number=1,
    )
    hosts: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class GuestRuntimeDetails(proto.Message):
    r"""Guest OS runtime information.

    Attributes:
        services (google.cloud.migrationcenter_v1.types.RunningServiceList):
            Running background services.
        processes (google.cloud.migrationcenter_v1.types.RunningProcessList):
            Running processes.
        network (google.cloud.migrationcenter_v1.types.RuntimeNetworkInfo):
            Runtime network information (connections,
            ports).
        last_boot_time (google.protobuf.timestamp_pb2.Timestamp):
            Last time the OS was booted.
        domain (str):
            Domain, e.g.
            c.stratozone-development.internal.
        machine_name (str):
            Machine name.
        installed_apps (google.cloud.migrationcenter_v1.types.GuestInstalledApplicationList):
            Installed applications information.
        open_file_list (google.cloud.migrationcenter_v1.types.OpenFileList):
            Open files information.
    """

    services: "RunningServiceList" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="RunningServiceList",
    )
    processes: "RunningProcessList" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="RunningProcessList",
    )
    network: "RuntimeNetworkInfo" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="RuntimeNetworkInfo",
    )
    last_boot_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    domain: str = proto.Field(
        proto.STRING,
        number=5,
    )
    machine_name: str = proto.Field(
        proto.STRING,
        number=6,
    )
    installed_apps: "GuestInstalledApplicationList" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="GuestInstalledApplicationList",
    )
    open_file_list: "OpenFileList" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="OpenFileList",
    )


class RunningServiceList(proto.Message):
    r"""List of running guest OS services.

    Attributes:
        entries (MutableSequence[google.cloud.migrationcenter_v1.types.RunningService]):
            Running service entries.
    """

    entries: MutableSequence["RunningService"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="RunningService",
    )


class RunningService(proto.Message):
    r"""Guest OS running service details.

    Attributes:
        service_name (str):
            Service name.
        state (google.cloud.migrationcenter_v1.types.RunningService.State):
            Service state (OS-agnostic).
        start_mode (google.cloud.migrationcenter_v1.types.RunningService.StartMode):
            Service start mode (OS-agnostic).
        exe_path (str):
            Service binary path.
        cmdline (str):
            Service command line.
        pid (int):
            Service pid.
    """

    class State(proto.Enum):
        r"""Service state (OS-agnostic).

        Values:
            STATE_UNSPECIFIED (0):
                Service state unspecified.
            ACTIVE (1):
                Service is active.
            PAUSED (2):
                Service is paused.
            STOPPED (3):
                Service is stopped.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        PAUSED = 2
        STOPPED = 3

    class StartMode(proto.Enum):
        r"""Service start mode (OS-agnostic).

        Values:
            START_MODE_UNSPECIFIED (0):
                Start mode unspecified.
            BOOT (1):
                The service is a device driver started by the
                system loader.
            SYSTEM (2):
                The service is a device driver started by the
                IOInitSystem function.
            AUTO (3):
                The service is started by the operating
                system, at system start-up
            MANUAL (4):
                The service is started only manually, by a
                user.
            DISABLED (5):
                The service is disabled.
        """

        START_MODE_UNSPECIFIED = 0
        BOOT = 1
        SYSTEM = 2
        AUTO = 3
        MANUAL = 4
        DISABLED = 5

    service_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=2,
        enum=State,
    )
    start_mode: StartMode = proto.Field(
        proto.ENUM,
        number=3,
        enum=StartMode,
    )
    exe_path: str = proto.Field(
        proto.STRING,
        number=4,
    )
    cmdline: str = proto.Field(
        proto.STRING,
        number=5,
    )
    pid: int = proto.Field(
        proto.INT64,
        number=6,
    )


class RunningProcessList(proto.Message):
    r"""List of running guest OS processes.

    Attributes:
        entries (MutableSequence[google.cloud.migrationcenter_v1.types.RunningProcess]):
            Running process entries.
    """

    entries: MutableSequence["RunningProcess"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="RunningProcess",
    )


class RunningProcess(proto.Message):
    r"""Guest OS running process details.

    Attributes:
        pid (int):
            Process ID.
        exe_path (str):
            Process binary path.
        cmdline (str):
            Process full command line.
        user (str):
            User running the process.
        attributes (MutableMapping[str, str]):
            Process extended attributes.
    """

    pid: int = proto.Field(
        proto.INT64,
        number=1,
    )
    exe_path: str = proto.Field(
        proto.STRING,
        number=2,
    )
    cmdline: str = proto.Field(
        proto.STRING,
        number=3,
    )
    user: str = proto.Field(
        proto.STRING,
        number=4,
    )
    attributes: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=100,
    )


class RuntimeNetworkInfo(proto.Message):
    r"""Runtime networking information.

    Attributes:
        scan_time (google.protobuf.timestamp_pb2.Timestamp):
            Time of the last network scan.
        connections (google.cloud.migrationcenter_v1.types.NetworkConnectionList):
            Network connections.
    """

    scan_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    connections: "NetworkConnectionList" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="NetworkConnectionList",
    )


class NetworkConnectionList(proto.Message):
    r"""Network connection list.

    Attributes:
        entries (MutableSequence[google.cloud.migrationcenter_v1.types.NetworkConnection]):
            Network connection entries.
    """

    entries: MutableSequence["NetworkConnection"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="NetworkConnection",
    )


class NetworkConnection(proto.Message):
    r"""

    Attributes:
        protocol (str):
            Connection protocol (e.g. TCP/UDP).
        local_ip_address (str):
            Local IP address.
        local_port (int):
            Local port.
        remote_ip_address (str):
            Remote IP address.
        remote_port (int):
            Remote port.
        state (google.cloud.migrationcenter_v1.types.NetworkConnection.State):
            Network connection state.
        pid (int):
            Process ID.
        process_name (str):
            Process or service name.
    """

    class State(proto.Enum):
        r"""Network connection state.

        Values:
            STATE_UNSPECIFIED (0):
                Connection state is unknown or unspecified.
            OPENING (1):
                The connection is being opened.
            OPEN (2):
                The connection is open.
            LISTEN (3):
                Listening for incoming connections.
            CLOSING (4):
                The connection is being closed.
            CLOSED (5):
                The connection is closed.
        """

        STATE_UNSPECIFIED = 0
        OPENING = 1
        OPEN = 2
        LISTEN = 3
        CLOSING = 4
        CLOSED = 5

    protocol: str = proto.Field(
        proto.STRING,
        number=1,
    )
    local_ip_address: str = proto.Field(
        proto.STRING,
        number=2,
    )
    local_port: int = proto.Field(
        proto.INT32,
        number=3,
    )
    remote_ip_address: str = proto.Field(
        proto.STRING,
        number=4,
    )
    remote_port: int = proto.Field(
        proto.INT32,
        number=5,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=6,
        enum=State,
    )
    pid: int = proto.Field(
        proto.INT64,
        number=7,
    )
    process_name: str = proto.Field(
        proto.STRING,
        number=8,
    )


class GuestInstalledApplicationList(proto.Message):
    r"""Guest installed application list.

    Attributes:
        entries (MutableSequence[google.cloud.migrationcenter_v1.types.GuestInstalledApplication]):
            Application entries.
    """

    entries: MutableSequence["GuestInstalledApplication"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="GuestInstalledApplication",
    )


class GuestInstalledApplication(proto.Message):
    r"""Guest installed application information.

    Attributes:
        application_name (str):
            Installed application name.
        vendor (str):
            Installed application vendor.
        install_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the application was installed.
        path (str):
            Source path.
        version (str):
            Installed application version.
    """

    application_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    vendor: str = proto.Field(
        proto.STRING,
        number=2,
    )
    install_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    path: str = proto.Field(
        proto.STRING,
        number=4,
    )
    version: str = proto.Field(
        proto.STRING,
        number=5,
    )


class OpenFileList(proto.Message):
    r"""Open file list.

    Attributes:
        entries (MutableSequence[google.cloud.migrationcenter_v1.types.OpenFileDetails]):
            Open file details entries.
    """

    entries: MutableSequence["OpenFileDetails"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="OpenFileDetails",
    )


class OpenFileDetails(proto.Message):
    r"""Open file Information.

    Attributes:
        command (str):
            Opened file command.
        user (str):
            Opened file user.
        file_type (str):
            Opened file file type.
        file_path (str):
            Opened file file path.
    """

    command: str = proto.Field(
        proto.STRING,
        number=1,
    )
    user: str = proto.Field(
        proto.STRING,
        number=2,
    )
    file_type: str = proto.Field(
        proto.STRING,
        number=3,
    )
    file_path: str = proto.Field(
        proto.STRING,
        number=4,
    )


class PlatformDetails(proto.Message):
    r"""Information about the platform.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        vmware_details (google.cloud.migrationcenter_v1.types.VmwarePlatformDetails):
            VMware specific details.

            This field is a member of `oneof`_ ``vendor_details``.
        aws_ec2_details (google.cloud.migrationcenter_v1.types.AwsEc2PlatformDetails):
            AWS EC2 specific details.

            This field is a member of `oneof`_ ``vendor_details``.
        azure_vm_details (google.cloud.migrationcenter_v1.types.AzureVmPlatformDetails):
            Azure VM specific details.

            This field is a member of `oneof`_ ``vendor_details``.
        generic_details (google.cloud.migrationcenter_v1.types.GenericPlatformDetails):
            Generic platform details.

            This field is a member of `oneof`_ ``vendor_details``.
        physical_details (google.cloud.migrationcenter_v1.types.PhysicalPlatformDetails):
            Physical machines platform details.

            This field is a member of `oneof`_ ``vendor_details``.
    """

    vmware_details: "VmwarePlatformDetails" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="vendor_details",
        message="VmwarePlatformDetails",
    )
    aws_ec2_details: "AwsEc2PlatformDetails" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="vendor_details",
        message="AwsEc2PlatformDetails",
    )
    azure_vm_details: "AzureVmPlatformDetails" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="vendor_details",
        message="AzureVmPlatformDetails",
    )
    generic_details: "GenericPlatformDetails" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="vendor_details",
        message="GenericPlatformDetails",
    )
    physical_details: "PhysicalPlatformDetails" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="vendor_details",
        message="PhysicalPlatformDetails",
    )


class VmwarePlatformDetails(proto.Message):
    r"""VMware specific details.

    Attributes:
        vcenter_version (str):
            vCenter version.
        esx_version (str):
            ESX version.
        osid (str):
            VMware os enum -
            https://vdc-repo.vmware.com/vmwb-repository/dcr-public/da47f910-60ac-438b-8b9b-6122f4d14524/16b7274a-bf8b-4b4c-a05e-746f2aa93c8c/doc/vim.vm.GuestOsDescriptor.GuestOsIdentifier.html.
        vcenter_folder (str):
            Folder name in vCenter where asset resides.
        vcenter_uri (str):
            vCenter URI used in collection.
        vcenter_vm_id (str):
            vCenter VM ID.
    """

    vcenter_version: str = proto.Field(
        proto.STRING,
        number=1,
    )
    esx_version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    osid: str = proto.Field(
        proto.STRING,
        number=3,
    )
    vcenter_folder: str = proto.Field(
        proto.STRING,
        number=4,
    )
    vcenter_uri: str = proto.Field(
        proto.STRING,
        number=5,
    )
    vcenter_vm_id: str = proto.Field(
        proto.STRING,
        number=6,
    )


class AwsEc2PlatformDetails(proto.Message):
    r"""AWS EC2 specific details.

    Attributes:
        machine_type_label (str):
            AWS platform's machine type label.
        location (str):
            The location of the machine in the AWS
            format.
    """

    machine_type_label: str = proto.Field(
        proto.STRING,
        number=1,
    )
    location: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AzureVmPlatformDetails(proto.Message):
    r"""Azure VM specific details.

    Attributes:
        machine_type_label (str):
            Azure platform's machine type label.
        location (str):
            The location of the machine in the Azure
            format.
        provisioning_state (str):
            Azure platform's provisioning state.
    """

    machine_type_label: str = proto.Field(
        proto.STRING,
        number=1,
    )
    location: str = proto.Field(
        proto.STRING,
        number=2,
    )
    provisioning_state: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GenericPlatformDetails(proto.Message):
    r"""Generic platform details.

    Attributes:
        location (str):
            Free text representation of the machine
            location. The format of this field should not be
            relied on. Different VMs in the same location
            may have different string values for this field.
    """

    location: str = proto.Field(
        proto.STRING,
        number=1,
    )


class PhysicalPlatformDetails(proto.Message):
    r"""Platform specific details for Physical Machines.

    Attributes:
        location (str):
            Free text representation of the machine
            location. The format of this field should not be
            relied on. Different machines in the same
            location may have different string values for
            this field.
    """

    location: str = proto.Field(
        proto.STRING,
        number=1,
    )


class MemoryUsageSample(proto.Message):
    r"""Memory usage sample.

    Attributes:
        utilized_percentage (float):
            Percentage of system memory utilized. Must be in the
            interval [0, 100].
    """

    utilized_percentage: float = proto.Field(
        proto.FLOAT,
        number=1,
    )


class CpuUsageSample(proto.Message):
    r"""CPU usage sample.

    Attributes:
        utilized_percentage (float):
            Percentage of total CPU capacity utilized. Must be in the
            interval [0, 100]. On most systems can be calculated using
            100 - idle percentage.
    """

    utilized_percentage: float = proto.Field(
        proto.FLOAT,
        number=1,
    )


class NetworkUsageSample(proto.Message):
    r"""Network usage sample. Values are across all network
    interfaces.

    Attributes:
        average_ingress_bps (float):
            Average network ingress in B/s sampled over a
            short window. Must be non-negative.
        average_egress_bps (float):
            Average network egress in B/s sampled over a
            short window. Must be non-negative.
    """

    average_ingress_bps: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    average_egress_bps: float = proto.Field(
        proto.FLOAT,
        number=2,
    )


class DiskUsageSample(proto.Message):
    r"""Disk usage sample. Values are across all disks.

    Attributes:
        average_iops (float):
            Average IOPS sampled over a short window.
            Must be non-negative.
    """

    average_iops: float = proto.Field(
        proto.FLOAT,
        number=1,
    )


class PerformanceSample(proto.Message):
    r"""Performance data sample.

    Attributes:
        sample_time (google.protobuf.timestamp_pb2.Timestamp):
            Time the sample was collected.
            If omitted, the frame report time will be used.
        memory (google.cloud.migrationcenter_v1.types.MemoryUsageSample):
            Memory usage sample.
        cpu (google.cloud.migrationcenter_v1.types.CpuUsageSample):
            CPU usage sample.
        network (google.cloud.migrationcenter_v1.types.NetworkUsageSample):
            Network usage sample.
        disk (google.cloud.migrationcenter_v1.types.DiskUsageSample):
            Disk usage sample.
    """

    sample_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    memory: "MemoryUsageSample" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="MemoryUsageSample",
    )
    cpu: "CpuUsageSample" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="CpuUsageSample",
    )
    network: "NetworkUsageSample" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="NetworkUsageSample",
    )
    disk: "DiskUsageSample" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="DiskUsageSample",
    )


class AssetPerformanceData(proto.Message):
    r"""Performance data for an asset.

    Attributes:
        daily_resource_usage_aggregations (MutableSequence[google.cloud.migrationcenter_v1.types.DailyResourceUsageAggregation]):
            Daily resource usage aggregations.
            Contains all of the data available for an asset,
            up to the last 420 days. Aggregations are sorted
            from oldest to most recent.
    """

    daily_resource_usage_aggregations: MutableSequence[
        "DailyResourceUsageAggregation"
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DailyResourceUsageAggregation",
    )


class DailyResourceUsageAggregation(proto.Message):
    r"""Usage data aggregation for a single day.

    Attributes:
        date (google.type.date_pb2.Date):
            Aggregation date. Day boundaries are at
            midnight UTC.
        cpu (google.cloud.migrationcenter_v1.types.DailyResourceUsageAggregation.CPU):
            CPU usage.
        memory (google.cloud.migrationcenter_v1.types.DailyResourceUsageAggregation.Memory):
            Memory usage.
        network (google.cloud.migrationcenter_v1.types.DailyResourceUsageAggregation.Network):
            Network usage.
        disk (google.cloud.migrationcenter_v1.types.DailyResourceUsageAggregation.Disk):
            Disk usage.
    """

    class Stats(proto.Message):
        r"""Statistical aggregation of samples for a single resource
        usage.

        Attributes:
            average (float):
                Average usage value.
            median (float):
                Median usage value.
            nintey_fifth_percentile (float):
                95th percentile usage value.
            peak (float):
                Peak usage value.
        """

        average: float = proto.Field(
            proto.FLOAT,
            number=1,
        )
        median: float = proto.Field(
            proto.FLOAT,
            number=2,
        )
        nintey_fifth_percentile: float = proto.Field(
            proto.FLOAT,
            number=3,
        )
        peak: float = proto.Field(
            proto.FLOAT,
            number=4,
        )

    class CPU(proto.Message):
        r"""Statistical aggregation of CPU usage.

        Attributes:
            utilization_percentage (google.cloud.migrationcenter_v1.types.DailyResourceUsageAggregation.Stats):
                CPU utilization percentage.
        """

        utilization_percentage: "DailyResourceUsageAggregation.Stats" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="DailyResourceUsageAggregation.Stats",
        )

    class Memory(proto.Message):
        r"""Statistical aggregation of memory usage.

        Attributes:
            utilization_percentage (google.cloud.migrationcenter_v1.types.DailyResourceUsageAggregation.Stats):
                Memory utilization percentage.
        """

        utilization_percentage: "DailyResourceUsageAggregation.Stats" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="DailyResourceUsageAggregation.Stats",
        )

    class Network(proto.Message):
        r"""Statistical aggregation of network usage.

        Attributes:
            ingress_bps (google.cloud.migrationcenter_v1.types.DailyResourceUsageAggregation.Stats):
                Network ingress in B/s.
            egress_bps (google.cloud.migrationcenter_v1.types.DailyResourceUsageAggregation.Stats):
                Network egress in B/s.
        """

        ingress_bps: "DailyResourceUsageAggregation.Stats" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="DailyResourceUsageAggregation.Stats",
        )
        egress_bps: "DailyResourceUsageAggregation.Stats" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="DailyResourceUsageAggregation.Stats",
        )

    class Disk(proto.Message):
        r"""Statistical aggregation of disk usage.

        Attributes:
            iops (google.cloud.migrationcenter_v1.types.DailyResourceUsageAggregation.Stats):
                Disk I/O operations per second.
        """

        iops: "DailyResourceUsageAggregation.Stats" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="DailyResourceUsageAggregation.Stats",
        )

    date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=1,
        message=date_pb2.Date,
    )
    cpu: CPU = proto.Field(
        proto.MESSAGE,
        number=2,
        message=CPU,
    )
    memory: Memory = proto.Field(
        proto.MESSAGE,
        number=3,
        message=Memory,
    )
    network: Network = proto.Field(
        proto.MESSAGE,
        number=4,
        message=Network,
    )
    disk: Disk = proto.Field(
        proto.MESSAGE,
        number=5,
        message=Disk,
    )


class InsightList(proto.Message):
    r"""Message containing insights list.

    Attributes:
        insights (MutableSequence[google.cloud.migrationcenter_v1.types.Insight]):
            Output only. Insights of the list.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Update timestamp.
    """

    insights: MutableSequence["Insight"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Insight",
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


class Insight(proto.Message):
    r"""An insight about an asset.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        migration_insight (google.cloud.migrationcenter_v1.types.MigrationInsight):
            Output only. An insight about potential
            migrations for an asset.

            This field is a member of `oneof`_ ``insight``.
        generic_insight (google.cloud.migrationcenter_v1.types.GenericInsight):
            Output only. A generic insight about an asset

            This field is a member of `oneof`_ ``insight``.
    """

    migration_insight: "MigrationInsight" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="insight",
        message="MigrationInsight",
    )
    generic_insight: "GenericInsight" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="insight",
        message="GenericInsight",
    )


class GenericInsight(proto.Message):
    r"""A generic insight about an asset.

    Attributes:
        message_id (int):
            Output only. Represents a globally unique message id for
            this insight, can be used for localization purposes, in case
            message_code is not yet known by the client use
            default_message instead.
        default_message (str):
            Output only. In case message_code is not yet known by the
            client default_message will be the message to be used
            instead.
        additional_information (MutableSequence[str]):
            Output only. Additional information about the
            insight, each entry can be a logical entry and
            must make sense if it is displayed with line
            breaks between each entry. Text can contain md
            style links.
    """

    message_id: int = proto.Field(
        proto.INT64,
        number=1,
    )
    default_message: str = proto.Field(
        proto.STRING,
        number=2,
    )
    additional_information: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class MigrationInsight(proto.Message):
    r"""An insight about potential migrations for an asset.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        fit (google.cloud.migrationcenter_v1.types.FitDescriptor):
            Output only. Description of how well the
            asset this insight is associated with fits the
            proposed migration.
        compute_engine_target (google.cloud.migrationcenter_v1.types.ComputeEngineMigrationTarget):
            Output only. A Google Compute Engine target.

            This field is a member of `oneof`_ ``migration_target``.
    """

    fit: "FitDescriptor" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="FitDescriptor",
    )
    compute_engine_target: "ComputeEngineMigrationTarget" = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="migration_target",
        message="ComputeEngineMigrationTarget",
    )


class ComputeEngineMigrationTarget(proto.Message):
    r"""Compute engine migration target.

    Attributes:
        shape (google.cloud.migrationcenter_v1.types.ComputeEngineShapeDescriptor):
            Description of the suggested shape for the
            migration target.
    """

    shape: "ComputeEngineShapeDescriptor" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ComputeEngineShapeDescriptor",
    )


class ComputeEngineShapeDescriptor(proto.Message):
    r"""Compute Engine target shape descriptor.

    Attributes:
        memory_mb (int):
            Memory in mebibytes.
        physical_core_count (int):
            Number of physical cores.
        logical_core_count (int):
            Number of logical cores.
        series (str):
            Compute Engine machine series.
        machine_type (str):
            Compute Engine machine type.
        storage (MutableSequence[google.cloud.migrationcenter_v1.types.ComputeStorageDescriptor]):
            Compute Engine storage. Never empty.
    """

    memory_mb: int = proto.Field(
        proto.INT32,
        number=1,
    )
    physical_core_count: int = proto.Field(
        proto.INT32,
        number=2,
    )
    logical_core_count: int = proto.Field(
        proto.INT32,
        number=3,
    )
    series: str = proto.Field(
        proto.STRING,
        number=4,
    )
    machine_type: str = proto.Field(
        proto.STRING,
        number=5,
    )
    storage: MutableSequence["ComputeStorageDescriptor"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="ComputeStorageDescriptor",
    )


class ComputeStorageDescriptor(proto.Message):
    r"""Compute Engine storage option descriptor.

    Attributes:
        type_ (google.cloud.migrationcenter_v1.types.PersistentDiskType):
            Disk type backing the storage.
        size_gb (int):
            Disk size in GiB.
    """

    type_: "PersistentDiskType" = proto.Field(
        proto.ENUM,
        number=1,
        enum="PersistentDiskType",
    )
    size_gb: int = proto.Field(
        proto.INT32,
        number=2,
    )


class FitDescriptor(proto.Message):
    r"""Describes the fit level of an asset for migration to a
    specific target.

    Attributes:
        fit_level (google.cloud.migrationcenter_v1.types.FitDescriptor.FitLevel):
            Fit level.
    """

    class FitLevel(proto.Enum):
        r"""Fit level.

        Values:
            FIT_LEVEL_UNSPECIFIED (0):
                Not enough information.
            FIT (1):
                Fit.
            NO_FIT (2):
                No Fit.
            REQUIRES_EFFORT (3):
                Fit with effort.
        """

        FIT_LEVEL_UNSPECIFIED = 0
        FIT = 1
        NO_FIT = 2
        REQUIRES_EFFORT = 3

    fit_level: FitLevel = proto.Field(
        proto.ENUM,
        number=1,
        enum=FitLevel,
    )


class Aggregation(proto.Message):
    r"""Message describing an aggregation. The message includes the
    aggregation type, parameters, and the field on which to perform
    the aggregation.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        field (str):
            The name of the field on which to aggregate.
        count (google.cloud.migrationcenter_v1.types.Aggregation.Count):
            Count the number of matching objects.

            This field is a member of `oneof`_ ``aggregation_function``.
        sum (google.cloud.migrationcenter_v1.types.Aggregation.Sum):
            Sum over a numeric field.

            This field is a member of `oneof`_ ``aggregation_function``.
        histogram (google.cloud.migrationcenter_v1.types.Aggregation.Histogram):
            Creates a bucketed histogram of field values.

            This field is a member of `oneof`_ ``aggregation_function``.
        frequency (google.cloud.migrationcenter_v1.types.Aggregation.Frequency):
            Creates a frequency distribution of all field
            values.

            This field is a member of `oneof`_ ``aggregation_function``.
    """

    class Count(proto.Message):
        r"""Object count."""

    class Sum(proto.Message):
        r"""Sum of field values."""

    class Histogram(proto.Message):
        r"""Histogram of bucketed assets counts by field value.

        Attributes:
            lower_bounds (MutableSequence[float]):
                Lower bounds of buckets. The response will contain ``n+1``
                buckets for ``n`` bounds. The first bucket will count all
                assets for which the field value is smaller than the first
                bound. Subsequent buckets will count assets for which the
                field value is greater or equal to a lower bound and smaller
                than the next one. The last bucket will count assets for
                which the field value is greater or equal to the final lower
                bound. You can define up to 20 lower bounds.
        """

        lower_bounds: MutableSequence[float] = proto.RepeatedField(
            proto.DOUBLE,
            number=1,
        )

    class Frequency(proto.Message):
        r"""Frequency distribution of all field values."""

    field: str = proto.Field(
        proto.STRING,
        number=1,
    )
    count: Count = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="aggregation_function",
        message=Count,
    )
    sum: Sum = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="aggregation_function",
        message=Sum,
    )
    histogram: Histogram = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="aggregation_function",
        message=Histogram,
    )
    frequency: Frequency = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="aggregation_function",
        message=Frequency,
    )


class AggregationResult(proto.Message):
    r"""Message describing a result of an aggregation.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        field (str):

        count (google.cloud.migrationcenter_v1.types.AggregationResult.Count):

            This field is a member of `oneof`_ ``result``.
        sum (google.cloud.migrationcenter_v1.types.AggregationResult.Sum):

            This field is a member of `oneof`_ ``result``.
        histogram (google.cloud.migrationcenter_v1.types.AggregationResult.Histogram):

            This field is a member of `oneof`_ ``result``.
        frequency (google.cloud.migrationcenter_v1.types.AggregationResult.Frequency):

            This field is a member of `oneof`_ ``result``.
    """

    class Count(proto.Message):
        r"""The result of a count aggregation.

        Attributes:
            value (int):

        """

        value: int = proto.Field(
            proto.INT64,
            number=1,
        )

    class Sum(proto.Message):
        r"""The result of a sum aggregation.

        Attributes:
            value (float):

        """

        value: float = proto.Field(
            proto.DOUBLE,
            number=1,
        )

    class Histogram(proto.Message):
        r"""The result of a bucketed histogram aggregation.

        Attributes:
            buckets (MutableSequence[google.cloud.migrationcenter_v1.types.AggregationResult.Histogram.Bucket]):
                Buckets in the histogram. There will be ``n+1`` buckets
                matching ``n`` lower bounds in the request. The first bucket
                will be from -infinity to the first bound. Subsequent
                buckets will be between one bound and the next. The final
                bucket will be from the final bound to infinity.
        """

        class Bucket(proto.Message):
            r"""A histogram bucket with a lower and upper bound, and a count
            of items with a field value between those bounds.
            The lower bound is inclusive and the upper bound is exclusive.
            Lower bound may be -infinity and upper bound may be infinity.

            Attributes:
                lower_bound (float):
                    Lower bound - inclusive.
                upper_bound (float):
                    Upper bound - exclusive.
                count (int):
                    Count of items in the bucket.
            """

            lower_bound: float = proto.Field(
                proto.DOUBLE,
                number=1,
            )
            upper_bound: float = proto.Field(
                proto.DOUBLE,
                number=2,
            )
            count: int = proto.Field(
                proto.INT64,
                number=3,
            )

        buckets: MutableSequence["AggregationResult.Histogram.Bucket"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message="AggregationResult.Histogram.Bucket",
            )
        )

    class Frequency(proto.Message):
        r"""The result of a frequency distribution aggregation.

        Attributes:
            values (MutableMapping[str, int]):

        """

        values: MutableMapping[str, int] = proto.MapField(
            proto.STRING,
            proto.INT64,
            number=1,
        )

    field: str = proto.Field(
        proto.STRING,
        number=1,
    )
    count: Count = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="result",
        message=Count,
    )
    sum: Sum = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="result",
        message=Sum,
    )
    histogram: Histogram = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="result",
        message=Histogram,
    )
    frequency: Frequency = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="result",
        message=Frequency,
    )


class FileValidationReport(proto.Message):
    r"""A resource that aggregates the validation errors found in an
    import job file.

    Attributes:
        file_name (str):
            The name of the file.
        row_errors (MutableSequence[google.cloud.migrationcenter_v1.types.ImportRowError]):
            Partial list of rows that encountered
            validation error.
        partial_report (bool):
            Flag indicating that processing was aborted
            due to maximum number of errors.
        file_errors (MutableSequence[google.cloud.migrationcenter_v1.types.ImportError]):
            List of file level errors.
    """

    file_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    row_errors: MutableSequence["ImportRowError"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="ImportRowError",
    )
    partial_report: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    file_errors: MutableSequence["ImportError"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="ImportError",
    )


class ValidationReport(proto.Message):
    r"""A resource that aggregates errors across import job files.

    Attributes:
        file_validations (MutableSequence[google.cloud.migrationcenter_v1.types.FileValidationReport]):
            List of errors found in files.
        job_errors (MutableSequence[google.cloud.migrationcenter_v1.types.ImportError]):
            List of job level errors.
    """

    file_validations: MutableSequence["FileValidationReport"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="FileValidationReport",
    )
    job_errors: MutableSequence["ImportError"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="ImportError",
    )


class ExecutionReport(proto.Message):
    r"""A resource that reports result of the import job execution.

    Attributes:
        frames_reported (int):
            Total number of asset frames reported for the
            import job.
        execution_errors (google.cloud.migrationcenter_v1.types.ValidationReport):
            Validation errors encountered during the
            execution of the import job.
        total_rows_count (int):
            Output only. Total number of rows in the
            import job.
    """

    frames_reported: int = proto.Field(
        proto.INT32,
        number=1,
    )
    execution_errors: "ValidationReport" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ValidationReport",
    )
    total_rows_count: int = proto.Field(
        proto.INT32,
        number=3,
    )


class ImportError(proto.Message):
    r"""A resource that reports the errors encountered while
    processing an import job.

    Attributes:
        error_details (str):
            The error information.
        severity (google.cloud.migrationcenter_v1.types.ImportError.Severity):
            The severity of the error.
    """

    class Severity(proto.Enum):
        r"""Enumerate possible error severity.

        Values:
            SEVERITY_UNSPECIFIED (0):
                No description available.
            ERROR (1):
                No description available.
            WARNING (2):
                No description available.
            INFO (3):
                No description available.
        """

        SEVERITY_UNSPECIFIED = 0
        ERROR = 1
        WARNING = 2
        INFO = 3

    error_details: str = proto.Field(
        proto.STRING,
        number=1,
    )
    severity: Severity = proto.Field(
        proto.ENUM,
        number=2,
        enum=Severity,
    )


class ImportRowError(proto.Message):
    r"""A resource that reports the import job errors at row level.

    Attributes:
        row_number (int):
            The row number where the error was detected.
        vm_name (str):
            The name of the VM in the row.
        vm_uuid (str):
            The VM UUID.
        errors (MutableSequence[google.cloud.migrationcenter_v1.types.ImportError]):
            The list of errors detected in the row.
    """

    row_number: int = proto.Field(
        proto.INT32,
        number=1,
    )
    vm_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    vm_uuid: str = proto.Field(
        proto.STRING,
        number=3,
    )
    errors: MutableSequence["ImportError"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="ImportError",
    )


class UploadFileInfo(proto.Message):
    r"""A resource that contains a URI to which a data file can be
    uploaded.

    Attributes:
        signed_uri (str):
            Output only. Upload URI for the file.
        headers (MutableMapping[str, str]):
            Output only. The headers that were used to
            sign the URI.
        uri_expiration_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Expiration time of the upload
            URI.
    """

    signed_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    headers: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )
    uri_expiration_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


class AssetList(proto.Message):
    r"""Lists the asset IDs of all assets.

    Attributes:
        asset_ids (MutableSequence[str]):
            Required. A list of asset IDs
    """

    asset_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class FrameViolationEntry(proto.Message):
    r"""A resource that contains a single violation of a reported
    ``AssetFrame`` resource.

    Attributes:
        field (str):
            The field of the original frame where the
            violation occurred.
        violation (str):
            A message describing the violation.
    """

    field: str = proto.Field(
        proto.STRING,
        number=1,
    )
    violation: str = proto.Field(
        proto.STRING,
        number=2,
    )


class VirtualMachinePreferences(proto.Message):
    r"""VirtualMachinePreferences enables you to create sets of
    assumptions, for example, a geographical location and pricing
    track, for your migrated virtual machines. The set of
    preferences influence recommendations for migrating virtual
    machine assets.

    Attributes:
        target_product (google.cloud.migrationcenter_v1.types.ComputeMigrationTargetProduct):
            Target product for assets using this
            preference set. Specify either target product or
            business goal, but not both.
        region_preferences (google.cloud.migrationcenter_v1.types.RegionPreferences):
            Region preferences for assets using this
            preference set. If you are unsure which value to
            set, the migration service API region is often a
            good value to start with.
        commitment_plan (google.cloud.migrationcenter_v1.types.CommitmentPlan):
            Commitment plan to consider when calculating
            costs for virtual machine insights and
            recommendations. If you are unsure which value
            to set, a 3 year commitment plan is often a good
            value to start with.
        sizing_optimization_strategy (google.cloud.migrationcenter_v1.types.SizingOptimizationStrategy):
            Sizing optimization strategy specifies the
            preferred strategy used when extrapolating usage
            data to calculate insights and recommendations
            for a virtual machine.
            If you are unsure which value to set, a moderate
            sizing optimization strategy is often a good
            value to start with.
        compute_engine_preferences (google.cloud.migrationcenter_v1.types.ComputeEnginePreferences):
            Compute Engine preferences concern insights
            and recommendations for Compute Engine target.
        vmware_engine_preferences (google.cloud.migrationcenter_v1.types.VmwareEnginePreferences):
            Preferences concerning insights and
            recommendations for Google Cloud VMware Engine.
        sole_tenancy_preferences (google.cloud.migrationcenter_v1.types.SoleTenancyPreferences):
            Preferences concerning Sole Tenant nodes and
            virtual machines.
    """

    target_product: "ComputeMigrationTargetProduct" = proto.Field(
        proto.ENUM,
        number=2,
        enum="ComputeMigrationTargetProduct",
    )
    region_preferences: "RegionPreferences" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="RegionPreferences",
    )
    commitment_plan: "CommitmentPlan" = proto.Field(
        proto.ENUM,
        number=4,
        enum="CommitmentPlan",
    )
    sizing_optimization_strategy: "SizingOptimizationStrategy" = proto.Field(
        proto.ENUM,
        number=5,
        enum="SizingOptimizationStrategy",
    )
    compute_engine_preferences: "ComputeEnginePreferences" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="ComputeEnginePreferences",
    )
    vmware_engine_preferences: "VmwareEnginePreferences" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="VmwareEnginePreferences",
    )
    sole_tenancy_preferences: "SoleTenancyPreferences" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="SoleTenancyPreferences",
    )


class ComputeEnginePreferences(proto.Message):
    r"""The user preferences relating to Compute Engine target
    platform.

    Attributes:
        machine_preferences (google.cloud.migrationcenter_v1.types.MachinePreferences):
            Preferences concerning the machine types to
            consider on Compute Engine.
        license_type (google.cloud.migrationcenter_v1.types.LicenseType):
            License type to consider when calculating
            costs for virtual machine insights and
            recommendations. If unspecified, costs are
            calculated based on the default licensing plan.
    """

    machine_preferences: "MachinePreferences" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="MachinePreferences",
    )
    license_type: "LicenseType" = proto.Field(
        proto.ENUM,
        number=3,
        enum="LicenseType",
    )


class MachinePreferences(proto.Message):
    r"""The type of machines to consider when calculating virtual
    machine migration insights and recommendations.
    Not all machine types are available in all zones and regions.

    Attributes:
        allowed_machine_series (MutableSequence[google.cloud.migrationcenter_v1.types.MachineSeries]):
            Compute Engine machine series to consider for
            insights and recommendations. If empty, no
            restriction is applied on the machine series.
    """

    allowed_machine_series: MutableSequence["MachineSeries"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="MachineSeries",
    )


class MachineSeries(proto.Message):
    r"""A Compute Engine machine series.

    Attributes:
        code (str):
            Code to identify a Compute Engine machine series. Consult
            https://cloud.google.com/compute/docs/machine-resource#machine_type_comparison
            for more details on the available series.
    """

    code: str = proto.Field(
        proto.STRING,
        number=1,
    )


class VmwareEnginePreferences(proto.Message):
    r"""The user preferences relating to Google Cloud VMware Engine
    target platform.

    Attributes:
        cpu_overcommit_ratio (float):
            CPU overcommit ratio.
            Acceptable values are between 1.0 and 8.0, with
            0.1 increment.
        memory_overcommit_ratio (float):
            Memory overcommit ratio.
            Acceptable values are 1.0, 1.25, 1.5, 1.75 and
            2.0.
        storage_deduplication_compression_ratio (float):
            The Deduplication and Compression ratio is
            based on the logical (Used Before) space
            required to store data before applying
            deduplication and compression, in relation to
            the physical (Used After) space required after
            applying deduplication and compression.
            Specifically, the ratio is the Used Before space
            divided by the Used After space. For example, if
            the Used Before space is 3 GB, but the physical
            Used After space is 1 GB, the deduplication and
            compression ratio is 3x. Acceptable values are
            between 1.0 and 4.0.
        commitment_plan (google.cloud.migrationcenter_v1.types.VmwareEnginePreferences.CommitmentPlan):
            Commitment plan to consider when calculating
            costs for virtual machine insights and
            recommendations. If you are unsure which value
            to set, a 3 year commitment plan is often a good
            value to start with.
    """

    class CommitmentPlan(proto.Enum):
        r"""Type of committed use discount.

        Values:
            COMMITMENT_PLAN_UNSPECIFIED (0):
                Unspecified commitment plan.
            ON_DEMAND (1):
                No commitment plan (on-demand usage).
            COMMITMENT_1_YEAR_MONTHLY_PAYMENTS (2):
                1 year commitment (monthly payments).
            COMMITMENT_3_YEAR_MONTHLY_PAYMENTS (3):
                3 year commitment (monthly payments).
            COMMITMENT_1_YEAR_UPFRONT_PAYMENT (4):
                1 year commitment (upfront payment).
            COMMITMENT_3_YEAR_UPFRONT_PAYMENT (5):
                3 years commitment (upfront payment).
        """

        COMMITMENT_PLAN_UNSPECIFIED = 0
        ON_DEMAND = 1
        COMMITMENT_1_YEAR_MONTHLY_PAYMENTS = 2
        COMMITMENT_3_YEAR_MONTHLY_PAYMENTS = 3
        COMMITMENT_1_YEAR_UPFRONT_PAYMENT = 4
        COMMITMENT_3_YEAR_UPFRONT_PAYMENT = 5

    cpu_overcommit_ratio: float = proto.Field(
        proto.DOUBLE,
        number=1,
    )
    memory_overcommit_ratio: float = proto.Field(
        proto.DOUBLE,
        number=2,
    )
    storage_deduplication_compression_ratio: float = proto.Field(
        proto.DOUBLE,
        number=3,
    )
    commitment_plan: CommitmentPlan = proto.Field(
        proto.ENUM,
        number=4,
        enum=CommitmentPlan,
    )


class SoleTenancyPreferences(proto.Message):
    r"""Preferences concerning Sole Tenancy nodes and VMs.

    Attributes:
        cpu_overcommit_ratio (float):
            CPU overcommit ratio.
            Acceptable values are between 1.0 and 2.0
            inclusive.
        host_maintenance_policy (google.cloud.migrationcenter_v1.types.SoleTenancyPreferences.HostMaintenancePolicy):
            Sole Tenancy nodes maintenance policy.
        commitment_plan (google.cloud.migrationcenter_v1.types.SoleTenancyPreferences.CommitmentPlan):
            Commitment plan to consider when calculating
            costs for virtual machine insights and
            recommendations. If you are unsure which value
            to set, a 3 year commitment plan is often a good
            value to start with.
        node_types (MutableSequence[google.cloud.migrationcenter_v1.types.SoleTenantNodeType]):
            A list of sole tenant node types.
            An empty list means that all possible node types
            will be considered.
    """

    class HostMaintenancePolicy(proto.Enum):
        r"""Sole Tenancy nodes maintenance policy.

        Values:
            HOST_MAINTENANCE_POLICY_UNSPECIFIED (0):
                Unspecified host maintenance policy.
            HOST_MAINTENANCE_POLICY_DEFAULT (1):
                Default host maintenance policy.
            HOST_MAINTENANCE_POLICY_RESTART_IN_PLACE (2):
                Restart in place host maintenance policy.
            HOST_MAINTENANCE_POLICY_MIGRATE_WITHIN_NODE_GROUP (3):
                Migrate within node group host maintenance
                policy.
        """

        HOST_MAINTENANCE_POLICY_UNSPECIFIED = 0
        HOST_MAINTENANCE_POLICY_DEFAULT = 1
        HOST_MAINTENANCE_POLICY_RESTART_IN_PLACE = 2
        HOST_MAINTENANCE_POLICY_MIGRATE_WITHIN_NODE_GROUP = 3

    class CommitmentPlan(proto.Enum):
        r"""Type of committed use discount.

        Values:
            COMMITMENT_PLAN_UNSPECIFIED (0):
                Unspecified commitment plan.
            ON_DEMAND (1):
                No commitment plan (on-demand usage).
            COMMITMENT_1_YEAR (2):
                1 year commitment.
            COMMITMENT_3_YEAR (3):
                3 years commitment.
        """

        COMMITMENT_PLAN_UNSPECIFIED = 0
        ON_DEMAND = 1
        COMMITMENT_1_YEAR = 2
        COMMITMENT_3_YEAR = 3

    cpu_overcommit_ratio: float = proto.Field(
        proto.DOUBLE,
        number=1,
    )
    host_maintenance_policy: HostMaintenancePolicy = proto.Field(
        proto.ENUM,
        number=2,
        enum=HostMaintenancePolicy,
    )
    commitment_plan: CommitmentPlan = proto.Field(
        proto.ENUM,
        number=3,
        enum=CommitmentPlan,
    )
    node_types: MutableSequence["SoleTenantNodeType"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="SoleTenantNodeType",
    )


class SoleTenantNodeType(proto.Message):
    r"""A Sole Tenant node type.

    Attributes:
        node_name (str):
            Name of the Sole Tenant node. Consult
            https://cloud.google.com/compute/docs/nodes/sole-tenant-nodes
    """

    node_name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class RegionPreferences(proto.Message):
    r"""The user preferences relating to target regions.

    Attributes:
        preferred_regions (MutableSequence[str]):
            A list of preferred regions,
            ordered by the most preferred region first.
            Set only valid Google Cloud region names.
            See
            https://cloud.google.com/compute/docs/regions-zones
            for available regions.
    """

    preferred_regions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class Settings(proto.Message):
    r"""Describes the Migration Center settings related to the
    project.

    Attributes:
        name (str):
            Output only. The name of the resource.
        preference_set (str):
            The preference set used by default for a
            project.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    preference_set: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ReportSummary(proto.Message):
    r"""Describes the Summary view of a Report, which contains
    aggregated values for all the groups and preference sets
    included in this Report.

    Attributes:
        all_assets_stats (google.cloud.migrationcenter_v1.types.ReportSummary.AssetAggregateStats):
            Aggregate statistics for all the assets
            across all the groups.
        group_findings (MutableSequence[google.cloud.migrationcenter_v1.types.ReportSummary.GroupFinding]):
            Findings for each Group included in this
            report.
    """

    class ChartData(proto.Message):
        r"""Describes a collection of data points rendered as a Chart.

        Attributes:
            data_points (MutableSequence[google.cloud.migrationcenter_v1.types.ReportSummary.ChartData.DataPoint]):
                Each data point in the chart is represented
                as a name-value pair with the name being the
                x-axis label, and the value being the y-axis
                value.
        """

        class DataPoint(proto.Message):
            r"""Describes a single data point in the Chart.

            Attributes:
                label (str):
                    The X-axis label for this data point.
                value (float):
                    The Y-axis value for this data point.
            """

            label: str = proto.Field(
                proto.STRING,
                number=1,
            )
            value: float = proto.Field(
                proto.DOUBLE,
                number=2,
            )

        data_points: MutableSequence["ReportSummary.ChartData.DataPoint"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message="ReportSummary.ChartData.DataPoint",
            )
        )

    class UtilizationChartData(proto.Message):
        r"""Utilization Chart is a specific type of visualization which
        displays a metric classified into "Used" and "Free" buckets.

        Attributes:
            used (int):
                Aggregate value which falls into the "Used"
                bucket.
            free (int):
                Aggregate value which falls into the "Free"
                bucket.
        """

        used: int = proto.Field(
            proto.INT64,
            number=1,
        )
        free: int = proto.Field(
            proto.INT64,
            number=2,
        )

    class HistogramChartData(proto.Message):
        r"""A Histogram Chart shows a distribution of values into
        buckets, showing a count of values which fall into a bucket.

        Attributes:
            buckets (MutableSequence[google.cloud.migrationcenter_v1.types.ReportSummary.HistogramChartData.Bucket]):
                Buckets in the histogram. There will be ``n+1`` buckets
                matching ``n`` lower bounds in the request. The first bucket
                will be from -infinity to the first bound. Subsequent
                buckets will be between one bound and the next. The final
                bucket will be from the final bound to infinity.
        """

        class Bucket(proto.Message):
            r"""A histogram bucket with a lower and upper bound, and a count
            of items with a field value between those bounds.
            The lower bound is inclusive and the upper bound is exclusive.
            Lower bound may be -infinity and upper bound may be infinity.

            Attributes:
                lower_bound (int):
                    Lower bound - inclusive.
                upper_bound (int):
                    Upper bound - exclusive.
                count (int):
                    Count of items in the bucket.
            """

            lower_bound: int = proto.Field(
                proto.INT64,
                number=1,
            )
            upper_bound: int = proto.Field(
                proto.INT64,
                number=2,
            )
            count: int = proto.Field(
                proto.INT64,
                number=3,
            )

        buckets: MutableSequence["ReportSummary.HistogramChartData.Bucket"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message="ReportSummary.HistogramChartData.Bucket",
            )
        )

    class AssetAggregateStats(proto.Message):
        r"""Aggregate statistics for a collection of assets.

        Attributes:
            total_memory_bytes (int):
                Sum of the memory in bytes of all the assets
                in this collection.
            total_storage_bytes (int):
                Sum of persistent storage in bytes of all the
                assets in this collection.
            total_cores (int):
                Sum of the CPU core count of all the assets
                in this collection.
            total_assets (int):
                Count of the number of unique assets in this
                collection.
            memory_utilization_chart (google.cloud.migrationcenter_v1.types.ReportSummary.UtilizationChartData):
                Total memory split into Used/Free buckets.
            storage_utilization_chart (google.cloud.migrationcenter_v1.types.ReportSummary.UtilizationChartData):
                Total memory split into Used/Free buckets.
            operating_system (google.cloud.migrationcenter_v1.types.ReportSummary.ChartData):
                Count of assets grouped by Operating System
                families.
            core_count_histogram (google.cloud.migrationcenter_v1.types.ReportSummary.HistogramChartData):
                Histogram showing a distribution of CPU core
                counts.
            memory_bytes_histogram (google.cloud.migrationcenter_v1.types.ReportSummary.HistogramChartData):
                Histogram showing a distribution of memory
                sizes.
            storage_bytes_histogram (google.cloud.migrationcenter_v1.types.ReportSummary.HistogramChartData):
                Histogram showing a distribution of memory
                sizes.
        """

        total_memory_bytes: int = proto.Field(
            proto.INT64,
            number=1,
        )
        total_storage_bytes: int = proto.Field(
            proto.INT64,
            number=2,
        )
        total_cores: int = proto.Field(
            proto.INT64,
            number=3,
        )
        total_assets: int = proto.Field(
            proto.INT64,
            number=4,
        )
        memory_utilization_chart: "ReportSummary.UtilizationChartData" = proto.Field(
            proto.MESSAGE,
            number=5,
            message="ReportSummary.UtilizationChartData",
        )
        storage_utilization_chart: "ReportSummary.UtilizationChartData" = proto.Field(
            proto.MESSAGE,
            number=6,
            message="ReportSummary.UtilizationChartData",
        )
        operating_system: "ReportSummary.ChartData" = proto.Field(
            proto.MESSAGE,
            number=7,
            message="ReportSummary.ChartData",
        )
        core_count_histogram: "ReportSummary.HistogramChartData" = proto.Field(
            proto.MESSAGE,
            number=8,
            message="ReportSummary.HistogramChartData",
        )
        memory_bytes_histogram: "ReportSummary.HistogramChartData" = proto.Field(
            proto.MESSAGE,
            number=9,
            message="ReportSummary.HistogramChartData",
        )
        storage_bytes_histogram: "ReportSummary.HistogramChartData" = proto.Field(
            proto.MESSAGE,
            number=10,
            message="ReportSummary.HistogramChartData",
        )

    class MachineSeriesAllocation(proto.Message):
        r"""Represents a data point tracking the count of assets
        allocated for a specific Machine Series.

        Attributes:
            machine_series (google.cloud.migrationcenter_v1.types.MachineSeries):
                The Machine Series (e.g. "E2", "N2")
            allocated_asset_count (int):
                Count of assets allocated to this machine
                series.
        """

        machine_series: "MachineSeries" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="MachineSeries",
        )
        allocated_asset_count: int = proto.Field(
            proto.INT64,
            number=2,
        )

    class ComputeEngineFinding(proto.Message):
        r"""A set of findings that applies to assets destined for Compute
        Engine.

        Attributes:
            allocated_regions (MutableSequence[str]):
                Set of regions in which the assets were
                allocated.
            allocated_asset_count (int):
                Count of assets which were allocated.
            machine_series_allocations (MutableSequence[google.cloud.migrationcenter_v1.types.ReportSummary.MachineSeriesAllocation]):
                Distribution of assets based on the Machine
                Series.
            allocated_disk_types (MutableSequence[google.cloud.migrationcenter_v1.types.PersistentDiskType]):
                Set of disk types allocated to assets.
        """

        allocated_regions: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        allocated_asset_count: int = proto.Field(
            proto.INT64,
            number=2,
        )
        machine_series_allocations: MutableSequence[
            "ReportSummary.MachineSeriesAllocation"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="ReportSummary.MachineSeriesAllocation",
        )
        allocated_disk_types: MutableSequence["PersistentDiskType"] = (
            proto.RepeatedField(
                proto.ENUM,
                number=4,
                enum="PersistentDiskType",
            )
        )

    class VmwareEngineFinding(proto.Message):
        r"""A set of findings that applies to assets destined for VMWare
        Engine.

        Attributes:
            allocated_regions (MutableSequence[str]):
                Set of regions in which the assets were
                allocated
            allocated_asset_count (int):
                Count of assets which are allocated
            node_allocations (MutableSequence[google.cloud.migrationcenter_v1.types.ReportSummary.VmwareNodeAllocation]):
                Set of per-nodetype allocation records
        """

        allocated_regions: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        allocated_asset_count: int = proto.Field(
            proto.INT64,
            number=2,
        )
        node_allocations: MutableSequence["ReportSummary.VmwareNodeAllocation"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=3,
                message="ReportSummary.VmwareNodeAllocation",
            )
        )

    class VmwareNodeAllocation(proto.Message):
        r"""Represents assets allocated to a specific VMWare Node type.

        Attributes:
            vmware_node (google.cloud.migrationcenter_v1.types.ReportSummary.VmwareNode):
                VMWare node type, e.g. "ve1-standard-72".
            node_count (int):
                Count of this node type to be provisioned
            allocated_asset_count (int):
                Count of assets allocated to these nodes
        """

        vmware_node: "ReportSummary.VmwareNode" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="ReportSummary.VmwareNode",
        )
        node_count: int = proto.Field(
            proto.INT64,
            number=2,
        )
        allocated_asset_count: int = proto.Field(
            proto.INT64,
            number=3,
        )

    class VmwareNode(proto.Message):
        r"""A VMWare Engine Node

        Attributes:
            code (str):
                Code to identify VMware Engine node series,
                e.g. "ve1-standard-72". Based on the displayName
                of
                cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.nodeTypes
        """

        code: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class SoleTenantFinding(proto.Message):
        r"""A set of findings that applies to assets destined for
        Sole-Tenant nodes.

        Attributes:
            allocated_regions (MutableSequence[str]):
                Set of regions in which the assets are
                allocated
            allocated_asset_count (int):
                Count of assets which are allocated
            node_allocations (MutableSequence[google.cloud.migrationcenter_v1.types.ReportSummary.SoleTenantNodeAllocation]):
                Set of per-nodetype allocation records
        """

        allocated_regions: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        allocated_asset_count: int = proto.Field(
            proto.INT64,
            number=2,
        )
        node_allocations: MutableSequence["ReportSummary.SoleTenantNodeAllocation"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=3,
                message="ReportSummary.SoleTenantNodeAllocation",
            )
        )

    class SoleTenantNodeAllocation(proto.Message):
        r"""Represents the assets allocated to a specific Sole-Tenant
        node type.

        Attributes:
            node (google.cloud.migrationcenter_v1.types.SoleTenantNodeType):
                Sole Tenant node type, e.g.
                "m3-node-128-3904".
            node_count (int):
                Count of this node type to be provisioned
            allocated_asset_count (int):
                Count of assets allocated to these nodes
        """

        node: "SoleTenantNodeType" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="SoleTenantNodeType",
        )
        node_count: int = proto.Field(
            proto.INT64,
            number=2,
        )
        allocated_asset_count: int = proto.Field(
            proto.INT64,
            number=3,
        )

    class GroupPreferenceSetFinding(proto.Message):
        r"""Summary Findings for a specific Group/PreferenceSet
        combination.

        Attributes:
            display_name (str):
                Display Name of the Preference Set
            description (str):
                Description for the Preference Set.
            machine_preferences (google.cloud.migrationcenter_v1.types.VirtualMachinePreferences):
                A set of preferences that applies to all
                machines in the context.
            monthly_cost_total (google.type.money_pb2.Money):
                Total monthly cost for this preference set.
            monthly_cost_compute (google.type.money_pb2.Money):
                Compute monthly cost for this preference set.
            monthly_cost_os_license (google.type.money_pb2.Money):
                Licensing monthly cost for this preference
                set.
            monthly_cost_network_egress (google.type.money_pb2.Money):
                Network Egress monthly cost for this
                preference set.
            monthly_cost_storage (google.type.money_pb2.Money):
                Storage monthly cost for this preference set.
            monthly_cost_other (google.type.money_pb2.Money):
                Miscellaneous monthly cost for this
                preference set.
            compute_engine_finding (google.cloud.migrationcenter_v1.types.ReportSummary.ComputeEngineFinding):
                A set of findings that applies to Compute
                Engine machines in the input.
            vmware_engine_finding (google.cloud.migrationcenter_v1.types.ReportSummary.VmwareEngineFinding):
                A set of findings that applies to VMWare
                machines in the input.
            sole_tenant_finding (google.cloud.migrationcenter_v1.types.ReportSummary.SoleTenantFinding):
                A set of findings that applies to Sole-Tenant
                machines in the input.
        """

        display_name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        description: str = proto.Field(
            proto.STRING,
            number=2,
        )
        machine_preferences: "VirtualMachinePreferences" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="VirtualMachinePreferences",
        )
        monthly_cost_total: money_pb2.Money = proto.Field(
            proto.MESSAGE,
            number=4,
            message=money_pb2.Money,
        )
        monthly_cost_compute: money_pb2.Money = proto.Field(
            proto.MESSAGE,
            number=5,
            message=money_pb2.Money,
        )
        monthly_cost_os_license: money_pb2.Money = proto.Field(
            proto.MESSAGE,
            number=6,
            message=money_pb2.Money,
        )
        monthly_cost_network_egress: money_pb2.Money = proto.Field(
            proto.MESSAGE,
            number=7,
            message=money_pb2.Money,
        )
        monthly_cost_storage: money_pb2.Money = proto.Field(
            proto.MESSAGE,
            number=8,
            message=money_pb2.Money,
        )
        monthly_cost_other: money_pb2.Money = proto.Field(
            proto.MESSAGE,
            number=9,
            message=money_pb2.Money,
        )
        compute_engine_finding: "ReportSummary.ComputeEngineFinding" = proto.Field(
            proto.MESSAGE,
            number=10,
            message="ReportSummary.ComputeEngineFinding",
        )
        vmware_engine_finding: "ReportSummary.VmwareEngineFinding" = proto.Field(
            proto.MESSAGE,
            number=11,
            message="ReportSummary.VmwareEngineFinding",
        )
        sole_tenant_finding: "ReportSummary.SoleTenantFinding" = proto.Field(
            proto.MESSAGE,
            number=12,
            message="ReportSummary.SoleTenantFinding",
        )

    class GroupFinding(proto.Message):
        r"""Summary Findings for a specific Group.

        Attributes:
            display_name (str):
                Display Name for the Group.
            description (str):
                Description for the Group.
            asset_aggregate_stats (google.cloud.migrationcenter_v1.types.ReportSummary.AssetAggregateStats):
                Summary statistics for all the assets in this
                group.
            overlapping_asset_count (int):
                This field is deprecated, do not rely on it
                having a value.
            preference_set_findings (MutableSequence[google.cloud.migrationcenter_v1.types.ReportSummary.GroupPreferenceSetFinding]):
                Findings for each of the PreferenceSets for
                this group.
        """

        display_name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        description: str = proto.Field(
            proto.STRING,
            number=2,
        )
        asset_aggregate_stats: "ReportSummary.AssetAggregateStats" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="ReportSummary.AssetAggregateStats",
        )
        overlapping_asset_count: int = proto.Field(
            proto.INT64,
            number=4,
        )
        preference_set_findings: MutableSequence[
            "ReportSummary.GroupPreferenceSetFinding"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=5,
            message="ReportSummary.GroupPreferenceSetFinding",
        )

    all_assets_stats: AssetAggregateStats = proto.Field(
        proto.MESSAGE,
        number=1,
        message=AssetAggregateStats,
    )
    group_findings: MutableSequence[GroupFinding] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=GroupFinding,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
