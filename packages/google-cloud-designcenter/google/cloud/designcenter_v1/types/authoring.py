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
    assessment,
    deployment,
    enums,
    export,
    metadata_,
)
from google.cloud.designcenter_v1.types import parameters as gcd_parameters

__protobuf__ = proto.module(
    package="google.cloud.designcenter.v1",
    manifest={
        "ApplicationTemplate",
        "SerializedApplicationTemplate",
        "AppHubApplicationParameters",
        "InputVariableAlias",
        "SerializedComponent",
        "SerializedConnection",
        "SerializedPolicy",
        "ApplicationTemplateRevision",
        "ApplicationTemplateSystemRevision",
        "Component",
        "Connection",
        "SerializedProvider",
    },
)


class ApplicationTemplate(proto.Message):
    r"""Application template resource.

    Attributes:
        name (str):
            Identifier. Application template name.
        display_name (str):
            Optional. Application template display name.
        description (str):
            Optional. Application template description.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Application template creation
            timestamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Application template update
            timestamp.
        application_parameters (MutableSequence[google.cloud.designcenter_v1.types.Parameter]):
            Optional. Parameters to apply to all
            components in an application. You can specify
            projectID and region.
        iac_format (google.cloud.designcenter_v1.types.ApplicationTemplate.IACFormat):
            Output only. The IaC format of the
            application template.
        serialized_application_template (google.cloud.designcenter_v1.types.SerializedApplicationTemplate):
            Output only. The serialized application
            template.
        latest_revision (str):
            Output only. The latest application template
            revision.
        artifact_location (google.cloud.designcenter_v1.types.ArtifactLocation):
            Output only. Details of the location where
            the IaC for this ApplicationTemplate was last
            successfully exported.
        composition_type (google.cloud.designcenter_v1.types.ApplicationCompositionType):
            Optional. Immutable. The composition type of
            the applicationTemplate: STANDARD OR COMPOSITE.
            This is a create time only param.
        root_input_variables (MutableSequence[google.cloud.designcenter_v1.types.ComponentVariable]):
            Optional. Root level input variables of the
            application template.
        root_output_variables (MutableSequence[google.cloud.designcenter_v1.types.ComponentVariable]):
            Optional. Root level output variables of the
            application template.
        saas_runtime_context (google.cloud.designcenter_v1.types.SaaSRuntimeContext):
            Optional. SaaS runtime context for the
            application template.
        latest_system_revision_uri (str):
            Output only. The URI of the most recent System Revision
            generated for this ApplicationTemplate. This ID corresponds
            to the ``name`` field in the
            ApplicationTemplateSystemRevision resource.
        iac_source (google.cloud.designcenter_v1.types.IACSource):
            Output only. Indicates the IaC source format
            of this application template.
        template_metadata (google.cloud.designcenter_v1.types.TFBlueprintMetadata):
            Output only. The input output variables
            parsed from the imported terraform code.
        inputs_as_root_module_variables (bool):
            Optional. If true, exposes all inputs as root
            module variables. This is only supported for
            STANDARD composition type templates.
    """

    class IACFormat(proto.Enum):
        r"""The IaC format of the application template.

        Values:
            IAC_FORMAT_UNSPECIFIED (0):
                IaC format is unspecified.
            TERRAFORM (1):
                IaC format is Terraform.
            HELM (2):
                IaC format is Helm.
        """

        IAC_FORMAT_UNSPECIFIED = 0
        TERRAFORM = 1
        HELM = 2

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
    application_parameters: MutableSequence[gcd_parameters.Parameter] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=6,
            message=gcd_parameters.Parameter,
        )
    )
    iac_format: IACFormat = proto.Field(
        proto.ENUM,
        number=10,
        enum=IACFormat,
    )
    serialized_application_template: "SerializedApplicationTemplate" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="SerializedApplicationTemplate",
    )
    latest_revision: str = proto.Field(
        proto.STRING,
        number=12,
    )
    artifact_location: export.ArtifactLocation = proto.Field(
        proto.MESSAGE,
        number=14,
        message=export.ArtifactLocation,
    )
    composition_type: enums.ApplicationCompositionType = proto.Field(
        proto.ENUM,
        number=15,
        enum=enums.ApplicationCompositionType,
    )
    root_input_variables: MutableSequence[gcd_parameters.ComponentVariable] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=16,
            message=gcd_parameters.ComponentVariable,
        )
    )
    root_output_variables: MutableSequence[gcd_parameters.ComponentVariable] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=17,
            message=gcd_parameters.ComponentVariable,
        )
    )
    saas_runtime_context: gcd_parameters.SaaSRuntimeContext = proto.Field(
        proto.MESSAGE,
        number=18,
        message=gcd_parameters.SaaSRuntimeContext,
    )
    latest_system_revision_uri: str = proto.Field(
        proto.STRING,
        number=19,
    )
    iac_source: enums.IACSource = proto.Field(
        proto.ENUM,
        number=20,
        enum=enums.IACSource,
    )
    template_metadata: metadata_.TFBlueprintMetadata = proto.Field(
        proto.MESSAGE,
        number=21,
        message=metadata_.TFBlueprintMetadata,
    )
    inputs_as_root_module_variables: bool = proto.Field(
        proto.BOOL,
        number=22,
    )


class SerializedApplicationTemplate(proto.Message):
    r"""Serialized application template.

    Attributes:
        uri (str):
            Optional. The application template URI.
        display_name (str):
            Optional. The application template display
            name.
        description (str):
            Optional. The application template
            description.
        application_parameters (MutableSequence[google.cloud.designcenter_v1.types.Parameter]):
            Optional. Parameters to apply to all
            components in the application template.
        iac_format (google.cloud.designcenter_v1.types.ApplicationTemplate.IACFormat):
            Optional. The IaC format of the application
            template.
        components (MutableSequence[google.cloud.designcenter_v1.types.SerializedComponent]):
            Optional. The application template
            components.
        apphub_application_parameters (google.cloud.designcenter_v1.types.AppHubApplicationParameters):
            Optional. The App Hub application parameters.
        has_global_resource (bool):
            Output only. Whether the application template
            is compatible with regional scope.
        composition_type (google.cloud.designcenter_v1.types.ApplicationCompositionType):
            Output only. The composition type of the
            applicationTemplate: STANDARD OR COMPOSITE.
        root_input_variables (MutableSequence[google.cloud.designcenter_v1.types.ComponentVariable]):
            Output only. Root level input variables of
            the application template.
        root_output_variables (MutableSequence[google.cloud.designcenter_v1.types.ComponentVariable]):
            Output only. Root level output variables of
            the application template.
        saas_runtime_context (google.cloud.designcenter_v1.types.SaaSRuntimeContext):
            Optional. SaaS runtime context for the
            application template.
        serialized_policies (MutableSequence[google.cloud.designcenter_v1.types.SerializedPolicy]):
            Output only. Policies of the application
            template.
        providers (MutableSequence[google.cloud.designcenter_v1.types.SerializedProvider]):
            Optional. Custom provider configurations
            imported from IaC.
        custom_variables (MutableSequence[google.cloud.designcenter_v1.types.TerraformInput]):
            Optional. Custom variables imported from
            variables.tf.
        custom_tfvars (MutableSequence[google.cloud.designcenter_v1.types.Parameter]):
            Optional. Custom variable values imported
            from terraform.tfvars.
        inputs_as_root_module_variables (bool):
            Optional. If true, exposes all inputs as root
            module variables. This is only supported for
            STANDARD composition type templates.
    """

    uri: str = proto.Field(
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
    application_parameters: MutableSequence[gcd_parameters.Parameter] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message=gcd_parameters.Parameter,
        )
    )
    iac_format: "ApplicationTemplate.IACFormat" = proto.Field(
        proto.ENUM,
        number=7,
        enum="ApplicationTemplate.IACFormat",
    )
    components: MutableSequence["SerializedComponent"] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message="SerializedComponent",
    )
    apphub_application_parameters: "AppHubApplicationParameters" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="AppHubApplicationParameters",
    )
    has_global_resource: bool = proto.Field(
        proto.BOOL,
        number=11,
    )
    composition_type: enums.ApplicationCompositionType = proto.Field(
        proto.ENUM,
        number=12,
        enum=enums.ApplicationCompositionType,
    )
    root_input_variables: MutableSequence[gcd_parameters.ComponentVariable] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=13,
            message=gcd_parameters.ComponentVariable,
        )
    )
    root_output_variables: MutableSequence[gcd_parameters.ComponentVariable] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=14,
            message=gcd_parameters.ComponentVariable,
        )
    )
    saas_runtime_context: gcd_parameters.SaaSRuntimeContext = proto.Field(
        proto.MESSAGE,
        number=15,
        message=gcd_parameters.SaaSRuntimeContext,
    )
    serialized_policies: MutableSequence["SerializedPolicy"] = proto.RepeatedField(
        proto.MESSAGE,
        number=16,
        message="SerializedPolicy",
    )
    providers: MutableSequence["SerializedProvider"] = proto.RepeatedField(
        proto.MESSAGE,
        number=17,
        message="SerializedProvider",
    )
    custom_variables: MutableSequence[metadata_.TerraformInput] = proto.RepeatedField(
        proto.MESSAGE,
        number=18,
        message=metadata_.TerraformInput,
    )
    custom_tfvars: MutableSequence[gcd_parameters.Parameter] = proto.RepeatedField(
        proto.MESSAGE,
        number=19,
        message=gcd_parameters.Parameter,
    )
    inputs_as_root_module_variables: bool = proto.Field(
        proto.BOOL,
        number=20,
    )


class AppHubApplicationParameters(proto.Message):
    r"""App Hub application parameters.

    Attributes:
        application_id (str):
            Optional. The App Hub application ID.
        scope (google.cloud.apphub_v1.types.Scope):
            Optional. The App Hub application scope.
        attributes (google.cloud.apphub_v1.types.Attributes):
            Optional. The App Hub application attributes.
        location (str):
            Optional. The App Hub application location.
            Only used for applications with REGIONAL scope.
        host_project_id (str):
            Optional. The host project ID where the App
            Hub application is created.
    """

    application_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    scope: application.Scope = proto.Field(
        proto.MESSAGE,
        number=2,
        message=application.Scope,
    )
    attributes: gca_attributes.Attributes = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gca_attributes.Attributes,
    )
    location: str = proto.Field(
        proto.STRING,
        number=4,
    )
    host_project_id: str = proto.Field(
        proto.STRING,
        number=5,
    )


class InputVariableAlias(proto.Message):
    r"""Input variable alias mapping for a component in a composite
    application template.

    Attributes:
        variable (str):
            Required. Name of the input variable inside
            the component's underlying template or module.
        alias (str):
            Required. Alias for the variable name to be
            exposed at the root level of the composite
            template.
    """

    variable: str = proto.Field(
        proto.STRING,
        number=1,
    )
    alias: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SerializedComponent(proto.Message):
    r"""Serialized component.

    Attributes:
        uri (str):
            Optional. The component URI.
        shared_template_revision_uri (str):
            Optional. The shared template used to
            generate the component.
        parameters (MutableSequence[google.cloud.designcenter_v1.types.Parameter]):
            Optional. The component parameters.
        connections (MutableSequence[google.cloud.designcenter_v1.types.SerializedConnection]):
            Optional. The component connections.
        roles (MutableSequence[str]):
            Optional. IAM roles required by the service
            account to deploy the component.
        apis (MutableSequence[str]):
            Optional. APIs required to be enabled to deploy the
            component, in the form of "\*.googleapis.com".
        display_name (str):
            Optional. The component display name.
        connections_parameters (MutableSequence[google.cloud.designcenter_v1.types.ConnectionParameters]):
            Output only. The connection parameters of the
            component.
        component_parameter_schema (MutableSequence[google.cloud.designcenter_v1.types.ComponentParameterSchema]):
            Output only. The component parameter schema,
            which includes possible parameter values.
        application_info (google.cloud.designcenter_v1.types.ComponentApplicationInfo):
            Optional. The application associated with the
            component.
        use_as_root_module (bool):
            Optional. Whether the component is exported
            as a separate terraform root module in a
            composite application template. If this is
            false, then native components will be exported
            as a submodule of a separate terraform root
            module.
        input_variable_aliases (MutableSequence[google.cloud.designcenter_v1.types.InputVariableAlias]):
            Optional. Input variable aliases defined for
            this serialized component.
        application_template_revision_uri (str):
            Optional. The application template revision
            used to generate the component.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    shared_template_revision_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    parameters: MutableSequence[gcd_parameters.Parameter] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=gcd_parameters.Parameter,
    )
    connections: MutableSequence["SerializedConnection"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="SerializedConnection",
    )
    roles: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    apis: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=7,
    )
    connections_parameters: MutableSequence[gcd_parameters.ConnectionParameters] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=8,
            message=gcd_parameters.ConnectionParameters,
        )
    )
    component_parameter_schema: MutableSequence[
        gcd_parameters.ComponentParameterSchema
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message=gcd_parameters.ComponentParameterSchema,
    )
    application_info: deployment.ComponentApplicationInfo = proto.Field(
        proto.MESSAGE,
        number=10,
        message=deployment.ComponentApplicationInfo,
    )
    use_as_root_module: bool = proto.Field(
        proto.BOOL,
        number=11,
    )
    input_variable_aliases: MutableSequence["InputVariableAlias"] = proto.RepeatedField(
        proto.MESSAGE,
        number=12,
        message="InputVariableAlias",
    )
    application_template_revision_uri: str = proto.Field(
        proto.STRING,
        number=13,
    )


class SerializedConnection(proto.Message):
    r"""Serialized connection.

    Attributes:
        uri (str):
            Optional. The connection URI.
        destination_component_uri (str):
            Optional. The destination component URI used
            to generate the connection.
        source_component_parameters (MutableSequence[google.cloud.designcenter_v1.types.Parameter]):
            Optional. The parameters of the connection
            associated with the source component.
        destination_component_parameters (MutableSequence[google.cloud.designcenter_v1.types.Parameter]):
            Optional. The parameters of the connection
            associated with the destination component.
        dependency_type (google.cloud.designcenter_v1.types.ConnectionDependencyType):
            Output only. The type of the connection (data
            or logical).
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    destination_component_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    source_component_parameters: MutableSequence[gcd_parameters.Parameter] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message=gcd_parameters.Parameter,
        )
    )
    destination_component_parameters: MutableSequence[gcd_parameters.Parameter] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=5,
            message=gcd_parameters.Parameter,
        )
    )
    dependency_type: enums.ConnectionDependencyType = proto.Field(
        proto.ENUM,
        number=6,
        enum=enums.ConnectionDependencyType,
    )


class SerializedPolicy(proto.Message):
    r"""Serialized policy.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        policy_uri (str):
            Optional. URI of the policy.

            This field is a member of `oneof`_ ``source_uri``.
        policy_revision_uri (str):
            Optional. URI of the policy revision.

            This field is a member of `oneof`_ ``source_uri``.
        uri (str):
            Required. The uri of the policy in application template.
            Format:
            ``projects/{project}/locations/{location}/spaces/{space}/applicationTemplates/{application_template}/policies/{policy}``
        display_name (str):
            Optional. The serialized policy display name.
            The number of characters should be less than 128
            characters.
        description (str):
            Optional. The serialized policy description.
            At most 2048 characters.
        policy_type (google.cloud.designcenter_v1.types.SerializedPolicy.PolicyType):
            Required. Policy type will be used to
            determine the domain of the policy.
        apply_conditions (MutableSequence[google.cloud.designcenter_v1.types.ApplyCondition]):
            Optional. The serialized policy apply
            conditions.
        cloud_control_configs (MutableSequence[google.cloud.designcenter_v1.types.CloudControlConfig]):
            Optional. Stored parameter values grouped by
            cloud control.
    """

    class PolicyType(proto.Enum):
        r"""The serialized policy type.

        Values:
            POLICY_TYPE_UNSPECIFIED (0):
                Default.
            COMPLIANCE_FRAMEWORK (1):
                Compliance framework policy.
        """

        POLICY_TYPE_UNSPECIFIED = 0
        COMPLIANCE_FRAMEWORK = 1

    policy_uri: str = proto.Field(
        proto.STRING,
        number=5,
        oneof="source_uri",
    )
    policy_revision_uri: str = proto.Field(
        proto.STRING,
        number=6,
        oneof="source_uri",
    )
    uri: str = proto.Field(
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
    policy_type: PolicyType = proto.Field(
        proto.ENUM,
        number=4,
        enum=PolicyType,
    )
    apply_conditions: MutableSequence[assessment.ApplyCondition] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message=assessment.ApplyCondition,
    )
    cloud_control_configs: MutableSequence[gcd_parameters.CloudControlConfig] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=8,
            message=gcd_parameters.CloudControlConfig,
        )
    )


class ApplicationTemplateRevision(proto.Message):
    r"""Application template revision resource.

    Attributes:
        name (str):
            Identifier. The application template revision
            name.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The application template
            revision creation timestamp.
        snapshot (google.cloud.designcenter_v1.types.SerializedApplicationTemplate):
            Output only. The serialized application
            template.
        artifact_location (google.cloud.designcenter_v1.types.ArtifactLocation):
            Output only. Details of the location where
            the IaC for this ApplicationTemplate Revision
            was last successfully exported.
        template_metadata (google.cloud.designcenter_v1.types.TFBlueprintMetadata):
            Output only. The input output variables
            parsed from the imported terraform code.
        application_parameters (MutableSequence[google.cloud.designcenter_v1.types.Parameter]):
            Optional. The values provided for the input
            variables.
        iac_source (google.cloud.designcenter_v1.types.IACSource):
            Output only. Indicates the IaC source format
            of this application template revision.
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
    snapshot: "SerializedApplicationTemplate" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="SerializedApplicationTemplate",
    )
    artifact_location: export.ArtifactLocation = proto.Field(
        proto.MESSAGE,
        number=6,
        message=export.ArtifactLocation,
    )
    template_metadata: metadata_.TFBlueprintMetadata = proto.Field(
        proto.MESSAGE,
        number=21,
        message=metadata_.TFBlueprintMetadata,
    )
    application_parameters: MutableSequence[gcd_parameters.Parameter] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=22,
            message=gcd_parameters.Parameter,
        )
    )
    iac_source: enums.IACSource = proto.Field(
        proto.ENUM,
        number=23,
        enum=enums.IACSource,
    )


class ApplicationTemplateSystemRevision(proto.Message):
    r"""Application template system revision resource.

    Attributes:
        name (str):
            Identifier. The application template system revision name.
            Format:
            projects/{project}/locations/{location}/spaces/{space}/applicationTemplates/{application_template}/systemRevisions/{system_revision}
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The application template system
            revision creation timestamp.
        annotations (MutableMapping[str, str]):
            Output only. Annotations from agentic workflows or other
            system processes. For example: {
            "designcenter.googleapis.com/agent_id": "gemini-3-flash-v1",
            "designcenter.googleapis.com/llm_agent_summary": "Added a
            Cloud SQL instance",
            "designcenter.googleapis.com/external_ref_id":
            "trace-uuid-88921-xyz" }
        snapshot (google.cloud.designcenter_v1.types.SerializedApplicationTemplate):
            Output only. The serialized application
            template snapshot at this revision.
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
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )
    snapshot: "SerializedApplicationTemplate" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="SerializedApplicationTemplate",
    )


class Component(proto.Message):
    r"""Component resource.

    Attributes:
        name (str):
            Identifier. The component name.
        shared_template_revision_uri (str):
            Required. Immutable. The shared template used
            to generate the component.
        parameters (MutableSequence[google.cloud.designcenter_v1.types.Parameter]):
            Optional. The component parameters.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The component creation
            timestamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The component update timestamp.
        roles (MutableSequence[str]):
            Output only. IAM roles required by the
            service account to deploy the component.
        apis (MutableSequence[str]):
            Output only. APIs required to be enabled to deploy the
            component, in the form of "\*.googleapis.com".
        display_name (str):
            Optional. The component display name.
        connections_parameters (MutableSequence[google.cloud.designcenter_v1.types.ConnectionParameters]):
            Output only. The connection parameters of the
            component.
        component_parameter_schema (MutableSequence[google.cloud.designcenter_v1.types.ComponentParameterSchema]):
            Output only. The component parameter schema,
            which includes possible parameter values.
            values.
        application_info (google.cloud.designcenter_v1.types.ComponentApplicationInfo):
            Optional. The application associated with the
            component.
        use_as_root_module (bool):
            Optional. Whether the component is exported
            as a separate terraform root module in a
            composite application template. If this is
            false, then native components will be exported
            as a submodule of a separate terraform root
            module.
        input_variable_aliases (MutableSequence[google.cloud.designcenter_v1.types.InputVariableAlias]):
            Optional. Input variable aliases defined on
            this live component.
        application_template_revision_uri (str):
            Optional. The application template revision
            used to generate the component.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    shared_template_revision_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    parameters: MutableSequence[gcd_parameters.Parameter] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=gcd_parameters.Parameter,
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
    roles: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    apis: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=8,
    )
    connections_parameters: MutableSequence[gcd_parameters.ConnectionParameters] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=9,
            message=gcd_parameters.ConnectionParameters,
        )
    )
    component_parameter_schema: MutableSequence[
        gcd_parameters.ComponentParameterSchema
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message=gcd_parameters.ComponentParameterSchema,
    )
    application_info: deployment.ComponentApplicationInfo = proto.Field(
        proto.MESSAGE,
        number=11,
        message=deployment.ComponentApplicationInfo,
    )
    use_as_root_module: bool = proto.Field(
        proto.BOOL,
        number=12,
    )
    input_variable_aliases: MutableSequence["InputVariableAlias"] = proto.RepeatedField(
        proto.MESSAGE,
        number=13,
        message="InputVariableAlias",
    )
    application_template_revision_uri: str = proto.Field(
        proto.STRING,
        number=14,
    )


class Connection(proto.Message):
    r"""Connection resource.

    Attributes:
        name (str):
            Identifier. The connection name.
        destination_component_uri (str):
            Required. The destination component URI used to generate the
            connection. Format is
            ``projects/$project/locations/$location/spaces/$space/applicationTemplates/$application_template/components/$component``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The connection creation
            timestamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The connection update timestamp.
        source_component_parameters (MutableSequence[google.cloud.designcenter_v1.types.Parameter]):
            Optional. The parameters of the connection
            associated with the source component.
        destination_component_parameters (MutableSequence[google.cloud.designcenter_v1.types.Parameter]):
            Optional. The parameters of the connection
            associated with the destination component.
        dependency_type (google.cloud.designcenter_v1.types.ConnectionDependencyType):
            Output only. The type of the connection (data
            or logical).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    destination_component_uri: str = proto.Field(
        proto.STRING,
        number=2,
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
    source_component_parameters: MutableSequence[gcd_parameters.Parameter] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=6,
            message=gcd_parameters.Parameter,
        )
    )
    destination_component_parameters: MutableSequence[gcd_parameters.Parameter] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=7,
            message=gcd_parameters.Parameter,
        )
    )
    dependency_type: enums.ConnectionDependencyType = proto.Field(
        proto.ENUM,
        number=8,
        enum=enums.ConnectionDependencyType,
    )


class SerializedProvider(proto.Message):
    r"""Represents a serialized Terraform provider configuration.

    Attributes:
        provider (str):
            Required. Name of the provider (e.g., ``"google"``,
            ``"google-beta"``, ``"google-nightly"``).
        provider_alias (str):
            Optional. Optional alias for the provider
            (supports multi-region setups).
        parameters (MutableSequence[google.cloud.designcenter_v1.types.Parameter]):
            Optional. Configuration parameters of the
            provider. Reuses the standard Parameter message.
    """

    provider: str = proto.Field(
        proto.STRING,
        number=1,
    )
    provider_alias: str = proto.Field(
        proto.STRING,
        number=2,
    )
    parameters: MutableSequence[gcd_parameters.Parameter] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=gcd_parameters.Parameter,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
