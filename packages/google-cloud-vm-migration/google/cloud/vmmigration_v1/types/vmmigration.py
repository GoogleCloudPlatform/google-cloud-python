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
import google.rpc.error_details_pb2 as error_details_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.vmmigration.v1",
    manifest={
        "ComputeEngineDiskType",
        "ComputeEngineLicenseType",
        "ComputeEngineBootOption",
        "OsCapability",
        "BootConversion",
        "UtilizationReportView",
        "MigratingVmView",
        "VmArchitecture",
        "ComputeEngineNetworkTier",
        "ReplicationCycle",
        "CycleStep",
        "InitializingReplicationStep",
        "ReplicatingStep",
        "PostProcessingStep",
        "ReplicationSync",
        "MigratingVm",
        "CutoverForecast",
        "CloneJob",
        "CloneStep",
        "AdaptingOSStep",
        "PreparingVMDisksStep",
        "InstantiatingMigratedVMStep",
        "CutoverJob",
        "CutoverStep",
        "ShuttingDownSourceVMStep",
        "CreateCloneJobRequest",
        "CancelCloneJobRequest",
        "CancelCloneJobResponse",
        "ListCloneJobsRequest",
        "ListCloneJobsResponse",
        "GetCloneJobRequest",
        "Source",
        "Encryption",
        "VmwareSourceDetails",
        "AwsSourceDetails",
        "AzureSourceDetails",
        "DatacenterConnector",
        "UpgradeStatus",
        "AvailableUpdates",
        "ApplianceVersion",
        "ListSourcesRequest",
        "ListSourcesResponse",
        "GetSourceRequest",
        "CreateSourceRequest",
        "UpdateSourceRequest",
        "DeleteSourceRequest",
        "FetchInventoryRequest",
        "VmwareVmDetails",
        "AwsVmDetails",
        "AwsSecurityGroup",
        "AzureVmDetails",
        "VmwareVmsDetails",
        "AwsVmsDetails",
        "AzureVmsDetails",
        "FetchInventoryResponse",
        "FetchStorageInventoryRequest",
        "FetchStorageInventoryResponse",
        "SourceStorageResource",
        "UtilizationReport",
        "VmUtilizationInfo",
        "VmUtilizationMetrics",
        "ListUtilizationReportsRequest",
        "ListUtilizationReportsResponse",
        "GetUtilizationReportRequest",
        "CreateUtilizationReportRequest",
        "DeleteUtilizationReportRequest",
        "ListDatacenterConnectorsResponse",
        "GetDatacenterConnectorRequest",
        "CreateDatacenterConnectorRequest",
        "DeleteDatacenterConnectorRequest",
        "UpgradeApplianceRequest",
        "UpgradeApplianceResponse",
        "ListDatacenterConnectorsRequest",
        "ComputeEngineTargetDefaults",
        "AdaptationModifier",
        "ComputeEngineTargetDetails",
        "NetworkInterface",
        "AppliedLicense",
        "SchedulingNodeAffinity",
        "ComputeScheduling",
        "ComputeEngineDisksTargetDefaults",
        "PersistentDiskDefaults",
        "VmAttachmentDetails",
        "DisksMigrationDisksTargetDefaults",
        "DisksMigrationVmTargetDefaults",
        "BootDiskDefaults",
        "ComputeEngineDisksTargetDetails",
        "PersistentDisk",
        "DisksMigrationDisksTargetDetails",
        "DisksMigrationVmTargetDetails",
        "SchedulePolicy",
        "CreateMigratingVmRequest",
        "ListMigratingVmsRequest",
        "ListMigratingVmsResponse",
        "GetMigratingVmRequest",
        "UpdateMigratingVmRequest",
        "DeleteMigratingVmRequest",
        "StartMigrationRequest",
        "StartMigrationResponse",
        "PauseMigrationRequest",
        "PauseMigrationResponse",
        "ResumeMigrationRequest",
        "ResumeMigrationResponse",
        "FinalizeMigrationRequest",
        "ExtendMigrationRequest",
        "ExtendMigrationResponse",
        "FinalizeMigrationResponse",
        "TargetProject",
        "GetTargetProjectRequest",
        "ListTargetProjectsRequest",
        "ListTargetProjectsResponse",
        "CreateTargetProjectRequest",
        "UpdateTargetProjectRequest",
        "DeleteTargetProjectRequest",
        "Group",
        "ListGroupsRequest",
        "ListGroupsResponse",
        "GetGroupRequest",
        "CreateGroupRequest",
        "UpdateGroupRequest",
        "DeleteGroupRequest",
        "AddGroupMigrationRequest",
        "AddGroupMigrationResponse",
        "RemoveGroupMigrationRequest",
        "RemoveGroupMigrationResponse",
        "CreateCutoverJobRequest",
        "CancelCutoverJobRequest",
        "CancelCutoverJobResponse",
        "ListCutoverJobsRequest",
        "ListCutoverJobsResponse",
        "GetCutoverJobRequest",
        "OperationMetadata",
        "MigrationError",
        "MigrationWarning",
        "VmwareSourceVmDetails",
        "AwsSourceVmDetails",
        "AzureSourceVmDetails",
        "ListReplicationCyclesRequest",
        "ListReplicationCyclesResponse",
        "GetReplicationCycleRequest",
        "VmCapabilities",
        "ImageImport",
        "ImageImportJob",
        "ImageImportStep",
        "InitializingImageImportStep",
        "LoadingImageSourceFilesStep",
        "CreatingImageStep",
        "DiskImageTargetDetails",
        "MachineImageTargetDetails",
        "ServiceAccount",
        "ShieldedInstanceConfig",
        "MachineImageParametersOverrides",
        "ImageImportOsAdaptationParameters",
        "DataDiskImageImport",
        "SkipOsAdaptation",
        "GetImageImportRequest",
        "ListImageImportsRequest",
        "ListImageImportsResponse",
        "CreateImageImportRequest",
        "DeleteImageImportRequest",
        "GetImageImportJobRequest",
        "ListImageImportJobsRequest",
        "ListImageImportJobsResponse",
        "CancelImageImportJobRequest",
        "CancelImageImportJobResponse",
        "DiskMigrationJob",
        "DiskMigrationJobTargetDetails",
        "DiskMigrationStep",
        "CreatingSourceDiskSnapshotStep",
        "CopyingSourceDiskSnapshotStep",
        "ProvisioningTargetDiskStep",
        "ComputeEngineDisk",
        "AwsSourceDiskDetails",
        "CreateDiskMigrationJobRequest",
        "ListDiskMigrationJobsRequest",
        "ListDiskMigrationJobsResponse",
        "GetDiskMigrationJobRequest",
        "UpdateDiskMigrationJobRequest",
        "DeleteDiskMigrationJobRequest",
        "RunDiskMigrationJobRequest",
        "RunDiskMigrationJobResponse",
        "CancelDiskMigrationJobRequest",
        "CancelDiskMigrationJobResponse",
    },
)


class ComputeEngineDiskType(proto.Enum):
    r"""Types of disks supported for Compute Engine VM.

    Values:
        COMPUTE_ENGINE_DISK_TYPE_UNSPECIFIED (0):
            An unspecified disk type. Will be used as
            STANDARD.
        COMPUTE_ENGINE_DISK_TYPE_STANDARD (1):
            A Standard disk type.
        COMPUTE_ENGINE_DISK_TYPE_SSD (2):
            SSD hard disk type.
        COMPUTE_ENGINE_DISK_TYPE_BALANCED (3):
            An alternative to SSD persistent disks that
            balance performance and cost.
        COMPUTE_ENGINE_DISK_TYPE_HYPERDISK_BALANCED (4):
            Hyperdisk balanced disk type.
    """

    COMPUTE_ENGINE_DISK_TYPE_UNSPECIFIED = 0
    COMPUTE_ENGINE_DISK_TYPE_STANDARD = 1
    COMPUTE_ENGINE_DISK_TYPE_SSD = 2
    COMPUTE_ENGINE_DISK_TYPE_BALANCED = 3
    COMPUTE_ENGINE_DISK_TYPE_HYPERDISK_BALANCED = 4


class ComputeEngineLicenseType(proto.Enum):
    r"""Types of licenses used in OS adaptation.

    Values:
        COMPUTE_ENGINE_LICENSE_TYPE_DEFAULT (0):
            The license type is the default for the OS.
        COMPUTE_ENGINE_LICENSE_TYPE_PAYG (1):
            The license type is Pay As You Go license
            type.
        COMPUTE_ENGINE_LICENSE_TYPE_BYOL (2):
            The license type is Bring Your Own License
            type.
    """

    COMPUTE_ENGINE_LICENSE_TYPE_DEFAULT = 0
    COMPUTE_ENGINE_LICENSE_TYPE_PAYG = 1
    COMPUTE_ENGINE_LICENSE_TYPE_BYOL = 2


class ComputeEngineBootOption(proto.Enum):
    r"""Possible values for vm boot option.

    Values:
        COMPUTE_ENGINE_BOOT_OPTION_UNSPECIFIED (0):
            The boot option is unknown.
        COMPUTE_ENGINE_BOOT_OPTION_EFI (1):
            The boot option is EFI.
        COMPUTE_ENGINE_BOOT_OPTION_BIOS (2):
            The boot option is BIOS.
    """

    COMPUTE_ENGINE_BOOT_OPTION_UNSPECIFIED = 0
    COMPUTE_ENGINE_BOOT_OPTION_EFI = 1
    COMPUTE_ENGINE_BOOT_OPTION_BIOS = 2


class OsCapability(proto.Enum):
    r"""VM operating system (OS) capabilities needed for determining
    compatibility with Compute Engine features supported by the
    migration.

    Values:
        OS_CAPABILITY_UNSPECIFIED (0):
            This is for API compatibility only and is not
            in use.
        OS_CAPABILITY_NVME_STORAGE_ACCESS (1):
            NVMe driver installed and the VM can use NVMe
            PD or local SSD.
        OS_CAPABILITY_GVNIC_NETWORK_INTERFACE (2):
            gVNIC virtual NIC driver supported.
        OS_CAPABILITY_IDPF_NETWORK_INTERFACE (3):
            IDPF virtual NIC driver supported.
    """

    OS_CAPABILITY_UNSPECIFIED = 0
    OS_CAPABILITY_NVME_STORAGE_ACCESS = 1
    OS_CAPABILITY_GVNIC_NETWORK_INTERFACE = 2
    OS_CAPABILITY_IDPF_NETWORK_INTERFACE = 3


class BootConversion(proto.Enum):
    r"""Possible boot options conversions.

    Values:
        BOOT_CONVERSION_UNSPECIFIED (0):
            Unspecified conversion type.
        NONE (1):
            No conversion.
        BIOS_TO_EFI (2):
            Convert from BIOS to EFI.
    """

    BOOT_CONVERSION_UNSPECIFIED = 0
    NONE = 1
    BIOS_TO_EFI = 2


class UtilizationReportView(proto.Enum):
    r"""Controls the level of details of a Utilization Report.

    Values:
        UTILIZATION_REPORT_VIEW_UNSPECIFIED (0):
            The default / unset value.
            The API will default to FULL on single report
            request and BASIC for multiple reports request.
        BASIC (1):
            Get the report metadata, without the list of
            VMs and their utilization info.
        FULL (2):
            Include everything.
    """

    UTILIZATION_REPORT_VIEW_UNSPECIFIED = 0
    BASIC = 1
    FULL = 2


class MigratingVmView(proto.Enum):
    r"""Controls the level of details of a Migrating VM.

    Values:
        MIGRATING_VM_VIEW_UNSPECIFIED (0):
            View is unspecified. The API will fallback to
            the default value.
        MIGRATING_VM_VIEW_BASIC (1):
            Get the migrating VM basic details.
            The basic details do not include the recent
            clone jobs and recent cutover jobs lists.
        MIGRATING_VM_VIEW_FULL (2):
            Include everything.
    """

    MIGRATING_VM_VIEW_UNSPECIFIED = 0
    MIGRATING_VM_VIEW_BASIC = 1
    MIGRATING_VM_VIEW_FULL = 2


class VmArchitecture(proto.Enum):
    r"""Possible values for the VM architecture.

    Values:
        VM_ARCHITECTURE_UNSPECIFIED (0):
            The architecture is unknown.
        VM_ARCHITECTURE_X86_FAMILY (1):
            The architecture is one of the x86
            architectures.
        VM_ARCHITECTURE_ARM64 (2):
            The architecture is ARM64.
    """

    VM_ARCHITECTURE_UNSPECIFIED = 0
    VM_ARCHITECTURE_X86_FAMILY = 1
    VM_ARCHITECTURE_ARM64 = 2


class ComputeEngineNetworkTier(proto.Enum):
    r"""Describes the networking tier used for configuring network
    access configuration.

    Values:
        COMPUTE_ENGINE_NETWORK_TIER_UNSPECIFIED (0):
            An unspecified network tier. Will be used as
            PREMIUM.
        NETWORK_TIER_STANDARD (1):
            A standard network tier.
        NETWORK_TIER_PREMIUM (2):
            A premium network tier.
    """

    COMPUTE_ENGINE_NETWORK_TIER_UNSPECIFIED = 0
    NETWORK_TIER_STANDARD = 1
    NETWORK_TIER_PREMIUM = 2


class ReplicationCycle(proto.Message):
    r"""ReplicationCycle contains information about the current
    replication cycle status.

    Attributes:
        name (str):
            The identifier of the ReplicationCycle.
        cycle_number (int):
            The cycle's ordinal number.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the replication cycle has started.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the replication cycle has ended.
        total_pause_duration (google.protobuf.duration_pb2.Duration):
            The accumulated duration the replication
            cycle was paused.
        progress_percent (int):
            The current progress in percentage of this
            cycle. Was replaced by 'steps' field, which
            breaks down the cycle progression more
            accurately.
        steps (MutableSequence[google.cloud.vmmigration_v1.types.CycleStep]):
            The cycle's steps list representing its
            progress.
        state (google.cloud.vmmigration_v1.types.ReplicationCycle.State):
            State of the ReplicationCycle.
        error (google.rpc.status_pb2.Status):
            Output only. Provides details on the state of
            the cycle in case of an error.
        warnings (MutableSequence[google.cloud.vmmigration_v1.types.MigrationWarning]):
            Output only. Warnings that occurred during
            the cycle.
    """

    class State(proto.Enum):
        r"""Possible states of a replication cycle.

        Values:
            STATE_UNSPECIFIED (0):
                The state is unknown. This is used for API
                compatibility only and is not used by the
                system.
            RUNNING (1):
                The replication cycle is running.
            PAUSED (2):
                The replication cycle is paused.
            FAILED (3):
                The replication cycle finished with errors.
            SUCCEEDED (4):
                The replication cycle finished successfully.
        """

        STATE_UNSPECIFIED = 0
        RUNNING = 1
        PAUSED = 2
        FAILED = 3
        SUCCEEDED = 4

    name: str = proto.Field(
        proto.STRING,
        number=13,
    )
    cycle_number: int = proto.Field(
        proto.INT32,
        number=10,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    total_pause_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=7,
        message=duration_pb2.Duration,
    )
    progress_percent: int = proto.Field(
        proto.INT32,
        number=5,
    )
    steps: MutableSequence["CycleStep"] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="CycleStep",
    )
    state: State = proto.Field(
        proto.ENUM,
        number=11,
        enum=State,
    )
    error: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=12,
        message=status_pb2.Status,
    )
    warnings: MutableSequence["MigrationWarning"] = proto.RepeatedField(
        proto.MESSAGE,
        number=14,
        message="MigrationWarning",
    )


class CycleStep(proto.Message):
    r"""CycleStep holds information about a step progress.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        initializing_replication (google.cloud.vmmigration_v1.types.InitializingReplicationStep):
            Initializing replication step.

            This field is a member of `oneof`_ ``step``.
        replicating (google.cloud.vmmigration_v1.types.ReplicatingStep):
            Replicating step.

            This field is a member of `oneof`_ ``step``.
        post_processing (google.cloud.vmmigration_v1.types.PostProcessingStep):
            Post processing step.

            This field is a member of `oneof`_ ``step``.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the cycle step has started.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the cycle step has ended.
    """

    initializing_replication: "InitializingReplicationStep" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="step",
        message="InitializingReplicationStep",
    )
    replicating: "ReplicatingStep" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="step",
        message="ReplicatingStep",
    )
    post_processing: "PostProcessingStep" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="step",
        message="PostProcessingStep",
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


class InitializingReplicationStep(proto.Message):
    r"""InitializingReplicationStep contains specific step details."""


class ReplicatingStep(proto.Message):
    r"""ReplicatingStep contains specific step details.

    Attributes:
        total_bytes (int):
            Total bytes to be handled in the step.
        replicated_bytes (int):
            Replicated bytes in the step.
        last_two_minutes_average_bytes_per_second (int):
            The source disks replication rate for the
            last 2 minutes in bytes per second.
        last_thirty_minutes_average_bytes_per_second (int):
            The source disks replication rate for the
            last 30 minutes in bytes per second.
    """

    total_bytes: int = proto.Field(
        proto.INT64,
        number=1,
    )
    replicated_bytes: int = proto.Field(
        proto.INT64,
        number=2,
    )
    last_two_minutes_average_bytes_per_second: int = proto.Field(
        proto.INT64,
        number=3,
    )
    last_thirty_minutes_average_bytes_per_second: int = proto.Field(
        proto.INT64,
        number=4,
    )


class PostProcessingStep(proto.Message):
    r"""PostProcessingStep contains specific step details."""


class ReplicationSync(proto.Message):
    r"""ReplicationSync contain information about the last replica
    sync to the cloud.

    Attributes:
        last_sync_time (google.protobuf.timestamp_pb2.Timestamp):
            The most updated snapshot created time in the
            source that finished replication.
    """

    last_sync_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )


class MigratingVm(proto.Message):
    r"""MigratingVm describes the VM that will be migrated from a
    Source environment and its replication state.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        compute_engine_target_defaults (google.cloud.vmmigration_v1.types.ComputeEngineTargetDefaults):
            Details of the target VM in Compute Engine.

            This field is a member of `oneof`_ ``target_vm_defaults``.
        compute_engine_disks_target_defaults (google.cloud.vmmigration_v1.types.ComputeEngineDisksTargetDefaults):
            Details of the target Persistent Disks in
            Compute Engine.

            This field is a member of `oneof`_ ``target_vm_defaults``.
        vmware_source_vm_details (google.cloud.vmmigration_v1.types.VmwareSourceVmDetails):
            Output only. Details of the VM from a Vmware
            source.

            This field is a member of `oneof`_ ``source_vm_details``.
        aws_source_vm_details (google.cloud.vmmigration_v1.types.AwsSourceVmDetails):
            Output only. Details of the VM from an AWS
            source.

            This field is a member of `oneof`_ ``source_vm_details``.
        azure_source_vm_details (google.cloud.vmmigration_v1.types.AzureSourceVmDetails):
            Output only. Details of the VM from an Azure
            source.

            This field is a member of `oneof`_ ``source_vm_details``.
        name (str):
            Output only. The identifier of the
            MigratingVm.
        source_vm_id (str):
            The unique ID of the VM in the source.
            The VM's name in vSphere can be changed, so this
            is not the VM's name but rather its moRef id.
            This id is of the form vm-<num>.
        display_name (str):
            The display name attached to the MigratingVm
            by the user.
        description (str):
            The description attached to the migrating VM
            by the user.
        policy (google.cloud.vmmigration_v1.types.SchedulePolicy):
            The replication schedule policy.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the migrating VM was
            created (this refers to this resource and not to
            the time it was installed in the source).
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last time the migrating VM
            resource was updated.
        last_sync (google.cloud.vmmigration_v1.types.ReplicationSync):
            Output only. The most updated snapshot
            created time in the source that finished
            replication.
        state (google.cloud.vmmigration_v1.types.MigratingVm.State):
            Output only. State of the MigratingVm.
        state_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last time the migrating VM
            state was updated.
        current_sync_info (google.cloud.vmmigration_v1.types.ReplicationCycle):
            Output only. Details of the current running
            replication cycle.
        last_replication_cycle (google.cloud.vmmigration_v1.types.ReplicationCycle):
            Output only. Details of the last replication cycle. This
            will be updated whenever a replication cycle is finished and
            is not to be confused with last_sync which is only updated
            on successful replication cycles.
        group (str):
            Output only. The group this migrating vm is included in, if
            any. The group is represented by the full path of the
            appropriate [Group][google.cloud.vmmigration.v1.Group]
            resource.
        labels (MutableMapping[str, str]):
            The labels of the migrating VM.
        recent_clone_jobs (MutableSequence[google.cloud.vmmigration_v1.types.CloneJob]):
            Output only. The recent [clone
            jobs][google.cloud.vmmigration.v1.CloneJob] performed on the
            migrating VM. This field holds the vm's last completed clone
            job and the vm's running clone job, if one exists. Note: To
            have this field populated you need to explicitly request it
            via the "view" parameter of the Get/List request.
        error (google.rpc.status_pb2.Status):
            Output only. Provides details on the state of
            the Migrating VM in case of an error in
            replication.
        recent_cutover_jobs (MutableSequence[google.cloud.vmmigration_v1.types.CutoverJob]):
            Output only. The recent cutover jobs
            performed on the migrating VM. This field holds
            the vm's last completed cutover job and the vm's
            running cutover job, if one exists.
            Note: To have this field populated you need to
            explicitly request it via the "view" parameter
            of the Get/List request.
        cutover_forecast (google.cloud.vmmigration_v1.types.CutoverForecast):
            Output only. Provides details of future
            CutoverJobs of a MigratingVm. Set to empty when
            cutover forecast is unavailable.
        expiration (google.cloud.vmmigration_v1.types.MigratingVm.Expiration):
            Output only. Provides details about the
            expiration state of the migrating VM.
    """

    class State(proto.Enum):
        r"""The possible values of the state/health of source VM.

        Values:
            STATE_UNSPECIFIED (0):
                The state was not sampled by the health
                checks yet.
            PENDING (1):
                The VM in the source is being verified.
            READY (2):
                The source VM was verified, and it's ready to
                start replication.
            FIRST_SYNC (3):
                Migration is going through the first sync
                cycle.
            ACTIVE (4):
                The replication is active, and it's running
                or scheduled to run.
            CUTTING_OVER (7):
                The source VM is being turned off, and a
                final replication is currently running.
            CUTOVER (8):
                The source VM was stopped and replicated. The
                replication is currently paused.
            FINAL_SYNC (9):
                A cutover job is active and replication cycle
                is running the final sync.
            PAUSED (10):
                The replication was paused by the user and no
                cycles are scheduled to run.
            FINALIZING (11):
                The migrating VM is being finalized and
                migration resources are being removed.
            FINALIZED (12):
                The replication process is done. The
                migrating VM is finalized and no longer consumes
                billable resources.
            ERROR (13):
                The replication process encountered an
                unrecoverable error and was aborted.
            EXPIRED (14):
                The migrating VM has passed its expiration
                date. It might be possible to bring it back to
                "Active" state by updating the TTL field. For
                more information, see the documentation.
            FINALIZED_EXPIRED (17):
                The migrating VM's has been finalized and
                migration resources have been removed.
        """

        STATE_UNSPECIFIED = 0
        PENDING = 1
        READY = 2
        FIRST_SYNC = 3
        ACTIVE = 4
        CUTTING_OVER = 7
        CUTOVER = 8
        FINAL_SYNC = 9
        PAUSED = 10
        FINALIZING = 11
        FINALIZED = 12
        ERROR = 13
        EXPIRED = 14
        FINALIZED_EXPIRED = 17

    class Expiration(proto.Message):
        r"""Expiration holds information about the expiration of a
        MigratingVm.

        Attributes:
            expire_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. Timestamp of when this resource
                is considered expired.
            extension_count (int):
                Output only. The number of times expiration
                was extended.
            extendable (bool):
                Output only. Describes whether the expiration
                can be extended.
        """

        expire_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=1,
            message=timestamp_pb2.Timestamp,
        )
        extension_count: int = proto.Field(
            proto.INT32,
            number=2,
        )
        extendable: bool = proto.Field(
            proto.BOOL,
            number=3,
        )

    compute_engine_target_defaults: "ComputeEngineTargetDefaults" = proto.Field(
        proto.MESSAGE,
        number=26,
        oneof="target_vm_defaults",
        message="ComputeEngineTargetDefaults",
    )
    compute_engine_disks_target_defaults: "ComputeEngineDisksTargetDefaults" = (
        proto.Field(
            proto.MESSAGE,
            number=34,
            oneof="target_vm_defaults",
            message="ComputeEngineDisksTargetDefaults",
        )
    )
    vmware_source_vm_details: "VmwareSourceVmDetails" = proto.Field(
        proto.MESSAGE,
        number=28,
        oneof="source_vm_details",
        message="VmwareSourceVmDetails",
    )
    aws_source_vm_details: "AwsSourceVmDetails" = proto.Field(
        proto.MESSAGE,
        number=29,
        oneof="source_vm_details",
        message="AwsSourceVmDetails",
    )
    azure_source_vm_details: "AzureSourceVmDetails" = proto.Field(
        proto.MESSAGE,
        number=30,
        oneof="source_vm_details",
        message="AzureSourceVmDetails",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    source_vm_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=18,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    policy: "SchedulePolicy" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="SchedulePolicy",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    last_sync: "ReplicationSync" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="ReplicationSync",
    )
    state: State = proto.Field(
        proto.ENUM,
        number=23,
        enum=State,
    )
    state_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=22,
        message=timestamp_pb2.Timestamp,
    )
    current_sync_info: "ReplicationCycle" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="ReplicationCycle",
    )
    last_replication_cycle: "ReplicationCycle" = proto.Field(
        proto.MESSAGE,
        number=32,
        message="ReplicationCycle",
    )
    group: str = proto.Field(
        proto.STRING,
        number=15,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=16,
    )
    recent_clone_jobs: MutableSequence["CloneJob"] = proto.RepeatedField(
        proto.MESSAGE,
        number=17,
        message="CloneJob",
    )
    error: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=19,
        message=status_pb2.Status,
    )
    recent_cutover_jobs: MutableSequence["CutoverJob"] = proto.RepeatedField(
        proto.MESSAGE,
        number=20,
        message="CutoverJob",
    )
    cutover_forecast: "CutoverForecast" = proto.Field(
        proto.MESSAGE,
        number=33,
        message="CutoverForecast",
    )
    expiration: Expiration = proto.Field(
        proto.MESSAGE,
        number=37,
        message=Expiration,
    )


class CutoverForecast(proto.Message):
    r"""CutoverForecast holds information about future CutoverJobs of
    a MigratingVm.

    Attributes:
        estimated_cutover_job_duration (google.protobuf.duration_pb2.Duration):
            Output only. Estimation of the CutoverJob
            duration.
    """

    estimated_cutover_job_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=1,
        message=duration_pb2.Duration,
    )


class CloneJob(proto.Message):
    r"""CloneJob describes the process of creating a clone of a
    [MigratingVM][google.cloud.vmmigration.v1.MigratingVm] to the
    requested target based on the latest successful uploaded snapshots.
    While the migration cycles of a MigratingVm take place, it is
    possible to verify the uploaded VM can be started in the cloud, by
    creating a clone. The clone can be created without any downtime, and
    it is created using the latest snapshots which are already in the
    cloud. The cloneJob is only responsible for its work, not its
    products, which means once it is finished, it will never touch the
    instance it created. It will only delete it in case of the CloneJob
    being cancelled or upon failure to clone.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        compute_engine_target_details (google.cloud.vmmigration_v1.types.ComputeEngineTargetDetails):
            Output only. Details of the target VM in
            Compute Engine.

            This field is a member of `oneof`_ ``target_vm_details``.
        compute_engine_disks_target_details (google.cloud.vmmigration_v1.types.ComputeEngineDisksTargetDetails):
            Output only. Details of the target Persistent
            Disks in Compute Engine.

            This field is a member of `oneof`_ ``target_vm_details``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the clone job was
            created (as an API call, not when it was
            actually created in the target).
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the clone job was
            ended.
        name (str):
            Output only. The name of the clone.
        state (google.cloud.vmmigration_v1.types.CloneJob.State):
            Output only. State of the clone job.
        state_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the state was last
            updated.
        error (google.rpc.status_pb2.Status):
            Output only. Provides details for the errors
            that led to the Clone Job's state.
        steps (MutableSequence[google.cloud.vmmigration_v1.types.CloneStep]):
            Output only. The clone steps list
            representing its progress.
    """

    class State(proto.Enum):
        r"""Possible states of the clone job.

        Values:
            STATE_UNSPECIFIED (0):
                The state is unknown. This is used for API
                compatibility only and is not used by the
                system.
            PENDING (1):
                The clone job has not yet started.
            ACTIVE (2):
                The clone job is active and running.
            FAILED (3):
                The clone job finished with errors.
            SUCCEEDED (4):
                The clone job finished successfully.
            CANCELLED (5):
                The clone job was cancelled.
            CANCELLING (6):
                The clone job is being cancelled.
            ADAPTING_OS (7):
                OS adaptation is running as part of the clone
                job to generate license.
        """

        STATE_UNSPECIFIED = 0
        PENDING = 1
        ACTIVE = 2
        FAILED = 3
        SUCCEEDED = 4
        CANCELLED = 5
        CANCELLING = 6
        ADAPTING_OS = 7

    compute_engine_target_details: "ComputeEngineTargetDetails" = proto.Field(
        proto.MESSAGE,
        number=20,
        oneof="target_vm_details",
        message="ComputeEngineTargetDetails",
    )
    compute_engine_disks_target_details: "ComputeEngineDisksTargetDetails" = (
        proto.Field(
            proto.MESSAGE,
            number=25,
            oneof="target_vm_details",
            message="ComputeEngineDisksTargetDetails",
        )
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=22,
        message=timestamp_pb2.Timestamp,
    )
    name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=12,
        enum=State,
    )
    state_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=14,
        message=timestamp_pb2.Timestamp,
    )
    error: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=17,
        message=status_pb2.Status,
    )
    steps: MutableSequence["CloneStep"] = proto.RepeatedField(
        proto.MESSAGE,
        number=23,
        message="CloneStep",
    )


class CloneStep(proto.Message):
    r"""CloneStep holds information about the clone step progress.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        adapting_os (google.cloud.vmmigration_v1.types.AdaptingOSStep):
            Adapting OS step.

            This field is a member of `oneof`_ ``step``.
        preparing_vm_disks (google.cloud.vmmigration_v1.types.PreparingVMDisksStep):
            Preparing VM disks step.

            This field is a member of `oneof`_ ``step``.
        instantiating_migrated_vm (google.cloud.vmmigration_v1.types.InstantiatingMigratedVMStep):
            Instantiating migrated VM step.

            This field is a member of `oneof`_ ``step``.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the step has started.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the step has ended.
    """

    adapting_os: "AdaptingOSStep" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="step",
        message="AdaptingOSStep",
    )
    preparing_vm_disks: "PreparingVMDisksStep" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="step",
        message="PreparingVMDisksStep",
    )
    instantiating_migrated_vm: "InstantiatingMigratedVMStep" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="step",
        message="InstantiatingMigratedVMStep",
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


class AdaptingOSStep(proto.Message):
    r"""AdaptingOSStep contains specific step details."""


class PreparingVMDisksStep(proto.Message):
    r"""PreparingVMDisksStep contains specific step details."""


class InstantiatingMigratedVMStep(proto.Message):
    r"""InstantiatingMigratedVMStep contains specific step details."""


class CutoverJob(proto.Message):
    r"""CutoverJob message describes a cutover of a migrating VM. The
    CutoverJob is the operation of shutting down the VM, creating a
    snapshot and cloning the VM using the replicated snapshot.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        compute_engine_target_details (google.cloud.vmmigration_v1.types.ComputeEngineTargetDetails):
            Output only. Details of the target VM in
            Compute Engine.

            This field is a member of `oneof`_ ``target_vm_details``.
        compute_engine_disks_target_details (google.cloud.vmmigration_v1.types.ComputeEngineDisksTargetDetails):
            Output only. Details of the target Persistent
            Disks in Compute Engine.

            This field is a member of `oneof`_ ``target_vm_details``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the cutover job was
            created (as an API call, not when it was
            actually created in the target).
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the cutover job had
            finished.
        name (str):
            Output only. The name of the cutover job.
        state (google.cloud.vmmigration_v1.types.CutoverJob.State):
            Output only. State of the cutover job.
        state_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the state was last
            updated.
        progress_percent (int):
            Output only. The current progress in
            percentage of the cutover job.
        error (google.rpc.status_pb2.Status):
            Output only. Provides details for the errors
            that led to the Cutover Job's state.
        state_message (str):
            Output only. A message providing possible
            extra details about the current state.
        steps (MutableSequence[google.cloud.vmmigration_v1.types.CutoverStep]):
            Output only. The cutover steps list
            representing its progress.
    """

    class State(proto.Enum):
        r"""Possible states of the cutover job.

        Values:
            STATE_UNSPECIFIED (0):
                The state is unknown. This is used for API
                compatibility only and is not used by the
                system.
            PENDING (1):
                The cutover job has not yet started.
            FAILED (2):
                The cutover job finished with errors.
            SUCCEEDED (3):
                The cutover job finished successfully.
            CANCELLED (4):
                The cutover job was cancelled.
            CANCELLING (5):
                The cutover job is being cancelled.
            ACTIVE (6):
                The cutover job is active and running.
            ADAPTING_OS (7):
                OS adaptation is running as part of the
                cutover job to generate license.
        """

        STATE_UNSPECIFIED = 0
        PENDING = 1
        FAILED = 2
        SUCCEEDED = 3
        CANCELLED = 4
        CANCELLING = 5
        ACTIVE = 6
        ADAPTING_OS = 7

    compute_engine_target_details: "ComputeEngineTargetDetails" = proto.Field(
        proto.MESSAGE,
        number=14,
        oneof="target_vm_details",
        message="ComputeEngineTargetDetails",
    )
    compute_engine_disks_target_details: "ComputeEngineDisksTargetDetails" = (
        proto.Field(
            proto.MESSAGE,
            number=20,
            oneof="target_vm_details",
            message="ComputeEngineDisksTargetDetails",
        )
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=16,
        message=timestamp_pb2.Timestamp,
    )
    name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=5,
        enum=State,
    )
    state_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    progress_percent: int = proto.Field(
        proto.INT32,
        number=13,
    )
    error: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=9,
        message=status_pb2.Status,
    )
    state_message: str = proto.Field(
        proto.STRING,
        number=10,
    )
    steps: MutableSequence["CutoverStep"] = proto.RepeatedField(
        proto.MESSAGE,
        number=17,
        message="CutoverStep",
    )


class CutoverStep(proto.Message):
    r"""CutoverStep holds information about the cutover step
    progress.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        previous_replication_cycle (google.cloud.vmmigration_v1.types.ReplicationCycle):
            A replication cycle prior cutover step.

            This field is a member of `oneof`_ ``step``.
        shutting_down_source_vm (google.cloud.vmmigration_v1.types.ShuttingDownSourceVMStep):
            Shutting down VM step.

            This field is a member of `oneof`_ ``step``.
        final_sync (google.cloud.vmmigration_v1.types.ReplicationCycle):
            Final sync step.

            This field is a member of `oneof`_ ``step``.
        preparing_vm_disks (google.cloud.vmmigration_v1.types.PreparingVMDisksStep):
            Preparing VM disks step.

            This field is a member of `oneof`_ ``step``.
        instantiating_migrated_vm (google.cloud.vmmigration_v1.types.InstantiatingMigratedVMStep):
            Instantiating migrated VM step.

            This field is a member of `oneof`_ ``step``.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the step has started.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the step has ended.
    """

    previous_replication_cycle: "ReplicationCycle" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="step",
        message="ReplicationCycle",
    )
    shutting_down_source_vm: "ShuttingDownSourceVMStep" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="step",
        message="ShuttingDownSourceVMStep",
    )
    final_sync: "ReplicationCycle" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="step",
        message="ReplicationCycle",
    )
    preparing_vm_disks: "PreparingVMDisksStep" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="step",
        message="PreparingVMDisksStep",
    )
    instantiating_migrated_vm: "InstantiatingMigratedVMStep" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="step",
        message="InstantiatingMigratedVMStep",
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


class ShuttingDownSourceVMStep(proto.Message):
    r"""ShuttingDownSourceVMStep contains specific step details."""


class CreateCloneJobRequest(proto.Message):
    r"""Request message for 'CreateCloneJob' request.

    Attributes:
        parent (str):
            Required. The Clone's parent.
        clone_job_id (str):
            Required. The clone job identifier.
        clone_job (google.cloud.vmmigration_v1.types.CloneJob):
            Required. The clone request body.
        request_id (str):
            A request ID to identify requests. Specify a
            unique request ID so that if you must retry your
            request, the server will know to ignore the
            request if it has already been completed. The
            server will guarantee that for at least 60
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
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    clone_job_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    clone_job: "CloneJob" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="CloneJob",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class CancelCloneJobRequest(proto.Message):
    r"""Request message for 'CancelCloneJob' request.

    Attributes:
        name (str):
            Required. The clone job id
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CancelCloneJobResponse(proto.Message):
    r"""Response message for 'CancelCloneJob' request."""


class ListCloneJobsRequest(proto.Message):
    r"""Request message for 'ListCloneJobsRequest' request.

    Attributes:
        parent (str):
            Required. The parent, which owns this
            collection of source VMs.
        page_size (int):
            Optional. The maximum number of clone jobs to
            return. The service may return fewer than this
            value. If unspecified, at most 500 clone jobs
            will be returned. The maximum value is 1000;
            values above 1000 will be coerced to 1000.
        page_token (str):
            Required. A page token, received from a previous
            ``ListCloneJobs`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListCloneJobs`` must match the call that provided the page
            token.
        filter (str):
            Optional. The filter request.
        order_by (str):
            Optional. the order by fields for the result.
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


class ListCloneJobsResponse(proto.Message):
    r"""Response message for 'ListCloneJobs' request.

    Attributes:
        clone_jobs (MutableSequence[google.cloud.vmmigration_v1.types.CloneJob]):
            Output only. The list of clone jobs response.
        next_page_token (str):
            Output only. A token, which can be sent as ``page_token`` to
            retrieve the next page. If this field is omitted, there are
            no subsequent pages.
        unreachable (MutableSequence[str]):
            Output only. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    clone_jobs: MutableSequence["CloneJob"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="CloneJob",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetCloneJobRequest(proto.Message):
    r"""Request message for 'GetCloneJob' request.

    Attributes:
        name (str):
            Required. The name of the CloneJob.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Source(proto.Message):
    r"""Source message describes a specific vm migration Source
    resource. It contains the source environment information.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        vmware (google.cloud.vmmigration_v1.types.VmwareSourceDetails):
            Vmware type source details.

            This field is a member of `oneof`_ ``source_details``.
        aws (google.cloud.vmmigration_v1.types.AwsSourceDetails):
            AWS type source details.

            This field is a member of `oneof`_ ``source_details``.
        azure (google.cloud.vmmigration_v1.types.AzureSourceDetails):
            Azure type source details.

            This field is a member of `oneof`_ ``source_details``.
        name (str):
            Output only. The Source name.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The create time timestamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The update time timestamp.
        labels (MutableMapping[str, str]):
            The labels of the source.
        description (str):
            User-provided description of the source.
        encryption (google.cloud.vmmigration_v1.types.Encryption):
            Optional. Immutable. The encryption details
            of the source data stored by the service.
    """

    vmware: "VmwareSourceDetails" = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="source_details",
        message="VmwareSourceDetails",
    )
    aws: "AwsSourceDetails" = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="source_details",
        message="AwsSourceDetails",
    )
    azure: "AzureSourceDetails" = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="source_details",
        message="AzureSourceDetails",
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
    description: str = proto.Field(
        proto.STRING,
        number=6,
    )
    encryption: "Encryption" = proto.Field(
        proto.MESSAGE,
        number=14,
        message="Encryption",
    )


class Encryption(proto.Message):
    r"""Encryption message describes the details of the applied
    encryption.

    Attributes:
        kms_key (str):
            Required. The name of the encryption key that
            is stored in Google Cloud KMS.
    """

    kms_key: str = proto.Field(
        proto.STRING,
        number=1,
    )


class VmwareSourceDetails(proto.Message):
    r"""VmwareSourceDetails message describes a specific source
    details for the vmware source type.

    Attributes:
        username (str):
            The credentials username.
        password (str):
            Input only. The credentials password. This is
            write only and can not be read in a GET
            operation.
        vcenter_ip (str):
            The ip address of the vcenter this Source
            represents.
        thumbprint (str):
            The thumbprint representing the certificate
            for the vcenter.
        resolved_vcenter_host (str):
            The hostname of the vcenter.
    """

    username: str = proto.Field(
        proto.STRING,
        number=1,
    )
    password: str = proto.Field(
        proto.STRING,
        number=2,
    )
    vcenter_ip: str = proto.Field(
        proto.STRING,
        number=3,
    )
    thumbprint: str = proto.Field(
        proto.STRING,
        number=4,
    )
    resolved_vcenter_host: str = proto.Field(
        proto.STRING,
        number=5,
    )


class AwsSourceDetails(proto.Message):
    r"""AwsSourceDetails message describes a specific source details
    for the AWS source type.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        access_key_creds (google.cloud.vmmigration_v1.types.AwsSourceDetails.AccessKeyCredentials):
            AWS Credentials using access key id and
            secret.

            This field is a member of `oneof`_ ``credentials_type``.
        aws_region (str):
            Immutable. The AWS region that the source VMs
            will be migrated from.
        state (google.cloud.vmmigration_v1.types.AwsSourceDetails.State):
            Output only. State of the source as
            determined by the health check.
        error (google.rpc.status_pb2.Status):
            Output only. Provides details on the state of
            the Source in case of an error.
        inventory_tag_list (MutableSequence[google.cloud.vmmigration_v1.types.AwsSourceDetails.Tag]):
            AWS resource tags to limit the scope of the
            source inventory.
        inventory_security_group_names (MutableSequence[str]):
            AWS security group names to limit the scope
            of the source inventory.
        migration_resources_user_tags (MutableMapping[str, str]):
            User specified tags to add to every M2VM generated resource
            in AWS. These tags will be set in addition to the default
            tags that are set as part of the migration process. The tags
            must not begin with the reserved prefix ``m2vm``.
        public_ip (str):
            Output only. The source's public IP. All
            communication initiated by this source will
            originate from this IP.
    """

    class State(proto.Enum):
        r"""The possible values of the state.

        Values:
            STATE_UNSPECIFIED (0):
                The state is unknown. This is used for API
                compatibility only and is not used by the
                system.
            PENDING (1):
                The state was not sampled by the health
                checks yet.
            FAILED (2):
                The source is available but might not be
                usable yet due to invalid credentials or another
                reason. The error message will contain further
                details.
            ACTIVE (3):
                The source exists and its credentials were
                verified.
        """

        STATE_UNSPECIFIED = 0
        PENDING = 1
        FAILED = 2
        ACTIVE = 3

    class AccessKeyCredentials(proto.Message):
        r"""Message describing AWS Credentials using access key id and
        secret.

        Attributes:
            access_key_id (str):
                AWS access key ID.
            secret_access_key (str):
                Input only. AWS secret access key.
            session_token (str):
                Input only. AWS session token.
                Used only when AWS security token service (STS)
                is responsible for creating the temporary
                credentials.
        """

        access_key_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        secret_access_key: str = proto.Field(
            proto.STRING,
            number=2,
        )
        session_token: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class Tag(proto.Message):
        r"""Tag is an AWS tag representation.

        Attributes:
            key (str):
                Required. Key of tag.
            value (str):
                Required. Value of tag.
        """

        key: str = proto.Field(
            proto.STRING,
            number=1,
        )
        value: str = proto.Field(
            proto.STRING,
            number=2,
        )

    access_key_creds: AccessKeyCredentials = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="credentials_type",
        message=AccessKeyCredentials,
    )
    aws_region: str = proto.Field(
        proto.STRING,
        number=3,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )
    error: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=5,
        message=status_pb2.Status,
    )
    inventory_tag_list: MutableSequence[Tag] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message=Tag,
    )
    inventory_security_group_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    migration_resources_user_tags: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=8,
    )
    public_ip: str = proto.Field(
        proto.STRING,
        number=9,
    )


class AzureSourceDetails(proto.Message):
    r"""AzureSourceDetails message describes a specific source
    details for the Azure source type.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        client_secret_creds (google.cloud.vmmigration_v1.types.AzureSourceDetails.ClientSecretCredentials):
            Azure Credentials using tenant ID, client ID
            and secret.

            This field is a member of `oneof`_ ``credentials_type``.
        subscription_id (str):
            Immutable. Azure subscription ID.
        azure_location (str):
            Immutable. The Azure location (region) that
            the source VMs will be migrated from.
        state (google.cloud.vmmigration_v1.types.AzureSourceDetails.State):
            Output only. State of the source as
            determined by the health check.
        error (google.rpc.status_pb2.Status):
            Output only. Provides details on the state of
            the Source in case of an error.
        migration_resources_user_tags (MutableMapping[str, str]):
            User specified tags to add to every M2VM generated resource
            in Azure. These tags will be set in addition to the default
            tags that are set as part of the migration process. The tags
            must not begin with the reserved prefix ``m4ce`` or
            ``m2vm``.
        resource_group_id (str):
            Output only. The ID of the Azure resource
            group that contains all resources related to the
            migration process of this source.
    """

    class State(proto.Enum):
        r"""The possible values of the state.

        Values:
            STATE_UNSPECIFIED (0):
                The state is unknown. This is used for API
                compatibility only and is not used by the
                system.
            PENDING (1):
                The state was not sampled by the health
                checks yet.
            FAILED (2):
                The source is available but might not be
                usable yet due to invalid credentials or another
                reason. The error message will contain further
                details.
            ACTIVE (3):
                The source exists and its credentials were
                verified.
        """

        STATE_UNSPECIFIED = 0
        PENDING = 1
        FAILED = 2
        ACTIVE = 3

    class ClientSecretCredentials(proto.Message):
        r"""Message describing Azure Credentials using tenant ID, client
        ID and secret.

        Attributes:
            tenant_id (str):
                Azure tenant ID.
            client_id (str):
                Azure client ID.
            client_secret (str):
                Input only. Azure client secret.
        """

        tenant_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        client_id: str = proto.Field(
            proto.STRING,
            number=2,
        )
        client_secret: str = proto.Field(
            proto.STRING,
            number=3,
        )

    client_secret_creds: ClientSecretCredentials = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="credentials_type",
        message=ClientSecretCredentials,
    )
    subscription_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    azure_location: str = proto.Field(
        proto.STRING,
        number=5,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=6,
        enum=State,
    )
    error: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=7,
        message=status_pb2.Status,
    )
    migration_resources_user_tags: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=8,
    )
    resource_group_id: str = proto.Field(
        proto.STRING,
        number=10,
    )


class DatacenterConnector(proto.Message):
    r"""DatacenterConnector message describes a connector between the
    Source and Google Cloud, which is installed on a vmware
    datacenter (an OVA vm installed by the user) to connect the
    Datacenter to Google Cloud and support vm migration data
    transfer.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the connector was
            created (as an API call, not when it was
            actually installed).
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last time the connector was
            updated with an API call.
        name (str):
            Output only. The connector's name.
        registration_id (str):
            Immutable. A unique key for this connector.
            This key is internal to the OVA connector and is
            supplied with its creation during the
            registration process and can not be modified.
        service_account (str):
            The service account to use in the connector
            when communicating with the cloud.
        version (str):
            The version running in the
            DatacenterConnector. This is supplied by the OVA
            connector during the registration process and
            can not be modified.
        bucket (str):
            Output only. The communication channel
            between the datacenter connector and Google
            Cloud.
        state (google.cloud.vmmigration_v1.types.DatacenterConnector.State):
            Output only. State of the
            DatacenterConnector, as determined by the health
            checks.
        state_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the state was last set.
        error (google.rpc.status_pb2.Status):
            Output only. Provides details on the state of
            the Datacenter Connector in case of an error.
        appliance_infrastructure_version (str):
            Output only. Appliance OVA version.
            This is the OVA which is manually installed by
            the user and contains the infrastructure for the
            automatically updatable components on the
            appliance.
        appliance_software_version (str):
            Output only. Appliance last installed update
            bundle version. This is the version of the
            automatically updatable components on the
            appliance.
        available_versions (google.cloud.vmmigration_v1.types.AvailableUpdates):
            Output only. The available versions for
            updating this appliance.
        upgrade_status (google.cloud.vmmigration_v1.types.UpgradeStatus):
            Output only. The status of the current / last
            upgradeAppliance operation.
    """

    class State(proto.Enum):
        r"""The possible values of the state.

        Values:
            STATE_UNSPECIFIED (0):
                The state is unknown. This is used for API
                compatibility only and is not used by the
                system.
            PENDING (1):
                The state was not sampled by the health
                checks yet.
            OFFLINE (2):
                The source was sampled by health checks and
                is not available.
            FAILED (3):
                The source is available but might not be
                usable yet due to unvalidated credentials or
                another reason. The credentials referred to are
                the ones to the Source. The error message will
                contain further details.
            ACTIVE (4):
                The source exists and its credentials were
                verified.
        """

        STATE_UNSPECIFIED = 0
        PENDING = 1
        OFFLINE = 2
        FAILED = 3
        ACTIVE = 4

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
    name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    registration_id: str = proto.Field(
        proto.STRING,
        number=12,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=5,
    )
    version: str = proto.Field(
        proto.STRING,
        number=6,
    )
    bucket: str = proto.Field(
        proto.STRING,
        number=10,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=7,
        enum=State,
    )
    state_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    error: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=11,
        message=status_pb2.Status,
    )
    appliance_infrastructure_version: str = proto.Field(
        proto.STRING,
        number=13,
    )
    appliance_software_version: str = proto.Field(
        proto.STRING,
        number=14,
    )
    available_versions: "AvailableUpdates" = proto.Field(
        proto.MESSAGE,
        number=15,
        message="AvailableUpdates",
    )
    upgrade_status: "UpgradeStatus" = proto.Field(
        proto.MESSAGE,
        number=16,
        message="UpgradeStatus",
    )


class UpgradeStatus(proto.Message):
    r"""UpgradeStatus contains information about upgradeAppliance
    operation.

    Attributes:
        version (str):
            The version to upgrade to.
        state (google.cloud.vmmigration_v1.types.UpgradeStatus.State):
            The state of the upgradeAppliance operation.
        error (google.rpc.status_pb2.Status):
            Output only. Provides details on the state of
            the upgrade operation in case of an error.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the operation was started.
        previous_version (str):
            The version from which we upgraded.
    """

    class State(proto.Enum):
        r"""The possible values of the state.

        Values:
            STATE_UNSPECIFIED (0):
                The state was not sampled by the health
                checks yet.
            RUNNING (1):
                The upgrade has started.
            FAILED (2):
                The upgrade failed.
            SUCCEEDED (3):
                The upgrade finished successfully.
        """

        STATE_UNSPECIFIED = 0
        RUNNING = 1
        FAILED = 2
        SUCCEEDED = 3

    version: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=2,
        enum=State,
    )
    error: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=3,
        message=status_pb2.Status,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    previous_version: str = proto.Field(
        proto.STRING,
        number=5,
    )


class AvailableUpdates(proto.Message):
    r"""Holds information about the available versions for upgrade.

    Attributes:
        new_deployable_appliance (google.cloud.vmmigration_v1.types.ApplianceVersion):
            The newest deployable version of the
            appliance. The current appliance can't be
            updated into this version, and the owner must
            manually deploy this OVA to a new appliance.
        in_place_update (google.cloud.vmmigration_v1.types.ApplianceVersion):
            The latest version for in place update.
            The current appliance can be updated to this
            version using the API or m4c CLI.
    """

    new_deployable_appliance: "ApplianceVersion" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ApplianceVersion",
    )
    in_place_update: "ApplianceVersion" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ApplianceVersion",
    )


class ApplianceVersion(proto.Message):
    r"""Describes an appliance version.

    Attributes:
        version (str):
            The appliance version.
        uri (str):
            A link for downloading the version.
        critical (bool):
            Determine whether it's critical to upgrade
            the appliance to this version.
        release_notes_uri (str):
            Link to a page that contains the version
            release notes.
    """

    version: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    critical: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    release_notes_uri: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListSourcesRequest(proto.Message):
    r"""Request message for 'ListSources' request.

    Attributes:
        parent (str):
            Required. The parent, which owns this
            collection of sources.
        page_size (int):
            Optional. The maximum number of sources to
            return. The service may return fewer than this
            value. If unspecified, at most 500 sources will
            be returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            Required. A page token, received from a previous
            ``ListSources`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListSources`` must match the call that provided the page
            token.
        filter (str):
            Optional. The filter request.
        order_by (str):
            Optional. the order by fields for the result.
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
    r"""Response message for 'ListSources' request.

    Attributes:
        sources (MutableSequence[google.cloud.vmmigration_v1.types.Source]):
            Output only. The list of sources response.
        next_page_token (str):
            Output only. A token, which can be sent as ``page_token`` to
            retrieve the next page. If this field is omitted, there are
            no subsequent pages.
        unreachable (MutableSequence[str]):
            Output only. Locations that could not be
            reached.
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
    r"""Request message for 'GetSource' request.

    Attributes:
        name (str):
            Required. The Source name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateSourceRequest(proto.Message):
    r"""Request message for 'CreateSource' request.

    Attributes:
        parent (str):
            Required. The Source's parent.
        source_id (str):
            Required. The source identifier.
        source (google.cloud.vmmigration_v1.types.Source):
            Required. The create request body.
        request_id (str):
            A request ID to identify requests. Specify a
            unique request ID so that if you must retry your
            request, the server will know to ignore the
            request if it has already been completed. The
            server will guarantee that for at least 60
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
    r"""Update message for 'UpdateSources' request.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Field mask is used to specify the fields to be overwritten
            in the Source resource by the update. The fields specified
            in the update_mask are relative to the resource, not the
            full request. A field will be overwritten if it is in the
            mask. If the user does not provide a mask then all fields
            will be overwritten.
        source (google.cloud.vmmigration_v1.types.Source):
            Required. The update request body.
        request_id (str):
            A request ID to identify requests. Specify a
            unique request ID so that if you must retry your
            request, the server will know to ignore the
            request if it has already been completed. The
            server will guarantee that for at least 60
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
    r"""Request message for 'DeleteSource' request.

    Attributes:
        name (str):
            Required. The Source name.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes after the first request.

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


class FetchInventoryRequest(proto.Message):
    r"""Request message for
    [fetchInventory][google.cloud.vmmigration.v1.VmMigration.FetchInventory].

    Attributes:
        source (str):
            Required. The name of the Source.
        force_refresh (bool):
            If this flag is set to true, the source will
            be queried instead of using cached results.
            Using this flag will make the call slower.
    """

    source: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force_refresh: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class VmwareVmDetails(proto.Message):
    r"""VmwareVmDetails describes a VM in vCenter.

    Attributes:
        vm_id (str):
            The VM's id in the source (note that this is
            not the MigratingVm's id). This is the moref id
            of the VM.
        datacenter_id (str):
            The id of the vCenter's datacenter this VM is
            contained in.
        datacenter_description (str):
            The descriptive name of the vCenter's
            datacenter this VM is contained in.
        uuid (str):
            The unique identifier of the VM in vCenter.
        display_name (str):
            The display name of the VM. Note that this is
            not necessarily unique.
        power_state (google.cloud.vmmigration_v1.types.VmwareVmDetails.PowerState):
            The power state of the VM at the moment list
            was taken.
        cpu_count (int):
            The number of cpus in the VM.
        memory_mb (int):
            The size of the memory of the VM in MB.
        disk_count (int):
            The number of disks the VM has.
        committed_storage_mb (int):
            The total size of the storage allocated to
            the VM in MB.
        guest_description (str):
            The VM's OS. See for example
            https://vdc-repo.vmware.com/vmwb-repository/dcr-public/da47f910-60ac-438b-8b9b-6122f4d14524/16b7274a-bf8b-4b4c-a05e-746f2aa93c8c/doc/vim.vm.GuestOsDescriptor.GuestOsIdentifier.html
            for types of strings this might hold.
        boot_option (google.cloud.vmmigration_v1.types.VmwareVmDetails.BootOption):
            Output only. The VM Boot Option.
        architecture (google.cloud.vmmigration_v1.types.VmwareVmDetails.VmArchitecture):
            Output only. The CPU architecture.
    """

    class PowerState(proto.Enum):
        r"""Possible values for the power state of the VM.

        Values:
            POWER_STATE_UNSPECIFIED (0):
                Power state is not specified.
            ON (1):
                The VM is turned ON.
            OFF (2):
                The VM is turned OFF.
            SUSPENDED (3):
                The VM is suspended. This is similar to
                hibernation or sleep mode.
        """

        POWER_STATE_UNSPECIFIED = 0
        ON = 1
        OFF = 2
        SUSPENDED = 3

    class BootOption(proto.Enum):
        r"""Possible values for vm boot option.

        Values:
            BOOT_OPTION_UNSPECIFIED (0):
                The boot option is unknown.
            EFI (1):
                The boot option is EFI.
            BIOS (2):
                The boot option is BIOS.
        """

        BOOT_OPTION_UNSPECIFIED = 0
        EFI = 1
        BIOS = 2

    class VmArchitecture(proto.Enum):
        r"""Possible values for the VM architecture.

        Values:
            VM_ARCHITECTURE_UNSPECIFIED (0):
                The architecture is unknown.
            VM_ARCHITECTURE_X86_FAMILY (1):
                The architecture is one of the x86
                architectures.
            VM_ARCHITECTURE_ARM64 (2):
                The architecture is ARM64.
        """

        VM_ARCHITECTURE_UNSPECIFIED = 0
        VM_ARCHITECTURE_X86_FAMILY = 1
        VM_ARCHITECTURE_ARM64 = 2

    vm_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    datacenter_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    datacenter_description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    uuid: str = proto.Field(
        proto.STRING,
        number=4,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    power_state: PowerState = proto.Field(
        proto.ENUM,
        number=6,
        enum=PowerState,
    )
    cpu_count: int = proto.Field(
        proto.INT32,
        number=7,
    )
    memory_mb: int = proto.Field(
        proto.INT32,
        number=8,
    )
    disk_count: int = proto.Field(
        proto.INT32,
        number=9,
    )
    committed_storage_mb: int = proto.Field(
        proto.INT64,
        number=12,
    )
    guest_description: str = proto.Field(
        proto.STRING,
        number=11,
    )
    boot_option: BootOption = proto.Field(
        proto.ENUM,
        number=13,
        enum=BootOption,
    )
    architecture: VmArchitecture = proto.Field(
        proto.ENUM,
        number=14,
        enum=VmArchitecture,
    )


class AwsVmDetails(proto.Message):
    r"""AwsVmDetails describes a VM in AWS.

    Attributes:
        vm_id (str):
            The VM ID in AWS.
        display_name (str):
            The display name of the VM. Note that this
            value is not necessarily unique.
        source_id (str):
            The id of the AWS's source this VM is
            connected to.
        source_description (str):
            The descriptive name of the AWS's source this
            VM is connected to.
        power_state (google.cloud.vmmigration_v1.types.AwsVmDetails.PowerState):
            Output only. The power state of the VM at the
            moment list was taken.
        cpu_count (int):
            The number of CPU cores the VM has.
        memory_mb (int):
            The memory size of the VM in MB.
        disk_count (int):
            The number of disks the VM has.
        committed_storage_mb (int):
            The total size of the storage allocated to
            the VM in MB.
        os_description (str):
            The VM's OS.
        boot_option (google.cloud.vmmigration_v1.types.AwsVmDetails.BootOption):
            The VM Boot Option.
        instance_type (str):
            The instance type of the VM.
        vpc_id (str):
            The VPC ID the VM belongs to.
        security_groups (MutableSequence[google.cloud.vmmigration_v1.types.AwsSecurityGroup]):
            The security groups the VM belongs to.
        tags (MutableMapping[str, str]):
            The tags of the VM.
        zone (str):
            The AWS zone of the VM.
        virtualization_type (google.cloud.vmmigration_v1.types.AwsVmDetails.VmVirtualizationType):
            The virtualization type.
        architecture (google.cloud.vmmigration_v1.types.AwsVmDetails.VmArchitecture):
            The CPU architecture.
        vcpu_count (int):
            The number of vCPUs the VM has. It is calculated as the
            number of CPU cores \* threads per CPU the VM has.
    """

    class PowerState(proto.Enum):
        r"""Possible values for the power state of the VM.

        Values:
            POWER_STATE_UNSPECIFIED (0):
                Power state is not specified.
            ON (1):
                The VM is turned on.
            OFF (2):
                The VM is turned off.
            SUSPENDED (3):
                The VM is suspended. This is similar to
                hibernation or sleep mode.
            PENDING (4):
                The VM is starting.
        """

        POWER_STATE_UNSPECIFIED = 0
        ON = 1
        OFF = 2
        SUSPENDED = 3
        PENDING = 4

    class BootOption(proto.Enum):
        r"""The possible values for the vm boot option.

        Values:
            BOOT_OPTION_UNSPECIFIED (0):
                The boot option is unknown.
            EFI (1):
                The boot option is UEFI.
            BIOS (2):
                The boot option is LEGACY-BIOS.
        """

        BOOT_OPTION_UNSPECIFIED = 0
        EFI = 1
        BIOS = 2

    class VmVirtualizationType(proto.Enum):
        r"""Possible values for the virtualization types of the VM.

        Values:
            VM_VIRTUALIZATION_TYPE_UNSPECIFIED (0):
                The virtualization type is unknown.
            HVM (1):
                The virtualziation type is HVM.
            PARAVIRTUAL (2):
                The virtualziation type is PARAVIRTUAL.
        """

        VM_VIRTUALIZATION_TYPE_UNSPECIFIED = 0
        HVM = 1
        PARAVIRTUAL = 2

    class VmArchitecture(proto.Enum):
        r"""Possible values for the architectures of the VM.

        Values:
            VM_ARCHITECTURE_UNSPECIFIED (0):
                The architecture is unknown.
            I386 (1):
                The architecture is I386.
            X86_64 (2):
                The architecture is X86_64.
            ARM64 (3):
                The architecture is ARM64.
            X86_64_MAC (4):
                The architecture is X86_64_MAC.
        """

        VM_ARCHITECTURE_UNSPECIFIED = 0
        I386 = 1
        X86_64 = 2
        ARM64 = 3
        X86_64_MAC = 4

    vm_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    source_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    source_description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    power_state: PowerState = proto.Field(
        proto.ENUM,
        number=5,
        enum=PowerState,
    )
    cpu_count: int = proto.Field(
        proto.INT32,
        number=6,
    )
    memory_mb: int = proto.Field(
        proto.INT32,
        number=7,
    )
    disk_count: int = proto.Field(
        proto.INT32,
        number=8,
    )
    committed_storage_mb: int = proto.Field(
        proto.INT64,
        number=9,
    )
    os_description: str = proto.Field(
        proto.STRING,
        number=10,
    )
    boot_option: BootOption = proto.Field(
        proto.ENUM,
        number=11,
        enum=BootOption,
    )
    instance_type: str = proto.Field(
        proto.STRING,
        number=12,
    )
    vpc_id: str = proto.Field(
        proto.STRING,
        number=13,
    )
    security_groups: MutableSequence["AwsSecurityGroup"] = proto.RepeatedField(
        proto.MESSAGE,
        number=14,
        message="AwsSecurityGroup",
    )
    tags: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=15,
    )
    zone: str = proto.Field(
        proto.STRING,
        number=16,
    )
    virtualization_type: VmVirtualizationType = proto.Field(
        proto.ENUM,
        number=17,
        enum=VmVirtualizationType,
    )
    architecture: VmArchitecture = proto.Field(
        proto.ENUM,
        number=18,
        enum=VmArchitecture,
    )
    vcpu_count: int = proto.Field(
        proto.INT32,
        number=19,
    )


class AwsSecurityGroup(proto.Message):
    r"""AwsSecurityGroup describes a security group of an AWS VM.

    Attributes:
        id (str):
            The AWS security group id.
        name (str):
            The AWS security group name.
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AzureVmDetails(proto.Message):
    r"""AzureVmDetails describes a VM in Azure.

    Attributes:
        vm_id (str):
            The VM full path in Azure.
        power_state (google.cloud.vmmigration_v1.types.AzureVmDetails.PowerState):
            The power state of the VM at the moment list
            was taken.
        vm_size (str):
            VM size as configured in Azure. Determines
            the VM's hardware spec.
        cpu_count (int):
            The number of cpus the VM has.
        memory_mb (int):
            The memory size of the VM in MB.
        disk_count (int):
            The number of disks the VM has, including OS
            disk.
        committed_storage_mb (int):
            The total size of the storage allocated to
            the VM in MB.
        os_disk (google.cloud.vmmigration_v1.types.AzureVmDetails.OSDisk):
            Description of the OS disk.
        disks (MutableSequence[google.cloud.vmmigration_v1.types.AzureVmDetails.Disk]):
            Description of the data disks.
        os_description (google.cloud.vmmigration_v1.types.AzureVmDetails.OSDescription):
            Description of the OS.
        boot_option (google.cloud.vmmigration_v1.types.AzureVmDetails.BootOption):
            The VM Boot Option.
        tags (MutableMapping[str, str]):
            The tags of the VM.
        computer_name (str):
            The VM's ComputerName.
        architecture (google.cloud.vmmigration_v1.types.AzureVmDetails.VmArchitecture):
            The CPU architecture.
    """

    class PowerState(proto.Enum):
        r"""Possible values for the power state of the VM.

        Values:
            POWER_STATE_UNSPECIFIED (0):
                Power state is not specified.
            STARTING (1):
                The VM is starting.
            RUNNING (2):
                The VM is running.
            STOPPING (3):
                The VM is stopping.
            STOPPED (4):
                The VM is stopped.
            DEALLOCATING (5):
                The VM is deallocating.
            DEALLOCATED (6):
                The VM is deallocated.
            UNKNOWN (7):
                The VM's power state is unknown.
        """

        POWER_STATE_UNSPECIFIED = 0
        STARTING = 1
        RUNNING = 2
        STOPPING = 3
        STOPPED = 4
        DEALLOCATING = 5
        DEALLOCATED = 6
        UNKNOWN = 7

    class BootOption(proto.Enum):
        r"""The possible values for the vm boot option.

        Values:
            BOOT_OPTION_UNSPECIFIED (0):
                The boot option is unknown.
            EFI (1):
                The boot option is UEFI.
            BIOS (2):
                The boot option is BIOS.
        """

        BOOT_OPTION_UNSPECIFIED = 0
        EFI = 1
        BIOS = 2

    class VmArchitecture(proto.Enum):
        r"""Possible values for the VM architecture.

        Values:
            VM_ARCHITECTURE_UNSPECIFIED (0):
                The architecture is unknown.
            VM_ARCHITECTURE_X86_FAMILY (1):
                The architecture is one of the x86
                architectures.
            VM_ARCHITECTURE_ARM64 (2):
                The architecture is ARM64.
        """

        VM_ARCHITECTURE_UNSPECIFIED = 0
        VM_ARCHITECTURE_X86_FAMILY = 1
        VM_ARCHITECTURE_ARM64 = 2

    class OSDisk(proto.Message):
        r"""A message describing the OS disk.

        Attributes:
            type_ (str):
                The disk's type.
            name (str):
                The disk's full name.
            size_gb (int):
                The disk's size in GB.
        """

        type_: str = proto.Field(
            proto.STRING,
            number=1,
        )
        name: str = proto.Field(
            proto.STRING,
            number=2,
        )
        size_gb: int = proto.Field(
            proto.INT32,
            number=3,
        )

    class Disk(proto.Message):
        r"""A message describing a data disk.

        Attributes:
            name (str):
                The disk name.
            size_gb (int):
                The disk size in GB.
            lun (int):
                The disk's Logical Unit Number (LUN).
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        size_gb: int = proto.Field(
            proto.INT32,
            number=2,
        )
        lun: int = proto.Field(
            proto.INT32,
            number=3,
        )

    class OSDescription(proto.Message):
        r"""A message describing the VM's OS. Including OS, Publisher,
        Offer and Plan if applicable.

        Attributes:
            type_ (str):
                OS type.
            publisher (str):
                OS publisher.
            offer (str):
                OS offer.
            plan (str):
                OS plan.
        """

        type_: str = proto.Field(
            proto.STRING,
            number=1,
        )
        publisher: str = proto.Field(
            proto.STRING,
            number=2,
        )
        offer: str = proto.Field(
            proto.STRING,
            number=3,
        )
        plan: str = proto.Field(
            proto.STRING,
            number=4,
        )

    vm_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    power_state: PowerState = proto.Field(
        proto.ENUM,
        number=2,
        enum=PowerState,
    )
    vm_size: str = proto.Field(
        proto.STRING,
        number=3,
    )
    cpu_count: int = proto.Field(
        proto.INT32,
        number=4,
    )
    memory_mb: int = proto.Field(
        proto.INT32,
        number=5,
    )
    disk_count: int = proto.Field(
        proto.INT32,
        number=6,
    )
    committed_storage_mb: int = proto.Field(
        proto.INT64,
        number=7,
    )
    os_disk: OSDisk = proto.Field(
        proto.MESSAGE,
        number=8,
        message=OSDisk,
    )
    disks: MutableSequence[Disk] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message=Disk,
    )
    os_description: OSDescription = proto.Field(
        proto.MESSAGE,
        number=10,
        message=OSDescription,
    )
    boot_option: BootOption = proto.Field(
        proto.ENUM,
        number=11,
        enum=BootOption,
    )
    tags: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=12,
    )
    computer_name: str = proto.Field(
        proto.STRING,
        number=13,
    )
    architecture: VmArchitecture = proto.Field(
        proto.ENUM,
        number=14,
        enum=VmArchitecture,
    )


class VmwareVmsDetails(proto.Message):
    r"""VmwareVmsDetails describes VMs in vCenter.

    Attributes:
        details (MutableSequence[google.cloud.vmmigration_v1.types.VmwareVmDetails]):
            The details of the vmware VMs.
    """

    details: MutableSequence["VmwareVmDetails"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="VmwareVmDetails",
    )


class AwsVmsDetails(proto.Message):
    r"""AWSVmsDetails describes VMs in AWS.

    Attributes:
        details (MutableSequence[google.cloud.vmmigration_v1.types.AwsVmDetails]):
            The details of the AWS VMs.
    """

    details: MutableSequence["AwsVmDetails"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AwsVmDetails",
    )


class AzureVmsDetails(proto.Message):
    r"""AzureVmsDetails describes VMs in Azure.

    Attributes:
        details (MutableSequence[google.cloud.vmmigration_v1.types.AzureVmDetails]):
            The details of the Azure VMs.
    """

    details: MutableSequence["AzureVmDetails"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AzureVmDetails",
    )


class FetchInventoryResponse(proto.Message):
    r"""Response message for
    [fetchInventory][google.cloud.vmmigration.v1.VmMigration.FetchInventory].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        vmware_vms (google.cloud.vmmigration_v1.types.VmwareVmsDetails):
            The description of the VMs in a Source of
            type Vmware.

            This field is a member of `oneof`_ ``SourceVms``.
        aws_vms (google.cloud.vmmigration_v1.types.AwsVmsDetails):
            The description of the VMs in a Source of
            type AWS.

            This field is a member of `oneof`_ ``SourceVms``.
        azure_vms (google.cloud.vmmigration_v1.types.AzureVmsDetails):
            The description of the VMs in a Source of
            type Azure.

            This field is a member of `oneof`_ ``SourceVms``.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the source
            was last queried (if the result is from the
            cache).
    """

    vmware_vms: "VmwareVmsDetails" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="SourceVms",
        message="VmwareVmsDetails",
    )
    aws_vms: "AwsVmsDetails" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="SourceVms",
        message="AwsVmsDetails",
    )
    azure_vms: "AzureVmsDetails" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="SourceVms",
        message="AzureVmsDetails",
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


class FetchStorageInventoryRequest(proto.Message):
    r"""Request message for
    [fetchStorageInventory][google.cloud.vmmigration.v1.VmMigration.FetchStorageInventory].

    Attributes:
        source (str):
            Required. The name of the Source.
        type_ (google.cloud.vmmigration_v1.types.FetchStorageInventoryRequest.StorageType):
            Required. The type of the storage inventory
            to fetch.
        force_refresh (bool):
            Optional. If this flag is set to true, the
            source will be queried instead of using cached
            results. Using this flag will make the call
            slower.
        page_size (int):
            Optional. The maximum number of VMs to
            return. The service may return fewer than this
            value.
        page_token (str):
            Optional. A page token, received from a previous
            ``FetchStorageInventory`` call. Provide this to retrieve the
            subsequent page. When paginating, all other parameters
            provided to ``FetchStorageInventory`` must match the call
            that provided the page token.
    """

    class StorageType(proto.Enum):
        r"""The type of the storage inventory to fetch.

        Values:
            STORAGE_TYPE_UNSPECIFIED (0):
                The type is unspecified.
            DISKS (1):
                The type is disks.
            SNAPSHOTS (2):
                The type is snapshots.
        """

        STORAGE_TYPE_UNSPECIFIED = 0
        DISKS = 1
        SNAPSHOTS = 2

    source: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: StorageType = proto.Field(
        proto.ENUM,
        number=2,
        enum=StorageType,
    )
    force_refresh: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=4,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=5,
    )


class FetchStorageInventoryResponse(proto.Message):
    r"""Response message for
    [fetchStorageInventory][google.cloud.vmmigration.v1.VmMigration.FetchStorageInventory].

    Attributes:
        resources (MutableSequence[google.cloud.vmmigration_v1.types.SourceStorageResource]):
            The list of storage resources in the source.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the source
            was last queried (if the result is from the
            cache).
        next_page_token (str):
            Output only. A token, which can be sent as ``page_token`` to
            retrieve the next page. If this field is omitted, there are
            no subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    resources: MutableSequence["SourceStorageResource"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SourceStorageResource",
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SourceStorageResource(proto.Message):
    r"""SourceStorageResource describes a storage resource in the
    source.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        aws_disk_details (google.cloud.vmmigration_v1.types.AwsSourceDiskDetails):
            Source AWS volume details.

            This field is a member of `oneof`_ ``StorageResource``.
    """

    aws_disk_details: "AwsSourceDiskDetails" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="StorageResource",
        message="AwsSourceDiskDetails",
    )


class UtilizationReport(proto.Message):
    r"""Utilization report details the utilization (CPU, memory,
    etc.) of selected source VMs.

    Attributes:
        name (str):
            Output only. The report unique name.
        display_name (str):
            The report display name, as assigned by the
            user.
        state (google.cloud.vmmigration_v1.types.UtilizationReport.State):
            Output only. Current state of the report.
        state_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the state was last set.
        error (google.rpc.status_pb2.Status):
            Output only. Provides details on the state of
            the report in case of an error.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the report was created
            (this refers to the time of the request, not the
            time the report creation completed).
        time_frame (google.cloud.vmmigration_v1.types.UtilizationReport.TimeFrame):
            Time frame of the report.
        frame_end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The point in time when the time frame ends.
            Notice that the time frame is counted backwards. For
            instance if the "frame_end_time" value is 2021/01/20 and the
            time frame is WEEK then the report covers the week between
            2021/01/20 and 2021/01/14.
        vm_count (int):
            Output only. Total number of VMs included in
            the report.
        vms (MutableSequence[google.cloud.vmmigration_v1.types.VmUtilizationInfo]):
            List of utilization information per VM. When sent as part of
            the request, the "vm_id" field is used in order to specify
            which VMs to include in the report. In that case all other
            fields are ignored.
    """

    class State(proto.Enum):
        r"""Utilization report state.

        Values:
            STATE_UNSPECIFIED (0):
                The state is unknown. This value is not in
                use.
            CREATING (1):
                The report is in the making.
            SUCCEEDED (2):
                Report creation completed successfully.
            FAILED (3):
                Report creation failed.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        SUCCEEDED = 2
        FAILED = 3

    class TimeFrame(proto.Enum):
        r"""Report time frame options.

        Values:
            TIME_FRAME_UNSPECIFIED (0):
                The time frame was not specified and will
                default to WEEK.
            WEEK (1):
                One week.
            MONTH (2):
                One month.
            YEAR (3):
                One year.
        """

        TIME_FRAME_UNSPECIFIED = 0
        WEEK = 1
        MONTH = 2
        YEAR = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )
    state_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    error: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=5,
        message=status_pb2.Status,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    time_frame: TimeFrame = proto.Field(
        proto.ENUM,
        number=7,
        enum=TimeFrame,
    )
    frame_end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    vm_count: int = proto.Field(
        proto.INT32,
        number=9,
    )
    vms: MutableSequence["VmUtilizationInfo"] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message="VmUtilizationInfo",
    )


class VmUtilizationInfo(proto.Message):
    r"""Utilization information of a single VM.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        vmware_vm_details (google.cloud.vmmigration_v1.types.VmwareVmDetails):
            The description of the VM in a Source of type
            Vmware.

            This field is a member of `oneof`_ ``VmDetails``.
        vm_id (str):
            The VM's ID in the source.
        utilization (google.cloud.vmmigration_v1.types.VmUtilizationMetrics):
            Utilization metrics for this VM.
    """

    vmware_vm_details: "VmwareVmDetails" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="VmDetails",
        message="VmwareVmDetails",
    )
    vm_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    utilization: "VmUtilizationMetrics" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="VmUtilizationMetrics",
    )


class VmUtilizationMetrics(proto.Message):
    r"""Utilization metrics values for a single VM.

    Attributes:
        cpu_max_percent (int):
            Max CPU usage, percent.
        cpu_average_percent (int):
            Average CPU usage, percent.
        memory_max_percent (int):
            Max memory usage, percent.
        memory_average_percent (int):
            Average memory usage, percent.
        disk_io_rate_max_kbps (int):
            Max disk IO rate, in kilobytes per second.
        disk_io_rate_average_kbps (int):
            Average disk IO rate, in kilobytes per
            second.
        network_throughput_max_kbps (int):
            Max network throughput (combined
            transmit-rates and receive-rates), in kilobytes
            per second.
        network_throughput_average_kbps (int):
            Average network throughput (combined
            transmit-rates and receive-rates), in kilobytes
            per second.
    """

    cpu_max_percent: int = proto.Field(
        proto.INT32,
        number=9,
    )
    cpu_average_percent: int = proto.Field(
        proto.INT32,
        number=10,
    )
    memory_max_percent: int = proto.Field(
        proto.INT32,
        number=11,
    )
    memory_average_percent: int = proto.Field(
        proto.INT32,
        number=12,
    )
    disk_io_rate_max_kbps: int = proto.Field(
        proto.INT64,
        number=13,
    )
    disk_io_rate_average_kbps: int = proto.Field(
        proto.INT64,
        number=14,
    )
    network_throughput_max_kbps: int = proto.Field(
        proto.INT64,
        number=15,
    )
    network_throughput_average_kbps: int = proto.Field(
        proto.INT64,
        number=16,
    )


class ListUtilizationReportsRequest(proto.Message):
    r"""Request message for 'ListUtilizationReports' request.

    Attributes:
        parent (str):
            Required. The Utilization Reports parent.
        view (google.cloud.vmmigration_v1.types.UtilizationReportView):
            Optional. The level of details of each
            report. Defaults to BASIC.
        page_size (int):
            Optional. The maximum number of reports to
            return. The service may return fewer than this
            value. If unspecified, at most 500 reports will
            be returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            Required. A page token, received from a previous
            ``ListUtilizationReports`` call. Provide this to retrieve
            the subsequent page.

            When paginating, all other parameters provided to
            ``ListUtilizationReports`` must match the call that provided
            the page token.
        filter (str):
            Optional. The filter request.
        order_by (str):
            Optional. the order by fields for the result.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: "UtilizationReportView" = proto.Field(
        proto.ENUM,
        number=2,
        enum="UtilizationReportView",
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=5,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=6,
    )


class ListUtilizationReportsResponse(proto.Message):
    r"""Response message for 'ListUtilizationReports' request.

    Attributes:
        utilization_reports (MutableSequence[google.cloud.vmmigration_v1.types.UtilizationReport]):
            Output only. The list of reports.
        next_page_token (str):
            Output only. A token, which can be sent as ``page_token`` to
            retrieve the next page. If this field is omitted, there are
            no subsequent pages.
        unreachable (MutableSequence[str]):
            Output only. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    utilization_reports: MutableSequence["UtilizationReport"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="UtilizationReport",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetUtilizationReportRequest(proto.Message):
    r"""Request message for 'GetUtilizationReport' request.

    Attributes:
        name (str):
            Required. The Utilization Report name.
        view (google.cloud.vmmigration_v1.types.UtilizationReportView):
            Optional. The level of details of the report.
            Defaults to FULL
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: "UtilizationReportView" = proto.Field(
        proto.ENUM,
        number=2,
        enum="UtilizationReportView",
    )


class CreateUtilizationReportRequest(proto.Message):
    r"""Request message for 'CreateUtilizationReport' request.

    Attributes:
        parent (str):
            Required. The Utilization Report's parent.
        utilization_report (google.cloud.vmmigration_v1.types.UtilizationReport):
            Required. The report to create.
        utilization_report_id (str):
            Required. The ID to use for the report, which will become
            the final component of the reports's resource name.

            This value maximum length is 63 characters, and valid
            characters are /[a-z][0-9]-/. It must start with an english
            letter and must not end with a hyphen.
        request_id (str):
            A request ID to identify requests. Specify a
            unique request ID so that if you must retry your
            request, the server will know to ignore the
            request if it has already been completed. The
            server will guarantee that for at least 60
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
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    utilization_report: "UtilizationReport" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="UtilizationReport",
    )
    utilization_report_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteUtilizationReportRequest(proto.Message):
    r"""Request message for 'DeleteUtilizationReport' request.

    Attributes:
        name (str):
            Required. The Utilization Report name.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes after the first request.

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


class ListDatacenterConnectorsResponse(proto.Message):
    r"""Response message for 'ListDatacenterConnectors' request.

    Attributes:
        datacenter_connectors (MutableSequence[google.cloud.vmmigration_v1.types.DatacenterConnector]):
            Output only. The list of sources response.
        next_page_token (str):
            Output only. A token, which can be sent as ``page_token`` to
            retrieve the next page. If this field is omitted, there are
            no subsequent pages.
        unreachable (MutableSequence[str]):
            Output only. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    datacenter_connectors: MutableSequence["DatacenterConnector"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DatacenterConnector",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetDatacenterConnectorRequest(proto.Message):
    r"""Request message for 'GetDatacenterConnector' request.

    Attributes:
        name (str):
            Required. The name of the
            DatacenterConnector.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateDatacenterConnectorRequest(proto.Message):
    r"""Request message for 'CreateDatacenterConnector' request.

    Attributes:
        parent (str):
            Required. The DatacenterConnector's parent. Required. The
            Source in where the new DatacenterConnector will be created.
            For example:
            ``projects/my-project/locations/us-central1/sources/my-source``
        datacenter_connector_id (str):
            Required. The datacenterConnector identifier.
        datacenter_connector (google.cloud.vmmigration_v1.types.DatacenterConnector):
            Required. The create request body.
        request_id (str):
            A request ID to identify requests. Specify a
            unique request ID so that if you must retry your
            request, the server will know to ignore the
            request if it has already been completed. The
            server will guarantee that for at least 60
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
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    datacenter_connector_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    datacenter_connector: "DatacenterConnector" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="DatacenterConnector",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteDatacenterConnectorRequest(proto.Message):
    r"""Request message for 'DeleteDatacenterConnector' request.

    Attributes:
        name (str):
            Required. The DatacenterConnector name.
        request_id (str):
            A request ID to identify requests. Specify a
            unique request ID so that if you must retry your
            request, the server will know to ignore the
            request if it has already been completed. The
            server will guarantee that for at least 60
            minutes after the first request.

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


class UpgradeApplianceRequest(proto.Message):
    r"""Request message for 'UpgradeAppliance' request.

    Attributes:
        datacenter_connector (str):
            Required. The DatacenterConnector name.
        request_id (str):
            A request ID to identify requests. Specify a
            unique request ID so that if you must retry your
            request, the server will know to ignore the
            request if it has already been completed. The
            server will guarantee that for at least 60
            minutes after the first request.

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

    datacenter_connector: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpgradeApplianceResponse(proto.Message):
    r"""Response message for 'UpgradeAppliance' request."""


class ListDatacenterConnectorsRequest(proto.Message):
    r"""Request message for 'ListDatacenterConnectors' request.

    Attributes:
        parent (str):
            Required. The parent, which owns this
            collection of connectors.
        page_size (int):
            Optional. The maximum number of connectors to
            return. The service may return fewer than this
            value. If unspecified, at most 500 sources will
            be returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            Required. A page token, received from a previous
            ``ListDatacenterConnectors`` call. Provide this to retrieve
            the subsequent page.

            When paginating, all other parameters provided to
            ``ListDatacenterConnectors`` must match the call that
            provided the page token.
        filter (str):
            Optional. The filter request.
        order_by (str):
            Optional. the order by fields for the result.
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


class ComputeEngineTargetDefaults(proto.Message):
    r"""ComputeEngineTargetDefaults is a collection of details for
    creating a VM in a target Compute Engine project.

    Attributes:
        vm_name (str):
            The name of the VM to create.
        target_project (str):
            The full path of the resource of type
            TargetProject which represents the Compute
            Engine project in which to create this VM.
        zone (str):
            The zone in which to create the VM.
        machine_type_series (str):
            The machine type series to create the VM
            with.
        machine_type (str):
            The machine type to create the VM with.
        network_tags (MutableSequence[str]):
            A list of network tags to associate with the
            VM.
        network_interfaces (MutableSequence[google.cloud.vmmigration_v1.types.NetworkInterface]):
            List of NICs connected to this VM.
        service_account (str):
            Optional. The service account to associate
            the VM with.
        disk_type (google.cloud.vmmigration_v1.types.ComputeEngineDiskType):
            The disk type to use in the VM.
        labels (MutableMapping[str, str]):
            A map of labels to associate with the VM.
        license_type (google.cloud.vmmigration_v1.types.ComputeEngineLicenseType):
            The license type to use in OS adaptation.
        applied_license (google.cloud.vmmigration_v1.types.AppliedLicense):
            Output only. The OS license returned from the
            adaptation module report.
        compute_scheduling (google.cloud.vmmigration_v1.types.ComputeScheduling):
            Compute instance scheduling information (if
            empty default is used).
        secure_boot (bool):
            Defines whether the instance has Secure Boot
            enabled. This can be set to true only if the VM
            boot option is EFI.
        enable_vtpm (bool):
            Optional. Defines whether the instance has
            vTPM enabled. This can be set to true only if
            the VM boot option is EFI.
        enable_integrity_monitoring (bool):
            Optional. Defines whether the instance has
            integrity monitoring enabled. This can be set to
            true only if the VM boot option is EFI, and vTPM
            is enabled.
        boot_option (google.cloud.vmmigration_v1.types.ComputeEngineBootOption):
            Output only. The VM Boot Option, as set in
            the source VM.
        metadata (MutableMapping[str, str]):
            The metadata key/value pairs to assign to the
            VM.
        additional_licenses (MutableSequence[str]):
            Additional licenses to assign to the VM.
        hostname (str):
            The hostname to assign to the VM.
        encryption (google.cloud.vmmigration_v1.types.Encryption):
            Optional. Immutable. The encryption to apply
            to the VM disks.
        boot_conversion (google.cloud.vmmigration_v1.types.BootConversion):
            Optional. By default the virtual machine will
            keep its existing boot option. Setting this
            property will trigger an internal process which
            will convert the virtual machine from using the
            existing boot option to another.
        adaptation_modifiers (MutableSequence[google.cloud.vmmigration_v1.types.AdaptationModifier]):
            Optional. AdaptationModifiers are the set of
            modifiers used during OS adaptation.
        disk_replica_zones (MutableSequence[str]):
            Optional. Additional replica zones of the target regional
            disks. If this list is not empty a regional disk will be
            created. The first supported zone would be the one stated in
            the
            [zone][google.cloud.vmmigration.v1.ComputeEngineTargetDefaults.zone]
            field. The rest are taken from this list. Please refer to
            the `regional disk creation
            API <https://cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources>`__
            for further details about regional vs zonal disks. If not
            specified, a zonal disk will be created in the same zone the
            VM is created.
        storage_pool (str):
            Optional. If specified this will be the
            storage pool in which the disk is created. This
            is the full path of the storage pool resource,
            for example:

            "projects/my-project/zones/us-central1-a/storagePools/my-storage-pool".
            The storage pool must be in the same project and
            zone as the target disks. The storage pool's
            type must match the disk type.
    """

    vm_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    target_project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    zone: str = proto.Field(
        proto.STRING,
        number=3,
    )
    machine_type_series: str = proto.Field(
        proto.STRING,
        number=4,
    )
    machine_type: str = proto.Field(
        proto.STRING,
        number=5,
    )
    network_tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    network_interfaces: MutableSequence["NetworkInterface"] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="NetworkInterface",
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=8,
    )
    disk_type: "ComputeEngineDiskType" = proto.Field(
        proto.ENUM,
        number=9,
        enum="ComputeEngineDiskType",
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=10,
    )
    license_type: "ComputeEngineLicenseType" = proto.Field(
        proto.ENUM,
        number=11,
        enum="ComputeEngineLicenseType",
    )
    applied_license: "AppliedLicense" = proto.Field(
        proto.MESSAGE,
        number=12,
        message="AppliedLicense",
    )
    compute_scheduling: "ComputeScheduling" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="ComputeScheduling",
    )
    secure_boot: bool = proto.Field(
        proto.BOOL,
        number=14,
    )
    enable_vtpm: bool = proto.Field(
        proto.BOOL,
        number=21,
    )
    enable_integrity_monitoring: bool = proto.Field(
        proto.BOOL,
        number=22,
    )
    boot_option: "ComputeEngineBootOption" = proto.Field(
        proto.ENUM,
        number=15,
        enum="ComputeEngineBootOption",
    )
    metadata: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=16,
    )
    additional_licenses: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=17,
    )
    hostname: str = proto.Field(
        proto.STRING,
        number=18,
    )
    encryption: "Encryption" = proto.Field(
        proto.MESSAGE,
        number=19,
        message="Encryption",
    )
    boot_conversion: "BootConversion" = proto.Field(
        proto.ENUM,
        number=20,
        enum="BootConversion",
    )
    adaptation_modifiers: MutableSequence["AdaptationModifier"] = proto.RepeatedField(
        proto.MESSAGE,
        number=23,
        message="AdaptationModifier",
    )
    disk_replica_zones: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=24,
    )
    storage_pool: str = proto.Field(
        proto.STRING,
        number=25,
    )


class AdaptationModifier(proto.Message):
    r"""AdaptationModifier a modifier to be used for configuration of
    the OS adaptation process.

    Attributes:
        modifier (str):
            Optional. The modifier name.
        value (str):
            Optional. The value of the modifier.
            The actual value depends on the modifier and can
            also be empty.
    """

    modifier: str = proto.Field(
        proto.STRING,
        number=3,
    )
    value: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ComputeEngineTargetDetails(proto.Message):
    r"""ComputeEngineTargetDetails is a collection of details for
    creating a VM in a target Compute Engine project.

    Attributes:
        vm_name (str):
            The name of the VM to create.
        project (str):
            The Google Cloud target project ID or project
            name.
        zone (str):
            The zone in which to create the VM.
        machine_type_series (str):
            The machine type series to create the VM
            with.
        machine_type (str):
            The machine type to create the VM with.
        network_tags (MutableSequence[str]):
            A list of network tags to associate with the
            VM.
        network_interfaces (MutableSequence[google.cloud.vmmigration_v1.types.NetworkInterface]):
            List of NICs connected to this VM.
        service_account (str):
            The service account to associate the VM with.
        disk_type (google.cloud.vmmigration_v1.types.ComputeEngineDiskType):
            The disk type to use in the VM.
        labels (MutableMapping[str, str]):
            A map of labels to associate with the VM.
        license_type (google.cloud.vmmigration_v1.types.ComputeEngineLicenseType):
            The license type to use in OS adaptation.
        applied_license (google.cloud.vmmigration_v1.types.AppliedLicense):
            The OS license returned from the adaptation
            module report.
        compute_scheduling (google.cloud.vmmigration_v1.types.ComputeScheduling):
            Compute instance scheduling information (if
            empty default is used).
        secure_boot (bool):
            Defines whether the instance has Secure Boot
            enabled. This can be set to true only if the VM
            boot option is EFI.
        enable_vtpm (bool):
            Optional. Defines whether the instance has
            vTPM enabled.
        enable_integrity_monitoring (bool):
            Optional. Defines whether the instance has
            integrity monitoring enabled.
        boot_option (google.cloud.vmmigration_v1.types.ComputeEngineBootOption):
            The VM Boot Option, as set in the source VM.
        metadata (MutableMapping[str, str]):
            The metadata key/value pairs to assign to the
            VM.
        additional_licenses (MutableSequence[str]):
            Additional licenses to assign to the VM.
        hostname (str):
            The hostname to assign to the VM.
        encryption (google.cloud.vmmigration_v1.types.Encryption):
            Optional. The encryption to apply to the VM
            disks.
        boot_conversion (google.cloud.vmmigration_v1.types.BootConversion):
            Optional. By default the virtual machine will
            keep its existing boot option. Setting this
            property will trigger an internal process which
            will convert the virtual machine from using the
            existing boot option to another.
        adaptation_modifiers (MutableSequence[google.cloud.vmmigration_v1.types.AdaptationModifier]):
            Optional. Modifiers to be used as
            configuration of the OS adaptation process.
        disk_replica_zones (MutableSequence[str]):
            Optional. Additional replica zones of the target regional
            disks. If this list is not empty a regional disk will be
            created. The first supported zone would be the one stated in
            the
            [zone][google.cloud.vmmigration.v1.ComputeEngineTargetDetails.zone]
            field. The rest are taken from this list. Please refer to
            the `regional disk creation
            API <https://cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources>`__
            for further details about regional vs zonal disks. If not
            specified, a zonal disk will be created in the same zone the
            VM is created.
        storage_pool (str):
            Optional. The storage pool used for the VM
            disks. If specified this will be the storage
            pool in which the disk is created. This is the
            full path of the storage pool resource, for
            example:

            "projects/my-project/zones/us-central1-a/storagePools/my-storage-pool".
            The storage pool must be in the same project and
            zone as the target disks. The storage pool's
            type must match the disk type.
    """

    vm_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    zone: str = proto.Field(
        proto.STRING,
        number=3,
    )
    machine_type_series: str = proto.Field(
        proto.STRING,
        number=4,
    )
    machine_type: str = proto.Field(
        proto.STRING,
        number=5,
    )
    network_tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    network_interfaces: MutableSequence["NetworkInterface"] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="NetworkInterface",
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=8,
    )
    disk_type: "ComputeEngineDiskType" = proto.Field(
        proto.ENUM,
        number=9,
        enum="ComputeEngineDiskType",
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=10,
    )
    license_type: "ComputeEngineLicenseType" = proto.Field(
        proto.ENUM,
        number=11,
        enum="ComputeEngineLicenseType",
    )
    applied_license: "AppliedLicense" = proto.Field(
        proto.MESSAGE,
        number=12,
        message="AppliedLicense",
    )
    compute_scheduling: "ComputeScheduling" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="ComputeScheduling",
    )
    secure_boot: bool = proto.Field(
        proto.BOOL,
        number=14,
    )
    enable_vtpm: bool = proto.Field(
        proto.BOOL,
        number=21,
    )
    enable_integrity_monitoring: bool = proto.Field(
        proto.BOOL,
        number=22,
    )
    boot_option: "ComputeEngineBootOption" = proto.Field(
        proto.ENUM,
        number=15,
        enum="ComputeEngineBootOption",
    )
    metadata: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=16,
    )
    additional_licenses: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=17,
    )
    hostname: str = proto.Field(
        proto.STRING,
        number=18,
    )
    encryption: "Encryption" = proto.Field(
        proto.MESSAGE,
        number=19,
        message="Encryption",
    )
    boot_conversion: "BootConversion" = proto.Field(
        proto.ENUM,
        number=20,
        enum="BootConversion",
    )
    adaptation_modifiers: MutableSequence["AdaptationModifier"] = proto.RepeatedField(
        proto.MESSAGE,
        number=23,
        message="AdaptationModifier",
    )
    disk_replica_zones: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=24,
    )
    storage_pool: str = proto.Field(
        proto.STRING,
        number=25,
    )


class NetworkInterface(proto.Message):
    r"""NetworkInterface represents a NIC of a VM.

    Attributes:
        network (str):
            Optional. The network to connect the NIC to.
        subnetwork (str):
            Optional. The subnetwork to connect the NIC
            to.
        internal_ip (str):
            Optional. The internal IP to define in the NIC. The formats
            accepted are: ``ephemeral`` \\ ipv4 address \\ a named
            address resource full path.
        external_ip (str):
            Optional. The external IP to define in the
            NIC.
        network_tier (google.cloud.vmmigration_v1.types.ComputeEngineNetworkTier):
            Optional. The networking tier used for
            optimizing connectivity between instances and
            systems on the internet. Applies only for
            external ephemeral IP addresses. If left empty,
            will default to PREMIUM.
    """

    network: str = proto.Field(
        proto.STRING,
        number=1,
    )
    subnetwork: str = proto.Field(
        proto.STRING,
        number=2,
    )
    internal_ip: str = proto.Field(
        proto.STRING,
        number=3,
    )
    external_ip: str = proto.Field(
        proto.STRING,
        number=4,
    )
    network_tier: "ComputeEngineNetworkTier" = proto.Field(
        proto.ENUM,
        number=5,
        enum="ComputeEngineNetworkTier",
    )


class AppliedLicense(proto.Message):
    r"""AppliedLicense holds the license data returned by adaptation
    module report.

    Attributes:
        type_ (google.cloud.vmmigration_v1.types.AppliedLicense.Type):
            The license type that was used in OS
            adaptation.
        os_license (str):
            The OS license returned from the adaptation
            module's report.
    """

    class Type(proto.Enum):
        r"""License types used in OS adaptation.

        Values:
            TYPE_UNSPECIFIED (0):
                Unspecified license for the OS.
            NONE (1):
                No license available for the OS.
            PAYG (2):
                The license type is Pay As You Go license
                type.
            BYOL (3):
                The license type is Bring Your Own License
                type.
        """

        TYPE_UNSPECIFIED = 0
        NONE = 1
        PAYG = 2
        BYOL = 3

    type_: Type = proto.Field(
        proto.ENUM,
        number=1,
        enum=Type,
    )
    os_license: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SchedulingNodeAffinity(proto.Message):
    r"""Node Affinity: the configuration of desired nodes onto which
    this Instance could be scheduled. Based on
    https://cloud.google.com/compute/docs/reference/rest/v1/instances/setScheduling

    Attributes:
        key (str):
            The label key of Node resource to reference.
        operator (google.cloud.vmmigration_v1.types.SchedulingNodeAffinity.Operator):
            The operator to use for the node resources specified in the
            ``values`` parameter.
        values (MutableSequence[str]):
            Corresponds to the label values of Node
            resource.
    """

    class Operator(proto.Enum):
        r"""Possible types of node selection operators. Valid operators are IN
        for affinity and NOT_IN for anti-affinity.

        Values:
            OPERATOR_UNSPECIFIED (0):
                An unknown, unexpected behavior.
            IN (1):
                The node resource group should be in these
                resources affinity.
            NOT_IN (2):
                The node resource group should not be in
                these resources affinity.
        """

        OPERATOR_UNSPECIFIED = 0
        IN = 1
        NOT_IN = 2

    key: str = proto.Field(
        proto.STRING,
        number=1,
    )
    operator: Operator = proto.Field(
        proto.ENUM,
        number=2,
        enum=Operator,
    )
    values: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class ComputeScheduling(proto.Message):
    r"""Scheduling information for VM on maintenance/restart
    behaviour and node allocation in sole tenant nodes. Options for
    instance behavior when the host machine undergoes maintenance
    that may temporarily impact instance performance.

    Attributes:
        on_host_maintenance (google.cloud.vmmigration_v1.types.ComputeScheduling.OnHostMaintenance):
            How the instance should behave when the host
            machine undergoes maintenance that may
            temporarily impact instance performance.
        restart_type (google.cloud.vmmigration_v1.types.ComputeScheduling.RestartType):
            Whether the Instance should be automatically restarted
            whenever it is terminated by Compute Engine (not terminated
            by user). This configuration is identical to
            ``automaticRestart`` field in Compute Engine create instance
            under scheduling. It was changed to an enum (instead of a
            boolean) to match the default value in Compute Engine which
            is automatic restart.
        node_affinities (MutableSequence[google.cloud.vmmigration_v1.types.SchedulingNodeAffinity]):
            A set of node affinity and anti-affinity
            configurations for sole tenant nodes.
        min_node_cpus (int):
            The minimum number of virtual CPUs this instance will
            consume when running on a sole-tenant node. Ignored if no
            node_affinites are configured.
    """

    class OnHostMaintenance(proto.Enum):
        r"""

        Values:
            ON_HOST_MAINTENANCE_UNSPECIFIED (0):
                An unknown, unexpected behavior.
            TERMINATE (1):
                Terminate the instance when the host machine
                undergoes maintenance.
            MIGRATE (2):
                Migrate the instance when the host machine
                undergoes maintenance.
        """

        ON_HOST_MAINTENANCE_UNSPECIFIED = 0
        TERMINATE = 1
        MIGRATE = 2

    class RestartType(proto.Enum):
        r"""Defines whether the Instance should be automatically
        restarted whenever it is terminated by Compute Engine (not
        terminated by user).

        Values:
            RESTART_TYPE_UNSPECIFIED (0):
                Unspecified behavior. This will use the
                default.
            AUTOMATIC_RESTART (1):
                The Instance should be automatically
                restarted whenever it is terminated by Compute
                Engine.
            NO_AUTOMATIC_RESTART (2):
                The Instance isn't automatically restarted
                whenever it is terminated by Compute Engine.
        """

        RESTART_TYPE_UNSPECIFIED = 0
        AUTOMATIC_RESTART = 1
        NO_AUTOMATIC_RESTART = 2

    on_host_maintenance: OnHostMaintenance = proto.Field(
        proto.ENUM,
        number=1,
        enum=OnHostMaintenance,
    )
    restart_type: RestartType = proto.Field(
        proto.ENUM,
        number=5,
        enum=RestartType,
    )
    node_affinities: MutableSequence["SchedulingNodeAffinity"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="SchedulingNodeAffinity",
    )
    min_node_cpus: int = proto.Field(
        proto.INT32,
        number=4,
    )


class ComputeEngineDisksTargetDefaults(proto.Message):
    r"""ComputeEngineDisksTargetDefaults is a collection of details
    for creating Persistent Disks in a target Compute Engine
    project.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        zone (str):
            The zone in which to create the Persistent
            Disks.

            This field is a member of `oneof`_ ``location``.
        disks_target_defaults (google.cloud.vmmigration_v1.types.DisksMigrationDisksTargetDefaults):
            Details of the disk only migration target.

            This field is a member of `oneof`_ ``vm_target``.
        vm_target_defaults (google.cloud.vmmigration_v1.types.DisksMigrationVmTargetDefaults):
            Details of the VM migration target.

            This field is a member of `oneof`_ ``vm_target``.
        target_project (str):
            The full path of the resource of type
            TargetProject which represents the Compute
            Engine project in which to create the Persistent
            Disks.
        disks (MutableSequence[google.cloud.vmmigration_v1.types.PersistentDiskDefaults]):
            The details of each Persistent Disk to
            create.
    """

    zone: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="location",
    )
    disks_target_defaults: "DisksMigrationDisksTargetDefaults" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="vm_target",
        message="DisksMigrationDisksTargetDefaults",
    )
    vm_target_defaults: "DisksMigrationVmTargetDefaults" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="vm_target",
        message="DisksMigrationVmTargetDefaults",
    )
    target_project: str = proto.Field(
        proto.STRING,
        number=1,
    )
    disks: MutableSequence["PersistentDiskDefaults"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="PersistentDiskDefaults",
    )


class PersistentDiskDefaults(proto.Message):
    r"""Details for creation of a Persistent Disk.

    Attributes:
        source_disk_number (int):
            Required. The ordinal number of the source VM
            disk.
        disk_name (str):
            Optional. The name of the Persistent Disk to
            create.
        disk_type (google.cloud.vmmigration_v1.types.ComputeEngineDiskType):
            The disk type to use.
        additional_labels (MutableMapping[str, str]):
            A map of labels to associate with the
            Persistent Disk.
        encryption (google.cloud.vmmigration_v1.types.Encryption):
            Optional. The encryption to apply to the
            disk.
        vm_attachment_details (google.cloud.vmmigration_v1.types.VmAttachmentDetails):
            Optional. Details for attachment of the disk
            to a VM. Used when the disk is set to be
            attached to a target VM.
    """

    source_disk_number: int = proto.Field(
        proto.INT32,
        number=1,
    )
    disk_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    disk_type: "ComputeEngineDiskType" = proto.Field(
        proto.ENUM,
        number=3,
        enum="ComputeEngineDiskType",
    )
    additional_labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    encryption: "Encryption" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="Encryption",
    )
    vm_attachment_details: "VmAttachmentDetails" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="VmAttachmentDetails",
    )


class VmAttachmentDetails(proto.Message):
    r"""Details for attachment of the disk to a VM.

    Attributes:
        device_name (str):
            Optional. Specifies a unique device name of your choice that
            is reflected into the /dev/disk/by-id/google-\* tree of a
            Linux operating system running within the instance. If not
            specified, the server chooses a default device name to apply
            to this disk, in the form persistent-disk-x, where x is a
            number assigned by Google Compute Engine. This field is only
            applicable for persistent disks.
    """

    device_name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DisksMigrationDisksTargetDefaults(proto.Message):
    r"""Details for a disk only migration."""


class DisksMigrationVmTargetDefaults(proto.Message):
    r"""Details for creation of a VM that migrated data disks will be
    attached to.

    Attributes:
        vm_name (str):
            Required. The name of the VM to create.
        machine_type_series (str):
            Optional. The machine type series to create
            the VM with. For presentation only.
        machine_type (str):
            Required. The machine type to create the VM
            with.
        network_tags (MutableSequence[str]):
            Optional. A list of network tags to associate
            with the VM.
        network_interfaces (MutableSequence[google.cloud.vmmigration_v1.types.NetworkInterface]):
            Optional. NICs to attach to the VM.
        service_account (str):
            Optional. The service account to associate
            the VM with.
        compute_scheduling (google.cloud.vmmigration_v1.types.ComputeScheduling):
            Optional. Compute instance scheduling
            information (if empty default is used).
        secure_boot (bool):
            Optional. Defines whether the instance has
            Secure Boot enabled. This can be set to true
            only if the VM boot option is EFI.
        enable_vtpm (bool):
            Optional. Defines whether the instance has
            vTPM enabled.
        enable_integrity_monitoring (bool):
            Optional. Defines whether the instance has
            integrity monitoring enabled.
        metadata (MutableMapping[str, str]):
            Optional. The metadata key/value pairs to
            assign to the VM.
        additional_licenses (MutableSequence[str]):
            Optional. Additional licenses to assign to
            the VM.
        hostname (str):
            Optional. The hostname to assign to the VM.
        labels (MutableMapping[str, str]):
            Optional. A map of labels to associate with
            the VM.
        boot_disk_defaults (google.cloud.vmmigration_v1.types.BootDiskDefaults):
            Optional. Details of the boot disk of the VM.
        encryption (google.cloud.vmmigration_v1.types.Encryption):
            Optional. The encryption to apply to the VM.
    """

    vm_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    machine_type_series: str = proto.Field(
        proto.STRING,
        number=2,
    )
    machine_type: str = proto.Field(
        proto.STRING,
        number=3,
    )
    network_tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    network_interfaces: MutableSequence["NetworkInterface"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="NetworkInterface",
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=6,
    )
    compute_scheduling: "ComputeScheduling" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="ComputeScheduling",
    )
    secure_boot: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    enable_vtpm: bool = proto.Field(
        proto.BOOL,
        number=16,
    )
    enable_integrity_monitoring: bool = proto.Field(
        proto.BOOL,
        number=17,
    )
    metadata: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=10,
    )
    additional_licenses: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=11,
    )
    hostname: str = proto.Field(
        proto.STRING,
        number=12,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=13,
    )
    boot_disk_defaults: "BootDiskDefaults" = proto.Field(
        proto.MESSAGE,
        number=14,
        message="BootDiskDefaults",
    )
    encryption: "Encryption" = proto.Field(
        proto.MESSAGE,
        number=15,
        message="Encryption",
    )


class BootDiskDefaults(proto.Message):
    r"""BootDiskDefaults hold information about the boot disk of a
    VM.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        image (google.cloud.vmmigration_v1.types.BootDiskDefaults.DiskImageDefaults):
            The image to use when creating the disk.

            This field is a member of `oneof`_ ``source``.
        disk_name (str):
            Optional. The name of the disk.
        disk_type (google.cloud.vmmigration_v1.types.ComputeEngineDiskType):
            Optional. The type of disk provisioning to
            use for the VM.
        device_name (str):
            Optional. Specifies a unique device name of your choice that
            is reflected into the /dev/disk/by-id/google-\* tree of a
            Linux operating system running within the instance. If not
            specified, the server chooses a default device name to apply
            to this disk, in the form persistent-disk-x, where x is a
            number assigned by Google Compute Engine. This field is only
            applicable for persistent disks.
        encryption (google.cloud.vmmigration_v1.types.Encryption):
            Optional. The encryption to apply to the boot
            disk.
    """

    class DiskImageDefaults(proto.Message):
        r"""Contains details about the image source used to create the
        disk.

        Attributes:
            source_image (str):
                Required. The Image resource used when
                creating the disk.
        """

        source_image: str = proto.Field(
            proto.STRING,
            number=1,
        )

    image: DiskImageDefaults = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="source",
        message=DiskImageDefaults,
    )
    disk_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    disk_type: "ComputeEngineDiskType" = proto.Field(
        proto.ENUM,
        number=2,
        enum="ComputeEngineDiskType",
    )
    device_name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    encryption: "Encryption" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="Encryption",
    )


class ComputeEngineDisksTargetDetails(proto.Message):
    r"""ComputeEngineDisksTargetDetails is a collection of created
    Persistent Disks details.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        disks_target_details (google.cloud.vmmigration_v1.types.DisksMigrationDisksTargetDetails):
            Details of the disks-only migration target.

            This field is a member of `oneof`_ ``vm_target``.
        vm_target_details (google.cloud.vmmigration_v1.types.DisksMigrationVmTargetDetails):
            Details for the VM the migrated data disks
            are attached to.

            This field is a member of `oneof`_ ``vm_target``.
        disks (MutableSequence[google.cloud.vmmigration_v1.types.PersistentDisk]):
            The details of each created Persistent Disk.
    """

    disks_target_details: "DisksMigrationDisksTargetDetails" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="vm_target",
        message="DisksMigrationDisksTargetDetails",
    )
    vm_target_details: "DisksMigrationVmTargetDetails" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="vm_target",
        message="DisksMigrationVmTargetDetails",
    )
    disks: MutableSequence["PersistentDisk"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="PersistentDisk",
    )


class PersistentDisk(proto.Message):
    r"""Details of a created Persistent Disk.

    Attributes:
        source_disk_number (int):
            The ordinal number of the source VM disk.
        disk_uri (str):
            The URI of the Persistent Disk.
    """

    source_disk_number: int = proto.Field(
        proto.INT32,
        number=1,
    )
    disk_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DisksMigrationDisksTargetDetails(proto.Message):
    r"""Details for a disks-only migration."""


class DisksMigrationVmTargetDetails(proto.Message):
    r"""Details for the VM created VM as part of disks migration.

    Attributes:
        vm_uri (str):
            Output only. The URI of the Compute Engine
            VM.
    """

    vm_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SchedulePolicy(proto.Message):
    r"""A policy for scheduling replications.

    Attributes:
        idle_duration (google.protobuf.duration_pb2.Duration):
            The idle duration between replication stages.
        skip_os_adaptation (bool):
            A flag to indicate whether to skip OS
            adaptation during the replication sync. OS
            adaptation is a process where the VM's operating
            system undergoes changes and adaptations to
            fully function on Compute Engine.
    """

    idle_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=1,
        message=duration_pb2.Duration,
    )
    skip_os_adaptation: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class CreateMigratingVmRequest(proto.Message):
    r"""Request message for 'CreateMigratingVm' request.

    Attributes:
        parent (str):
            Required. The MigratingVm's parent.
        migrating_vm_id (str):
            Required. The migratingVm identifier.
        migrating_vm (google.cloud.vmmigration_v1.types.MigratingVm):
            Required. The create request body.
        request_id (str):
            A request ID to identify requests. Specify a
            unique request ID so that if you must retry your
            request, the server will know to ignore the
            request if it has already been completed. The
            server will guarantee that for at least 60
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
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    migrating_vm_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    migrating_vm: "MigratingVm" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="MigratingVm",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListMigratingVmsRequest(proto.Message):
    r"""Request message for 'LisMigratingVmsRequest' request.

    Attributes:
        parent (str):
            Required. The parent, which owns this
            collection of MigratingVms.
        page_size (int):
            Optional. The maximum number of migrating VMs
            to return. The service may return fewer than
            this value. If unspecified, at most 500
            migrating VMs will be returned. The maximum
            value is 1000; values above 1000 will be coerced
            to 1000.
        page_token (str):
            Required. A page token, received from a previous
            ``ListMigratingVms`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListMigratingVms`` must match the call that provided the
            page token.
        filter (str):
            Optional. The filter request.
        order_by (str):
            Optional. the order by fields for the result.
        view (google.cloud.vmmigration_v1.types.MigratingVmView):
            Optional. The level of details of each
            migrating VM.
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
    view: "MigratingVmView" = proto.Field(
        proto.ENUM,
        number=6,
        enum="MigratingVmView",
    )


class ListMigratingVmsResponse(proto.Message):
    r"""Response message for 'ListMigratingVms' request.

    Attributes:
        migrating_vms (MutableSequence[google.cloud.vmmigration_v1.types.MigratingVm]):
            Output only. The list of Migrating VMs
            response.
        next_page_token (str):
            Output only. A token, which can be sent as ``page_token`` to
            retrieve the next page. If this field is omitted, there are
            no subsequent pages.
        unreachable (MutableSequence[str]):
            Output only. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    migrating_vms: MutableSequence["MigratingVm"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="MigratingVm",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetMigratingVmRequest(proto.Message):
    r"""Request message for 'GetMigratingVm' request.

    Attributes:
        name (str):
            Required. The name of the MigratingVm.
        view (google.cloud.vmmigration_v1.types.MigratingVmView):
            Optional. The level of details of the
            migrating VM.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: "MigratingVmView" = proto.Field(
        proto.ENUM,
        number=2,
        enum="MigratingVmView",
    )


class UpdateMigratingVmRequest(proto.Message):
    r"""Request message for 'UpdateMigratingVm' request.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Field mask is used to specify the fields to be overwritten
            in the MigratingVm resource by the update. The fields
            specified in the update_mask are relative to the resource,
            not the full request. A field will be overwritten if it is
            in the mask. If the user does not provide a mask then all
            fields will be overwritten.
        migrating_vm (google.cloud.vmmigration_v1.types.MigratingVm):
            Required. The update request body.
        request_id (str):
            A request ID to identify requests. Specify a
            unique request ID so that if you must retry your
            request, the server will know to ignore the
            request if it has already been completed. The
            server will guarantee that for at least 60
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
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    migrating_vm: "MigratingVm" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="MigratingVm",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteMigratingVmRequest(proto.Message):
    r"""Request message for 'DeleteMigratingVm' request.

    Attributes:
        name (str):
            Required. The name of the MigratingVm.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class StartMigrationRequest(proto.Message):
    r"""Request message for 'StartMigrationRequest' request.

    Attributes:
        migrating_vm (str):
            Required. The name of the MigratingVm.
    """

    migrating_vm: str = proto.Field(
        proto.STRING,
        number=1,
    )


class StartMigrationResponse(proto.Message):
    r"""Response message for 'StartMigration' request."""


class PauseMigrationRequest(proto.Message):
    r"""Request message for 'PauseMigration' request.

    Attributes:
        migrating_vm (str):
            Required. The name of the MigratingVm.
    """

    migrating_vm: str = proto.Field(
        proto.STRING,
        number=1,
    )


class PauseMigrationResponse(proto.Message):
    r"""Response message for 'PauseMigration' request."""


class ResumeMigrationRequest(proto.Message):
    r"""Request message for 'ResumeMigration' request.

    Attributes:
        migrating_vm (str):
            Required. The name of the MigratingVm.
    """

    migrating_vm: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ResumeMigrationResponse(proto.Message):
    r"""Response message for 'ResumeMigration' request."""


class FinalizeMigrationRequest(proto.Message):
    r"""Request message for 'FinalizeMigration' request.

    Attributes:
        migrating_vm (str):
            Required. The name of the MigratingVm.
    """

    migrating_vm: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ExtendMigrationRequest(proto.Message):
    r"""Request message for 'ExtendMigrationRequest' request.

    Attributes:
        migrating_vm (str):
            Required. The name of the MigratingVm.
    """

    migrating_vm: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ExtendMigrationResponse(proto.Message):
    r"""Response message for 'ExtendMigration' request."""


class FinalizeMigrationResponse(proto.Message):
    r"""Response message for 'FinalizeMigration' request."""


class TargetProject(proto.Message):
    r"""TargetProject message represents a target Compute Engine
    project for a migration or a clone.

    Attributes:
        name (str):
            Output only. The name of the target project.
        project (str):
            Required. The target project ID (number) or
            project name.
        description (str):
            The target project's description.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time this target project
            resource was created (not related to when the
            Compute Engine project it points to was
            created).
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last time the target project
            resource was updated.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )


class GetTargetProjectRequest(proto.Message):
    r"""Request message for 'GetTargetProject' call.

    Attributes:
        name (str):
            Required. The TargetProject name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListTargetProjectsRequest(proto.Message):
    r"""Request message for 'ListTargetProjects' call.

    Attributes:
        parent (str):
            Required. The parent, which owns this
            collection of targets.
        page_size (int):
            Optional. The maximum number of targets to
            return. The service may return fewer than this
            value. If unspecified, at most 500 targets will
            be returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            Required. A page token, received from a previous
            ``ListTargets`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListTargets`` must match the call that provided the page
            token.
        filter (str):
            Optional. The filter request.
        order_by (str):
            Optional. the order by fields for the result.
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


class ListTargetProjectsResponse(proto.Message):
    r"""Response message for 'ListTargetProjects' call.

    Attributes:
        target_projects (MutableSequence[google.cloud.vmmigration_v1.types.TargetProject]):
            Output only. The list of target response.
        next_page_token (str):
            Output only. A token, which can be sent as ``page_token`` to
            retrieve the next page. If this field is omitted, there are
            no subsequent pages.
        unreachable (MutableSequence[str]):
            Output only. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    target_projects: MutableSequence["TargetProject"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="TargetProject",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class CreateTargetProjectRequest(proto.Message):
    r"""Request message for 'CreateTargetProject' request.

    Attributes:
        parent (str):
            Required. The TargetProject's parent.
        target_project_id (str):
            Required. The target_project identifier.
        target_project (google.cloud.vmmigration_v1.types.TargetProject):
            Required. The create request body.
        request_id (str):
            A request ID to identify requests. Specify a
            unique request ID so that if you must retry your
            request, the server will know to ignore the
            request if it has already been completed. The
            server will guarantee that for at least 60
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
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    target_project_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    target_project: "TargetProject" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="TargetProject",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateTargetProjectRequest(proto.Message):
    r"""Update message for 'UpdateTargetProject' request.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Field mask is used to specify the fields to be overwritten
            in the TargetProject resource by the update. The fields
            specified in the update_mask are relative to the resource,
            not the full request. A field will be overwritten if it is
            in the mask. If the user does not provide a mask then all
            fields will be overwritten.
        target_project (google.cloud.vmmigration_v1.types.TargetProject):
            Required. The update request body.
        request_id (str):
            A request ID to identify requests. Specify a
            unique request ID so that if you must retry your
            request, the server will know to ignore the
            request if it has already been completed. The
            server will guarantee that for at least 60
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
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    target_project: "TargetProject" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="TargetProject",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteTargetProjectRequest(proto.Message):
    r"""Request message for 'DeleteTargetProject' request.

    Attributes:
        name (str):
            Required. The TargetProject name.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes after the first request.

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


class Group(proto.Message):
    r"""Describes message for 'Group' resource. The Group is a
    collections of several MigratingVms.

    Attributes:
        name (str):
            Output only. The Group name.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The create time timestamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The update time timestamp.
        description (str):
            User-provided description of the group.
        display_name (str):
            Display name is a user defined name for this
            group which can be updated.
        migration_target_type (google.cloud.vmmigration_v1.types.Group.MigrationTargetType):
            Immutable. The target type of this group.
    """

    class MigrationTargetType(proto.Enum):
        r"""The possible types of the group.

        Values:
            MIGRATION_TARGET_TYPE_UNSPECIFIED (0):
                Group type is not specified. This defaults to
                Compute Engine targets.
            MIGRATION_TARGET_TYPE_GCE (1):
                All MigratingVMs in the group must have
                Compute Engine targets.
            MIGRATION_TARGET_TYPE_DISKS (2):
                All MigratingVMs in the group must have
                Compute Engine Disks targets.
        """

        MIGRATION_TARGET_TYPE_UNSPECIFIED = 0
        MIGRATION_TARGET_TYPE_GCE = 1
        MIGRATION_TARGET_TYPE_DISKS = 2

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
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    migration_target_type: MigrationTargetType = proto.Field(
        proto.ENUM,
        number=6,
        enum=MigrationTargetType,
    )


class ListGroupsRequest(proto.Message):
    r"""Request message for 'ListGroups' request.

    Attributes:
        parent (str):
            Required. The parent, which owns this
            collection of groups.
        page_size (int):
            Optional. The maximum number of groups to
            return. The service may return fewer than this
            value. If unspecified, at most 500 groups will
            be returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            Required. A page token, received from a previous
            ``ListGroups`` call. Provide this to retrieve the subsequent
            page.

            When paginating, all other parameters provided to
            ``ListGroups`` must match the call that provided the page
            token.
        filter (str):
            Optional. The filter request.
        order_by (str):
            Optional. the order by fields for the result.
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
    r"""Response message for 'ListGroups' request.

    Attributes:
        groups (MutableSequence[google.cloud.vmmigration_v1.types.Group]):
            Output only. The list of groups response.
        next_page_token (str):
            Output only. A token, which can be sent as ``page_token`` to
            retrieve the next page. If this field is omitted, there are
            no subsequent pages.
        unreachable (MutableSequence[str]):
            Output only. Locations that could not be
            reached.
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
    r"""Request message for 'GetGroup' request.

    Attributes:
        name (str):
            Required. The group name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateGroupRequest(proto.Message):
    r"""Request message for 'CreateGroup' request.

    Attributes:
        parent (str):
            Required. The Group's parent.
        group_id (str):
            Required. The group identifier.
        group (google.cloud.vmmigration_v1.types.Group):
            Required. The create request body.
        request_id (str):
            A request ID to identify requests. Specify a
            unique request ID so that if you must retry your
            request, the server will know to ignore the
            request if it has already been completed. The
            server will guarantee that for at least 60
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
    r"""Update message for 'UpdateGroups' request.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Field mask is used to specify the fields to be overwritten
            in the Group resource by the update. The fields specified in
            the update_mask are relative to the resource, not the full
            request. A field will be overwritten if it is in the mask.
            If the user does not provide a mask then all fields will be
            overwritten.
        group (google.cloud.vmmigration_v1.types.Group):
            Required. The update request body.
        request_id (str):
            A request ID to identify requests. Specify a
            unique request ID so that if you must retry your
            request, the server will know to ignore the
            request if it has already been completed. The
            server will guarantee that for at least 60
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
    r"""Request message for 'DeleteGroup' request.

    Attributes:
        name (str):
            Required. The Group name.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes after the first request.

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


class AddGroupMigrationRequest(proto.Message):
    r"""Request message for 'AddGroupMigration' request.

    Attributes:
        group (str):
            Required. The full path name of the Group to
            add to.
        migrating_vm (str):
            The full path name of the MigratingVm to add.
    """

    group: str = proto.Field(
        proto.STRING,
        number=1,
    )
    migrating_vm: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AddGroupMigrationResponse(proto.Message):
    r"""Response message for 'AddGroupMigration' request."""


class RemoveGroupMigrationRequest(proto.Message):
    r"""Request message for 'RemoveMigration' request.

    Attributes:
        group (str):
            Required. The name of the Group.
        migrating_vm (str):
            The MigratingVm to remove.
    """

    group: str = proto.Field(
        proto.STRING,
        number=1,
    )
    migrating_vm: str = proto.Field(
        proto.STRING,
        number=2,
    )


class RemoveGroupMigrationResponse(proto.Message):
    r"""Response message for 'RemoveMigration' request."""


class CreateCutoverJobRequest(proto.Message):
    r"""Request message for 'CreateCutoverJob' request.

    Attributes:
        parent (str):
            Required. The Cutover's parent.
        cutover_job_id (str):
            Required. The cutover job identifier.
        cutover_job (google.cloud.vmmigration_v1.types.CutoverJob):
            Required. The cutover request body.
        request_id (str):
            A request ID to identify requests. Specify a
            unique request ID so that if you must retry your
            request, the server will know to ignore the
            request if it has already been completed. The
            server will guarantee that for at least 60
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
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cutover_job_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    cutover_job: "CutoverJob" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="CutoverJob",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class CancelCutoverJobRequest(proto.Message):
    r"""Request message for 'CancelCutoverJob' request.

    Attributes:
        name (str):
            Required. The cutover job id
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CancelCutoverJobResponse(proto.Message):
    r"""Response message for 'CancelCutoverJob' request."""


class ListCutoverJobsRequest(proto.Message):
    r"""Request message for 'ListCutoverJobsRequest' request.

    Attributes:
        parent (str):
            Required. The parent, which owns this
            collection of migrating VMs.
        page_size (int):
            Optional. The maximum number of cutover jobs
            to return. The service may return fewer than
            this value. If unspecified, at most 500 cutover
            jobs will be returned. The maximum value is
            1000; values above 1000 will be coerced to 1000.
        page_token (str):
            Required. A page token, received from a previous
            ``ListCutoverJobs`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListCutoverJobs`` must match the call that provided the
            page token.
        filter (str):
            Optional. The filter request.
        order_by (str):
            Optional. the order by fields for the result.
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


class ListCutoverJobsResponse(proto.Message):
    r"""Response message for 'ListCutoverJobs' request.

    Attributes:
        cutover_jobs (MutableSequence[google.cloud.vmmigration_v1.types.CutoverJob]):
            Output only. The list of cutover jobs
            response.
        next_page_token (str):
            Output only. A token, which can be sent as ``page_token`` to
            retrieve the next page. If this field is omitted, there are
            no subsequent pages.
        unreachable (MutableSequence[str]):
            Output only. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    cutover_jobs: MutableSequence["CutoverJob"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="CutoverJob",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetCutoverJobRequest(proto.Message):
    r"""Request message for 'GetCutoverJob' request.

    Attributes:
        name (str):
            Required. The name of the CutoverJob.
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


class MigrationError(proto.Message):
    r"""Represents migration resource error information that can be
    used with google.rpc.Status message. MigrationError is used to
    present the user with error information in migration operations.

    Attributes:
        code (google.cloud.vmmigration_v1.types.MigrationError.ErrorCode):
            Output only. The error code.
        error_message (google.rpc.error_details_pb2.LocalizedMessage):
            Output only. The localized error message.
        action_item (google.rpc.error_details_pb2.LocalizedMessage):
            Output only. Suggested action for solving the
            error.
        help_links (MutableSequence[google.rpc.error_details_pb2.Link]):
            Output only. URL(s) pointing to additional
            information on handling the current error.
        error_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the error occurred.
    """

    class ErrorCode(proto.Enum):
        r"""Represents resource error codes.

        Values:
            ERROR_CODE_UNSPECIFIED (0):
                Default value. This value is not used.
            UNKNOWN_ERROR (1):
                Migrate to Virtual Machines encountered an
                unknown error.
            SOURCE_VALIDATION_ERROR (2):
                Migrate to Virtual Machines encountered an
                error while validating replication source
                health.
            SOURCE_REPLICATION_ERROR (3):
                Migrate to Virtual Machines encountered an
                error during source data operation.
            TARGET_REPLICATION_ERROR (4):
                Migrate to Virtual Machines encountered an
                error during target data operation.
            OS_ADAPTATION_ERROR (5):
                Migrate to Virtual Machines encountered an
                error during OS adaptation.
            CLONE_ERROR (6):
                Migrate to Virtual Machines encountered an
                error in clone operation.
            CUTOVER_ERROR (7):
                Migrate to Virtual Machines encountered an
                error in cutover operation.
            UTILIZATION_REPORT_ERROR (8):
                Migrate to Virtual Machines encountered an
                error during utilization report creation.
            APPLIANCE_UPGRADE_ERROR (9):
                Migrate to Virtual Machines encountered an
                error during appliance upgrade.
            IMAGE_IMPORT_ERROR (10):
                Migrate to Virtual Machines encountered an
                error in image import operation.
            DISK_MIGRATION_ERROR (11):
                Migrate to Virtual Machines encountered an
                error in disk migration operation.
        """

        ERROR_CODE_UNSPECIFIED = 0
        UNKNOWN_ERROR = 1
        SOURCE_VALIDATION_ERROR = 2
        SOURCE_REPLICATION_ERROR = 3
        TARGET_REPLICATION_ERROR = 4
        OS_ADAPTATION_ERROR = 5
        CLONE_ERROR = 6
        CUTOVER_ERROR = 7
        UTILIZATION_REPORT_ERROR = 8
        APPLIANCE_UPGRADE_ERROR = 9
        IMAGE_IMPORT_ERROR = 10
        DISK_MIGRATION_ERROR = 11

    code: ErrorCode = proto.Field(
        proto.ENUM,
        number=1,
        enum=ErrorCode,
    )
    error_message: error_details_pb2.LocalizedMessage = proto.Field(
        proto.MESSAGE,
        number=2,
        message=error_details_pb2.LocalizedMessage,
    )
    action_item: error_details_pb2.LocalizedMessage = proto.Field(
        proto.MESSAGE,
        number=3,
        message=error_details_pb2.LocalizedMessage,
    )
    help_links: MutableSequence[error_details_pb2.Help.Link] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=error_details_pb2.Help.Link,
    )
    error_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )


class MigrationWarning(proto.Message):
    r"""Represents migration resource warning information that can be
    used with google.rpc.Status message. MigrationWarning is used to
    present the user with warning information in migration
    operations.

    Attributes:
        code (google.cloud.vmmigration_v1.types.MigrationWarning.WarningCode):
            The warning code.
        warning_message (google.rpc.error_details_pb2.LocalizedMessage):
            Output only. The localized warning message.
        action_item (google.rpc.error_details_pb2.LocalizedMessage):
            Output only. Suggested action for solving the
            warning.
        help_links (MutableSequence[google.rpc.error_details_pb2.Link]):
            Output only. URL(s) pointing to additional
            information on handling the current warning.
        warning_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the warning occurred.
    """

    class WarningCode(proto.Enum):
        r"""Represents possible warning codes.

        Values:
            WARNING_CODE_UNSPECIFIED (0):
                Default value. This value is not used.
            ADAPTATION_WARNING (1):
                A warning originated from OS Adaptation.
        """

        WARNING_CODE_UNSPECIFIED = 0
        ADAPTATION_WARNING = 1

    code: WarningCode = proto.Field(
        proto.ENUM,
        number=1,
        enum=WarningCode,
    )
    warning_message: error_details_pb2.LocalizedMessage = proto.Field(
        proto.MESSAGE,
        number=2,
        message=error_details_pb2.LocalizedMessage,
    )
    action_item: error_details_pb2.LocalizedMessage = proto.Field(
        proto.MESSAGE,
        number=3,
        message=error_details_pb2.LocalizedMessage,
    )
    help_links: MutableSequence[error_details_pb2.Help.Link] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=error_details_pb2.Help.Link,
    )
    warning_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )


class VmwareSourceVmDetails(proto.Message):
    r"""Represent the source Vmware VM details.

    Attributes:
        firmware (google.cloud.vmmigration_v1.types.VmwareSourceVmDetails.Firmware):
            Output only. The firmware type of the source
            VM.
        committed_storage_bytes (int):
            Output only. The total size of the disks
            being migrated in bytes.
        disks (MutableSequence[google.cloud.vmmigration_v1.types.VmwareSourceVmDetails.VmwareDiskDetails]):
            Output only. The disks attached to the source
            VM.
        vm_capabilities_info (google.cloud.vmmigration_v1.types.VmCapabilities):
            Output only. Information about VM
            capabilities needed for some Compute Engine
            features.
        architecture (google.cloud.vmmigration_v1.types.VmArchitecture):
            Output only. The VM architecture.
    """

    class Firmware(proto.Enum):
        r"""Possible values for Vmware VM firmware.

        Values:
            FIRMWARE_UNSPECIFIED (0):
                The firmware is unknown.
            EFI (1):
                The firmware is EFI.
            BIOS (2):
                The firmware is BIOS.
        """

        FIRMWARE_UNSPECIFIED = 0
        EFI = 1
        BIOS = 2

    class VmwareDiskDetails(proto.Message):
        r"""The details of a Vmware VM disk.

        Attributes:
            disk_number (int):
                Output only. The ordinal number of the disk.
            size_gb (int):
                Output only. Size in GB.
            label (str):
                Output only. The disk label.
        """

        disk_number: int = proto.Field(
            proto.INT32,
            number=1,
        )
        size_gb: int = proto.Field(
            proto.INT64,
            number=2,
        )
        label: str = proto.Field(
            proto.STRING,
            number=3,
        )

    firmware: Firmware = proto.Field(
        proto.ENUM,
        number=1,
        enum=Firmware,
    )
    committed_storage_bytes: int = proto.Field(
        proto.INT64,
        number=2,
    )
    disks: MutableSequence[VmwareDiskDetails] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=VmwareDiskDetails,
    )
    vm_capabilities_info: "VmCapabilities" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="VmCapabilities",
    )
    architecture: "VmArchitecture" = proto.Field(
        proto.ENUM,
        number=6,
        enum="VmArchitecture",
    )


class AwsSourceVmDetails(proto.Message):
    r"""Represent the source AWS VM details.

    Attributes:
        firmware (google.cloud.vmmigration_v1.types.AwsSourceVmDetails.Firmware):
            Output only. The firmware type of the source
            VM.
        committed_storage_bytes (int):
            Output only. The total size of the disks
            being migrated in bytes.
        disks (MutableSequence[google.cloud.vmmigration_v1.types.AwsSourceVmDetails.AwsDiskDetails]):
            Output only. The disks attached to the source
            VM.
        vm_capabilities_info (google.cloud.vmmigration_v1.types.VmCapabilities):
            Output only. Information about VM
            capabilities needed for some Compute Engine
            features.
        architecture (google.cloud.vmmigration_v1.types.VmArchitecture):
            Output only. The VM architecture.
    """

    class Firmware(proto.Enum):
        r"""Possible values for AWS VM firmware.

        Values:
            FIRMWARE_UNSPECIFIED (0):
                The firmware is unknown.
            EFI (1):
                The firmware is EFI.
            BIOS (2):
                The firmware is BIOS.
        """

        FIRMWARE_UNSPECIFIED = 0
        EFI = 1
        BIOS = 2

    class AwsDiskDetails(proto.Message):
        r"""The details of an AWS instance disk.

        Attributes:
            disk_number (int):
                Output only. The ordinal number of the disk.
            volume_id (str):
                Output only. AWS volume ID.
            size_gb (int):
                Output only. Size in GB.
        """

        disk_number: int = proto.Field(
            proto.INT32,
            number=1,
        )
        volume_id: str = proto.Field(
            proto.STRING,
            number=2,
        )
        size_gb: int = proto.Field(
            proto.INT64,
            number=3,
        )

    firmware: Firmware = proto.Field(
        proto.ENUM,
        number=1,
        enum=Firmware,
    )
    committed_storage_bytes: int = proto.Field(
        proto.INT64,
        number=2,
    )
    disks: MutableSequence[AwsDiskDetails] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=AwsDiskDetails,
    )
    vm_capabilities_info: "VmCapabilities" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="VmCapabilities",
    )
    architecture: "VmArchitecture" = proto.Field(
        proto.ENUM,
        number=6,
        enum="VmArchitecture",
    )


class AzureSourceVmDetails(proto.Message):
    r"""Represent the source Azure VM details.

    Attributes:
        firmware (google.cloud.vmmigration_v1.types.AzureSourceVmDetails.Firmware):
            Output only. The firmware type of the source
            VM.
        committed_storage_bytes (int):
            Output only. The total size of the disks
            being migrated in bytes.
        disks (MutableSequence[google.cloud.vmmigration_v1.types.AzureSourceVmDetails.AzureDiskDetails]):
            Output only. The disks attached to the source
            VM.
        vm_capabilities_info (google.cloud.vmmigration_v1.types.VmCapabilities):
            Output only. Information about VM
            capabilities needed for some Compute Engine
            features.
        architecture (google.cloud.vmmigration_v1.types.VmArchitecture):
            Output only. The VM architecture.
    """

    class Firmware(proto.Enum):
        r"""Possible values for Azure VM firmware.

        Values:
            FIRMWARE_UNSPECIFIED (0):
                The firmware is unknown.
            EFI (1):
                The firmware is EFI.
            BIOS (2):
                The firmware is BIOS.
        """

        FIRMWARE_UNSPECIFIED = 0
        EFI = 1
        BIOS = 2

    class AzureDiskDetails(proto.Message):
        r"""The details of an Azure VM disk.

        Attributes:
            disk_number (int):
                Output only. The ordinal number of the disk.
            disk_id (str):
                Output only. Azure disk ID.
            size_gb (int):
                Output only. Size in GB.
        """

        disk_number: int = proto.Field(
            proto.INT32,
            number=1,
        )
        disk_id: str = proto.Field(
            proto.STRING,
            number=2,
        )
        size_gb: int = proto.Field(
            proto.INT64,
            number=3,
        )

    firmware: Firmware = proto.Field(
        proto.ENUM,
        number=1,
        enum=Firmware,
    )
    committed_storage_bytes: int = proto.Field(
        proto.INT64,
        number=2,
    )
    disks: MutableSequence[AzureDiskDetails] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=AzureDiskDetails,
    )
    vm_capabilities_info: "VmCapabilities" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="VmCapabilities",
    )
    architecture: "VmArchitecture" = proto.Field(
        proto.ENUM,
        number=6,
        enum="VmArchitecture",
    )


class ListReplicationCyclesRequest(proto.Message):
    r"""Request message for 'LisReplicationCyclesRequest' request.

    Attributes:
        parent (str):
            Required. The parent, which owns this
            collection of ReplicationCycles.
        page_size (int):
            Optional. The maximum number of replication
            cycles to return. The service may return fewer
            than this value. If unspecified, at most 100
            migrating VMs will be returned. The maximum
            value is 100; values above 100 will be coerced
            to 100.
        page_token (str):
            Required. A page token, received from a previous
            ``ListReplicationCycles`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListReplicationCycles`` must match the call that provided
            the page token.
        filter (str):
            Optional. The filter request.
        order_by (str):
            Optional. the order by fields for the result.
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


class ListReplicationCyclesResponse(proto.Message):
    r"""Response message for 'ListReplicationCycles' request.

    Attributes:
        replication_cycles (MutableSequence[google.cloud.vmmigration_v1.types.ReplicationCycle]):
            Output only. The list of replication cycles
            response.
        next_page_token (str):
            Output only. A token, which can be sent as ``page_token`` to
            retrieve the next page. If this field is omitted, there are
            no subsequent pages.
        unreachable (MutableSequence[str]):
            Output only. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    replication_cycles: MutableSequence["ReplicationCycle"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ReplicationCycle",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetReplicationCycleRequest(proto.Message):
    r"""Request message for 'GetReplicationCycle' request.

    Attributes:
        name (str):
            Required. The name of the ReplicationCycle.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class VmCapabilities(proto.Message):
    r"""Migrating VM source information about the VM capabilities
    needed for some Compute Engine features.

    Attributes:
        os_capabilities (MutableSequence[google.cloud.vmmigration_v1.types.OsCapability]):
            Output only. Unordered list. List of certain
            VM OS capabilities needed for some Compute
            Engine features.
        last_os_capabilities_update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last time OS capabilities
            list was updated.
    """

    os_capabilities: MutableSequence["OsCapability"] = proto.RepeatedField(
        proto.ENUM,
        number=1,
        enum="OsCapability",
    )
    last_os_capabilities_update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


class ImageImport(proto.Message):
    r"""ImageImport describes the configuration of the image import
    to run.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        cloud_storage_uri (str):
            Immutable. The path to the Cloud Storage file
            from which the image should be imported.

            This field is a member of `oneof`_ ``source``.
        disk_image_target_defaults (google.cloud.vmmigration_v1.types.DiskImageTargetDetails):
            Immutable. Target details for importing a
            disk image, will be used by ImageImportJob.

            This field is a member of `oneof`_ ``target_defaults``.
        machine_image_target_defaults (google.cloud.vmmigration_v1.types.MachineImageTargetDetails):
            Immutable. Target details for importing a
            machine image, will be used by ImageImportJob.

            This field is a member of `oneof`_ ``target_defaults``.
        name (str):
            Output only. The resource path of the
            ImageImport.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the image import was
            created.
        recent_image_import_jobs (MutableSequence[google.cloud.vmmigration_v1.types.ImageImportJob]):
            Output only. The result of the most recent
            runs for this ImageImport. All jobs for this
            ImageImport can be listed via
            ListImageImportJobs.
        encryption (google.cloud.vmmigration_v1.types.Encryption):
            Immutable. The encryption details used by the
            image import process during the image adaptation
            for Compute Engine.
    """

    cloud_storage_uri: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="source",
    )
    disk_image_target_defaults: "DiskImageTargetDetails" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="target_defaults",
        message="DiskImageTargetDetails",
    )
    machine_image_target_defaults: "MachineImageTargetDetails" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="target_defaults",
        message="MachineImageTargetDetails",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    recent_image_import_jobs: MutableSequence["ImageImportJob"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="ImageImportJob",
    )
    encryption: "Encryption" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="Encryption",
    )


class ImageImportJob(proto.Message):
    r"""ImageImportJob describes the progress and result of an image
    import.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        cloud_storage_uri (str):
            Output only. The path to the Cloud Storage
            file from which the image should be imported.

            This field is a member of `oneof`_ ``source``.
        disk_image_target_details (google.cloud.vmmigration_v1.types.DiskImageTargetDetails):
            Output only. Target details used to import a
            disk image.

            This field is a member of `oneof`_ ``target_details``.
        machine_image_target_details (google.cloud.vmmigration_v1.types.MachineImageTargetDetails):
            Output only. Target details used to import a
            machine image.

            This field is a member of `oneof`_ ``target_details``.
        name (str):
            Output only. The resource path of the
            ImageImportJob.
        created_resources (MutableSequence[str]):
            Output only. The resource paths of the
            resources created by the image import job.
        state (google.cloud.vmmigration_v1.types.ImageImportJob.State):
            Output only. The state of the image import.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the image import was
            created (as an API call, not when it was
            actually created in the target).
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the image import was
            ended.
        errors (MutableSequence[google.rpc.status_pb2.Status]):
            Output only. Provides details on the error
            that led to the image import state in case of an
            error.
        warnings (MutableSequence[google.cloud.vmmigration_v1.types.MigrationWarning]):
            Output only. Warnings that occurred during
            the image import.
        steps (MutableSequence[google.cloud.vmmigration_v1.types.ImageImportStep]):
            Output only. The image import steps list
            representing its progress.
    """

    class State(proto.Enum):
        r"""Possible states of the image import.

        Values:
            STATE_UNSPECIFIED (0):
                The state is unknown.
            PENDING (1):
                The image import has not yet started.
            RUNNING (2):
                The image import is active and running.
            SUCCEEDED (3):
                The image import has finished successfully.
            FAILED (4):
                The image import has finished with errors.
            CANCELLING (5):
                The image import is being cancelled.
            CANCELLED (6):
                The image import was cancelled.
        """

        STATE_UNSPECIFIED = 0
        PENDING = 1
        RUNNING = 2
        SUCCEEDED = 3
        FAILED = 4
        CANCELLING = 5
        CANCELLED = 6

    cloud_storage_uri: str = proto.Field(
        proto.STRING,
        number=10,
        oneof="source",
    )
    disk_image_target_details: "DiskImageTargetDetails" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="target_details",
        message="DiskImageTargetDetails",
    )
    machine_image_target_details: "MachineImageTargetDetails" = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="target_details",
        message="MachineImageTargetDetails",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    created_resources: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    errors: MutableSequence[status_pb2.Status] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message=status_pb2.Status,
    )
    warnings: MutableSequence["MigrationWarning"] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message="MigrationWarning",
    )
    steps: MutableSequence["ImageImportStep"] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="ImageImportStep",
    )


class ImageImportStep(proto.Message):
    r"""ImageImportStep holds information about the image import step
    progress.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        initializing (google.cloud.vmmigration_v1.types.InitializingImageImportStep):
            Initializing step.

            This field is a member of `oneof`_ ``step``.
        loading_source_files (google.cloud.vmmigration_v1.types.LoadingImageSourceFilesStep):
            Loading source files step.

            This field is a member of `oneof`_ ``step``.
        adapting_os (google.cloud.vmmigration_v1.types.AdaptingOSStep):
            Adapting OS step.

            This field is a member of `oneof`_ ``step``.
        creating_image (google.cloud.vmmigration_v1.types.CreatingImageStep):
            Creating image step.

            This field is a member of `oneof`_ ``step``.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the step has started.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the step has ended.
    """

    initializing: "InitializingImageImportStep" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="step",
        message="InitializingImageImportStep",
    )
    loading_source_files: "LoadingImageSourceFilesStep" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="step",
        message="LoadingImageSourceFilesStep",
    )
    adapting_os: "AdaptingOSStep" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="step",
        message="AdaptingOSStep",
    )
    creating_image: "CreatingImageStep" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="step",
        message="CreatingImageStep",
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


class InitializingImageImportStep(proto.Message):
    r"""InitializingImageImportStep contains specific step details."""


class LoadingImageSourceFilesStep(proto.Message):
    r"""LoadingImageSourceFilesStep contains specific step details."""


class CreatingImageStep(proto.Message):
    r"""CreatingImageStep contains specific step details."""


class DiskImageTargetDetails(proto.Message):
    r"""The target details of the image resource that will be created
    by the import job.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        os_adaptation_parameters (google.cloud.vmmigration_v1.types.ImageImportOsAdaptationParameters):
            Optional. Use to set the parameters relevant
            for the OS adaptation process.

            This field is a member of `oneof`_ ``os_adaptation_config``.
        data_disk_image_import (google.cloud.vmmigration_v1.types.DataDiskImageImport):
            Optional. Use to skip OS adaptation process.

            This field is a member of `oneof`_ ``os_adaptation_config``.
        image_name (str):
            Required. The name of the image to be
            created.
        target_project (str):
            Required. Reference to the TargetProject
            resource that represents the target project in
            which the imported image will be created.
        description (str):
            Optional. An optional description of the
            image.
        family_name (str):
            Optional. The name of the image family to
            which the new image belongs.
        labels (MutableMapping[str, str]):
            Optional. A map of labels to associate with
            the image.
        additional_licenses (MutableSequence[str]):
            Optional. Additional licenses to assign to the image.
            Format:
            https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/licenses/LICENSE_NAME
            Or
            https://www.googleapis.com/compute/beta/projects/PROJECT_ID/global/licenses/LICENSE_NAME
        single_region_storage (bool):
            Optional. Set to true to set the image
            storageLocations to the single region of the
            import job. When false, the closest multi-region
            is selected.
        encryption (google.cloud.vmmigration_v1.types.Encryption):
            Immutable. The encryption to apply to the
            image.
    """

    os_adaptation_parameters: "ImageImportOsAdaptationParameters" = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="os_adaptation_config",
        message="ImageImportOsAdaptationParameters",
    )
    data_disk_image_import: "DataDiskImageImport" = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="os_adaptation_config",
        message="DataDiskImageImport",
    )
    image_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    target_project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    family_name: str = proto.Field(
        proto.STRING,
        number=6,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    additional_licenses: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    single_region_storage: bool = proto.Field(
        proto.BOOL,
        number=9,
    )
    encryption: "Encryption" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="Encryption",
    )


class MachineImageTargetDetails(proto.Message):
    r"""The target details of the machine image resource that will be
    created by the image import job.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        os_adaptation_parameters (google.cloud.vmmigration_v1.types.ImageImportOsAdaptationParameters):
            Optional. Use to set the parameters relevant
            for the OS adaptation process.

            This field is a member of `oneof`_ ``os_adaptation_config``.
        skip_os_adaptation (google.cloud.vmmigration_v1.types.SkipOsAdaptation):
            Optional. Use to skip OS adaptation process.

            This field is a member of `oneof`_ ``os_adaptation_config``.
        machine_image_name (str):
            Required. The name of the machine image to be
            created.
        target_project (str):
            Required. Reference to the TargetProject
            resource that represents the target project in
            which the imported machine image will be
            created.
        description (str):
            Optional. An optional description of the
            machine image.
        single_region_storage (bool):
            Optional. Set to true to set the machine
            image storageLocations to the single region of
            the import job. When false, the closest
            multi-region is selected.
        encryption (google.cloud.vmmigration_v1.types.Encryption):
            Immutable. The encryption to apply to the
            machine image. If the Image Import resource has
            an encryption, this field must be set to the
            same encryption key.
        machine_image_parameters_overrides (google.cloud.vmmigration_v1.types.MachineImageParametersOverrides):
            Optional. Parameters overriding decisions
            based on the source machine image
            configurations.
        service_account (google.cloud.vmmigration_v1.types.ServiceAccount):
            Optional. The service account to assign to
            the instance created by the machine image.
        additional_licenses (MutableSequence[str]):
            Optional. Additional licenses to assign to the instance
            created by the machine image. Format:
            https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/licenses/LICENSE_NAME
            Or
            https://www.googleapis.com/compute/beta/projects/PROJECT_ID/global/licenses/LICENSE_NAME
        labels (MutableMapping[str, str]):
            Optional. The labels to apply to the instance
            created by the machine image.
        tags (MutableSequence[str]):
            Optional. The tags to apply to the instance
            created by the machine image.
        shielded_instance_config (google.cloud.vmmigration_v1.types.ShieldedInstanceConfig):
            Optional. Shielded instance configuration.
        network_interfaces (MutableSequence[google.cloud.vmmigration_v1.types.NetworkInterface]):
            Optional. The network interfaces to create
            with the instance created by the machine image.
            Internal and external IP addresses, and network
            tiers are ignored for machine image import.
    """

    os_adaptation_parameters: "ImageImportOsAdaptationParameters" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="os_adaptation_config",
        message="ImageImportOsAdaptationParameters",
    )
    skip_os_adaptation: "SkipOsAdaptation" = proto.Field(
        proto.MESSAGE,
        number=16,
        oneof="os_adaptation_config",
        message="SkipOsAdaptation",
    )
    machine_image_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    target_project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    single_region_storage: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    encryption: "Encryption" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="Encryption",
    )
    machine_image_parameters_overrides: "MachineImageParametersOverrides" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="MachineImageParametersOverrides",
    )
    service_account: "ServiceAccount" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="ServiceAccount",
    )
    additional_licenses: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=9,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=10,
    )
    tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=11,
    )
    shielded_instance_config: "ShieldedInstanceConfig" = proto.Field(
        proto.MESSAGE,
        number=12,
        message="ShieldedInstanceConfig",
    )
    network_interfaces: MutableSequence["NetworkInterface"] = proto.RepeatedField(
        proto.MESSAGE,
        number=13,
        message="NetworkInterface",
    )


class ServiceAccount(proto.Message):
    r"""Service account to assign to the instance created by the
    machine image.

    Attributes:
        email (str):
            Required. The email address of the service
            account.
        scopes (MutableSequence[str]):
            Optional. The list of scopes to be made
            available for this service account.
    """

    email: str = proto.Field(
        proto.STRING,
        number=1,
    )
    scopes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class ShieldedInstanceConfig(proto.Message):
    r"""Shielded instance configuration.

    Attributes:
        secure_boot (google.cloud.vmmigration_v1.types.ShieldedInstanceConfig.SecureBoot):
            Optional. Defines whether the instance
            created by the machine image has Secure Boot
            enabled. This can be set to true only if the
            image boot option is EFI.
        enable_vtpm (bool):
            Optional. Defines whether the instance
            created by the machine image has vTPM enabled.
            This can be set to true only if the image boot
            option is EFI.
        enable_integrity_monitoring (bool):
            Optional. Defines whether the instance
            created by the machine image has integrity
            monitoring enabled. This can be set to true only
            if the image boot option is EFI, and vTPM is
            enabled.
    """

    class SecureBoot(proto.Enum):
        r"""Possible values for secure boot.

        Values:
            SECURE_BOOT_UNSPECIFIED (0):
                No explicit value is selected. Will use the
                configuration of the source (if exists,
                otherwise the default will be false).
            TRUE (1):
                Use secure boot. This can be set to true only
                if the image boot option is EFI.
            FALSE (2):
                Do not use secure boot.
        """

        SECURE_BOOT_UNSPECIFIED = 0
        TRUE = 1
        FALSE = 2

    secure_boot: SecureBoot = proto.Field(
        proto.ENUM,
        number=1,
        enum=SecureBoot,
    )
    enable_vtpm: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    enable_integrity_monitoring: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class MachineImageParametersOverrides(proto.Message):
    r"""Parameters overriding decisions based on the source machine
    image configurations.

    Attributes:
        machine_type (str):
            Optional. The machine type to create the
            MachineImage with. If empty, the service will
            choose a relevant machine type based on the
            information from the source image.
            For more information about machine types, please
            refer to
            https://cloud.google.com/compute/docs/machine-resource.
    """

    machine_type: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ImageImportOsAdaptationParameters(proto.Message):
    r"""Parameters affecting the OS adaptation process.

    Attributes:
        generalize (bool):
            Optional. Set to true in order to generalize
            the imported image. The generalization process
            enables co-existence of multiple VMs created
            from the same image.
            For Windows, generalizing the image removes
            computer-specific information such as installed
            drivers and the computer security identifier
            (SID).
        license_type (google.cloud.vmmigration_v1.types.ComputeEngineLicenseType):
            Optional. Choose which type of license to
            apply to the imported image.
        boot_conversion (google.cloud.vmmigration_v1.types.BootConversion):
            Optional. By default the image will keep its
            existing boot option. Setting this property will
            trigger an internal process which will convert
            the image from using the existing boot option to
            another. The size of the boot disk might be
            increased to allow the conversion
        adaptation_modifiers (MutableSequence[google.cloud.vmmigration_v1.types.AdaptationModifier]):
            Optional. Modifiers to be used as
            configuration of the OS adaptation process.
    """

    generalize: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    license_type: "ComputeEngineLicenseType" = proto.Field(
        proto.ENUM,
        number=2,
        enum="ComputeEngineLicenseType",
    )
    boot_conversion: "BootConversion" = proto.Field(
        proto.ENUM,
        number=3,
        enum="BootConversion",
    )
    adaptation_modifiers: MutableSequence["AdaptationModifier"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="AdaptationModifier",
    )


class DataDiskImageImport(proto.Message):
    r"""Used when the image import is not using OS adaptation
    process.

    Attributes:
        guest_os_features (MutableSequence[str]):
            Optional. A list of guest OS features to
            apply to the imported image. These features are
            flags that are used by Compute Engine to enable
            certain capabilities for virtual machine
            instances that are created from the image.

            This field does not change the OS of the image;
            it only marks the image with the specified
            features. The user must ensure that the OS is
            compatible with the features.

            For a list of available features, see
            https://cloud.google.com/compute/docs/images/create-custom#guest-os-features.
    """

    guest_os_features: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class SkipOsAdaptation(proto.Message):
    r"""Mentions that the machine image import is not using OS
    adaptation process.

    """


class GetImageImportRequest(proto.Message):
    r"""Request message for 'GetImageImport' call.

    Attributes:
        name (str):
            Required. The ImageImport name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListImageImportsRequest(proto.Message):
    r"""Request message for 'ListImageImports' call.

    Attributes:
        parent (str):
            Required. The parent, which owns this
            collection of targets.
        page_size (int):
            Optional. The maximum number of targets to
            return. The service may return fewer than this
            value. If unspecified, at most 500 targets will
            be returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListImageImports`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListImageImports`` must match the call that provided the
            page token.
        filter (str):
            Optional. The filter request (according to AIP-160).
        order_by (str):
            Optional. The order by fields for the result (according to
            AIP-132). Currently ordering is only possible by "name"
            field.
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


class ListImageImportsResponse(proto.Message):
    r"""Response message for 'ListImageImports' call.

    Attributes:
        image_imports (MutableSequence[google.cloud.vmmigration_v1.types.ImageImport]):
            Output only. The list of target response.
        next_page_token (str):
            Output only. A token, which can be sent as ``page_token`` to
            retrieve the next page. If this field is omitted, there are
            no subsequent pages.
        unreachable (MutableSequence[str]):
            Output only. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    image_imports: MutableSequence["ImageImport"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ImageImport",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class CreateImageImportRequest(proto.Message):
    r"""Request message for 'CreateImageImport' request.

    Attributes:
        parent (str):
            Required. The ImageImport's parent.
        image_import_id (str):
            Required. The image import identifier. This value maximum
            length is 63 characters, and valid characters are
            /[a-z][0-9]-/. It must start with an english letter and must
            not end with a hyphen.
        image_import (google.cloud.vmmigration_v1.types.ImageImport):
            Required. The create request body.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes since the first request.

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
    image_import_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    image_import: "ImageImport" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ImageImport",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteImageImportRequest(proto.Message):
    r"""Request message for 'DeleteImageImport' request.

    Attributes:
        name (str):
            Required. The ImageImport name.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and t he request times out.
            If you make the request again with the same
            request ID, the server can check if original
            operation with the same request ID was received,
            and if so, will ignore the second request. This
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


class GetImageImportJobRequest(proto.Message):
    r"""Request message for 'GetImageImportJob' call.

    Attributes:
        name (str):
            Required. The ImageImportJob name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListImageImportJobsRequest(proto.Message):
    r"""Request message for 'ListImageImportJobs' call.

    Attributes:
        parent (str):
            Required. The parent, which owns this
            collection of targets.
        page_size (int):
            Optional. The maximum number of targets to
            return. The service may return fewer than this
            value. If unspecified, at most 500 targets will
            be returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListImageImportJobs`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListImageImportJobs`` must match the call that provided
            the page token.
        filter (str):
            Optional. The filter request (according to AIP-160).
        order_by (str):
            Optional. The order by fields for the result (according to
            AIP-132). Currently ordering is only possible by "name"
            field.
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


class ListImageImportJobsResponse(proto.Message):
    r"""Response message for 'ListImageImportJobs' call.

    Attributes:
        image_import_jobs (MutableSequence[google.cloud.vmmigration_v1.types.ImageImportJob]):
            Output only. The list of target response.
        next_page_token (str):
            Output only. A token, which can be sent as ``page_token`` to
            retrieve the next page. If this field is omitted, there are
            no subsequent pages.
        unreachable (MutableSequence[str]):
            Output only. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    image_import_jobs: MutableSequence["ImageImportJob"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ImageImportJob",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class CancelImageImportJobRequest(proto.Message):
    r"""Request message for 'CancelImageImportJob' request.

    Attributes:
        name (str):
            Required. The image import job id.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CancelImageImportJobResponse(proto.Message):
    r"""Response message for 'CancelImageImportJob' request."""


class DiskMigrationJob(proto.Message):
    r"""Describes the disk which will be migrated from the source
    environment. The source disk has to be unattached.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        aws_source_disk_details (google.cloud.vmmigration_v1.types.AwsSourceDiskDetails):
            Details of the unattached AWS source disk.

            This field is a member of `oneof`_ ``source_disk_details``.
        name (str):
            Output only. Identifier. The identifier of
            the DiskMigrationJob.
        target_details (google.cloud.vmmigration_v1.types.DiskMigrationJobTargetDetails):
            Required. Details of the target Disk in
            Compute Engine.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the DiskMigrationJob
            resource was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last time the
            DiskMigrationJob resource was updated.
        state (google.cloud.vmmigration_v1.types.DiskMigrationJob.State):
            Output only. State of the DiskMigrationJob.
        errors (MutableSequence[google.rpc.status_pb2.Status]):
            Output only. Provides details on the errors
            that led to the disk migration job's state in
            case of an error.
        steps (MutableSequence[google.cloud.vmmigration_v1.types.DiskMigrationStep]):
            Output only. The disk migration steps list
            representing its progress.
    """

    class State(proto.Enum):
        r"""The possible values of the state/health of DiskMigrationJob.

        Values:
            STATE_UNSPECIFIED (0):
                The state is unspecified. This is not in use.
            READY (1):
                The initial state of the disk migration.
                In this state the customers can update the
                target details.
            RUNNING (3):
                The migration is active, and it's running or
                scheduled to run.
            SUCCEEDED (4):
                The migration completed successfully.
            CANCELLING (5):
                Migration cancellation was initiated.
            CANCELLED (6):
                The migration was cancelled.
            FAILED (7):
                The migration process encountered an
                unrecoverable error and was aborted.
        """

        STATE_UNSPECIFIED = 0
        READY = 1
        RUNNING = 3
        SUCCEEDED = 4
        CANCELLING = 5
        CANCELLED = 6
        FAILED = 7

    aws_source_disk_details: "AwsSourceDiskDetails" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="source_disk_details",
        message="AwsSourceDiskDetails",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    target_details: "DiskMigrationJobTargetDetails" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="DiskMigrationJobTargetDetails",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=6,
        enum=State,
    )
    errors: MutableSequence[status_pb2.Status] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message=status_pb2.Status,
    )
    steps: MutableSequence["DiskMigrationStep"] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message="DiskMigrationStep",
    )


class DiskMigrationJobTargetDetails(proto.Message):
    r"""Details of the target disk in Compute Engine.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        target_disk (google.cloud.vmmigration_v1.types.ComputeEngineDisk):
            Required. The target disk.

            This field is a member of `oneof`_ ``target_storage``.
        target_project (str):
            Required. The name of the resource of type
            TargetProject which represents the Compute
            Engine project in which to create the disk.
            Should be of the form:
            projects/{project}/locations/global/targetProjects/{target-project}
        labels (MutableMapping[str, str]):
            Optional. A map of labels to associate with
            the disk.
        encryption (google.cloud.vmmigration_v1.types.Encryption):
            Optional. The encryption to apply to the
            disk. If the DiskMigrationJob parent Source
            resource has an encryption, this field must be
            set to the same encryption key.
    """

    target_disk: "ComputeEngineDisk" = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="target_storage",
        message="ComputeEngineDisk",
    )
    target_project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    encryption: "Encryption" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="Encryption",
    )


class DiskMigrationStep(proto.Message):
    r"""DiskMigrationStep holds information about the disk migration
    step progress.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        creating_source_disk_snapshot (google.cloud.vmmigration_v1.types.CreatingSourceDiskSnapshotStep):
            Creating source disk snapshot step.

            This field is a member of `oneof`_ ``step``.
        copying_source_disk_snapshot (google.cloud.vmmigration_v1.types.CopyingSourceDiskSnapshotStep):
            Copying source disk snapshot step.

            This field is a member of `oneof`_ ``step``.
        provisioning_target_disk (google.cloud.vmmigration_v1.types.ProvisioningTargetDiskStep):
            Creating target disk step.

            This field is a member of `oneof`_ ``step``.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the step has started.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the step has ended.
    """

    creating_source_disk_snapshot: "CreatingSourceDiskSnapshotStep" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="step",
        message="CreatingSourceDiskSnapshotStep",
    )
    copying_source_disk_snapshot: "CopyingSourceDiskSnapshotStep" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="step",
        message="CopyingSourceDiskSnapshotStep",
    )
    provisioning_target_disk: "ProvisioningTargetDiskStep" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="step",
        message="ProvisioningTargetDiskStep",
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


class CreatingSourceDiskSnapshotStep(proto.Message):
    r"""CreatingSourceDiskSnapshotStep contains specific step
    details.

    """


class CopyingSourceDiskSnapshotStep(proto.Message):
    r"""CopyingSourceDiskSnapshotStep contains specific step details."""


class ProvisioningTargetDiskStep(proto.Message):
    r"""ProvisioningTargetDiskStep contains specific step details."""


class ComputeEngineDisk(proto.Message):
    r"""Compute Engine disk target details.

    Attributes:
        disk_id (str):
            Optional. Target Compute Engine Disk ID.
            This is the resource ID segment of the Compute
            Engine Disk to create. In the resource name
            compute/v1/projects/{project}/zones/{zone}/disks/disk1
            "disk1" is the resource ID for the disk.
        zone (str):
            Required. The Compute Engine zone in which to
            create the disk. Should be of the form:
            projects/{target-project}/locations/{zone}
        replica_zones (MutableSequence[str]):
            Optional. Replication zones of the regional
            disk. Should be of the form:
            projects/{target-project}/locations/{replica-zone}
            Currently only one replica zone is supported.
        disk_type (google.cloud.vmmigration_v1.types.ComputeEngineDiskType):
            Required. The disk type to use.
    """

    disk_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    zone: str = proto.Field(
        proto.STRING,
        number=2,
    )
    replica_zones: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    disk_type: "ComputeEngineDiskType" = proto.Field(
        proto.ENUM,
        number=4,
        enum="ComputeEngineDiskType",
    )


class AwsSourceDiskDetails(proto.Message):
    r"""Represents the source AWS Disk details.

    Attributes:
        volume_id (str):
            Required. AWS volume ID.
        size_gib (int):
            Output only. Size in GiB.
        disk_type (google.cloud.vmmigration_v1.types.AwsSourceDiskDetails.Type):
            Optional. Output only. Disk type.
        tags (MutableMapping[str, str]):
            Optional. Output only. A map of AWS volume
            tags.
    """

    class Type(proto.Enum):
        r"""Possible values for disk types.

        Values:
            TYPE_UNSPECIFIED (0):
                Unspecified AWS disk type. Should not be
                used.
            GP2 (1):
                GP2 disk type.
            GP3 (2):
                GP3 disk type.
            IO1 (3):
                IO1 disk type.
            IO2 (4):
                IO2 disk type.
            ST1 (5):
                ST1 disk type.
            SC1 (6):
                SC1 disk type.
            STANDARD (7):
                Standard disk type.
        """

        TYPE_UNSPECIFIED = 0
        GP2 = 1
        GP3 = 2
        IO1 = 3
        IO2 = 4
        ST1 = 5
        SC1 = 6
        STANDARD = 7

    volume_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    size_gib: int = proto.Field(
        proto.INT64,
        number=2,
    )
    disk_type: Type = proto.Field(
        proto.ENUM,
        number=3,
        enum=Type,
    )
    tags: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )


class CreateDiskMigrationJobRequest(proto.Message):
    r"""Request message for 'CreateDiskMigrationJob' request.

    Attributes:
        parent (str):
            Required. The DiskMigrationJob's parent.
        disk_migration_job_id (str):
            Required. The DiskMigrationJob identifier.
            The maximum length of this value is 63
            characters. Valid characters are lower case
            Latin letters, digits and hyphen. It must start
            with a Latin letter and must not end with a
            hyphen.
        disk_migration_job (google.cloud.vmmigration_v1.types.DiskMigrationJob):
            Required. The create request body.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request timed out. If
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
    disk_migration_job_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    disk_migration_job: "DiskMigrationJob" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="DiskMigrationJob",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListDiskMigrationJobsRequest(proto.Message):
    r"""Request message for 'ListDiskMigrationJobsRequest' request.

    Attributes:
        parent (str):
            Required. The parent, which owns this
            collection of DiskMigrationJobs.
        page_size (int):
            Optional. The maximum number of disk
            migration jobs to return. The service may return
            fewer than this value. If unspecified, at most
            500 disk migration jobs will be returned.
            The maximum value is 1000; values above 1000
            will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListDiskMigrationJobs`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all parameters provided to
            ``ListDiskMigrationJobs`` except ``page_size`` must match
            the call that provided the page token.
        filter (str):
            Optional. The filter request (according to AIP-160).
        order_by (str):
            Optional. Ordering of the result list.
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


class ListDiskMigrationJobsResponse(proto.Message):
    r"""Response message for 'ListDiskMigrationJobs' request.

    Attributes:
        disk_migration_jobs (MutableSequence[google.cloud.vmmigration_v1.types.DiskMigrationJob]):
            Output only. The list of the disk migration
            jobs.
        next_page_token (str):
            Optional. Output only. A token, which can be sent as
            ``page_token`` to retrieve the next page. If this field is
            omitted, there are no subsequent pages.
        unreachable (MutableSequence[str]):
            Output only. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    disk_migration_jobs: MutableSequence["DiskMigrationJob"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DiskMigrationJob",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetDiskMigrationJobRequest(proto.Message):
    r"""Request message for 'GetDiskMigrationJob' request.

    Attributes:
        name (str):
            Required. The name of the DiskMigrationJob.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateDiskMigrationJobRequest(proto.Message):
    r"""Request message for 'UpdateDiskMigrationJob' request.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the DiskMigrationJob resource by the update.
            The fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask,
            then a mask equivalent to all fields that are populated
            (have a non-empty value), will be implied.
        disk_migration_job (google.cloud.vmmigration_v1.types.DiskMigrationJob):
            Required. The update request body.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request timed out. If
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
    disk_migration_job: "DiskMigrationJob" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DiskMigrationJob",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteDiskMigrationJobRequest(proto.Message):
    r"""Request message for 'DeleteDiskMigrationJob' request.

    Attributes:
        name (str):
            Required. The name of the DiskMigrationJob.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class RunDiskMigrationJobRequest(proto.Message):
    r"""Request message for 'RunDiskMigrationJobRequest' request.

    Attributes:
        name (str):
            Required. The name of the DiskMigrationJob.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class RunDiskMigrationJobResponse(proto.Message):
    r"""Response message for 'RunDiskMigrationJob' request."""


class CancelDiskMigrationJobRequest(proto.Message):
    r"""Request message for 'CancelDiskMigrationJob' request.

    Attributes:
        name (str):
            Required. The name of the DiskMigrationJob.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CancelDiskMigrationJobResponse(proto.Message):
    r"""Response message for 'CancelDiskMigrationJob' request."""


__all__ = tuple(sorted(__protobuf__.manifest))
