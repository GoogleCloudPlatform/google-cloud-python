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
    package="google.cloud.configdelivery.v1",
    manifest={
        "DeletionPropagationPolicy",
        "ResourceBundle",
        "ListResourceBundlesRequest",
        "ListResourceBundlesResponse",
        "GetResourceBundleRequest",
        "CreateResourceBundleRequest",
        "UpdateResourceBundleRequest",
        "DeleteResourceBundleRequest",
        "FleetPackage",
        "FleetPackageInfo",
        "FleetPackageError",
        "ClusterInfo",
        "ResourceBundleDeploymentInfo",
        "Fleet",
        "AllAtOnceStrategy",
        "RollingStrategy",
        "RolloutStrategy",
        "RolloutStrategyInfo",
        "AllAtOnceStrategyInfo",
        "RollingStrategyInfo",
        "ListFleetPackagesRequest",
        "ListFleetPackagesResponse",
        "GetFleetPackageRequest",
        "CreateFleetPackageRequest",
        "UpdateFleetPackageRequest",
        "DeleteFleetPackageRequest",
        "OperationMetadata",
        "Release",
        "Variant",
        "ListVariantsRequest",
        "ListVariantsResponse",
        "GetVariantRequest",
        "CreateVariantRequest",
        "UpdateVariantRequest",
        "DeleteVariantRequest",
        "ReleaseInfo",
        "ListReleasesRequest",
        "ListReleasesResponse",
        "GetReleaseRequest",
        "CreateReleaseRequest",
        "UpdateReleaseRequest",
        "DeleteReleaseRequest",
        "ListRolloutsRequest",
        "ListRolloutsResponse",
        "GetRolloutRequest",
        "RolloutInfo",
        "Rollout",
        "SuspendRolloutRequest",
        "ResumeRolloutRequest",
        "AbortRolloutRequest",
    },
)


class DeletionPropagationPolicy(proto.Enum):
    r"""Deletion Propagation Policy determines what happens to the
    underlying Kubernetes resources on a cluster when the
    ``FleetPackage`` managing those resources no longer targets the
    cluster or is deleted.

    Values:
        DELETION_PROPAGATION_POLICY_UNSPECIFIED (0):
            Unspecified deletion propagation policy.
            Defaults to FOREGROUND.
        FOREGROUND (1):
            Foreground deletion propagation policy. Any
            resources synced to the cluster will be deleted.
        ORPHAN (2):
            Orphan deletion propagation policy. Any
            resources synced to the cluster will be
            abandoned.
    """

    DELETION_PROPAGATION_POLICY_UNSPECIFIED = 0
    FOREGROUND = 1
    ORPHAN = 2


class ResourceBundle(proto.Message):
    r"""ResourceBundle represent a collection of kubernetes
    configuration resources.

    Attributes:
        name (str):
            Identifier. Name of the ``ResourceBundle``. Format is
            ``projects/{project}/locations/{location}/resourceBundle /[a-z][a-z0-9\-]{0,62}``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time ``ResourceBundle`` was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time ``ResourceBundle`` was last updated.
        labels (MutableMapping[str, str]):
            Optional. Labels as key value pairs.
        description (str):
            Optional. Human readable description of the
            ``ResourceBundle``.
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
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListResourceBundlesRequest(proto.Message):
    r"""Message for requesting list of ResourceBundles.

    Attributes:
        parent (str):
            Required. Parent value for
            ListResourceBundlesRequest.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
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


class ListResourceBundlesResponse(proto.Message):
    r"""Message for response to listing ResourceBundles.

    Attributes:
        resource_bundles (MutableSequence[google.cloud.configdelivery_v1.types.ResourceBundle]):
            The list of ResourceBundle.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Unordered list. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    resource_bundles: MutableSequence["ResourceBundle"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ResourceBundle",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetResourceBundleRequest(proto.Message):
    r"""Message for getting a ResourceBundle.

    Attributes:
        name (str):
            Required. Name of the resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateResourceBundleRequest(proto.Message):
    r"""Message for creating a ResourceBundle.

    Attributes:
        parent (str):
            Required. Value for parent.
        resource_bundle_id (str):
            Required. Id of the requesting object If auto-generating Id
            server-side, remove this field and resource_bundle_id from
            the method_signature of Create RPC
        resource_bundle (google.cloud.configdelivery_v1.types.ResourceBundle):
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
    resource_bundle_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    resource_bundle: "ResourceBundle" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ResourceBundle",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateResourceBundleRequest(proto.Message):
    r"""Message for updating a ResourceBundle

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the ResourceBundle resource by the update.
            The fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        resource_bundle (google.cloud.configdelivery_v1.types.ResourceBundle):
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
    resource_bundle: "ResourceBundle" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ResourceBundle",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteResourceBundleRequest(proto.Message):
    r"""Message for deleting a ResourceBundle

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
        force (bool):
            Optional. If set to true, any releases of
            this resource bundle will also be deleted.
            (Otherwise, the request will only work if the
            resource bundle has no releases.)
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


class FleetPackage(proto.Message):
    r"""A ``FleetPackage`` resource in the Config Delivery API.

    A ``FleetPackage`` defines a package through which kubernetes
    configuration is deployed to a fleet of kubernetes clusters.

    Attributes:
        name (str):
            Identifier. Name of the ``FleetPackage``. Format is
            ``projects/{project}/locations/{location}/fleetPackages/{fleetPackage}``.
            The ``fleetPackage`` component must match
            ``[a-z][a-z0-9\-]{0,62}``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time at which the ``FleetPackage`` was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Most recent time at which the ``FleetPackage``
            was updated.
        labels (MutableMapping[str, str]):
            Optional. Labels are attributes that can be set and used by
            both the user and by Config Delivery. Labels must meet the
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
        resource_bundle_selector (google.cloud.configdelivery_v1.types.FleetPackage.ResourceBundleSelector):
            Required. Information specifying the source
            of kubernetes configuration to deploy.
        target (google.cloud.configdelivery_v1.types.FleetPackage.Target):
            Optional. Configuration to select target
            clusters to deploy kubernetes configuration to.
        rollout_strategy (google.cloud.configdelivery_v1.types.RolloutStrategy):
            Optional. The strategy to use to deploy
            kubernetes configuration to clusters.
        variant_selector (google.cloud.configdelivery_v1.types.FleetPackage.VariantSelector):
            Required. Information specifying how to map a
            ``ResourceBundle`` variant to a target cluster.
        info (google.cloud.configdelivery_v1.types.FleetPackageInfo):
            Output only. Information containing the rollout status of
            the ``FleetPackage`` across all the target clusters.
        deletion_propagation_policy (google.cloud.configdelivery_v1.types.DeletionPropagationPolicy):
            Optional. Information around how to handle kubernetes
            resources at the target clusters when the ``FleetPackage``
            is deleted.
        state (google.cloud.configdelivery_v1.types.FleetPackage.State):
            Optional. The desired state of the fleet
            package.
    """

    class State(proto.Enum):
        r"""State indicates the desired state for the fleet package. Unspecified
        value is equivalent to ``ACTIVE``. If state is set to ``SUSPENDED``,
        active rollout (if any) will continue but no new rollouts will be
        scheduled.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified state.
            ACTIVE (1):
                ``FleetPackage`` is intended to be active.
            SUSPENDED (2):
                ``FleetPackage`` is intended to be suspended.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        SUSPENDED = 2

    class ResourceBundleSelector(proto.Message):
        r"""Information specifying the source of kubernetes configuration
        to deploy.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            resource_bundle (google.cloud.configdelivery_v1.types.FleetPackage.ResourceBundleTag):
                Information specifying ``ResourceBundle``.

                This field is a member of `oneof`_ ``source``.
            cloud_build_repository (google.cloud.configdelivery_v1.types.FleetPackage.CloudBuildRepository):
                Information specifying ``CloudBuildRepository``.

                This field is a member of `oneof`_ ``source``.
        """

        resource_bundle: "FleetPackage.ResourceBundleTag" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="source",
            message="FleetPackage.ResourceBundleTag",
        )
        cloud_build_repository: "FleetPackage.CloudBuildRepository" = proto.Field(
            proto.MESSAGE,
            number=3,
            oneof="source",
            message="FleetPackage.CloudBuildRepository",
        )

    class ResourceBundleTag(proto.Message):
        r"""ResourceBundleTag contains the information to refer to a release for
        a ``ResourceBundle``.

        Attributes:
            name (str):
                Required. Name of the ``ResourceBundle``. Format is
                projects/{p}/locations/{l}/resourceBundles/{r}.
            tag (str):
                Required. Tag refers to a version of the release in a
                ``ResourceBundle``. This is a Git tag in the semantic
                version format ``vX.Y.Z``.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        tag: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class CloudBuildRepository(proto.Message):
        r"""CloudBuildRepository contains information about fetching Kubernetes
        configuration from a ``CloudBuildRepository``.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            variants_pattern (str):
                Optional. variants_pattern is a glob pattern that will be
                used to find variants in the repository. Examples:
                ``variants/*.yaml``, ``us-*``

                This field is a member of `oneof`_ ``variants``.
            name (str):
                Required. Name of the cloud build repository.
                Format is
                projects/{p}/locations/{l}/connections/{c}/repositories/{r}.
            path (str):
                Optional. path to the directory or file
                within the repository that contains the
                kubernetes configuration. If unspecified, path
                is assumed to the top level root directory of
                the repository.
            tag (str):
                Required. git tag of the underlying git repository. The git
                tag must be in the semantic version format ``vX.Y.Z``.
            service_account (str):
                Required. Google service account to use in
                CloudBuild triggers to fetch and store
                kubernetes configuration.
        """

        variants_pattern: str = proto.Field(
            proto.STRING,
            number=5,
            oneof="variants",
        )
        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        path: str = proto.Field(
            proto.STRING,
            number=2,
        )
        tag: str = proto.Field(
            proto.STRING,
            number=3,
        )
        service_account: str = proto.Field(
            proto.STRING,
            number=4,
        )

    class Target(proto.Message):
        r"""The target defines different ways to target set of kubernetes
        clusters.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            fleet (google.cloud.configdelivery_v1.types.Fleet):
                The GKE fleet information.

                This field is a member of `oneof`_ ``target``.
        """

        fleet: "Fleet" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="target",
            message="Fleet",
        )

    class VariantSelector(proto.Message):
        r"""VariantSelector contains information for selecting a variant in
        ``ResourceBundle`` to deploy to a target cluster.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            variant_name_template (str):
                Required. variant_name_template is a template that can refer
                to variables containing cluster membership metadata such as
                location, name, and labels to generate the name of the
                variant for a target cluster. The variable syntax is similar
                to the unix shell variables.

                Available variables are ``${membership.name}``,
                ``${membership.location}``, ``${membership.project}`` and
                ``${membership.labels['label_name']}``.

                If you want to deploy a specific variant, say "default" to
                all the clusters, you can use "default" (string without any
                variables) as the variant_name_template.

                This field is a member of `oneof`_ ``strategy``.
        """

        variant_name_template: str = proto.Field(
            proto.STRING,
            number=1,
            oneof="strategy",
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
    resource_bundle_selector: ResourceBundleSelector = proto.Field(
        proto.MESSAGE,
        number=5,
        message=ResourceBundleSelector,
    )
    target: Target = proto.Field(
        proto.MESSAGE,
        number=9,
        message=Target,
    )
    rollout_strategy: "RolloutStrategy" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="RolloutStrategy",
    )
    variant_selector: VariantSelector = proto.Field(
        proto.MESSAGE,
        number=11,
        message=VariantSelector,
    )
    info: "FleetPackageInfo" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="FleetPackageInfo",
    )
    deletion_propagation_policy: "DeletionPropagationPolicy" = proto.Field(
        proto.ENUM,
        number=15,
        enum="DeletionPropagationPolicy",
    )
    state: State = proto.Field(
        proto.ENUM,
        number=16,
        enum=State,
    )


class FleetPackageInfo(proto.Message):
    r"""FleetPackageInfo represents the status of the ``FleetPackage``
    across all the target clusters.

    Attributes:
        active_rollout (str):
            Optional. The active rollout, if any. Format is
            ``projects/{project}/locations/{location}/fleetPackages/{fleet_package}/rollouts/{rollout}``.
        last_completed_rollout (str):
            Optional. The last completed rollout, if any. Format is
            ``projects/{project}/locations/{location}/fleetPackages/{fleet_package}/rollouts/{rollout}``.
        state (google.cloud.configdelivery_v1.types.FleetPackageInfo.State):
            Optional. Output only. The current state of the
            ``FleetPackage``.
        errors (MutableSequence[google.cloud.configdelivery_v1.types.FleetPackageError]):
            Optional. Output only. Errors encountered
            during configuration deployment (if any).
    """

    class State(proto.Enum):
        r"""Possible values for the ``FleetPackage`` state.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified state.
            ACTIVE (1):
                ``FleetPackage`` is active.
            SUSPENDED (2):
                ``FleetPackage`` is suspended.
            FAILED (3):
                ``FleetPackage`` has failed to reconcile.
            DELETING (4):
                ``FleetPackage`` is being deleted.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        SUSPENDED = 2
        FAILED = 3
        DELETING = 4

    active_rollout: str = proto.Field(
        proto.STRING,
        number=1,
    )
    last_completed_rollout: str = proto.Field(
        proto.STRING,
        number=2,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )
    errors: MutableSequence["FleetPackageError"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="FleetPackageError",
    )


class FleetPackageError(proto.Message):
    r"""Information representing an error encountered during rolling
    out configurations.

    Attributes:
        error_message (str):
            Optional. A description of the error.
    """

    error_message: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ClusterInfo(proto.Message):
    r"""ClusterInfo represents status of a resource bundle rollout
    for a cluster.

    Attributes:
        membership (str):
            Output only. gkehub membership of target
            cluster
        desired (google.cloud.configdelivery_v1.types.ResourceBundleDeploymentInfo):
            Output only. Desired state for the resource
            bundle.
        initial (google.cloud.configdelivery_v1.types.ResourceBundleDeploymentInfo):
            Output only. Initial state of the resource
            bundle prior to the deployment.
        current (google.cloud.configdelivery_v1.types.ResourceBundleDeploymentInfo):
            Output only. Current state of the resource
            bundle.
        state (google.cloud.configdelivery_v1.types.ClusterInfo.State):
            Output only. State of the rollout for the
            cluster.
        messages (MutableSequence[str]):
            Output only. Unordered list. Messages convey
            additional information related to the
            deployment.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when reconciliation
            starts.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when reconciliation
            ends.
    """

    class State(proto.Enum):
        r"""State of the rollout for the cluster.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified state.
            WAITING (1):
                Waiting state.
            IN_PROGRESS (2):
                In progress state.
            STALLED (3):
                Stalled state.
            COMPLETED (4):
                Completed state.
            ABORTED (5):
                Aborted state.
            CANCELLED (6):
                Cancelled state.
            ERROR (7):
                Error state.
            UNCHANGED (8):
                Unchanged state.
            SKIPPED (9):
                Skipped state.
        """

        STATE_UNSPECIFIED = 0
        WAITING = 1
        IN_PROGRESS = 2
        STALLED = 3
        COMPLETED = 4
        ABORTED = 5
        CANCELLED = 6
        ERROR = 7
        UNCHANGED = 8
        SKIPPED = 9

    membership: str = proto.Field(
        proto.STRING,
        number=1,
    )
    desired: "ResourceBundleDeploymentInfo" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ResourceBundleDeploymentInfo",
    )
    initial: "ResourceBundleDeploymentInfo" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ResourceBundleDeploymentInfo",
    )
    current: "ResourceBundleDeploymentInfo" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="ResourceBundleDeploymentInfo",
    )
    state: State = proto.Field(
        proto.ENUM,
        number=5,
        enum=State,
    )
    messages: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )


class ResourceBundleDeploymentInfo(proto.Message):
    r"""ResourceBundleDeploymentInfo represents the status of a
    resource bundle deployment.

    Attributes:
        release (str):
            Output only. Refers to a ``ResourceBundle`` release.
        version (str):
            Output only. Refers to a version of the ``ResourceBundle``
            release.
        variant (str):
            Output only. Refers to a variant in a ``ResourceBundle``
            release.
        sync_state (google.cloud.configdelivery_v1.types.ResourceBundleDeploymentInfo.SyncState):
            Output only. Synchronization state of the ``ResourceBundle``
            deployment.
        messages (MutableSequence[str]):
            Output only. Unordered list. Messages contains information
            related to the ``ResourceBundle`` deployment. For example,
            in case of an error, indicate the reason for the error. In
            case of a pending deployment, reason for why the deployment
            of new release is pending.
    """

    class SyncState(proto.Enum):
        r"""Synchronization state of the resource bundle deployment.

        Values:
            SYNC_STATE_UNSPECIFIED (0):
                Unspecified state.
            RECONCILING (1):
                Reconciling state.
            STALLED (2):
                Stalled state.
            SYNCED (3):
                Synced state.
            PENDING (4):
                Pending state.
            ERROR (5):
                Error state.
            DELETION_PENDING (6):
                Deletion pending state.
            DELETING (7):
                Deleting state.
            DELETED (8):
                Deleted state.
        """

        SYNC_STATE_UNSPECIFIED = 0
        RECONCILING = 1
        STALLED = 2
        SYNCED = 3
        PENDING = 4
        ERROR = 5
        DELETION_PENDING = 6
        DELETING = 7
        DELETED = 8

    release: str = proto.Field(
        proto.STRING,
        number=1,
    )
    version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    variant: str = proto.Field(
        proto.STRING,
        number=3,
    )
    sync_state: SyncState = proto.Field(
        proto.ENUM,
        number=4,
        enum=SyncState,
    )
    messages: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )


class Fleet(proto.Message):
    r"""The fleet where the ``FleetPackage`` should be deployed.

    Attributes:
        project (str):
            Required. The host project for the GKE fleet. Format is
            ``projects/{project}``.
        selector (google.cloud.configdelivery_v1.types.Fleet.LabelSelector):
            Optional. selector allows targeting a subset
            of fleet members using their labels.
    """

    class LabelSelector(proto.Message):
        r"""A label selector is a label query over a set of resources. An
        empty label selector matches all objects.

        Attributes:
            match_labels (MutableMapping[str, str]):
                Optional. match_labels is a map of {key,value} pairs. Each
                {key,value} pair must match an existing label key and value
                exactly in order to satisfy the match.
        """

        match_labels: MutableMapping[str, str] = proto.MapField(
            proto.STRING,
            proto.STRING,
            number=1,
        )

    project: str = proto.Field(
        proto.STRING,
        number=1,
    )
    selector: LabelSelector = proto.Field(
        proto.MESSAGE,
        number=2,
        message=LabelSelector,
    )


class AllAtOnceStrategy(proto.Message):
    r"""AllAtOnceStrategy causes all clusters to be updated
    concurrently.

    """


class RollingStrategy(proto.Message):
    r"""RollingStrategy causes a specified number of clusters to be
    updated concurrently until all clusters are updated.

    Attributes:
        max_concurrent (int):
            Optional. Maximum number of clusters to
            update the resource bundle on concurrently.
    """

    max_concurrent: int = proto.Field(
        proto.INT32,
        number=1,
    )


class RolloutStrategy(proto.Message):
    r"""RolloutStrategy defines different ways to rollout a resource
    bundle across a set of clusters.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        all_at_once (google.cloud.configdelivery_v1.types.AllAtOnceStrategy):
            AllAtOnceStrategy causes all clusters to be
            updated concurrently.

            This field is a member of `oneof`_ ``strategy``.
        rolling (google.cloud.configdelivery_v1.types.RollingStrategy):
            RollingStrategy causes a specified number of
            clusters to be updated concurrently until all
            clusters are updated.

            This field is a member of `oneof`_ ``strategy``.
    """

    all_at_once: "AllAtOnceStrategy" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="strategy",
        message="AllAtOnceStrategy",
    )
    rolling: "RollingStrategy" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="strategy",
        message="RollingStrategy",
    )


class RolloutStrategyInfo(proto.Message):
    r"""RolloutStrategyInfo represents the status of execution of
    different types of rollout strategies. Only the field
    corresponding to the rollout strategy specified at the rollout
    resource will be populated.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        all_at_once_strategy_info (google.cloud.configdelivery_v1.types.AllAtOnceStrategyInfo):
            AllAtOnceStrategyInfo represents the status
            of AllAtOnce rollout strategy execution.

            This field is a member of `oneof`_ ``strategy``.
        rolling_strategy_info (google.cloud.configdelivery_v1.types.RollingStrategyInfo):
            RollingStrategyInfo represents the status of
            Rolling rollout strategy execution.

            This field is a member of `oneof`_ ``strategy``.
    """

    all_at_once_strategy_info: "AllAtOnceStrategyInfo" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="strategy",
        message="AllAtOnceStrategyInfo",
    )
    rolling_strategy_info: "RollingStrategyInfo" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="strategy",
        message="RollingStrategyInfo",
    )


class AllAtOnceStrategyInfo(proto.Message):
    r"""AllAtOnceStrategyInfo represents the status of execution of
    AllAtOnce rollout strategy.

    Attributes:
        clusters (MutableSequence[google.cloud.configdelivery_v1.types.ClusterInfo]):
            Unordered list. resource bundle's deployment
            status for all targeted clusters.
    """

    clusters: MutableSequence["ClusterInfo"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ClusterInfo",
    )


class RollingStrategyInfo(proto.Message):
    r"""RollingStrategyInfo represents the status of execution of
    Rolling rollout strategy.

    Attributes:
        clusters (MutableSequence[google.cloud.configdelivery_v1.types.ClusterInfo]):
            Unordered list. resource bundle's deployment
            status for all targeted clusters.
    """

    clusters: MutableSequence["ClusterInfo"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ClusterInfo",
    )


class ListFleetPackagesRequest(proto.Message):
    r"""Message for requesting list of FleetPackage.

    Attributes:
        parent (str):
            Required. Parent value for
            ListFleetPackagesRequest.
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


class ListFleetPackagesResponse(proto.Message):
    r"""Message for response to listing FleetPackage

    Attributes:
        fleet_packages (MutableSequence[google.cloud.configdelivery_v1.types.FleetPackage]):
            The list of FleetPackage
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Unordered list. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    fleet_packages: MutableSequence["FleetPackage"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="FleetPackage",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetFleetPackageRequest(proto.Message):
    r"""Message for getting a FleetPackage

    Attributes:
        name (str):
            Required. Name of the resource
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateFleetPackageRequest(proto.Message):
    r"""Message for creating a FleetPackage

    Attributes:
        parent (str):
            Required. Value for parent.
        fleet_package_id (str):
            Required. Id of the requesting object If auto-generating Id
            server-side, remove this field and fleet_package_id from the
            method_signature of Create RPC
        fleet_package (google.cloud.configdelivery_v1.types.FleetPackage):
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
    fleet_package_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    fleet_package: "FleetPackage" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="FleetPackage",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateFleetPackageRequest(proto.Message):
    r"""Message for updating a FleetPackage

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the FleetPackage resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        fleet_package (google.cloud.configdelivery_v1.types.FleetPackage):
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
    fleet_package: "FleetPackage" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="FleetPackage",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteFleetPackageRequest(proto.Message):
    r"""Message for deleting a FleetPackage

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
        force (bool):
            Optional. If set to true, any rollouts for
            this FleetPackage will also be deleted.
            (Otherwise, the request will only work if the
            fleet package has no rollouts.)
        allow_missing (bool):
            Optional. If set to true, then deleting an
            already deleted or non existing FleetPackage
            will succeed.
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
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=4,
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
            cancelled successfully have
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


class Release(proto.Message):
    r"""``Release`` represents a versioned release containing kubernetes
    manifests.

    Attributes:
        name (str):
            Identifier. Name of the Release. Format is
            ``projects/{project}/locations/location}/resourceBundles/{resource_bundle}/release/[a-z][a-z0-9\-]{0,62}``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time ``Release`` was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time ``Release`` was last updated.
        labels (MutableMapping[str, str]):
            Optional. Labels as key value pairs.
        lifecycle (google.cloud.configdelivery_v1.types.Release.Lifecycle):
            Optional. lifecycle of the ``Release``.
        version (str):
            Required. version of the ``Release``. This must be v...
        publish_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time the ``Release`` was published.
        info (google.cloud.configdelivery_v1.types.ReleaseInfo):
            Optional. ``ResourceBundle`` Release extra information e.g.,
            artifact registry image path.
    """

    class Lifecycle(proto.Enum):
        r"""Lifecycle indicates the state of the ``Release``. A published
        release is immutable.

        Values:
            LIFECYCLE_UNSPECIFIED (0):
                indicates lifecycle has not been specified.
            DRAFT (1):
                indicates that the ``Release`` is being edited.
            PUBLISHED (2):
                indicates that the ``Release`` is now published (or
                released) and immutable.
        """

        LIFECYCLE_UNSPECIFIED = 0
        DRAFT = 1
        PUBLISHED = 2

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
    lifecycle: Lifecycle = proto.Field(
        proto.ENUM,
        number=5,
        enum=Lifecycle,
    )
    version: str = proto.Field(
        proto.STRING,
        number=6,
    )
    publish_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    info: "ReleaseInfo" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="ReleaseInfo",
    )


class Variant(proto.Message):
    r"""Variant represents the content of a ``ResourceBundle`` variant.

    Attributes:
        labels (MutableMapping[str, str]):
            Optional. labels to represent any metadata
            associated with the variant.
        resources (MutableSequence[str]):
            Required. Input only. Unordered list.
            resources contain the kubernetes manifests
            (YAMLs) for this variant.
        name (str):
            Identifier. Name follows format of
            projects/{project}/locations/{location}/resourceBundles/{resource_bundle}/releases/{release}/variants/{variant}
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Create time stamp
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Update time stamp
    """

    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=1,
    )
    resources: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    name: str = proto.Field(
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


class ListVariantsRequest(proto.Message):
    r"""Message for requesting list of Variants.

    Attributes:
        parent (str):
            Required. Parent value for
            ListVariantsRequest.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
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


class ListVariantsResponse(proto.Message):
    r"""Message for response to listing Variants

    Attributes:
        variants (MutableSequence[google.cloud.configdelivery_v1.types.Variant]):
            The list of Variants
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Unordered list. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    variants: MutableSequence["Variant"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Variant",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetVariantRequest(proto.Message):
    r"""Message for getting a Variant

    Attributes:
        name (str):
            Required. Name of the resource
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateVariantRequest(proto.Message):
    r"""Message for creating a Variant

    Attributes:
        parent (str):
            Required. Value for parent.
        variant_id (str):
            Required. Id of the requesting object
        variant (google.cloud.configdelivery_v1.types.Variant):
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
    variant_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    variant: "Variant" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Variant",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateVariantRequest(proto.Message):
    r"""Message for updating a Variant

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the Variant resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        variant (google.cloud.configdelivery_v1.types.Variant):
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
    variant: "Variant" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Variant",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteVariantRequest(proto.Message):
    r"""Message for deleting a Variant

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


class ReleaseInfo(proto.Message):
    r"""ReleaseInfo contains extra information about the ``ResourceBundle``
    release e.g., link to an artifact registry OCI image.

    Attributes:
        oci_image_path (str):
            Output only. path to the oci image the service uploads to on
            a ``Release`` creation.
        variant_oci_image_paths (MutableMapping[str, str]):
            Optional. per-variant paths to the oci images
            the service uploads on package release creation
    """

    oci_image_path: str = proto.Field(
        proto.STRING,
        number=1,
    )
    variant_oci_image_paths: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )


class ListReleasesRequest(proto.Message):
    r"""Message for requesting list of Releases.

    Attributes:
        parent (str):
            Required. Parent value for
            ListReleasesRequest.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
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


class ListReleasesResponse(proto.Message):
    r"""Message for response to listing Releases

    Attributes:
        releases (MutableSequence[google.cloud.configdelivery_v1.types.Release]):
            The list of Releases
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Unordered list. Locations that could not be
            reached.
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
    r"""Message for getting a Release

    Attributes:
        name (str):
            Required. Name of the resource
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateReleaseRequest(proto.Message):
    r"""Message for creating a Release

    Attributes:
        parent (str):
            Required. Value for parent.
        release_id (str):
            Required. Id of the requesting object If auto-generating Id
            server-side, remove this field and release_id from the
            method_signature of Create RPC
        release (google.cloud.configdelivery_v1.types.Release):
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


class UpdateReleaseRequest(proto.Message):
    r"""Message for updating a Release

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the Release resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        release (google.cloud.configdelivery_v1.types.Release):
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
    release: "Release" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Release",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteReleaseRequest(proto.Message):
    r"""Message for deleting a Release

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
        force (bool):
            Optional. If set to true, any variants of
            this release will also be deleted. (Otherwise,
            the request will only work if the release has no
            variants.)
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


class ListRolloutsRequest(proto.Message):
    r"""Message for requesting list of Rollouts

    Attributes:
        parent (str):
            Required. Parent value for
            ListRolloutsRequest
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


class ListRolloutsResponse(proto.Message):
    r"""Message for response to listing Rollouts

    Attributes:
        rollouts (MutableSequence[google.cloud.configdelivery_v1.types.Rollout]):
            The list of Rollouts
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Unordered list. Locations that could not be
            reached.
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
    r"""Message for getting a Rollout

    Attributes:
        name (str):
            Required. Name of the resource
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class RolloutInfo(proto.Message):
    r"""RolloutInfo represents the state of the ``FleetPackage`` at all the
    clusters the rollout is targeting.

    Attributes:
        state (google.cloud.configdelivery_v1.types.RolloutInfo.State):
            Output only. state contains the overall
            status of the Rollout.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the rollout started.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the rollout completed.
        message (str):
            Output only. Message containing additional
            information related to the rollout.
        rollout_strategy_info (google.cloud.configdelivery_v1.types.RolloutStrategyInfo):
            Output only. Rollout strategy info represents
            the status of execution of rollout strategy.
    """

    class State(proto.Enum):
        r"""State of the rollout

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified state.
            COMPLETED (1):
                Rollout completed.
            SUSPENDED (2):
                Rollout suspended.
            ABORTED (3):
                Rollout aborted.
            IN_PROGRESS (5):
                Rollout in progress.
            STALLED (6):
                Rollout stalled.
            CANCELLED (7):
                Rollout cancelled.
            ABORTING (8):
                Rollout aborting.
        """

        STATE_UNSPECIFIED = 0
        COMPLETED = 1
        SUSPENDED = 2
        ABORTED = 3
        IN_PROGRESS = 5
        STALLED = 6
        CANCELLED = 7
        ABORTING = 8

    state: State = proto.Field(
        proto.ENUM,
        number=1,
        enum=State,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    message: str = proto.Field(
        proto.STRING,
        number=6,
    )
    rollout_strategy_info: "RolloutStrategyInfo" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="RolloutStrategyInfo",
    )


class Rollout(proto.Message):
    r"""Rollout resource represents an instance of ``FleetPackage`` rollout
    operation across a fleet. This is a system generated resource and
    will be read only for end-users. It will be primarily used by the
    service to process the changes in the ``FleetPackage`` and other
    changes in the environment.

    Attributes:
        name (str):
            Identifier. Name of the Rollout. Format is
            ``projects/{project}/locations/{location}/fleetPackages/{fleet_package}/rollouts/[a-z][a-z0-9\-]{0,62}``.
        release (str):
            Reference to the ``Release`` being rolled out.
        rollout_strategy (google.cloud.configdelivery_v1.types.RolloutStrategy):
            Rollout strategy for rolling out ``FleetPackage`` to
            clusters.
        info (google.cloud.configdelivery_v1.types.RolloutInfo):
            Current details of the rollout.
        deletion_propagation_policy (google.cloud.configdelivery_v1.types.DeletionPropagationPolicy):
            Deletion propagation policy of the rollout.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the rollout was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the rollout was most
            recently updated.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    release: str = proto.Field(
        proto.STRING,
        number=2,
    )
    rollout_strategy: "RolloutStrategy" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="RolloutStrategy",
    )
    info: "RolloutInfo" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="RolloutInfo",
    )
    deletion_propagation_policy: "DeletionPropagationPolicy" = proto.Field(
        proto.ENUM,
        number=7,
        enum="DeletionPropagationPolicy",
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


class SuspendRolloutRequest(proto.Message):
    r"""Message for suspending a rollout.

    Attributes:
        name (str):
            Required. Name of the Rollout.
        reason (str):
            Optional. Reason for suspension.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    reason: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ResumeRolloutRequest(proto.Message):
    r"""Message for resuming a rollout.

    Attributes:
        name (str):
            Required. Name of the Rollout.
        reason (str):
            Optional. Reason for resuming the rollout.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    reason: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AbortRolloutRequest(proto.Message):
    r"""Message for aborting a rollout.

    Attributes:
        name (str):
            Required. Name of the Rollout.
        reason (str):
            Optional. Reason for aborting.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    reason: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
