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

from google.cloud.notebooks_v1.types import diagnostic_config as gcn_diagnostic_config
from google.cloud.notebooks_v1.types import environment as gcn_environment
from google.cloud.notebooks_v1.types import execution as gcn_execution
from google.cloud.notebooks_v1.types import instance as gcn_instance
from google.cloud.notebooks_v1.types import instance_config
from google.cloud.notebooks_v1.types import schedule as gcn_schedule

__protobuf__ = proto.module(
    package="google.cloud.notebooks.v1",
    manifest={
        "UpgradeType",
        "OperationMetadata",
        "ListInstancesRequest",
        "ListInstancesResponse",
        "GetInstanceRequest",
        "CreateInstanceRequest",
        "RegisterInstanceRequest",
        "SetInstanceAcceleratorRequest",
        "SetInstanceMachineTypeRequest",
        "UpdateInstanceConfigRequest",
        "SetInstanceLabelsRequest",
        "UpdateInstanceMetadataItemsRequest",
        "UpdateInstanceMetadataItemsResponse",
        "UpdateShieldedInstanceConfigRequest",
        "DeleteInstanceRequest",
        "StartInstanceRequest",
        "StopInstanceRequest",
        "ResetInstanceRequest",
        "ReportInstanceInfoRequest",
        "IsInstanceUpgradeableRequest",
        "IsInstanceUpgradeableResponse",
        "GetInstanceHealthRequest",
        "GetInstanceHealthResponse",
        "UpgradeInstanceRequest",
        "RollbackInstanceRequest",
        "UpgradeInstanceInternalRequest",
        "ListEnvironmentsRequest",
        "DiagnoseInstanceRequest",
        "ListEnvironmentsResponse",
        "GetEnvironmentRequest",
        "CreateEnvironmentRequest",
        "DeleteEnvironmentRequest",
        "ListSchedulesRequest",
        "ListSchedulesResponse",
        "GetScheduleRequest",
        "DeleteScheduleRequest",
        "CreateScheduleRequest",
        "TriggerScheduleRequest",
        "ListExecutionsRequest",
        "ListExecutionsResponse",
        "GetExecutionRequest",
        "DeleteExecutionRequest",
        "CreateExecutionRequest",
    },
)


class UpgradeType(proto.Enum):
    r"""Definition of the types of upgrade that can be used on this
    instance.

    Values:
        UPGRADE_TYPE_UNSPECIFIED (0):
            Upgrade type is not specified.
        UPGRADE_FRAMEWORK (1):
            Upgrade ML framework.
        UPGRADE_OS (2):
            Upgrade Operating System.
        UPGRADE_CUDA (3):
            Upgrade CUDA.
        UPGRADE_ALL (4):
            Upgrade All (OS, Framework and CUDA).
    """

    UPGRADE_TYPE_UNSPECIFIED = 0
    UPGRADE_FRAMEWORK = 1
    UPGRADE_OS = 2
    UPGRADE_CUDA = 3
    UPGRADE_ALL = 4


class OperationMetadata(proto.Message):
    r"""Represents the metadata of the long-running operation.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the operation was created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the operation finished running.
        target (str):
            Server-defined resource path for the target
            of the operation.
        verb (str):
            Name of the verb executed by the operation.
        status_message (str):
            Human-readable status of the operation, if
            any.
        requested_cancellation (bool):
            Identifies whether the user has requested cancellation of
            the operation. Operations that have successfully been
            cancelled have [Operation.error][] value with a
            [google.rpc.Status.code][google.rpc.Status.code] of 1,
            corresponding to ``Code.CANCELLED``.
        api_version (str):
            API version used to start the operation.
        endpoint (str):
            API endpoint name of this operation.
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
    endpoint: str = proto.Field(
        proto.STRING,
        number=8,
    )


class ListInstancesRequest(proto.Message):
    r"""Request for listing notebook instances.

    Attributes:
        parent (str):
            Required. Format:
            ``parent=projects/{project_id}/locations/{location}``
        page_size (int):
            Maximum return size of the list call.
        page_token (str):
            A previous returned page token that can be
            used to continue listing from the last result.
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


class ListInstancesResponse(proto.Message):
    r"""Response for listing notebook instances.

    Attributes:
        instances (MutableSequence[google.cloud.notebooks_v1.types.Instance]):
            A list of returned instances.
        next_page_token (str):
            Page token that can be used to continue
            listing from the last result in the next list
            call.
        unreachable (MutableSequence[str]):
            Locations that could not be reached. For example,
            ``['us-west1-a', 'us-central1-b']``. A ListInstancesResponse
            will only contain either instances or unreachables,
    """

    @property
    def raw_page(self):
        return self

    instances: MutableSequence[gcn_instance.Instance] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcn_instance.Instance,
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
    r"""Request for getting a notebook instance.

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateInstanceRequest(proto.Message):
    r"""Request for creating a notebook instance.

    Attributes:
        parent (str):
            Required. Format:
            ``parent=projects/{project_id}/locations/{location}``
        instance_id (str):
            Required. User-defined unique ID of this
            instance.
        instance (google.cloud.notebooks_v1.types.Instance):
            Required. The instance to be created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    instance: gcn_instance.Instance = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcn_instance.Instance,
    )


class RegisterInstanceRequest(proto.Message):
    r"""Request for registering a notebook instance.

    Attributes:
        parent (str):
            Required. Format:
            ``parent=projects/{project_id}/locations/{location}``
        instance_id (str):
            Required. User defined unique ID of this instance. The
            ``instance_id`` must be 1 to 63 characters long and contain
            only lowercase letters, numeric characters, and dashes. The
            first character must be a lowercase letter and the last
            character cannot be a dash.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SetInstanceAcceleratorRequest(proto.Message):
    r"""Request for setting instance accelerator.

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
        type_ (google.cloud.notebooks_v1.types.Instance.AcceleratorType):
            Required. Type of this accelerator.
        core_count (int):
            Required. Count of cores of this accelerator. Note that not
            all combinations of ``type`` and ``core_count`` are valid.
            Check `GPUs on Compute
            Engine <https://cloud.google.com/compute/docs/gpus/#gpus-list>`__
            to find a valid combination. TPUs are not supported.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: gcn_instance.Instance.AcceleratorType = proto.Field(
        proto.ENUM,
        number=2,
        enum=gcn_instance.Instance.AcceleratorType,
    )
    core_count: int = proto.Field(
        proto.INT64,
        number=3,
    )


class SetInstanceMachineTypeRequest(proto.Message):
    r"""Request for setting instance machine type.

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
        machine_type (str):
            Required. The `Compute Engine machine
            type <https://cloud.google.com/compute/docs/machine-types>`__.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    machine_type: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateInstanceConfigRequest(proto.Message):
    r"""Request for updating instance configurations.

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
        config (google.cloud.notebooks_v1.types.InstanceConfig):
            The instance configurations to be updated.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    config: instance_config.InstanceConfig = proto.Field(
        proto.MESSAGE,
        number=2,
        message=instance_config.InstanceConfig,
    )


class SetInstanceLabelsRequest(proto.Message):
    r"""Request for setting instance labels.

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
        labels (MutableMapping[str, str]):
            Labels to apply to this instance.
            These can be later modified by the setLabels
            method
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )


class UpdateInstanceMetadataItemsRequest(proto.Message):
    r"""Request for adding/changing metadata items  for an instance.

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
        items (MutableMapping[str, str]):
            Metadata items to add/update for the
            instance.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    items: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )


class UpdateInstanceMetadataItemsResponse(proto.Message):
    r"""Response for adding/changing metadata items for an instance.

    Attributes:
        items (MutableMapping[str, str]):
            Map of items that were added/updated to/in
            the metadata.
    """

    items: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=1,
    )


class UpdateShieldedInstanceConfigRequest(proto.Message):
    r"""Request for updating the Shielded Instance config for a
    notebook instance. You can only use this method on a stopped
    instance

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
        shielded_instance_config (google.cloud.notebooks_v1.types.Instance.ShieldedInstanceConfig):
            ShieldedInstance configuration to be updated.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    shielded_instance_config: gcn_instance.Instance.ShieldedInstanceConfig = (
        proto.Field(
            proto.MESSAGE,
            number=2,
            message=gcn_instance.Instance.ShieldedInstanceConfig,
        )
    )


class DeleteInstanceRequest(proto.Message):
    r"""Request for deleting a notebook instance.

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class StartInstanceRequest(proto.Message):
    r"""Request for starting a notebook instance

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class StopInstanceRequest(proto.Message):
    r"""Request for stopping a notebook instance

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ResetInstanceRequest(proto.Message):
    r"""Request for resetting a notebook instance

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ReportInstanceInfoRequest(proto.Message):
    r"""Request for notebook instances to report information to
    Notebooks API.

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
        vm_id (str):
            Required. The VM hardware token for
            authenticating the VM.
            https://cloud.google.com/compute/docs/instances/verifying-instance-identity
        metadata (MutableMapping[str, str]):
            The metadata reported to Notebooks API. This
            will be merged to the instance metadata store
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    vm_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    metadata: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )


class IsInstanceUpgradeableRequest(proto.Message):
    r"""Request for checking if a notebook instance is upgradeable.

    Attributes:
        notebook_instance (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
        type_ (google.cloud.notebooks_v1.types.UpgradeType):
            Optional. The optional UpgradeType. Setting
            this field will search for additional compute
            images to upgrade this instance.
    """

    notebook_instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: "UpgradeType" = proto.Field(
        proto.ENUM,
        number=2,
        enum="UpgradeType",
    )


class IsInstanceUpgradeableResponse(proto.Message):
    r"""Response for checking if a notebook instance is upgradeable.

    Attributes:
        upgradeable (bool):
            If an instance is upgradeable.
        upgrade_version (str):
            The version this instance will be upgraded to
            if calling the upgrade endpoint. This field will
            only be populated if field upgradeable is true.
        upgrade_info (str):
            Additional information about upgrade.
        upgrade_image (str):
            The new image self link this instance will be
            upgraded to if calling the upgrade endpoint.
            This field will only be populated if field
            upgradeable is true.
    """

    upgradeable: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    upgrade_version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    upgrade_info: str = proto.Field(
        proto.STRING,
        number=3,
    )
    upgrade_image: str = proto.Field(
        proto.STRING,
        number=4,
    )


class GetInstanceHealthRequest(proto.Message):
    r"""Request for checking if a notebook instance is healthy.

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetInstanceHealthResponse(proto.Message):
    r"""Response for checking if a notebook instance is healthy.

    Attributes:
        health_state (google.cloud.notebooks_v1.types.GetInstanceHealthResponse.HealthState):
            Output only. Runtime health_state.
        health_info (MutableMapping[str, str]):
            Output only. Additional information about instance health.
            Example: healthInfo": { "docker_proxy_agent_status": "1",
            "docker_status": "1", "jupyterlab_api_status": "-1",
            "jupyterlab_status": "-1", "updated": "2020-10-18
            09:40:03.573409" }
    """

    class HealthState(proto.Enum):
        r"""If an instance is healthy or not.

        Values:
            HEALTH_STATE_UNSPECIFIED (0):
                The instance substate is unknown.
            HEALTHY (1):
                The instance is known to be in an healthy
                state (for example, critical daemons are
                running) Applies to ACTIVE state.
            UNHEALTHY (2):
                The instance is known to be in an unhealthy
                state (for example, critical daemons are not
                running) Applies to ACTIVE state.
            AGENT_NOT_INSTALLED (3):
                The instance has not installed health
                monitoring agent. Applies to ACTIVE state.
            AGENT_NOT_RUNNING (4):
                The instance health monitoring agent is not
                running. Applies to ACTIVE state.
        """

        HEALTH_STATE_UNSPECIFIED = 0
        HEALTHY = 1
        UNHEALTHY = 2
        AGENT_NOT_INSTALLED = 3
        AGENT_NOT_RUNNING = 4

    health_state: HealthState = proto.Field(
        proto.ENUM,
        number=1,
        enum=HealthState,
    )
    health_info: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )


class UpgradeInstanceRequest(proto.Message):
    r"""Request for upgrading a notebook instance

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
        type_ (google.cloud.notebooks_v1.types.UpgradeType):
            Optional. The optional UpgradeType. Setting
            this field will search for additional compute
            images to upgrade this instance.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: "UpgradeType" = proto.Field(
        proto.ENUM,
        number=2,
        enum="UpgradeType",
    )


class RollbackInstanceRequest(proto.Message):
    r"""Request for rollbacking a notebook instance

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
        target_snapshot (str):
            Required. The snapshot for rollback. Example:
            ``projects/test-project/global/snapshots/krwlzipynril``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    target_snapshot: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpgradeInstanceInternalRequest(proto.Message):
    r"""Request for upgrading a notebook instance from within the VM

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
        vm_id (str):
            Required. The VM hardware token for
            authenticating the VM.
            https://cloud.google.com/compute/docs/instances/verifying-instance-identity
        type_ (google.cloud.notebooks_v1.types.UpgradeType):
            Optional. The optional UpgradeType. Setting
            this field will search for additional compute
            images to upgrade this instance.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    vm_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    type_: "UpgradeType" = proto.Field(
        proto.ENUM,
        number=3,
        enum="UpgradeType",
    )


class ListEnvironmentsRequest(proto.Message):
    r"""Request for listing environments.

    Attributes:
        parent (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}``
        page_size (int):
            Maximum return size of the list call.
        page_token (str):
            A previous returned page token that can be
            used to continue listing from the last result.
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


class DiagnoseInstanceRequest(proto.Message):
    r"""Request for creating a notebook instance diagnostic file.

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
        diagnostic_config (google.cloud.notebooks_v1.types.DiagnosticConfig):
            Required. Defines flags that are used to run
            the diagnostic tool
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    diagnostic_config: gcn_diagnostic_config.DiagnosticConfig = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcn_diagnostic_config.DiagnosticConfig,
    )


class ListEnvironmentsResponse(proto.Message):
    r"""Response for listing environments.

    Attributes:
        environments (MutableSequence[google.cloud.notebooks_v1.types.Environment]):
            A list of returned environments.
        next_page_token (str):
            A page token that can be used to continue
            listing from the last result in the next list
            call.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    environments: MutableSequence[gcn_environment.Environment] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcn_environment.Environment,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetEnvironmentRequest(proto.Message):
    r"""Request for getting a notebook environment.

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/environments/{environment_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateEnvironmentRequest(proto.Message):
    r"""Request for creating a notebook environment.

    Attributes:
        parent (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}``
        environment_id (str):
            Required. User-defined unique ID of this environment. The
            ``environment_id`` must be 1 to 63 characters long and
            contain only lowercase letters, numeric characters, and
            dashes. The first character must be a lowercase letter and
            the last character cannot be a dash.
        environment (google.cloud.notebooks_v1.types.Environment):
            Required. The environment to be created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    environment_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    environment: gcn_environment.Environment = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcn_environment.Environment,
    )


class DeleteEnvironmentRequest(proto.Message):
    r"""Request for deleting a notebook environment.

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/environments/{environment_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListSchedulesRequest(proto.Message):
    r"""Request for listing scheduled notebook job.

    Attributes:
        parent (str):
            Required. Format:
            ``parent=projects/{project_id}/locations/{location}``
        page_size (int):
            Maximum return size of the list call.
        page_token (str):
            A previous returned page token that can be
            used to continue listing from the last result.
        filter (str):
            Filter applied to resulting schedules.
        order_by (str):
            Field to order results by.
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


class ListSchedulesResponse(proto.Message):
    r"""Response for listing scheduled notebook job.

    Attributes:
        schedules (MutableSequence[google.cloud.notebooks_v1.types.Schedule]):
            A list of returned instances.
        next_page_token (str):
            Page token that can be used to continue
            listing from the last result in the next list
            call.
        unreachable (MutableSequence[str]):
            Schedules that could not be reached. For example:

            ::

                ['projects/{project_id}/location/{location}/schedules/monthly_digest',
                 'projects/{project_id}/location/{location}/schedules/weekly_sentiment']
    """

    @property
    def raw_page(self):
        return self

    schedules: MutableSequence[gcn_schedule.Schedule] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcn_schedule.Schedule,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetScheduleRequest(proto.Message):
    r"""Request for getting scheduled notebook.

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/schedules/{schedule_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteScheduleRequest(proto.Message):
    r"""Request for deleting an Schedule

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/schedules/{schedule_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateScheduleRequest(proto.Message):
    r"""Request for created scheduled notebooks

    Attributes:
        parent (str):
            Required. Format:
            ``parent=projects/{project_id}/locations/{location}``
        schedule_id (str):
            Required. User-defined unique ID of this
            schedule.
        schedule (google.cloud.notebooks_v1.types.Schedule):
            Required. The schedule to be created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    schedule_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    schedule: gcn_schedule.Schedule = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcn_schedule.Schedule,
    )


class TriggerScheduleRequest(proto.Message):
    r"""Request for created scheduled notebooks

    Attributes:
        name (str):
            Required. Format:
            ``parent=projects/{project_id}/locations/{location}/schedules/{schedule_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListExecutionsRequest(proto.Message):
    r"""Request for listing scheduled notebook executions.

    Attributes:
        parent (str):
            Required. Format:
            ``parent=projects/{project_id}/locations/{location}``
        page_size (int):
            Maximum return size of the list call.
        page_token (str):
            A previous returned page token that can be
            used to continue listing from the last result.
        filter (str):
            Filter applied to resulting executions. Currently only
            supports filtering executions by a specified
            ``schedule_id``. Format: ``schedule_id=<Schedule_ID>``
        order_by (str):
            Sort by field.
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


class ListExecutionsResponse(proto.Message):
    r"""Response for listing scheduled notebook executions

    Attributes:
        executions (MutableSequence[google.cloud.notebooks_v1.types.Execution]):
            A list of returned instances.
        next_page_token (str):
            Page token that can be used to continue
            listing from the last result in the next list
            call.
        unreachable (MutableSequence[str]):
            Executions IDs that could not be reached. For example:

            ::

                ['projects/{project_id}/location/{location}/executions/imagenet_test1',
                 'projects/{project_id}/location/{location}/executions/classifier_train1']
    """

    @property
    def raw_page(self):
        return self

    executions: MutableSequence[gcn_execution.Execution] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcn_execution.Execution,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetExecutionRequest(proto.Message):
    r"""Request for getting scheduled notebook execution

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/executions/{execution_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteExecutionRequest(proto.Message):
    r"""Request for deleting a scheduled notebook execution

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/executions/{execution_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateExecutionRequest(proto.Message):
    r"""Request to create notebook execution

    Attributes:
        parent (str):
            Required. Format:
            ``parent=projects/{project_id}/locations/{location}``
        execution_id (str):
            Required. User-defined unique ID of this
            execution.
        execution (google.cloud.notebooks_v1.types.Execution):
            Required. The execution to be created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    execution_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    execution: gcn_execution.Execution = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcn_execution.Execution,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
