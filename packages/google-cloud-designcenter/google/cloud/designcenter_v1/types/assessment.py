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

import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.designcenter_v1.types import parameters as gcd_parameters

__protobuf__ = proto.module(
    package="google.cloud.designcenter.v1",
    manifest={
        "DomainAssessmentReport",
        "ScoreCard",
        "ApplyCondition",
        "SkippedDomain",
        "Domain",
        "Framework",
        "CloudControl",
        "ParameterSpec",
        "AdcMetadata",
        "AssessedFramework",
        "AssessmentFinding",
        "SCCMetadata",
        "AssetDetails",
        "RemediationStep",
    },
)


class DomainAssessmentReport(proto.Message):
    r"""The assessment report for each domain.

    Attributes:
        report_name (str):
            Optional. The report name as per Application
            Design Center.
        domain_id (str):
            Output only. The ID of the domain.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the report was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the report was
            last updated.
        status (google.cloud.designcenter_v1.types.DomainAssessmentReport.Status):
            Optional. Status of assessment report.
        adc_metadata (google.cloud.designcenter_v1.types.AdcMetadata):
            Output only. Specific information and
            metadata.
        assessed_frameworks (MutableSequence[google.cloud.designcenter_v1.types.AssessedFramework]):
            Required. List of frameworks assessed and
            their findings.
        additional_info (str):
            Optional. Additional information about the
            report.
        skipped_asset_types (MutableSequence[str]):
            Optional. List of asset types skipped during
            assessment.
        domain_redirect_info (google.cloud.designcenter_v1.types.DomainAssessmentReport.DomainRedirectInfo):
            Optional. Information on how to redirect to
            domain.
        report_score (google.cloud.designcenter_v1.types.ScoreCard):
            Output only. Score card associated with the
            report.
    """

    class Status(proto.Enum):
        r"""Status of domain assessment report.

        Values:
            STATUS_UNSPECIFIED (0):
                No status specified.
            PENDING (1):
                Pending domain assessment.
            COMPLETED (2):
                Complete domain assessment.
            FAILED (3):
                Failed domain assessment.
        """

        STATUS_UNSPECIFIED = 0
        PENDING = 1
        COMPLETED = 2
        FAILED = 3

    class DomainRedirectInfo(proto.Message):
        r"""Information on how to redirect to domain.

        Attributes:
            url (str):
                Required. URL to the domain page.
            url_text (str):
                Required. Text to display in UI on the
                redirect URL.
            open_in_same_tab (bool):
                Optional. Flag to open the URL in new tab.
                Default: false.
        """

        url: str = proto.Field(
            proto.STRING,
            number=1,
        )
        url_text: str = proto.Field(
            proto.STRING,
            number=2,
        )
        open_in_same_tab: bool = proto.Field(
            proto.BOOL,
            number=3,
        )

    report_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    domain_id: str = proto.Field(
        proto.STRING,
        number=2,
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
    status: Status = proto.Field(
        proto.ENUM,
        number=5,
        enum=Status,
    )
    adc_metadata: "AdcMetadata" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="AdcMetadata",
    )
    assessed_frameworks: MutableSequence["AssessedFramework"] = proto.RepeatedField(
        proto.MESSAGE,
        number=14,
        message="AssessedFramework",
    )
    additional_info: str = proto.Field(
        proto.STRING,
        number=11,
    )
    skipped_asset_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=12,
    )
    domain_redirect_info: DomainRedirectInfo = proto.Field(
        proto.MESSAGE,
        number=13,
        message=DomainRedirectInfo,
    )
    report_score: "ScoreCard" = proto.Field(
        proto.MESSAGE,
        number=15,
        message="ScoreCard",
    )


class ScoreCard(proto.Message):
    r"""Score card associated with the report.

    Attributes:
        report_score (int):
            Required. Calculated score of the report.
        max_score (int):
            Required. Maximum score of the report. For example, for a
            score of 75/100, report_score is 75 and max_score is 100.
        min_score_required (int):
            Optional. Minimum score required to pass
            assessment.
        average_score (int):
            Optional. Average score for similar reports.
    """

    report_score: int = proto.Field(
        proto.INT32,
        number=1,
    )
    max_score: int = proto.Field(
        proto.INT32,
        number=2,
    )
    min_score_required: int = proto.Field(
        proto.INT32,
        number=3,
    )
    average_score: int = proto.Field(
        proto.INT32,
        number=4,
    )


class ApplyCondition(proto.Message):
    r"""Condition for applying the policy. Accepts the ``criticality`` and
    ``environment`` parameters from the application template.

    Attributes:
        condition_key (str):
            Required. The key of the parameter for the
            condition.
        condition_value (str):
            Required. The value of the parameter for the
            condition.
    """

    condition_key: str = proto.Field(
        proto.STRING,
        number=1,
    )
    condition_value: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SkippedDomain(proto.Message):
    r"""Domains skipped during the best practice assessment.

    Attributes:
        domain (google.cloud.designcenter_v1.types.Domain):
            Output only. Details of the domain skipped.
        skip_reason (google.cloud.designcenter_v1.types.SkippedDomain.Reason):
            Output only. Reason for skipping the domain
            from assessment.
    """

    class Reason(proto.Enum):
        r"""Reason for skipping the domain from assessment.

        Values:
            REASON_UNSPECIFIED (0):
                No reason specified.
            UNAVAILABLE (1):
                Domain is unavailable.
            FAILURE (2):
                Domain assessment failed.
            TIMEOUT (3):
                Domain assessment timed out.
        """

        REASON_UNSPECIFIED = 0
        UNAVAILABLE = 1
        FAILURE = 2
        TIMEOUT = 3

    domain: "Domain" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Domain",
    )
    skip_reason: Reason = proto.Field(
        proto.ENUM,
        number=2,
        enum=Reason,
    )


class Domain(proto.Message):
    r"""Domain for assessment.

    Attributes:
        domain_name (str):
            Required. The domain name. Uniquely
            identifies the domain.
        display_name (str):
            Optional. The domain display name is user
            friendly name used for UI.
        description (str):
            Optional. The domain description.
        frameworks (MutableSequence[google.cloud.designcenter_v1.types.Framework]):
            Optional. The frameworks that are applicable
            in this domain.
        inactive (bool):
            Optional. Whether the domain is inactive.
            Default: false.
    """

    domain_name: str = proto.Field(
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
    frameworks: MutableSequence["Framework"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="Framework",
    )
    inactive: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class Framework(proto.Message):
    r"""Framework for assessment.

    Attributes:
        name (str):
            Required. The framework name.
        major_revision_id (int):
            Optional. The major revision id of the
            framework.
        parent_domain (google.cloud.designcenter_v1.types.Domain):
            Required. The domain to which this framework
            belongs.
        display_name (str):
            Optional. The framework display name.
        description (str):
            Optional. The framework description.
        url (str):
            Optional. The URL to a framework.
        active (bool):
            Optional. Whether the framework is active.
        cloud_control_details (MutableSequence[google.cloud.designcenter_v1.types.CloudControl]):
            Optional. The cloud controls that are
            associated with the framework.
        deployment_status (google.cloud.designcenter_v1.types.Framework.DeploymentStatus):
            Optional. The deployment status of the
            framework.
        managed_project_applicable (bool):
            Output only. Indicates if the framework is
            defined in the managed project. Only
            managed-project frameworks can be manually
            attached.
    """

    class DeploymentStatus(proto.Enum):
        r"""Enum for deployment status of a framework.

        Values:
            DEPLOYMENT_STATUS_UNSPECIFIED (0):
                Deployment status unspecified.
            DEPLOYED (1):
                Framework is deployed.
            UNDEPLOYED (2):
                Framework is undeployed.
        """

        DEPLOYMENT_STATUS_UNSPECIFIED = 0
        DEPLOYED = 1
        UNDEPLOYED = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    major_revision_id: int = proto.Field(
        proto.INT32,
        number=11,
    )
    parent_domain: "Domain" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="Domain",
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    url: str = proto.Field(
        proto.STRING,
        number=5,
    )
    active: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    cloud_control_details: MutableSequence["CloudControl"] = proto.RepeatedField(
        proto.MESSAGE,
        number=12,
        message="CloudControl",
    )
    deployment_status: DeploymentStatus = proto.Field(
        proto.ENUM,
        number=10,
        enum=DeploymentStatus,
    )
    managed_project_applicable: bool = proto.Field(
        proto.BOOL,
        number=13,
    )


class CloudControl(proto.Message):
    r"""Cloud control for a framework.

    Attributes:
        name (str):
            Required. The name of the cloud control.
        description (str):
            Optional. The description of the cloud
            control.
        major_revision_id (int):
            Required. The major revision id of the cloud
            control.
        enforcement_mode (google.cloud.designcenter_v1.types.CloudControl.EnforcementMode):
            Optional. The enforcement mode of the cloud
            control.
        parameter_specs (MutableSequence[google.cloud.designcenter_v1.types.ParameterSpec]):
            Optional. The specifications of the
            parameters supported by the cloud control.
        parameters (MutableSequence[google.cloud.designcenter_v1.types.Parameter]):
            Optional. The parameter values that are
            already configured for the cloud control, if
            any. Used to pre-populate the parameter values
            presented to the user.
    """

    class EnforcementMode(proto.Enum):
        r"""Enum for enforcement mode of a cloud control.

        Values:
            ENFORCEMENT_MODE_UNSPECIFIED (0):
                Enforcement type unspecified.
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

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    major_revision_id: int = proto.Field(
        proto.INT32,
        number=3,
    )
    enforcement_mode: EnforcementMode = proto.Field(
        proto.ENUM,
        number=4,
        enum=EnforcementMode,
    )
    parameter_specs: MutableSequence["ParameterSpec"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="ParameterSpec",
    )
    parameters: MutableSequence[gcd_parameters.Parameter] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=gcd_parameters.Parameter,
    )


class ParameterSpec(proto.Message):
    r"""The specification of a parameter that can be configured on a
    cloud control or a framework.

    Attributes:
        key (str):
            Required. The key of the parameter, matching
            [Parameter.key][google.cloud.designcenter.v1.Parameter.key]
            of the value supplied for it.
        display_name (str):
            Optional. The parameter display name, which
            is a user friendly name used for UI.
        description (str):
            Optional. The parameter description.
        required (bool):
            Optional. Whether a value must be provided
            for the parameter.
        value_type (google.cloud.designcenter_v1.types.ParameterSpec.ValueType):
            Optional. The type of value that the
            parameter accepts.
        default_value (google.protobuf.struct_pb2.Value):
            Optional. The default value of the parameter,
            used when the user does not provide one.
        sub_parameter_specs (MutableSequence[google.cloud.designcenter_v1.types.ParameterSpec]):
            Optional. The specifications of the sub-parameters. Only set
            when ``value_type`` is ``ONEOF``.
    """

    class ValueType(proto.Enum):
        r"""The type of value that the parameter accepts.

        Values:
            VALUE_TYPE_UNSPECIFIED (0):
                Default. This value is unused.
            STRING (3):
                A string value.
            BOOLEAN (4):
                A boolean value.
            STRINGLIST (5):
                A list of string values.
            NUMBER (6):
                A numeric value.
            ONEOF (7):
                Exactly one of the sub-parameters must be
                provided.
        """

        VALUE_TYPE_UNSPECIFIED = 0
        STRING = 3
        BOOLEAN = 4
        STRINGLIST = 5
        NUMBER = 6
        ONEOF = 7

    key: str = proto.Field(
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
    required: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    value_type: ValueType = proto.Field(
        proto.ENUM,
        number=5,
        enum=ValueType,
    )
    default_value: struct_pb2.Value = proto.Field(
        proto.MESSAGE,
        number=6,
        message=struct_pb2.Value,
    )
    sub_parameter_specs: MutableSequence["ParameterSpec"] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message="ParameterSpec",
    )


class AdcMetadata(proto.Message):
    r"""Application Design Center specific information and metadata.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        application_uri (str):
            Output only. Application URI

            This field is a member of `oneof`_ ``app_uri``.
        application_template_uri (str):
            Output only. ApplicationTemplate URI

            This field is a member of `oneof`_ ``app_uri``.
        space_uri (str):
            Output only. Space URI

            This field is a member of `oneof`_ ``app_uri``.
        catalog_template_revision_uri (str):
            Output only. CatalogTemplateRevision URI

            This field is a member of `oneof`_ ``app_uri``.
    """

    application_uri: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="app_uri",
    )
    application_template_uri: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="app_uri",
    )
    space_uri: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="app_uri",
    )
    catalog_template_revision_uri: str = proto.Field(
        proto.STRING,
        number=4,
        oneof="app_uri",
    )


class AssessedFramework(proto.Message):
    r"""Framework assessed and their findings.

    Attributes:
        framework (google.cloud.designcenter_v1.types.Framework):
            Required. The framework that was assessed.
        findings (MutableSequence[google.cloud.designcenter_v1.types.AssessmentFinding]):
            Required. A list of every Finding found
            during the assessment.
        score_card (google.cloud.designcenter_v1.types.ScoreCard):
            Optional. Score card associated with the
            report.
        skipped (bool):
            Optional. Whether the framework was skipped
            during assessment.
        skipped_reason (str):
            Optional. Reason for skipping the framework
            during assessment.
    """

    framework: "Framework" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Framework",
    )
    findings: MutableSequence["AssessmentFinding"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="AssessmentFinding",
    )
    score_card: "ScoreCard" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ScoreCard",
    )
    skipped: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    skipped_reason: str = proto.Field(
        proto.STRING,
        number=5,
    )


class AssessmentFinding(proto.Message):
    r"""Details of an Assessment Finding.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        remediation_step (google.cloud.designcenter_v1.types.RemediationStep):
            Optional. A description of the steps that
            users can take to fix the finding.

            This field is a member of `oneof`_ ``next_step``.
        additional_notes (str):
            Optional. A description of the additional
            details about finding.

            This field is a member of `oneof`_ ``additional_details``.
        id (str):
            Output only. The Finding ID.
        assessed_framework_id (str):
            Optional. The framework that was assessed.
        adc_metadata (google.cloud.designcenter_v1.types.AssessmentFinding.FindingADCMetadata):
            Output only. Metadata related to the
            Application Design Center with the finding.
        finding_type (google.cloud.designcenter_v1.types.AssessmentFinding.Type):
            Required. The type of the finding. Findings
            can be informational, warning, or error.
        severity (google.cloud.designcenter_v1.types.AssessmentFinding.Severity):
            Optional. The severity of the finding.
        assessed_asset (google.cloud.designcenter_v1.types.AssetDetails):
            Required. Details of the Cloud Asset
            Inventory asset that was assessed.
        assessed_framework (google.cloud.designcenter_v1.types.Framework):
            Optional. Details of the framework that was
            assessed.
        description (str):
            Optional. Description of the finding.
        findings_uri (str):
            Optional. Link to the findings, if persisted
            by the domain.
        scc_metadata (google.cloud.designcenter_v1.types.SCCMetadata):
            Output only. SCC related metadata for the
            finding.
    """

    class Type(proto.Enum):
        r"""The type of finding.

        Values:
            TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            WARNING (1):
                Warning finding. Deployment will not be
                blocked.
            ERROR (2):
                Error finding. Deployment will be blocked on
                ERROR.
        """

        TYPE_UNSPECIFIED = 0
        WARNING = 1
        ERROR = 2

    class Severity(proto.Enum):
        r"""The severity of a finding.

        Values:
            SEVERITY_UNSPECIFIED (0):
                Default value. This value is unused.
            CRITICAL (1):
                Critical severity.
            HIGH (2):
                High severity.
            MEDIUM (3):
                Medium severity.
            LOW (4):
                Low severity.
        """

        SEVERITY_UNSPECIFIED = 0
        CRITICAL = 1
        HIGH = 2
        MEDIUM = 3
        LOW = 4

    class FindingADCMetadata(proto.Message):
        r"""Metadata related to the Application Design Center with the
        finding.

        Attributes:
            component_name (str):
                Output only. Component the finding belongs
                to.
        """

        component_name: str = proto.Field(
            proto.STRING,
            number=1,
        )

    remediation_step: "RemediationStep" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="next_step",
        message="RemediationStep",
    )
    additional_notes: str = proto.Field(
        proto.STRING,
        number=10,
        oneof="additional_details",
    )
    id: str = proto.Field(
        proto.STRING,
        number=12,
    )
    assessed_framework_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    adc_metadata: FindingADCMetadata = proto.Field(
        proto.MESSAGE,
        number=3,
        message=FindingADCMetadata,
    )
    finding_type: Type = proto.Field(
        proto.ENUM,
        number=4,
        enum=Type,
    )
    severity: Severity = proto.Field(
        proto.ENUM,
        number=5,
        enum=Severity,
    )
    assessed_asset: "AssetDetails" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="AssetDetails",
    )
    assessed_framework: "Framework" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="Framework",
    )
    description: str = proto.Field(
        proto.STRING,
        number=9,
    )
    findings_uri: str = proto.Field(
        proto.STRING,
        number=11,
    )
    scc_metadata: "SCCMetadata" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="SCCMetadata",
    )


class SCCMetadata(proto.Message):
    r"""SCC metadata for the assessment finding.

    Attributes:
        finding_class (str):
            Optional. The SCC finding class. Also known
            as category.
        finding_type (str):
            Optional. The SCC finding type.
    """

    finding_class: str = proto.Field(
        proto.STRING,
        number=1,
    )
    finding_type: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AssetDetails(proto.Message):
    r"""Details of a Cloud Asset Inventory asset that caused the
    finding.

    Attributes:
        asset_id (str):
            Required. Information about the Cloud Asset Inventory asset
            that the framework is assessed against. The full resource
            name of the asset in CAIS format.

            For details about the format of the full resource name for
            each asset type, see [Resource name format]
            (https://cloud.google.com/asset-inventory/docs/resource-name-format).
        asset_type (str):
            Optional. The type of Cloud Asset Inventory asset. For a
            list of asset types, see `Supported asset
            types <https://cloud.google.com/asset-inventory/docs/supported-asset-types>`__.
    """

    asset_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    asset_type: str = proto.Field(
        proto.STRING,
        number=2,
    )


class RemediationStep(proto.Message):
    r"""Remediation steps that can be taken to rectify the finding.

    Attributes:
        remediation_steps (MutableSequence[str]):
            Required. A description of the steps that
            users can take to remediate the findings.
        remediation_documentation_url (str):
            Optional. Remediation documentation URL.
        note (str):
            Optional. Any other note related to the
            remediation.
    """

    remediation_steps: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    remediation_documentation_url: str = proto.Field(
        proto.STRING,
        number=2,
    )
    note: str = proto.Field(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
