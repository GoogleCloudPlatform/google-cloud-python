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
import google.type.date_pb2 as date_pb2  # type: ignore
import google.type.dayofweek_pb2 as dayofweek_pb2  # type: ignore
import google.type.timeofday_pb2 as timeofday_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.deploy.v1",
    manifest={
        "SkaffoldSupportState",
        "BackoffMode",
        "RepairState",
        "DeliveryPipeline",
        "SerialPipeline",
        "Stage",
        "DeployParameters",
        "Strategy",
        "Predeploy",
        "Postdeploy",
        "Standard",
        "Canary",
        "CanaryDeployment",
        "CustomCanaryDeployment",
        "KubernetesConfig",
        "CloudRunConfig",
        "RuntimeConfig",
        "PipelineReadyCondition",
        "TargetsPresentCondition",
        "TargetsTypeCondition",
        "PipelineCondition",
        "ListDeliveryPipelinesRequest",
        "ListDeliveryPipelinesResponse",
        "GetDeliveryPipelineRequest",
        "CreateDeliveryPipelineRequest",
        "UpdateDeliveryPipelineRequest",
        "DeleteDeliveryPipelineRequest",
        "RollbackTargetConfig",
        "RollbackTargetRequest",
        "RollbackTargetResponse",
        "Target",
        "ExecutionConfig",
        "DefaultPool",
        "PrivatePool",
        "GkeCluster",
        "AnthosCluster",
        "CloudRunLocation",
        "MultiTarget",
        "CustomTarget",
        "AssociatedEntities",
        "ListTargetsRequest",
        "ListTargetsResponse",
        "GetTargetRequest",
        "CreateTargetRequest",
        "UpdateTargetRequest",
        "DeleteTargetRequest",
        "CustomTargetType",
        "CustomTargetSkaffoldActions",
        "SkaffoldModules",
        "ListCustomTargetTypesRequest",
        "ListCustomTargetTypesResponse",
        "GetCustomTargetTypeRequest",
        "CreateCustomTargetTypeRequest",
        "UpdateCustomTargetTypeRequest",
        "DeleteCustomTargetTypeRequest",
        "DeployPolicy",
        "DeployPolicyResourceSelector",
        "DeliveryPipelineAttribute",
        "TargetAttribute",
        "PolicyRule",
        "RolloutRestriction",
        "TimeWindows",
        "OneTimeWindow",
        "WeeklyWindow",
        "PolicyViolation",
        "PolicyViolationDetails",
        "Release",
        "CreateDeployPolicyRequest",
        "UpdateDeployPolicyRequest",
        "DeleteDeployPolicyRequest",
        "ListDeployPoliciesRequest",
        "ListDeployPoliciesResponse",
        "GetDeployPolicyRequest",
        "BuildArtifact",
        "TargetArtifact",
        "DeployArtifact",
        "CloudRunRenderMetadata",
        "RenderMetadata",
        "ListReleasesRequest",
        "ListReleasesResponse",
        "GetReleaseRequest",
        "CreateReleaseRequest",
        "Rollout",
        "Metadata",
        "DeployJobRunMetadata",
        "CloudRunMetadata",
        "CustomTargetDeployMetadata",
        "AutomationRolloutMetadata",
        "CustomMetadata",
        "Phase",
        "DeploymentJobs",
        "ChildRolloutJobs",
        "Job",
        "DeployJob",
        "VerifyJob",
        "PredeployJob",
        "PostdeployJob",
        "CreateChildRolloutJob",
        "AdvanceChildRolloutJob",
        "ListRolloutsRequest",
        "ListRolloutsResponse",
        "GetRolloutRequest",
        "CreateRolloutRequest",
        "OperationMetadata",
        "ApproveRolloutRequest",
        "ApproveRolloutResponse",
        "AdvanceRolloutRequest",
        "AdvanceRolloutResponse",
        "CancelRolloutRequest",
        "CancelRolloutResponse",
        "IgnoreJobRequest",
        "IgnoreJobResponse",
        "RetryJobRequest",
        "RetryJobResponse",
        "AbandonReleaseRequest",
        "AbandonReleaseResponse",
        "JobRun",
        "DeployJobRun",
        "VerifyJobRun",
        "PredeployJobRun",
        "PostdeployJobRun",
        "CreateChildRolloutJobRun",
        "AdvanceChildRolloutJobRun",
        "ListJobRunsRequest",
        "ListJobRunsResponse",
        "GetJobRunRequest",
        "TerminateJobRunRequest",
        "TerminateJobRunResponse",
        "Config",
        "SkaffoldVersion",
        "GetConfigRequest",
        "Automation",
        "AutomationResourceSelector",
        "AutomationRule",
        "TimedPromoteReleaseRule",
        "PromoteReleaseRule",
        "AdvanceRolloutRule",
        "RepairRolloutRule",
        "RepairPhaseConfig",
        "Retry",
        "Rollback",
        "AutomationRuleCondition",
        "TimedPromoteReleaseCondition",
        "CreateAutomationRequest",
        "UpdateAutomationRequest",
        "DeleteAutomationRequest",
        "ListAutomationsRequest",
        "ListAutomationsResponse",
        "GetAutomationRequest",
        "AutomationRun",
        "PromoteReleaseOperation",
        "AdvanceRolloutOperation",
        "RepairRolloutOperation",
        "TimedPromoteReleaseOperation",
        "RepairPhase",
        "RetryPhase",
        "RetryAttempt",
        "RollbackAttempt",
        "ListAutomationRunsRequest",
        "ListAutomationRunsResponse",
        "GetAutomationRunRequest",
        "CancelAutomationRunRequest",
        "CancelAutomationRunResponse",
    },
)


class SkaffoldSupportState(proto.Enum):
    r"""The support state of a specific Skaffold version.

    Values:
        SKAFFOLD_SUPPORT_STATE_UNSPECIFIED (0):
            Default value. This value is unused.
        SKAFFOLD_SUPPORT_STATE_SUPPORTED (1):
            This Skaffold version is currently supported.
        SKAFFOLD_SUPPORT_STATE_MAINTENANCE_MODE (2):
            This Skaffold version is in maintenance mode.
        SKAFFOLD_SUPPORT_STATE_UNSUPPORTED (3):
            This Skaffold version is no longer supported.
    """

    SKAFFOLD_SUPPORT_STATE_UNSPECIFIED = 0
    SKAFFOLD_SUPPORT_STATE_SUPPORTED = 1
    SKAFFOLD_SUPPORT_STATE_MAINTENANCE_MODE = 2
    SKAFFOLD_SUPPORT_STATE_UNSUPPORTED = 3


class BackoffMode(proto.Enum):
    r"""The pattern of how wait time is increased.

    Values:
        BACKOFF_MODE_UNSPECIFIED (0):
            No WaitMode is specified.
        BACKOFF_MODE_LINEAR (1):
            Increases the wait time linearly.
        BACKOFF_MODE_EXPONENTIAL (2):
            Increases the wait time exponentially.
    """

    BACKOFF_MODE_UNSPECIFIED = 0
    BACKOFF_MODE_LINEAR = 1
    BACKOFF_MODE_EXPONENTIAL = 2


class RepairState(proto.Enum):
    r"""Valid state of a repair attempt.

    Values:
        REPAIR_STATE_UNSPECIFIED (0):
            The ``repair`` has an unspecified state.
        REPAIR_STATE_SUCCEEDED (1):
            The ``repair`` action has succeeded.
        REPAIR_STATE_CANCELLED (2):
            The ``repair`` action was cancelled.
        REPAIR_STATE_FAILED (3):
            The ``repair`` action has failed.
        REPAIR_STATE_IN_PROGRESS (4):
            The ``repair`` action is in progress.
        REPAIR_STATE_PENDING (5):
            The ``repair`` action is pending.
        REPAIR_STATE_ABORTED (7):
            The ``repair`` action was aborted.
    """

    REPAIR_STATE_UNSPECIFIED = 0
    REPAIR_STATE_SUCCEEDED = 1
    REPAIR_STATE_CANCELLED = 2
    REPAIR_STATE_FAILED = 3
    REPAIR_STATE_IN_PROGRESS = 4
    REPAIR_STATE_PENDING = 5
    REPAIR_STATE_ABORTED = 7


class DeliveryPipeline(proto.Message):
    r"""A ``DeliveryPipeline`` resource in the Cloud Deploy API.

    A ``DeliveryPipeline`` defines a pipeline through which a Skaffold
    configuration can progress.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. Name of the ``DeliveryPipeline``. Format is
            ``projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}``.
            The ``deliveryPipeline`` component must match
            ``[a-z]([a-z0-9-]{0,61}[a-z0-9])?``
        uid (str):
            Output only. Unique identifier of the ``DeliveryPipeline``.
        description (str):
            Optional. Description of the ``DeliveryPipeline``. Max
            length is 255 characters.
        annotations (MutableMapping[str, str]):
            Optional. User annotations. These attributes
            can only be set and used by the user, and not by
            Cloud Deploy.
        labels (MutableMapping[str, str]):
            Labels are attributes that can be set and used by both the
            user and by Cloud Deploy. Labels must meet the following
            constraints:

            - Keys and values can contain only lowercase letters,
              numeric characters, underscores, and dashes.
            - All characters must use UTF-8 encoding, and international
              characters are allowed.
            - Keys must start with a lowercase letter or international
              character.
            - Each resource is limited to a maximum of 64 labels.

            Both keys and values are additionally constrained to be <=
            128 bytes.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time at which the pipeline was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Most recent time at which the
            pipeline was updated.
        serial_pipeline (google.cloud.deploy_v1.types.SerialPipeline):
            Optional. SerialPipeline defines a sequential set of stages
            for a ``DeliveryPipeline``.

            This field is a member of `oneof`_ ``pipeline``.
        condition (google.cloud.deploy_v1.types.PipelineCondition):
            Output only. Information around the state of
            the Delivery Pipeline.
        etag (str):
            This checksum is computed by the server based
            on the value of other fields, and may be sent on
            update and delete requests to ensure the client
            has an up-to-date value before proceeding.
        suspended (bool):
            Optional. When suspended, no new releases or
            rollouts can be created, but in-progress ones
            will complete.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    serial_pipeline: "SerialPipeline" = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="pipeline",
        message="SerialPipeline",
    )
    condition: "PipelineCondition" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="PipelineCondition",
    )
    etag: str = proto.Field(
        proto.STRING,
        number=10,
    )
    suspended: bool = proto.Field(
        proto.BOOL,
        number=12,
    )


class SerialPipeline(proto.Message):
    r"""SerialPipeline defines a sequential set of stages for a
    ``DeliveryPipeline``.

    Attributes:
        stages (MutableSequence[google.cloud.deploy_v1.types.Stage]):
            Optional. Each stage specifies configuration for a
            ``Target``. The ordering of this list defines the promotion
            flow.
    """

    stages: MutableSequence["Stage"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Stage",
    )


class Stage(proto.Message):
    r"""Stage specifies a location to which to deploy.

    Attributes:
        target_id (str):
            Optional. The target_id to which this stage points. This
            field refers exclusively to the last segment of a target
            name. For example, this field would just be ``my-target``
            (rather than
            ``projects/project/locations/location/targets/my-target``).
            The location of the ``Target`` is inferred to be the same as
            the location of the ``DeliveryPipeline`` that contains this
            ``Stage``.
        profiles (MutableSequence[str]):
            Optional. Skaffold profiles to use when rendering the
            manifest for this stage's ``Target``.
        strategy (google.cloud.deploy_v1.types.Strategy):
            Optional. The strategy to use for a ``Rollout`` to this
            stage.
        deploy_parameters (MutableSequence[google.cloud.deploy_v1.types.DeployParameters]):
            Optional. The deploy parameters to use for
            the target in this stage.
    """

    target_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    profiles: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    strategy: "Strategy" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="Strategy",
    )
    deploy_parameters: MutableSequence["DeployParameters"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="DeployParameters",
    )


class DeployParameters(proto.Message):
    r"""DeployParameters contains deploy parameters information.

    Attributes:
        values (MutableMapping[str, str]):
            Required. Values are deploy parameters in
            key-value pairs.
        match_target_labels (MutableMapping[str, str]):
            Optional. Deploy parameters are applied to
            targets with match labels. If unspecified,
            deploy parameters are applied to all targets
            (including child targets of a multi-target).
    """

    values: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=1,
    )
    match_target_labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )


class Strategy(proto.Message):
    r"""Strategy contains deployment strategy information.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        standard (google.cloud.deploy_v1.types.Standard):
            Optional. Standard deployment strategy
            executes a single deploy and allows verifying
            the deployment.

            This field is a member of `oneof`_ ``deployment_strategy``.
        canary (google.cloud.deploy_v1.types.Canary):
            Optional. Canary deployment strategy provides
            progressive percentage based deployments to a
            Target.

            This field is a member of `oneof`_ ``deployment_strategy``.
    """

    standard: "Standard" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="deployment_strategy",
        message="Standard",
    )
    canary: "Canary" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="deployment_strategy",
        message="Canary",
    )


class Predeploy(proto.Message):
    r"""Predeploy contains the predeploy job configuration
    information.

    Attributes:
        actions (MutableSequence[str]):
            Optional. A sequence of Skaffold custom
            actions to invoke during execution of the
            predeploy job.
    """

    actions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class Postdeploy(proto.Message):
    r"""Postdeploy contains the postdeploy job configuration
    information.

    Attributes:
        actions (MutableSequence[str]):
            Optional. A sequence of Skaffold custom
            actions to invoke during execution of the
            postdeploy job.
    """

    actions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class Standard(proto.Message):
    r"""Standard represents the standard deployment strategy.

    Attributes:
        verify (bool):
            Optional. Whether to verify a deployment via
            ``skaffold verify``.
        predeploy (google.cloud.deploy_v1.types.Predeploy):
            Optional. Configuration for the predeploy
            job. If this is not configured, the predeploy
            job will not be present.
        postdeploy (google.cloud.deploy_v1.types.Postdeploy):
            Optional. Configuration for the postdeploy
            job. If this is not configured, the postdeploy
            job will not be present.
    """

    verify: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    predeploy: "Predeploy" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Predeploy",
    )
    postdeploy: "Postdeploy" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Postdeploy",
    )


class Canary(proto.Message):
    r"""Canary represents the canary deployment strategy.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        runtime_config (google.cloud.deploy_v1.types.RuntimeConfig):
            Optional. Runtime specific configurations for
            the deployment strategy. The runtime
            configuration is used to determine how Cloud
            Deploy will split traffic to enable a
            progressive deployment.
        canary_deployment (google.cloud.deploy_v1.types.CanaryDeployment):
            Optional. Configures the progressive based
            deployment for a Target.

            This field is a member of `oneof`_ ``mode``.
        custom_canary_deployment (google.cloud.deploy_v1.types.CustomCanaryDeployment):
            Optional. Configures the progressive based
            deployment for a Target, but allows customizing
            at the phase level where a phase represents each
            of the percentage deployments.

            This field is a member of `oneof`_ ``mode``.
    """

    runtime_config: "RuntimeConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="RuntimeConfig",
    )
    canary_deployment: "CanaryDeployment" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="mode",
        message="CanaryDeployment",
    )
    custom_canary_deployment: "CustomCanaryDeployment" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="mode",
        message="CustomCanaryDeployment",
    )


class CanaryDeployment(proto.Message):
    r"""CanaryDeployment represents the canary deployment
    configuration

    Attributes:
        percentages (MutableSequence[int]):
            Required. The percentage based deployments that will occur
            as a part of a ``Rollout``. List is expected in ascending
            order and each integer n is 0 <= n < 100. If the
            GatewayServiceMesh is configured for Kubernetes, then the
            range for n is 0 <= n <= 100.
        verify (bool):
            Optional. Whether to run verify tests after each percentage
            deployment via ``skaffold verify``.
        predeploy (google.cloud.deploy_v1.types.Predeploy):
            Optional. Configuration for the predeploy job
            of the first phase. If this is not configured,
            there will be no predeploy job for this phase.
        postdeploy (google.cloud.deploy_v1.types.Postdeploy):
            Optional. Configuration for the postdeploy
            job of the last phase. If this is not
            configured, there will be no postdeploy job for
            this phase.
    """

    percentages: MutableSequence[int] = proto.RepeatedField(
        proto.INT32,
        number=1,
    )
    verify: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    predeploy: "Predeploy" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Predeploy",
    )
    postdeploy: "Postdeploy" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="Postdeploy",
    )


class CustomCanaryDeployment(proto.Message):
    r"""CustomCanaryDeployment represents the custom canary
    deployment configuration.

    Attributes:
        phase_configs (MutableSequence[google.cloud.deploy_v1.types.CustomCanaryDeployment.PhaseConfig]):
            Required. Configuration for each phase in the
            canary deployment in the order executed.
    """

    class PhaseConfig(proto.Message):
        r"""PhaseConfig represents the configuration for a phase in the
        custom canary deployment.

        Attributes:
            phase_id (str):
                Required. The ID to assign to the ``Rollout`` phase. This
                value must consist of lower-case letters, numbers, and
                hyphens, start with a letter and end with a letter or a
                number, and have a max length of 63 characters. In other
                words, it must match the following regex:
                ``^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$``.
            percentage (int):
                Required. Percentage deployment for the
                phase.
            profiles (MutableSequence[str]):
                Optional. Skaffold profiles to use when rendering the
                manifest for this phase. These are in addition to the
                profiles list specified in the ``DeliveryPipeline`` stage.
            verify (bool):
                Optional. Whether to run verify tests after the deployment
                via ``skaffold verify``.
            predeploy (google.cloud.deploy_v1.types.Predeploy):
                Optional. Configuration for the predeploy job
                of this phase. If this is not configured, there
                will be no predeploy job for this phase.
            postdeploy (google.cloud.deploy_v1.types.Postdeploy):
                Optional. Configuration for the postdeploy
                job of this phase. If this is not configured,
                there will be no postdeploy job for this phase.
        """

        phase_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        percentage: int = proto.Field(
            proto.INT32,
            number=2,
        )
        profiles: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=3,
        )
        verify: bool = proto.Field(
            proto.BOOL,
            number=4,
        )
        predeploy: "Predeploy" = proto.Field(
            proto.MESSAGE,
            number=5,
            message="Predeploy",
        )
        postdeploy: "Postdeploy" = proto.Field(
            proto.MESSAGE,
            number=6,
            message="Postdeploy",
        )

    phase_configs: MutableSequence[PhaseConfig] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=PhaseConfig,
    )


class KubernetesConfig(proto.Message):
    r"""KubernetesConfig contains the Kubernetes runtime
    configuration.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gateway_service_mesh (google.cloud.deploy_v1.types.KubernetesConfig.GatewayServiceMesh):
            Optional. Kubernetes Gateway API service mesh
            configuration.

            This field is a member of `oneof`_ ``service_definition``.
        service_networking (google.cloud.deploy_v1.types.KubernetesConfig.ServiceNetworking):
            Optional. Kubernetes Service networking
            configuration.

            This field is a member of `oneof`_ ``service_definition``.
    """

    class GatewayServiceMesh(proto.Message):
        r"""Information about the Kubernetes Gateway API service mesh
        configuration.

        Attributes:
            http_route (str):
                Required. Name of the Gateway API HTTPRoute.
            service (str):
                Required. Name of the Kubernetes Service.
            deployment (str):
                Required. Name of the Kubernetes Deployment
                whose traffic is managed by the specified
                HTTPRoute and Service.
            route_update_wait_time (google.protobuf.duration_pb2.Duration):
                Optional. The time to wait for route updates
                to propagate. The maximum configurable time is 3
                hours, in seconds format. If unspecified, there
                is no wait time.
            stable_cutback_duration (google.protobuf.duration_pb2.Duration):
                Optional. The amount of time to migrate
                traffic back from the canary Service to the
                original Service during the stable phase
                deployment. If specified, must be between 15s
                and 3600s. If unspecified, there is no cutback
                time.
            pod_selector_label (str):
                Optional. The label to use when selecting
                Pods for the Deployment and Service resources.
                This label must already be present in both
                resources.
            route_destinations (google.cloud.deploy_v1.types.KubernetesConfig.GatewayServiceMesh.RouteDestinations):
                Optional. Route destinations allow
                configuring the Gateway API HTTPRoute to be
                deployed to additional clusters. This option is
                available for multi-cluster service mesh set ups
                that require the route to exist in the clusters
                that call the service. If unspecified, the
                HTTPRoute will only be deployed to the Target
                cluster.
        """

        class RouteDestinations(proto.Message):
            r"""Information about route destinations for the Gateway API
            service mesh.

            Attributes:
                destination_ids (MutableSequence[str]):
                    Required. The clusters where the Gateway API
                    HTTPRoute resource will be deployed to. Valid
                    entries include the associated entities IDs
                    configured in the Target resource and "@self" to
                    include the Target cluster.
                propagate_service (bool):
                    Optional. Whether to propagate the Kubernetes
                    Service to the route destination clusters. The
                    Service will always be deployed to the Target
                    cluster even if the HTTPRoute is not. This
                    option may be used to facilitate successful DNS
                    lookup in the route destination clusters. Can
                    only be set to true if destinations are
                    specified.
            """

            destination_ids: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=1,
            )
            propagate_service: bool = proto.Field(
                proto.BOOL,
                number=2,
            )

        http_route: str = proto.Field(
            proto.STRING,
            number=1,
        )
        service: str = proto.Field(
            proto.STRING,
            number=2,
        )
        deployment: str = proto.Field(
            proto.STRING,
            number=3,
        )
        route_update_wait_time: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=4,
            message=duration_pb2.Duration,
        )
        stable_cutback_duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=5,
            message=duration_pb2.Duration,
        )
        pod_selector_label: str = proto.Field(
            proto.STRING,
            number=6,
        )
        route_destinations: "KubernetesConfig.GatewayServiceMesh.RouteDestinations" = (
            proto.Field(
                proto.MESSAGE,
                number=8,
                message="KubernetesConfig.GatewayServiceMesh.RouteDestinations",
            )
        )

    class ServiceNetworking(proto.Message):
        r"""Information about the Kubernetes Service networking
        configuration.

        Attributes:
            service (str):
                Required. Name of the Kubernetes Service.
            deployment (str):
                Required. Name of the Kubernetes Deployment
                whose traffic is managed by the specified
                Service.
            disable_pod_overprovisioning (bool):
                Optional. Whether to disable Pod
                overprovisioning. If Pod overprovisioning is
                disabled then Cloud Deploy will limit the number
                of total Pods used for the deployment strategy
                to the number of Pods the Deployment has on the
                cluster.
            pod_selector_label (str):
                Optional. The label to use when selecting
                Pods for the Deployment resource. This label
                must already be present in the Deployment.
        """

        service: str = proto.Field(
            proto.STRING,
            number=1,
        )
        deployment: str = proto.Field(
            proto.STRING,
            number=2,
        )
        disable_pod_overprovisioning: bool = proto.Field(
            proto.BOOL,
            number=3,
        )
        pod_selector_label: str = proto.Field(
            proto.STRING,
            number=4,
        )

    gateway_service_mesh: GatewayServiceMesh = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="service_definition",
        message=GatewayServiceMesh,
    )
    service_networking: ServiceNetworking = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="service_definition",
        message=ServiceNetworking,
    )


class CloudRunConfig(proto.Message):
    r"""CloudRunConfig contains the Cloud Run runtime configuration.

    Attributes:
        automatic_traffic_control (bool):
            Optional. Whether Cloud Deploy should update
            the traffic stanza in a Cloud Run Service on the
            user's behalf to facilitate traffic splitting.
            This is required to be true for
            CanaryDeployments, but optional for
            CustomCanaryDeployments.
        canary_revision_tags (MutableSequence[str]):
            Optional. A list of tags that are added to
            the canary revision while the canary phase is in
            progress.
        prior_revision_tags (MutableSequence[str]):
            Optional. A list of tags that are added to
            the prior revision while the canary phase is in
            progress.
        stable_revision_tags (MutableSequence[str]):
            Optional. A list of tags that are added to
            the final stable revision when the stable phase
            is applied.
    """

    automatic_traffic_control: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    canary_revision_tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    prior_revision_tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    stable_revision_tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )


class RuntimeConfig(proto.Message):
    r"""RuntimeConfig contains the runtime specific configurations
    for a deployment strategy.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        kubernetes (google.cloud.deploy_v1.types.KubernetesConfig):
            Optional. Kubernetes runtime configuration.

            This field is a member of `oneof`_ ``runtime_config``.
        cloud_run (google.cloud.deploy_v1.types.CloudRunConfig):
            Optional. Cloud Run runtime configuration.

            This field is a member of `oneof`_ ``runtime_config``.
    """

    kubernetes: "KubernetesConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="runtime_config",
        message="KubernetesConfig",
    )
    cloud_run: "CloudRunConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="runtime_config",
        message="CloudRunConfig",
    )


class PipelineReadyCondition(proto.Message):
    r"""PipelineReadyCondition contains information around the status
    of the Pipeline.

    Attributes:
        status (bool):
            True if the Pipeline is in a valid state. Otherwise at least
            one condition in ``PipelineCondition`` is in an invalid
            state. Iterate over those conditions and see which
            condition(s) has status = false to find out what is wrong
            with the Pipeline.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Last time the condition was updated.
    """

    status: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


class TargetsPresentCondition(proto.Message):
    r"""``TargetsPresentCondition`` contains information on any Targets
    referenced in the Delivery Pipeline that do not actually exist.

    Attributes:
        status (bool):
            True if there aren't any missing Targets.
        missing_targets (MutableSequence[str]):
            The list of Target names that do not exist. For example,
            ``projects/{project_id}/locations/{location_name}/targets/{target_name}``.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Last time the condition was updated.
    """

    status: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    missing_targets: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


class TargetsTypeCondition(proto.Message):
    r"""TargetsTypeCondition contains information on whether the
    Targets defined in the Delivery Pipeline are of the same type.

    Attributes:
        status (bool):
            True if the targets are all a comparable
            type. For example this is true if all targets
            are GKE clusters. This is false if some targets
            are Cloud Run targets and others are GKE
            clusters.
        error_details (str):
            Human readable error message.
    """

    status: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    error_details: str = proto.Field(
        proto.STRING,
        number=2,
    )


class PipelineCondition(proto.Message):
    r"""PipelineCondition contains all conditions relevant to a
    Delivery Pipeline.

    Attributes:
        pipeline_ready_condition (google.cloud.deploy_v1.types.PipelineReadyCondition):
            Details around the Pipeline's overall status.
        targets_present_condition (google.cloud.deploy_v1.types.TargetsPresentCondition):
            Details around targets enumerated in the
            pipeline.
        targets_type_condition (google.cloud.deploy_v1.types.TargetsTypeCondition):
            Details on the whether the targets enumerated
            in the pipeline are of the same type.
    """

    pipeline_ready_condition: "PipelineReadyCondition" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="PipelineReadyCondition",
    )
    targets_present_condition: "TargetsPresentCondition" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="TargetsPresentCondition",
    )
    targets_type_condition: "TargetsTypeCondition" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="TargetsTypeCondition",
    )


class ListDeliveryPipelinesRequest(proto.Message):
    r"""The request object for ``ListDeliveryPipelines``.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            pipelines. Format must be
            ``projects/{project_id}/locations/{location_name}``.
        page_size (int):
            The maximum number of pipelines to return.
            The service may return fewer than this value. If
            unspecified, at most 50 pipelines will be
            returned. The maximum value is 1000; values
            above 1000 will be set to 1000.
        page_token (str):
            A page token, received from a previous
            ``ListDeliveryPipelines`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other provided parameters match the
            call that provided the page token.
        filter (str):
            Filter pipelines to be returned. See
            https://google.aip.dev/160 for more details.
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


class ListDeliveryPipelinesResponse(proto.Message):
    r"""The response object from ``ListDeliveryPipelines``.

    Attributes:
        delivery_pipelines (MutableSequence[google.cloud.deploy_v1.types.DeliveryPipeline]):
            The ``DeliveryPipeline`` objects.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    delivery_pipelines: MutableSequence["DeliveryPipeline"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DeliveryPipeline",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetDeliveryPipelineRequest(proto.Message):
    r"""The request object for ``GetDeliveryPipeline``

    Attributes:
        name (str):
            Required. Name of the ``DeliveryPipeline``. Format must be
            ``projects/{project_id}/locations/{location_name}/deliveryPipelines/{pipeline_name}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateDeliveryPipelineRequest(proto.Message):
    r"""The request object for ``CreateDeliveryPipeline``.

    Attributes:
        parent (str):
            Required. The parent collection in which the
            ``DeliveryPipeline`` must be created. The format is
            ``projects/{project_id}/locations/{location_name}``.
        delivery_pipeline_id (str):
            Required. ID of the ``DeliveryPipeline``.
        delivery_pipeline (google.cloud.deploy_v1.types.DeliveryPipeline):
            Required. The ``DeliveryPipeline`` to create.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server knows to ignore
            the request if it has already been completed.
            The server guarantees that for at least 60
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
        validate_only (bool):
            Optional. If set to true, the request is
            validated and the user is provided with an
            expected result, but no actual change is made.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    delivery_pipeline_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    delivery_pipeline: "DeliveryPipeline" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="DeliveryPipeline",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class UpdateDeliveryPipelineRequest(proto.Message):
    r"""The request object for ``UpdateDeliveryPipeline``.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten by the update in the ``DeliveryPipeline``
            resource. The fields specified in the update_mask are
            relative to the resource, not the full request. A field will
            be overwritten if it's in the mask. If the user doesn't
            provide a mask then all fields are overwritten.
        delivery_pipeline (google.cloud.deploy_v1.types.DeliveryPipeline):
            Required. The ``DeliveryPipeline`` to update.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server knows to ignore
            the request if it has already been completed.
            The server guarantees that for at least 60
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
        allow_missing (bool):
            Optional. If set to true, updating a ``DeliveryPipeline``
            that does not exist will result in the creation of a new
            ``DeliveryPipeline``.
        validate_only (bool):
            Optional. If set to true, the request is
            validated and the user is provided with an
            expected result, but no actual change is made.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    delivery_pipeline: "DeliveryPipeline" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DeliveryPipeline",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class DeleteDeliveryPipelineRequest(proto.Message):
    r"""The request object for ``DeleteDeliveryPipeline``.

    Attributes:
        name (str):
            Required. The name of the ``DeliveryPipeline`` to delete.
            The format is
            ``projects/{project_id}/locations/{location_name}/deliveryPipelines/{pipeline_name}``.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server knows to ignore
            the request if it has already been completed.
            The server guarantees that for at least 60
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
        allow_missing (bool):
            Optional. If set to true, then deleting an already deleted
            or non-existing ``DeliveryPipeline`` will succeed.
        validate_only (bool):
            Optional. If set, validate the request and
            preview the review, but do not actually post it.
        force (bool):
            Optional. If set to true, all child resources
            under this pipeline will also be deleted.
            Otherwise, the request will only work if the
            pipeline has no child resources.
        etag (str):
            Optional. This checksum is computed by the
            server based on the value of other fields, and
            may be sent on update and delete requests to
            ensure the client has an up-to-date value before
            proceeding.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=5,
    )


class RollbackTargetConfig(proto.Message):
    r"""Configs for the Rollback rollout.

    Attributes:
        rollout (google.cloud.deploy_v1.types.Rollout):
            Optional. The rollback ``Rollout`` to create.
        starting_phase_id (str):
            Optional. The starting phase ID for the ``Rollout``. If
            unspecified, the ``Rollout`` will start in the stable phase.
    """

    rollout: "Rollout" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Rollout",
    )
    starting_phase_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class RollbackTargetRequest(proto.Message):
    r"""The request object for ``RollbackTarget``.

    Attributes:
        name (str):
            Required. The ``DeliveryPipeline`` for which the rollback
            ``Rollout`` must be created. The format is
            ``projects/{project_id}/locations/{location_name}/deliveryPipelines/{pipeline_name}``.
        target_id (str):
            Required. ID of the ``Target`` that is being rolled back.
        rollout_id (str):
            Required. ID of the rollback ``Rollout`` to create.
        release_id (str):
            Optional. ID of the ``Release`` to roll back to. If this
            isn't specified, the previous successful ``Rollout`` to the
            specified target will be used to determine the ``Release``.
        rollout_to_roll_back (str):
            Optional. If provided, this must be the latest ``Rollout``
            that is on the ``Target``.
        rollback_config (google.cloud.deploy_v1.types.RollbackTargetConfig):
            Optional. Configs for the rollback ``Rollout``.
        validate_only (bool):
            Optional. If set to true, the request is validated and the
            user is provided with a ``RollbackTargetResponse``.
        override_deploy_policy (MutableSequence[str]):
            Optional. Deploy policies to override. Format is
            ``projects/{project}/locations/{location}/deployPolicies/{deploy_policy}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    target_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    rollout_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    release_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    rollout_to_roll_back: str = proto.Field(
        proto.STRING,
        number=5,
    )
    rollback_config: "RollbackTargetConfig" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="RollbackTargetConfig",
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    override_deploy_policy: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=9,
    )


class RollbackTargetResponse(proto.Message):
    r"""The response object from ``RollbackTarget``.

    Attributes:
        rollback_config (google.cloud.deploy_v1.types.RollbackTargetConfig):
            The config of the rollback ``Rollout`` created or will be
            created.
    """

    rollback_config: "RollbackTargetConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="RollbackTargetConfig",
    )


class Target(proto.Message):
    r"""A ``Target`` resource in the Cloud Deploy API.

    A ``Target`` defines a location to which a Skaffold configuration
    can be deployed.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. Name of the ``Target``. Format is
            ``projects/{project}/locations/{location}/targets/{target}``.
            The ``target`` component must match
            ``[a-z]([a-z0-9-]{0,61}[a-z0-9])?``
        target_id (str):
            Output only. Resource id of the ``Target``.
        uid (str):
            Output only. Unique identifier of the ``Target``.
        description (str):
            Optional. Description of the ``Target``. Max length is 255
            characters.
        annotations (MutableMapping[str, str]):
            Optional. User annotations. These attributes
            can only be set and used by the user, and not by
            Cloud Deploy. See
            https://google.aip.dev/128#annotations for more
            details such as format and size limitations.
        labels (MutableMapping[str, str]):
            Optional. Labels are attributes that can be set and used by
            both the user and by Cloud Deploy. Labels must meet the
            following constraints:

            - Keys and values can contain only lowercase letters,
              numeric characters, underscores, and dashes.
            - All characters must use UTF-8 encoding, and international
              characters are allowed.
            - Keys must start with a lowercase letter or international
              character.
            - Each resource is limited to a maximum of 64 labels.

            Both keys and values are additionally constrained to be <=
            128 bytes.
        require_approval (bool):
            Optional. Whether or not the ``Target`` requires approval.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time at which the ``Target`` was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Most recent time at which the ``Target`` was
            updated.
        gke (google.cloud.deploy_v1.types.GkeCluster):
            Optional. Information specifying a GKE
            Cluster.

            This field is a member of `oneof`_ ``deployment_target``.
        anthos_cluster (google.cloud.deploy_v1.types.AnthosCluster):
            Optional. Information specifying an Anthos
            Cluster.

            This field is a member of `oneof`_ ``deployment_target``.
        run (google.cloud.deploy_v1.types.CloudRunLocation):
            Optional. Information specifying a Cloud Run
            deployment target.

            This field is a member of `oneof`_ ``deployment_target``.
        multi_target (google.cloud.deploy_v1.types.MultiTarget):
            Optional. Information specifying a
            multiTarget.

            This field is a member of `oneof`_ ``deployment_target``.
        custom_target (google.cloud.deploy_v1.types.CustomTarget):
            Optional. Information specifying a Custom
            Target.

            This field is a member of `oneof`_ ``deployment_target``.
        associated_entities (MutableMapping[str, google.cloud.deploy_v1.types.AssociatedEntities]):
            Optional. Map of entity IDs to their associated entities.
            Associated entities allows specifying places other than the
            deployment target for specific features. For example, the
            Gateway API canary can be configured to deploy the HTTPRoute
            to a different cluster(s) than the deployment cluster using
            associated entities. An entity ID must consist of lower-case
            letters, numbers, and hyphens, start with a letter and end
            with a letter or a number, and have a max length of 63
            characters. In other words, it must match the following
            regex: ``^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$``.
        etag (str):
            Optional. This checksum is computed by the
            server based on the value of other fields, and
            may be sent on update and delete requests to
            ensure the client has an up-to-date value before
            proceeding.
        execution_configs (MutableSequence[google.cloud.deploy_v1.types.ExecutionConfig]):
            Optional. Configurations for all execution that relates to
            this ``Target``. Each ``ExecutionEnvironmentUsage`` value
            may only be used in a single configuration; using the same
            value multiple times is an error. When one or more
            configurations are specified, they must include the
            ``RENDER`` and ``DEPLOY`` ``ExecutionEnvironmentUsage``
            values. When no configurations are specified, execution will
            use the default specified in ``DefaultPool``.
        deploy_parameters (MutableMapping[str, str]):
            Optional. The deploy parameters to use for
            this target.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    target_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=3,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    require_approval: bool = proto.Field(
        proto.BOOL,
        number=13,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    gke: "GkeCluster" = proto.Field(
        proto.MESSAGE,
        number=15,
        oneof="deployment_target",
        message="GkeCluster",
    )
    anthos_cluster: "AnthosCluster" = proto.Field(
        proto.MESSAGE,
        number=17,
        oneof="deployment_target",
        message="AnthosCluster",
    )
    run: "CloudRunLocation" = proto.Field(
        proto.MESSAGE,
        number=18,
        oneof="deployment_target",
        message="CloudRunLocation",
    )
    multi_target: "MultiTarget" = proto.Field(
        proto.MESSAGE,
        number=19,
        oneof="deployment_target",
        message="MultiTarget",
    )
    custom_target: "CustomTarget" = proto.Field(
        proto.MESSAGE,
        number=21,
        oneof="deployment_target",
        message="CustomTarget",
    )
    associated_entities: MutableMapping[str, "AssociatedEntities"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=23,
        message="AssociatedEntities",
    )
    etag: str = proto.Field(
        proto.STRING,
        number=12,
    )
    execution_configs: MutableSequence["ExecutionConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=16,
        message="ExecutionConfig",
    )
    deploy_parameters: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=20,
    )


class ExecutionConfig(proto.Message):
    r"""Configuration of the environment to use when calling
    Skaffold.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        usages (MutableSequence[google.cloud.deploy_v1.types.ExecutionConfig.ExecutionEnvironmentUsage]):
            Required. Usages when this configuration
            should be applied.
        default_pool (google.cloud.deploy_v1.types.DefaultPool):
            Optional. Use default Cloud Build pool.

            This field is a member of `oneof`_ ``execution_environment``.
        private_pool (google.cloud.deploy_v1.types.PrivatePool):
            Optional. Use private Cloud Build pool.

            This field is a member of `oneof`_ ``execution_environment``.
        worker_pool (str):
            Optional. The resource name of the ``WorkerPool``, with the
            format
            ``projects/{project}/locations/{location}/workerPools/{worker_pool}``.
            If this optional field is unspecified, the default Cloud
            Build pool will be used.
        service_account (str):
            Optional. Google service account to use for execution. If
            unspecified, the project execution service account
            (<PROJECT_NUMBER>-compute@developer.gserviceaccount.com) is
            used.
        artifact_storage (str):
            Optional. Cloud Storage location in which to
            store execution outputs. This can either be a
            bucket ("gs://my-bucket") or a path within a
            bucket ("gs://my-bucket/my-dir").
            If unspecified, a default bucket located in the
            same region will be used.
        execution_timeout (google.protobuf.duration_pb2.Duration):
            Optional. Execution timeout for a Cloud Build
            Execution. This must be between 10m and 24h in
            seconds format. If unspecified, a default
            timeout of 1h is used.
        verbose (bool):
            Optional. If true, additional logging will be
            enabled when running builds in this execution
            environment.
    """

    class ExecutionEnvironmentUsage(proto.Enum):
        r"""Possible usages of this configuration.

        Values:
            EXECUTION_ENVIRONMENT_USAGE_UNSPECIFIED (0):
                Default value. This value is unused.
            RENDER (1):
                Use for rendering.
            DEPLOY (2):
                Use for deploying and deployment hooks.
            VERIFY (3):
                Use for deployment verification.
            PREDEPLOY (4):
                Use for predeploy job execution.
            POSTDEPLOY (5):
                Use for postdeploy job execution.
        """

        EXECUTION_ENVIRONMENT_USAGE_UNSPECIFIED = 0
        RENDER = 1
        DEPLOY = 2
        VERIFY = 3
        PREDEPLOY = 4
        POSTDEPLOY = 5

    usages: MutableSequence[ExecutionEnvironmentUsage] = proto.RepeatedField(
        proto.ENUM,
        number=1,
        enum=ExecutionEnvironmentUsage,
    )
    default_pool: "DefaultPool" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="execution_environment",
        message="DefaultPool",
    )
    private_pool: "PrivatePool" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="execution_environment",
        message="PrivatePool",
    )
    worker_pool: str = proto.Field(
        proto.STRING,
        number=4,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=5,
    )
    artifact_storage: str = proto.Field(
        proto.STRING,
        number=6,
    )
    execution_timeout: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=7,
        message=duration_pb2.Duration,
    )
    verbose: bool = proto.Field(
        proto.BOOL,
        number=8,
    )


class DefaultPool(proto.Message):
    r"""Execution using the default Cloud Build pool.

    Attributes:
        service_account (str):
            Optional. Google service account to use for execution. If
            unspecified, the project execution service account
            (<PROJECT_NUMBER>-compute@developer.gserviceaccount.com)
            will be used.
        artifact_storage (str):
            Optional. Cloud Storage location where
            execution outputs should be stored. This can
            either be a bucket ("gs://my-bucket") or a path
            within a bucket ("gs://my-bucket/my-dir").
            If unspecified, a default bucket located in the
            same region will be used.
    """

    service_account: str = proto.Field(
        proto.STRING,
        number=1,
    )
    artifact_storage: str = proto.Field(
        proto.STRING,
        number=2,
    )


class PrivatePool(proto.Message):
    r"""Execution using a private Cloud Build pool.

    Attributes:
        worker_pool (str):
            Required. Resource name of the Cloud Build worker pool to
            use. The format is
            ``projects/{project}/locations/{location}/workerPools/{pool}``.
        service_account (str):
            Optional. Google service account to use for execution. If
            unspecified, the project execution service account
            (<PROJECT_NUMBER>-compute@developer.gserviceaccount.com)
            will be used.
        artifact_storage (str):
            Optional. Cloud Storage location where
            execution outputs should be stored. This can
            either be a bucket ("gs://my-bucket") or a path
            within a bucket ("gs://my-bucket/my-dir").
            If unspecified, a default bucket located in the
            same region will be used.
    """

    worker_pool: str = proto.Field(
        proto.STRING,
        number=1,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=2,
    )
    artifact_storage: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GkeCluster(proto.Message):
    r"""Information specifying a GKE Cluster.

    Attributes:
        cluster (str):
            Optional. Information specifying a GKE Cluster. Format is
            ``projects/{project_id}/locations/{location_id}/clusters/{cluster_id}``.
        internal_ip (bool):
            Optional. If true, ``cluster`` is accessed using the private
            IP address of the control plane endpoint. Otherwise, the
            default IP address of the control plane endpoint is used.
            The default IP address is the private IP address for
            clusters with private control-plane endpoints and the public
            IP address otherwise.

            Only specify this option when ``cluster`` is a `private GKE
            cluster <https://cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept>`__.
            Note that ``internal_ip`` and ``dns_endpoint`` cannot both
            be set to true.
        proxy_url (str):
            Optional. If set, used to configure a
            `proxy <https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/#proxy>`__
            to the Kubernetes server.
        dns_endpoint (bool):
            Optional. If set, the cluster will be accessed using the DNS
            endpoint. Note that both ``dns_endpoint`` and
            ``internal_ip`` cannot be set to true.
    """

    cluster: str = proto.Field(
        proto.STRING,
        number=1,
    )
    internal_ip: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    proxy_url: str = proto.Field(
        proto.STRING,
        number=3,
    )
    dns_endpoint: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class AnthosCluster(proto.Message):
    r"""Information specifying an Anthos Cluster.

    Attributes:
        membership (str):
            Optional. Membership of the GKE Hub-registered cluster to
            which to apply the Skaffold configuration. Format is
            ``projects/{project}/locations/{location}/memberships/{membership_name}``.
    """

    membership: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CloudRunLocation(proto.Message):
    r"""Information specifying where to deploy a Cloud Run Service.

    Attributes:
        location (str):
            Required. The location for the Cloud Run Service. Format
            must be ``projects/{project}/locations/{location}``.
    """

    location: str = proto.Field(
        proto.STRING,
        number=1,
    )


class MultiTarget(proto.Message):
    r"""Information specifying a multiTarget.

    Attributes:
        target_ids (MutableSequence[str]):
            Required. The target_ids of this multiTarget.
    """

    target_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class CustomTarget(proto.Message):
    r"""Information specifying a Custom Target.

    Attributes:
        custom_target_type (str):
            Required. The name of the CustomTargetType. Format must be
            ``projects/{project}/locations/{location}/customTargetTypes/{custom_target_type}``.
    """

    custom_target_type: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AssociatedEntities(proto.Message):
    r"""Information about entities associated with a ``Target``.

    Attributes:
        gke_clusters (MutableSequence[google.cloud.deploy_v1.types.GkeCluster]):
            Optional. Information specifying GKE clusters
            as associated entities.
        anthos_clusters (MutableSequence[google.cloud.deploy_v1.types.AnthosCluster]):
            Optional. Information specifying Anthos
            clusters as associated entities.
    """

    gke_clusters: MutableSequence["GkeCluster"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="GkeCluster",
    )
    anthos_clusters: MutableSequence["AnthosCluster"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="AnthosCluster",
    )


class ListTargetsRequest(proto.Message):
    r"""The request object for ``ListTargets``.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of targets.
            Format must be
            ``projects/{project_id}/locations/{location_name}``.
        page_size (int):
            Optional. The maximum number of ``Target`` objects to
            return. The service may return fewer than this value. If
            unspecified, at most 50 ``Target`` objects will be returned.
            The maximum value is 1000; values above 1000 will be set to
            1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListTargets`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other provided parameters match the
            call that provided the page token.
        filter (str):
            Optional. Filter targets to be returned. See
            https://google.aip.dev/160 for more details.
        order_by (str):
            Optional. Field to sort by. See
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


class ListTargetsResponse(proto.Message):
    r"""The response object from ``ListTargets``.

    Attributes:
        targets (MutableSequence[google.cloud.deploy_v1.types.Target]):
            The ``Target`` objects.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    targets: MutableSequence["Target"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Target",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetTargetRequest(proto.Message):
    r"""The request object for ``GetTarget``.

    Attributes:
        name (str):
            Required. Name of the ``Target``. Format must be
            ``projects/{project_id}/locations/{location_name}/targets/{target_name}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateTargetRequest(proto.Message):
    r"""The request object for ``CreateTarget``.

    Attributes:
        parent (str):
            Required. The parent collection in which the ``Target`` must
            be created. The format is
            ``projects/{project_id}/locations/{location_name}``.
        target_id (str):
            Required. ID of the ``Target``.
        target (google.cloud.deploy_v1.types.Target):
            Required. The ``Target`` to create.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server knows to ignore
            the request if it has already been completed.
            The server guarantees that for at least 60
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
        validate_only (bool):
            Optional. If set to true, the request is
            validated and the user is provided with an
            expected result, but no actual change is made.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    target_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    target: "Target" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Target",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class UpdateTargetRequest(proto.Message):
    r"""The request object for ``UpdateTarget``.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten by the update in the ``Target`` resource. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it's in the mask. If the user doesn't provide a mask then
            all fields are overwritten.
        target (google.cloud.deploy_v1.types.Target):
            Required. The ``Target`` to update.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server knows to ignore
            the request if it has already been completed.
            The server guarantees that for at least 60
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
        allow_missing (bool):
            Optional. If set to true, updating a ``Target`` that does
            not exist will result in the creation of a new ``Target``.
        validate_only (bool):
            Optional. If set to true, the request is
            validated and the user is provided with an
            expected result, but no actual change is made.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    target: "Target" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Target",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class DeleteTargetRequest(proto.Message):
    r"""The request object for ``DeleteTarget``.

    Attributes:
        name (str):
            Required. The name of the ``Target`` to delete. The format
            is
            ``projects/{project_id}/locations/{location_name}/targets/{target_name}``.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server knows to ignore
            the request if it has already been completed.
            The server guarantees that for at least 60
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
        allow_missing (bool):
            Optional. If set to true, then deleting an already deleted
            or non-existing ``Target`` will succeed.
        validate_only (bool):
            Optional. If set, validate the request and
            preview the review, but do not actually post it.
        etag (str):
            Optional. This checksum is computed by the
            server based on the value of other fields, and
            may be sent on update and delete requests to
            ensure the client has an up-to-date value before
            proceeding.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
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


class CustomTargetType(proto.Message):
    r"""A ``CustomTargetType`` resource in the Cloud Deploy API.

    A ``CustomTargetType`` defines a type of custom target that can be
    referenced in a ``Target`` in order to facilitate deploying to other
    systems besides the supported runtimes.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. Name of the ``CustomTargetType``. Format is
            ``projects/{project}/locations/{location}/customTargetTypes/{customTargetType}``.
            The ``customTargetType`` component must match
            ``[a-z]([a-z0-9-]{0,61}[a-z0-9])?``
        custom_target_type_id (str):
            Output only. Resource id of the ``CustomTargetType``.
        uid (str):
            Output only. Unique identifier of the ``CustomTargetType``.
        description (str):
            Optional. Description of the ``CustomTargetType``. Max
            length is 255 characters.
        annotations (MutableMapping[str, str]):
            Optional. User annotations. These attributes
            can only be set and used by the user, and not by
            Cloud Deploy. See
            https://google.aip.dev/128#annotations for more
            details such as format and size limitations.
        labels (MutableMapping[str, str]):
            Optional. Labels are attributes that can be set and used by
            both the user and by Cloud Deploy. Labels must meet the
            following constraints:

            - Keys and values can contain only lowercase letters,
              numeric characters, underscores, and dashes.
            - All characters must use UTF-8 encoding, and international
              characters are allowed.
            - Keys must start with a lowercase letter or international
              character.
            - Each resource is limited to a maximum of 64 labels.

            Both keys and values are additionally constrained to be <=
            128 bytes.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time at which the ``CustomTargetType`` was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Most recent time at which the
            ``CustomTargetType`` was updated.
        etag (str):
            Optional. This checksum is computed by the
            server based on the value of other fields, and
            may be sent on update and delete requests to
            ensure the client has an up-to-date value before
            proceeding.
        custom_actions (google.cloud.deploy_v1.types.CustomTargetSkaffoldActions):
            Optional. Configures render and deploy for the
            ``CustomTargetType`` using Skaffold custom actions.

            This field is a member of `oneof`_ ``definition``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    custom_target_type_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=3,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=9,
    )
    custom_actions: "CustomTargetSkaffoldActions" = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="definition",
        message="CustomTargetSkaffoldActions",
    )


class CustomTargetSkaffoldActions(proto.Message):
    r"""CustomTargetSkaffoldActions represents the ``CustomTargetType``
    configuration using Skaffold custom actions.

    Attributes:
        render_action (str):
            Optional. The Skaffold custom action responsible for render
            operations. If not provided then Cloud Deploy will perform
            the render operations via ``skaffold render``.
        deploy_action (str):
            Required. The Skaffold custom action
            responsible for deploy operations.
        include_skaffold_modules (MutableSequence[google.cloud.deploy_v1.types.SkaffoldModules]):
            Optional. List of Skaffold modules Cloud
            Deploy will include in the Skaffold Config as
            required before performing diagnose.
    """

    render_action: str = proto.Field(
        proto.STRING,
        number=1,
    )
    deploy_action: str = proto.Field(
        proto.STRING,
        number=2,
    )
    include_skaffold_modules: MutableSequence["SkaffoldModules"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="SkaffoldModules",
    )


class SkaffoldModules(proto.Message):
    r"""Skaffold Config modules and their remote source.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        configs (MutableSequence[str]):
            Optional. The Skaffold Config modules to use
            from the specified source.
        git (google.cloud.deploy_v1.types.SkaffoldModules.SkaffoldGitSource):
            Optional. Remote git repository containing
            the Skaffold Config modules.

            This field is a member of `oneof`_ ``source``.
        google_cloud_storage (google.cloud.deploy_v1.types.SkaffoldModules.SkaffoldGCSSource):
            Optional. Cloud Storage bucket containing the
            Skaffold Config modules.

            This field is a member of `oneof`_ ``source``.
        google_cloud_build_repo (google.cloud.deploy_v1.types.SkaffoldModules.SkaffoldGCBRepoSource):
            Optional. Cloud Build V2 repository
            containing the Skaffold Config modules.

            This field is a member of `oneof`_ ``source``.
    """

    class SkaffoldGitSource(proto.Message):
        r"""Git repository containing Skaffold Config modules.

        Attributes:
            repo (str):
                Required. Git repository the package should
                be cloned from.
            path (str):
                Optional. Relative path from the repository
                root to the Skaffold file.
            ref (str):
                Optional. Git branch or tag to use when
                cloning the repository.
        """

        repo: str = proto.Field(
            proto.STRING,
            number=1,
        )
        path: str = proto.Field(
            proto.STRING,
            number=2,
        )
        ref: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class SkaffoldGCSSource(proto.Message):
        r"""Cloud Storage bucket containing Skaffold Config modules.

        Attributes:
            source (str):
                Required. Cloud Storage source paths to copy recursively.
                For example, providing "gs://my-bucket/dir/configs/\*" will
                result in Skaffold copying all files within the
                "dir/configs" directory in the bucket "my-bucket".
            path (str):
                Optional. Relative path from the source to
                the Skaffold file.
        """

        source: str = proto.Field(
            proto.STRING,
            number=1,
        )
        path: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class SkaffoldGCBRepoSource(proto.Message):
        r"""Cloud Build V2 Repository containing Skaffold Configs.

        Attributes:
            repository (str):
                Required. Name of the Cloud Build V2
                Repository. Format is
                projects/{project}/locations/{location}/connections/{connection}/repositories/{repository}.
            path (str):
                Optional. Relative path from the repository
                root to the Skaffold Config file.
            ref (str):
                Optional. Branch or tag to use when cloning
                the repository.
        """

        repository: str = proto.Field(
            proto.STRING,
            number=1,
        )
        path: str = proto.Field(
            proto.STRING,
            number=2,
        )
        ref: str = proto.Field(
            proto.STRING,
            number=3,
        )

    configs: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    git: SkaffoldGitSource = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="source",
        message=SkaffoldGitSource,
    )
    google_cloud_storage: SkaffoldGCSSource = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="source",
        message=SkaffoldGCSSource,
    )
    google_cloud_build_repo: SkaffoldGCBRepoSource = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="source",
        message=SkaffoldGCBRepoSource,
    )


class ListCustomTargetTypesRequest(proto.Message):
    r"""The request object for ``ListCustomTargetTypes``.

    Attributes:
        parent (str):
            Required. The parent that owns this collection of custom
            target types. Format must be
            ``projects/{project_id}/locations/{location_name}``.
        page_size (int):
            Optional. The maximum number of ``CustomTargetType`` objects
            to return. The service may return fewer than this value. If
            unspecified, at most 50 ``CustomTargetType`` objects will be
            returned. The maximum value is 1000; values above 1000 will
            be set to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListCustomTargetTypes`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other provided parameters match the
            call that provided the page token.
        filter (str):
            Optional. Filter custom target types to be
            returned. See https://google.aip.dev/160 for
            more details.
        order_by (str):
            Optional. Field to sort by. See
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


class ListCustomTargetTypesResponse(proto.Message):
    r"""The response object from ``ListCustomTargetTypes.``

    Attributes:
        custom_target_types (MutableSequence[google.cloud.deploy_v1.types.CustomTargetType]):
            The ``CustomTargetType`` objects.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    custom_target_types: MutableSequence["CustomTargetType"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="CustomTargetType",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetCustomTargetTypeRequest(proto.Message):
    r"""The request object for ``GetCustomTargetType``.

    Attributes:
        name (str):
            Required. Name of the ``CustomTargetType``. Format must be
            ``projects/{project_id}/locations/{location_name}/customTargetTypes/{custom_target_type}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateCustomTargetTypeRequest(proto.Message):
    r"""The request object for ``CreateCustomTargetType``.

    Attributes:
        parent (str):
            Required. The parent collection in which the
            ``CustomTargetType`` must be created. The format is
            ``projects/{project_id}/locations/{location_name}``.
        custom_target_type_id (str):
            Required. ID of the ``CustomTargetType``.
        custom_target_type (google.cloud.deploy_v1.types.CustomTargetType):
            Required. The ``CustomTargetType`` to create.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server knows to ignore
            the request if it has already been completed.
            The server guarantees that for at least 60
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
        validate_only (bool):
            Optional. If set to true, the request is
            validated and the user is provided with an
            expected result, but no actual change is made.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    custom_target_type_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    custom_target_type: "CustomTargetType" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="CustomTargetType",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class UpdateCustomTargetTypeRequest(proto.Message):
    r"""The request object for ``UpdateCustomTargetType``.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten by the update in the ``CustomTargetType``
            resource. The fields specified in the update_mask are
            relative to the resource, not the full request. A field will
            be overwritten if it's in the mask. If the user doesn't
            provide a mask then all fields are overwritten.
        custom_target_type (google.cloud.deploy_v1.types.CustomTargetType):
            Required. The ``CustomTargetType`` to update.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server knows to ignore
            the request if it has already been completed.
            The server guarantees that for at least 60
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
        allow_missing (bool):
            Optional. If set to true, updating a ``CustomTargetType``
            that does not exist will result in the creation of a new
            ``CustomTargetType``.
        validate_only (bool):
            Optional. If set to true, the request is
            validated and the user is provided with an
            expected result, but no actual change is made.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    custom_target_type: "CustomTargetType" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="CustomTargetType",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class DeleteCustomTargetTypeRequest(proto.Message):
    r"""The request object for ``DeleteCustomTargetType``.

    Attributes:
        name (str):
            Required. The name of the ``CustomTargetType`` to delete.
            Format must be
            ``projects/{project_id}/locations/{location_name}/customTargetTypes/{custom_target_type}``.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server knows to ignore
            the request if it has already been completed.
            The server guarantees that for at least 60
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
        allow_missing (bool):
            Optional. If set to true, then deleting an already deleted
            or non-existing ``CustomTargetType`` will succeed.
        validate_only (bool):
            Optional. If set to true, the request is
            validated but no actual change is made.
        etag (str):
            Optional. This checksum is computed by the
            server based on the value of other fields, and
            may be sent on update and delete requests to
            ensure the client has an up-to-date value before
            proceeding.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
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


class DeployPolicy(proto.Message):
    r"""A ``DeployPolicy`` resource in the Cloud Deploy API.

    A ``DeployPolicy`` inhibits manual or automation-driven actions
    within a Delivery Pipeline or Target.

    Attributes:
        name (str):
            Output only. Name of the ``DeployPolicy``. Format is
            ``projects/{project}/locations/{location}/deployPolicies/{deployPolicy}``.
            The ``deployPolicy`` component must match
            ``[a-z]([a-z0-9-]{0,61}[a-z0-9])?``
        uid (str):
            Output only. Unique identifier of the ``DeployPolicy``.
        description (str):
            Optional. Description of the ``DeployPolicy``. Max length is
            255 characters.
        annotations (MutableMapping[str, str]):
            Optional. User annotations. These attributes can only be set
            and used by the user, and not by Cloud Deploy. Annotations
            must meet the following constraints:

            - Annotations are key/value pairs.
            - Valid annotation keys have two segments: an optional
              prefix and name, separated by a slash (``/``).
            - The name segment is required and must be 63 characters or
              less, beginning and ending with an alphanumeric character
              (``[a-z0-9A-Z]``) with dashes (``-``), underscores
              (``_``), dots (``.``), and alphanumerics between.
            - The prefix is optional. If specified, the prefix must be a
              DNS subdomain: a series of DNS labels separated by
              dots(``.``), not longer than 253 characters in total,
              followed by a slash (``/``).

            See
            https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/#syntax-and-character-set
            for more details.
        labels (MutableMapping[str, str]):
            Labels are attributes that can be set and used by both the
            user and by Cloud Deploy. Labels must meet the following
            constraints:

            - Keys and values can contain only lowercase letters,
              numeric characters, underscores, and dashes.
            - All characters must use UTF-8 encoding, and international
              characters are allowed.
            - Keys must start with a lowercase letter or international
              character.
            - Each resource is limited to a maximum of 64 labels.

            Both keys and values are additionally constrained to be <=
            128 bytes.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time at which the deploy policy
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Most recent time at which the
            deploy policy was updated.
        suspended (bool):
            Optional. When suspended, the policy will not
            prevent actions from occurring, even if the
            action violates the policy.
        selectors (MutableSequence[google.cloud.deploy_v1.types.DeployPolicyResourceSelector]):
            Required. Selected resources to which the
            policy will be applied. At least one selector is
            required. If one selector matches the resource
            the policy applies. For example, if there are
            two selectors and the action being attempted
            matches one of them, the policy will apply to
            that action.
        rules (MutableSequence[google.cloud.deploy_v1.types.PolicyRule]):
            Required. Rules to apply. At least one rule
            must be present.
        etag (str):
            The weak etag of the ``DeployPolicy`` resource. This
            checksum is computed by the server based on the value of
            other fields, and may be sent on update and delete requests
            to ensure the client has an up-to-date value before
            proceeding.
    """

    class Invoker(proto.Enum):
        r"""What invoked the action. Filters enforcing the policy
        depending on what invoked the action.

        Values:
            INVOKER_UNSPECIFIED (0):
                Unspecified.
            USER (1):
                The action is user-driven. For example,
                creating a rollout manually via a gcloud create
                command.
            DEPLOY_AUTOMATION (2):
                Automated action by Cloud Deploy.
        """

        INVOKER_UNSPECIFIED = 0
        USER = 1
        DEPLOY_AUTOMATION = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    suspended: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    selectors: MutableSequence["DeployPolicyResourceSelector"] = proto.RepeatedField(
        proto.MESSAGE,
        number=12,
        message="DeployPolicyResourceSelector",
    )
    rules: MutableSequence["PolicyRule"] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message="PolicyRule",
    )
    etag: str = proto.Field(
        proto.STRING,
        number=11,
    )


class DeployPolicyResourceSelector(proto.Message):
    r"""Contains information on the resources to select for a deploy
    policy. Attributes provided must all match the resource in order
    for policy restrictions to apply. For example, if delivery
    pipelines attributes given are an id "prod" and labels "foo:
    bar", a delivery pipeline resource must match both that id and
    have that label in order to be subject to the policy.

    Attributes:
        delivery_pipeline (google.cloud.deploy_v1.types.DeliveryPipelineAttribute):
            Optional. Contains attributes about a
            delivery pipeline.
        target (google.cloud.deploy_v1.types.TargetAttribute):
            Optional. Contains attributes about a target.
    """

    delivery_pipeline: "DeliveryPipelineAttribute" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="DeliveryPipelineAttribute",
    )
    target: "TargetAttribute" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="TargetAttribute",
    )


class DeliveryPipelineAttribute(proto.Message):
    r"""Contains criteria for selecting DeliveryPipelines.

    Attributes:
        id (str):
            Optional. ID of the ``DeliveryPipeline``. The value of this
            field could be one of the following:

            - The last segment of a pipeline name
            - "\*", all delivery pipelines in a location
        labels (MutableMapping[str, str]):
            DeliveryPipeline labels.
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )


class TargetAttribute(proto.Message):
    r"""Contains criteria for selecting Targets. This could be used
    to select targets for a Deploy Policy or for an Automation.

    Attributes:
        id (str):
            Optional. ID of the ``Target``. The value of this field
            could be one of the following:

            - The last segment of a target name
            - "\*", all targets in a location
        labels (MutableMapping[str, str]):
            Target labels.
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )


class PolicyRule(proto.Message):
    r"""Deploy Policy rule.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        rollout_restriction (google.cloud.deploy_v1.types.RolloutRestriction):
            Optional. Rollout restrictions.

            This field is a member of `oneof`_ ``rule``.
    """

    rollout_restriction: "RolloutRestriction" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="rule",
        message="RolloutRestriction",
    )


class RolloutRestriction(proto.Message):
    r"""Rollout restrictions.

    Attributes:
        id (str):
            Required. Restriction rule ID. Required and must be unique
            within a DeployPolicy. The format is
            ``[a-z]([a-z0-9-]{0,61}[a-z0-9])?``.
        invokers (MutableSequence[google.cloud.deploy_v1.types.DeployPolicy.Invoker]):
            Optional. What invoked the action. If left
            empty, all invoker types will be restricted.
        actions (MutableSequence[google.cloud.deploy_v1.types.RolloutRestriction.RolloutActions]):
            Optional. Rollout actions to be restricted as
            part of the policy. If left empty, all actions
            will be restricted.
        time_windows (google.cloud.deploy_v1.types.TimeWindows):
            Required. Time window within which actions
            are restricted.
    """

    class RolloutActions(proto.Enum):
        r"""Rollout actions to be restricted as part of the policy.

        Values:
            ROLLOUT_ACTIONS_UNSPECIFIED (0):
                Unspecified.
            ADVANCE (1):
                Advance the rollout to the next phase.
            APPROVE (2):
                Approve the rollout.
            CANCEL (3):
                Cancel the rollout.
            CREATE (4):
                Create a rollout.
            IGNORE_JOB (5):
                Ignore a job result on the rollout.
            RETRY_JOB (6):
                Retry a job for a rollout.
            ROLLBACK (7):
                Rollback a rollout.
            TERMINATE_JOBRUN (8):
                Terminate a jobrun.
        """

        ROLLOUT_ACTIONS_UNSPECIFIED = 0
        ADVANCE = 1
        APPROVE = 2
        CANCEL = 3
        CREATE = 4
        IGNORE_JOB = 5
        RETRY_JOB = 6
        ROLLBACK = 7
        TERMINATE_JOBRUN = 8

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    invokers: MutableSequence["DeployPolicy.Invoker"] = proto.RepeatedField(
        proto.ENUM,
        number=2,
        enum="DeployPolicy.Invoker",
    )
    actions: MutableSequence[RolloutActions] = proto.RepeatedField(
        proto.ENUM,
        number=3,
        enum=RolloutActions,
    )
    time_windows: "TimeWindows" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="TimeWindows",
    )


class TimeWindows(proto.Message):
    r"""Time windows within which actions are restricted. See the
    `documentation <https://cloud.google.com/deploy/docs/deploy-policy#dates_times>`__
    for more information on how to configure dates/times.

    Attributes:
        time_zone (str):
            Required. The time zone in IANA format `IANA Time Zone
            Database <https://www.iana.org/time-zones>`__ (e.g.
            America/New_York).
        one_time_windows (MutableSequence[google.cloud.deploy_v1.types.OneTimeWindow]):
            Optional. One-time windows within which
            actions are restricted.
        weekly_windows (MutableSequence[google.cloud.deploy_v1.types.WeeklyWindow]):
            Optional. Recurring weekly windows within
            which actions are restricted.
    """

    time_zone: str = proto.Field(
        proto.STRING,
        number=1,
    )
    one_time_windows: MutableSequence["OneTimeWindow"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="OneTimeWindow",
    )
    weekly_windows: MutableSequence["WeeklyWindow"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="WeeklyWindow",
    )


class OneTimeWindow(proto.Message):
    r"""One-time window within which actions are restricted. For
    example, blocking actions over New Year's Eve from December 31st
    at 5pm to January 1st at 9am.

    Attributes:
        start_date (google.type.date_pb2.Date):
            Required. Start date.
        start_time (google.type.timeofday_pb2.TimeOfDay):
            Required. Start time (inclusive). Use 00:00
            for the beginning of the day.
        end_date (google.type.date_pb2.Date):
            Required. End date.
        end_time (google.type.timeofday_pb2.TimeOfDay):
            Required. End time (exclusive). You may use
            24:00 for the end of the day.
    """

    start_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=1,
        message=date_pb2.Date,
    )
    start_time: timeofday_pb2.TimeOfDay = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timeofday_pb2.TimeOfDay,
    )
    end_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=3,
        message=date_pb2.Date,
    )
    end_time: timeofday_pb2.TimeOfDay = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timeofday_pb2.TimeOfDay,
    )


class WeeklyWindow(proto.Message):
    r"""Weekly windows. For example, blocking actions every Saturday
    and Sunday. Another example would be blocking actions every
    weekday from 5pm to midnight.

    Attributes:
        days_of_week (MutableSequence[google.type.dayofweek_pb2.DayOfWeek]):
            Optional. Days of week. If left empty, all
            days of the week will be included.
        start_time (google.type.timeofday_pb2.TimeOfDay):
            Optional. Start time (inclusive). Use 00:00 for the
            beginning of the day. If you specify start_time you must
            also specify end_time. If left empty, this will block for
            the entire day for the days specified in days_of_week.
        end_time (google.type.timeofday_pb2.TimeOfDay):
            Optional. End time (exclusive). Use 24:00 to indicate
            midnight. If you specify end_time you must also specify
            start_time. If left empty, this will block for the entire
            day for the days specified in days_of_week.
    """

    days_of_week: MutableSequence[dayofweek_pb2.DayOfWeek] = proto.RepeatedField(
        proto.ENUM,
        number=1,
        enum=dayofweek_pb2.DayOfWeek,
    )
    start_time: timeofday_pb2.TimeOfDay = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timeofday_pb2.TimeOfDay,
    )
    end_time: timeofday_pb2.TimeOfDay = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timeofday_pb2.TimeOfDay,
    )


class PolicyViolation(proto.Message):
    r"""Returned from an action if one or more policies were
    violated, and therefore the action was prevented. Contains
    information about what policies were violated and why.

    Attributes:
        policy_violation_details (MutableSequence[google.cloud.deploy_v1.types.PolicyViolationDetails]):
            Policy violation details.
    """

    policy_violation_details: MutableSequence["PolicyViolationDetails"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="PolicyViolationDetails",
        )
    )


class PolicyViolationDetails(proto.Message):
    r"""Policy violation details.

    Attributes:
        policy (str):
            Name of the policy that was violated. Policy resource will
            be in the format of
            ``projects/{project}/locations/{location}/policies/{policy}``.
        rule_id (str):
            Id of the rule that triggered the policy
            violation.
        failure_message (str):
            User readable message about why the request
            violated a policy. This is not intended for
            machine parsing.
    """

    policy: str = proto.Field(
        proto.STRING,
        number=1,
    )
    rule_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    failure_message: str = proto.Field(
        proto.STRING,
        number=3,
    )


class Release(proto.Message):
    r"""A ``Release`` resource in the Cloud Deploy API.

    A ``Release`` defines a specific Skaffold configuration instance
    that can be deployed.

    Attributes:
        name (str):
            Identifier. Name of the ``Release``. Format is
            ``projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{release}``.
            The ``release`` component must match
            ``[a-z]([a-z0-9-]{0,61}[a-z0-9])?``
        uid (str):
            Output only. Unique identifier of the ``Release``.
        description (str):
            Optional. Description of the ``Release``. Max length is 255
            characters.
        annotations (MutableMapping[str, str]):
            Optional. User annotations. These attributes
            can only be set and used by the user, and not by
            Cloud Deploy. See
            https://google.aip.dev/128#annotations for more
            details such as format and size limitations.
        labels (MutableMapping[str, str]):
            Labels are attributes that can be set and used by both the
            user and by Cloud Deploy. Labels must meet the following
            constraints:

            - Keys and values can contain only lowercase letters,
              numeric characters, underscores, and dashes.
            - All characters must use UTF-8 encoding, and international
              characters are allowed.
            - Keys must start with a lowercase letter or international
              character.
            - Each resource is limited to a maximum of 64 labels.

            Both keys and values are additionally constrained to be <=
            128 bytes.
        abandoned (bool):
            Output only. Indicates whether this is an
            abandoned release.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time at which the ``Release`` was created.
        render_start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time at which the render began.
        render_end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time at which the render
            completed.
        skaffold_config_uri (str):
            Optional. Cloud Storage URI of tar.gz archive
            containing Skaffold configuration.
        skaffold_config_path (str):
            Optional. Filepath of the Skaffold config
            inside of the config URI.
        build_artifacts (MutableSequence[google.cloud.deploy_v1.types.BuildArtifact]):
            Optional. List of artifacts to pass through
            to Skaffold command.
        delivery_pipeline_snapshot (google.cloud.deploy_v1.types.DeliveryPipeline):
            Output only. Snapshot of the parent pipeline
            taken at release creation time.
        target_snapshots (MutableSequence[google.cloud.deploy_v1.types.Target]):
            Output only. Snapshot of the targets taken at
            release creation time.
        custom_target_type_snapshots (MutableSequence[google.cloud.deploy_v1.types.CustomTargetType]):
            Output only. Snapshot of the custom target
            types referenced by the targets taken at release
            creation time.
        render_state (google.cloud.deploy_v1.types.Release.RenderState):
            Output only. Current state of the render
            operation.
        etag (str):
            This checksum is computed by the server based
            on the value of other fields, and may be sent on
            update and delete requests to ensure the client
            has an up-to-date value before proceeding.
        skaffold_version (str):
            Optional. The Skaffold version to use when
            operating on this release, such as "1.20.0". Not
            all versions are valid; Cloud Deploy supports a
            specific set of versions.

            If unset, the most recent supported Skaffold
            version will be used.
        target_artifacts (MutableMapping[str, google.cloud.deploy_v1.types.TargetArtifact]):
            Output only. Map from target ID to the target
            artifacts created during the render operation.
        target_renders (MutableMapping[str, google.cloud.deploy_v1.types.Release.TargetRender]):
            Output only. Map from target ID to details of
            the render operation for that target.
        condition (google.cloud.deploy_v1.types.Release.ReleaseCondition):
            Output only. Information around the state of
            the Release.
        deploy_parameters (MutableMapping[str, str]):
            Optional. The deploy parameters to use for
            all targets in this release.
    """

    class RenderState(proto.Enum):
        r"""Valid states of the render operation.

        Values:
            RENDER_STATE_UNSPECIFIED (0):
                The render state is unspecified.
            SUCCEEDED (1):
                All rendering operations have completed
                successfully.
            FAILED (2):
                All rendering operations have completed, and
                one or more have failed.
            IN_PROGRESS (3):
                Rendering has started and is not complete.
        """

        RENDER_STATE_UNSPECIFIED = 0
        SUCCEEDED = 1
        FAILED = 2
        IN_PROGRESS = 3

    class TargetRender(proto.Message):
        r"""Details of rendering for a single target.

        Attributes:
            rendering_build (str):
                Output only. The resource name of the Cloud Build ``Build``
                object that is used to render the manifest for this target.
                Format is
                ``projects/{project}/locations/{location}/builds/{build}``.
            rendering_state (google.cloud.deploy_v1.types.Release.TargetRender.TargetRenderState):
                Output only. Current state of the render
                operation for this Target.
            metadata (google.cloud.deploy_v1.types.RenderMetadata):
                Output only. Metadata related to the ``Release`` render for
                this Target.
            failure_cause (google.cloud.deploy_v1.types.Release.TargetRender.FailureCause):
                Output only. Reason this render failed. This
                will always be unspecified while the render in
                progress.
            failure_message (str):
                Output only. Additional information about the
                render failure, if available.
        """

        class TargetRenderState(proto.Enum):
            r"""Valid states of the render operation.

            Values:
                TARGET_RENDER_STATE_UNSPECIFIED (0):
                    The render operation state is unspecified.
                SUCCEEDED (1):
                    The render operation has completed
                    successfully.
                FAILED (2):
                    The render operation has failed.
                IN_PROGRESS (3):
                    The render operation is in progress.
            """

            TARGET_RENDER_STATE_UNSPECIFIED = 0
            SUCCEEDED = 1
            FAILED = 2
            IN_PROGRESS = 3

        class FailureCause(proto.Enum):
            r"""Well-known rendering failures.

            Values:
                FAILURE_CAUSE_UNSPECIFIED (0):
                    No reason for failure is specified.
                CLOUD_BUILD_UNAVAILABLE (1):
                    Cloud Build is not available, either because it is not
                    enabled or because Cloud Deploy has insufficient
                    permissions. See `required
                    permission <https://cloud.google.com/deploy/docs/cloud-deploy-service-account#required_permissions>`__.
                EXECUTION_FAILED (2):
                    The render operation did not complete
                    successfully; check Cloud Build logs.
                CLOUD_BUILD_REQUEST_FAILED (3):
                    Cloud Build failed to fulfill Cloud Deploy's request. See
                    failure_message for additional details.
                VERIFICATION_CONFIG_NOT_FOUND (4):
                    The render operation did not complete
                    successfully because the verification stanza
                    required for verify was not found on the
                    Skaffold configuration.
                CUSTOM_ACTION_NOT_FOUND (5):
                    The render operation did not complete successfully because
                    the custom action(s) required for Rollout jobs were not
                    found in the Skaffold configuration. See failure_message for
                    additional details.
                DEPLOYMENT_STRATEGY_NOT_SUPPORTED (6):
                    Release failed during rendering because the
                    release configuration is not supported with the
                    specified deployment strategy.
                RENDER_FEATURE_NOT_SUPPORTED (7):
                    The render operation had a feature configured
                    that is not supported.
            """

            FAILURE_CAUSE_UNSPECIFIED = 0
            CLOUD_BUILD_UNAVAILABLE = 1
            EXECUTION_FAILED = 2
            CLOUD_BUILD_REQUEST_FAILED = 3
            VERIFICATION_CONFIG_NOT_FOUND = 4
            CUSTOM_ACTION_NOT_FOUND = 5
            DEPLOYMENT_STRATEGY_NOT_SUPPORTED = 6
            RENDER_FEATURE_NOT_SUPPORTED = 7

        rendering_build: str = proto.Field(
            proto.STRING,
            number=1,
        )
        rendering_state: "Release.TargetRender.TargetRenderState" = proto.Field(
            proto.ENUM,
            number=2,
            enum="Release.TargetRender.TargetRenderState",
        )
        metadata: "RenderMetadata" = proto.Field(
            proto.MESSAGE,
            number=6,
            message="RenderMetadata",
        )
        failure_cause: "Release.TargetRender.FailureCause" = proto.Field(
            proto.ENUM,
            number=4,
            enum="Release.TargetRender.FailureCause",
        )
        failure_message: str = proto.Field(
            proto.STRING,
            number=5,
        )

    class ReleaseReadyCondition(proto.Message):
        r"""ReleaseReadyCondition contains information around the status
        of the Release. If a release is not ready, you cannot create a
        rollout with the release.

        Attributes:
            status (bool):
                True if the Release is in a valid state. Otherwise at least
                one condition in ``ReleaseCondition`` is in an invalid
                state. Iterate over those conditions and see which
                condition(s) has status = false to find out what is wrong
                with the Release.
        """

        status: bool = proto.Field(
            proto.BOOL,
            number=1,
        )

    class SkaffoldSupportedCondition(proto.Message):
        r"""SkaffoldSupportedCondition contains information about when
        support for the release's version of Skaffold ends.

        Attributes:
            status (bool):
                True if the version of Skaffold used by this
                release is supported.
            skaffold_support_state (google.cloud.deploy_v1.types.SkaffoldSupportState):
                The Skaffold support state for this release's
                version of Skaffold.
            maintenance_mode_time (google.protobuf.timestamp_pb2.Timestamp):
                The time at which this release's version of
                Skaffold will enter maintenance mode.
            support_expiration_time (google.protobuf.timestamp_pb2.Timestamp):
                The time at which this release's version of
                Skaffold will no longer be supported.
        """

        status: bool = proto.Field(
            proto.BOOL,
            number=1,
        )
        skaffold_support_state: "SkaffoldSupportState" = proto.Field(
            proto.ENUM,
            number=2,
            enum="SkaffoldSupportState",
        )
        maintenance_mode_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=3,
            message=timestamp_pb2.Timestamp,
        )
        support_expiration_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=4,
            message=timestamp_pb2.Timestamp,
        )

    class ReleaseCondition(proto.Message):
        r"""ReleaseCondition contains all conditions relevant to a
        Release.

        Attributes:
            release_ready_condition (google.cloud.deploy_v1.types.Release.ReleaseReadyCondition):
                Details around the Releases's overall status.
            skaffold_supported_condition (google.cloud.deploy_v1.types.Release.SkaffoldSupportedCondition):
                Details around the support state of the
                release's Skaffold version.
        """

        release_ready_condition: "Release.ReleaseReadyCondition" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="Release.ReleaseReadyCondition",
        )
        skaffold_supported_condition: "Release.SkaffoldSupportedCondition" = (
            proto.Field(
                proto.MESSAGE,
                number=2,
                message="Release.SkaffoldSupportedCondition",
            )
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    abandoned: bool = proto.Field(
        proto.BOOL,
        number=23,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    render_start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    render_end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    skaffold_config_uri: str = proto.Field(
        proto.STRING,
        number=17,
    )
    skaffold_config_path: str = proto.Field(
        proto.STRING,
        number=9,
    )
    build_artifacts: MutableSequence["BuildArtifact"] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message="BuildArtifact",
    )
    delivery_pipeline_snapshot: "DeliveryPipeline" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="DeliveryPipeline",
    )
    target_snapshots: MutableSequence["Target"] = proto.RepeatedField(
        proto.MESSAGE,
        number=12,
        message="Target",
    )
    custom_target_type_snapshots: MutableSequence["CustomTargetType"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=27,
            message="CustomTargetType",
        )
    )
    render_state: RenderState = proto.Field(
        proto.ENUM,
        number=13,
        enum=RenderState,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=16,
    )
    skaffold_version: str = proto.Field(
        proto.STRING,
        number=19,
    )
    target_artifacts: MutableMapping[str, "TargetArtifact"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=20,
        message="TargetArtifact",
    )
    target_renders: MutableMapping[str, TargetRender] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=22,
        message=TargetRender,
    )
    condition: ReleaseCondition = proto.Field(
        proto.MESSAGE,
        number=24,
        message=ReleaseCondition,
    )
    deploy_parameters: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=25,
    )


class CreateDeployPolicyRequest(proto.Message):
    r"""The request object for ``CreateDeployPolicy``.

    Attributes:
        parent (str):
            Required. The parent collection in which the
            ``DeployPolicy`` must be created. The format is
            ``projects/{project_id}/locations/{location_name}``.
        deploy_policy_id (str):
            Required. ID of the ``DeployPolicy``.
        deploy_policy (google.cloud.deploy_v1.types.DeployPolicy):
            Required. The ``DeployPolicy`` to create.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server knows to ignore
            the request if it has already been completed.
            The server guarantees that for at least 60
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
        validate_only (bool):
            Optional. If set to true, the request is
            validated and the user is provided with an
            expected result, but no actual change is made.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    deploy_policy_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    deploy_policy: "DeployPolicy" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="DeployPolicy",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class UpdateDeployPolicyRequest(proto.Message):
    r"""The request object for ``UpdateDeployPolicy``.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten by the update in the ``DeployPolicy`` resource.
            The fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it's in the mask. If the user doesn't provide a mask then
            all fields are overwritten.
        deploy_policy (google.cloud.deploy_v1.types.DeployPolicy):
            Required. The ``DeployPolicy`` to update.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server knows to ignore
            the request if it has already been completed.
            The server guarantees that for at least 60
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
        allow_missing (bool):
            Optional. If set to true, updating a ``DeployPolicy`` that
            does not exist will result in the creation of a new
            ``DeployPolicy``.
        validate_only (bool):
            Optional. If set to true, the request is
            validated and the user is provided with an
            expected result, but no actual change is made.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    deploy_policy: "DeployPolicy" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DeployPolicy",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class DeleteDeployPolicyRequest(proto.Message):
    r"""The request object for ``DeleteDeployPolicy``.

    Attributes:
        name (str):
            Required. The name of the ``DeployPolicy`` to delete. The
            format is
            ``projects/{project_id}/locations/{location_name}/deployPolicies/{deploy_policy_name}``.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server knows to ignore
            the request if it has already been completed.
            The server guarantees that for at least 60
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
        allow_missing (bool):
            Optional. If set to true, then deleting an already deleted
            or non-existing ``DeployPolicy`` will succeed.
        validate_only (bool):
            Optional. If set, validate the request and
            preview the review, but do not actually post it.
        etag (str):
            Optional. This checksum is computed by the
            server based on the value of other fields, and
            may be sent on update and delete requests to
            ensure the client has an up-to-date value before
            proceeding.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
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


class ListDeployPoliciesRequest(proto.Message):
    r"""The request object for ``ListDeployPolicies``.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of deploy
            policies. Format must be
            ``projects/{project_id}/locations/{location_name}``.
        page_size (int):
            The maximum number of deploy policies to
            return. The service may return fewer than this
            value. If unspecified, at most 50 deploy
            policies will be returned. The maximum value is
            1000; values above 1000 will be set to 1000.
        page_token (str):
            A page token, received from a previous
            ``ListDeployPolicies`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other provided parameters match the
            call that provided the page token.
        filter (str):
            Filter deploy policies to be returned. See
            https://google.aip.dev/160 for more details. All
            fields can be used in the filter.
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


class ListDeployPoliciesResponse(proto.Message):
    r"""The response object from ``ListDeployPolicies``.

    Attributes:
        deploy_policies (MutableSequence[google.cloud.deploy_v1.types.DeployPolicy]):
            The ``DeployPolicy`` objects.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    deploy_policies: MutableSequence["DeployPolicy"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DeployPolicy",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetDeployPolicyRequest(proto.Message):
    r"""The request object for ``GetDeployPolicy``

    Attributes:
        name (str):
            Required. Name of the ``DeployPolicy``. Format must be
            ``projects/{project_id}/locations/{location_name}/deployPolicies/{deploy_policy_name}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class BuildArtifact(proto.Message):
    r"""Description of an a image to use during Skaffold rendering.

    Attributes:
        image (str):
            Optional. Image name in Skaffold
            configuration.
        tag (str):
            Optional. Image tag to use. This will
            generally be the full path to an image, such as
            "gcr.io/my-project/busybox:1.2.3" or
            "gcr.io/my-project/busybox@sha256:abc123".
    """

    image: str = proto.Field(
        proto.STRING,
        number=3,
    )
    tag: str = proto.Field(
        proto.STRING,
        number=2,
    )


class TargetArtifact(proto.Message):
    r"""The artifacts produced by a target render operation.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        artifact_uri (str):
            Output only. URI of a directory containing
            the artifacts. This contains deployment
            configuration used by Skaffold during a rollout,
            and all paths are relative to this location.

            This field is a member of `oneof`_ ``uri``.
        skaffold_config_path (str):
            Output only. File path of the resolved
            Skaffold configuration for the stable phase,
            relative to the URI.
        manifest_path (str):
            Output only. File path of the rendered
            manifest relative to the URI for the stable
            phase.
        phase_artifacts (MutableMapping[str, google.cloud.deploy_v1.types.TargetArtifact.PhaseArtifact]):
            Output only. Map from the phase ID to the phase artifacts
            for the ``Target``.
    """

    class PhaseArtifact(proto.Message):
        r"""Contains the paths to the artifacts, relative to the URI, for
        a phase.

        Attributes:
            skaffold_config_path (str):
                Output only. File path of the resolved
                Skaffold configuration relative to the URI.
            manifest_path (str):
                Output only. File path of the rendered
                manifest relative to the URI.
            job_manifests_path (str):
                Output only. File path of the directory of
                rendered job manifests relative to the URI. This
                is only set if it is applicable.
        """

        skaffold_config_path: str = proto.Field(
            proto.STRING,
            number=1,
        )
        manifest_path: str = proto.Field(
            proto.STRING,
            number=3,
        )
        job_manifests_path: str = proto.Field(
            proto.STRING,
            number=4,
        )

    artifact_uri: str = proto.Field(
        proto.STRING,
        number=4,
        oneof="uri",
    )
    skaffold_config_path: str = proto.Field(
        proto.STRING,
        number=2,
    )
    manifest_path: str = proto.Field(
        proto.STRING,
        number=3,
    )
    phase_artifacts: MutableMapping[str, PhaseArtifact] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=5,
        message=PhaseArtifact,
    )


class DeployArtifact(proto.Message):
    r"""The artifacts produced by a deploy operation.

    Attributes:
        artifact_uri (str):
            Output only. URI of a directory containing
            the artifacts. All paths are relative to this
            location.
        manifest_paths (MutableSequence[str]):
            Output only. File paths of the manifests
            applied during the deploy operation relative to
            the URI.
    """

    artifact_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    manifest_paths: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class CloudRunRenderMetadata(proto.Message):
    r"""CloudRunRenderMetadata contains Cloud Run information associated
    with a ``Release`` render.

    Attributes:
        service (str):
            Output only. The name of the Cloud Run Service in the
            rendered manifest. Format is
            ``projects/{project}/locations/{location}/services/{service}``.
    """

    service: str = proto.Field(
        proto.STRING,
        number=1,
    )


class RenderMetadata(proto.Message):
    r"""RenderMetadata includes information associated with a ``Release``
    render.

    Attributes:
        cloud_run (google.cloud.deploy_v1.types.CloudRunRenderMetadata):
            Output only. Metadata associated with
            rendering for Cloud Run.
        custom (google.cloud.deploy_v1.types.CustomMetadata):
            Output only. Custom metadata provided by
            user-defined render operation.
    """

    cloud_run: "CloudRunRenderMetadata" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="CloudRunRenderMetadata",
    )
    custom: "CustomMetadata" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="CustomMetadata",
    )


class ListReleasesRequest(proto.Message):
    r"""The request object for ``ListReleases``.

    Attributes:
        parent (str):
            Required. The ``DeliveryPipeline`` which owns this
            collection of ``Release`` objects.
        page_size (int):
            Optional. The maximum number of ``Release`` objects to
            return. The service may return fewer than this value. If
            unspecified, at most 50 ``Release`` objects will be
            returned. The maximum value is 1000; values above 1000 will
            be set to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListReleases`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other provided parameters match the
            call that provided the page token.
        filter (str):
            Optional. Filter releases to be returned. See
            https://google.aip.dev/160 for more details.
        order_by (str):
            Optional. Field to sort by. See
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


class ListReleasesResponse(proto.Message):
    r"""The response object from ``ListReleases``.

    Attributes:
        releases (MutableSequence[google.cloud.deploy_v1.types.Release]):
            The ``Release`` objects.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    releases: MutableSequence["Release"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Release",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetReleaseRequest(proto.Message):
    r"""The request object for ``GetRelease``.

    Attributes:
        name (str):
            Required. Name of the ``Release``. Format must be
            ``projects/{project_id}/locations/{location_name}/deliveryPipelines/{pipeline_name}/releases/{release_name}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateReleaseRequest(proto.Message):
    r"""The request object for ``CreateRelease``,

    Attributes:
        parent (str):
            Required. The parent collection in which the ``Release`` is
            created. The format is
            ``projects/{project_id}/locations/{location_name}/deliveryPipelines/{pipeline_name}``.
        release_id (str):
            Required. ID of the ``Release``.
        release (google.cloud.deploy_v1.types.Release):
            Required. The ``Release`` to create.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server knows to ignore
            the request if it has already been completed.
            The server guarantees that for at least 60
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
        validate_only (bool):
            Optional. If set to true, the request is
            validated and the user is provided with an
            expected result, but no actual change is made.
        override_deploy_policy (MutableSequence[str]):
            Optional. Deploy policies to override. Format is
            ``projects/{project}/locations/{location}/deployPolicies/{deployPolicy}``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    release_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    release: "Release" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Release",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    override_deploy_policy: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )


class Rollout(proto.Message):
    r"""A ``Rollout`` resource in the Cloud Deploy API.

    A ``Rollout`` contains information around a specific deployment to a
    ``Target``.

    Attributes:
        name (str):
            Identifier. Name of the ``Rollout``. Format is
            ``projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{release}/rollouts/{rollout}``.
            The ``rollout`` component must match
            ``[a-z]([a-z0-9-]{0,61}[a-z0-9])?``
        uid (str):
            Output only. Unique identifier of the ``Rollout``.
        description (str):
            Optional. Description of the ``Rollout`` for user purposes.
            Max length is 255 characters.
        annotations (MutableMapping[str, str]):
            Optional. User annotations. These attributes
            can only be set and used by the user, and not by
            Cloud Deploy. See
            https://google.aip.dev/128#annotations for more
            details such as format and size limitations.
        labels (MutableMapping[str, str]):
            Labels are attributes that can be set and used by both the
            user and by Cloud Deploy. Labels must meet the following
            constraints:

            - Keys and values can contain only lowercase letters,
              numeric characters, underscores, and dashes.
            - All characters must use UTF-8 encoding, and international
              characters are allowed.
            - Keys must start with a lowercase letter or international
              character.
            - Each resource is limited to a maximum of 64 labels.

            Both keys and values are additionally constrained to be <=
            128 bytes.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time at which the ``Rollout`` was created.
        approve_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time at which the ``Rollout`` was approved.
        enqueue_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time at which the ``Rollout`` was enqueued.
        deploy_start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time at which the ``Rollout`` started
            deploying.
        deploy_end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time at which the ``Rollout`` finished
            deploying.
        target_id (str):
            Required. The ID of Target to which this ``Rollout`` is
            deploying.
        approval_state (google.cloud.deploy_v1.types.Rollout.ApprovalState):
            Output only. Approval state of the ``Rollout``.
        state (google.cloud.deploy_v1.types.Rollout.State):
            Output only. Current state of the ``Rollout``.
        failure_reason (str):
            Output only. Additional information about the
            rollout failure, if available.
        deploying_build (str):
            Output only. The resource name of the Cloud Build ``Build``
            object that is used to deploy the Rollout. Format is
            ``projects/{project}/locations/{location}/builds/{build}``.
        etag (str):
            This checksum is computed by the server based
            on the value of other fields, and may be sent on
            update and delete requests to ensure the client
            has an up-to-date value before proceeding.
        deploy_failure_cause (google.cloud.deploy_v1.types.Rollout.FailureCause):
            Output only. The reason this rollout failed.
            This will always be unspecified while the
            rollout is in progress.
        phases (MutableSequence[google.cloud.deploy_v1.types.Phase]):
            Output only. The phases that represent the workflows of this
            ``Rollout``.
        metadata (google.cloud.deploy_v1.types.Metadata):
            Output only. Metadata contains information
            about the rollout.
        controller_rollout (str):
            Output only. Name of the ``ControllerRollout``. Format is
            ``projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{release}/rollouts/{rollout}``.
        rollback_of_rollout (str):
            Output only. Name of the ``Rollout`` that is rolled back by
            this ``Rollout``. Empty if this ``Rollout`` wasn't created
            as a rollback.
        rolled_back_by_rollouts (MutableSequence[str]):
            Output only. Names of ``Rollouts`` that rolled back this
            ``Rollout``.
        active_repair_automation_run (str):
            Output only. The AutomationRun actively
            repairing the rollout.
    """

    class ApprovalState(proto.Enum):
        r"""Valid approval states of a ``Rollout``.

        Values:
            APPROVAL_STATE_UNSPECIFIED (0):
                The ``Rollout`` has an unspecified approval state.
            NEEDS_APPROVAL (1):
                The ``Rollout`` requires approval.
            DOES_NOT_NEED_APPROVAL (2):
                The ``Rollout`` does not require approval.
            APPROVED (3):
                The ``Rollout`` has been approved.
            REJECTED (4):
                The ``Rollout`` has been rejected.
        """

        APPROVAL_STATE_UNSPECIFIED = 0
        NEEDS_APPROVAL = 1
        DOES_NOT_NEED_APPROVAL = 2
        APPROVED = 3
        REJECTED = 4

    class State(proto.Enum):
        r"""Valid states of a ``Rollout``.

        Values:
            STATE_UNSPECIFIED (0):
                The ``Rollout`` has an unspecified state.
            SUCCEEDED (1):
                The ``Rollout`` has completed successfully.
            FAILED (2):
                The ``Rollout`` has failed.
            IN_PROGRESS (3):
                The ``Rollout`` is being deployed.
            PENDING_APPROVAL (4):
                The ``Rollout`` needs approval.
            APPROVAL_REJECTED (5):
                An approver rejected the ``Rollout``.
            PENDING (6):
                The ``Rollout`` is waiting for an earlier Rollout(s) to
                complete on this ``Target``.
            PENDING_RELEASE (7):
                The ``Rollout`` is waiting for the ``Release`` to be fully
                rendered.
            CANCELLING (8):
                The ``Rollout`` is in the process of being cancelled.
            CANCELLED (9):
                The ``Rollout`` has been cancelled.
            HALTED (10):
                The ``Rollout`` is halted.
        """

        STATE_UNSPECIFIED = 0
        SUCCEEDED = 1
        FAILED = 2
        IN_PROGRESS = 3
        PENDING_APPROVAL = 4
        APPROVAL_REJECTED = 5
        PENDING = 6
        PENDING_RELEASE = 7
        CANCELLING = 8
        CANCELLED = 9
        HALTED = 10

    class FailureCause(proto.Enum):
        r"""Well-known rollout failures.

        Values:
            FAILURE_CAUSE_UNSPECIFIED (0):
                No reason for failure is specified.
            CLOUD_BUILD_UNAVAILABLE (1):
                Cloud Build is not available, either because it is not
                enabled or because Cloud Deploy has insufficient
                permissions. See `required
                permission <https://cloud.google.com/deploy/docs/cloud-deploy-service-account#required_permissions>`__.
            EXECUTION_FAILED (2):
                The deploy operation did not complete
                successfully; check Cloud Build logs.
            DEADLINE_EXCEEDED (3):
                Deployment did not complete within the
                allotted time.
            RELEASE_FAILED (4):
                Release is in a failed state.
            RELEASE_ABANDONED (5):
                Release is abandoned.
            VERIFICATION_CONFIG_NOT_FOUND (6):
                No Skaffold verify configuration was found.
            CLOUD_BUILD_REQUEST_FAILED (7):
                Cloud Build failed to fulfill Cloud Deploy's request. See
                failure_message for additional details.
            OPERATION_FEATURE_NOT_SUPPORTED (8):
                A Rollout operation had a feature configured
                that is not supported.
        """

        FAILURE_CAUSE_UNSPECIFIED = 0
        CLOUD_BUILD_UNAVAILABLE = 1
        EXECUTION_FAILED = 2
        DEADLINE_EXCEEDED = 3
        RELEASE_FAILED = 4
        RELEASE_ABANDONED = 5
        VERIFICATION_CONFIG_NOT_FOUND = 6
        CLOUD_BUILD_REQUEST_FAILED = 7
        OPERATION_FEATURE_NOT_SUPPORTED = 8

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    approve_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    enqueue_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    deploy_start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    deploy_end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    target_id: str = proto.Field(
        proto.STRING,
        number=18,
    )
    approval_state: ApprovalState = proto.Field(
        proto.ENUM,
        number=12,
        enum=ApprovalState,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=13,
        enum=State,
    )
    failure_reason: str = proto.Field(
        proto.STRING,
        number=14,
    )
    deploying_build: str = proto.Field(
        proto.STRING,
        number=17,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=16,
    )
    deploy_failure_cause: FailureCause = proto.Field(
        proto.ENUM,
        number=19,
        enum=FailureCause,
    )
    phases: MutableSequence["Phase"] = proto.RepeatedField(
        proto.MESSAGE,
        number=23,
        message="Phase",
    )
    metadata: "Metadata" = proto.Field(
        proto.MESSAGE,
        number=24,
        message="Metadata",
    )
    controller_rollout: str = proto.Field(
        proto.STRING,
        number=25,
    )
    rollback_of_rollout: str = proto.Field(
        proto.STRING,
        number=26,
    )
    rolled_back_by_rollouts: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=27,
    )
    active_repair_automation_run: str = proto.Field(
        proto.STRING,
        number=28,
    )


class Metadata(proto.Message):
    r"""Metadata includes information associated with a ``Rollout``.

    Attributes:
        cloud_run (google.cloud.deploy_v1.types.CloudRunMetadata):
            Output only. The name of the Cloud Run Service that is
            associated with a ``Rollout``.
        automation (google.cloud.deploy_v1.types.AutomationRolloutMetadata):
            Output only. AutomationRolloutMetadata
            contains the information about the interactions
            between Automation service and this rollout.
        custom (google.cloud.deploy_v1.types.CustomMetadata):
            Output only. Custom metadata provided by user-defined
            ``Rollout`` operations.
    """

    cloud_run: "CloudRunMetadata" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="CloudRunMetadata",
    )
    automation: "AutomationRolloutMetadata" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="AutomationRolloutMetadata",
    )
    custom: "CustomMetadata" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="CustomMetadata",
    )


class DeployJobRunMetadata(proto.Message):
    r"""DeployJobRunMetadata surfaces information associated with a
    ``DeployJobRun`` to the user.

    Attributes:
        cloud_run (google.cloud.deploy_v1.types.CloudRunMetadata):
            Output only. The name of the Cloud Run Service that is
            associated with a ``DeployJobRun``.
        custom_target (google.cloud.deploy_v1.types.CustomTargetDeployMetadata):
            Output only. Custom Target metadata associated with a
            ``DeployJobRun``.
        custom (google.cloud.deploy_v1.types.CustomMetadata):
            Output only. Custom metadata provided by
            user-defined deploy operation.
    """

    cloud_run: "CloudRunMetadata" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="CloudRunMetadata",
    )
    custom_target: "CustomTargetDeployMetadata" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="CustomTargetDeployMetadata",
    )
    custom: "CustomMetadata" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="CustomMetadata",
    )


class CloudRunMetadata(proto.Message):
    r"""CloudRunMetadata contains information from a Cloud Run
    deployment.

    Attributes:
        service (str):
            Output only. The name of the Cloud Run Service that is
            associated with a ``Rollout``. Format is
            ``projects/{project}/locations/{location}/services/{service}``.
        service_urls (MutableSequence[str]):
            Output only. The Cloud Run Service urls that are associated
            with a ``Rollout``.
        revision (str):
            Output only. The Cloud Run Revision id associated with a
            ``Rollout``.
        job (str):
            Output only. The name of the Cloud Run job that is
            associated with a ``Rollout``. Format is
            ``projects/{project}/locations/{location}/jobs/{job_name}``.
    """

    service: str = proto.Field(
        proto.STRING,
        number=1,
    )
    service_urls: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    revision: str = proto.Field(
        proto.STRING,
        number=3,
    )
    job: str = proto.Field(
        proto.STRING,
        number=4,
    )


class CustomTargetDeployMetadata(proto.Message):
    r"""CustomTargetDeployMetadata contains information from a Custom
    Target deploy operation.

    Attributes:
        skip_message (str):
            Output only. Skip message provided in the
            results of a custom deploy operation.
    """

    skip_message: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AutomationRolloutMetadata(proto.Message):
    r"""AutomationRolloutMetadata contains Automation-related actions
    that were performed on a rollout.

    Attributes:
        promote_automation_run (str):
            Output only. The name of the AutomationRun
            initiated by a promote release rule.
        advance_automation_runs (MutableSequence[str]):
            Output only. The names of the AutomationRuns
            initiated by an advance rollout rule.
        repair_automation_runs (MutableSequence[str]):
            Output only. The names of the AutomationRuns
            initiated by a repair rollout rule.
    """

    promote_automation_run: str = proto.Field(
        proto.STRING,
        number=1,
    )
    advance_automation_runs: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    repair_automation_runs: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class CustomMetadata(proto.Message):
    r"""CustomMetadata contains information from a user-defined
    operation.

    Attributes:
        values (MutableMapping[str, str]):
            Output only. Key-value pairs provided by the
            user-defined operation.
    """

    values: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=1,
    )


class Phase(proto.Message):
    r"""Phase represents a collection of jobs that are logically grouped
    together for a ``Rollout``.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        id (str):
            Output only. The ID of the Phase.
        state (google.cloud.deploy_v1.types.Phase.State):
            Output only. Current state of the Phase.
        skip_message (str):
            Output only. Additional information on why
            the Phase was skipped, if available.
        deployment_jobs (google.cloud.deploy_v1.types.DeploymentJobs):
            Output only. Deployment job composition.

            This field is a member of `oneof`_ ``jobs``.
        child_rollout_jobs (google.cloud.deploy_v1.types.ChildRolloutJobs):
            Output only. ChildRollout job composition.

            This field is a member of `oneof`_ ``jobs``.
    """

    class State(proto.Enum):
        r"""Valid states of a Phase.

        Values:
            STATE_UNSPECIFIED (0):
                The Phase has an unspecified state.
            PENDING (1):
                The Phase is waiting for an earlier Phase(s)
                to complete.
            IN_PROGRESS (2):
                The Phase is in progress.
            SUCCEEDED (3):
                The Phase has succeeded.
            FAILED (4):
                The Phase has failed.
            ABORTED (5):
                The Phase was aborted.
            SKIPPED (6):
                The Phase was skipped.
        """

        STATE_UNSPECIFIED = 0
        PENDING = 1
        IN_PROGRESS = 2
        SUCCEEDED = 3
        FAILED = 4
        ABORTED = 5
        SKIPPED = 6

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )
    skip_message: str = proto.Field(
        proto.STRING,
        number=6,
    )
    deployment_jobs: "DeploymentJobs" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="jobs",
        message="DeploymentJobs",
    )
    child_rollout_jobs: "ChildRolloutJobs" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="jobs",
        message="ChildRolloutJobs",
    )


class DeploymentJobs(proto.Message):
    r"""Deployment job composition.

    Attributes:
        predeploy_job (google.cloud.deploy_v1.types.Job):
            Output only. The predeploy Job, which is the
            first job on the phase.
        deploy_job (google.cloud.deploy_v1.types.Job):
            Output only. The deploy Job. This is the
            deploy job in the phase.
        verify_job (google.cloud.deploy_v1.types.Job):
            Output only. The verify Job. Runs after a
            deploy if the deploy succeeds.
        postdeploy_job (google.cloud.deploy_v1.types.Job):
            Output only. The postdeploy Job, which is the
            last job on the phase.
    """

    predeploy_job: "Job" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Job",
    )
    deploy_job: "Job" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Job",
    )
    verify_job: "Job" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Job",
    )
    postdeploy_job: "Job" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="Job",
    )


class ChildRolloutJobs(proto.Message):
    r"""ChildRollouts job composition

    Attributes:
        create_rollout_jobs (MutableSequence[google.cloud.deploy_v1.types.Job]):
            Output only. List of CreateChildRolloutJobs
        advance_rollout_jobs (MutableSequence[google.cloud.deploy_v1.types.Job]):
            Output only. List of AdvanceChildRolloutJobs
    """

    create_rollout_jobs: MutableSequence["Job"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Job",
    )
    advance_rollout_jobs: MutableSequence["Job"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Job",
    )


class Job(proto.Message):
    r"""Job represents an operation for a ``Rollout``.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        id (str):
            Output only. The ID of the Job.
        state (google.cloud.deploy_v1.types.Job.State):
            Output only. The current state of the Job.
        skip_message (str):
            Output only. Additional information on why
            the Job was skipped, if available.
        job_run (str):
            Output only. The name of the ``JobRun`` responsible for the
            most recent invocation of this Job.
        deploy_job (google.cloud.deploy_v1.types.DeployJob):
            Output only. A deploy Job.

            This field is a member of `oneof`_ ``job_type``.
        verify_job (google.cloud.deploy_v1.types.VerifyJob):
            Output only. A verify Job.

            This field is a member of `oneof`_ ``job_type``.
        predeploy_job (google.cloud.deploy_v1.types.PredeployJob):
            Output only. A predeploy Job.

            This field is a member of `oneof`_ ``job_type``.
        postdeploy_job (google.cloud.deploy_v1.types.PostdeployJob):
            Output only. A postdeploy Job.

            This field is a member of `oneof`_ ``job_type``.
        create_child_rollout_job (google.cloud.deploy_v1.types.CreateChildRolloutJob):
            Output only. A createChildRollout Job.

            This field is a member of `oneof`_ ``job_type``.
        advance_child_rollout_job (google.cloud.deploy_v1.types.AdvanceChildRolloutJob):
            Output only. An advanceChildRollout Job.

            This field is a member of `oneof`_ ``job_type``.
    """

    class State(proto.Enum):
        r"""Valid states of a Job.

        Values:
            STATE_UNSPECIFIED (0):
                The Job has an unspecified state.
            PENDING (1):
                The Job is waiting for an earlier Phase(s) or
                Job(s) to complete.
            DISABLED (2):
                The Job is disabled.
            IN_PROGRESS (3):
                The Job is in progress.
            SUCCEEDED (4):
                The Job succeeded.
            FAILED (5):
                The Job failed.
            ABORTED (6):
                The Job was aborted.
            SKIPPED (7):
                The Job was skipped.
            IGNORED (8):
                The Job was ignored.
        """

        STATE_UNSPECIFIED = 0
        PENDING = 1
        DISABLED = 2
        IN_PROGRESS = 3
        SUCCEEDED = 4
        FAILED = 5
        ABORTED = 6
        SKIPPED = 7
        IGNORED = 8

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=2,
        enum=State,
    )
    skip_message: str = proto.Field(
        proto.STRING,
        number=8,
    )
    job_run: str = proto.Field(
        proto.STRING,
        number=3,
    )
    deploy_job: "DeployJob" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="job_type",
        message="DeployJob",
    )
    verify_job: "VerifyJob" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="job_type",
        message="VerifyJob",
    )
    predeploy_job: "PredeployJob" = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="job_type",
        message="PredeployJob",
    )
    postdeploy_job: "PostdeployJob" = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="job_type",
        message="PostdeployJob",
    )
    create_child_rollout_job: "CreateChildRolloutJob" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="job_type",
        message="CreateChildRolloutJob",
    )
    advance_child_rollout_job: "AdvanceChildRolloutJob" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="job_type",
        message="AdvanceChildRolloutJob",
    )


class DeployJob(proto.Message):
    r"""A deploy Job."""


class VerifyJob(proto.Message):
    r"""A verify Job."""


class PredeployJob(proto.Message):
    r"""A predeploy Job.

    Attributes:
        actions (MutableSequence[str]):
            Output only. The custom actions that the
            predeploy Job executes.
    """

    actions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class PostdeployJob(proto.Message):
    r"""A postdeploy Job.

    Attributes:
        actions (MutableSequence[str]):
            Output only. The custom actions that the
            postdeploy Job executes.
    """

    actions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class CreateChildRolloutJob(proto.Message):
    r"""A createChildRollout Job."""


class AdvanceChildRolloutJob(proto.Message):
    r"""An advanceChildRollout Job."""


class ListRolloutsRequest(proto.Message):
    r"""ListRolloutsRequest is the request object used by ``ListRollouts``.

    Attributes:
        parent (str):
            Required. The ``Release`` which owns this collection of
            ``Rollout`` objects.
        page_size (int):
            Optional. The maximum number of ``Rollout`` objects to
            return. The service may return fewer than this value. If
            unspecified, at most 50 ``Rollout`` objects will be
            returned. The maximum value is 1000; values above 1000 will
            be set to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListRollouts`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other provided parameters match the
            call that provided the page token.
        filter (str):
            Optional. Filter rollouts to be returned. See
            https://google.aip.dev/160 for more details.
        order_by (str):
            Optional. Field to sort by. See
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


class ListRolloutsResponse(proto.Message):
    r"""ListRolloutsResponse is the response object returned by
    ``ListRollouts``.

    Attributes:
        rollouts (MutableSequence[google.cloud.deploy_v1.types.Rollout]):
            The ``Rollout`` objects.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    rollouts: MutableSequence["Rollout"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Rollout",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetRolloutRequest(proto.Message):
    r"""GetRolloutRequest is the request object used by ``GetRollout``.

    Attributes:
        name (str):
            Required. Name of the ``Rollout``. Format must be
            ``projects/{project_id}/locations/{location_name}/deliveryPipelines/{pipeline_name}/releases/{release_name}/rollouts/{rollout_name}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateRolloutRequest(proto.Message):
    r"""CreateRolloutRequest is the request object used by
    ``CreateRollout``.

    Attributes:
        parent (str):
            Required. The parent collection in which the ``Rollout``
            must be created. The format is
            ``projects/{project_id}/locations/{location_name}/deliveryPipelines/{pipeline_name}/releases/{release_name}``.
        rollout_id (str):
            Required. ID of the ``Rollout``.
        rollout (google.cloud.deploy_v1.types.Rollout):
            Required. The ``Rollout`` to create.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server knows to ignore
            the request if it has already been completed.
            The server guarantees that for at least 60
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
        validate_only (bool):
            Optional. If set to true, the request is
            validated and the user is provided with an
            expected result, but no actual change is made.
        override_deploy_policy (MutableSequence[str]):
            Optional. Deploy policies to override. Format is
            ``projects/{project}/locations/{location}/deployPolicies/{deployPolicy}``.
        starting_phase_id (str):
            Optional. The starting phase ID for the ``Rollout``. If
            empty the ``Rollout`` will start at the first phase.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    rollout_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    rollout: "Rollout" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Rollout",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    override_deploy_policy: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    starting_phase_id: str = proto.Field(
        proto.STRING,
        number=7,
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
            successfully been cancelled have
            [google.longrunning.Operation.error][google.longrunning.Operation.error]
            value with a
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


class ApproveRolloutRequest(proto.Message):
    r"""The request object used by ``ApproveRollout``.

    Attributes:
        name (str):
            Required. Name of the Rollout. Format is
            ``projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{release}/rollouts/{rollout}``.
        approved (bool):
            Required. True = approve; false = reject
        override_deploy_policy (MutableSequence[str]):
            Optional. Deploy policies to override. Format is
            ``projects/{project}/locations/{location}/deployPolicies/{deployPolicy}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    approved: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    override_deploy_policy: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class ApproveRolloutResponse(proto.Message):
    r"""The response object from ``ApproveRollout``."""


class AdvanceRolloutRequest(proto.Message):
    r"""The request object used by ``AdvanceRollout``.

    Attributes:
        name (str):
            Required. Name of the Rollout. Format is
            ``projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{release}/rollouts/{rollout}``.
        phase_id (str):
            Required. The phase ID to advance the ``Rollout`` to.
        override_deploy_policy (MutableSequence[str]):
            Optional. Deploy policies to override. Format is
            ``projects/{project}/locations/{location}/deployPolicies/{deployPolicy}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    phase_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    override_deploy_policy: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class AdvanceRolloutResponse(proto.Message):
    r"""The response object from ``AdvanceRollout``."""


class CancelRolloutRequest(proto.Message):
    r"""The request object used by ``CancelRollout``.

    Attributes:
        name (str):
            Required. Name of the Rollout. Format is
            ``projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{release}/rollouts/{rollout}``.
        override_deploy_policy (MutableSequence[str]):
            Optional. Deploy policies to override. Format is
            ``projects/{project}/locations/{location}/deployPolicies/{deployPolicy}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    override_deploy_policy: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class CancelRolloutResponse(proto.Message):
    r"""The response object from ``CancelRollout``."""


class IgnoreJobRequest(proto.Message):
    r"""The request object used by ``IgnoreJob``.

    Attributes:
        rollout (str):
            Required. Name of the Rollout. Format is
            ``projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{release}/rollouts/{rollout}``.
        phase_id (str):
            Required. The phase ID the Job to ignore
            belongs to.
        job_id (str):
            Required. The job ID for the Job to ignore.
        override_deploy_policy (MutableSequence[str]):
            Optional. Deploy policies to override. Format is
            ``projects/{project}/locations/{location}/deployPolicies/{deployPolicy}``.
    """

    rollout: str = proto.Field(
        proto.STRING,
        number=1,
    )
    phase_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    job_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    override_deploy_policy: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )


class IgnoreJobResponse(proto.Message):
    r"""The response object from ``IgnoreJob``."""


class RetryJobRequest(proto.Message):
    r"""RetryJobRequest is the request object used by ``RetryJob``.

    Attributes:
        rollout (str):
            Required. Name of the Rollout. Format is
            ``projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{release}/rollouts/{rollout}``.
        phase_id (str):
            Required. The phase ID the Job to retry
            belongs to.
        job_id (str):
            Required. The job ID for the Job to retry.
        override_deploy_policy (MutableSequence[str]):
            Optional. Deploy policies to override. Format is
            ``projects/{project}/locations/{location}/deployPolicies/{deployPolicy}``.
    """

    rollout: str = proto.Field(
        proto.STRING,
        number=1,
    )
    phase_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    job_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    override_deploy_policy: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )


class RetryJobResponse(proto.Message):
    r"""The response object from 'RetryJob'."""


class AbandonReleaseRequest(proto.Message):
    r"""The request object used by ``AbandonRelease``.

    Attributes:
        name (str):
            Required. Name of the Release. Format is
            ``projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{release}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AbandonReleaseResponse(proto.Message):
    r"""The response object for ``AbandonRelease``."""


class JobRun(proto.Message):
    r"""A ``JobRun`` resource in the Cloud Deploy API.

    A ``JobRun`` contains information of a single ``Rollout`` job
    evaluation.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. Name of the ``JobRun``. Format is
            ``projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{releases}/rollouts/{rollouts}/jobRuns/{uuid}``.
        uid (str):
            Output only. Unique identifier of the ``JobRun``.
        phase_id (str):
            Output only. ID of the ``Rollout`` phase this ``JobRun``
            belongs in.
        job_id (str):
            Output only. ID of the ``Rollout`` job this ``JobRun``
            corresponds to.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time at which the ``JobRun`` was created.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time at which the ``JobRun`` was started.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time at which the ``JobRun`` ended.
        state (google.cloud.deploy_v1.types.JobRun.State):
            Output only. The current state of the ``JobRun``.
        deploy_job_run (google.cloud.deploy_v1.types.DeployJobRun):
            Output only. Information specific to a deploy ``JobRun``.

            This field is a member of `oneof`_ ``job_run``.
        verify_job_run (google.cloud.deploy_v1.types.VerifyJobRun):
            Output only. Information specific to a verify ``JobRun``.

            This field is a member of `oneof`_ ``job_run``.
        predeploy_job_run (google.cloud.deploy_v1.types.PredeployJobRun):
            Output only. Information specific to a predeploy ``JobRun``.

            This field is a member of `oneof`_ ``job_run``.
        postdeploy_job_run (google.cloud.deploy_v1.types.PostdeployJobRun):
            Output only. Information specific to a postdeploy
            ``JobRun``.

            This field is a member of `oneof`_ ``job_run``.
        create_child_rollout_job_run (google.cloud.deploy_v1.types.CreateChildRolloutJobRun):
            Output only. Information specific to a createChildRollout
            ``JobRun``.

            This field is a member of `oneof`_ ``job_run``.
        advance_child_rollout_job_run (google.cloud.deploy_v1.types.AdvanceChildRolloutJobRun):
            Output only. Information specific to an advanceChildRollout
            ``JobRun``

            This field is a member of `oneof`_ ``job_run``.
        etag (str):
            Output only. This checksum is computed by the
            server based on the value of other fields, and
            may be sent on update and delete requests to
            ensure the client has an up-to-date value before
            proceeding.
    """

    class State(proto.Enum):
        r"""Valid states of a ``JobRun``.

        Values:
            STATE_UNSPECIFIED (0):
                The ``JobRun`` has an unspecified state.
            IN_PROGRESS (1):
                The ``JobRun`` is in progress.
            SUCCEEDED (2):
                The ``JobRun`` has succeeded.
            FAILED (3):
                The ``JobRun`` has failed.
            TERMINATING (4):
                The ``JobRun`` is terminating.
            TERMINATED (5):
                The ``JobRun`` was terminated.
        """

        STATE_UNSPECIFIED = 0
        IN_PROGRESS = 1
        SUCCEEDED = 2
        FAILED = 3
        TERMINATING = 4
        TERMINATED = 5

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    phase_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    job_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=8,
        enum=State,
    )
    deploy_job_run: "DeployJobRun" = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="job_run",
        message="DeployJobRun",
    )
    verify_job_run: "VerifyJobRun" = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="job_run",
        message="VerifyJobRun",
    )
    predeploy_job_run: "PredeployJobRun" = proto.Field(
        proto.MESSAGE,
        number=14,
        oneof="job_run",
        message="PredeployJobRun",
    )
    postdeploy_job_run: "PostdeployJobRun" = proto.Field(
        proto.MESSAGE,
        number=15,
        oneof="job_run",
        message="PostdeployJobRun",
    )
    create_child_rollout_job_run: "CreateChildRolloutJobRun" = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="job_run",
        message="CreateChildRolloutJobRun",
    )
    advance_child_rollout_job_run: "AdvanceChildRolloutJobRun" = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="job_run",
        message="AdvanceChildRolloutJobRun",
    )
    etag: str = proto.Field(
        proto.STRING,
        number=11,
    )


class DeployJobRun(proto.Message):
    r"""DeployJobRun contains information specific to a deploy ``JobRun``.

    Attributes:
        build (str):
            Output only. The resource name of the Cloud Build ``Build``
            object that is used to deploy. Format is
            ``projects/{project}/locations/{location}/builds/{build}``.
        failure_cause (google.cloud.deploy_v1.types.DeployJobRun.FailureCause):
            Output only. The reason the deploy failed.
            This will always be unspecified while the deploy
            is in progress or if it succeeded.
        failure_message (str):
            Output only. Additional information about the
            deploy failure, if available.
        metadata (google.cloud.deploy_v1.types.DeployJobRunMetadata):
            Output only. Metadata containing information
            about the deploy job run.
        artifact (google.cloud.deploy_v1.types.DeployArtifact):
            Output only. The artifact of a deploy job
            run, if available.
    """

    class FailureCause(proto.Enum):
        r"""Well-known deploy failures.

        Values:
            FAILURE_CAUSE_UNSPECIFIED (0):
                No reason for failure is specified.
            CLOUD_BUILD_UNAVAILABLE (1):
                Cloud Build is not available, either because it is not
                enabled or because Cloud Deploy has insufficient
                permissions. See `Required
                permission <https://cloud.google.com/deploy/docs/cloud-deploy-service-account#required_permissions>`__.
            EXECUTION_FAILED (2):
                The deploy operation did not complete
                successfully; check Cloud Build logs.
            DEADLINE_EXCEEDED (3):
                The deploy job run did not complete within
                the allotted time.
            MISSING_RESOURCES_FOR_CANARY (4):
                There were missing resources in the runtime
                environment required for a canary deployment.
                Check the Cloud Build logs for more information.
            CLOUD_BUILD_REQUEST_FAILED (5):
                Cloud Build failed to fulfill Cloud Deploy's request. See
                failure_message for additional details.
            DEPLOY_FEATURE_NOT_SUPPORTED (6):
                The deploy operation had a feature configured
                that is not supported.
        """

        FAILURE_CAUSE_UNSPECIFIED = 0
        CLOUD_BUILD_UNAVAILABLE = 1
        EXECUTION_FAILED = 2
        DEADLINE_EXCEEDED = 3
        MISSING_RESOURCES_FOR_CANARY = 4
        CLOUD_BUILD_REQUEST_FAILED = 5
        DEPLOY_FEATURE_NOT_SUPPORTED = 6

    build: str = proto.Field(
        proto.STRING,
        number=1,
    )
    failure_cause: FailureCause = proto.Field(
        proto.ENUM,
        number=2,
        enum=FailureCause,
    )
    failure_message: str = proto.Field(
        proto.STRING,
        number=3,
    )
    metadata: "DeployJobRunMetadata" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="DeployJobRunMetadata",
    )
    artifact: "DeployArtifact" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="DeployArtifact",
    )


class VerifyJobRun(proto.Message):
    r"""VerifyJobRun contains information specific to a verify ``JobRun``.

    Attributes:
        build (str):
            Output only. The resource name of the Cloud Build ``Build``
            object that is used to verify. Format is
            ``projects/{project}/locations/{location}/builds/{build}``.
        artifact_uri (str):
            Output only. URI of a directory containing
            the verify artifacts. This contains the Skaffold
            event log.
        event_log_path (str):
            Output only. File path of the Skaffold event
            log relative to the artifact URI.
        failure_cause (google.cloud.deploy_v1.types.VerifyJobRun.FailureCause):
            Output only. The reason the verify failed.
            This will always be unspecified while the verify
            is in progress or if it succeeded.
        failure_message (str):
            Output only. Additional information about the
            verify failure, if available.
    """

    class FailureCause(proto.Enum):
        r"""Well-known verify failures.

        Values:
            FAILURE_CAUSE_UNSPECIFIED (0):
                No reason for failure is specified.
            CLOUD_BUILD_UNAVAILABLE (1):
                Cloud Build is not available, either because it is not
                enabled or because Cloud Deploy has insufficient
                permissions. See `required
                permission <https://cloud.google.com/deploy/docs/cloud-deploy-service-account#required_permissions>`__.
            EXECUTION_FAILED (2):
                The verify operation did not complete
                successfully; check Cloud Build logs.
            DEADLINE_EXCEEDED (3):
                The verify job run did not complete within
                the allotted time.
            VERIFICATION_CONFIG_NOT_FOUND (4):
                No Skaffold verify configuration was found.
            CLOUD_BUILD_REQUEST_FAILED (5):
                Cloud Build failed to fulfill Cloud Deploy's request. See
                failure_message for additional details.
        """

        FAILURE_CAUSE_UNSPECIFIED = 0
        CLOUD_BUILD_UNAVAILABLE = 1
        EXECUTION_FAILED = 2
        DEADLINE_EXCEEDED = 3
        VERIFICATION_CONFIG_NOT_FOUND = 4
        CLOUD_BUILD_REQUEST_FAILED = 5

    build: str = proto.Field(
        proto.STRING,
        number=1,
    )
    artifact_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    event_log_path: str = proto.Field(
        proto.STRING,
        number=3,
    )
    failure_cause: FailureCause = proto.Field(
        proto.ENUM,
        number=4,
        enum=FailureCause,
    )
    failure_message: str = proto.Field(
        proto.STRING,
        number=5,
    )


class PredeployJobRun(proto.Message):
    r"""PredeployJobRun contains information specific to a predeploy
    ``JobRun``.

    Attributes:
        build (str):
            Output only. The resource name of the Cloud Build ``Build``
            object that is used to execute the custom actions associated
            with the predeploy Job. Format is
            ``projects/{project}/locations/{location}/builds/{build}``.
        failure_cause (google.cloud.deploy_v1.types.PredeployJobRun.FailureCause):
            Output only. The reason the predeploy failed.
            This will always be unspecified while the
            predeploy is in progress or if it succeeded.
        failure_message (str):
            Output only. Additional information about the
            predeploy failure, if available.
    """

    class FailureCause(proto.Enum):
        r"""Well-known predeploy failures.

        Values:
            FAILURE_CAUSE_UNSPECIFIED (0):
                No reason for failure is specified.
            CLOUD_BUILD_UNAVAILABLE (1):
                Cloud Build is not available, either because it is not
                enabled or because Cloud Deploy has insufficient
                permissions. See `required
                permission <https://cloud.google.com/deploy/docs/cloud-deploy-service-account#required_permissions>`__.
            EXECUTION_FAILED (2):
                The predeploy operation did not complete
                successfully; check Cloud Build logs.
            DEADLINE_EXCEEDED (3):
                The predeploy job run did not complete within
                the allotted time.
            CLOUD_BUILD_REQUEST_FAILED (4):
                Cloud Build failed to fulfill Cloud Deploy's request. See
                failure_message for additional details.
        """

        FAILURE_CAUSE_UNSPECIFIED = 0
        CLOUD_BUILD_UNAVAILABLE = 1
        EXECUTION_FAILED = 2
        DEADLINE_EXCEEDED = 3
        CLOUD_BUILD_REQUEST_FAILED = 4

    build: str = proto.Field(
        proto.STRING,
        number=1,
    )
    failure_cause: FailureCause = proto.Field(
        proto.ENUM,
        number=2,
        enum=FailureCause,
    )
    failure_message: str = proto.Field(
        proto.STRING,
        number=3,
    )


class PostdeployJobRun(proto.Message):
    r"""PostdeployJobRun contains information specific to a postdeploy
    ``JobRun``.

    Attributes:
        build (str):
            Output only. The resource name of the Cloud Build ``Build``
            object that is used to execute the custom actions associated
            with the postdeploy Job. Format is
            ``projects/{project}/locations/{location}/builds/{build}``.
        failure_cause (google.cloud.deploy_v1.types.PostdeployJobRun.FailureCause):
            Output only. The reason the postdeploy
            failed. This will always be unspecified while
            the postdeploy is in progress or if it
            succeeded.
        failure_message (str):
            Output only. Additional information about the
            postdeploy failure, if available.
    """

    class FailureCause(proto.Enum):
        r"""Well-known postdeploy failures.

        Values:
            FAILURE_CAUSE_UNSPECIFIED (0):
                No reason for failure is specified.
            CLOUD_BUILD_UNAVAILABLE (1):
                Cloud Build is not available, either because it is not
                enabled or because Cloud Deploy has insufficient
                permissions. See `required
                permission <https://cloud.google.com/deploy/docs/cloud-deploy-service-account#required_permissions>`__.
            EXECUTION_FAILED (2):
                The postdeploy operation did not complete
                successfully; check Cloud Build logs.
            DEADLINE_EXCEEDED (3):
                The postdeploy job run did not complete
                within the allotted time.
            CLOUD_BUILD_REQUEST_FAILED (4):
                Cloud Build failed to fulfill Cloud Deploy's request. See
                failure_message for additional details.
        """

        FAILURE_CAUSE_UNSPECIFIED = 0
        CLOUD_BUILD_UNAVAILABLE = 1
        EXECUTION_FAILED = 2
        DEADLINE_EXCEEDED = 3
        CLOUD_BUILD_REQUEST_FAILED = 4

    build: str = proto.Field(
        proto.STRING,
        number=1,
    )
    failure_cause: FailureCause = proto.Field(
        proto.ENUM,
        number=2,
        enum=FailureCause,
    )
    failure_message: str = proto.Field(
        proto.STRING,
        number=3,
    )


class CreateChildRolloutJobRun(proto.Message):
    r"""CreateChildRolloutJobRun contains information specific to a
    createChildRollout ``JobRun``.

    Attributes:
        rollout (str):
            Output only. Name of the ``ChildRollout``. Format is
            ``projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{release}/rollouts/{rollout}``.
        rollout_phase_id (str):
            Output only. The ID of the childRollout Phase
            initiated by this JobRun.
    """

    rollout: str = proto.Field(
        proto.STRING,
        number=1,
    )
    rollout_phase_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AdvanceChildRolloutJobRun(proto.Message):
    r"""AdvanceChildRolloutJobRun contains information specific to a
    advanceChildRollout ``JobRun``.

    Attributes:
        rollout (str):
            Output only. Name of the ``ChildRollout``. Format is
            ``projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{release}/rollouts/{rollout}``.
        rollout_phase_id (str):
            Output only. the ID of the ChildRollout's
            Phase.
    """

    rollout: str = proto.Field(
        proto.STRING,
        number=1,
    )
    rollout_phase_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListJobRunsRequest(proto.Message):
    r"""ListJobRunsRequest is the request object used by ``ListJobRuns``.

    Attributes:
        parent (str):
            Required. The ``Rollout`` which owns this collection of
            ``JobRun`` objects.
        page_size (int):
            Optional. The maximum number of ``JobRun`` objects to
            return. The service may return fewer than this value. If
            unspecified, at most 50 ``JobRun`` objects will be returned.
            The maximum value is 1000; values above 1000 will be set to
            1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListJobRuns`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other provided parameters match the
            call that provided the page token.
        filter (str):
            Optional. Filter results to be returned. See
            https://google.aip.dev/160 for more details.
        order_by (str):
            Optional. Field to sort by. See
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


class ListJobRunsResponse(proto.Message):
    r"""ListJobRunsResponse is the response object returned by
    ``ListJobRuns``.

    Attributes:
        job_runs (MutableSequence[google.cloud.deploy_v1.types.JobRun]):
            The ``JobRun`` objects.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached
    """

    @property
    def raw_page(self):
        return self

    job_runs: MutableSequence["JobRun"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="JobRun",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetJobRunRequest(proto.Message):
    r"""GetJobRunRequest is the request object used by ``GetJobRun``.

    Attributes:
        name (str):
            Required. Name of the ``JobRun``. Format must be
            ``projects/{project_id}/locations/{location_name}/deliveryPipelines/{pipeline_name}/releases/{release_name}/rollouts/{rollout_name}/jobRuns/{job_run_name}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class TerminateJobRunRequest(proto.Message):
    r"""The request object used by ``TerminateJobRun``.

    Attributes:
        name (str):
            Required. Name of the ``JobRun``. Format must be
            ``projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{release}/rollouts/{rollout}/jobRuns/{jobRun}``.
        override_deploy_policy (MutableSequence[str]):
            Optional. Deploy policies to override. Format is
            ``projects/{project}/locations/{location}/deployPolicies/{deployPolicy}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    override_deploy_policy: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class TerminateJobRunResponse(proto.Message):
    r"""The response object from ``TerminateJobRun``."""


class Config(proto.Message):
    r"""Service-wide configuration.

    Attributes:
        name (str):
            Name of the configuration.
        supported_versions (MutableSequence[google.cloud.deploy_v1.types.SkaffoldVersion]):
            All supported versions of Skaffold.
        default_skaffold_version (str):
            Default Skaffold version that is assigned
            when a Release is created without specifying a
            Skaffold version.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    supported_versions: MutableSequence["SkaffoldVersion"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="SkaffoldVersion",
    )
    default_skaffold_version: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SkaffoldVersion(proto.Message):
    r"""Details of a supported Skaffold version.

    Attributes:
        version (str):
            Release version number. For example,
            "1.20.3".
        maintenance_mode_time (google.protobuf.timestamp_pb2.Timestamp):
            The time at which this version of Skaffold
            will enter maintenance mode.
        support_expiration_time (google.protobuf.timestamp_pb2.Timestamp):
            The time at which this version of Skaffold
            will no longer be supported.
        support_end_date (google.type.date_pb2.Date):
            Date when this version is expected to no
            longer be supported.
    """

    version: str = proto.Field(
        proto.STRING,
        number=1,
    )
    maintenance_mode_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    support_expiration_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    support_end_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=2,
        message=date_pb2.Date,
    )


class GetConfigRequest(proto.Message):
    r"""Request to get a configuration.

    Attributes:
        name (str):
            Required. Name of requested configuration.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Automation(proto.Message):
    r"""An ``Automation`` resource in the Cloud Deploy API.

    An ``Automation`` enables the automation of manually driven actions
    for a Delivery Pipeline, which includes Release promotion among
    Targets, Rollout repair and Rollout deployment strategy advancement.
    The intention of Automation is to reduce manual intervention in the
    continuous delivery process.

    Attributes:
        name (str):
            Output only. Name of the ``Automation``. Format is
            ``projects/{project}/locations/{location}/deliveryPipelines/{delivery_pipeline}/automations/{automation}``.
        uid (str):
            Output only. Unique identifier of the ``Automation``.
        description (str):
            Optional. Description of the ``Automation``. Max length is
            255 characters.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time at which the automation was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time at which the automation was
            updated.
        annotations (MutableMapping[str, str]):
            Optional. User annotations. These attributes can only be set
            and used by the user, and not by Cloud Deploy. Annotations
            must meet the following constraints:

            - Annotations are key/value pairs.
            - Valid annotation keys have two segments: an optional
              prefix and name, separated by a slash (``/``).
            - The name segment is required and must be 63 characters or
              less, beginning and ending with an alphanumeric character
              (``[a-z0-9A-Z]``) with dashes (``-``), underscores
              (``_``), dots (``.``), and alphanumerics between.
            - The prefix is optional. If specified, the prefix must be a
              DNS subdomain: a series of DNS labels separated by
              dots(``.``), not longer than 253 characters in total,
              followed by a slash (``/``).

            See
            https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/#syntax-and-character-set
            for more details.
        labels (MutableMapping[str, str]):
            Optional. Labels are attributes that can be set and used by
            both the user and by Cloud Deploy. Labels must meet the
            following constraints:

            - Keys and values can contain only lowercase letters,
              numeric characters, underscores, and dashes.
            - All characters must use UTF-8 encoding, and international
              characters are allowed.
            - Keys must start with a lowercase letter or international
              character.
            - Each resource is limited to a maximum of 64 labels.

            Both keys and values are additionally constrained to be <=
            63 characters.
        etag (str):
            Optional. The weak etag of the ``Automation`` resource. This
            checksum is computed by the server based on the value of
            other fields, and may be sent on update and delete requests
            to ensure the client has an up-to-date value before
            proceeding.
        suspended (bool):
            Optional. When Suspended, automation is
            deactivated from execution.
        service_account (str):
            Required. Email address of the user-managed
            IAM service account that creates Cloud Deploy
            release and rollout resources.
        selector (google.cloud.deploy_v1.types.AutomationResourceSelector):
            Required. Selected resources to which the
            automation will be applied.
        rules (MutableSequence[google.cloud.deploy_v1.types.AutomationRule]):
            Required. List of Automation rules associated
            with the Automation resource. Must have at least
            one rule and limited to 250 rules per Delivery
            Pipeline. Note: the order of the rules here is
            not the same as the order of execution.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
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
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=8,
    )
    suspended: bool = proto.Field(
        proto.BOOL,
        number=9,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=10,
    )
    selector: "AutomationResourceSelector" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="AutomationResourceSelector",
    )
    rules: MutableSequence["AutomationRule"] = proto.RepeatedField(
        proto.MESSAGE,
        number=14,
        message="AutomationRule",
    )


class AutomationResourceSelector(proto.Message):
    r"""AutomationResourceSelector contains the information to select
    the resources to which an Automation is going to be applied.

    Attributes:
        targets (MutableSequence[google.cloud.deploy_v1.types.TargetAttribute]):
            Optional. Contains attributes about a target.
    """

    targets: MutableSequence["TargetAttribute"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="TargetAttribute",
    )


class AutomationRule(proto.Message):
    r"""``AutomationRule`` defines the automation activities.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        promote_release_rule (google.cloud.deploy_v1.types.PromoteReleaseRule):
            Optional. ``PromoteReleaseRule`` will automatically promote
            a release from the current target to a specified target.

            This field is a member of `oneof`_ ``rule``.
        advance_rollout_rule (google.cloud.deploy_v1.types.AdvanceRolloutRule):
            Optional. The ``AdvanceRolloutRule`` will automatically
            advance a successful Rollout.

            This field is a member of `oneof`_ ``rule``.
        repair_rollout_rule (google.cloud.deploy_v1.types.RepairRolloutRule):
            Optional. The ``RepairRolloutRule`` will automatically
            repair a failed rollout.

            This field is a member of `oneof`_ ``rule``.
        timed_promote_release_rule (google.cloud.deploy_v1.types.TimedPromoteReleaseRule):
            Optional. The ``TimedPromoteReleaseRule`` will automatically
            promote a release from the current target(s) to the
            specified target(s) on a configured schedule.

            This field is a member of `oneof`_ ``rule``.
    """

    promote_release_rule: "PromoteReleaseRule" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="rule",
        message="PromoteReleaseRule",
    )
    advance_rollout_rule: "AdvanceRolloutRule" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="rule",
        message="AdvanceRolloutRule",
    )
    repair_rollout_rule: "RepairRolloutRule" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="rule",
        message="RepairRolloutRule",
    )
    timed_promote_release_rule: "TimedPromoteReleaseRule" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="rule",
        message="TimedPromoteReleaseRule",
    )


class TimedPromoteReleaseRule(proto.Message):
    r"""The ``TimedPromoteReleaseRule`` will automatically promote a release
    from the current target(s) to the specified target(s) on a
    configured schedule.

    Attributes:
        id (str):
            Required. ID of the rule. This ID must be unique in the
            ``Automation`` resource to which this rule belongs. The
            format is ``[a-z]([a-z0-9-]{0,61}[a-z0-9])?``.
        destination_target_id (str):
            Optional. The ID of the stage in the pipeline to which this
            ``Release`` is deploying. If unspecified, default it to the
            next stage in the promotion flow. The value of this field
            could be one of the following:

            - The last segment of a target name
            - "@next", the next target in the promotion sequence
        schedule (str):
            Required. Schedule in crontab format. e.g. "0 9 \* \* 1" for
            every Monday at 9am.
        time_zone (str):
            Required. The time zone in IANA format `IANA Time Zone
            Database <https://www.iana.org/time-zones>`__ (e.g.
            America/New_York).
        condition (google.cloud.deploy_v1.types.AutomationRuleCondition):
            Output only. Information around the state of
            the Automation rule.
        destination_phase (str):
            Optional. The starting phase of the rollout
            created by this rule. Default to the first
            phase.
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    destination_target_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    schedule: str = proto.Field(
        proto.STRING,
        number=3,
    )
    time_zone: str = proto.Field(
        proto.STRING,
        number=4,
    )
    condition: "AutomationRuleCondition" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="AutomationRuleCondition",
    )
    destination_phase: str = proto.Field(
        proto.STRING,
        number=6,
    )


class PromoteReleaseRule(proto.Message):
    r"""The ``PromoteRelease`` rule will automatically promote a release
    from the current target to a specified target.

    Attributes:
        id (str):
            Required. ID of the rule. This id must be unique in the
            ``Automation`` resource to which this rule belongs. The
            format is ``[a-z]([a-z0-9-]{0,61}[a-z0-9])?``.
        wait (google.protobuf.duration_pb2.Duration):
            Optional. How long the release need to be
            paused until being promoted to the next target.
        destination_target_id (str):
            Optional. The ID of the stage in the pipeline to which this
            ``Release`` is deploying. If unspecified, default it to the
            next stage in the promotion flow. The value of this field
            could be one of the following:

            - The last segment of a target name
            - "@next", the next target in the promotion sequence
        condition (google.cloud.deploy_v1.types.AutomationRuleCondition):
            Output only. Information around the state of
            the Automation rule.
        destination_phase (str):
            Optional. The starting phase of the rollout
            created by this operation. Default to the first
            phase.
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    wait: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )
    destination_target_id: str = proto.Field(
        proto.STRING,
        number=7,
    )
    condition: "AutomationRuleCondition" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="AutomationRuleCondition",
    )
    destination_phase: str = proto.Field(
        proto.STRING,
        number=8,
    )


class AdvanceRolloutRule(proto.Message):
    r"""The ``AdvanceRollout`` automation rule will automatically advance a
    successful Rollout to the next phase.

    Attributes:
        id (str):
            Required. ID of the rule. This id must be unique in the
            ``Automation`` resource to which this rule belongs. The
            format is ``[a-z]([a-z0-9-]{0,61}[a-z0-9])?``.
        source_phases (MutableSequence[str]):
            Optional. Proceeds only after phase name matched any one in
            the list. This value must consist of lower-case letters,
            numbers, and hyphens, start with a letter and end with a
            letter or a number, and have a max length of 63 characters.
            In other words, it must match the following regex:
            ``^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$``.
        wait (google.protobuf.duration_pb2.Duration):
            Optional. How long to wait after a rollout is
            finished.
        condition (google.cloud.deploy_v1.types.AutomationRuleCondition):
            Output only. Information around the state of
            the Automation rule.
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    source_phases: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    wait: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=3,
        message=duration_pb2.Duration,
    )
    condition: "AutomationRuleCondition" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="AutomationRuleCondition",
    )


class RepairRolloutRule(proto.Message):
    r"""The ``RepairRolloutRule`` automation rule will automatically repair
    a failed ``Rollout``.

    Attributes:
        id (str):
            Required. ID of the rule. This id must be unique in the
            ``Automation`` resource to which this rule belongs. The
            format is ``[a-z]([a-z0-9-]{0,61}[a-z0-9])?``.
        phases (MutableSequence[str]):
            Optional. Phases within which jobs are subject to automatic
            repair actions on failure. Proceeds only after phase name
            matched any one in the list, or for all phases if
            unspecified. This value must consist of lower-case letters,
            numbers, and hyphens, start with a letter and end with a
            letter or a number, and have a max length of 63 characters.
            In other words, it must match the following regex:
            ``^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$``.
        jobs (MutableSequence[str]):
            Optional. Jobs to repair. Proceeds only after job name
            matched any one in the list, or for all jobs if unspecified
            or empty. The phase that includes the job must match the
            phase ID specified in ``source_phase``. This value must
            consist of lower-case letters, numbers, and hyphens, start
            with a letter and end with a letter or a number, and have a
            max length of 63 characters. In other words, it must match
            the following regex: ``^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$``.
        condition (google.cloud.deploy_v1.types.AutomationRuleCondition):
            Output only. Information around the state of
            the 'Automation' rule.
        repair_phases (MutableSequence[google.cloud.deploy_v1.types.RepairPhaseConfig]):
            Required. Defines the types of automatic
            repair phases for failed jobs.
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    phases: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    jobs: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    condition: "AutomationRuleCondition" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="AutomationRuleCondition",
    )
    repair_phases: MutableSequence["RepairPhaseConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message="RepairPhaseConfig",
    )


class RepairPhaseConfig(proto.Message):
    r"""Configuration of the repair phase.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        retry (google.cloud.deploy_v1.types.Retry):
            Optional. Retries a failed job.

            This field is a member of `oneof`_ ``repair_phase``.
        rollback (google.cloud.deploy_v1.types.Rollback):
            Optional. Rolls back a ``Rollout``.

            This field is a member of `oneof`_ ``repair_phase``.
    """

    retry: "Retry" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="repair_phase",
        message="Retry",
    )
    rollback: "Rollback" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="repair_phase",
        message="Rollback",
    )


class Retry(proto.Message):
    r"""Retries the failed job.

    Attributes:
        attempts (int):
            Required. Total number of retries. Retry is
            skipped if set to 0; The minimum value is 1, and
            the maximum value is 10.
        wait (google.protobuf.duration_pb2.Duration):
            Optional. How long to wait for the first
            retry. Default is 0, and the maximum value is
            14d.
        backoff_mode (google.cloud.deploy_v1.types.BackoffMode):
            Optional. The pattern of how wait time will be increased.
            Default is linear. Backoff mode will be ignored if ``wait``
            is 0.
    """

    attempts: int = proto.Field(
        proto.INT64,
        number=1,
    )
    wait: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )
    backoff_mode: "BackoffMode" = proto.Field(
        proto.ENUM,
        number=3,
        enum="BackoffMode",
    )


class Rollback(proto.Message):
    r"""Rolls back a ``Rollout``.

    Attributes:
        destination_phase (str):
            Optional. The starting phase ID for the ``Rollout``. If
            unspecified, the ``Rollout`` will start in the stable phase.
        disable_rollback_if_rollout_pending (bool):
            Optional. If pending rollout exists on the
            target, the rollback operation will be aborted.
    """

    destination_phase: str = proto.Field(
        proto.STRING,
        number=1,
    )
    disable_rollback_if_rollout_pending: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class AutomationRuleCondition(proto.Message):
    r"""``AutomationRuleCondition`` contains conditions relevant to an
    ``Automation`` rule.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        targets_present_condition (google.cloud.deploy_v1.types.TargetsPresentCondition):
            Optional. Details around targets enumerated
            in the rule.
        timed_promote_release_condition (google.cloud.deploy_v1.types.TimedPromoteReleaseCondition):
            Optional. TimedPromoteReleaseCondition
            contains rule conditions specific to a an
            Automation with a timed promote release rule
            defined.

            This field is a member of `oneof`_ ``rule_type_condition``.
    """

    targets_present_condition: "TargetsPresentCondition" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="TargetsPresentCondition",
    )
    timed_promote_release_condition: "TimedPromoteReleaseCondition" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="rule_type_condition",
        message="TimedPromoteReleaseCondition",
    )


class TimedPromoteReleaseCondition(proto.Message):
    r"""``TimedPromoteReleaseCondition`` contains conditions specific to an
    Automation with a Timed Promote Release rule defined.

    Attributes:
        next_promotion_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. When the next scheduled
            promotion(s) will occur.
        targets_list (MutableSequence[google.cloud.deploy_v1.types.TimedPromoteReleaseCondition.Targets]):
            Output only. A list of targets involved in
            the upcoming timed promotion(s).
    """

    class Targets(proto.Message):
        r"""The targets involved in a single timed promotion.

        Attributes:
            source_target_id (str):
                Optional. The source target ID.
            destination_target_id (str):
                Optional. The destination target ID.
        """

        source_target_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        destination_target_id: str = proto.Field(
            proto.STRING,
            number=2,
        )

    next_promotion_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    targets_list: MutableSequence[Targets] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=Targets,
    )


class CreateAutomationRequest(proto.Message):
    r"""The request object for ``CreateAutomation``.

    Attributes:
        parent (str):
            Required. The parent collection in which the ``Automation``
            must be created. The format is
            ``projects/{project_id}/locations/{location_name}/deliveryPipelines/{pipeline_name}``.
        automation_id (str):
            Required. ID of the ``Automation``.
        automation (google.cloud.deploy_v1.types.Automation):
            Required. The ``Automation`` to create.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server knows to ignore
            the request if it has already been completed.
            The server guarantees that for at least 60
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
        validate_only (bool):
            Optional. If set to true, the request is
            validated and the user is provided with an
            expected result, but no actual change is made.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    automation_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    automation: "Automation" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Automation",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class UpdateAutomationRequest(proto.Message):
    r"""The request object for ``UpdateAutomation``.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten by the update in the ``Automation`` resource.
            The fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it's in the mask. If the user doesn't provide a mask then
            all fields are overwritten.
        automation (google.cloud.deploy_v1.types.Automation):
            Required. The ``Automation`` to update.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server knows to ignore
            the request if it has already been completed.
            The server guarantees that for at least 60
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
        allow_missing (bool):
            Optional. If set to true, updating a ``Automation`` that
            does not exist will result in the creation of a new
            ``Automation``.
        validate_only (bool):
            Optional. If set to true, the request is
            validated and the user is provided with an
            expected result, but no actual change is made.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    automation: "Automation" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Automation",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class DeleteAutomationRequest(proto.Message):
    r"""The request object for ``DeleteAutomation``.

    Attributes:
        name (str):
            Required. The name of the ``Automation`` to delete. The
            format is
            ``projects/{project_id}/locations/{location_name}/deliveryPipelines/{pipeline_name}/automations/{automation_name}``.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server knows to ignore
            the request if it has already been completed.
            The server guarantees that for at least 60
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
        allow_missing (bool):
            Optional. If set to true, then deleting an already deleted
            or non-existing ``Automation`` will succeed.
        validate_only (bool):
            Optional. If set, validate the request and
            verify whether the resource exists, but do not
            actually post it.
        etag (str):
            Optional. The weak etag of the request.
            This checksum is computed by the server based on
            the value of other fields, and may be sent on
            update and delete requests to ensure the client
            has an up-to-date value before proceeding.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
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


class ListAutomationsRequest(proto.Message):
    r"""The request object for ``ListAutomations``.

    Attributes:
        parent (str):
            Required. The parent ``Delivery Pipeline``, which owns this
            collection of automations. Format must be
            ``projects/{project_id}/locations/{location_name}/deliveryPipelines/{pipeline_name}``.
        page_size (int):
            The maximum number of automations to return.
            The service may return fewer than this value. If
            unspecified, at most 50 automations will be
            returned. The maximum value is 1000; values
            above 1000 will be set to 1000.
        page_token (str):
            A page token, received from a previous ``ListAutomations``
            call. Provide this to retrieve the subsequent page.

            When paginating, all other provided parameters match the
            call that provided the page token.
        filter (str):
            Filter automations to be returned. All fields
            can be used in the filter.
        order_by (str):
            Field to sort by.
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


class ListAutomationsResponse(proto.Message):
    r"""The response object from ``ListAutomations``.

    Attributes:
        automations (MutableSequence[google.cloud.deploy_v1.types.Automation]):
            The ``Automation`` objects.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    automations: MutableSequence["Automation"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Automation",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetAutomationRequest(proto.Message):
    r"""The request object for ``GetAutomation``

    Attributes:
        name (str):
            Required. Name of the ``Automation``. Format must be
            ``projects/{project_id}/locations/{location_name}/deliveryPipelines/{pipeline_name}/automations/{automation_name}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AutomationRun(proto.Message):
    r"""An ``AutomationRun`` resource in the Cloud Deploy API.

    An ``AutomationRun`` represents an execution instance of an
    automation rule.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. Name of the ``AutomationRun``. Format is
            ``projects/{project}/locations/{location}/deliveryPipelines/{delivery_pipeline}/automationRuns/{automation_run}``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time at which the ``AutomationRun`` was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time at which the automationRun
            was updated.
        etag (str):
            Output only. The weak etag of the ``AutomationRun``
            resource. This checksum is computed by the server based on
            the value of other fields, and may be sent on update and
            delete requests to ensure the client has an up-to-date value
            before proceeding.
        service_account (str):
            Output only. Email address of the
            user-managed IAM service account that performs
            the operations against Cloud Deploy resources.
        automation_snapshot (google.cloud.deploy_v1.types.Automation):
            Output only. Snapshot of the Automation taken
            at AutomationRun creation time.
        target_id (str):
            Output only. The ID of the source target that initiates the
            ``AutomationRun``. The value of this field is the last
            segment of a target name.
        state (google.cloud.deploy_v1.types.AutomationRun.State):
            Output only. Current state of the ``AutomationRun``.
        state_description (str):
            Output only. Explains the current state of the
            ``AutomationRun``. Present only when an explanation is
            needed.
        policy_violation (google.cloud.deploy_v1.types.PolicyViolation):
            Output only. Contains information about what policies
            prevented the ``AutomationRun`` from proceeding.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time the ``AutomationRun`` expires. An
            ``AutomationRun`` expires after 14 days from its creation
            date.
        rule_id (str):
            Output only. The ID of the automation rule
            that initiated the operation.
        automation_id (str):
            Output only. The ID of the automation that
            initiated the operation.
        promote_release_operation (google.cloud.deploy_v1.types.PromoteReleaseOperation):
            Output only. Promotes a release to a
            specified 'Target'.

            This field is a member of `oneof`_ ``operation``.
        advance_rollout_operation (google.cloud.deploy_v1.types.AdvanceRolloutOperation):
            Output only. Advances a rollout to the next
            phase.

            This field is a member of `oneof`_ ``operation``.
        repair_rollout_operation (google.cloud.deploy_v1.types.RepairRolloutOperation):
            Output only. Repairs a failed 'Rollout'.

            This field is a member of `oneof`_ ``operation``.
        timed_promote_release_operation (google.cloud.deploy_v1.types.TimedPromoteReleaseOperation):
            Output only. Promotes a release to a
            specified 'Target' as defined in a Timed Promote
            Release rule.

            This field is a member of `oneof`_ ``operation``.
        wait_until_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Earliest time the ``AutomationRun`` will
            attempt to resume. Wait-time is configured by ``wait`` in
            automation rule.
    """

    class State(proto.Enum):
        r"""Valid state of an ``AutomationRun``.

        Values:
            STATE_UNSPECIFIED (0):
                The ``AutomationRun`` has an unspecified state.
            SUCCEEDED (1):
                The ``AutomationRun`` has succeeded.
            CANCELLED (2):
                The ``AutomationRun`` was cancelled.
            FAILED (3):
                The ``AutomationRun`` has failed.
            IN_PROGRESS (4):
                The ``AutomationRun`` is in progress.
            PENDING (5):
                The ``AutomationRun`` is pending.
            ABORTED (6):
                The ``AutomationRun`` was aborted.
        """

        STATE_UNSPECIFIED = 0
        SUCCEEDED = 1
        CANCELLED = 2
        FAILED = 3
        IN_PROGRESS = 4
        PENDING = 5
        ABORTED = 6

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
    etag: str = proto.Field(
        proto.STRING,
        number=4,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=5,
    )
    automation_snapshot: "Automation" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="Automation",
    )
    target_id: str = proto.Field(
        proto.STRING,
        number=7,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=8,
        enum=State,
    )
    state_description: str = proto.Field(
        proto.STRING,
        number=9,
    )
    policy_violation: "PolicyViolation" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="PolicyViolation",
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )
    rule_id: str = proto.Field(
        proto.STRING,
        number=12,
    )
    automation_id: str = proto.Field(
        proto.STRING,
        number=15,
    )
    promote_release_operation: "PromoteReleaseOperation" = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="operation",
        message="PromoteReleaseOperation",
    )
    advance_rollout_operation: "AdvanceRolloutOperation" = proto.Field(
        proto.MESSAGE,
        number=14,
        oneof="operation",
        message="AdvanceRolloutOperation",
    )
    repair_rollout_operation: "RepairRolloutOperation" = proto.Field(
        proto.MESSAGE,
        number=17,
        oneof="operation",
        message="RepairRolloutOperation",
    )
    timed_promote_release_operation: "TimedPromoteReleaseOperation" = proto.Field(
        proto.MESSAGE,
        number=19,
        oneof="operation",
        message="TimedPromoteReleaseOperation",
    )
    wait_until_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=16,
        message=timestamp_pb2.Timestamp,
    )


class PromoteReleaseOperation(proto.Message):
    r"""Contains the information of an automated promote-release
    operation.

    Attributes:
        target_id (str):
            Output only. The ID of the target that
            represents the promotion stage to which the
            release will be promoted. The value of this
            field is the last segment of a target name.
        wait (google.protobuf.duration_pb2.Duration):
            Output only. How long the operation will be
            paused.
        rollout (str):
            Output only. The name of the rollout that initiates the
            ``AutomationRun``.
        phase (str):
            Output only. The starting phase of the
            rollout created by this operation.
    """

    target_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    wait: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )
    rollout: str = proto.Field(
        proto.STRING,
        number=3,
    )
    phase: str = proto.Field(
        proto.STRING,
        number=4,
    )


class AdvanceRolloutOperation(proto.Message):
    r"""Contains the information of an automated advance-rollout
    operation.

    Attributes:
        source_phase (str):
            Output only. The phase of a deployment that
            initiated the operation.
        wait (google.protobuf.duration_pb2.Duration):
            Output only. How long the operation will be
            paused.
        rollout (str):
            Output only. The name of the rollout that initiates the
            ``AutomationRun``.
        destination_phase (str):
            Output only. The phase the rollout will be
            advanced to.
    """

    source_phase: str = proto.Field(
        proto.STRING,
        number=5,
    )
    wait: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )
    rollout: str = proto.Field(
        proto.STRING,
        number=3,
    )
    destination_phase: str = proto.Field(
        proto.STRING,
        number=4,
    )


class RepairRolloutOperation(proto.Message):
    r"""Contains the information for an automated ``repair rollout``
    operation.

    Attributes:
        rollout (str):
            Output only. The name of the rollout that initiates the
            ``AutomationRun``.
        current_repair_phase_index (int):
            Output only. The index of the current repair
            action in the repair sequence.
        repair_phases (MutableSequence[google.cloud.deploy_v1.types.RepairPhase]):
            Output only. Records of the repair attempts.
            Each repair phase may have multiple retry
            attempts or single rollback attempt.
        phase_id (str):
            Output only. The phase ID of the phase that
            includes the job being repaired.
        job_id (str):
            Output only. The job ID for the Job to
            repair.
    """

    rollout: str = proto.Field(
        proto.STRING,
        number=1,
    )
    current_repair_phase_index: int = proto.Field(
        proto.INT64,
        number=6,
    )
    repair_phases: MutableSequence["RepairPhase"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="RepairPhase",
    )
    phase_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    job_id: str = proto.Field(
        proto.STRING,
        number=5,
    )


class TimedPromoteReleaseOperation(proto.Message):
    r"""Contains the information of an automated timed
    promote-release operation.

    Attributes:
        target_id (str):
            Output only. The ID of the target that
            represents the promotion stage to which the
            release will be promoted. The value of this
            field is the last segment of a target name.
        release (str):
            Output only. The name of the release to be
            promoted.
        phase (str):
            Output only. The starting phase of the
            rollout created by this operation.
    """

    target_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    release: str = proto.Field(
        proto.STRING,
        number=2,
    )
    phase: str = proto.Field(
        proto.STRING,
        number=3,
    )


class RepairPhase(proto.Message):
    r"""RepairPhase tracks the repair attempts that have been made for each
    ``RepairPhaseConfig`` specified in the ``Automation`` resource.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        retry (google.cloud.deploy_v1.types.RetryPhase):
            Output only. Records of the retry attempts
            for retry repair mode.

            This field is a member of `oneof`_ ``repair_phase``.
        rollback (google.cloud.deploy_v1.types.RollbackAttempt):
            Output only. Rollback attempt for rollback
            repair mode .

            This field is a member of `oneof`_ ``repair_phase``.
    """

    retry: "RetryPhase" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="repair_phase",
        message="RetryPhase",
    )
    rollback: "RollbackAttempt" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="repair_phase",
        message="RollbackAttempt",
    )


class RetryPhase(proto.Message):
    r"""RetryPhase contains the retry attempts and the metadata for
    initiating a new attempt.

    Attributes:
        total_attempts (int):
            Output only. The number of attempts that have
            been made.
        backoff_mode (google.cloud.deploy_v1.types.BackoffMode):
            Output only. The pattern of how the wait time
            of the retry attempt is calculated.
        attempts (MutableSequence[google.cloud.deploy_v1.types.RetryAttempt]):
            Output only. Detail of a retry action.
    """

    total_attempts: int = proto.Field(
        proto.INT64,
        number=1,
    )
    backoff_mode: "BackoffMode" = proto.Field(
        proto.ENUM,
        number=2,
        enum="BackoffMode",
    )
    attempts: MutableSequence["RetryAttempt"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="RetryAttempt",
    )


class RetryAttempt(proto.Message):
    r"""RetryAttempt represents an action of retrying the failed
    Cloud Deploy job.

    Attributes:
        attempt (int):
            Output only. The index of this retry attempt.
        wait (google.protobuf.duration_pb2.Duration):
            Output only. How long the operation will be
            paused.
        state (google.cloud.deploy_v1.types.RepairState):
            Output only. Valid state of this retry
            action.
        state_desc (str):
            Output only. Description of the state of the
            Retry.
    """

    attempt: int = proto.Field(
        proto.INT64,
        number=1,
    )
    wait: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )
    state: "RepairState" = proto.Field(
        proto.ENUM,
        number=5,
        enum="RepairState",
    )
    state_desc: str = proto.Field(
        proto.STRING,
        number=6,
    )


class RollbackAttempt(proto.Message):
    r"""RollbackAttempt represents an action of rolling back a Cloud
    Deploy 'Target'.

    Attributes:
        destination_phase (str):
            Output only. The phase to which the rollout
            will be rolled back to.
        rollout_id (str):
            Output only. ID of the rollback ``Rollout`` to create.
        state (google.cloud.deploy_v1.types.RepairState):
            Output only. Valid state of this rollback
            action.
        state_desc (str):
            Output only. Description of the state of the
            Rollback.
        disable_rollback_if_rollout_pending (bool):
            Output only. If active rollout exists on the
            target, abort this rollback.
    """

    destination_phase: str = proto.Field(
        proto.STRING,
        number=1,
    )
    rollout_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    state: "RepairState" = proto.Field(
        proto.ENUM,
        number=3,
        enum="RepairState",
    )
    state_desc: str = proto.Field(
        proto.STRING,
        number=4,
    )
    disable_rollback_if_rollout_pending: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class ListAutomationRunsRequest(proto.Message):
    r"""The request object for ``ListAutomationRuns``.

    Attributes:
        parent (str):
            Required. The parent ``Delivery Pipeline``, which owns this
            collection of automationRuns. Format must be
            ``projects/{project}/locations/{location}/deliveryPipelines/{delivery_pipeline}``.
        page_size (int):
            The maximum number of automationRuns to
            return. The service may return fewer than this
            value. If unspecified, at most 50 automationRuns
            will be returned. The maximum value is 1000;
            values above 1000 will be set to 1000.
        page_token (str):
            A page token, received from a previous
            ``ListAutomationRuns`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other provided parameters match the
            call that provided the page token.
        filter (str):
            Filter automationRuns to be returned. All
            fields can be used in the filter.
        order_by (str):
            Field to sort by.
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


class ListAutomationRunsResponse(proto.Message):
    r"""The response object from ``ListAutomationRuns``.

    Attributes:
        automation_runs (MutableSequence[google.cloud.deploy_v1.types.AutomationRun]):
            The ``AutomationRuns`` objects.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    automation_runs: MutableSequence["AutomationRun"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AutomationRun",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetAutomationRunRequest(proto.Message):
    r"""The request object for ``GetAutomationRun``

    Attributes:
        name (str):
            Required. Name of the ``AutomationRun``. Format must be
            ``projects/{project}/locations/{location}/deliveryPipelines/{delivery_pipeline}/automationRuns/{automation_run}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CancelAutomationRunRequest(proto.Message):
    r"""The request object used by ``CancelAutomationRun``.

    Attributes:
        name (str):
            Required. Name of the ``AutomationRun``. Format is
            ``projects/{project}/locations/{location}/deliveryPipelines/{delivery_pipeline}/automationRuns/{automation_run}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CancelAutomationRunResponse(proto.Message):
    r"""The response object from ``CancelAutomationRun``."""


__all__ = tuple(sorted(__protobuf__.manifest))
