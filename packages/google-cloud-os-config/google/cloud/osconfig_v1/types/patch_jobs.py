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

from google.cloud.osconfig_v1.types import osconfig_common

__protobuf__ = proto.module(
    package="google.cloud.osconfig.v1",
    manifest={
        "ExecutePatchJobRequest",
        "GetPatchJobRequest",
        "ListPatchJobInstanceDetailsRequest",
        "ListPatchJobInstanceDetailsResponse",
        "PatchJobInstanceDetails",
        "ListPatchJobsRequest",
        "ListPatchJobsResponse",
        "PatchJob",
        "PatchConfig",
        "Instance",
        "CancelPatchJobRequest",
        "AptSettings",
        "YumSettings",
        "GooSettings",
        "ZypperSettings",
        "WindowsUpdateSettings",
        "ExecStep",
        "ExecStepConfig",
        "GcsObject",
        "PatchInstanceFilter",
        "PatchRollout",
    },
)


class ExecutePatchJobRequest(proto.Message):
    r"""A request message to initiate patching across Compute Engine
    instances.

    Attributes:
        parent (str):
            Required. The project in which to run this patch in the form
            ``projects/*``
        description (str):
            Description of the patch job. Length of the
            description is limited to 1024 characters.
        instance_filter (google.cloud.osconfig_v1.types.PatchInstanceFilter):
            Required. Instances to patch, either
            explicitly or filtered by some criteria such as
            zone or labels.
        patch_config (google.cloud.osconfig_v1.types.PatchConfig):
            Patch configuration being applied. If
            omitted, instances are patched using the default
            configurations.
        duration (google.protobuf.duration_pb2.Duration):
            Duration of the patch job. After the duration
            ends, the patch job times out.
        dry_run (bool):
            If this patch is a dry-run only, instances
            are contacted but will do nothing.
        display_name (str):
            Display name for this patch job. This does
            not have to be unique.
        rollout (google.cloud.osconfig_v1.types.PatchRollout):
            Rollout strategy of the patch job.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    instance_filter: "PatchInstanceFilter" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="PatchInstanceFilter",
    )
    patch_config: "PatchConfig" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="PatchConfig",
    )
    duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=5,
        message=duration_pb2.Duration,
    )
    dry_run: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=8,
    )
    rollout: "PatchRollout" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="PatchRollout",
    )


class GetPatchJobRequest(proto.Message):
    r"""Request to get an active or completed patch job.

    Attributes:
        name (str):
            Required. Name of the patch in the form
            ``projects/*/patchJobs/*``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListPatchJobInstanceDetailsRequest(proto.Message):
    r"""Request to list details for all instances that are part of a
    patch job.

    Attributes:
        parent (str):
            Required. The parent for the instances are in the form of
            ``projects/*/patchJobs/*``.
        page_size (int):
            The maximum number of instance details
            records to return.  Default is 100.
        page_token (str):
            A pagination token returned from a previous
            call that indicates where this listing should
            continue from.
        filter (str):
            A filter expression that filters results listed in the
            response. This field supports filtering results by instance
            zone, name, state, or ``failure_reason``.
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


class ListPatchJobInstanceDetailsResponse(proto.Message):
    r"""A response message for listing the instances details for a
    patch job.

    Attributes:
        patch_job_instance_details (MutableSequence[google.cloud.osconfig_v1.types.PatchJobInstanceDetails]):
            A list of instance status.
        next_page_token (str):
            A pagination token that can be used to get
            the next page of results.
    """

    @property
    def raw_page(self):
        return self

    patch_job_instance_details: MutableSequence["PatchJobInstanceDetails"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="PatchJobInstanceDetails",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class PatchJobInstanceDetails(proto.Message):
    r"""Patch details for a VM instance. For more information about
    reviewing VM instance details, see `Listing all VM instance details
    for a specific patch
    job <https://cloud.google.com/compute/docs/os-patch-management/manage-patch-jobs#list-instance-details>`__.

    Attributes:
        name (str):
            The instance name in the form
            ``projects/*/zones/*/instances/*``
        instance_system_id (str):
            The unique identifier for the instance. This
            identifier is defined by the server.
        state (google.cloud.osconfig_v1.types.Instance.PatchState):
            Current state of instance patch.
        failure_reason (str):
            If the patch fails, this field provides the
            reason.
        attempt_count (int):
            The number of times the agent that the agent
            attempts to apply the patch.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance_system_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    state: "Instance.PatchState" = proto.Field(
        proto.ENUM,
        number=3,
        enum="Instance.PatchState",
    )
    failure_reason: str = proto.Field(
        proto.STRING,
        number=4,
    )
    attempt_count: int = proto.Field(
        proto.INT64,
        number=5,
    )


class ListPatchJobsRequest(proto.Message):
    r"""A request message for listing patch jobs.

    Attributes:
        parent (str):
            Required. In the form of ``projects/*``
        page_size (int):
            The maximum number of instance status to
            return.
        page_token (str):
            A pagination token returned from a previous
            call that indicates where this listing should
            continue from.
        filter (str):
            If provided, this field specifies the criteria that must be
            met by patch jobs to be included in the response. Currently,
            filtering is only available on the patch_deployment field.
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


class ListPatchJobsResponse(proto.Message):
    r"""A response message for listing patch jobs.

    Attributes:
        patch_jobs (MutableSequence[google.cloud.osconfig_v1.types.PatchJob]):
            The list of patch jobs.
        next_page_token (str):
            A pagination token that can be used to get
            the next page of results.
    """

    @property
    def raw_page(self):
        return self

    patch_jobs: MutableSequence["PatchJob"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="PatchJob",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class PatchJob(proto.Message):
    r"""A high level representation of a patch job that is either in
    progress or has completed.

    Instance details are not included in the job. To paginate through
    instance details, use ListPatchJobInstanceDetails.

    For more information about patch jobs, see `Creating patch
    jobs <https://cloud.google.com/compute/docs/os-patch-management/create-patch-job>`__.

    Attributes:
        name (str):
            Unique identifier for this patch job in the form
            ``projects/*/patchJobs/*``
        display_name (str):
            Display name for this patch job. This is not
            a unique identifier.
        description (str):
            Description of the patch job. Length of the
            description is limited to 1024 characters.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Time this patch job was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Last time this patch job was updated.
        state (google.cloud.osconfig_v1.types.PatchJob.State):
            The current state of the PatchJob.
        instance_filter (google.cloud.osconfig_v1.types.PatchInstanceFilter):
            Instances to patch.
        patch_config (google.cloud.osconfig_v1.types.PatchConfig):
            Patch configuration being applied.
        duration (google.protobuf.duration_pb2.Duration):
            Duration of the patch job. After the duration
            ends, the patch job times out.
        instance_details_summary (google.cloud.osconfig_v1.types.PatchJob.InstanceDetailsSummary):
            Summary of instance details.
        dry_run (bool):
            If this patch job is a dry run, the agent
            reports that it has finished without running any
            updates on the VM instance.
        error_message (str):
            If this patch job failed, this message
            provides information about the failure.
        percent_complete (float):
            Reflects the overall progress of the patch
            job in the range of 0.0 being no progress to
            100.0 being complete.
        patch_deployment (str):
            Output only. Name of the patch deployment
            that created this patch job.
        rollout (google.cloud.osconfig_v1.types.PatchRollout):
            Rollout strategy being applied.
    """

    class State(proto.Enum):
        r"""Enumeration of the various states a patch job passes through
        as it executes.

        Values:
            STATE_UNSPECIFIED (0):
                State must be specified.
            STARTED (1):
                The patch job was successfully initiated.
            INSTANCE_LOOKUP (2):
                The patch job is looking up instances to run
                the patch on.
            PATCHING (3):
                Instances are being patched.
            SUCCEEDED (4):
                Patch job completed successfully.
            COMPLETED_WITH_ERRORS (5):
                Patch job completed but there were errors.
            CANCELED (6):
                The patch job was canceled.
            TIMED_OUT (7):
                The patch job timed out.
        """

        STATE_UNSPECIFIED = 0
        STARTED = 1
        INSTANCE_LOOKUP = 2
        PATCHING = 3
        SUCCEEDED = 4
        COMPLETED_WITH_ERRORS = 5
        CANCELED = 6
        TIMED_OUT = 7

    class InstanceDetailsSummary(proto.Message):
        r"""A summary of the current patch state across all instances that this
        patch job affects. Contains counts of instances in different states.
        These states map to ``InstancePatchState``. List patch job instance
        details to see the specific states of each instance.

        Attributes:
            pending_instance_count (int):
                Number of instances pending patch job.
            inactive_instance_count (int):
                Number of instances that are inactive.
            notified_instance_count (int):
                Number of instances notified about patch job.
            started_instance_count (int):
                Number of instances that have started.
            downloading_patches_instance_count (int):
                Number of instances that are downloading
                patches.
            applying_patches_instance_count (int):
                Number of instances that are applying
                patches.
            rebooting_instance_count (int):
                Number of instances rebooting.
            succeeded_instance_count (int):
                Number of instances that have completed
                successfully.
            succeeded_reboot_required_instance_count (int):
                Number of instances that require reboot.
            failed_instance_count (int):
                Number of instances that failed.
            acked_instance_count (int):
                Number of instances that have acked and will
                start shortly.
            timed_out_instance_count (int):
                Number of instances that exceeded the time
                out while applying the patch.
            pre_patch_step_instance_count (int):
                Number of instances that are running the
                pre-patch step.
            post_patch_step_instance_count (int):
                Number of instances that are running the
                post-patch step.
            no_agent_detected_instance_count (int):
                Number of instances that do not appear to be
                running the agent. Check to ensure that the
                agent is installed, running, and able to
                communicate with the service.
        """

        pending_instance_count: int = proto.Field(
            proto.INT64,
            number=1,
        )
        inactive_instance_count: int = proto.Field(
            proto.INT64,
            number=2,
        )
        notified_instance_count: int = proto.Field(
            proto.INT64,
            number=3,
        )
        started_instance_count: int = proto.Field(
            proto.INT64,
            number=4,
        )
        downloading_patches_instance_count: int = proto.Field(
            proto.INT64,
            number=5,
        )
        applying_patches_instance_count: int = proto.Field(
            proto.INT64,
            number=6,
        )
        rebooting_instance_count: int = proto.Field(
            proto.INT64,
            number=7,
        )
        succeeded_instance_count: int = proto.Field(
            proto.INT64,
            number=8,
        )
        succeeded_reboot_required_instance_count: int = proto.Field(
            proto.INT64,
            number=9,
        )
        failed_instance_count: int = proto.Field(
            proto.INT64,
            number=10,
        )
        acked_instance_count: int = proto.Field(
            proto.INT64,
            number=11,
        )
        timed_out_instance_count: int = proto.Field(
            proto.INT64,
            number=12,
        )
        pre_patch_step_instance_count: int = proto.Field(
            proto.INT64,
            number=13,
        )
        post_patch_step_instance_count: int = proto.Field(
            proto.INT64,
            number=14,
        )
        no_agent_detected_instance_count: int = proto.Field(
            proto.INT64,
            number=15,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=14,
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
    state: State = proto.Field(
        proto.ENUM,
        number=5,
        enum=State,
    )
    instance_filter: "PatchInstanceFilter" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="PatchInstanceFilter",
    )
    patch_config: "PatchConfig" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="PatchConfig",
    )
    duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=8,
        message=duration_pb2.Duration,
    )
    instance_details_summary: InstanceDetailsSummary = proto.Field(
        proto.MESSAGE,
        number=9,
        message=InstanceDetailsSummary,
    )
    dry_run: bool = proto.Field(
        proto.BOOL,
        number=10,
    )
    error_message: str = proto.Field(
        proto.STRING,
        number=11,
    )
    percent_complete: float = proto.Field(
        proto.DOUBLE,
        number=12,
    )
    patch_deployment: str = proto.Field(
        proto.STRING,
        number=15,
    )
    rollout: "PatchRollout" = proto.Field(
        proto.MESSAGE,
        number=16,
        message="PatchRollout",
    )


class PatchConfig(proto.Message):
    r"""Patch configuration specifications. Contains details on how
    to apply the patch(es) to a VM instance.

    Attributes:
        reboot_config (google.cloud.osconfig_v1.types.PatchConfig.RebootConfig):
            Post-patch reboot settings.
        apt (google.cloud.osconfig_v1.types.AptSettings):
            Apt update settings. Use this setting to override the
            default ``apt`` patch rules.
        yum (google.cloud.osconfig_v1.types.YumSettings):
            Yum update settings. Use this setting to override the
            default ``yum`` patch rules.
        goo (google.cloud.osconfig_v1.types.GooSettings):
            Goo update settings. Use this setting to override the
            default ``goo`` patch rules.
        zypper (google.cloud.osconfig_v1.types.ZypperSettings):
            Zypper update settings. Use this setting to override the
            default ``zypper`` patch rules.
        windows_update (google.cloud.osconfig_v1.types.WindowsUpdateSettings):
            Windows update settings. Use this override
            the default windows patch rules.
        pre_step (google.cloud.osconfig_v1.types.ExecStep):
            The ``ExecStep`` to run before the patch update.
        post_step (google.cloud.osconfig_v1.types.ExecStep):
            The ``ExecStep`` to run after the patch update.
        mig_instances_allowed (bool):
            Allows the patch job to run on Managed
            instance groups (MIGs).
    """

    class RebootConfig(proto.Enum):
        r"""Post-patch reboot settings.

        Values:
            REBOOT_CONFIG_UNSPECIFIED (0):
                The default behavior is DEFAULT.
            DEFAULT (1):
                The agent decides if a reboot is necessary by checking
                signals such as registry keys on Windows or
                ``/var/run/reboot-required`` on APT based systems. On RPM
                based systems, a set of core system package install times
                are compared with system boot time.
            ALWAYS (2):
                Always reboot the machine after the update
                completes.
            NEVER (3):
                Never reboot the machine after the update
                completes.
        """

        REBOOT_CONFIG_UNSPECIFIED = 0
        DEFAULT = 1
        ALWAYS = 2
        NEVER = 3

    reboot_config: RebootConfig = proto.Field(
        proto.ENUM,
        number=1,
        enum=RebootConfig,
    )
    apt: "AptSettings" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="AptSettings",
    )
    yum: "YumSettings" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="YumSettings",
    )
    goo: "GooSettings" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="GooSettings",
    )
    zypper: "ZypperSettings" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="ZypperSettings",
    )
    windows_update: "WindowsUpdateSettings" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="WindowsUpdateSettings",
    )
    pre_step: "ExecStep" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="ExecStep",
    )
    post_step: "ExecStep" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="ExecStep",
    )
    mig_instances_allowed: bool = proto.Field(
        proto.BOOL,
        number=10,
    )


class Instance(proto.Message):
    r"""Namespace for instance state enums."""

    class PatchState(proto.Enum):
        r"""Patch state of an instance.

        Values:
            PATCH_STATE_UNSPECIFIED (0):
                Unspecified.
            PENDING (1):
                The instance is not yet notified.
            INACTIVE (2):
                Instance is inactive and cannot be patched.
            NOTIFIED (3):
                The instance is notified that it should be
                patched.
            STARTED (4):
                The instance has started the patching
                process.
            DOWNLOADING_PATCHES (5):
                The instance is downloading patches.
            APPLYING_PATCHES (6):
                The instance is applying patches.
            REBOOTING (7):
                The instance is rebooting.
            SUCCEEDED (8):
                The instance has completed applying patches.
            SUCCEEDED_REBOOT_REQUIRED (9):
                The instance has completed applying patches
                but a reboot is required.
            FAILED (10):
                The instance has failed to apply the patch.
            ACKED (11):
                The instance acked the notification and will
                start shortly.
            TIMED_OUT (12):
                The instance exceeded the time out while
                applying the patch.
            RUNNING_PRE_PATCH_STEP (13):
                The instance is running the pre-patch step.
            RUNNING_POST_PATCH_STEP (14):
                The instance is running the post-patch step.
            NO_AGENT_DETECTED (15):
                The service could not detect the presence of
                the agent. Check to ensure that the agent is
                installed, running, and able to communicate with
                the service.
        """

        PATCH_STATE_UNSPECIFIED = 0
        PENDING = 1
        INACTIVE = 2
        NOTIFIED = 3
        STARTED = 4
        DOWNLOADING_PATCHES = 5
        APPLYING_PATCHES = 6
        REBOOTING = 7
        SUCCEEDED = 8
        SUCCEEDED_REBOOT_REQUIRED = 9
        FAILED = 10
        ACKED = 11
        TIMED_OUT = 12
        RUNNING_PRE_PATCH_STEP = 13
        RUNNING_POST_PATCH_STEP = 14
        NO_AGENT_DETECTED = 15


class CancelPatchJobRequest(proto.Message):
    r"""Message for canceling a patch job.

    Attributes:
        name (str):
            Required. Name of the patch in the form
            ``projects/*/patchJobs/*``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AptSettings(proto.Message):
    r"""Apt patching is completed by executing
    ``apt-get update && apt-get upgrade``. Additional options can be set
    to control how this is executed.

    Attributes:
        type_ (google.cloud.osconfig_v1.types.AptSettings.Type):
            By changing the type to DIST, the patching is performed
            using ``apt-get dist-upgrade`` instead.
        excludes (MutableSequence[str]):
            List of packages to exclude from update.
            These packages will be excluded
        exclusive_packages (MutableSequence[str]):
            An exclusive list of packages to be updated.
            These are the only packages that will be
            updated. If these packages are not installed,
            they will be ignored. This field cannot be
            specified with any other patch configuration
            fields.
    """

    class Type(proto.Enum):
        r"""Apt patch type.

        Values:
            TYPE_UNSPECIFIED (0):
                By default, upgrade will be performed.
            DIST (1):
                Runs ``apt-get dist-upgrade``.
            UPGRADE (2):
                Runs ``apt-get upgrade``.
        """

        TYPE_UNSPECIFIED = 0
        DIST = 1
        UPGRADE = 2

    type_: Type = proto.Field(
        proto.ENUM,
        number=1,
        enum=Type,
    )
    excludes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    exclusive_packages: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class YumSettings(proto.Message):
    r"""Yum patching is performed by executing ``yum update``. Additional
    options can be set to control how this is executed.

    Note that not all settings are supported on all platforms.

    Attributes:
        security (bool):
            Adds the ``--security`` flag to ``yum update``. Not
            supported on all platforms.
        minimal (bool):
            Will cause patch to run ``yum update-minimal`` instead.
        excludes (MutableSequence[str]):
            List of packages to exclude from update. These packages are
            excluded by using the yum ``--exclude`` flag.
        exclusive_packages (MutableSequence[str]):
            An exclusive list of packages to be updated.
            These are the only packages that will be
            updated. If these packages are not installed,
            they will be ignored. This field must not be
            specified with any other patch configuration
            fields.
    """

    security: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    minimal: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    excludes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    exclusive_packages: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )


class GooSettings(proto.Message):
    r"""Googet patching is performed by running ``googet update``."""


class ZypperSettings(proto.Message):
    r"""Zypper patching is performed by running ``zypper patch``. See also
    https://en.opensuse.org/SDB:Zypper_manual.

    Attributes:
        with_optional (bool):
            Adds the ``--with-optional`` flag to ``zypper patch``.
        with_update (bool):
            Adds the ``--with-update`` flag, to ``zypper patch``.
        categories (MutableSequence[str]):
            Install only patches with these categories.
            Common categories include security, recommended,
            and feature.
        severities (MutableSequence[str]):
            Install only patches with these severities.
            Common severities include critical, important,
            moderate, and low.
        excludes (MutableSequence[str]):
            List of patches to exclude from update.
        exclusive_patches (MutableSequence[str]):
            An exclusive list of patches to be updated. These are the
            only patches that will be installed using 'zypper patch
            patch:<patch_name>' command. This field must not be used
            with any other patch configuration fields.
    """

    with_optional: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    with_update: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    categories: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    severities: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    excludes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    exclusive_patches: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )


class WindowsUpdateSettings(proto.Message):
    r"""Windows patching is performed using the Windows Update Agent.

    Attributes:
        classifications (MutableSequence[google.cloud.osconfig_v1.types.WindowsUpdateSettings.Classification]):
            Only apply updates of these windows update
            classifications. If empty, all updates are
            applied.
        excludes (MutableSequence[str]):
            List of KBs to exclude from update.
        exclusive_patches (MutableSequence[str]):
            An exclusive list of kbs to be updated. These
            are the only patches that will be updated. This
            field must not be used with other patch
            configurations.
    """

    class Classification(proto.Enum):
        r"""Microsoft Windows update classifications as defined in [1]
        https://support.microsoft.com/en-us/help/824684/description-of-the-standard-terminology-that-is-used-to-describe-micro

        Values:
            CLASSIFICATION_UNSPECIFIED (0):
                Invalid. If classifications are included,
                they must be specified.
            CRITICAL (1):
                "A widely released fix for a specific problem that addresses
                a critical, non-security-related bug." [1]
            SECURITY (2):
                "A widely released fix for a product-specific,
                security-related vulnerability. Security vulnerabilities are
                rated by their severity. The severity rating is indicated in
                the Microsoft security bulletin as critical, important,
                moderate, or low." [1]
            DEFINITION (3):
                "A widely released and frequent software update that
                contains additions to a product's definition database.
                Definition databases are often used to detect objects that
                have specific attributes, such as malicious code, phishing
                websites, or junk mail." [1]
            DRIVER (4):
                "Software that controls the input and output of a device."
                [1]
            FEATURE_PACK (5):
                "New product functionality that is first distributed outside
                the context of a product release and that is typically
                included in the next full product release." [1]
            SERVICE_PACK (6):
                "A tested, cumulative set of all hotfixes, security updates,
                critical updates, and updates. Additionally, service packs
                may contain additional fixes for problems that are found
                internally since the release of the product. Service packs
                my also contain a limited number of customer-requested
                design changes or features." [1]
            TOOL (7):
                "A utility or feature that helps complete a task or set of
                tasks." [1]
            UPDATE_ROLLUP (8):
                "A tested, cumulative set of hotfixes, security updates,
                critical updates, and updates that are packaged together for
                easy deployment. A rollup generally targets a specific area,
                such as security, or a component of a product, such as
                Internet Information Services (IIS)." [1]
            UPDATE (9):
                "A widely released fix for a specific problem. An update
                addresses a noncritical, non-security-related bug." [1]
        """

        CLASSIFICATION_UNSPECIFIED = 0
        CRITICAL = 1
        SECURITY = 2
        DEFINITION = 3
        DRIVER = 4
        FEATURE_PACK = 5
        SERVICE_PACK = 6
        TOOL = 7
        UPDATE_ROLLUP = 8
        UPDATE = 9

    classifications: MutableSequence[Classification] = proto.RepeatedField(
        proto.ENUM,
        number=1,
        enum=Classification,
    )
    excludes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    exclusive_patches: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class ExecStep(proto.Message):
    r"""A step that runs an executable for a PatchJob.

    Attributes:
        linux_exec_step_config (google.cloud.osconfig_v1.types.ExecStepConfig):
            The ExecStepConfig for all Linux VMs targeted
            by the PatchJob.
        windows_exec_step_config (google.cloud.osconfig_v1.types.ExecStepConfig):
            The ExecStepConfig for all Windows VMs
            targeted by the PatchJob.
    """

    linux_exec_step_config: "ExecStepConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ExecStepConfig",
    )
    windows_exec_step_config: "ExecStepConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ExecStepConfig",
    )


class ExecStepConfig(proto.Message):
    r"""Common configurations for an ExecStep.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        local_path (str):
            An absolute path to the executable on the VM.

            This field is a member of `oneof`_ ``executable``.
        gcs_object (google.cloud.osconfig_v1.types.GcsObject):
            A Cloud Storage object containing the
            executable.

            This field is a member of `oneof`_ ``executable``.
        allowed_success_codes (MutableSequence[int]):
            Defaults to [0]. A list of possible return values that the
            execution can return to indicate a success.
        interpreter (google.cloud.osconfig_v1.types.ExecStepConfig.Interpreter):
            The script interpreter to use to run the script. If no
            interpreter is specified the script will be executed
            directly, which will likely only succeed for scripts with
            [shebang lines]
            (https://en.wikipedia.org/wiki/Shebang\_(Unix)).
    """

    class Interpreter(proto.Enum):
        r"""The interpreter used to execute the a file.

        Values:
            INTERPRETER_UNSPECIFIED (0):
                Invalid for a Windows ExecStepConfig. For a
                Linux ExecStepConfig, the interpreter will be
                parsed from the shebang line of the script if
                unspecified.
            SHELL (1):
                Indicates that the script is run with ``/bin/sh`` on Linux
                and ``cmd`` on Windows.
            POWERSHELL (2):
                Indicates that the file is run with PowerShell flags
                ``-NonInteractive``, ``-NoProfile``, and
                ``-ExecutionPolicy Bypass``.
        """

        INTERPRETER_UNSPECIFIED = 0
        SHELL = 1
        POWERSHELL = 2

    local_path: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="executable",
    )
    gcs_object: "GcsObject" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="executable",
        message="GcsObject",
    )
    allowed_success_codes: MutableSequence[int] = proto.RepeatedField(
        proto.INT32,
        number=3,
    )
    interpreter: Interpreter = proto.Field(
        proto.ENUM,
        number=4,
        enum=Interpreter,
    )


class GcsObject(proto.Message):
    r"""Cloud Storage object representation.

    Attributes:
        bucket (str):
            Required. Bucket of the Cloud Storage object.
        object_ (str):
            Required. Name of the Cloud Storage object.
        generation_number (int):
            Required. Generation number of the Cloud
            Storage object. This is used to ensure that the
            ExecStep specified by this PatchJob does not
            change.
    """

    bucket: str = proto.Field(
        proto.STRING,
        number=1,
    )
    object_: str = proto.Field(
        proto.STRING,
        number=2,
    )
    generation_number: int = proto.Field(
        proto.INT64,
        number=3,
    )


class PatchInstanceFilter(proto.Message):
    r"""A filter to target VM instances for patching. The targeted
    VMs must meet all criteria specified. So if both labels and
    zones are specified, the patch job targets only VMs with those
    labels and in those zones.

    Attributes:
        all_ (bool):
            Target all VM instances in the project. If
            true, no other criteria is permitted.
        group_labels (MutableSequence[google.cloud.osconfig_v1.types.PatchInstanceFilter.GroupLabel]):
            Targets VM instances matching ANY of these
            GroupLabels. This allows targeting of disparate
            groups of VM instances.
        zones (MutableSequence[str]):
            Targets VM instances in ANY of these zones.
            Leave empty to target VM instances in any zone.
        instances (MutableSequence[str]):
            Targets any of the VM instances specified. Instances are
            specified by their URI in the form
            ``zones/[ZONE]/instances/[INSTANCE_NAME]``,
            ``projects/[PROJECT_ID]/zones/[ZONE]/instances/[INSTANCE_NAME]``,
            or
            ``https://www.googleapis.com/compute/v1/projects/[PROJECT_ID]/zones/[ZONE]/instances/[INSTANCE_NAME]``
        instance_name_prefixes (MutableSequence[str]):
            Targets VMs whose name starts with one of
            these prefixes. Similar to labels, this is
            another way to group VMs when targeting configs,
            for example prefix="prod-".
    """

    class GroupLabel(proto.Message):
        r"""Targets a group of VM instances by using their `assigned
        labels <https://cloud.google.com/compute/docs/labeling-resources>`__.
        Labels are key-value pairs. A ``GroupLabel`` is a combination of
        labels that is used to target VMs for a patch job.

        For example, a patch job can target VMs that have the following
        ``GroupLabel``: ``{"env":"test", "app":"web"}``. This means that the
        patch job is applied to VMs that have both the labels ``env=test``
        and ``app=web``.

        Attributes:
            labels (MutableMapping[str, str]):
                Compute Engine instance labels that must be
                present for a VM instance to be targeted by this
                filter.
        """

        labels: MutableMapping[str, str] = proto.MapField(
            proto.STRING,
            proto.STRING,
            number=1,
        )

    all_: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    group_labels: MutableSequence[GroupLabel] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=GroupLabel,
    )
    zones: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    instances: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    instance_name_prefixes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )


class PatchRollout(proto.Message):
    r"""Patch rollout configuration specifications. Contains details
    on the concurrency control when applying patch(es) to all
    targeted VMs.

    Attributes:
        mode (google.cloud.osconfig_v1.types.PatchRollout.Mode):
            Mode of the patch rollout.
        disruption_budget (google.cloud.osconfig_v1.types.FixedOrPercent):
            The maximum number (or percentage) of VMs per zone to
            disrupt at any given moment. The number of VMs calculated
            from multiplying the percentage by the total number of VMs
            in a zone is rounded up.

            During patching, a VM is considered disrupted from the time
            the agent is notified to begin until patching has completed.
            This disruption time includes the time to complete reboot
            and any post-patch steps.

            A VM contributes to the disruption budget if its patching
            operation fails either when applying the patches, running
            pre or post patch steps, or if it fails to respond with a
            success notification before timing out. VMs that are not
            running or do not have an active agent do not count toward
            this disruption budget.

            For zone-by-zone rollouts, if the disruption budget in a
            zone is exceeded, the patch job stops, because continuing to
            the next zone requires completion of the patch process in
            the previous zone.

            For example, if the disruption budget has a fixed value of
            ``10``, and 8 VMs fail to patch in the current zone, the
            patch job continues to patch 2 VMs at a time until the zone
            is completed. When that zone is completed successfully,
            patching begins with 10 VMs at a time in the next zone. If
            10 VMs in the next zone fail to patch, the patch job stops.
    """

    class Mode(proto.Enum):
        r"""Type of the rollout.

        Values:
            MODE_UNSPECIFIED (0):
                Mode must be specified.
            ZONE_BY_ZONE (1):
                Patches are applied one zone at a time. The
                patch job begins in the region with the lowest
                number of targeted VMs. Within the region,
                patching begins in the zone with the lowest
                number of targeted VMs. If multiple regions (or
                zones within a region) have the same number of
                targeted VMs, a tie-breaker is achieved by
                sorting the regions or zones in alphabetical
                order.
            CONCURRENT_ZONES (2):
                Patches are applied to VMs in all zones at
                the same time.
        """

        MODE_UNSPECIFIED = 0
        ZONE_BY_ZONE = 1
        CONCURRENT_ZONES = 2

    mode: Mode = proto.Field(
        proto.ENUM,
        number=1,
        enum=Mode,
    )
    disruption_budget: osconfig_common.FixedOrPercent = proto.Field(
        proto.MESSAGE,
        number=2,
        message=osconfig_common.FixedOrPercent,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
