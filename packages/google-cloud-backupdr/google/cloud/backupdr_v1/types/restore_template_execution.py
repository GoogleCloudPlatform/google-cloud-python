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
import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.backupdr_v1.types import (
    restore_template_common,
    restore_verification_plan,
)

__protobuf__ = proto.module(
    package="google.cloud.backupdr.v1",
    manifest={
        "PhaseState",
        "RestoreTemplateExecution",
        "PreparePhaseInfo",
        "PreRestorePhaseInfo",
        "RestorePhaseInfo",
        "PostRestorePhaseInfo",
        "VerificationPhaseInfo",
        "CleanupPhaseInfo",
        "GetRestoreTemplateExecutionRequest",
        "TriggerRestoreCleanupRequest",
        "ListRestoreTemplateExecutionsRequest",
        "ListRestoreTemplateExecutionsResponse",
    },
)


class PhaseState(proto.Enum):
    r"""Represents the state of a specific phase (RUNNING, SUCCEEDED,
    FAILED, etc.).

    Values:
        PHASE_STATE_UNSPECIFIED (0):
            Phase state is not set.
        PENDING (1):
            This phase is pending execution.
        RUNNING (2):
            The phase is actively executing.
        SUCCEEDED (3):
            The phase completed successfully.
        FAILED (4):
            The phase encountered an error and failed.
        TIMED_OUT (5):
            The phase timed out.
        SKIPPED (6):
            The phase was skipped.
        WAITING (7):
            The phase is waiting to be executed.
    """

    PHASE_STATE_UNSPECIFIED = 0
    PENDING = 1
    RUNNING = 2
    SUCCEEDED = 3
    FAILED = 4
    TIMED_OUT = 5
    SKIPPED = 6
    WAITING = 7


class RestoreTemplateExecution(proto.Message):
    r"""A ``RestoreTemplateExecution`` represents a single historical or
    active execution run.

    Attributes:
        name (str):
            Identifier. Resource name of the execution.
        resource_type (str):
            Output only. The workload resource type being restored. The
            format is "{service_name}/{resource_kind}", for example,
            "compute.googleapis.com/Instance".
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create time of the execution.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Update time of the execution.
        type_ (google.cloud.backupdr_v1.types.RestoreTemplateExecution.ExecutionType):
            Output only. The type of the execution.
        phase (google.cloud.backupdr_v1.types.RestoreTemplateExecution.ExecutionPhase):
            Output only. The current active phase.
        state (google.cloud.backupdr_v1.types.RestoreTemplateExecution.ExecutionState):
            Output only. State of the execution.
        prepare_phase_info (google.cloud.backupdr_v1.types.PreparePhaseInfo):
            Output only. Info for the prepare phase.
        pre_restore_phase_info (google.cloud.backupdr_v1.types.PreRestorePhaseInfo):
            Output only. Info for the pre-restore phase.
        restore_phase_info (google.cloud.backupdr_v1.types.RestorePhaseInfo):
            Output only. Info for the restore phase.
        post_restore_phase_info (google.cloud.backupdr_v1.types.PostRestorePhaseInfo):
            Output only. Info for the post-restore phase.
        verification_phase_info (google.cloud.backupdr_v1.types.VerificationPhaseInfo):
            Output only. Info for the verification phase.
        cleanup_phase_info (google.cloud.backupdr_v1.types.CleanupPhaseInfo):
            Output only. Info for the cleanup phase.
    """

    class ExecutionType(proto.Enum):
        r"""The type of execution.

        Values:
            EXECUTION_TYPE_UNSPECIFIED (0):
                Execution type not specified.
            SCHEDULED (1):
                Scheduled execution.
            ON_DEMAND (2):
                On-demand execution.
        """

        EXECUTION_TYPE_UNSPECIFIED = 0
        SCHEDULED = 1
        ON_DEMAND = 2

    class ExecutionPhase(proto.Enum):
        r"""The phase of execution.

        Values:
            EXECUTION_PHASE_UNSPECIFIED (0):
                Execution phase not specified.
            PREPARING (1):
                Preparing for execution.
            EXECUTING_PRE_RESTORE_ACTION (2):
                Executing pre-restore action.
            RESTORING (3):
                Restoring the resource.
            EXECUTING_POST_RESTORE_ACTION (4):
                Executing post-restore action.
            VERIFYING (5):
                Verifying the restored resource.
            CLEANING_UP (6):
                Cleaning up resources.
            COMPLETED (7):
                Execution completed.
        """

        EXECUTION_PHASE_UNSPECIFIED = 0
        PREPARING = 1
        EXECUTING_PRE_RESTORE_ACTION = 2
        RESTORING = 3
        EXECUTING_POST_RESTORE_ACTION = 4
        VERIFYING = 5
        CLEANING_UP = 6
        COMPLETED = 7

    class ExecutionState(proto.Enum):
        r"""State of the execution.

        Values:
            EXECUTION_STATE_UNSPECIFIED (0):
                State not set.
            RUNNING (1):
                Execution is running.
            SUCCEEDED (2):
                Execution succeeded.
            FAILED (3):
                Execution failed.
            DELETING (4):
                Resources are being deleted (cleanup).
        """

        EXECUTION_STATE_UNSPECIFIED = 0
        RUNNING = 1
        SUCCEEDED = 2
        FAILED = 3
        DELETING = 4

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    resource_type: str = proto.Field(
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
    type_: ExecutionType = proto.Field(
        proto.ENUM,
        number=5,
        enum=ExecutionType,
    )
    phase: ExecutionPhase = proto.Field(
        proto.ENUM,
        number=6,
        enum=ExecutionPhase,
    )
    state: ExecutionState = proto.Field(
        proto.ENUM,
        number=7,
        enum=ExecutionState,
    )
    prepare_phase_info: "PreparePhaseInfo" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="PreparePhaseInfo",
    )
    pre_restore_phase_info: "PreRestorePhaseInfo" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="PreRestorePhaseInfo",
    )
    restore_phase_info: "RestorePhaseInfo" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="RestorePhaseInfo",
    )
    post_restore_phase_info: "PostRestorePhaseInfo" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="PostRestorePhaseInfo",
    )
    verification_phase_info: "VerificationPhaseInfo" = proto.Field(
        proto.MESSAGE,
        number=12,
        message="VerificationPhaseInfo",
    )
    cleanup_phase_info: "CleanupPhaseInfo" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="CleanupPhaseInfo",
    )


class PreparePhaseInfo(proto.Message):
    r"""Info for Prepare phase execution.

    Attributes:
        phase_state (google.cloud.backupdr_v1.types.PhaseState):
            Output only. The state of this phase.
        error (google.rpc.status_pb2.Status):
            Output only. Error details if the phase
            failed.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Start time of the phase.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. End time of the phase.
        backup_selection_config (google.cloud.backupdr_v1.types.BackupSelectionConfig):
            Output only. Snapshot of config used in this
            execution.
        backup (str):
            Output only. The source backup used for the
            restore. The fully qualified URI of the backupdr
            backup.
        is_backup_explicitly_passed (bool):
            Output only. Indicates whether the backup was
            explicitly passed in the request.
        restore_verification_plan_association (str):
            Output only. The restore verification plan
            association associated with the execution.
    """

    phase_state: "PhaseState" = proto.Field(
        proto.ENUM,
        number=1,
        enum="PhaseState",
    )
    error: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=2,
        message=status_pb2.Status,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    backup_selection_config: restore_template_common.BackupSelectionConfig = (
        proto.Field(
            proto.MESSAGE,
            number=5,
            message=restore_template_common.BackupSelectionConfig,
        )
    )
    backup: str = proto.Field(
        proto.STRING,
        number=6,
    )
    is_backup_explicitly_passed: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    restore_verification_plan_association: str = proto.Field(
        proto.STRING,
        number=8,
    )


class PreRestorePhaseInfo(proto.Message):
    r"""Info for Pre-Restore phase execution.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        phase_state (google.cloud.backupdr_v1.types.PhaseState):
            Output only. The state of this phase.
        error (google.rpc.status_pb2.Status):
            Output only. Error details if the phase
            failed.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Start time of the phase.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. End time of the phase.
        pre_restore_config (google.cloud.backupdr_v1.types.PreRestoreConfig):
            Output only. Snapshot of config that will be
            executed before restore operation.
        cloud_run_execution (str):
            Output only. The fully qualified URI of the
            Cloud Run Execution triggered for pre-restore
            actions.

            This field is a member of `oneof`_ ``result``.
    """

    phase_state: "PhaseState" = proto.Field(
        proto.ENUM,
        number=1,
        enum="PhaseState",
    )
    error: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=2,
        message=status_pb2.Status,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    pre_restore_config: restore_template_common.PreRestoreConfig = proto.Field(
        proto.MESSAGE,
        number=5,
        message=restore_template_common.PreRestoreConfig,
    )
    cloud_run_execution: str = proto.Field(
        proto.STRING,
        number=6,
        oneof="result",
    )


class RestorePhaseInfo(proto.Message):
    r"""Info for Restore phase execution.

    Attributes:
        phase_state (google.cloud.backupdr_v1.types.PhaseState):
            Output only. The state of this phase.
        error (google.rpc.status_pb2.Status):
            Output only. Error details if the phase
            failed.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Start time of the phase.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. End time of the phase.
        restore_properties (google.protobuf.struct_pb2.Struct):
            Output only. Snapshot of environment config
            used during restore of this
            RestoreTemplateExecution.
        restore_resource (str):
            Output only. The resource created or restored
            by this execution.
        restore_duration (google.protobuf.duration_pb2.Duration):
            Output only. Time taken to restore the
            resource.
    """

    phase_state: "PhaseState" = proto.Field(
        proto.ENUM,
        number=1,
        enum="PhaseState",
    )
    error: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=2,
        message=status_pb2.Status,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    restore_properties: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=5,
        message=struct_pb2.Struct,
    )
    restore_resource: str = proto.Field(
        proto.STRING,
        number=7,
    )
    restore_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=8,
        message=duration_pb2.Duration,
    )


class PostRestorePhaseInfo(proto.Message):
    r"""Info for Post-Restore phase execution.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        phase_state (google.cloud.backupdr_v1.types.PhaseState):
            Output only. The state of this phase.
        error (google.rpc.status_pb2.Status):
            Output only. Error details if the phase
            failed.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Start time of the phase.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. End time of the phase.
        post_restore_config (google.cloud.backupdr_v1.types.PostRestoreConfig):
            Output only. Snapshot of config that will be
            executed after successful restore operation.
        cloud_run_execution (str):
            Output only. The fully qualified URI of the
            Cloud Run Execution triggered for post-restore
            actions.

            This field is a member of `oneof`_ ``result``.
    """

    phase_state: "PhaseState" = proto.Field(
        proto.ENUM,
        number=1,
        enum="PhaseState",
    )
    error: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=2,
        message=status_pb2.Status,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    post_restore_config: restore_template_common.PostRestoreConfig = proto.Field(
        proto.MESSAGE,
        number=5,
        message=restore_template_common.PostRestoreConfig,
    )
    cloud_run_execution: str = proto.Field(
        proto.STRING,
        number=6,
        oneof="result",
    )


class VerificationPhaseInfo(proto.Message):
    r"""Info for Verification phase execution.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        phase_state (google.cloud.backupdr_v1.types.PhaseState):
            Output only. The state of this phase.
        error (google.rpc.status_pb2.Status):
            Output only. Error details if the phase
            failed.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Start time of the phase.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. End time of the phase.
        verification_config (google.cloud.backupdr_v1.types.VerificationConfig):
            Output only. Snapshot of config that will be
            executed after successful post restore
            validation.
        cloud_run_execution (str):
            Output only. The fully qualified URI of the
            Cloud Run Execution triggered for verification.

            This field is a member of `oneof`_ ``result``.
    """

    phase_state: "PhaseState" = proto.Field(
        proto.ENUM,
        number=1,
        enum="PhaseState",
    )
    error: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=2,
        message=status_pb2.Status,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    verification_config: restore_template_common.VerificationConfig = proto.Field(
        proto.MESSAGE,
        number=5,
        message=restore_template_common.VerificationConfig,
    )
    cloud_run_execution: str = proto.Field(
        proto.STRING,
        number=6,
        oneof="result",
    )


class CleanupPhaseInfo(proto.Message):
    r"""Info for Cleanup phase execution.

    Attributes:
        phase_state (google.cloud.backupdr_v1.types.PhaseState):
            Output only. The state of this phase.
        error (google.rpc.status_pb2.Status):
            Output only. Error details if the phase
            failed.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Start time of the phase.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. End time of the phase.
        cleanup_duration (google.protobuf.duration_pb2.Duration):
            Output only. Time taken to perform the
            cleanup of restored resource.
        success_cleanup_rule (google.cloud.backupdr_v1.types.RestoreVerificationCleanupRule):
            Output only. Snapshot of cleanup rule
            provided for this execution when execution is
            successful.
        failure_cleanup_rule (google.cloud.backupdr_v1.types.RestoreVerificationCleanupRule):
            Output only. Snapshot of cleanup rule
            provided for this execution when execution is
            failed.
        cleanup_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the resources will
            be cleaned up.
    """

    phase_state: "PhaseState" = proto.Field(
        proto.ENUM,
        number=1,
        enum="PhaseState",
    )
    error: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=2,
        message=status_pb2.Status,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    cleanup_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=5,
        message=duration_pb2.Duration,
    )
    success_cleanup_rule: restore_verification_plan.RestoreVerificationCleanupRule = (
        proto.Field(
            proto.MESSAGE,
            number=6,
            message=restore_verification_plan.RestoreVerificationCleanupRule,
        )
    )
    failure_cleanup_rule: restore_verification_plan.RestoreVerificationCleanupRule = (
        proto.Field(
            proto.MESSAGE,
            number=7,
            message=restore_verification_plan.RestoreVerificationCleanupRule,
        )
    )
    cleanup_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )


class GetRestoreTemplateExecutionRequest(proto.Message):
    r"""Request message for getting a RestoreTemplateExecution
    instance.

    Attributes:
        name (str):
            Required. The name of the restore template execution to
            retrieve. Format:
            'projects/{project_id}/locations/{location}/restoreTemplates/{restore_template_id}/executions/{execution_id}'
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class TriggerRestoreCleanupRequest(proto.Message):
    r"""Request message for triggering a restore cleanup.

    Attributes:
        name (str):
            Required. Name of the restore template execution. Format:
            'projects/{project_id}/locations/{location}/restoreTemplates/{restore_template_id}/executions/{execution_id}'
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.

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


class ListRestoreTemplateExecutionsRequest(proto.Message):
    r"""Request message for listing RestoreTemplateExecutions.

    Attributes:
        parent (str):
            Required. The project, location, and restore template for
            which to retrieve executions information. Format:
            ``projects/{project}/locations/{location}/restoreTemplates/{restore_template}``.
        page_size (int):
            Optional. Requested page size.
        page_token (str):
            Optional. A token identifying a page of
            results.
        filter (str):
            Optional. Filtering results.
        order_by (str):
            Optional. Hint for how to order the results.
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


class ListRestoreTemplateExecutionsResponse(proto.Message):
    r"""Response message for listing RestoreTemplateExecutions.

    Attributes:
        restore_template_executions (MutableSequence[google.cloud.backupdr_v1.types.RestoreTemplateExecution]):
            The list of RestoreTemplateExecution
            instances.
        next_page_token (str):
            A token identifying a page of results.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    restore_template_executions: MutableSequence["RestoreTemplateExecution"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="RestoreTemplateExecution",
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


__all__ = tuple(sorted(__protobuf__.manifest))
