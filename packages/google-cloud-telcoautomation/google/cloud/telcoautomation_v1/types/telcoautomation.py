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
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.telcoautomation.v1",
    manifest={
        "BlueprintView",
        "DeploymentView",
        "ResourceType",
        "Status",
        "DeploymentLevel",
        "OrchestrationCluster",
        "EdgeSlm",
        "Blueprint",
        "PublicBlueprint",
        "Deployment",
        "HydratedDeployment",
        "ListOrchestrationClustersRequest",
        "ListOrchestrationClustersResponse",
        "GetOrchestrationClusterRequest",
        "CreateOrchestrationClusterRequest",
        "DeleteOrchestrationClusterRequest",
        "ListEdgeSlmsRequest",
        "ListEdgeSlmsResponse",
        "GetEdgeSlmRequest",
        "CreateEdgeSlmRequest",
        "DeleteEdgeSlmRequest",
        "CreateBlueprintRequest",
        "UpdateBlueprintRequest",
        "GetBlueprintRequest",
        "DeleteBlueprintRequest",
        "ListBlueprintsRequest",
        "ListBlueprintsResponse",
        "ApproveBlueprintRequest",
        "ProposeBlueprintRequest",
        "RejectBlueprintRequest",
        "ListBlueprintRevisionsRequest",
        "ListBlueprintRevisionsResponse",
        "SearchBlueprintRevisionsRequest",
        "SearchBlueprintRevisionsResponse",
        "DiscardBlueprintChangesRequest",
        "DiscardBlueprintChangesResponse",
        "ListPublicBlueprintsRequest",
        "ListPublicBlueprintsResponse",
        "GetPublicBlueprintRequest",
        "CreateDeploymentRequest",
        "UpdateDeploymentRequest",
        "GetDeploymentRequest",
        "RemoveDeploymentRequest",
        "ListDeploymentsRequest",
        "ListDeploymentsResponse",
        "ListDeploymentRevisionsRequest",
        "ListDeploymentRevisionsResponse",
        "SearchDeploymentRevisionsRequest",
        "SearchDeploymentRevisionsResponse",
        "DiscardDeploymentChangesRequest",
        "DiscardDeploymentChangesResponse",
        "ApplyDeploymentRequest",
        "ComputeDeploymentStatusRequest",
        "ComputeDeploymentStatusResponse",
        "RollbackDeploymentRequest",
        "OperationMetadata",
        "GetHydratedDeploymentRequest",
        "ListHydratedDeploymentsRequest",
        "ListHydratedDeploymentsResponse",
        "UpdateHydratedDeploymentRequest",
        "ApplyHydratedDeploymentRequest",
        "ManagementConfig",
        "StandardManagementConfig",
        "FullManagementConfig",
        "MasterAuthorizedNetworksConfig",
        "File",
        "ResourceStatus",
        "NFDeployStatus",
        "NFDeploySiteStatus",
        "HydrationStatus",
        "SiteVersion",
        "WorkloadStatus",
    },
)


class BlueprintView(proto.Enum):
    r"""BlueprintView defines the type of view of the blueprint.

    Values:
        BLUEPRINT_VIEW_UNSPECIFIED (0):
            Unspecified enum value.
        BLUEPRINT_VIEW_BASIC (1):
            View which only contains metadata.
        BLUEPRINT_VIEW_FULL (2):
            View which contains metadata and files it
            encapsulates.
    """

    BLUEPRINT_VIEW_UNSPECIFIED = 0
    BLUEPRINT_VIEW_BASIC = 1
    BLUEPRINT_VIEW_FULL = 2


class DeploymentView(proto.Enum):
    r"""DeploymentView defines the type of view of the deployment.

    Values:
        DEPLOYMENT_VIEW_UNSPECIFIED (0):
            Unspecified enum value.
        DEPLOYMENT_VIEW_BASIC (1):
            View which only contains metadata.
        DEPLOYMENT_VIEW_FULL (2):
            View which contains metadata and files it
            encapsulates.
    """

    DEPLOYMENT_VIEW_UNSPECIFIED = 0
    DEPLOYMENT_VIEW_BASIC = 1
    DEPLOYMENT_VIEW_FULL = 2


class ResourceType(proto.Enum):
    r"""Represent type of CR.

    Values:
        RESOURCE_TYPE_UNSPECIFIED (0):
            Unspecified resource type.
        NF_DEPLOY_RESOURCE (1):
            User specified NF Deploy CR.
        DEPLOYMENT_RESOURCE (2):
            CRs that are part of a blueprint.
    """

    RESOURCE_TYPE_UNSPECIFIED = 0
    NF_DEPLOY_RESOURCE = 1
    DEPLOYMENT_RESOURCE = 2


class Status(proto.Enum):
    r"""Status of an entity (resource, deployment).

    Values:
        STATUS_UNSPECIFIED (0):
            Unknown state.
        STATUS_IN_PROGRESS (1):
            Under progress.
        STATUS_ACTIVE (2):
            Running and ready to serve traffic.
        STATUS_FAILED (3):
            Failed or stalled.
        STATUS_DELETING (4):
            Delete in progress.
        STATUS_DELETED (5):
            Deleted deployment.
        STATUS_PEERING (10):
            NFDeploy specific status. Peering in
            progress.
        STATUS_NOT_APPLICABLE (11):
            K8s objects such as
            NetworkAttachmentDefinition don't have a defined
            status.
    """

    STATUS_UNSPECIFIED = 0
    STATUS_IN_PROGRESS = 1
    STATUS_ACTIVE = 2
    STATUS_FAILED = 3
    STATUS_DELETING = 4
    STATUS_DELETED = 5
    STATUS_PEERING = 10
    STATUS_NOT_APPLICABLE = 11


class DeploymentLevel(proto.Enum):
    r"""DeploymentLevel of a blueprint signifies where the blueprint
    will be applied.

    Values:
        DEPLOYMENT_LEVEL_UNSPECIFIED (0):
            Default unspecified deployment level.
        HYDRATION (1):
            Blueprints at HYDRATION level cannot be used
            to create a Deployment (A user cannot manually
            initate deployment of these blueprints on
            orchestration or workload cluster).
            These blueprints stay in a user's private
            catalog and are configured and deployed by TNA
            automation.
        SINGLE_DEPLOYMENT (2):
            Blueprints at SINGLE_DEPLOYMENT level can be a) Modified in
            private catalog. b) Used to create a deployment on
            orchestration cluster by the user, once approved.
        MULTI_DEPLOYMENT (3):
            Blueprints at MULTI_DEPLOYMENT level can be a) Modified in
            private catalog. b) Used to create a deployment on
            orchestration cluster which will create further hydrated
            deployments.
        WORKLOAD_CLUSTER_DEPLOYMENT (4):
            Blueprints at WORKLOAD_CLUSTER_DEPLOYMENT level can be a)
            Modified in private catalog. b) Used to create a deployment
            on workload cluster by the user, once approved.
    """

    DEPLOYMENT_LEVEL_UNSPECIFIED = 0
    HYDRATION = 1
    SINGLE_DEPLOYMENT = 2
    MULTI_DEPLOYMENT = 3
    WORKLOAD_CLUSTER_DEPLOYMENT = 4


class OrchestrationCluster(proto.Message):
    r"""Orchestration cluster represents a GKE cluster with config
    controller and TNA specific components installed on it.

    Attributes:
        name (str):
            Name of the orchestration cluster. The name
            of orchestration cluster cannot be more than 24
            characters.
        management_config (google.cloud.telcoautomation_v1.types.ManagementConfig):
            Management configuration of the underlying
            GKE cluster.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Create time stamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Update time stamp.
        labels (MutableMapping[str, str]):
            Labels as key value pairs.
        tna_version (str):
            Output only. Provides the TNA version
            installed on the cluster.
        state (google.cloud.telcoautomation_v1.types.OrchestrationCluster.State):
            Output only. State of the Orchestration
            Cluster.
    """

    class State(proto.Enum):
        r"""Possible states that the Orchestration Cluster can be in.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified state.
            CREATING (1):
                OrchestrationCluster is being created.
            ACTIVE (2):
                OrchestrationCluster has been created and is
                ready for use.
            DELETING (3):
                OrchestrationCluster is being deleted.
            FAILED (4):
                OrchestrationCluster encountered an error and
                is in an indeterministic state. User can still
                initiate a delete operation on this state.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        DELETING = 3
        FAILED = 4

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    management_config: "ManagementConfig" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="ManagementConfig",
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
    tna_version: str = proto.Field(
        proto.STRING,
        number=6,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=7,
        enum=State,
    )


class EdgeSlm(proto.Message):
    r"""EdgeSlm represents an SLM instance which manages the
    lifecycle of edge components installed on Workload clusters
    managed by an Orchestration Cluster.

    Attributes:
        name (str):
            Name of the EdgeSlm resource.
        orchestration_cluster (str):
            Immutable. Reference to the orchestration cluster on which
            templates for this resources will be applied. This should be
            of format
            projects/{project}/locations/{location}/orchestrationClusters/{orchestration_cluster}.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Create time stamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Update time stamp.
        labels (MutableMapping[str, str]):
            Optional. Labels as key value pairs. The key
            and value should contain characters which are
            UTF-8 compliant and less than 50 characters.
        tna_version (str):
            Output only. Provides the active TNA version
            for this resource.
        state (google.cloud.telcoautomation_v1.types.EdgeSlm.State):
            Output only. State of the EdgeSlm resource.
        workload_cluster_type (google.cloud.telcoautomation_v1.types.EdgeSlm.WorkloadClusterType):
            Optional. Type of workload cluster for which
            an EdgeSLM resource is created.
    """

    class State(proto.Enum):
        r"""Possible states of the resource.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified state.
            CREATING (1):
                EdgeSlm is being created.
            ACTIVE (2):
                EdgeSlm has been created and is ready for
                use.
            DELETING (3):
                EdgeSlm is being deleted.
            FAILED (4):
                EdgeSlm encountered an error and is in an
                indeterministic state. User can still initiate a
                delete operation on this state.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        DELETING = 3
        FAILED = 4

    class WorkloadClusterType(proto.Enum):
        r"""Workload clusters supported by TNA. New values will be added
        to the enum list as TNA adds supports for new workload clusters
        in future.

        Values:
            WORKLOAD_CLUSTER_TYPE_UNSPECIFIED (0):
                Unspecified workload cluster.
            GDCE (1):
                Workload cluster is a GDCE cluster.
            GKE (2):
                Workload cluster is a GKE cluster.
        """

        WORKLOAD_CLUSTER_TYPE_UNSPECIFIED = 0
        GDCE = 1
        GKE = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    orchestration_cluster: str = proto.Field(
        proto.STRING,
        number=5,
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
    tna_version: str = proto.Field(
        proto.STRING,
        number=6,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=7,
        enum=State,
    )
    workload_cluster_type: WorkloadClusterType = proto.Field(
        proto.ENUM,
        number=8,
        enum=WorkloadClusterType,
    )


class Blueprint(proto.Message):
    r"""A Blueprint contains a collection of kubernetes resources in
    the form of YAML files. The file contents of a blueprint are
    collectively known as package. A blueprint can be
    a) imported from TNA's public catalog
    b) modified as per a user's need
    c) proposed and approved.
    On approval, a revision of blueprint is created which can be
    used to create a deployment on Orchestration or Workload
    Cluster.

    Attributes:
        name (str):
            The name of the blueprint. If unspecified, the name will be
            autogenerated from server side. Name of the blueprint must
            not contain ``@`` character.
        revision_id (str):
            Output only. Immutable. The revision ID of
            the blueprint. A new revision is committed
            whenever a blueprint is approved.
        source_blueprint (str):
            Required. Immutable. The public blueprint ID
            from which this blueprint was created.
        revision_create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp that the revision
            was created.
        approval_state (google.cloud.telcoautomation_v1.types.Blueprint.ApprovalState):
            Output only. Approval state of the blueprint
            (DRAFT, PROPOSED, APPROVED)
        display_name (str):
            Optional. Human readable name of a Blueprint.
        repository (str):
            Output only. Name of the repository where the
            blueprint files are stored.
        files (MutableSequence[google.cloud.telcoautomation_v1.types.File]):
            Optional. Files present in a blueprint.
            When invoking UpdateBlueprint API, only the
            modified files should be included in this. Files
            that are not included in the update of a
            blueprint will not be changed.
        labels (MutableMapping[str, str]):
            Optional. Labels are key-value attributes
            that can be set on a blueprint resource by the
            user.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Blueprint creation time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the blueprint
            was updated.
        source_provider (str):
            Output only. Source provider is the author of
            a public blueprint, from which this blueprint is
            created.
        deployment_level (google.cloud.telcoautomation_v1.types.DeploymentLevel):
            Output only. DeploymentLevel of a blueprint signifies where
            the blueprint will be applied. e.g. [HYDRATION,
            SINGLE_DEPLOYMENT, MULTI_DEPLOYMENT]
        rollback_support (bool):
            Output only. Indicates if the deployment
            created from this blueprint can be rolled back.
    """

    class ApprovalState(proto.Enum):
        r"""Approval state indicates the state of a Blueprint in its
        approval lifecycle.

        Values:
            APPROVAL_STATE_UNSPECIFIED (0):
                Unspecified state.
            DRAFT (1):
                A blueprint starts in DRAFT state once it is
                created. All edits are made to the blueprint in
                DRAFT state.
            PROPOSED (2):
                When the edits are ready for review,
                blueprint can be proposed and moves to PROPOSED
                state. Edits cannot be made to a blueprint in
                PROPOSED state.
            APPROVED (3):
                When a proposed blueprint is approved, it
                moves to APPROVED state. A new revision is
                committed. The latest committed revision can be
                used to create a deployment on Orchestration or
                Workload Cluster. Edits to an APPROVED blueprint
                changes its state back to DRAFT. The last
                committed revision of a blueprint represents its
                latest APPROVED state.
        """

        APPROVAL_STATE_UNSPECIFIED = 0
        DRAFT = 1
        PROPOSED = 2
        APPROVED = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    revision_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    source_blueprint: str = proto.Field(
        proto.STRING,
        number=3,
    )
    revision_create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    approval_state: ApprovalState = proto.Field(
        proto.ENUM,
        number=6,
        enum=ApprovalState,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=7,
    )
    repository: str = proto.Field(
        proto.STRING,
        number=8,
    )
    files: MutableSequence["File"] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="File",
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=10,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=12,
        message=timestamp_pb2.Timestamp,
    )
    source_provider: str = proto.Field(
        proto.STRING,
        number=13,
    )
    deployment_level: "DeploymentLevel" = proto.Field(
        proto.ENUM,
        number=14,
        enum="DeploymentLevel",
    )
    rollback_support: bool = proto.Field(
        proto.BOOL,
        number=15,
    )


class PublicBlueprint(proto.Message):
    r"""A Blueprint contains a collection of kubernetes resources in
    the form of YAML files. The file contents of a blueprint are
    collectively known as package.
    Public blueprint is a TNA provided blueprint that in present in
    TNA's public catalog. A user can copy the public blueprint to
    their private catalog for further modifications.

    Attributes:
        name (str):
            Name of the public blueprint.
        display_name (str):
            The display name of the public blueprint.
        description (str):
            The description of the public blueprint.
        deployment_level (google.cloud.telcoautomation_v1.types.DeploymentLevel):
            DeploymentLevel of a blueprint signifies where the blueprint
            will be applied. e.g. [HYDRATION, SINGLE_DEPLOYMENT,
            MULTI_DEPLOYMENT]
        source_provider (str):
            Source provider is the author of a public
            blueprint. e.g. Google, vendors
        rollback_support (bool):
            Output only. Indicates if the deployment
            created from this blueprint can be rolled back.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    deployment_level: "DeploymentLevel" = proto.Field(
        proto.ENUM,
        number=4,
        enum="DeploymentLevel",
    )
    source_provider: str = proto.Field(
        proto.STRING,
        number=5,
    )
    rollback_support: bool = proto.Field(
        proto.BOOL,
        number=15,
    )


class Deployment(proto.Message):
    r"""Deployment contains a collection of YAML files (This
    collection is also known as package) that can to applied on an
    orchestration cluster (GKE cluster with TNA addons) or a
    workload cluster.

    Attributes:
        name (str):
            The name of the deployment.
        revision_id (str):
            Output only. Immutable. The revision ID of
            the deployment. A new revision is committed
            whenever a change in deployment is applied.
        source_blueprint_revision (str):
            Required. The blueprint revision from which
            this deployment was created.
        revision_create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp that the revision
            was created.
        state (google.cloud.telcoautomation_v1.types.Deployment.State):
            Output only. State of the deployment (DRAFT,
            APPLIED, DELETING).
        display_name (str):
            Optional. Human readable name of a
            Deployment.
        repository (str):
            Output only. Name of the repository where the
            deployment package files are stored.
        files (MutableSequence[google.cloud.telcoautomation_v1.types.File]):
            Optional. Files present in a deployment.
            When invoking UpdateDeployment API, only the
            modified files should be included in this. Files
            that are not included in the update of a
            deployment will not be changed.
        labels (MutableMapping[str, str]):
            Optional. Labels are key-value attributes
            that can be set on a deployment resource by the
            user.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Deployment creation time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the
            deployment was updated.
        source_provider (str):
            Output only. Source provider is the author of
            a public blueprint, from which this deployment
            is created.
        workload_cluster (str):
            Optional. Immutable. The WorkloadCluster on which to create
            the Deployment. This field should only be passed when the
            deployment_level of the source blueprint specifies
            deployments on workload clusters e.g.
            WORKLOAD_CLUSTER_DEPLOYMENT.
        deployment_level (google.cloud.telcoautomation_v1.types.DeploymentLevel):
            Output only. Attributes to where the deployment can inflict
            changes. The value can only be [SINGLE_DEPLOYMENT,
            MULTI_DEPLOYMENT].
        rollback_support (bool):
            Output only. Indicates if the deployment can
            be rolled back, exported from public blueprint.
    """

    class State(proto.Enum):
        r"""State defines which state the current deployment is in.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified state.
            DRAFT (1):
                A deployment starts in DRAFT state. All edits
                are made in DRAFT state. A deployment opened for
                editing after applying will be in draft state,
                while its prevision revision will be its current
                applied version.
            APPLIED (2):
                This state means that the contents (YAML
                files containing kubernetes resources) of the
                deployment have been applied to an Orchestration
                or Workload Cluster. A revision is created when
                a deployment is applied. This revision will
                represent the latest view of what is applied on
                the cluster until the deployment is modified and
                applied again, which will create a new revision.
            DELETING (3):
                A deployment in DELETING state has been marked for deletion.
                Its deletion status can be queried using
                ``ComputeDeploymentStatus`` API. No updates are allowed to a
                deployment in DELETING state.
        """

        STATE_UNSPECIFIED = 0
        DRAFT = 1
        APPLIED = 2
        DELETING = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    revision_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    source_blueprint_revision: str = proto.Field(
        proto.STRING,
        number=3,
    )
    revision_create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=5,
        enum=State,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=6,
    )
    repository: str = proto.Field(
        proto.STRING,
        number=7,
    )
    files: MutableSequence["File"] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message="File",
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=9,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )
    source_provider: str = proto.Field(
        proto.STRING,
        number=12,
    )
    workload_cluster: str = proto.Field(
        proto.STRING,
        number=13,
    )
    deployment_level: "DeploymentLevel" = proto.Field(
        proto.ENUM,
        number=14,
        enum="DeploymentLevel",
    )
    rollback_support: bool = proto.Field(
        proto.BOOL,
        number=15,
    )


class HydratedDeployment(proto.Message):
    r"""A collection of kubernetes yaml files which are deployed on a
    Workload Cluster. Hydrated Deployments are created by TNA intent
    based automation.

    Attributes:
        name (str):
            Output only. The name of the hydrated
            deployment.
        state (google.cloud.telcoautomation_v1.types.HydratedDeployment.State):
            Output only. State of the hydrated deployment
            (DRAFT, APPLIED).
        files (MutableSequence[google.cloud.telcoautomation_v1.types.File]):
            Optional. File contents of a hydrated
            deployment. When invoking
            UpdateHydratedBlueprint API, only the modified
            files should be included in this. Files that are
            not included in the update of a hydrated
            deployment will not be changed.
        workload_cluster (str):
            Output only. WorkloadCluster identifies which
            workload cluster will the hydrated deployment
            will be deployed on.
    """

    class State(proto.Enum):
        r"""State defines which state the current hydrated deployment is
        in.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified state.
            DRAFT (1):
                A hydrated deployment starts in DRAFT state.
                All edits are made in DRAFT state.
            APPLIED (2):
                When the edit is applied, the hydrated
                deployment moves to APPLIED state. No changes
                can be made once a hydrated deployment is
                applied.
        """

        STATE_UNSPECIFIED = 0
        DRAFT = 1
        APPLIED = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=2,
        enum=State,
    )
    files: MutableSequence["File"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="File",
    )
    workload_cluster: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListOrchestrationClustersRequest(proto.Message):
    r"""Message for requesting list of OrchestrationClusters.

    Attributes:
        parent (str):
            Required. Parent value for
            ListOrchestrationClustersRequest
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
            Hint for how to order the results.
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


class ListOrchestrationClustersResponse(proto.Message):
    r"""Message for response to listing OrchestrationClusters.

    Attributes:
        orchestration_clusters (MutableSequence[google.cloud.telcoautomation_v1.types.OrchestrationCluster]):
            The list of OrchestrationCluster
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    orchestration_clusters: MutableSequence["OrchestrationCluster"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="OrchestrationCluster",
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


class GetOrchestrationClusterRequest(proto.Message):
    r"""Message for getting a OrchestrationCluster.

    Attributes:
        name (str):
            Required. Name of the resource
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateOrchestrationClusterRequest(proto.Message):
    r"""Message for creating a OrchestrationCluster.

    Attributes:
        parent (str):
            Required. Value for parent.
        orchestration_cluster_id (str):
            Required. Id of the requesting object If auto-generating Id
            server-side, remove this field and orchestration_cluster_id
            from the method_signature of Create RPC
        orchestration_cluster (google.cloud.telcoautomation_v1.types.OrchestrationCluster):
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
    orchestration_cluster_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    orchestration_cluster: "OrchestrationCluster" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="OrchestrationCluster",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteOrchestrationClusterRequest(proto.Message):
    r"""Message for deleting a OrchestrationCluster.

    Attributes:
        name (str):
            Required. Name of the resource
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


class ListEdgeSlmsRequest(proto.Message):
    r"""Message for requesting list of EdgeSlms

    Attributes:
        parent (str):
            Required. Parent value for
            ListEdgeSlmsRequest
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


class ListEdgeSlmsResponse(proto.Message):
    r"""Message for response to listing EdgeSlms.

    Attributes:
        edge_slms (MutableSequence[google.cloud.telcoautomation_v1.types.EdgeSlm]):
            The list of EdgeSlm
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    edge_slms: MutableSequence["EdgeSlm"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="EdgeSlm",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetEdgeSlmRequest(proto.Message):
    r"""Message for getting a EdgeSlm.

    Attributes:
        name (str):
            Required. Name of the resource
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateEdgeSlmRequest(proto.Message):
    r"""Message for creating a EdgeSlm.

    Attributes:
        parent (str):
            Required. Value for parent.
        edge_slm_id (str):
            Required. Id of the requesting object If auto-generating Id
            server-side, remove this field and edge_slm_id from the
            method_signature of Create RPC
        edge_slm (google.cloud.telcoautomation_v1.types.EdgeSlm):
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
    edge_slm_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    edge_slm: "EdgeSlm" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="EdgeSlm",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteEdgeSlmRequest(proto.Message):
    r"""Message for deleting a EdgeSlm.

    Attributes:
        name (str):
            Required. Name of the resource
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


class CreateBlueprintRequest(proto.Message):
    r"""Request object for ``CreateBlueprint``.

    Attributes:
        parent (str):
            Required. The name of parent resource. Format should be -
            "projects/{project_id}/locations/{location_name}/orchestrationClusters/{orchestration_cluster}".
        blueprint_id (str):
            Optional. The name of the blueprint.
        blueprint (google.cloud.telcoautomation_v1.types.Blueprint):
            Required. The ``Blueprint`` to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    blueprint_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    blueprint: "Blueprint" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Blueprint",
    )


class UpdateBlueprintRequest(proto.Message):
    r"""Request object for ``UpdateBlueprint``.

    Attributes:
        blueprint (google.cloud.telcoautomation_v1.types.Blueprint):
            Required. The ``blueprint`` to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Update mask is used to specify the fields to be
            overwritten in the ``blueprint`` resource by the update.
    """

    blueprint: "Blueprint" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Blueprint",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class GetBlueprintRequest(proto.Message):
    r"""Request object for ``GetBlueprint``.

    Attributes:
        name (str):
            Required. The name of the blueprint. Case 1: If the name
            provided in the request is {blueprint_id}@{revision_id},
            then the revision with revision_id will be returned. Case 2:
            If the name provided in the request is {blueprint}, then the
            current state of the blueprint is returned.
        view (google.cloud.telcoautomation_v1.types.BlueprintView):
            Optional. Defines the type of view of the blueprint. When
            field is not present BLUEPRINT_VIEW_BASIC is considered as
            default.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: "BlueprintView" = proto.Field(
        proto.ENUM,
        number=2,
        enum="BlueprintView",
    )


class DeleteBlueprintRequest(proto.Message):
    r"""Request object for ``DeleteBlueprint``.

    Attributes:
        name (str):
            Required. The name of blueprint to delete. Blueprint name
            should be in the format {blueprint_id}, if
            {blueprint_id}@{revision_id} is passed then the API throws
            invalid argument.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListBlueprintsRequest(proto.Message):
    r"""Request object for ``ListBlueprints``.

    Attributes:
        parent (str):
            Required. The name of parent orchestration cluster resource.
            Format should be -
            "projects/{project_id}/locations/{location_name}/orchestrationClusters/{orchestration_cluster}".
        filter (str):
            Optional. Filtering only supports equality on blueprint
            state. It should be in the form: "state = DRAFT". ``OR``
            operator can be used to get response for multiple states.
            e.g. "state = DRAFT OR state = PROPOSED".
        page_size (int):
            Optional. The maximum number of blueprints to
            return per page.
        page_token (str):
            Optional. The page token, received from a
            previous ListBlueprints call. It can be provided
            to retrieve the subsequent page.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListBlueprintsResponse(proto.Message):
    r"""Response object for ``ListBlueprints``.

    Attributes:
        blueprints (MutableSequence[google.cloud.telcoautomation_v1.types.Blueprint]):
            The list of requested blueprints.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    blueprints: MutableSequence["Blueprint"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Blueprint",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ApproveBlueprintRequest(proto.Message):
    r"""Request object for ``ApproveBlueprint``.

    Attributes:
        name (str):
            Required. The name of the blueprint to
            approve. The blueprint must be in Proposed
            state. A new revision is committed on approval.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ProposeBlueprintRequest(proto.Message):
    r"""Request object for ``ProposeBlueprint``.

    Attributes:
        name (str):
            Required. The name of the blueprint being
            proposed.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class RejectBlueprintRequest(proto.Message):
    r"""Request object for ``RejectBlueprint``.

    Attributes:
        name (str):
            Required. The name of the blueprint being
            rejected.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListBlueprintRevisionsRequest(proto.Message):
    r"""Request object for ``ListBlueprintRevisions``.

    Attributes:
        name (str):
            Required. The name of the blueprint to list
            revisions for.
        page_size (int):
            The maximum number of revisions to return per
            page.
        page_token (str):
            The page token, received from a previous
            ListBlueprintRevisions call It can be provided
            to retrieve the subsequent page.
    """

    name: str = proto.Field(
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


class ListBlueprintRevisionsResponse(proto.Message):
    r"""Response object for ``ListBlueprintRevisions``.

    Attributes:
        blueprints (MutableSequence[google.cloud.telcoautomation_v1.types.Blueprint]):
            The revisions of the blueprint.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    blueprints: MutableSequence["Blueprint"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Blueprint",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SearchBlueprintRevisionsRequest(proto.Message):
    r"""Request object for ``SearchBlueprintRevisions``.

    Attributes:
        parent (str):
            Required. The name of parent orchestration cluster resource.
            Format should be -
            "projects/{project_id}/locations/{location_name}/orchestrationClusters/{orchestration_cluster}".
        query (str):
            Required. Supported queries:

            1. ""                       : Lists all
                revisions across all blueprints.
            2. "latest=true"            : Lists latest
                revisions across all blueprints.
            3. "name={name}"            : Lists all
                revisions of blueprint with name {name}.
            4. "name={name} latest=true": Lists latest
                revision of blueprint with name {name}
        page_size (int):
            Optional. The maximum number of blueprints
            revisions to return per page. max page size =
            100, default page size = 20.
        page_token (str):
            Optional. The page token, received from a
            previous search call. It can be provided to
            retrieve the subsequent page.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    query: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class SearchBlueprintRevisionsResponse(proto.Message):
    r"""Response object for ``SearchBlueprintRevisions``.

    Attributes:
        blueprints (MutableSequence[google.cloud.telcoautomation_v1.types.Blueprint]):
            The list of requested blueprint revisions.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    blueprints: MutableSequence["Blueprint"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Blueprint",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DiscardBlueprintChangesRequest(proto.Message):
    r"""Request object for ``DiscardBlueprintChanges``.

    Attributes:
        name (str):
            Required. The name of the blueprint of which
            changes are being discarded.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DiscardBlueprintChangesResponse(proto.Message):
    r"""Response object for ``DiscardBlueprintChanges``."""


class ListPublicBlueprintsRequest(proto.Message):
    r"""Request object for ``ListPublicBlueprints``.

    Attributes:
        parent (str):
            Required. Parent value of public blueprint. Format should be
            - "projects/{project_id}/locations/{location_name}".
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
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


class ListPublicBlueprintsResponse(proto.Message):
    r"""Response object for ``ListPublicBlueprints``.

    Attributes:
        public_blueprints (MutableSequence[google.cloud.telcoautomation_v1.types.PublicBlueprint]):
            The list of public blueprints to return.
        next_page_token (str):
            Output only. A token identifying a page of
            results the server should return.
    """

    @property
    def raw_page(self):
        return self

    public_blueprints: MutableSequence["PublicBlueprint"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="PublicBlueprint",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetPublicBlueprintRequest(proto.Message):
    r"""Request object for ``GetPublicBlueprint``.

    Attributes:
        name (str):
            Required. The name of the public blueprint.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateDeploymentRequest(proto.Message):
    r"""Request object for ``CreateDeployment``.

    Attributes:
        parent (str):
            Required. The name of parent resource. Format should be -
            "projects/{project_id}/locations/{location_name}/orchestrationClusters/{orchestration_cluster}".
        deployment_id (str):
            Optional. The name of the deployment.
        deployment (google.cloud.telcoautomation_v1.types.Deployment):
            Required. The ``Deployment`` to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    deployment_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    deployment: "Deployment" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Deployment",
    )


class UpdateDeploymentRequest(proto.Message):
    r"""Request object for ``UpdateDeployment``.

    Attributes:
        deployment (google.cloud.telcoautomation_v1.types.Deployment):
            Required. The ``deployment`` to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Update mask is used to specify the fields to be
            overwritten in the ``deployment`` resource by the update.
    """

    deployment: "Deployment" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Deployment",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class GetDeploymentRequest(proto.Message):
    r"""Request object for ``GetDeployment``.

    Attributes:
        name (str):
            Required. The name of the deployment. Case 1: If the name
            provided in the request is {deployment_id}@{revision_id},
            then the revision with revision_id will be returned. Case 2:
            If the name provided in the request is {deployment}, then
            the current state of the deployment is returned.
        view (google.cloud.telcoautomation_v1.types.DeploymentView):
            Optional. Defines the type of view of the deployment. When
            field is not present VIEW_BASIC is considered as default.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: "DeploymentView" = proto.Field(
        proto.ENUM,
        number=2,
        enum="DeploymentView",
    )


class RemoveDeploymentRequest(proto.Message):
    r"""Request object for ``RemoveDeployment``.

    Attributes:
        name (str):
            Required. The name of deployment to initiate
            delete.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListDeploymentsRequest(proto.Message):
    r"""Request object for ``ListDeployments``.

    Attributes:
        parent (str):
            Required. The name of parent orchestration cluster resource.
            Format should be -
            "projects/{project_id}/locations/{location_name}/orchestrationClusters/{orchestration_cluster}".
        filter (str):
            Optional. Filtering only supports equality on deployment
            state. It should be in the form: "state = DRAFT". ``OR``
            operator can be used to get response for multiple states.
            e.g. "state = DRAFT OR state = APPLIED".
        page_size (int):
            Optional. The maximum number of deployments
            to return per page.
        page_token (str):
            Optional. The page token, received from a
            previous ListDeployments call. It can be
            provided to retrieve the subsequent page.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListDeploymentsResponse(proto.Message):
    r"""Response object for ``ListDeployments``.

    Attributes:
        deployments (MutableSequence[google.cloud.telcoautomation_v1.types.Deployment]):
            The list of requested deployments.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    deployments: MutableSequence["Deployment"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Deployment",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListDeploymentRevisionsRequest(proto.Message):
    r"""Request for listing all revisions of a deployment.

    Attributes:
        name (str):
            Required. The name of the deployment to list
            revisions for.
        page_size (int):
            Optional. The maximum number of revisions to
            return per page.
        page_token (str):
            Optional. The page token, received from a
            previous ListDeploymentRevisions call Provide
            this to retrieve the subsequent page.
    """

    name: str = proto.Field(
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


class ListDeploymentRevisionsResponse(proto.Message):
    r"""List of deployment revisions for a given deployment.

    Attributes:
        deployments (MutableSequence[google.cloud.telcoautomation_v1.types.Deployment]):
            The revisions of the deployment.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    deployments: MutableSequence["Deployment"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Deployment",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SearchDeploymentRevisionsRequest(proto.Message):
    r"""Request object for ``SearchDeploymentRevisions``.

    Attributes:
        parent (str):
            Required. The name of parent orchestration cluster resource.
            Format should be -
            "projects/{project_id}/locations/{location_name}/orchestrationClusters/{orchestration_cluster}".
        query (str):
            Required. Supported queries:

            1. ""                       : Lists all
                revisions across all deployments.
            2. "latest=true"            : Lists latest
                revisions across all deployments.
            3. "name={name}"            : Lists all
                revisions of deployment with name {name}.
            4. "name={name} latest=true": Lists latest
                revision of deployment with name {name}
        page_size (int):
            Optional. The maximum number of deployment
            revisions to return per page. max page size =
            100, default page size = 20.
        page_token (str):
            Optional. The page token, received from a
            previous search call. It can be provided to
            retrieve the subsequent page.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    query: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class SearchDeploymentRevisionsResponse(proto.Message):
    r"""Response object for ``SearchDeploymentRevisions``.

    Attributes:
        deployments (MutableSequence[google.cloud.telcoautomation_v1.types.Deployment]):
            The list of requested deployment revisions.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    deployments: MutableSequence["Deployment"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Deployment",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DiscardDeploymentChangesRequest(proto.Message):
    r"""Request object for ``DiscardDeploymentChanges``.

    Attributes:
        name (str):
            Required. The name of the deployment of which
            changes are being discarded.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DiscardDeploymentChangesResponse(proto.Message):
    r"""Response object for ``DiscardDeploymentChanges``."""


class ApplyDeploymentRequest(proto.Message):
    r"""Request object for ``ApplyDeployment``. The resources in given
    deployment gets applied to Orchestration Cluster. A new revision is
    created when a deployment is applied.

    Attributes:
        name (str):
            Required. The name of the deployment to apply
            to orchestration cluster.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ComputeDeploymentStatusRequest(proto.Message):
    r"""Request object for ``ComputeDeploymentStatus``.

    Attributes:
        name (str):
            Required. The name of the deployment without
            revisionID.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ComputeDeploymentStatusResponse(proto.Message):
    r"""Response object for ``ComputeDeploymentStatus``.

    Attributes:
        name (str):
            The name of the deployment.
        aggregated_status (google.cloud.telcoautomation_v1.types.Status):
            Output only. Aggregated status of a
            deployment.
        resource_statuses (MutableSequence[google.cloud.telcoautomation_v1.types.ResourceStatus]):
            Output only. Resource level status details in
            deployments.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    aggregated_status: "Status" = proto.Field(
        proto.ENUM,
        number=2,
        enum="Status",
    )
    resource_statuses: MutableSequence["ResourceStatus"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="ResourceStatus",
    )


class RollbackDeploymentRequest(proto.Message):
    r"""Request object for ``RollbackDeployment``.

    Attributes:
        name (str):
            Required. Name of the deployment.
        revision_id (str):
            Required. The revision id of deployment to
            roll back to.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    revision_id: str = proto.Field(
        proto.STRING,
        number=2,
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


class GetHydratedDeploymentRequest(proto.Message):
    r"""Request object for ``GetHydratedDeployment``.

    Attributes:
        name (str):
            Required. Name of the hydrated deployment.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListHydratedDeploymentsRequest(proto.Message):
    r"""Request object for ``ListHydratedDeployments``.

    Attributes:
        parent (str):
            Required. The deployment managing the
            hydrated deployments.
        page_size (int):
            Optional. The maximum number of hydrated
            deployments to return. The service may return
            fewer than this value. If unspecified, at most
            50 hydrated deployments will be returned. The
            maximum value is 1000. Values above 1000 will be
            set to 1000.
        page_token (str):
            Optional. The page token, received from a
            previous ListHydratedDeployments call. Provide
            this to retrieve the subsequent page.
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


class ListHydratedDeploymentsResponse(proto.Message):
    r"""Response object for ``ListHydratedDeployments``.

    Attributes:
        hydrated_deployments (MutableSequence[google.cloud.telcoautomation_v1.types.HydratedDeployment]):
            The list of hydrated deployments.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    hydrated_deployments: MutableSequence["HydratedDeployment"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="HydratedDeployment",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateHydratedDeploymentRequest(proto.Message):
    r"""Request object for ``UpdateHydratedDeployment``.

    Attributes:
        hydrated_deployment (google.cloud.telcoautomation_v1.types.HydratedDeployment):
            Required. The hydrated deployment to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to update. Update mask supports
            a special value ``*`` which fully replaces (equivalent to
            PUT) the resource provided.
    """

    hydrated_deployment: "HydratedDeployment" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="HydratedDeployment",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class ApplyHydratedDeploymentRequest(proto.Message):
    r"""Request for applying a hydrated deployment.

    Attributes:
        name (str):
            Required. The name of the hydrated deployment
            to apply.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ManagementConfig(proto.Message):
    r"""Configuration of the cluster management

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        standard_management_config (google.cloud.telcoautomation_v1.types.StandardManagementConfig):
            Configuration of the standard (GKE) cluster
            management

            This field is a member of `oneof`_ ``oneof_config``.
        full_management_config (google.cloud.telcoautomation_v1.types.FullManagementConfig):
            Configuration of the full (Autopilot) cluster
            management. Full cluster management is a preview
            feature.

            This field is a member of `oneof`_ ``oneof_config``.
    """

    standard_management_config: "StandardManagementConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="oneof_config",
        message="StandardManagementConfig",
    )
    full_management_config: "FullManagementConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="oneof_config",
        message="FullManagementConfig",
    )


class StandardManagementConfig(proto.Message):
    r"""Configuration of the standard (GKE) cluster management.

    Attributes:
        network (str):
            Optional. Name of the VPC Network to put the
            GKE cluster and nodes in. The VPC will be
            created if it doesn't exist.
        subnet (str):
            Optional. Specifies the subnet that the
            interface will be part of. Network key must be
            specified and the subnet must be a subnetwork of
            the specified network.
        master_ipv4_cidr_block (str):
            Optional. The /28 network that the masters
            will use. It should be free within the network.
        cluster_cidr_block (str):
            Optional. The IP address range for the
            cluster pod IPs. Set to blank to have a range
            chosen with the default size. Set to /netmask
            (e.g. /14) to have a range chosen with a
            specific netmask. Set to a CIDR notation (e.g.
            10.96.0.0/14) from the RFC-1918 private networks
            (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16)
            to pick a specific range to use.
        services_cidr_block (str):
            Optional. The IP address range for the
            cluster service IPs. Set to blank to have a
            range chosen with the default size. Set to
            /netmask (e.g. /14) to have a range chosen with
            a specific netmask. Set to a CIDR notation (e.g.
            10.96.0.0/14) from the RFC-1918 private networks
            (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16)
            to pick a specific range to use.
        cluster_named_range (str):
            Optional. The name of the existing secondary range in the
            cluster's subnetwork to use for pod IP addresses.
            Alternatively, cluster_cidr_block can be used to
            automatically create a GKE-managed one.
        services_named_range (str):
            Optional. The name of the existing secondary range in the
            cluster's subnetwork to use for service ClusterIPs.
            Alternatively, services_cidr_block can be used to
            automatically create a GKE-managed one.
        master_authorized_networks_config (google.cloud.telcoautomation_v1.types.MasterAuthorizedNetworksConfig):
            Optional. Master Authorized Network that supports multiple
            CIDR blocks. Allows access to the k8s master from multiple
            blocks. It cannot be set at the same time with the field
            man_block.
    """

    network: str = proto.Field(
        proto.STRING,
        number=1,
    )
    subnet: str = proto.Field(
        proto.STRING,
        number=2,
    )
    master_ipv4_cidr_block: str = proto.Field(
        proto.STRING,
        number=3,
    )
    cluster_cidr_block: str = proto.Field(
        proto.STRING,
        number=4,
    )
    services_cidr_block: str = proto.Field(
        proto.STRING,
        number=5,
    )
    cluster_named_range: str = proto.Field(
        proto.STRING,
        number=6,
    )
    services_named_range: str = proto.Field(
        proto.STRING,
        number=7,
    )
    master_authorized_networks_config: "MasterAuthorizedNetworksConfig" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="MasterAuthorizedNetworksConfig",
    )


class FullManagementConfig(proto.Message):
    r"""Configuration of the full (Autopilot) cluster management

    Attributes:
        network (str):
            Optional. Name of the VPC Network to put the
            GKE cluster and nodes in. The VPC will be
            created if it doesn't exist.
        subnet (str):
            Optional. Specifies the subnet that the
            interface will be part of. Network key must be
            specified and the subnet must be a subnetwork of
            the specified network.
        master_ipv4_cidr_block (str):
            Optional. The /28 network that the masters
            will use.
        cluster_cidr_block (str):
            Optional. The IP address range for the
            cluster pod IPs. Set to blank to have a range
            chosen with the default size. Set to /netmask
            (e.g. /14) to have a range chosen with a
            specific netmask. Set to a CIDR notation (e.g.
            10.96.0.0/14) from the RFC-1918 private networks
            (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16)
            to pick a specific range to use.
        services_cidr_block (str):
            Optional. The IP address range for the
            cluster service IPs. Set to blank to have a
            range chosen with the default size. Set to
            /netmask (e.g. /14) to have a range chosen with
            a specific netmask. Set to a CIDR notation (e.g.
            10.96.0.0/14) from the RFC-1918 private networks
            (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16)
            to pick a specific range to use.
        cluster_named_range (str):
            Optional. The name of the existing secondary range in the
            cluster's subnetwork to use for pod IP addresses.
            Alternatively, cluster_cidr_block can be used to
            automatically create a GKE-managed one.
        services_named_range (str):
            Optional. The name of the existing secondary range in the
            cluster's subnetwork to use for service ClusterIPs.
            Alternatively, services_cidr_block can be used to
            automatically create a GKE-managed one.
        master_authorized_networks_config (google.cloud.telcoautomation_v1.types.MasterAuthorizedNetworksConfig):
            Optional. Master Authorized Network that supports multiple
            CIDR blocks. Allows access to the k8s master from multiple
            blocks. It cannot be set at the same time with the field
            man_block.
    """

    network: str = proto.Field(
        proto.STRING,
        number=1,
    )
    subnet: str = proto.Field(
        proto.STRING,
        number=2,
    )
    master_ipv4_cidr_block: str = proto.Field(
        proto.STRING,
        number=3,
    )
    cluster_cidr_block: str = proto.Field(
        proto.STRING,
        number=4,
    )
    services_cidr_block: str = proto.Field(
        proto.STRING,
        number=5,
    )
    cluster_named_range: str = proto.Field(
        proto.STRING,
        number=6,
    )
    services_named_range: str = proto.Field(
        proto.STRING,
        number=7,
    )
    master_authorized_networks_config: "MasterAuthorizedNetworksConfig" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="MasterAuthorizedNetworksConfig",
    )


class MasterAuthorizedNetworksConfig(proto.Message):
    r"""Configuration of the Master Authorized Network that support
    multiple CIDRs

    Attributes:
        cidr_blocks (MutableSequence[google.cloud.telcoautomation_v1.types.MasterAuthorizedNetworksConfig.CidrBlock]):
            Optional. cidr_blocks define up to 50 external networks that
            could access Kubernetes master through HTTPS.
    """

    class CidrBlock(proto.Message):
        r"""CidrBlock contains an optional name and one CIDR block.

        Attributes:
            display_name (str):
                Optional. display_name is an optional field for users to
                identify CIDR blocks.
            cidr_block (str):
                Optional. cidr_block must be specified in CIDR notation when
                using master_authorized_networks_config. Currently, the user
                could still use the deprecated man_block field, so this
                field is currently optional, but will be required in the
                future.
        """

        display_name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        cidr_block: str = proto.Field(
            proto.STRING,
            number=2,
        )

    cidr_blocks: MutableSequence[CidrBlock] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=CidrBlock,
    )


class File(proto.Message):
    r"""File represents a yaml file present in a blueprint's package.

    Attributes:
        path (str):
            Required. Path of the file in package. e.g.
            ``gdce/v1/cluster.yaml``
        content (str):
            Optional. The contents of a file in string
            format.
        deleted (bool):
            Optional. Signifies whether a file is marked
            for deletion.
        editable (bool):
            Optional. Indicates whether changes are
            allowed to a file. If the field is not set, the
            file cannot be edited.
    """

    path: str = proto.Field(
        proto.STRING,
        number=1,
    )
    content: str = proto.Field(
        proto.STRING,
        number=2,
    )
    deleted: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    editable: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class ResourceStatus(proto.Message):
    r"""Status of a deployment resource.

    Attributes:
        name (str):
            Name of the resource.
        resource_namespace (str):
            Namespace of the resource.
        group (str):
            Group to which the resource belongs to.
        version (str):
            Version of the resource.
        kind (str):
            Kind of the resource.
        resource_type (google.cloud.telcoautomation_v1.types.ResourceType):
            Output only. Resource type.
        status (google.cloud.telcoautomation_v1.types.Status):
            Output only. Status of the resource.
        nf_deploy_status (google.cloud.telcoautomation_v1.types.NFDeployStatus):
            Output only. Detailed status of NFDeploy.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    resource_namespace: str = proto.Field(
        proto.STRING,
        number=2,
    )
    group: str = proto.Field(
        proto.STRING,
        number=3,
    )
    version: str = proto.Field(
        proto.STRING,
        number=4,
    )
    kind: str = proto.Field(
        proto.STRING,
        number=5,
    )
    resource_type: "ResourceType" = proto.Field(
        proto.ENUM,
        number=6,
        enum="ResourceType",
    )
    status: "Status" = proto.Field(
        proto.ENUM,
        number=7,
        enum="Status",
    )
    nf_deploy_status: "NFDeployStatus" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="NFDeployStatus",
    )


class NFDeployStatus(proto.Message):
    r"""Deployment status of NFDeploy.

    Attributes:
        targeted_nfs (int):
            Output only. Total number of NFs targeted by
            this deployment
        ready_nfs (int):
            Output only. Total number of NFs targeted by
            this deployment with a Ready Condition set.
        sites (MutableSequence[google.cloud.telcoautomation_v1.types.NFDeploySiteStatus]):
            Output only. Per-Site Status.
    """

    targeted_nfs: int = proto.Field(
        proto.INT32,
        number=1,
    )
    ready_nfs: int = proto.Field(
        proto.INT32,
        number=2,
    )
    sites: MutableSequence["NFDeploySiteStatus"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="NFDeploySiteStatus",
    )


class NFDeploySiteStatus(proto.Message):
    r"""Per-Site Status.

    Attributes:
        site (str):
            Output only. Site id.
        pending_deletion (bool):
            Output only. If true, the Site Deletion is in
            progress.
        hydration (google.cloud.telcoautomation_v1.types.HydrationStatus):
            Output only. Hydration status.
        workload (google.cloud.telcoautomation_v1.types.WorkloadStatus):
            Output only. Workload status.
    """

    site: str = proto.Field(
        proto.STRING,
        number=1,
    )
    pending_deletion: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    hydration: "HydrationStatus" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="HydrationStatus",
    )
    workload: "WorkloadStatus" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="WorkloadStatus",
    )


class HydrationStatus(proto.Message):
    r"""Hydration status.

    Attributes:
        site_version (google.cloud.telcoautomation_v1.types.SiteVersion):
            Output only. SiteVersion Hydration is
            targeting.
        status (str):
            Output only. Status.
    """

    site_version: "SiteVersion" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="SiteVersion",
    )
    status: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SiteVersion(proto.Message):
    r"""SiteVersion Hydration is targeting.

    Attributes:
        nf_vendor (str):
            Output only. NF vendor.
        nf_type (str):
            Output only. NF vendor type.
        nf_version (str):
            Output only. NF version.
    """

    nf_vendor: str = proto.Field(
        proto.STRING,
        number=1,
    )
    nf_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    nf_version: str = proto.Field(
        proto.STRING,
        number=3,
    )


class WorkloadStatus(proto.Message):
    r"""Workload status.

    Attributes:
        site_version (google.cloud.telcoautomation_v1.types.SiteVersion):
            Output only. SiteVersion running in the
            workload cluster.
        status (str):
            Output only. Status.
    """

    site_version: "SiteVersion" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="SiteVersion",
    )
    status: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
