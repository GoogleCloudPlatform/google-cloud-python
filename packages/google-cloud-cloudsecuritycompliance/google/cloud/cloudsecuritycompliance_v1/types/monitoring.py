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
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.type.interval_pb2 as interval_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.cloudsecuritycompliance_v1.types import common

__protobuf__ = proto.module(
    package="google.cloud.cloudsecuritycompliance.v1",
    manifest={
        "EvaluationState",
        "FindingClass",
        "FrameworkComplianceSummaryView",
        "ListFrameworkComplianceSummariesRequest",
        "ListFrameworkComplianceSummariesResponse",
        "FrameworkComplianceReport",
        "FetchFrameworkComplianceReportRequest",
        "ListFindingSummariesRequest",
        "ListFindingSummariesResponse",
        "ListControlComplianceSummariesRequest",
        "ListControlComplianceSummariesResponse",
        "AggregateFrameworkComplianceReportRequest",
        "AggregateFrameworkComplianceReportResponse",
        "ControlAssessmentDetails",
        "FrameworkComplianceSummary",
        "FindingSummary",
        "ControlComplianceSummary",
        "CloudControlReport",
        "ManualCloudControlAssessmentDetails",
        "CloudControlAssessmentDetails",
        "SimilarControls",
        "AggregatedComplianceReport",
        "TargetResourceDetails",
        "Trend",
    },
)


class EvaluationState(proto.Enum):
    r"""The evaluation state of the control.

    Values:
        EVALUATION_STATE_UNSPECIFIED (0):
            Default value. This value is unused.
        EVALUATION_STATE_PASSED (1):
            The control is passing.
        EVALUATION_STATE_FAILED (2):
            The control is failing.
        EVALUATION_STATE_NOT_ASSESSED (3):
            The control is not assessed.
    """

    EVALUATION_STATE_UNSPECIFIED = 0
    EVALUATION_STATE_PASSED = 1
    EVALUATION_STATE_FAILED = 2
    EVALUATION_STATE_NOT_ASSESSED = 3


class FindingClass(proto.Enum):
    r"""A finding is a record of assessment data like security, risk,
    health, or privacy.

    Values:
        FINDING_CLASS_UNSPECIFIED (0):
            Default value. This value is unused.
        THREAT (1):
            The activity is unwanted or malicious.
        VULNERABILITY (2):
            A potential weakness in software that
            increases risk to confidentiality, integrity,
            and availability.
        MISCONFIGURATION (3):
            A potential weakness in a cloud resource or
            asset configuration that increases risk.
        OBSERVATION (4):
            A security observation that is for
            informational purposes.
        SCC_ERROR (5):
            An error that prevents Security Command
            Center from functioning properly.
        POSTURE_VIOLATION (6):
            A potential security risk that's due to a
            change in the security posture.
        TOXIC_COMBINATION (7):
            A combination of security issues that
            represent a more severe security problem when
            taken together.
        SENSITIVE_DATA_RISK (8):
            A potential security risk to data assets that
            contain sensitive data.
        CHOKEPOINT (9):
            A resource or resource group where high risk
            attack paths converge, based on attack path
            simulations (APS).
    """

    FINDING_CLASS_UNSPECIFIED = 0
    THREAT = 1
    VULNERABILITY = 2
    MISCONFIGURATION = 3
    OBSERVATION = 4
    SCC_ERROR = 5
    POSTURE_VIOLATION = 6
    TOXIC_COMBINATION = 7
    SENSITIVE_DATA_RISK = 8
    CHOKEPOINT = 9


class FrameworkComplianceSummaryView(proto.Enum):
    r"""Specifies the view of the framework compliance summary to be
    returned. New values may be added in the future.

    Values:
        FRAMEWORK_COMPLIANCE_SUMMARY_VIEW_UNSPECIFIED (0):
            The default / unset value. The API will
            default to the BASIC view.
        FRAMEWORK_COMPLIANCE_SUMMARY_VIEW_BASIC (1):
            Includes basic compliance metadata, but omits
            trend data.
        FRAMEWORK_COMPLIANCE_SUMMARY_VIEW_FULL (2):
            Includes all information, including
            [finding_count][google.cloud.cloudsecuritycompliance.v1main.FrameworkComplianceSummary.finding_count]
            and
            [controls_passing_trend][google.cloud.cloudsecuritycompliance.v1main.FrameworkComplianceSummary.controls_passing_trend].
            Trend data is provided for the last 30 days.
    """

    FRAMEWORK_COMPLIANCE_SUMMARY_VIEW_UNSPECIFIED = 0
    FRAMEWORK_COMPLIANCE_SUMMARY_VIEW_BASIC = 1
    FRAMEWORK_COMPLIANCE_SUMMARY_VIEW_FULL = 2


class ListFrameworkComplianceSummariesRequest(proto.Message):
    r"""The request message for
    [ListFrameworkComplianceSummariesRequest][google.cloud.cloudsecuritycompliance.v1.ListFrameworkComplianceSummariesRequest].

    Attributes:
        parent (str):
            Required. The parent scope for the framework
            compliance summary.
        page_size (int):
            Optional. The requested page size. The server
            might return fewer items than requested. If
            unspecified, the server picks an appropriate
            default.
        page_token (str):
            Optional. A token that identifies the page of
            results that the server should return.
        filter (str):
            Optional. The filtering results.
        view (google.cloud.cloudsecuritycompliance_v1.types.FrameworkComplianceSummaryView):
            Optional. Specifies the level of detail to
            return in the response.
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
    view: "FrameworkComplianceSummaryView" = proto.Field(
        proto.ENUM,
        number=5,
        enum="FrameworkComplianceSummaryView",
    )


class ListFrameworkComplianceSummariesResponse(proto.Message):
    r"""The response message for
    [ListFrameworkComplianceSummariesResponse][google.cloud.cloudsecuritycompliance.v1.ListFrameworkComplianceSummariesResponse].

    Attributes:
        framework_compliance_summaries (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.FrameworkComplianceSummary]):
            The list of framework compliance summaries.
        next_page_token (str):
            Output only. The token to retrieve the next
            page of results.
    """

    @property
    def raw_page(self):
        return self

    framework_compliance_summaries: MutableSequence["FrameworkComplianceSummary"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="FrameworkComplianceSummary",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class FrameworkComplianceReport(proto.Message):
    r"""The response message for [GetFrameworkComplianceReport][].

    Attributes:
        framework (str):
            The name of the framework.
        framework_description (str):
            The description of the framework.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last updated time of the
            report.
        control_assessment_details (google.cloud.cloudsecuritycompliance_v1.types.ControlAssessmentDetails):
            The control assessment details of the
            framework.
        framework_type (google.cloud.cloudsecuritycompliance_v1.types.Framework.FrameworkType):
            The type of framework.
        supported_cloud_providers (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.CloudProvider]):
            The list of cloud providers supported by the
            framework.
        framework_categories (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.FrameworkCategory]):
            The list of framework categories supported.
        framework_display_name (str):
            Optional. The display name for the framework.
        name (str):
            Identifier. The name of the framework
            compliance report.
        major_revision_id (int):
            The latest major revision ID of the
            framework.
        minor_revision_id (int):
            The latest minor revision ID of the latest
            major revision of the framework.
        target_resource_details (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.TargetResourceDetails]):
            The target resource details of the framework.
    """

    framework: str = proto.Field(
        proto.STRING,
        number=1,
    )
    framework_description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    control_assessment_details: "ControlAssessmentDetails" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="ControlAssessmentDetails",
    )
    framework_type: common.Framework.FrameworkType = proto.Field(
        proto.ENUM,
        number=5,
        enum=common.Framework.FrameworkType,
    )
    supported_cloud_providers: MutableSequence[common.CloudProvider] = (
        proto.RepeatedField(
            proto.ENUM,
            number=6,
            enum=common.CloudProvider,
        )
    )
    framework_categories: MutableSequence[common.FrameworkCategory] = (
        proto.RepeatedField(
            proto.ENUM,
            number=7,
            enum=common.FrameworkCategory,
        )
    )
    framework_display_name: str = proto.Field(
        proto.STRING,
        number=8,
    )
    name: str = proto.Field(
        proto.STRING,
        number=9,
    )
    major_revision_id: int = proto.Field(
        proto.INT64,
        number=10,
    )
    minor_revision_id: int = proto.Field(
        proto.INT64,
        number=11,
    )
    target_resource_details: MutableSequence["TargetResourceDetails"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=12,
            message="TargetResourceDetails",
        )
    )


class FetchFrameworkComplianceReportRequest(proto.Message):
    r"""The request message for [FetchFrameworkComplianceReport][].

    Attributes:
        name (str):
            Required. The name of the framework
            compliance report to retrieve.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The end time of the report.
        filter (str):
            Optional. The filtering results.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListFindingSummariesRequest(proto.Message):
    r"""The request message for [ListFindingSummaries][].

    Attributes:
        parent (str):
            Required. The parent scope for the framework
            overview page.
        page_size (int):
            Optional. The requested page size. The server
            might return fewer items than  requested. If
            unspecified, the server picks an appropriate
            default.
        page_token (str):
            Optional. A token that identifies the page of
            results that the server should return.
        filter (str):
            Optional. The filtering results.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The end time of the finding
            summary.
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
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )


class ListFindingSummariesResponse(proto.Message):
    r"""The response message for [ListFindingSummaries][].

    Attributes:
        finding_summaries (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.FindingSummary]):
            List of finding summary by category.
        next_page_token (str):
            Output only. The token to retrieve the next
            page of results.
    """

    @property
    def raw_page(self):
        return self

    finding_summaries: MutableSequence["FindingSummary"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="FindingSummary",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListControlComplianceSummariesRequest(proto.Message):
    r"""The request message for [ListControlComplianceSummaries][].

    Attributes:
        parent (str):
            Required. The parent scope for the framework
            overview page.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The end time of the control
            compliance summary.
        page_size (int):
            Optional. The requested page size. The server
            might return fewer items than requested. If
            unspecified, the server picks an appropriate
            default.
        page_token (str):
            Optional. A token that identifies the page of
            results that the server should return.
        filter (str):
            Optional. The filtering results.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListControlComplianceSummariesResponse(proto.Message):
    r"""The response message for [ListControlComplianceSummaries][].

    Attributes:
        control_compliance_summaries (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.ControlComplianceSummary]):
            The list of control compliance details.
        next_page_token (str):
            Output only. The token to retrieve the next
            page of results.
    """

    @property
    def raw_page(self):
        return self

    control_compliance_summaries: MutableSequence["ControlComplianceSummary"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="ControlComplianceSummary",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AggregateFrameworkComplianceReportRequest(proto.Message):
    r"""The request message for [AggregateFrameworkComplianceReport][].

    Attributes:
        name (str):
            Required. The name of the aggregated compliance report over
            time to retrieve.

            The supported format is:
            ``organizations/{organization_id}/locations/{location}/frameworkComplianceReports/{framework_compliance_report}``
        interval (google.type.interval_pb2.Interval):
            Optional. The start and end time range for
            the aggregated compliance report.
        filter (str):
            Optional. The filtering results.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    interval: interval_pb2.Interval = proto.Field(
        proto.MESSAGE,
        number=2,
        message=interval_pb2.Interval,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=3,
    )


class AggregateFrameworkComplianceReportResponse(proto.Message):
    r"""The response message for [AggregateFrameworkComplianceReport][].

    Attributes:
        aggregated_compliance_reports (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.AggregatedComplianceReport]):
            The list of aggregated compliance reports.
    """

    aggregated_compliance_reports: MutableSequence["AggregatedComplianceReport"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="AggregatedComplianceReport",
        )
    )


class ControlAssessmentDetails(proto.Message):
    r"""The details for a control assessment.

    Attributes:
        passing_controls (int):
            The number of controls that are passing or
            not assessed.
        failing_controls (int):
            The number of controls that are failing.
        assessed_passing_controls (int):
            The number of controls that were assessed and
            are passing.
        not_assessed_controls (int):
            The number of controls that aren't assessed
            because they require manual review.
    """

    passing_controls: int = proto.Field(
        proto.INT32,
        number=1,
    )
    failing_controls: int = proto.Field(
        proto.INT32,
        number=2,
    )
    assessed_passing_controls: int = proto.Field(
        proto.INT32,
        number=3,
    )
    not_assessed_controls: int = proto.Field(
        proto.INT32,
        number=4,
    )


class FrameworkComplianceSummary(proto.Message):
    r"""The details for a framework compliance summary.

    Attributes:
        framework (str):
            The name of the framework.
        control_assessment_details (google.cloud.cloudsecuritycompliance_v1.types.ControlAssessmentDetails):
            The control assessment details of the
            framework.
        framework_type (google.cloud.cloudsecuritycompliance_v1.types.Framework.FrameworkType):
            The type of framework.
        supported_cloud_providers (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.CloudProvider]):
            The list of cloud providers supported by the
            framework.
        framework_categories (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.FrameworkCategory]):
            The list of framework categories supported by
            the framework.
        framework_display_name (str):
            Optional. The display name for the framework.
        name (str):
            Identifier. The name of the framework
            compliance summary.
        major_revision_id (int):
            The major revision ID of the framework.
        minor_revision_id (int):
            The minor revision ID of the framework.
        target_resource_details (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.TargetResourceDetails]):
            The target resource details for the
            framework.
        finding_count (int):
            Output only. The count of the findings
            generated against the framework.
        controls_passing_trend (google.cloud.cloudsecuritycompliance_v1.types.Trend):
            Output only. The trend of controls that are
            passing for the given duration.
    """

    framework: str = proto.Field(
        proto.STRING,
        number=1,
    )
    control_assessment_details: "ControlAssessmentDetails" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ControlAssessmentDetails",
    )
    framework_type: common.Framework.FrameworkType = proto.Field(
        proto.ENUM,
        number=3,
        enum=common.Framework.FrameworkType,
    )
    supported_cloud_providers: MutableSequence[common.CloudProvider] = (
        proto.RepeatedField(
            proto.ENUM,
            number=4,
            enum=common.CloudProvider,
        )
    )
    framework_categories: MutableSequence[common.FrameworkCategory] = (
        proto.RepeatedField(
            proto.ENUM,
            number=5,
            enum=common.FrameworkCategory,
        )
    )
    framework_display_name: str = proto.Field(
        proto.STRING,
        number=6,
    )
    name: str = proto.Field(
        proto.STRING,
        number=7,
    )
    major_revision_id: int = proto.Field(
        proto.INT64,
        number=8,
    )
    minor_revision_id: int = proto.Field(
        proto.INT64,
        number=9,
    )
    target_resource_details: MutableSequence["TargetResourceDetails"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=10,
            message="TargetResourceDetails",
        )
    )
    finding_count: int = proto.Field(
        proto.INT64,
        number=11,
    )
    controls_passing_trend: "Trend" = proto.Field(
        proto.MESSAGE,
        number=12,
        message="Trend",
    )


class FindingSummary(proto.Message):
    r"""The details for a finding.

    Attributes:
        finding_category (str):
            The category of the finding.
        finding_class (google.cloud.cloudsecuritycompliance_v1.types.FindingClass):
            The class of the finding.
        severity (google.cloud.cloudsecuritycompliance_v1.types.Severity):
            The severity of the finding.
        finding_count (int):
            The count of the finding.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last updated time of the
            finding.
        related_frameworks (MutableSequence[str]):
            Optional. The list of compliance frameworks
            that the finding belongs to.
        name (str):
            Identifier. The name of the finding summary.
    """

    finding_category: str = proto.Field(
        proto.STRING,
        number=1,
    )
    finding_class: "FindingClass" = proto.Field(
        proto.ENUM,
        number=2,
        enum="FindingClass",
    )
    severity: common.Severity = proto.Field(
        proto.ENUM,
        number=3,
        enum=common.Severity,
    )
    finding_count: int = proto.Field(
        proto.INT64,
        number=4,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    related_frameworks: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    name: str = proto.Field(
        proto.STRING,
        number=7,
    )


class ControlComplianceSummary(proto.Message):
    r"""The details for control compliance.

    Attributes:
        control (str):
            The name of the control.
        display_name (str):
            The display name of the control.
        description (str):
            The description of the control.
        overall_evaluation_state (google.cloud.cloudsecuritycompliance_v1.types.EvaluationState):
            Output only. The overall evaluation status of
            the control.
        total_findings_count (int):
            The total number of findings for the control.
        compliance_frameworks (MutableSequence[str]):
            The list of compliance frameworks that the
            control belongs to.
        similar_controls (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.SimilarControls]):
            The list of similar controls.
        cloud_control_reports (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.CloudControlReport]):
            The list of cloud control reports.
        control_responsibility_type (google.cloud.cloudsecuritycompliance_v1.types.RegulatoryControlResponsibilityType):
            The responsibility type for the control.
        is_fake_control (bool):
            Whether the control is a fake control. Fake
            controls are created and mapped to cloud
            controls that don't belong to a control group.
        name (str):
            Identifier. The name of the control
            compliance summary.
    """

    control: str = proto.Field(
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
    overall_evaluation_state: "EvaluationState" = proto.Field(
        proto.ENUM,
        number=4,
        enum="EvaluationState",
    )
    total_findings_count: int = proto.Field(
        proto.INT32,
        number=5,
    )
    compliance_frameworks: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    similar_controls: MutableSequence["SimilarControls"] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="SimilarControls",
    )
    cloud_control_reports: MutableSequence["CloudControlReport"] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message="CloudControlReport",
    )
    control_responsibility_type: common.RegulatoryControlResponsibilityType = (
        proto.Field(
            proto.ENUM,
            number=9,
            enum=common.RegulatoryControlResponsibilityType,
        )
    )
    is_fake_control: bool = proto.Field(
        proto.BOOL,
        number=10,
    )
    name: str = proto.Field(
        proto.STRING,
        number=11,
    )


class CloudControlReport(proto.Message):
    r"""The cloud control report.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        manual_cloud_control_assessment_details (google.cloud.cloudsecuritycompliance_v1.types.ManualCloudControlAssessmentDetails):
            The details of a manual cloud control
            assessment.

            This field is a member of `oneof`_ ``assessment_details``.
        cloud_control_assessment_details (google.cloud.cloudsecuritycompliance_v1.types.CloudControlAssessmentDetails):
            The details of a cloud control assessment.

            This field is a member of `oneof`_ ``assessment_details``.
        cloud_control (str):
            The name of the cloud control.
        display_name (str):
            The display name of the cloud control.
        description (str):
            The description of the cloud control.
        categories (MutableSequence[str]):
            The list of categories for the cloud control.
        similar_controls (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.SimilarControls]):
            The list of similar controls.
        cloud_control_type (google.cloud.cloudsecuritycompliance_v1.types.CloudControl.Type):
            The type of the cloud control.
        finding_category (str):
            The category of the finding.
        rules (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.Rule]):
            The list of rules that correspond to the
            cloud control.
        finding_severity (google.cloud.cloudsecuritycompliance_v1.types.Severity):
            The severity of the finding.
        enforcement_mode (google.cloud.cloudsecuritycompliance_v1.types.EnforcementMode):
            The enforcement mode of the cloud control.
        cloud_control_deployment (str):
            The name of the cloud control deployment.
        major_revision_id (int):
            The major revision ID of the cloud control.
        minor_revision_id (int):
            The minor revision ID of the cloud control.
        framework_major_revision_ids (MutableSequence[int]):
            The major revision IDs of the frameworks that
            the cloud control belongs to.
    """

    manual_cloud_control_assessment_details: "ManualCloudControlAssessmentDetails" = (
        proto.Field(
            proto.MESSAGE,
            number=13,
            oneof="assessment_details",
            message="ManualCloudControlAssessmentDetails",
        )
    )
    cloud_control_assessment_details: "CloudControlAssessmentDetails" = proto.Field(
        proto.MESSAGE,
        number=14,
        oneof="assessment_details",
        message="CloudControlAssessmentDetails",
    )
    cloud_control: str = proto.Field(
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
    categories: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    similar_controls: MutableSequence["SimilarControls"] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="SimilarControls",
    )
    cloud_control_type: common.CloudControl.Type = proto.Field(
        proto.ENUM,
        number=10,
        enum=common.CloudControl.Type,
    )
    finding_category: str = proto.Field(
        proto.STRING,
        number=11,
    )
    rules: MutableSequence[common.Rule] = proto.RepeatedField(
        proto.MESSAGE,
        number=12,
        message=common.Rule,
    )
    finding_severity: common.Severity = proto.Field(
        proto.ENUM,
        number=15,
        enum=common.Severity,
    )
    enforcement_mode: common.EnforcementMode = proto.Field(
        proto.ENUM,
        number=16,
        enum=common.EnforcementMode,
    )
    cloud_control_deployment: str = proto.Field(
        proto.STRING,
        number=17,
    )
    major_revision_id: int = proto.Field(
        proto.INT64,
        number=18,
    )
    minor_revision_id: int = proto.Field(
        proto.INT64,
        number=19,
    )
    framework_major_revision_ids: MutableSequence[int] = proto.RepeatedField(
        proto.INT64,
        number=20,
    )


class ManualCloudControlAssessmentDetails(proto.Message):
    r"""The details for a manual cloud control assessment.

    Attributes:
        manual_cloud_control_guide (MutableSequence[str]):
            The guide for assessing a cloud control
            manually.
    """

    manual_cloud_control_guide: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class CloudControlAssessmentDetails(proto.Message):
    r"""The cloud control assessment details for non-manual cloud
    controls.

    Attributes:
        findings_count (int):
            The number of findings for the cloud control.
        evaluation_state (google.cloud.cloudsecuritycompliance_v1.types.EvaluationState):
            Output only. The evaluation status of the
            cloud control.
    """

    findings_count: int = proto.Field(
        proto.INT32,
        number=1,
    )
    evaluation_state: "EvaluationState" = proto.Field(
        proto.ENUM,
        number=2,
        enum="EvaluationState",
    )


class SimilarControls(proto.Message):
    r"""The similar controls.

    Attributes:
        framework (str):
            The name of the framework.
        control_id (str):
            The ID of the control.
    """

    framework: str = proto.Field(
        proto.STRING,
        number=1,
    )
    control_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AggregatedComplianceReport(proto.Message):
    r"""The aggregated compliance report.

    Attributes:
        control_assessment_details (google.cloud.cloudsecuritycompliance_v1.types.ControlAssessmentDetails):
            The control assessment details of the
            framework.
        report_time (google.protobuf.timestamp_pb2.Timestamp):
            The report time of the aggregated compliance
            report.
    """

    control_assessment_details: "ControlAssessmentDetails" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ControlAssessmentDetails",
    )
    report_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


class TargetResourceDetails(proto.Message):
    r"""The details for a target resource.

    Attributes:
        framework_deployment (str):
            The framework deployment name for the target resource.

            For example,
            ``organizations/{organization_id}/locations/{location}/frameworkDeployments/{framework_deployment_id}``
        target_resource_display_name (str):
            The display name of the target resource. For example,
            ``google.com``, ``staging-project``, or
            ``development-folder``.
        target_resource (str):
            The target resource. For example,
            ``organizations/1234567890``, ``projects/1234567890``, or
            ``folders/1234567890``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The create time of the target resource.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            The update time of the target resource.
        major_revision_id (int):
            The major revision ID of the framework for
            the target resource.
        minor_revision_id (int):
            The minor revision ID of the framework for
            the target resource.
    """

    framework_deployment: str = proto.Field(
        proto.STRING,
        number=1,
    )
    target_resource_display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    target_resource: str = proto.Field(
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
    major_revision_id: int = proto.Field(
        proto.INT64,
        number=6,
    )
    minor_revision_id: int = proto.Field(
        proto.INT64,
        number=7,
    )


class Trend(proto.Message):
    r"""The trend of a compliance metric.

    Attributes:
        duration (google.protobuf.duration_pb2.Duration):
            Output only. The duration for the trend.
        value_percent (float):
            Output only. The trend value as a percentage.
            The value can be positive or negative.
    """

    duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=1,
        message=duration_pb2.Duration,
    )
    value_percent: float = proto.Field(
        proto.DOUBLE,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
