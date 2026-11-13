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

from google.cloud.sqladmin_v1.types import cloud_sql_resources

__protobuf__ = proto.module(
    package="google.cloud.sql.v1",
    manifest={
        "BlueGreenDeployment",
        "CreateBlueGreenDeploymentRequest",
        "GetBlueGreenDeploymentRequest",
        "SwitchoverBlueGreenDeploymentRequest",
        "ListBlueGreenDeploymentsRequest",
        "ListBlueGreenDeploymentsResponse",
        "DeleteBlueGreenDeploymentRequest",
    },
)


class BlueGreenDeployment(proto.Message):
    r"""A ``BlueGreenDeployment`` resource represents a Cloud SQL blue-green
    deployment setup.

    Attributes:
        name (str):
            Output only. Identifier. The full resource name of the
            deployment. Format:
            projects/{project}/locations/{location}/blueGreenDeployments/{deployment_id}
        description (str):
            Optional. User-provided description for the
            deployment. The description can be up to 255
            characters long.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the deployment was created.
            Example: ``2024-01-01T00:00:00Z``
        state (google.cloud.sqladmin_v1.types.BlueGreenDeployment.State):
            Output only. The current state of the
            blue-green deployment.
        source_instance (str):
            Required. Immutable. Required on create, and
            immutable. The full resource name of the source
            instance (the "blue" instance). Format:

            projects/{project}/instances/{instance}
        switchover_target_instance (str):
            Output only. The full resource name of the
            primary target instance (the "green" instance)
            that will be promoted during switchover. This
            field is always populated once the deployment is
            created. Format:

            projects/{project}/instances/{instance}
        error_detail (str):
            Output only. Provides details on why switchover is not
            possible. This field is empty unless a switchover attempt
            failed or the state is ``SWITCHOVER_NOT_READY``. Example:
            "The target database version does not match the source
            instance database version.".
        deployment_mappings (MutableSequence[google.cloud.sqladmin_v1.types.BlueGreenDeployment.SourceTargetPairedNode]):
            Output only. A list representing the pairs of
            source and target instances in the deployment.
        deployment_tasks (google.cloud.sqladmin_v1.types.BlueGreenDeployment.DeploymentTasks):
            Output only. Combined list of tasks for all
            paired nodes.
        requested_config (google.cloud.sqladmin_v1.types.BlueGreenDeployment.RequestedConfig):
            Optional. Immutable. Optional on create, and
            immutable. The configuration intended for the
            target instance(s) when the deployment was
            created.
    """

    class State(proto.Enum):
        r"""The state of the blue-green deployment.

        Values:
            STATE_UNSPECIFIED (0):
                The default value. This value is used if the
                state is omitted or unknown.
            PROVISIONING (1):
                The deployment is being provisioned.
            SWITCHOVER_READY (2):
                The deployment is ready for switchover.
            SWITCHOVER_NOT_READY (3):
                The deployment is not ready for switchover.
            SWITCHOVER_IN_PROGRESS (4):
                The deployment is in the process of switching
                over.
            SWITCHOVER_COMPLETED (5):
                The deployment has completed switchover.
            DELETING (6):
                The deployment is being deleted.
        """

        STATE_UNSPECIFIED = 0
        PROVISIONING = 1
        SWITCHOVER_READY = 2
        SWITCHOVER_NOT_READY = 3
        SWITCHOVER_IN_PROGRESS = 4
        SWITCHOVER_COMPLETED = 5
        DELETING = 6

    class RequestedConfig(proto.Message):
        r"""Configuration specified by the user at creation time for the
        target (green) instance.

        Attributes:
            database_version (str):
                Optional. The target database major version for the upgrade.
                For example, ``MYSQL_8_0`` or ``POSTGRES_15``.
        """

        database_version: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class DeploymentTasks(proto.Message):
        r"""Combined list of tasks for all paired nodes in the
        deployment.

        Attributes:
            task (MutableSequence[google.cloud.sqladmin_v1.types.BlueGreenDeployment.SourceTargetPairedNode.DeploymentTask]):
                Output only. Tasks performed or being
                performed on the paired nodes of the deployment
                at a consolidated level.
        """

        task: MutableSequence[
            "BlueGreenDeployment.SourceTargetPairedNode.DeploymentTask"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="BlueGreenDeployment.SourceTargetPairedNode.DeploymentTask",
        )

    class SourceTargetPairedNode(proto.Message):
        r"""Represents a pairing of a source instance node and a target
        instance node.

        Attributes:
            source (google.cloud.sqladmin_v1.types.BlueGreenDeployment.SourceTargetPairedNode.NodeInfo):
                Output only. Specifies the resource name of
                the source instance in this pair.
            target (google.cloud.sqladmin_v1.types.BlueGreenDeployment.SourceTargetPairedNode.NodeInfo):
                Output only. Specifies details of the
                corresponding target instance in this pair.
            state (google.cloud.sqladmin_v1.types.BlueGreenDeployment.SourceTargetPairedNode.State):
                Output only. Specifies the current state of
                this specific source-target pair.
            diffs (MutableSequence[google.cloud.sqladmin_v1.types.BlueGreenDeployment.SourceTargetPairedNode.ConfigDiff]):
                Output only. Describes the list of differences for the
                ``SourceTargetPairedNode``.
        """

        class State(proto.Enum):
            r"""The state of a pair of source and target instances in
            deployment (paired node).

            Values:
                STATE_UNSPECIFIED (0):
                    The state of the paired node is unknown.
                PROVISIONING (1):
                    The paired node is being provisioned.
                PROVISIONED (2):
                    The paired node is provisioned.
                UPGRADING (3):
                    The paired node is upgrading.
                UPGRADED (4):
                    The paired node is upgraded.
                UPGRADE_FAILED (5):
                    Upgrade failed on the paired node.
                SWITCHOVER_IN_PROGRESS (6):
                    Switchover is in progress.
                SWITCHOVER_FAILED (7):
                    Switchover failed on the paired node.
                SWITCHOVER_SUCCEEDED (8):
                    Switchover completed successfully.
                DELETING (11):
                    The paired node is being deleted.
            """

            STATE_UNSPECIFIED = 0
            PROVISIONING = 1
            PROVISIONED = 2
            UPGRADING = 3
            UPGRADED = 4
            UPGRADE_FAILED = 5
            SWITCHOVER_IN_PROGRESS = 6
            SWITCHOVER_FAILED = 7
            SWITCHOVER_SUCCEEDED = 8
            DELETING = 11

        class ConfigDiff(proto.Message):
            r"""Represents a specific configuration difference between blue
            and green instances.

            Attributes:
                field (str):
                    Output only. The name of the field that differs in the blue
                    and green instances, fully-qualified. Example:
                    ``settings.tier``
                source_value (str):
                    Output only. The value on the source
                    instance.
                target_value (str):
                    Output only. The value on the target
                    instance.
            """

            field: str = proto.Field(
                proto.STRING,
                number=1,
            )
            source_value: str = proto.Field(
                proto.STRING,
                number=2,
            )
            target_value: str = proto.Field(
                proto.STRING,
                number=3,
            )

        class NodeInfo(proto.Message):
            r"""Details about an instance within the deployment.

            Attributes:
                instance (str):
                    Output only. The full resource name of the
                    instance. Format:
                    projects/{project}/instances/{instance}
                connection (str):
                    Output only. The instance connection name.
                dns (str):
                    Output only. The unique DNS name for this
                    instance.
                ip_mappings (MutableSequence[google.cloud.sqladmin_v1.types.IpMapping]):
                    Output only. The list of IP addresses for
                    this instance.
            """

            instance: str = proto.Field(
                proto.STRING,
                number=1,
            )
            connection: str = proto.Field(
                proto.STRING,
                number=2,
            )
            dns: str = proto.Field(
                proto.STRING,
                number=3,
            )
            ip_mappings: MutableSequence[cloud_sql_resources.IpMapping] = (
                proto.RepeatedField(
                    proto.MESSAGE,
                    number=4,
                    message=cloud_sql_resources.IpMapping,
                )
            )

        class DeploymentTask(proto.Message):
            r"""Represents a task executed as part of the deployment on a
            target instance.

            Attributes:
                type_ (google.cloud.sqladmin_v1.types.BlueGreenDeployment.SourceTargetPairedNode.DeploymentTask.Type):
                    Output only. The type of the task.
                state (google.cloud.sqladmin_v1.types.BlueGreenDeployment.SourceTargetPairedNode.DeploymentTask.State):
                    Output only. The current state of the task.
                start_time (google.protobuf.timestamp_pb2.Timestamp):
                    Output only. Task start time.
                end_time (google.protobuf.timestamp_pb2.Timestamp):
                    Output only. Task end time (if completed).
                error_message (str):
                    Output only. Optional error details if the task state is
                    ``FAILED``.
            """

            class Type(proto.Enum):
                r"""The type of the task. This enum type ``Type`` is prone to change,
                and new values may be added in the future.

                Values:
                    TYPE_UNSPECIFIED (0):
                        The default value. This value is used if the
                        type is omitted.
                    PROVISION (1):
                        Provisions the green environment, which
                        includes creating the target instance.
                    UPGRADE (2):
                        Upgrades the green environment, for example,
                        performing a major version upgrade on the target
                        instance.
                    SWITCHOVER (3):
                        Promotes the target instance and then demotes
                        the source instance for this pair.
                    DELETE (4):
                        Deletes the blue-green deployment, including
                        underlying resources.
                    POST_SWITCHOVER_OPERATIONS (5):
                        Post-switchover operations, including
                        cleaning up resources of the old instance,
                        taking final backups, and updating metadata.
                """

                TYPE_UNSPECIFIED = 0
                PROVISION = 1
                UPGRADE = 2
                SWITCHOVER = 3
                DELETE = 4
                POST_SWITCHOVER_OPERATIONS = 5

            class State(proto.Enum):
                r"""The state of the task.
                This enum is not frozen, and new values may be added in the
                future.

                Values:
                    STATE_UNSPECIFIED (0):
                        The state of the task is unknown.
                    PENDING (1):
                        The task is pending.
                    RUNNING (2):
                        The task is running.
                    SUCCEEDED (3):
                        The task has succeeded.
                    FAILED (4):
                        The task has failed.
                """

                STATE_UNSPECIFIED = 0
                PENDING = 1
                RUNNING = 2
                SUCCEEDED = 3
                FAILED = 4

            type_: "BlueGreenDeployment.SourceTargetPairedNode.DeploymentTask.Type" = proto.Field(
                proto.ENUM,
                number=1,
                enum="BlueGreenDeployment.SourceTargetPairedNode.DeploymentTask.Type",
            )
            state: "BlueGreenDeployment.SourceTargetPairedNode.DeploymentTask.State" = proto.Field(
                proto.ENUM,
                number=2,
                enum="BlueGreenDeployment.SourceTargetPairedNode.DeploymentTask.State",
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
            error_message: str = proto.Field(
                proto.STRING,
                number=5,
            )

        source: "BlueGreenDeployment.SourceTargetPairedNode.NodeInfo" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="BlueGreenDeployment.SourceTargetPairedNode.NodeInfo",
        )
        target: "BlueGreenDeployment.SourceTargetPairedNode.NodeInfo" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="BlueGreenDeployment.SourceTargetPairedNode.NodeInfo",
        )
        state: "BlueGreenDeployment.SourceTargetPairedNode.State" = proto.Field(
            proto.ENUM,
            number=3,
            enum="BlueGreenDeployment.SourceTargetPairedNode.State",
        )
        diffs: MutableSequence[
            "BlueGreenDeployment.SourceTargetPairedNode.ConfigDiff"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=100,
            message="BlueGreenDeployment.SourceTargetPairedNode.ConfigDiff",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
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
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )
    source_instance: str = proto.Field(
        proto.STRING,
        number=5,
    )
    switchover_target_instance: str = proto.Field(
        proto.STRING,
        number=6,
    )
    error_detail: str = proto.Field(
        proto.STRING,
        number=7,
    )
    deployment_mappings: MutableSequence[SourceTargetPairedNode] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message=SourceTargetPairedNode,
    )
    deployment_tasks: DeploymentTasks = proto.Field(
        proto.MESSAGE,
        number=9,
        message=DeploymentTasks,
    )
    requested_config: RequestedConfig = proto.Field(
        proto.MESSAGE,
        number=10,
        message=RequestedConfig,
    )


class CreateBlueGreenDeploymentRequest(proto.Message):
    r"""The request message for creating a ``BlueGreenDeployment`` resource.

    Attributes:
        parent (str):
            Required. The parent resource where this
            blue-green deployment will be created. Format:
            projects/{project}/locations/{location}
        blue_green_deployment_id (str):
            Required. The ID to use for the blue-green
            deployment, which will become the final
            component of the deployment's resource name. The
            ID must be unique within the given project and
            location and between 2-63 characters.
        blue_green_deployment (google.cloud.sqladmin_v1.types.BlueGreenDeployment):
            Required. The ``BlueGreenDeployment`` resource to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    blue_green_deployment_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    blue_green_deployment: "BlueGreenDeployment" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="BlueGreenDeployment",
    )


class GetBlueGreenDeploymentRequest(proto.Message):
    r"""The request message for getting a BlueGreenDeployment.

    Attributes:
        name (str):
            Required. The name of the blue-green deployment to retrieve.
            Format:
            projects/{project}/locations/{location}/blueGreenDeployments/{blue_green_deployment}
        view (google.cloud.sqladmin_v1.types.GetBlueGreenDeploymentRequest.BlueGreenDeploymentView):
            Optional. Specifies whether to return the
            basic or detailed view of the resource in the
            response.
    """

    class BlueGreenDeploymentView(proto.Enum):
        r"""The view of a ``BlueGreenDeployment`` resource.

        Values:
            BLUE_GREEN_DEPLOYMENT_VIEW_UNSPECIFIED (0):
                Blue-green deployment view enumeration. This allows the
                caller to specify what view they query. If unspecified
                (BLUE_GREEN_DEPLOYMENT_VIEW_UNSPECIFIED), the behavior is
                the same as BASIC.
            BASIC (1):
                Includes basic metadata about the blue-green deployment.
                ``BASIC`` is the default view.
            DETAILED (2):
                Includes basic metadata and configuration differences
                between source and target instances (``database_version``,
                ``tier``, ``edition``, ``availability_type``,
                ``data_disk_size_gb``, and ``data_disk_type``).
        """

        BLUE_GREEN_DEPLOYMENT_VIEW_UNSPECIFIED = 0
        BASIC = 1
        DETAILED = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: BlueGreenDeploymentView = proto.Field(
        proto.ENUM,
        number=2,
        enum=BlueGreenDeploymentView,
    )


class SwitchoverBlueGreenDeploymentRequest(proto.Message):
    r"""Request message for switching over a ``BlueGreenDeployment``
    resource.

    Attributes:
        name (str):
            Required. The name of the blue-green deployment to switch
            over. Format:
            projects/{project}/locations/{location}/blueGreenDeployments/{blue_green_deployment}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListBlueGreenDeploymentsRequest(proto.Message):
    r"""The request message for listing blue-green deployment
    resources.

    Attributes:
        parent (str):
            Required. The parent resource whose
            blue-green deployments are to be listed. Format:
            projects/{project}/locations/{location}
        page_size (int):
            Optional. The maximum number of deployments
            to return. The service may return fewer
            deployments than this value. If unspecified, at
            most 500 deployments are returned. The maximum
            value is 1000; values above 1000 are treated as
            1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListBlueGreenDeployments`` call. Provide this to retrieve
            the subsequent page.
        filter (str):
            Optional. A filter expression that filters
            the results.
        order_by (str):
            Optional. A comma-separated list of fields to
            order the results by.
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


class ListBlueGreenDeploymentsResponse(proto.Message):
    r"""The response message for listing blue-green deployment
    resources.

    Attributes:
        blue_green_deployments (MutableSequence[google.cloud.sqladmin_v1.types.BlueGreenDeployment]):
            The list of blue-green deployment resources.
        next_page_token (str):
            A token to retrieve the next page of results,
            or empty if there are no more results.
    """

    @property
    def raw_page(self):
        return self

    blue_green_deployments: MutableSequence["BlueGreenDeployment"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="BlueGreenDeployment",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteBlueGreenDeploymentRequest(proto.Message):
    r"""Request message for deleting a BlueGreenDeployment.

    Attributes:
        name (str):
            Required. The name of the blue-green deployment to delete.
            Format:
            projects/{project}/locations/{location}/blueGreenDeployments/{blue_green_deployment}
        delete_old_source (bool):
            Optional. If set to true, and the switchover
            is complete, this deletes the old source
            instance along with the deployment.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    delete_old_source: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
