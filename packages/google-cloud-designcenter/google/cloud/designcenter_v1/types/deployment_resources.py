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
from google.cloud.apphub_v1.types import application
from google.cloud.apphub_v1.types import attributes as gca_attributes

from google.cloud.designcenter_v1.types import (
    authoring,
    deployment,
    enums,
    export,
    metadata_,
    parameters,
)

__protobuf__ = proto.module(
    package="google.cloud.designcenter.v1",
    manifest={
        "Application",
    },
)


class Application(proto.Message):
    r"""Represents the application resource.

    Attributes:
        name (str):
            Identifier. The name of the application.
            Format:

            projects/{project}/locations/{location}/spaces/{space}/applications/{application}
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create timestamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Update timestamp.
        source (google.cloud.designcenter_v1.types.DeploymentSource):
            Required. The application deployment source.
        app_parameters (MutableSequence[google.cloud.designcenter_v1.types.Parameter]):
            Optional. A list of parameters to attach to
            the deployment source object, which is a catalog
            entry or application template snapshot.
        component_parameters (MutableSequence[google.cloud.designcenter_v1.types.ComponentParameters]):
            Optional. A list of component parameters to
            associate with the application.
        service_account (str):
            Optional. Your own service account that you
            use to deploy an application.
        display_name (str):
            Optional. Display name of the application.
        description (str):
            Optional. Description of the application.
        attributes (google.cloud.apphub_v1.types.Attributes):
            Optional. Attributes of the application.
        scope (google.cloud.apphub_v1.types.Scope):
            Required. Scope of the application.
        import_existing_resources (bool):
            Optional. Import existing resources into the
            application.
        preview_reference (str):
            Output only. Preview reference for the
            application.
        deployment_revision (str):
            Output only. [Output only] Optional Infra Manager deployment
            Id with revision
        apphub_application (str):
            Output only. The App Hub App associated with
            the application.
        serialized_application_template (google.cloud.designcenter_v1.types.SerializedApplicationTemplate):
            Output only. [Output only] Serialized application template.
        state (google.cloud.designcenter_v1.types.Application.State):
            Output only. Deployment state of the
            application.
        deployment_metadata (google.cloud.designcenter_v1.types.DeploymentMetadata):
            Output only. Deployment metadata of the
            application.
        project_parameters (MutableSequence[google.cloud.designcenter_v1.types.ProjectParameters]):
            Output only. List of project parameters for
            the application.
        deployment_region (str):
            Optional. The region where the application is
            deployed.
        updated_template_revision (google.cloud.designcenter_v1.types.UpdatedTemplateRevision):
            Output only. The updated template revision
            because of which the application is outdated.
        deployment_project (str):
            Optional. Deployment project of the
            application.
        connection_configs (MutableSequence[google.cloud.designcenter_v1.types.ConnectionConfig]):
            Optional. Connection configuration for the
            application.
        artifact_location (google.cloud.designcenter_v1.types.ArtifactLocation):
            Output only. Details of the location where
            the IaC for this application was last
            successfully exported.
        type_ (google.cloud.designcenter_v1.types.ApplicationType):
            Optional. The type of the application.
        deployment_target (google.cloud.designcenter_v1.types.DeploymentTarget):
            Optional. The deployment target of the
            application.
        composition_type (google.cloud.designcenter_v1.types.ApplicationCompositionType):
            Output only. The composition type of the
            application: STANDARD OR COMPOSITE.
        composite_application_parameters (google.cloud.designcenter_v1.types.CompositeApplicationParameters):
            Optional. Parameters that are required for
            composite applications.
        deployment_group_metadata (google.cloud.designcenter_v1.types.DeploymentGroupMetadata):
            Output only. The deployment group metadata of
            the application. This is applicable only for
            composite applications.
        params_update_strategy (google.cloud.designcenter_v1.types.Application.UpdateStrategy):
            Optional. Specifies the strategy to use when
            updating the application parameters while
            updating the application template revision.
        roles_apis_config (MutableSequence[google.cloud.designcenter_v1.types.RolesAndApisConfig]):
            Optional. Project-specific configurations
            required for application deployment, including
            IAM roles and APIs. The list can contain up to
            100 items.
        template_metadata (google.cloud.designcenter_v1.types.TFBlueprintMetadata):
            Output only. The input output variables
            parsed from the imported terraform code.
        iac_source (google.cloud.designcenter_v1.types.IACSource):
            Output only. Indicates the IaC source format
            of this application.
    """

    class State(proto.Enum):
        r"""Possible values for the application deployment state.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified application deployment state.
            DRAFT (1):
                Application is in draft.
            CREATING_DEPLOYMENT (2):
                New application deployment is in progress.
            UPDATING_DEPLOYMENT (3):
                Update application deployment is in progress.
            DELETING (4):
                Delete application deployment is in progress.
            DEPLOYED (5):
                Application deployment is completed.
            DELETED (6):
                Application deployment is deleted.
            FAILED (7):
                Application deployment is failed.
            DEPLOYING (8):
                Application deployment is in progress.
        """

        STATE_UNSPECIFIED = 0
        DRAFT = 1
        CREATING_DEPLOYMENT = 2
        UPDATING_DEPLOYMENT = 3
        DELETING = 4
        DEPLOYED = 5
        DELETED = 6
        FAILED = 7
        DEPLOYING = 8

    class UpdateStrategy(proto.Enum):
        r"""Specifies the strategy to use when updating an application.

        Values:
            UPDATE_STRATEGY_UNSPECIFIED (0):
                Retains the existing value for the field.
            REPLACE (2):
                Replaces the existing field values with the
                provided ones.
        """

        UPDATE_STRATEGY_UNSPECIFIED = 0
        REPLACE = 2

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
    source: deployment.DeploymentSource = proto.Field(
        proto.MESSAGE,
        number=4,
        message=deployment.DeploymentSource,
    )
    app_parameters: MutableSequence[parameters.Parameter] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=parameters.Parameter,
    )
    component_parameters: MutableSequence[deployment.ComponentParameters] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=10,
            message=deployment.ComponentParameters,
        )
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=11,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=12,
    )
    description: str = proto.Field(
        proto.STRING,
        number=13,
    )
    attributes: gca_attributes.Attributes = proto.Field(
        proto.MESSAGE,
        number=14,
        message=gca_attributes.Attributes,
    )
    scope: application.Scope = proto.Field(
        proto.MESSAGE,
        number=15,
        message=application.Scope,
    )
    import_existing_resources: bool = proto.Field(
        proto.BOOL,
        number=16,
    )
    preview_reference: str = proto.Field(
        proto.STRING,
        number=17,
    )
    deployment_revision: str = proto.Field(
        proto.STRING,
        number=18,
    )
    apphub_application: str = proto.Field(
        proto.STRING,
        number=19,
    )
    serialized_application_template: authoring.SerializedApplicationTemplate = (
        proto.Field(
            proto.MESSAGE,
            number=20,
            message=authoring.SerializedApplicationTemplate,
        )
    )
    state: State = proto.Field(
        proto.ENUM,
        number=21,
        enum=State,
    )
    deployment_metadata: deployment.DeploymentMetadata = proto.Field(
        proto.MESSAGE,
        number=22,
        message=deployment.DeploymentMetadata,
    )
    project_parameters: MutableSequence[deployment.ProjectParameters] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=23,
            message=deployment.ProjectParameters,
        )
    )
    deployment_region: str = proto.Field(
        proto.STRING,
        number=24,
    )
    updated_template_revision: deployment.UpdatedTemplateRevision = proto.Field(
        proto.MESSAGE,
        number=26,
        message=deployment.UpdatedTemplateRevision,
    )
    deployment_project: str = proto.Field(
        proto.STRING,
        number=27,
    )
    connection_configs: MutableSequence[deployment.ConnectionConfig] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=28,
            message=deployment.ConnectionConfig,
        )
    )
    artifact_location: export.ArtifactLocation = proto.Field(
        proto.MESSAGE,
        number=29,
        message=export.ArtifactLocation,
    )
    type_: enums.ApplicationType = proto.Field(
        proto.ENUM,
        number=30,
        enum=enums.ApplicationType,
    )
    deployment_target: deployment.DeploymentTarget = proto.Field(
        proto.MESSAGE,
        number=31,
        message=deployment.DeploymentTarget,
    )
    composition_type: enums.ApplicationCompositionType = proto.Field(
        proto.ENUM,
        number=32,
        enum=enums.ApplicationCompositionType,
    )
    composite_application_parameters: deployment.CompositeApplicationParameters = (
        proto.Field(
            proto.MESSAGE,
            number=33,
            message=deployment.CompositeApplicationParameters,
        )
    )
    deployment_group_metadata: deployment.DeploymentGroupMetadata = proto.Field(
        proto.MESSAGE,
        number=34,
        message=deployment.DeploymentGroupMetadata,
    )
    params_update_strategy: UpdateStrategy = proto.Field(
        proto.ENUM,
        number=35,
        enum=UpdateStrategy,
    )
    roles_apis_config: MutableSequence[deployment.RolesAndApisConfig] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=36,
            message=deployment.RolesAndApisConfig,
        )
    )
    template_metadata: metadata_.TFBlueprintMetadata = proto.Field(
        proto.MESSAGE,
        number=37,
        message=metadata_.TFBlueprintMetadata,
    )
    iac_source: enums.IACSource = proto.Field(
        proto.ENUM,
        number=38,
        enum=enums.IACSource,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
