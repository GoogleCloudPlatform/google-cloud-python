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

__protobuf__ = proto.module(
    package="google.cloud.cloudsecuritycompliance.v1",
    manifest={
        "RegulatoryControlResponsibilityType",
        "EnforcementMode",
        "FrameworkCategory",
        "CloudControlCategory",
        "CloudProvider",
        "Severity",
        "RuleActionType",
        "TargetResourceType",
        "Framework",
        "CloudControlDetails",
        "FrameworkReference",
        "Parameter",
        "CloudControl",
        "ParameterSpec",
        "Validation",
        "AllowedValues",
        "RegexpPattern",
        "IntRange",
        "StringList",
        "ParamValue",
        "ParameterSubstitutionRule",
        "AttributeSubstitutionRule",
        "PlaceholderSubstitutionRule",
        "Rule",
        "CELExpression",
        "OperationMetadata",
        "Control",
        "ControlFamily",
    },
)


class RegulatoryControlResponsibilityType(proto.Enum):
    r"""The responsibility type for the regulatory control.

    Values:
        REGULATORY_CONTROL_RESPONSIBILITY_TYPE_UNSPECIFIED (0):
            Default value. This value is unused.
        GOOGLE (1):
            Google's responsibility.
        CUSTOMER (2):
            Your responsibility.
        SHARED (3):
            Shared responsibility.
    """

    REGULATORY_CONTROL_RESPONSIBILITY_TYPE_UNSPECIFIED = 0
    GOOGLE = 1
    CUSTOMER = 2
    SHARED = 3


class EnforcementMode(proto.Enum):
    r"""The enforcement mode for the cloud control.

    Values:
        ENFORCEMENT_MODE_UNSPECIFIED (0):
            Default value. This value is unused.
        PREVENTIVE (1):
            The cloud control is enforced to prevent
            non-compliance.
        DETECTIVE (2):
            The cloud control is enforced to detect
            non-compliance.
        AUDIT (3):
            The cloud control is enforced to audit for
            non-compliance.
    """

    ENFORCEMENT_MODE_UNSPECIFIED = 0
    PREVENTIVE = 1
    DETECTIVE = 2
    AUDIT = 3


class FrameworkCategory(proto.Enum):
    r"""The category for the framework.

    Values:
        FRAMEWORK_CATEGORY_UNSPECIFIED (0):
            Default value. This value is unused.
        INDUSTRY_DEFINED_STANDARD (1):
            An industry-defined framework.
        ASSURED_WORKLOADS (2):
            An Assured Workloads framework.
        DATA_SECURITY (3):
            A data security posture framework.
        GOOGLE_BEST_PRACTICES (4):
            A Google's best practices framework.
        CUSTOM_FRAMEWORK (5):
            A user-created framework.
    """

    FRAMEWORK_CATEGORY_UNSPECIFIED = 0
    INDUSTRY_DEFINED_STANDARD = 1
    ASSURED_WORKLOADS = 2
    DATA_SECURITY = 3
    GOOGLE_BEST_PRACTICES = 4
    CUSTOM_FRAMEWORK = 5


class CloudControlCategory(proto.Enum):
    r"""The category for the cloud control.

    Values:
        CLOUD_CONTROL_CATEGORY_UNSPECIFIED (0):
            Default value. This value is unused.
        CC_CATEGORY_INFRASTRUCTURE (1):
            The infrastructure security category.
        CC_CATEGORY_ARTIFICIAL_INTELLIGENCE (2):
            The artificial intelligence category.
        CC_CATEGORY_PHYSICAL_SECURITY (3):
            The physical security category.
        CC_CATEGORY_DATA_SECURITY (4):
            The data security category.
        CC_CATEGORY_NETWORK_SECURITY (5):
            The network security category.
        CC_CATEGORY_INCIDENT_MANAGEMENT (6):
            The incident management category.
        CC_CATEGORY_IDENTITY_AND_ACCESS_MANAGEMENT (7):
            The identity and access management category.
        CC_CATEGORY_ENCRYPTION (8):
            The encryption category.
        CC_CATEGORY_LOGS_MANAGEMENT_AND_INFRASTRUCTURE (9):
            The logs management and infrastructure
            category.
        CC_CATEGORY_HR_ADMIN_AND_PROCESSES (10):
            The HR, admin, and processes category.
        CC_CATEGORY_THIRD_PARTY_AND_SUB_PROCESSOR_MANAGEMENT (11):
            The third-party and sub-processor management
            category.
        CC_CATEGORY_LEGAL_AND_DISCLOSURES (12):
            The legal and disclosures category.
        CC_CATEGORY_VULNERABILITY_MANAGEMENT (13):
            The vulnerability management category.
        CC_CATEGORY_PRIVACY (14):
            The privacy category.
        CC_CATEGORY_BCDR (15):
            The business continuity and disaster recovery
            (BCDR) category.
        CC_CATEGORY_ADMIN_ACCESS (16):
            The admin access category.
        CC_CATEGORY_DATA_RESIDENCY (17):
            DRZ (Data Residency).
        CC_CATEGORY_RESOURCE_USAGE_RESTRICTION (18):
            RUR (Resource Usage Restriction).
        CC_CATEGORY_SERVICE_SPECIFIC (19):
            SERVICE SPECIFIC
    """

    CLOUD_CONTROL_CATEGORY_UNSPECIFIED = 0
    CC_CATEGORY_INFRASTRUCTURE = 1
    CC_CATEGORY_ARTIFICIAL_INTELLIGENCE = 2
    CC_CATEGORY_PHYSICAL_SECURITY = 3
    CC_CATEGORY_DATA_SECURITY = 4
    CC_CATEGORY_NETWORK_SECURITY = 5
    CC_CATEGORY_INCIDENT_MANAGEMENT = 6
    CC_CATEGORY_IDENTITY_AND_ACCESS_MANAGEMENT = 7
    CC_CATEGORY_ENCRYPTION = 8
    CC_CATEGORY_LOGS_MANAGEMENT_AND_INFRASTRUCTURE = 9
    CC_CATEGORY_HR_ADMIN_AND_PROCESSES = 10
    CC_CATEGORY_THIRD_PARTY_AND_SUB_PROCESSOR_MANAGEMENT = 11
    CC_CATEGORY_LEGAL_AND_DISCLOSURES = 12
    CC_CATEGORY_VULNERABILITY_MANAGEMENT = 13
    CC_CATEGORY_PRIVACY = 14
    CC_CATEGORY_BCDR = 15
    CC_CATEGORY_ADMIN_ACCESS = 16
    CC_CATEGORY_DATA_RESIDENCY = 17
    CC_CATEGORY_RESOURCE_USAGE_RESTRICTION = 18
    CC_CATEGORY_SERVICE_SPECIFIC = 19


class CloudProvider(proto.Enum):
    r"""The cloud provider that's associated with the cloud control.

    Values:
        CLOUD_PROVIDER_UNSPECIFIED (0):
            Default value. This value is unused.
        AWS (1):
            Amazon Web Services (AWS).
        AZURE (2):
            Microsoft Azure.
        GCP (3):
            Google Cloud.
    """

    CLOUD_PROVIDER_UNSPECIFIED = 0
    AWS = 1
    AZURE = 2
    GCP = 3


class Severity(proto.Enum):
    r"""The severity of the finding.

    Values:
        SEVERITY_UNSPECIFIED (0):
            Default value. This value is unused.
        CRITICAL (1):
            A critical vulnerability is easily
            discoverable by an external actor, exploitable,
            and results in the direct ability to execute
            arbitrary code, exfiltrate data, and otherwise
            gain additional access and privileges to cloud
            resources and workloads. Examples include
            publicly accessible unprotected user data and
            public SSH access with weak or no passwords.

            A critical threat is a threat that can access,
            modify, or delete data or execute unauthorized
            code within existing resources.
        HIGH (2):
            A high-risk vulnerability can be easily
            discovered and exploited in combination with
            other vulnerabilities to gain direct access and
            the ability to execute arbitrary code,
            exfiltrate data, and otherwise gain additional
            access and privileges to cloud resources and
            workloads. An example is a database with weak or
            no passwords that is only accessible internally.
            This database could easily be compromised by an
            actor that had access to the internal network.

            A high-risk threat is a threat that can create
            new computational resources in an environment
            but can't access data or execute code in
            existing resources.
        MEDIUM (3):
            A medium-risk vulnerability can be used by an
            actor to gain access to resources or privileges
            that enable them to eventually (through multiple
            steps or a complex exploit) gain access and the
            ability to execute arbitrary code or exfiltrate
            data. An example is a service account with
            access to more projects than it should have. If
            an actor gains access to the service account,
            they could potentially use that access to
            manipulate a project the service account was not
            intended to.

            A medium-risk threat can cause operational
            impact but might not access data or execute
            unauthorized code.
        LOW (4):
            A low-risk vulnerability hampers a security
            organization's ability to detect vulnerabilities
            or active threats in their deployment, or
            prevents the root cause investigation of
            security issues. An example is monitoring and
            logs being disabled for resource configurations
            and access.

            A low-risk threat is a threat that has obtained
            minimal access to an environment but can't
            access data, execute code, or create resources.
    """

    SEVERITY_UNSPECIFIED = 0
    CRITICAL = 1
    HIGH = 2
    MEDIUM = 3
    LOW = 4


class RuleActionType(proto.Enum):
    r"""The action type of the rule.

    Values:
        RULE_ACTION_TYPE_UNSPECIFIED (0):
            Default value. This value is unused.
        RULE_ACTION_TYPE_PREVENTIVE (1):
            The rule is intended to prevent
            non-compliance.
        RULE_ACTION_TYPE_DETECTIVE (2):
            The rule is intended to detect
            non-compliance.
        RULE_ACTION_TYPE_AUDIT (3):
            The rule is intended to audit non-compliance.
    """

    RULE_ACTION_TYPE_UNSPECIFIED = 0
    RULE_ACTION_TYPE_PREVENTIVE = 1
    RULE_ACTION_TYPE_DETECTIVE = 2
    RULE_ACTION_TYPE_AUDIT = 3


class TargetResourceType(proto.Enum):
    r"""The type of resource that a control or framework can be
    applied to.

    Values:
        TARGET_RESOURCE_TYPE_UNSPECIFIED (0):
            Default value. This value is unused.
        TARGET_RESOURCE_CRM_TYPE_ORG (1):
            The target resource is a Google Cloud
            organization.
        TARGET_RESOURCE_CRM_TYPE_FOLDER (2):
            The target resource is a folder.
        TARGET_RESOURCE_CRM_TYPE_PROJECT (3):
            The target resource is a project.
        TARGET_RESOURCE_TYPE_APPLICATION (4):
            The target resource is an application in App
            Hub.
    """

    TARGET_RESOURCE_TYPE_UNSPECIFIED = 0
    TARGET_RESOURCE_CRM_TYPE_ORG = 1
    TARGET_RESOURCE_CRM_TYPE_FOLDER = 2
    TARGET_RESOURCE_CRM_TYPE_PROJECT = 3
    TARGET_RESOURCE_TYPE_APPLICATION = 4


class Framework(proto.Message):
    r"""A framework is a collection of cloud controls and regulatory
    controls that represent security best practices or
    industry-defined standards such as FedRAMP or NIST.

    Attributes:
        name (str):
            Required. Identifier. The name of the framework, in one of
            the following formats:
            ``organizations/{organization}/locations/{location}/frameworks/{framework}``
            or
            ``projects/{project}/locations/{location}/frameworks/{framework}``.

            The only supported location is ``global``.
        major_revision_id (int):
            Output only. The major version of the
            framework, which is incremented in ascending
            order.
        display_name (str):
            Optional. The friendly name of the framework.
            The maximum length is 200 characters.
        description (str):
            Optional. The description of the framework.
            The maximum length is 2000 characters.
        type_ (google.cloud.cloudsecuritycompliance_v1.types.Framework.FrameworkType):
            Output only. The type of framework.
        cloud_control_details (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.CloudControlDetails]):
            Optional. The cloud control details that are
            directly added without any grouping in the
            framework.
        category (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.FrameworkCategory]):
            Optional. The category of the framework.
        supported_cloud_providers (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.CloudProvider]):
            Output only. The cloud providers that are
            supported by the framework.
        supported_target_resource_types (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.TargetResourceType]):
            Output only. The target resource types that
            are supported by the framework.
        supported_enforcement_modes (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.EnforcementMode]):
            Output only. The supported enforcement modes
            of the framework.
    """

    class FrameworkType(proto.Enum):
        r"""The type of framework.

        Values:
            FRAMEWORK_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            BUILT_IN (1):
                A framework that's provided and managed by
                Google.
            CUSTOM (2):
                A framework that's created and managed by
                you.
        """

        FRAMEWORK_TYPE_UNSPECIFIED = 0
        BUILT_IN = 1
        CUSTOM = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    major_revision_id: int = proto.Field(
        proto.INT64,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    type_: FrameworkType = proto.Field(
        proto.ENUM,
        number=6,
        enum=FrameworkType,
    )
    cloud_control_details: MutableSequence["CloudControlDetails"] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message="CloudControlDetails",
    )
    category: MutableSequence["FrameworkCategory"] = proto.RepeatedField(
        proto.ENUM,
        number=9,
        enum="FrameworkCategory",
    )
    supported_cloud_providers: MutableSequence["CloudProvider"] = proto.RepeatedField(
        proto.ENUM,
        number=10,
        enum="CloudProvider",
    )
    supported_target_resource_types: MutableSequence["TargetResourceType"] = (
        proto.RepeatedField(
            proto.ENUM,
            number=11,
            enum="TargetResourceType",
        )
    )
    supported_enforcement_modes: MutableSequence["EnforcementMode"] = (
        proto.RepeatedField(
            proto.ENUM,
            number=13,
            enum="EnforcementMode",
        )
    )


class CloudControlDetails(proto.Message):
    r"""The details of a cloud control.

    Attributes:
        name (str):
            Required. The name of the cloud control, in one of the
            following formats:
            ``organizations/{organization}/locations/{location}/cloudControls/{cloud_control}``
            or
            ``projects/{project}/locations/{location}/cloudControls/{cloud_control}``.

            The only supported location is ``global``.
        major_revision_id (int):
            Required. The major version of the cloud
            control.
        parameters (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.Parameter]):
            Optional. Parameters are key-value pairs that let you
            provide your custom location requirements, environment
            requirements, or other settings that are relevant to the
            cloud control. An example parameter is
            ``{"name": "location","value": "us-west-1"}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    major_revision_id: int = proto.Field(
        proto.INT64,
        number=2,
    )
    parameters: MutableSequence["Parameter"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="Parameter",
    )


class FrameworkReference(proto.Message):
    r"""The reference of a framework, in one of the following formats:

    - ``organizations/{organization}/locations/{location}/frameworks/{framework}``
    - ``projects/{project}/locations/{location}/frameworks/{framework}``.

    The only supported location is ``global``.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        framework (str):
            Required. The major version of the framework.
            If not specified, the version corresponds to the
            latest version of the framework.
        major_revision_id (int):
            Optional. The major version of the framework.
            If not specified, the version corresponds to the
            latest version of the framework.

            This field is a member of `oneof`_ ``_major_revision_id``.
    """

    framework: str = proto.Field(
        proto.STRING,
        number=1,
    )
    major_revision_id: int = proto.Field(
        proto.INT64,
        number=2,
        optional=True,
    )


class Parameter(proto.Message):
    r"""Parameters are key-value pairs that let you provide your
    custom location requirements, environment requirements, or other
    settings that are relevant to the cloud control.

    Attributes:
        name (str):
            Required. The name or key of the parameter.
        parameter_value (google.cloud.cloudsecuritycompliance_v1.types.ParamValue):
            Required. The value of the parameter.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    parameter_value: "ParamValue" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ParamValue",
    )


class CloudControl(proto.Message):
    r"""A cloud control is a set of rules and associated metadata
    that you can use to define your organization's security or
    compliance intent.

    Attributes:
        name (str):
            Required. Identifier. The name of the cloud control, in
            either of the formats:
            ``organizations/{organization}/locations/{location}/cloudControls/{cloud_control}``
            or
            ``projects/{project}/locations/{location}/cloudControls/{cloud_control}``.

            The only supported location is ``global``.
        major_revision_id (int):
            Output only. The major version of the cloud
            control, which is incremented in ascending
            order.
        description (str):
            Optional. A description of the cloud control.
            The maximum length is 2000 characters.
        display_name (str):
            Optional. The friendly name of the cloud
            control. The maximum length is 200 characters.
        supported_enforcement_modes (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.EnforcementMode]):
            Output only. The supported enforcement modes
            for the cloud control.
        parameter_spec (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.ParameterSpec]):
            Optional. The parameter specifications for
            the cloud control.
        rules (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.Rule]):
            Optional. The rules that you can enforce to
            meet your security or compliance intent.
        severity (google.cloud.cloudsecuritycompliance_v1.types.Severity):
            Optional. The severity of the findings that
            are generated by the cloud control.
        finding_category (str):
            Optional. The finding category for the cloud
            control findings. The maximum length is 255
            characters.
        supported_cloud_providers (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.CloudProvider]):
            Optional. The supported cloud providers.
        related_frameworks (MutableSequence[str]):
            Output only. The frameworks that include this
            cloud control.
        remediation_steps (str):
            Optional. The remediation steps for the cloud
            control findings. The maximum length is 400
            characters.
        categories (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.CloudControlCategory]):
            Optional. The categories for the cloud
            control.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time that the cloud control was last
            updated. ``create_time`` is used because a new cloud control
            is created whenever an existing cloud control is updated.
        supported_target_resource_types (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.TargetResourceType]):
            Optional. The target resource types that are
            supported by the cloud control.
    """

    class Type(proto.Enum):
        r"""The type of cloud control.

        Values:
            TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            CUSTOM (1):
                A cloud control that's created and managed by
                you.
            BUILT_IN (2):
                A cloud control that's provided and managed
                by Google.
        """

        TYPE_UNSPECIFIED = 0
        CUSTOM = 1
        BUILT_IN = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    major_revision_id: int = proto.Field(
        proto.INT64,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    supported_enforcement_modes: MutableSequence["EnforcementMode"] = (
        proto.RepeatedField(
            proto.ENUM,
            number=7,
            enum="EnforcementMode",
        )
    )
    parameter_spec: MutableSequence["ParameterSpec"] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message="ParameterSpec",
    )
    rules: MutableSequence["Rule"] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="Rule",
    )
    severity: "Severity" = proto.Field(
        proto.ENUM,
        number=11,
        enum="Severity",
    )
    finding_category: str = proto.Field(
        proto.STRING,
        number=12,
    )
    supported_cloud_providers: MutableSequence["CloudProvider"] = proto.RepeatedField(
        proto.ENUM,
        number=13,
        enum="CloudProvider",
    )
    related_frameworks: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=14,
    )
    remediation_steps: str = proto.Field(
        proto.STRING,
        number=15,
    )
    categories: MutableSequence["CloudControlCategory"] = proto.RepeatedField(
        proto.ENUM,
        number=16,
        enum="CloudControlCategory",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=17,
        message=timestamp_pb2.Timestamp,
    )
    supported_target_resource_types: MutableSequence["TargetResourceType"] = (
        proto.RepeatedField(
            proto.ENUM,
            number=18,
            enum="TargetResourceType",
        )
    )


class ParameterSpec(proto.Message):
    r"""The parameter specification for the cloud control.

    Attributes:
        name (str):
            Required. The name of the parameter.
        display_name (str):
            Optional. The friendly name of the parameter.
            The maximum length is 200 characters.
        description (str):
            Optional. The description of the parameter.
            The maximum length is 2000 characters.
        is_required (bool):
            Required. Whether the parameter is required.
        value_type (google.cloud.cloudsecuritycompliance_v1.types.ParameterSpec.ValueType):
            Required. The parameter value type.
        default_value (google.cloud.cloudsecuritycompliance_v1.types.ParamValue):
            Optional. The default value of the parameter.
        substitution_rules (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.ParameterSubstitutionRule]):
            Optional. The list of parameter
            substitutions.
        sub_parameters (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.ParameterSpec]):
            Optional. The parameter specification for ``oneOf``
            attributes.
        validation (google.cloud.cloudsecuritycompliance_v1.types.Validation):
            Optional. The permitted set of values for the
            parameter.
    """

    class ValueType(proto.Enum):
        r"""The type of parameter value.

        Values:
            VALUE_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            STRING (3):
                A string value.
            BOOLEAN (4):
                A boolean value.
            STRINGLIST (5):
                A string list value.
            NUMBER (6):
                A numeric value.
            ONEOF (7):
                A oneOf value.
        """

        VALUE_TYPE_UNSPECIFIED = 0
        STRING = 3
        BOOLEAN = 4
        STRINGLIST = 5
        NUMBER = 6
        ONEOF = 7

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
    is_required: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    value_type: ValueType = proto.Field(
        proto.ENUM,
        number=5,
        enum=ValueType,
    )
    default_value: "ParamValue" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="ParamValue",
    )
    substitution_rules: MutableSequence["ParameterSubstitutionRule"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=7,
            message="ParameterSubstitutionRule",
        )
    )
    sub_parameters: MutableSequence["ParameterSpec"] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message="ParameterSpec",
    )
    validation: "Validation" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="Validation",
    )


class Validation(proto.Message):
    r"""The validation of the parameter.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        allowed_values (google.cloud.cloudsecuritycompliance_v1.types.AllowedValues):
            The permitted set of values for the
            parameter.

            This field is a member of `oneof`_ ``constraint``.
        int_range (google.cloud.cloudsecuritycompliance_v1.types.IntRange):
            The permitted range for numeric parameters.

            This field is a member of `oneof`_ ``constraint``.
        regexp_pattern (google.cloud.cloudsecuritycompliance_v1.types.RegexpPattern):
            The regular expression for string parameters.

            This field is a member of `oneof`_ ``constraint``.
    """

    allowed_values: "AllowedValues" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="constraint",
        message="AllowedValues",
    )
    int_range: "IntRange" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="constraint",
        message="IntRange",
    )
    regexp_pattern: "RegexpPattern" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="constraint",
        message="RegexpPattern",
    )


class AllowedValues(proto.Message):
    r"""The allowed set of values for the parameter.

    Attributes:
        values (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.ParamValue]):
            Required. The list of allowed values for the
            parameter.
    """

    values: MutableSequence["ParamValue"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ParamValue",
    )


class RegexpPattern(proto.Message):
    r"""The regular expression (regex) validator for parameter
    values.

    Attributes:
        pattern (str):
            Required. The regex pattern to match the
            values of the parameter with.
    """

    pattern: str = proto.Field(
        proto.STRING,
        number=1,
    )


class IntRange(proto.Message):
    r"""The number range for number parameters.

    Attributes:
        min_ (int):
            Required. The minimum permitted value for the
            numeric parameter (inclusive).
        max_ (int):
            Required. The maximum permitted value for the
            numeric parameter (inclusive).
    """

    min_: int = proto.Field(
        proto.INT64,
        number=1,
    )
    max_: int = proto.Field(
        proto.INT64,
        number=2,
    )


class StringList(proto.Message):
    r"""A list of strings for the parameter value.

    Attributes:
        values (MutableSequence[str]):
            Required. The strings in the list.
    """

    values: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class ParamValue(proto.Message):
    r"""The possible parameter value types.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        string_value (str):
            Optional. A string value.

            This field is a member of `oneof`_ ``kind``.
        bool_value (bool):
            Optional. A boolean value.

            This field is a member of `oneof`_ ``kind``.
        string_list_value (google.cloud.cloudsecuritycompliance_v1.types.StringList):
            Optional. A repeated string.

            This field is a member of `oneof`_ ``kind``.
        number_value (float):
            Optional. A double value.

            This field is a member of `oneof`_ ``kind``.
        oneof_value (google.cloud.cloudsecuritycompliance_v1.types.Parameter):
            Optional. Sub-parameter values.

            This field is a member of `oneof`_ ``kind``.
    """

    string_value: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="kind",
    )
    bool_value: bool = proto.Field(
        proto.BOOL,
        number=4,
        oneof="kind",
    )
    string_list_value: "StringList" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="kind",
        message="StringList",
    )
    number_value: float = proto.Field(
        proto.DOUBLE,
        number=6,
        oneof="kind",
    )
    oneof_value: "Parameter" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="kind",
        message="Parameter",
    )


class ParameterSubstitutionRule(proto.Message):
    r"""The parameter substitution rules.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        placeholder_substitution_rule (google.cloud.cloudsecuritycompliance_v1.types.PlaceholderSubstitutionRule):
            The placeholder substitution rule.

            This field is a member of `oneof`_ ``substitution_type``.
        attribute_substitution_rule (google.cloud.cloudsecuritycompliance_v1.types.AttributeSubstitutionRule):
            The attribute substitution rule.

            This field is a member of `oneof`_ ``substitution_type``.
    """

    placeholder_substitution_rule: "PlaceholderSubstitutionRule" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="substitution_type",
        message="PlaceholderSubstitutionRule",
    )
    attribute_substitution_rule: "AttributeSubstitutionRule" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="substitution_type",
        message="AttributeSubstitutionRule",
    )


class AttributeSubstitutionRule(proto.Message):
    r"""The attribute at the given path that's substituted entirely.

    Attributes:
        attribute (str):
            The fully qualified proto attribute path, in dot notation.
            For example:
            ``rules[0].cel_expression.resource_types_values``
    """

    attribute: str = proto.Field(
        proto.STRING,
        number=1,
    )


class PlaceholderSubstitutionRule(proto.Message):
    r"""The placeholder that's substituted in the rendered string.

    Attributes:
        attribute (str):
            The fully qualified proto attribute path, in
            dot notation.
    """

    attribute: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Rule(proto.Message):
    r"""A rule in the cloud control.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        cel_expression (google.cloud.cloudsecuritycompliance_v1.types.CELExpression):
            The rule's logic expression in Common
            Expression Language (CEL).

            This field is a member of `oneof`_ ``implementation``.
        description (str):
            Optional. The rule description. The maximum
            length is 2000 characters.
        rule_action_types (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.RuleActionType]):
            Required. The functionality that's enabled by
            the rule.
    """

    cel_expression: "CELExpression" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="implementation",
        message="CELExpression",
    )
    description: str = proto.Field(
        proto.STRING,
        number=10,
    )
    rule_action_types: MutableSequence["RuleActionType"] = proto.RepeatedField(
        proto.ENUM,
        number=16,
        enum="RuleActionType",
    )


class CELExpression(proto.Message):
    r"""A Common Expression Language (CEL) expression that's used to
    create a rule.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        resource_types_values (google.cloud.cloudsecuritycompliance_v1.types.StringList):
            The resource instance types on which this expression is
            defined. The format is ``<SERVICE_NAME>/<type>``. For
            example: ``compute.googleapis.com/Instance``

            This field is a member of `oneof`_ ``criteria``.
        expression (str):
            Required. The logical expression in CEL. The maximum length
            of the condition is 1000 characters. For more information,
            see `CEL
            expression <https://cloud.google.com/security-command-center/docs/compliance-manager-write-cel-expressions>`__.
    """

    resource_types_values: "StringList" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="criteria",
        message="StringList",
    )
    expression: str = proto.Field(
        proto.STRING,
        number=1,
    )


class OperationMetadata(proto.Message):
    r"""The metadata for the long-running operation.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        target (str):
            Output only. The server-defined resource path
            for the target of the operation.
        verb (str):
            Output only. The name of the verb that was
            executed by the operation.
        status_message (str):
            Output only. The human-readable status of the
            operation, if any.
        requested_cancellation (bool):
            Output only. Identifies whether the user has requested that
            the operation be cancelled. If an operation was cancelled
            successfully, then the field
            [google.longrunning.Operation.error][google.longrunning.Operation.error]
            contains the value
            [google.rpc.Code.CANCELLED][google.rpc.Code.CANCELLED].
        api_version (str):
            Output only. The API version that was used to
            start the operation.
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


class Control(proto.Message):
    r"""The regulatory control.

    Attributes:
        name (str):
            Output only. The name of a regulatory control, in one of the
            following formats:

            - ``organizations/{organization}/locations/{location}/controls/{control}``
            - ``projects/{project}/locations/{location}/controls/{control}``.

            The only supported location is ``global``.
        display_name (str):
            Output only. The friendly name for the
            regulatory control.
        description (str):
            Output only. The description of the
            regulatory control.
        family (google.cloud.cloudsecuritycompliance_v1.types.Control.Family):
            Output only. The regulatory group that the
            control belongs to.
        control_family (google.cloud.cloudsecuritycompliance_v1.types.ControlFamily):
            Output only. The regulatory family that the
            control belongs to.
        responsibility_type (google.cloud.cloudsecuritycompliance_v1.types.RegulatoryControlResponsibilityType):
            Output only. The entity that's responsible
            for the control, whether Google, you as the
            customer, or both.
        google_responsibility_description (str):
            Output only. A description of Google's
            responsibility for the regulatory control.
        google_responsibility_implementation (str):
            Output only. A description of Google's
            responsibility for implementing the regulatory
            control.
        customer_responsibility_description (str):
            Output only. A description of your
            responsibility for the regulatory control.
        customer_responsibility_implementation (str):
            Output only. A description of the your
            responsibility for implementing the regulatory
            control.
        shared_responsibility_description (str):
            Output only. A description of the
            responsibility that's shared between Google and
            you in implementing this control.
        additional_content_uri (str):
            Output only. A link to the documentation
            that's related to this control.
        related_frameworks (MutableSequence[str]):
            Output only. The frameworks that include this
            control.
    """

    class Family(proto.Enum):
        r"""The regulatory control family.

        Values:
            FAMILY_UNSPECIFIED (0):
                Default value. This value is unused.
            AC (1):
                Access control
            AT (2):
                Awareness and araining
            AU (3):
                Audit and accountability
            CA (4):
                Certification, accreditation, and security
                assessments
            CM (5):
                Configuration management
            CP (6):
                Contingency planning
            IA (7):
                Identification and authentication
            IR (8):
                Incident response
            MA (9):
                Maintenance
            MP (10):
                Media protection
            PE (11):
                Physical and environmental protection
            PL (12):
                Security planning
            PS (13):
                Personnel aecurity
            RA (14):
                Risk assessment
            SA (15):
                System services and acquisition
            SC (16):
                System and communications protection
            SI (17):
                System and information integrity
            SR (18):
                Supply chain risk management
        """

        FAMILY_UNSPECIFIED = 0
        AC = 1
        AT = 2
        AU = 3
        CA = 4
        CM = 5
        CP = 6
        IA = 7
        IR = 8
        MA = 9
        MP = 10
        PE = 11
        PL = 12
        PS = 13
        RA = 14
        SA = 15
        SC = 16
        SI = 17
        SR = 18

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    family: Family = proto.Field(
        proto.ENUM,
        number=5,
        enum=Family,
    )
    control_family: "ControlFamily" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="ControlFamily",
    )
    responsibility_type: "RegulatoryControlResponsibilityType" = proto.Field(
        proto.ENUM,
        number=7,
        enum="RegulatoryControlResponsibilityType",
    )
    google_responsibility_description: str = proto.Field(
        proto.STRING,
        number=8,
    )
    google_responsibility_implementation: str = proto.Field(
        proto.STRING,
        number=9,
    )
    customer_responsibility_description: str = proto.Field(
        proto.STRING,
        number=10,
    )
    customer_responsibility_implementation: str = proto.Field(
        proto.STRING,
        number=11,
    )
    shared_responsibility_description: str = proto.Field(
        proto.STRING,
        number=12,
    )
    additional_content_uri: str = proto.Field(
        proto.STRING,
        number=13,
    )
    related_frameworks: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=14,
    )


class ControlFamily(proto.Message):
    r"""The regulatory family of the control.

    Attributes:
        family_id (str):
            The identifier for the regulatory control
            family.
        display_name (str):
            The friendly name for the regulatory control
            family.
    """

    family_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
