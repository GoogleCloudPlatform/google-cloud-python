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
import proto  # type: ignore

from google.cloud.designcenter_v1.types import enums

__protobuf__ = proto.module(
    package="google.cloud.designcenter.v1",
    manifest={
        "TFBlueprintMetadata",
        "ProviderVersion",
        "TerraformInput",
        "TerraformVariableValidation",
        "TerraformInputConnections",
        "TerraformOutput",
        "TerraformBlueprintUiMetadata",
        "AlternateDefault",
        "ValueLabel",
        "DisplayVariableToggle",
        "TerraformUiInput",
        "TerraformUiInputDisplayVariable",
        "TerraformUiOutput",
        "TerraformUiOutputDisplay",
        "HelmChartMetadata",
        "HelmChartInput",
        "HelmChartOutput",
        "MetadataInput",
        "MetadataInputSpec",
        "TemplateInfo",
        "IacFormatInfo",
        "TemplateSchema",
        "TemplateVariable",
        "TemplateConnections",
        "ConnectionSource",
        "ConnectionSpec",
        "TemplateRequirements",
        "TemplateRoles",
        "TemplateUi",
        "TemplateUiInput",
        "TemplateUiOutput",
        "TemplateUiOutputDisplayVariable",
        "DisplayVariable",
        "ValueLabelInput",
        "AlternateDefaultInput",
        "LogicalProduct",
        "InferredMetadata",
        "ResourceType",
        "TerraformModuleMetadata",
        "ModuleDetails",
        "ModuleInput",
        "ModuleOutput",
        "ModuleDependency",
        "ProviderDependency",
        "ModuleResource",
        "ListCatalogTemplateRevisionMetadataResponse",
        "CatalogTemplateRevisionMetadata",
    },
)


class TFBlueprintMetadata(proto.Message):
    r"""Terraform input and output metadata.

    Attributes:
        terraform_input (MutableSequence[google.cloud.designcenter_v1.types.TerraformInput]):
            Output only. Terraform inputs.
        terraform_output (MutableSequence[google.cloud.designcenter_v1.types.TerraformOutput]):
            Output only. Terraform outputs.
        apis (MutableSequence[str]):
            Output only. APIs that must be enabled to
            deploy the template, in the form of
            "compute.googleapis.com".
        roles (MutableSequence[str]):
            Output only. IAM roles required by the
            service account deploying the template, in the
            form of "roles/compute.admin".
        deployment_duration (google.protobuf.duration_pb2.Duration):
            Optional. The time estimate for deploying the
            blueprint.
        icon_uri (str):
            Output only. The icon URI for the blueprint.
        connections (MutableSequence[google.cloud.designcenter_v1.types.TerraformInputConnections]):
            Output only. Union of all the Terraform input
            connections.
        ui_metadata (google.cloud.designcenter_v1.types.TerraformBlueprintUiMetadata):
            Output only. UI metadata for the blueprint.
        provider_versions (MutableSequence[google.cloud.designcenter_v1.types.ProviderVersion]):
            Output only. Provider versions required to
            deploy the blueprint.
    """

    terraform_input: MutableSequence["TerraformInput"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="TerraformInput",
    )
    terraform_output: MutableSequence["TerraformOutput"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="TerraformOutput",
    )
    apis: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    roles: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    deployment_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=6,
        message=duration_pb2.Duration,
    )
    icon_uri: str = proto.Field(
        proto.STRING,
        number=9,
    )
    connections: MutableSequence["TerraformInputConnections"] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message="TerraformInputConnections",
    )
    ui_metadata: "TerraformBlueprintUiMetadata" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="TerraformBlueprintUiMetadata",
    )
    provider_versions: MutableSequence["ProviderVersion"] = proto.RepeatedField(
        proto.MESSAGE,
        number=12,
        message="ProviderVersion",
    )


class ProviderVersion(proto.Message):
    r"""ProviderVersion defines the required version for a provider.

    Attributes:
        source (str):
            Output only. The provider source in the format:
            [hostname]/[namespace]/[name]. Hostname is optional, and
            defaults to the Terraform registry.
        version (str):
            Output only. Version constraint string.
    """

    source: str = proto.Field(
        proto.STRING,
        number=1,
    )
    version: str = proto.Field(
        proto.STRING,
        number=2,
    )


class TerraformInput(proto.Message):
    r"""Terraform inputs.

    Attributes:
        terraform_input_variable (str):
            Output only. Input variable name present in
            Terraform.
        description (str):
            Output only. Terraform variable description.
        type_ (str):
            Output only. The Terraform input data type.
        default_value (google.protobuf.struct_pb2.Value):
            Output only. The default value of the
            Terraform input variable.
        connections (MutableSequence[google.cloud.designcenter_v1.types.TerraformInputConnections]):
            Output only. Terraform input connections.
        is_required (bool):
            Output only. Indicates if input is required.
        sensitive (bool):
            Optional. Indicates if the Terraform variable
            is sensitive.
        validation_rules (MutableSequence[google.cloud.designcenter_v1.types.TerraformVariableValidation]):
            Optional. Optional validation rules defined
            on the variable.
    """

    terraform_input_variable: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=3,
    )
    default_value: struct_pb2.Value = proto.Field(
        proto.MESSAGE,
        number=4,
        message=struct_pb2.Value,
    )
    connections: MutableSequence["TerraformInputConnections"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="TerraformInputConnections",
    )
    is_required: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    sensitive: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    validation_rules: MutableSequence["TerraformVariableValidation"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=8,
            message="TerraformVariableValidation",
        )
    )


class TerraformVariableValidation(proto.Message):
    r"""Represents a custom validation rule defined on a Terraform
    input variable.

    Attributes:
        condition (str):
            Optional. The HCL expression for the validation condition
            (e.g., "length(var.image_id) > 4").
        error_message (str):
            Optional. The error message displayed when
            the condition is false.
    """

    condition: str = proto.Field(
        proto.STRING,
        number=1,
    )
    error_message: str = proto.Field(
        proto.STRING,
        number=2,
    )


class TerraformInputConnections(proto.Message):
    r"""TerraformInputConnections

    Attributes:
        cft_template_uri (str):
            Output only. List of other templates that can
            be connected to.
        cft_template_version (str):
            Output only. Version of the other template
            that can be connected to.
        output_var (str):
            Output only. Output variable name present in
            Terraform.
        input_path (str):
            Output only. Input path of the other template
            that can be connected to.
    """

    cft_template_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cft_template_version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    output_var: str = proto.Field(
        proto.STRING,
        number=3,
    )
    input_path: str = proto.Field(
        proto.STRING,
        number=4,
    )


class TerraformOutput(proto.Message):
    r"""Terraform outputs.

    Attributes:
        type_ (google.protobuf.struct_pb2.Value):
            Output only. Type of Terraform output.
        terraform_output_variable (str):
            Output only. Output variable name present in
            Terraform.
        description (str):
            Output only. Description of the Terraform
            varaiable.
    """

    type_: struct_pb2.Value = proto.Field(
        proto.MESSAGE,
        number=1,
        message=struct_pb2.Value,
    )
    terraform_output_variable: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )


class TerraformBlueprintUiMetadata(proto.Message):
    r"""Terraform blueprint UI metadata.

    Attributes:
        terraform_ui_input (google.cloud.designcenter_v1.types.TerraformUiInput):
            Output only. Terraform UI inputs.
        terraform_ui_output (google.cloud.designcenter_v1.types.TerraformUiOutput):
            Output only. Terraform UI outputs.
    """

    terraform_ui_input: "TerraformUiInput" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="TerraformUiInput",
    )
    terraform_ui_output: "TerraformUiOutput" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="TerraformUiOutput",
    )


class AlternateDefault(proto.Message):
    r"""Alternate default for a UI input.

    Attributes:
        type_ (google.cloud.designcenter_v1.types.DisplayVariableAlternateType):
            Output only. Type of alternate default.
        value (google.protobuf.struct_pb2.Value):
            Output only. Value of the alternate default.
    """

    type_: enums.DisplayVariableAlternateType = proto.Field(
        proto.ENUM,
        number=1,
        enum=enums.DisplayVariableAlternateType,
    )
    value: struct_pb2.Value = proto.Field(
        proto.MESSAGE,
        number=2,
        message=struct_pb2.Value,
    )


class ValueLabel(proto.Message):
    r"""Value label for a UI input.

    Attributes:
        value (str):
            Output only. Value of the enum.
        label (str):
            Output only. Label of the enum.
    """

    value: str = proto.Field(
        proto.STRING,
        number=1,
    )
    label: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DisplayVariableToggle(proto.Message):
    r"""Display variable toggle.

    Attributes:
        variable (str):
            Output only. The name of the variable used to
            toggle the display of another variable.
        variable_values (MutableSequence[str]):
            Output only. The value of the variable used
            to toggle the display of another variable.
        variable_type (google.cloud.designcenter_v1.types.DisplayVariableToggle.ToggleVariableType):
            Output only. The type of the variable used to
            toggle the display of another variable.
    """

    class ToggleVariableType(proto.Enum):
        r"""Toogle variable type enum.

        Values:
            TOGGLE_VARIABLE_TYPE_UNSPECIFIED (0):
                Default
            TOGGLE_VARIABLE_TYPE_BOOLEAN (1):
                Boolean
            TOGGLE_VARIABLE_TYPE_STRING (2):
                String
            TOGGLE_VARIABLE_TYPE_INTEGER (3):
                Integer
        """

        TOGGLE_VARIABLE_TYPE_UNSPECIFIED = 0
        TOGGLE_VARIABLE_TYPE_BOOLEAN = 1
        TOGGLE_VARIABLE_TYPE_STRING = 2
        TOGGLE_VARIABLE_TYPE_INTEGER = 3

    variable: str = proto.Field(
        proto.STRING,
        number=1,
    )
    variable_values: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    variable_type: ToggleVariableType = proto.Field(
        proto.ENUM,
        number=3,
        enum=ToggleVariableType,
    )


class TerraformUiInput(proto.Message):
    r"""Terraform blueprint UI input.

    Attributes:
        terraform_ui_inputs (MutableMapping[str, google.cloud.designcenter_v1.types.TerraformUiInputDisplayVariable]):
            Output only. Terraform UI inputs.
    """

    terraform_ui_inputs: MutableMapping[str, "TerraformUiInputDisplayVariable"] = (
        proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=1,
            message="TerraformUiInputDisplayVariable",
        )
    )


class TerraformUiInputDisplayVariable(proto.Message):
    r"""Terraform blueprint UI input display variable.

    Attributes:
        display_name (str):
            Output only. Display name of the input.
        title (str):
            Output only. Title of the input.
        alternate_defaults (MutableSequence[google.cloud.designcenter_v1.types.AlternateDefault]):
            Output only. Alternate defaults for the
            input.
        regex_validation (str):
            Output only. Regex based validation rules for
            the variable.
        min_ (float):
            Output only. Minimum value for numeric types.
        max_ (float):
            Output only. Maximum value for numeric types.
        validation (str):
            Output only. Text describing the validation
            rules for the property. Typically shown after an
            invalid input. Optional. UTF-8 text. No markup.
            At most 128 characters.
        enum_value_labels (MutableSequence[google.cloud.designcenter_v1.types.ValueLabel]):
            Output only. Labels for enum values.
            Values must be UTF-8 text with no markup, and at
            most 64 characters.
        level (int):
            Output only. Indicates the "advanced" level
            of the input property. Level 0 (default) will
            always be shown. Level 1 corresponds to one
            expansion (user clicks "show advanced options"
            or "more options"). Higher levels correspond to
            further expansions, or they may be collapsed to
            level 1 by the UI implementation.
            Optional.
        subtext (str):
            Output only. Property subtext, displayed
            below the title.
        toggle_using_variables (MutableSequence[google.cloud.designcenter_v1.types.DisplayVariableToggle]):
            Output only. Variables used to toggle the
            display of another variable.
        properties (MutableMapping[str, google.cloud.designcenter_v1.types.TerraformUiInputDisplayVariable]):
            Output only. A map that defines all fields of
            the input variable.
    """

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    title: str = proto.Field(
        proto.STRING,
        number=2,
    )
    alternate_defaults: MutableSequence["AlternateDefault"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="AlternateDefault",
    )
    regex_validation: str = proto.Field(
        proto.STRING,
        number=5,
    )
    min_: float = proto.Field(
        proto.FLOAT,
        number=6,
    )
    max_: float = proto.Field(
        proto.FLOAT,
        number=7,
    )
    validation: str = proto.Field(
        proto.STRING,
        number=8,
    )
    enum_value_labels: MutableSequence["ValueLabel"] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="ValueLabel",
    )
    level: int = proto.Field(
        proto.INT32,
        number=10,
    )
    subtext: str = proto.Field(
        proto.STRING,
        number=11,
    )
    toggle_using_variables: MutableSequence["DisplayVariableToggle"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=12,
            message="DisplayVariableToggle",
        )
    )
    properties: MutableMapping[str, "TerraformUiInputDisplayVariable"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=13,
        message="TerraformUiInputDisplayVariable",
    )


class TerraformUiOutput(proto.Message):
    r"""Terraform blueprint UI output.

    Attributes:
        output_message (str):
            Output only. Message to be displayed in the
            UI.
        terraform_ui_outputs (MutableMapping[str, google.cloud.designcenter_v1.types.TerraformUiOutputDisplay]):
            Output only. Visibility of the output.
    """

    output_message: str = proto.Field(
        proto.STRING,
        number=1,
    )
    terraform_ui_outputs: MutableMapping[str, "TerraformUiOutputDisplay"] = (
        proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=2,
            message="TerraformUiOutputDisplay",
        )
    )


class TerraformUiOutputDisplay(proto.Message):
    r"""Terraform blueprint UI output display.

    Attributes:
        visibility (google.cloud.designcenter_v1.types.DisplayVariableVisibility):
            Output only. Visibility of the output.
    """

    visibility: enums.DisplayVariableVisibility = proto.Field(
        proto.ENUM,
        number=1,
        enum=enums.DisplayVariableVisibility,
    )


class HelmChartMetadata(proto.Message):
    r"""Helm Chart metadata.

    Attributes:
        helm_input (MutableSequence[google.cloud.designcenter_v1.types.HelmChartInput]):
            Output only. Helm Chart inputs.
        helm_output (MutableSequence[google.cloud.designcenter_v1.types.HelmChartOutput]):
            Output only. Helm Chart outputs.
    """

    helm_input: MutableSequence["HelmChartInput"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="HelmChartInput",
    )
    helm_output: MutableSequence["HelmChartOutput"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="HelmChartOutput",
    )


class HelmChartInput(proto.Message):
    r"""Helm Chart inputs.
    Documentation: https://helm.sh/docs/

    Attributes:
        helm_input_variable (str):
            Output only. Input variable name present in
            Helm Chart values.yaml
        description (str):
            Output only. Input variable description.
        type_ (str):
            Output only. Input data type.
        default_value (google.protobuf.struct_pb2.Value):
            Output only. The default value of the input
            variable.
        is_required (bool):
            Output only. Indicates if input is required.
        nested_inputs (MutableMapping[str, google.cloud.designcenter_v1.types.HelmChartInput]):
            Output only. Contains details of nested
            inputs.
    """

    helm_input_variable: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=3,
    )
    default_value: struct_pb2.Value = proto.Field(
        proto.MESSAGE,
        number=4,
        message=struct_pb2.Value,
    )
    is_required: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    nested_inputs: MutableMapping[str, "HelmChartInput"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=7,
        message="HelmChartInput",
    )


class HelmChartOutput(proto.Message):
    r"""Helm Chart outputs.

    Attributes:
        value (google.protobuf.struct_pb2.Value):
            Output only. Type of output.
        helm_output_variable (str):
            Output only. Output variable name present.
        description (str):
            Output only. Description of the variable.
    """

    value: struct_pb2.Value = proto.Field(
        proto.MESSAGE,
        number=1,
        message=struct_pb2.Value,
    )
    helm_output_variable: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )


class MetadataInput(proto.Message):
    r"""Metadata for the input

    Attributes:
        spec (google.cloud.designcenter_v1.types.MetadataInputSpec):
            Required. spec containing the metadata
    """

    spec: "MetadataInputSpec" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="MetadataInputSpec",
    )


class MetadataInputSpec(proto.Message):
    r"""Specifications for the input

    Attributes:
        info (google.cloud.designcenter_v1.types.TemplateInfo):
            Optional. TemplateInfo provides the actuation
            tool information.
        interfaces (google.cloud.designcenter_v1.types.TemplateSchema):
            Optional. TemplateSchemas provides the input
            variables lists and connection information.
        requirements (google.cloud.designcenter_v1.types.TemplateRequirements):
            Required. TemplateRequirements defines the
            roles required and the provider versions.
        ui (google.cloud.designcenter_v1.types.TemplateUi):
            Optional. TemplateUi defines the UI related
            information for the Template.
    """

    info: "TemplateInfo" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="TemplateInfo",
    )
    interfaces: "TemplateSchema" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="TemplateSchema",
    )
    requirements: "TemplateRequirements" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="TemplateRequirements",
    )
    ui: "TemplateUi" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="TemplateUi",
    )


class TemplateInfo(proto.Message):
    r"""TemplateInfo provides the actuation tool information.

    Attributes:
        actuation_tool (google.cloud.designcenter_v1.types.IacFormatInfo):
            Required. IaCFormatInfo defines the actuation
            tool used to provision the Template.
    """

    actuation_tool: "IacFormatInfo" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="IacFormatInfo",
    )


class IacFormatInfo(proto.Message):
    r"""IacFormatInfo defines the actuation tool used to provision
    the Template.

    Attributes:
        flavor (str):
            Required. Flavor is the type of the actuation
            tool.
        version (str):
            Required. Required version for the actuation tool.
            required_version = ">= 0.13".
    """

    flavor: str = proto.Field(
        proto.STRING,
        number=1,
    )
    version: str = proto.Field(
        proto.STRING,
        number=2,
    )


class TemplateSchema(proto.Message):
    r"""TemplateSchema provides the input variables lists and
    connection information.

    Attributes:
        variables (MutableSequence[google.cloud.designcenter_v1.types.TemplateVariable]):
            Required. All defined variables for the
            Template
    """

    variables: MutableSequence["TemplateVariable"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="TemplateVariable",
    )


class TemplateVariable(proto.Message):
    r"""TemplateTerraform inputs.

    Attributes:
        name (str):
            Required. Input variable name present in
            Terraform.
        connections (MutableSequence[google.cloud.designcenter_v1.types.TemplateConnections]):
            Required. Terraform input connections.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    connections: MutableSequence["TemplateConnections"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="TemplateConnections",
    )


class TemplateConnections(proto.Message):
    r"""TemplateConnections

    Attributes:
        source (google.cloud.designcenter_v1.types.ConnectionSource):
            Required. Source of the connection.
        spec (google.cloud.designcenter_v1.types.ConnectionSpec):
            Required. Connection specifications.
    """

    source: "ConnectionSource" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ConnectionSource",
    )
    spec: "ConnectionSpec" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ConnectionSpec",
    )


class ConnectionSource(proto.Message):
    r"""Defines the source of a connection.

    Attributes:
        source (str):
            Required. Source of the connection. Defined using the same
            format as module source of form
            [hostname]/namespace/name/provider for registry references
            and unprefixed github.com URLs for github references.
        version (str):
            Required. Version constraint syntax using the
            same format as module version constraints.
    """

    source: str = proto.Field(
        proto.STRING,
        number=1,
    )
    version: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ConnectionSpec(proto.Message):
    r"""Defines the specifications of a connection.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        output_expr (str):
            Required. Output expression identifying
            output being connected to variable.
        input_path (str):
            Optional. Optional dot separated attribuite
            notation to connect to a specific object field
            of the input variable.

            This field is a member of `oneof`_ ``_input_path``.
    """

    output_expr: str = proto.Field(
        proto.STRING,
        number=1,
    )
    input_path: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )


class TemplateRequirements(proto.Message):
    r"""TemplateRequirements defines the roles required and the
    associated services that need to be enabled to provision
    Template resources.

    Attributes:
        roles (MutableSequence[google.cloud.designcenter_v1.types.TemplateRoles]):
            Required. All roles required for the
            component
        provider_versions (MutableSequence[google.cloud.designcenter_v1.types.ProviderVersion]):
            Required. Required provider versions.
    """

    roles: MutableSequence["TemplateRoles"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="TemplateRoles",
    )
    provider_versions: MutableSequence["ProviderVersion"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="ProviderVersion",
    )


class TemplateRoles(proto.Message):
    r"""Template Roles provide the level and roles

    Attributes:
        level (str):
            Required. Level of the role.
        roles (MutableSequence[str]):
            Required. List of roles.
    """

    level: str = proto.Field(
        proto.STRING,
        number=1,
    )
    roles: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class TemplateUi(proto.Message):
    r"""TemplateUi defines the UI related information for the
    Template.

    Attributes:
        input (google.cloud.designcenter_v1.types.TemplateUiInput):
            Required. The top-level input section that
            defines the list of variables and their sections
            on the deployment page.
        runtime (google.cloud.designcenter_v1.types.TemplateUiOutput):
            Optional. The top-level output section that
            defines the list of outputs and their visibility
            on the deployment page.
    """

    input: "TemplateUiInput" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="TemplateUiInput",
    )
    runtime: "TemplateUiOutput" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="TemplateUiOutput",
    )


class TemplateUiInput(proto.Message):
    r"""TemplateUiInput defines the list of variables and their
    sections on the deployment page.

    Attributes:
        variables (MutableMapping[str, google.cloud.designcenter_v1.types.DisplayVariable]):
            Required. variables is a map defining all
            inputs on the UI.
    """

    variables: MutableMapping[str, "DisplayVariable"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=1,
        message="DisplayVariable",
    )


class TemplateUiOutput(proto.Message):
    r"""TemplateUiOutput defines the list of outputs and their
    visibility on the deployment page.

    Attributes:
        output_message (str):
            Optional. Message to be displayed in the UI.
        outputs (MutableMapping[str, google.cloud.designcenter_v1.types.TemplateUiOutputDisplayVariable]):
            Required. outputs is a map defining all
            outputs on the UI.
    """

    output_message: str = proto.Field(
        proto.STRING,
        number=1,
    )
    outputs: MutableMapping[str, "TemplateUiOutputDisplayVariable"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=2,
        message="TemplateUiOutputDisplayVariable",
    )


class TemplateUiOutputDisplayVariable(proto.Message):
    r"""Additional display specific Template pertaining to a
    particular output variable.

    Attributes:
        visibility (google.cloud.designcenter_v1.types.DisplayVariableVisibility):
            Required. Visibility of the output.
    """

    visibility: enums.DisplayVariableVisibility = proto.Field(
        proto.ENUM,
        number=1,
        enum=enums.DisplayVariableVisibility,
    )


class DisplayVariable(proto.Message):
    r"""Additional display specific Template pertaining to a
    particular input variable.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. The variable name from the
            corresponding standard Template file.
        title (str):
            Required. Visible title for the variable on
            the UI.
        alternate_defaults (MutableSequence[google.cloud.designcenter_v1.types.AlternateDefaultInput]):
            Optional. Alternate defaults for the input.
        regex_validation (str):
            Optional. Regex based validation rules for
            the variable.
        min_ (float):
            Optional. Minimum value for numeric types.

            This field is a member of `oneof`_ ``_min``.
        max_ (float):
            Optional. Maximum value for numeric types.

            This field is a member of `oneof`_ ``_max``.
        validation (str):
            Optional. Text describing the validation
            rules for the property. Typically shown after an
            invalid input. Optional. UTF-8 text. No markup.
            At most 128 characters.
        enum_value_labels (MutableSequence[google.cloud.designcenter_v1.types.ValueLabelInput]):
            Optional. Labels for enum values.
            Values must be UTF-8 text with no markup, and at
            most 64 characters.
        level (int):
            Optional. Indicates the "advanced" level of
            the input property. Level 0 (default) will
            always be shown. Level 1 corresponds to one
            expansion (user clicks "show advanced options"
            or "more options"). Higher levels correspond to
            further expansions, or they may be collapsed to
            level 1 by the UI implementation.
            Optional.
        subtext (str):
            Optional. Property subtext, displayed below
            the title.
        properties (MutableMapping[str, google.cloud.designcenter_v1.types.DisplayVariable]):
            Optional. properties is a map defining all
            the fields of the input variable.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    title: str = proto.Field(
        proto.STRING,
        number=2,
    )
    alternate_defaults: MutableSequence["AlternateDefaultInput"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="AlternateDefaultInput",
    )
    regex_validation: str = proto.Field(
        proto.STRING,
        number=4,
    )
    min_: float = proto.Field(
        proto.FLOAT,
        number=5,
        optional=True,
    )
    max_: float = proto.Field(
        proto.FLOAT,
        number=6,
        optional=True,
    )
    validation: str = proto.Field(
        proto.STRING,
        number=7,
    )
    enum_value_labels: MutableSequence["ValueLabelInput"] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message="ValueLabelInput",
    )
    level: int = proto.Field(
        proto.INT32,
        number=9,
    )
    subtext: str = proto.Field(
        proto.STRING,
        number=10,
    )
    properties: MutableMapping[str, "DisplayVariable"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=11,
        message="DisplayVariable",
    )


class ValueLabelInput(proto.Message):
    r"""Value label input for a UI.

    Attributes:
        value (str):
            Optional. Value of the enum.
        label (str):
            Optional. Label of the enum.
    """

    value: str = proto.Field(
        proto.STRING,
        number=1,
    )
    label: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AlternateDefaultInput(proto.Message):
    r"""Alternate default input for a UI.

    Attributes:
        type_ (google.cloud.designcenter_v1.types.DisplayVariableAlternateType):
            Optional. Type of alternate default.
        value (google.protobuf.struct_pb2.Value):
            Optional. Value of the alternate default.
    """

    type_: enums.DisplayVariableAlternateType = proto.Field(
        proto.ENUM,
        number=1,
        enum=enums.DisplayVariableAlternateType,
    )
    value: struct_pb2.Value = proto.Field(
        proto.MESSAGE,
        number=2,
        message=struct_pb2.Value,
    )


class LogicalProduct(proto.Message):
    r"""Represents a Product Main logical product.

    Attributes:
        name (str):
            Output only. The resource name of the logical product.
            Format: logicalProducts/{logical_product}
        title (str):
            Output only. The display name of the logical
            product.
        short_description (str):
            Output only. A short description of the
            logical product.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    title: str = proto.Field(
        proto.STRING,
        number=2,
    )
    short_description: str = proto.Field(
        proto.STRING,
        number=3,
    )


class InferredMetadata(proto.Message):
    r"""Inferred metadata.

    Attributes:
        description (str):
            Output only. Inferred description.
        template_metadata (google.cloud.designcenter_v1.types.TFBlueprintMetadata):
            Output only. Inferred template metadata
            related to Terraform input and output.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Inferred metadata creation
            timestamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Inferred metadata update
            timestamp.
    """

    description: str = proto.Field(
        proto.STRING,
        number=1,
    )
    template_metadata: "TFBlueprintMetadata" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="TFBlueprintMetadata",
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


class ResourceType(proto.Message):
    r"""Represents the type of a resource within a component
    template.

    Attributes:
        tf_resource (str):
            Output only. The Terraform resource type. For example:
            "google_compute_instance".
        cais_resource (str):
            Output only. The CAIS resource type.
    """

    tf_resource: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cais_resource: str = proto.Field(
        proto.STRING,
        number=2,
    )


class TerraformModuleMetadata(proto.Message):
    r"""Top-level message representing a Terraform module and its
    metadata.

    Attributes:
        uri (str):
            Optional. The URI of the Terraform module.
        id (str):
            Optional. Unique identifier for the module
            version, e.g.,
            "GoogleCloudPlatform/secret-manager/google/0.9.0".
        owner (str):
            Optional. Owner of the module.
        module_namespace (str):
            Optional. Namespace for the module, often the
            organization.
        name (str):
            Optional. Name of the module.
        version (str):
            Optional. Semantic version of the module.
        provider (str):
            Optional. Primary provider used by the
            module, e.g., "google".
        description (str):
            Optional. Description of the module's
            purpose.
        source (str):
            Optional. URL to the source repository.
        tag (str):
            Optional. Git tag or ref for this version.
        root (google.cloud.designcenter_v1.types.ModuleDetails):
            Optional. Details of the root module.
        submodules (MutableSequence[google.cloud.designcenter_v1.types.ModuleDetails]):
            Optional. List of submodules within this
            module.
        examples (MutableSequence[google.cloud.designcenter_v1.types.ModuleDetails]):
            Optional. List of examples for this module.
        providers (MutableSequence[str]):
            Optional. List of provider names used.
        versions (MutableSequence[str]):
            Optional. List of available versions for this
            module.
        revisions (MutableSequence[str]):
            Optional. List of available revisions for
            this module.
        connections (MutableSequence[google.cloud.designcenter_v1.types.TerraformInputConnections]):
            Optional. Terraform input connections.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    owner: str = proto.Field(
        proto.STRING,
        number=3,
    )
    module_namespace: str = proto.Field(
        proto.STRING,
        number=4,
    )
    name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    version: str = proto.Field(
        proto.STRING,
        number=6,
    )
    provider: str = proto.Field(
        proto.STRING,
        number=7,
    )
    description: str = proto.Field(
        proto.STRING,
        number=9,
    )
    source: str = proto.Field(
        proto.STRING,
        number=10,
    )
    tag: str = proto.Field(
        proto.STRING,
        number=11,
    )
    root: "ModuleDetails" = proto.Field(
        proto.MESSAGE,
        number=15,
        message="ModuleDetails",
    )
    submodules: MutableSequence["ModuleDetails"] = proto.RepeatedField(
        proto.MESSAGE,
        number=16,
        message="ModuleDetails",
    )
    examples: MutableSequence["ModuleDetails"] = proto.RepeatedField(
        proto.MESSAGE,
        number=17,
        message="ModuleDetails",
    )
    providers: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=18,
    )
    versions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=19,
    )
    revisions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=20,
    )
    connections: MutableSequence["TerraformInputConnections"] = proto.RepeatedField(
        proto.MESSAGE,
        number=21,
        message="TerraformInputConnections",
    )


class ModuleDetails(proto.Message):
    r"""Details about a specific module, submodule, or example.

    Attributes:
        path (str):
            Optional. Relative path to the
            module/example.
        name (str):
            Optional. Name of the module/example.
        readme (str):
            Optional. Content of the README file.
        empty (bool):
            Optional. Indicates if the module/example
            directory is empty of .tf files.
        inputs (MutableSequence[google.cloud.designcenter_v1.types.ModuleInput]):
            Optional. List of input variables.
        outputs (MutableSequence[google.cloud.designcenter_v1.types.ModuleOutput]):
            Optional. List of outputs.
        module_dependencies (MutableSequence[google.cloud.designcenter_v1.types.ModuleDependency]):
            Optional. List of module dependencies.
        provider_dependencies (MutableSequence[google.cloud.designcenter_v1.types.ProviderDependency]):
            Optional. List of provider dependencies.
        resources (MutableSequence[google.cloud.designcenter_v1.types.ModuleResource]):
            Optional. List of resources defined.
    """

    path: str = proto.Field(
        proto.STRING,
        number=1,
    )
    name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    readme: str = proto.Field(
        proto.STRING,
        number=3,
    )
    empty: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    inputs: MutableSequence["ModuleInput"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="ModuleInput",
    )
    outputs: MutableSequence["ModuleOutput"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="ModuleOutput",
    )
    module_dependencies: MutableSequence["ModuleDependency"] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="ModuleDependency",
    )
    provider_dependencies: MutableSequence["ProviderDependency"] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message="ProviderDependency",
    )
    resources: MutableSequence["ModuleResource"] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="ModuleResource",
    )


class ModuleInput(proto.Message):
    r"""Represents an input variable for a module.

    Attributes:
        name (str):
            Optional. Name of the input variable.
        type_ (str):
            Optional. Terraform type of the variable.
        description (str):
            Optional. Description of the variable.
        default_value (google.protobuf.struct_pb2.Value):
            Optional. Default value of the variable as a
            string representation. Using
            google.protobuf.Value to allow for different
            types, though a string is common.
        required (bool):
            Optional. Whether the input variable is
            required.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    default_value: struct_pb2.Value = proto.Field(
        proto.MESSAGE,
        number=4,
        message=struct_pb2.Value,
    )
    required: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class ModuleOutput(proto.Message):
    r"""Represents an output value from a module.

    Attributes:
        name (str):
            Optional. Name of the output.
        description (str):
            Optional. Description of the output.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ModuleDependency(proto.Message):
    r"""Represents a dependency on another Terraform module.

    Attributes:
        name (str):
            Optional. Local name of the module instance.
        source (str):
            Optional. Source of the module.
        version (str):
            Optional. Version constraint for the module.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    source: str = proto.Field(
        proto.STRING,
        number=2,
    )
    version: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ProviderDependency(proto.Message):
    r"""Represents a dependency on a Terraform provider.

    Attributes:
        name (str):
            Optional. Name of the provider.
        provider_namespace (str):
            Optional. Namespace of the provider (e.g.,
            "hashicorp").
        source (str):
            Optional. Source path of the provider.
        version (str):
            Optional. Version constraints for the
            provider.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    provider_namespace: str = proto.Field(
        proto.STRING,
        number=2,
    )
    source: str = proto.Field(
        proto.STRING,
        number=3,
    )
    version: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ModuleResource(proto.Message):
    r"""Represents a resource declared within a module.

    Attributes:
        name (str):
            Optional. Local name of the resource
            instance.
        type_ (str):
            Optional. Type of the resource (e.g.,
            "google_secret_manager_secret").
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListCatalogTemplateRevisionMetadataResponse(proto.Message):
    r"""Response message for ListCatalogTemplateRevisionMetadata.

    Attributes:
        catalog_template_revision_metadata (MutableSequence[google.cloud.designcenter_v1.types.CatalogTemplateRevisionMetadata]):
            List of catalog template revisions.
        next_page_token (str):
            If there might be more results than those
            appearing in this response, then nextPageToken
            is included. To get the next set of results,
            call this method again using the value of
            nextPageToken as pageToken.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    catalog_template_revision_metadata: MutableSequence[
        "CatalogTemplateRevisionMetadata"
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="CatalogTemplateRevisionMetadata",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class CatalogTemplateRevisionMetadata(proto.Message):
    r"""Represents metadata of a catalog template revision in the
    management context.

    Attributes:
        name (str):
            Output only. The catalog template name in following format:
            ``projects/$project/locations/$location/spaces/$space/catalogs/$catalog/templates/$template``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The catalog template creation
            timestamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The catalog template update
            timestamp.
        uuid (str):
            Output only. The template revisions UUID.
        latest_revision_id (str):
            Output only. Latest revision of the template.
        display_name (str):
            Optional. The display name of the catalog
            template.
        template_category (google.cloud.designcenter_v1.types.TemplateCategory):
            Required. The category of the catalog
            template.
        git_source_uri (str):
            Optional. The Git source URI where the
            template repository is hosted.
        description (str):
            Optional. The catalog template description.
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
    uuid: str = proto.Field(
        proto.STRING,
        number=4,
    )
    latest_revision_id: str = proto.Field(
        proto.STRING,
        number=5,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=6,
    )
    template_category: enums.TemplateCategory = proto.Field(
        proto.ENUM,
        number=7,
        enum=enums.TemplateCategory,
    )
    git_source_uri: str = proto.Field(
        proto.STRING,
        number=8,
    )
    description: str = proto.Field(
        proto.STRING,
        number=9,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
