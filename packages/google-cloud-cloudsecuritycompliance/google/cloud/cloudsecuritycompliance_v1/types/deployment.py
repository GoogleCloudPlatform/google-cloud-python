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

from google.cloud.cloudsecuritycompliance_v1.types import common

__protobuf__ = proto.module(
    package="google.cloud.cloudsecuritycompliance.v1",
    manifest={
        "DeploymentState",
        "FrameworkDeployment",
        "CloudControlDeployment",
        "TargetResourceConfig",
        "TargetResourceCreationConfig",
        "FolderCreationConfig",
        "ProjectCreationConfig",
        "CloudControlMetadata",
        "CreateFrameworkDeploymentRequest",
        "DeleteFrameworkDeploymentRequest",
        "GetFrameworkDeploymentRequest",
        "ListFrameworkDeploymentsRequest",
        "ListFrameworkDeploymentsResponse",
        "GetCloudControlDeploymentRequest",
        "ListCloudControlDeploymentsRequest",
        "ListCloudControlDeploymentsResponse",
        "CloudControlDeploymentReference",
        "FrameworkDeploymentReference",
    },
)


class DeploymentState(proto.Enum):
    r"""The state of the deployment resource.

    Values:
        DEPLOYMENT_STATE_UNSPECIFIED (0):
            Default value. This value is unused.
        DEPLOYMENT_STATE_VALIDATING (1):
            Validating the deployment.
        DEPLOYMENT_STATE_CREATING (2):
            Deployment is being created.
        DEPLOYMENT_STATE_DELETING (3):
            Deployment is being deleted.
        DEPLOYMENT_STATE_UPDATING (8):
            Deployment is being updated.
        DEPLOYMENT_STATE_FAILED (4):
            Deployment has failed. All the changes made
            by the deployment were successfully rolled back.
            You can retry or delete a deployment that's in
            this state.
        DEPLOYMENT_STATE_READY (5):
            Deployment is successful and ready to use.
        DEPLOYMENT_STATE_PARTIALLY_DEPLOYED (6):
            Deployment is partially deployed. All the
            cloud controls weren't deployed successfully.
            Retrying the operation resumes from the first
            failed step.
        DEPLOYMENT_STATE_PARTIALLY_DELETED (7):
            Deployment is partially deleted. All the
            cloud control deployments weren't deleted
            successfully. Retrying the operation resumes
            from the first failed step.
    """

    DEPLOYMENT_STATE_UNSPECIFIED = 0
    DEPLOYMENT_STATE_VALIDATING = 1
    DEPLOYMENT_STATE_CREATING = 2
    DEPLOYMENT_STATE_DELETING = 3
    DEPLOYMENT_STATE_UPDATING = 8
    DEPLOYMENT_STATE_FAILED = 4
    DEPLOYMENT_STATE_READY = 5
    DEPLOYMENT_STATE_PARTIALLY_DEPLOYED = 6
    DEPLOYMENT_STATE_PARTIALLY_DELETED = 7


class FrameworkDeployment(proto.Message):
    r"""Framework deployments represent the assignment of a framework
    to a target resource. Supported target resources are
    organizations, folders, and projects.

    Attributes:
        name (str):
            Identifier. The name of the framework deployment, in the
            format
            ``organizations/{organization}/locations/{location}/frameworkDeployments/{framework_deployment}``
            or
            ``projects/{project}/locations/{location}/frameworkDeployments/{framework_deployment}``.
            The only supported location is ``global``.
        target_resource_config (google.cloud.cloudsecuritycompliance_v1.types.TargetResourceConfig):
            Required. The details of the target resource
            that you want to deploy the framework to. You
            can specify an existing resource, or create a
            new one.
        computed_target_resource (str):
            Output only. The target resource to deploy the framework to,
            in one the following formats:

            - ``organizations/{organizationID}``
            - ``folders/{folderID}``
            - ``projects/{projectID}``
        framework (google.cloud.cloudsecuritycompliance_v1.types.FrameworkReference):
            Required. A reference to the framework that
            you're deploying.
        description (str):
            Optional. A user-provided description of the
            framework deployment.
        cloud_control_metadata (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.CloudControlMetadata]):
            Required. The deployment mode and parameters
            for each of the cloud controls in the framework.
            Every cloud control in the framework includes
            metadata.
        deployment_state (google.cloud.cloudsecuritycompliance_v1.types.DeploymentState):
            Output only. The state for the framework
            deployment.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the resource
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the resource
            last updated.
        etag (str):
            Optional. To prevent concurrent updates from overwriting
            each other, always provide the ``etag`` when you update a
            framework deployment. You can also provide the ``etag`` when
            you delete a framework deployment, to help ensure that
            you're deleting the intended version of the framework
            deployment.
        target_resource_display_name (str):
            Output only. The display name of the target
            resource.
        cloud_control_deployment_references (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.CloudControlDeploymentReference]):
            Output only. The references to the cloud control
            deployments. The reference includes all the cloud control
            deployments that are in the framework or in a cloud control
            group.

            For example, if a framework deployment deploys two cloud
            controls, ``cc-deployment-1`` and ``cc-deployment-2``, then
            the references are:

            ::

               {
                cloud_control_deployment_reference: {
                  cloud_control_deployment:
                  "organizations/{organization}/locations/{location}/cloudControlDeployments/cc-deployment-1"
                },
                cloud_control_deployment_reference: {
                 cloud_control_deployment:
                 "organizations/{organization}/locations/{location}/cloudControlDeployments/cc-deployment-2"
                }
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    target_resource_config: "TargetResourceConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="TargetResourceConfig",
    )
    computed_target_resource: str = proto.Field(
        proto.STRING,
        number=3,
    )
    framework: common.FrameworkReference = proto.Field(
        proto.MESSAGE,
        number=4,
        message=common.FrameworkReference,
    )
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    cloud_control_metadata: MutableSequence["CloudControlMetadata"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=6,
            message="CloudControlMetadata",
        )
    )
    deployment_state: "DeploymentState" = proto.Field(
        proto.ENUM,
        number=7,
        enum="DeploymentState",
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
    etag: str = proto.Field(
        proto.STRING,
        number=11,
    )
    target_resource_display_name: str = proto.Field(
        proto.STRING,
        number=13,
    )
    cloud_control_deployment_references: MutableSequence[
        "CloudControlDeploymentReference"
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=14,
        message="CloudControlDeploymentReference",
    )


class CloudControlDeployment(proto.Message):
    r"""A cloud control deployment represents the deployment of a particular
    cloud control on a target resource. Supported target resources are
    ``organizations/{organizationID}``, ``folders/{folderID}``, and
    ``projects/{projectID}``.

    Attributes:
        name (str):
            Identifier. The name for the cloud control deployment, in
            the format
            ``organizations/{organization}/locations/{location}/cloudControlDeployments/{cloud_control_deployment}``
            or
            ``projects/{project}/locations/{location}/cloudControlDeployments/{cloud_control_deployment}``.
            The only supported location is ``global``.
        target_resource_config (google.cloud.cloudsecuritycompliance_v1.types.TargetResourceConfig):
            Required. The details of the target resource
            that the cloud control is deployed You can use
            an existing target resource or create a new
            target.
        target_resource (str):
            Output only. The resource that the cloud control is deployed
            on, in one of the following formats:

            - ``organizations/{organizationID}``
            - ``folders/{folderID}``
            - ``projects/{projectID}``
        cloud_control_metadata (google.cloud.cloudsecuritycompliance_v1.types.CloudControlMetadata):
            Required. The deployment mode and parameters
            for the cloud control.
        description (str):
            Optional. A friendly description for the
            cloud control deployment.
        deployment_state (google.cloud.cloudsecuritycompliance_v1.types.DeploymentState):
            Output only. The state of the cloud control
            deployment.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the resource was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the resource was
            last updated.
        etag (str):
            Optional. To prevent concurrent updates from overwriting
            each other, provide the ``etag`` when you update a cloud
            control deployment. You can also provide the ``etag`` when
            you delete a cloud control deployment to help ensure that
            you're deleting the intended version of the deployment.
        parameter_substituted_cloud_control (google.cloud.cloudsecuritycompliance_v1.types.CloudControl):
            Output only. The cloud control after the
            given parameters are substituted.
        framework_deployment_references (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.FrameworkDeploymentReference]):
            Output only. The references to the framework
            deployments that this cloud control deployment
            is part of. A cloud control deployment can be
            part of multiple framework deployments.
        target_resource_display_name (str):
            Output only. The display name of the target
            resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    target_resource_config: "TargetResourceConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="TargetResourceConfig",
    )
    target_resource: str = proto.Field(
        proto.STRING,
        number=3,
    )
    cloud_control_metadata: "CloudControlMetadata" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="CloudControlMetadata",
    )
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    deployment_state: "DeploymentState" = proto.Field(
        proto.ENUM,
        number=6,
        enum="DeploymentState",
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
    parameter_substituted_cloud_control: common.CloudControl = proto.Field(
        proto.MESSAGE,
        number=10,
        message=common.CloudControl,
    )
    framework_deployment_references: MutableSequence["FrameworkDeploymentReference"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=11,
            message="FrameworkDeploymentReference",
        )
    )
    target_resource_display_name: str = proto.Field(
        proto.STRING,
        number=12,
    )


class TargetResourceConfig(proto.Message):
    r"""The name of the target resource or the configuration that's
    required to create a new target resource.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        existing_target_resource (str):
            Optional. The resource hierarchy node, in one of the
            following formats:

            - ``organizations/{organizationID}``
            - ``folders/{folderID}``
            - ``projects/{projectID}``

            This field is a member of `oneof`_ ``resource_config``.
        target_resource_creation_config (google.cloud.cloudsecuritycompliance_v1.types.TargetResourceCreationConfig):
            Optional. The details that are required to
            create a resource and use that resource as the
            target resource for deployment.

            This field is a member of `oneof`_ ``resource_config``.
    """

    existing_target_resource: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="resource_config",
    )
    target_resource_creation_config: "TargetResourceCreationConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="resource_config",
        message="TargetResourceCreationConfig",
    )


class TargetResourceCreationConfig(proto.Message):
    r"""The configuration that's required to create a target
    resource.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        folder_creation_config (google.cloud.cloudsecuritycompliance_v1.types.FolderCreationConfig):
            Optional. The configuration that's required
            to create a folder.

            This field is a member of `oneof`_ ``resource_creation_config``.
        project_creation_config (google.cloud.cloudsecuritycompliance_v1.types.ProjectCreationConfig):
            Optional. The configuration that's required
            to create a project.

            This field is a member of `oneof`_ ``resource_creation_config``.
    """

    folder_creation_config: "FolderCreationConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="resource_creation_config",
        message="FolderCreationConfig",
    )
    project_creation_config: "ProjectCreationConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="resource_creation_config",
        message="ProjectCreationConfig",
    )


class FolderCreationConfig(proto.Message):
    r"""The configuration that's required to create a folder to be
    used as the target resource for a deployment.

    Attributes:
        parent (str):
            Required. The parent of the folder, in the format
            ``organizations/{organizationID}`` or
            ``folders/{folderID}``.
        folder_display_name (str):
            Required. The display name of the folder.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    folder_display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ProjectCreationConfig(proto.Message):
    r"""The configuration that's required to create a project to be
    used as the target resource of a deployment.

    Attributes:
        parent (str):
            Required. The parent of the project, in the format
            ``organizations/{organizationID}`` or
            ``folders/{folderID}``.
        project_display_name (str):
            Required. The display name of the project.
        billing_account_id (str):
            Required. The billing account ID for the
            project.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project_display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    billing_account_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class CloudControlMetadata(proto.Message):
    r"""The enforcement mode and parameters of a cloud
    control deployment.

    Attributes:
        cloud_control_details (google.cloud.cloudsecuritycompliance_v1.types.CloudControlDetails):
            Required. The cloud control name and
            parameters.
        enforcement_mode (google.cloud.cloudsecuritycompliance_v1.types.EnforcementMode):
            Required. The enforcement mode of the cloud
            control.
    """

    cloud_control_details: common.CloudControlDetails = proto.Field(
        proto.MESSAGE,
        number=1,
        message=common.CloudControlDetails,
    )
    enforcement_mode: common.EnforcementMode = proto.Field(
        proto.ENUM,
        number=2,
        enum=common.EnforcementMode,
    )


class CreateFrameworkDeploymentRequest(proto.Message):
    r"""The request message for [CreateFrameworkDeployment][].

    Attributes:
        parent (str):
            Required. The parent resource of the framework deployment in
            the format
            ``organizations/{organization}/locations/{location}`` or
            ``projects/{project}/locations/{location}``. Only the global
            location is supported.
        framework_deployment_id (str):
            Optional. An identifier for the framework
            deployment that's unique in scope of the parent.
            If you don't specify a value, then a random UUID
            is generated.
        framework_deployment (google.cloud.cloudsecuritycompliance_v1.types.FrameworkDeployment):
            Required. The framework deployment that
            you're creating.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    framework_deployment_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    framework_deployment: "FrameworkDeployment" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="FrameworkDeployment",
    )


class DeleteFrameworkDeploymentRequest(proto.Message):
    r"""The request message for [DeleteFrameworkDeployment][].

    Attributes:
        name (str):
            Required. The name of the framework deployment that you want
            to delete, in the format
            ``organizations/{organization}/locations/{location}/frameworkDeployments/{framework_deployment}``
            or
            ``projects/{project}/locations/{location}/frameworkDeployments/{framework_deployment}``.
            The only supported location is ``global``.
        etag (str):
            Optional. An opaque identifier for the current version of
            the resource.

            If you provide this value, then it must match the existing
            value. If the values don't match, then the request fails
            with an [``ABORTED``][google.rpc.Code.ABORTED] error.

            If you omit this value, then the resource is deleted
            regardless of its current ``etag`` value.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetFrameworkDeploymentRequest(proto.Message):
    r"""The request message for [GetFrameworkDeployment][].

    Attributes:
        name (str):
            Required. The name of the framework deployment, in the
            format
            ``organizations/{organization}/locations/{location}/frameworkDeployments/{framework_deployment}``
            or
            ``projects/{project}/locations/{location}/frameworkDeployments/{framework_deployment}``.
            The only supported location is ``global``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListFrameworkDeploymentsRequest(proto.Message):
    r"""The request message for [ListFrameworkDeployments][].

    Attributes:
        parent (str):
            Required. The parent resource of the framework deployment,
            in the format
            ``organizations/{organization}/locations/{location}`` or
            ``projects/{project}/locations/{location}``. The only
            supported location is ``global``.
        page_size (int):
            Optional. The requested page size. The server
            might return fewer items than requested.
            If unspecified, the server picks an appropriate
            default.
        page_token (str):
            Optional. A token that identifies a page of
            results the server should return.
        filter (str):
            Optional. The filter to be applied on the resource, as
            defined by `AIP-160:
            Filtering <https://google.aip.dev/160>`__.
        order_by (str):
            Optional. The sort order for the results. The following
            values are supported:

            - ``name``
            - ``name desc``

            If you do not specify a value, then the results are not
            sorted.
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


class ListFrameworkDeploymentsResponse(proto.Message):
    r"""The response message for [ListFrameworkDeployments][].

    Attributes:
        framework_deployments (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.FrameworkDeployment]):
            The list of framework deployments.
        next_page_token (str):
            A token that identifies the next page of
            results that the server should return.
    """

    @property
    def raw_page(self):
        return self

    framework_deployments: MutableSequence["FrameworkDeployment"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="FrameworkDeployment",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetCloudControlDeploymentRequest(proto.Message):
    r"""The request message for [GetCloudControlDeployment][].

    Attributes:
        name (str):
            Required. The name for the cloud control deployment, in the
            format
            ``organizations/{organization}/locations/{location}/cloudControlDeployments/{cloud_control_deployment}``
            or
            ``projects/{project}/locations/{location}/cloudControlDeployments/{cloud_control_deployment}``.
            The only supported location is ``global``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListCloudControlDeploymentsRequest(proto.Message):
    r"""The request message for [ListCloudControlDeployments][].

    Attributes:
        parent (str):
            Required. The parent resource for the cloud control
            deployment, in the format
            ``organizations/{organization}/locations/{location}`` or
            ``projects/{project}/locations/{location}``. The only
            supported location is ``global``.
        page_size (int):
            Optional. The requested page size. The server
            might return fewer items than you requested.
            If unspecified, the server picks an appropriate
            default.
        page_token (str):
            Optional. A token that identifies the page of
            results that the server should return.
        filter (str):
            Optional. The filter to apply on the resource, as defined by
            `AIP-160: Filtering <https://google.aip.dev/160>`__.
        order_by (str):
            Optional. The sort order for the results. The following
            values are supported:

            - ``name``
            - ``name desc``

            If you do not specify a value, then the results are not
            sorted.
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


class ListCloudControlDeploymentsResponse(proto.Message):
    r"""The response message for [ListCloudControlDeployments][].

    Attributes:
        cloud_control_deployments (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.CloudControlDeployment]):
            The list of cloud control deployments.
        next_page_token (str):
            A token that identifies the next page of
            results that the server should return.
    """

    @property
    def raw_page(self):
        return self

    cloud_control_deployments: MutableSequence["CloudControlDeployment"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="CloudControlDeployment",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CloudControlDeploymentReference(proto.Message):
    r"""The reference to a cloud control deployment.

    Attributes:
        cloud_control_deployment (str):
            Output only. The name of the CloudControlDeployment. The
            format is
            ``organizations/{organization}/locations/{location}/cloudControlDeployments/{cloud_control_deployment}``
            or
            ``projects/{project}/locations/{location}/cloudControlDeployments/{cloud_control_deployment}``.
            The only supported location is ``global``.
    """

    cloud_control_deployment: str = proto.Field(
        proto.STRING,
        number=1,
    )


class FrameworkDeploymentReference(proto.Message):
    r"""The reference to a framework deployment.

    Attributes:
        framework_deployment (str):
            Output only. The name of the framework deployment, in the
            format
            ``organizations/{organization}/locations/{location}/frameworkDeployments/{framework_deployment}``
            or
            ``projects/{project}/locations/{location}/frameworkDeployments/{framework_deployment}``.
            The only supported location is ``global``.
        framework_reference (google.cloud.cloudsecuritycompliance_v1.types.FrameworkReference):
            Optional. The reference to the framework that this
            deployment is for. For example:

            ::

               {
                 framework:
                 "organizations/{organization}/locations/{location}/frameworks/{framework}",
                 major_revision_id: 1
               }

            The only supported location is ``global``.
        framework_display_name (str):
            Optional. The display name of the framework
            that this framework deployment is for.
    """

    framework_deployment: str = proto.Field(
        proto.STRING,
        number=1,
    )
    framework_reference: common.FrameworkReference = proto.Field(
        proto.MESSAGE,
        number=2,
        message=common.FrameworkReference,
    )
    framework_display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
