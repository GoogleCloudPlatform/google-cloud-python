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
        "ComplianceState",
        "GenerateFrameworkAuditScopeReportRequest",
        "GenerateFrameworkAuditScopeReportResponse",
        "ReportSummary",
        "CreateFrameworkAuditRequest",
        "FrameworkAuditDestination",
        "BucketDestination",
        "FrameworkAudit",
        "ListFrameworkAuditsRequest",
        "ListFrameworkAuditsResponse",
        "GetFrameworkAuditRequest",
        "CloudControlGroupAuditDetails",
        "FindingDetails",
        "ObservationDetails",
        "EvidenceDetails",
        "CloudControlAuditDetails",
    },
)


class ComplianceState(proto.Enum):
    r"""The state of compliance after evaluation is complete.

    Values:
        COMPLIANCE_STATE_UNSPECIFIED (0):
            Default value. This value is unused.
        COMPLIANT (1):
            The resource is compliant.
        VIOLATION (2):
            The resource has a violation.
        MANUAL_REVIEW_NEEDED (3):
            The resource requires manual review from you.
        ERROR (4):
            An error occurred while computing the
            resource status.
        AUDIT_NOT_SUPPORTED (5):
            The resource can't be audited.
    """

    COMPLIANCE_STATE_UNSPECIFIED = 0
    COMPLIANT = 1
    VIOLATION = 2
    MANUAL_REVIEW_NEEDED = 3
    ERROR = 4
    AUDIT_NOT_SUPPORTED = 5


class GenerateFrameworkAuditScopeReportRequest(proto.Message):
    r"""The request message for [GenerateFrameworkAuditScopeReport][].

    Attributes:
        scope (str):
            Required. The organization, folder or project for the audit
            report.

            Supported formats are the following:

            - ``projects/{project_id}/locations/{location}``
            - ``folders/{folder_id}/locations/{location}``
            - ``organizations/{organization_id}/locations/{location}``
        report_format (google.cloud.cloudsecuritycompliance_v1.types.GenerateFrameworkAuditScopeReportRequest.Format):
            Required. The format that the scope report
            bytes is returned in.
        compliance_framework (str):
            Required. The compliance framework that the
            scope report is generated for.
    """

    class Format(proto.Enum):
        r"""The set of options for the audit scope report format.

        Values:
            FORMAT_UNSPECIFIED (0):
                Default value. This value is unused.
            ODF (1):
                The report format is the Open Document Format
                (ODF).
        """

        FORMAT_UNSPECIFIED = 0
        ODF = 1

    scope: str = proto.Field(
        proto.STRING,
        number=1,
    )
    report_format: Format = proto.Field(
        proto.ENUM,
        number=2,
        enum=Format,
    )
    compliance_framework: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GenerateFrameworkAuditScopeReportResponse(proto.Message):
    r"""The response message for [GenerateFrameworkAuditScopeReport][].

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        scope_report_contents (bytes):
            The audit scope report content in byte
            format.

            This field is a member of `oneof`_ ``audit_report``.
        name (str):
            Identifier. The name of the audit report, in
            the format that was given in the request.
        compliance_framework (str):
            Required. The compliance framework that the
            audit scope report is generated for.
    """

    scope_report_contents: bytes = proto.Field(
        proto.BYTES,
        number=3,
        oneof="audit_report",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    compliance_framework: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ReportSummary(proto.Message):
    r"""Additional information for an audit operation.

    Attributes:
        total_count (int):
            Output only. The total number of checks.
        compliant_count (int):
            Output only. The number of compliant checks.
        violation_count (int):
            Output only. The number of checks with
            violations.
        manual_review_needed_count (int):
            Output only. The number of checks with
            "manual review needed" status.
        error_count (int):
            Output only. The number of checks that can't
            be performed due to errors.
    """

    total_count: int = proto.Field(
        proto.INT32,
        number=1,
    )
    compliant_count: int = proto.Field(
        proto.INT32,
        number=2,
    )
    violation_count: int = proto.Field(
        proto.INT32,
        number=3,
    )
    manual_review_needed_count: int = proto.Field(
        proto.INT32,
        number=4,
    )
    error_count: int = proto.Field(
        proto.INT32,
        number=5,
    )


class CreateFrameworkAuditRequest(proto.Message):
    r"""The request message for [CreateFrameworkAudit][].

    Attributes:
        parent (str):
            Required. The parent resource where this framework audit is
            created.

            Supported formats are the following:

            - ``organizations/{organization_id}/locations/{location}``
            - ``folders/{folder_id}/locations/{location}``
            - ``projects/{project_id}/locations/{location}``
        framework_audit_id (str):
            Optional. The ID to use for the framework audit. The ID
            becomes the final component of the framework audit's full
            resource name.

            The ID must be between 4-63 characters, and valid characters
            are ``\[a-z][0-9]-\``.
        framework_audit (google.cloud.cloudsecuritycompliance_v1.types.FrameworkAudit):
            Required. The framework audit to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    framework_audit_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    framework_audit: "FrameworkAudit" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="FrameworkAudit",
    )


class FrameworkAuditDestination(proto.Message):
    r"""A destination for the framework audit.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        bucket (google.cloud.cloudsecuritycompliance_v1.types.BucketDestination):
            The Cloud Storage bucket destination.

            This field is a member of `oneof`_ ``destination_type``.
    """

    bucket: "BucketDestination" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="destination_type",
        message="BucketDestination",
    )


class BucketDestination(proto.Message):
    r"""A Cloud Storage bucket destination.

    Attributes:
        bucket_uri (str):
            Required. The URI of the Cloud Storage
            bucket.
        framework_audit_format (google.cloud.cloudsecuritycompliance_v1.types.BucketDestination.Format):
            Optional. The format of the framework audit.
    """

    class Format(proto.Enum):
        r"""The set of options for the framework audit format.

        Values:
            FORMAT_UNSPECIFIED (0):
                Default value. This value is unused.
            ODF (1):
                The format for the framework audit report is
                Open Document.
        """

        FORMAT_UNSPECIFIED = 0
        ODF = 1

    bucket_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    framework_audit_format: Format = proto.Field(
        proto.ENUM,
        number=3,
        enum=Format,
    )


class FrameworkAudit(proto.Message):
    r"""A framework audit.

    Attributes:
        name (str):
            Output only. Identifier. The name of the
            framework audit.
        framework_audit_id (str):
            Output only. The ID of the framework audit.
        compliance_framework (str):
            Output only. The compliance framework used
            for the audit.
        scope (str):
            Output only. The scope of the audit.
        framework_audit_destination (google.cloud.cloudsecuritycompliance_v1.types.FrameworkAuditDestination):
            Required. The destination for the audit
            reports.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time that the audit started.
        finish_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time that the audit
            finished.
        compliance_state (google.cloud.cloudsecuritycompliance_v1.types.ComplianceState):
            Output only. The overall compliance state of
            the audit.
        report_summary (google.cloud.cloudsecuritycompliance_v1.types.ReportSummary):
            Output only. The summary of the report.
        cloud_control_group_audit_details (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.CloudControlGroupAuditDetails]):
            Optional. The details for the cloud control
            groups within this audit.
        cloud_control_audit_details (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.CloudControlAuditDetails]):
            Optional. The details for the cloud controls
            within this audit.
        operation_id (str):
            Output only. The ID of the long-running
            operation.
        state (google.cloud.cloudsecuritycompliance_v1.types.FrameworkAudit.State):
            Output only. The framework audit state of the
            audit.
    """

    class State(proto.Enum):
        r"""The state of the framework audit.

        Values:
            STATE_UNSPECIFIED (0):
                Default value. This value is unused.
            SCHEDULED (1):
                The audit is scheduled.
            RUNNING (2):
                The audit is running.
            UPLOADING (3):
                The audit results are being uploaded.
            FAILED (4):
                The audit failed.
            SUCCEEDED (5):
                The audit completed successfully.
        """

        STATE_UNSPECIFIED = 0
        SCHEDULED = 1
        RUNNING = 2
        UPLOADING = 3
        FAILED = 4
        SUCCEEDED = 5

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    framework_audit_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    compliance_framework: str = proto.Field(
        proto.STRING,
        number=3,
    )
    scope: str = proto.Field(
        proto.STRING,
        number=4,
    )
    framework_audit_destination: "FrameworkAuditDestination" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="FrameworkAuditDestination",
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    finish_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    compliance_state: "ComplianceState" = proto.Field(
        proto.ENUM,
        number=8,
        enum="ComplianceState",
    )
    report_summary: "ReportSummary" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="ReportSummary",
    )
    cloud_control_group_audit_details: MutableSequence[
        "CloudControlGroupAuditDetails"
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message="CloudControlGroupAuditDetails",
    )
    cloud_control_audit_details: MutableSequence["CloudControlAuditDetails"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=11,
            message="CloudControlAuditDetails",
        )
    )
    operation_id: str = proto.Field(
        proto.STRING,
        number=12,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=13,
        enum=State,
    )


class ListFrameworkAuditsRequest(proto.Message):
    r"""The request message for [ListFrameworkAudits][].

    Attributes:
        parent (str):
            Required. The parent resource where the framework audits are
            listed.

            Supported formats are the following:

            - ``organizations/{organization_id}/locations/{location}``
            - ``folders/{folder_id}/locations/{location}``
            - ``projects/{project_id}/locations/{location}``
        page_size (int):
            Optional. The maximum number of framework
            audits to return. The service might return fewer
            audits than this value. If unspecified, a
            maximum of 10 framework audits are returned. The
            maximum value is 50; values above 50 are limited
            to 50.
        page_token (str):
            Optional. The ``next_page_token`` value that's returned from
            a previous list request, if any.
        filter (str):
            Optional. The filters to apply to the framework audits.
            Supported filters are ``compliance_framework``,
            ``compliance_state``, ``create_time,`` and
            ``framework_audit_name``. If the filter is invalid, an
            invalid argument error is returned. For syntax details, see
            [AIP-160][https://google.aip.dev/160].
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


class ListFrameworkAuditsResponse(proto.Message):
    r"""The response message for [ListFrameworkAudits][].

    Attributes:
        framework_audits (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.FrameworkAudit]):
            The framework audits.
        next_page_token (str):
            A token, which you can send as the ``page_token`` to
            retrieve the next page. If this field is omitted, there are
            no subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    framework_audits: MutableSequence["FrameworkAudit"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="FrameworkAudit",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetFrameworkAuditRequest(proto.Message):
    r"""The request message for [GetFrameworkAudit][].

    Attributes:
        name (str):
            Required. The name of the framework audit to retrieve.

            Supported formats are the following:

            - ``organizations/{organization_id}/locations/{location}/frameworkAudits/{frameworkAuditName}``
            - ``folders/{folder_id}/locations/{location}/frameworkAudits/{frameworkAuditName}``
            - ``projects/{project_id}/locations/{location}/frameworkAudits/{frameworkAuditName}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CloudControlGroupAuditDetails(proto.Message):
    r"""The details for a cloud control group.

    Attributes:
        cloud_control_group_id (str):
            Output only. The ID of the cloud control
            group.
        display_name (str):
            Output only. The display name of the cloud
            control group.
        description (str):
            Output only. The description of the cloud
            control group.
        responsibility_type (str):
            Output only. The responsibility type.
        google_responsibility_description (str):
            Output only. The description of Google's
            responsibility.
        google_responsibility_implementation (str):
            Output only. The implementation of Google's
            responsibility.
        customer_responsibility_description (str):
            Output only. The description of your
            responsibility.
        customer_responsibility_implementation (str):
            Output only. The implementation of your
            responsibility.
        compliance_state (google.cloud.cloudsecuritycompliance_v1.types.ComplianceState):
            Output only. The compliance state of the
            control group.
        control_id (str):
            Output only. The ID of the regulatory
            control.
        control_family (google.cloud.cloudsecuritycompliance_v1.types.ControlFamily):
            Output only. The control family.
        cloud_control_details (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.CloudControlAuditDetails]):
            Output only. The details for the cloud
            controls within this group.
        report_summary (google.cloud.cloudsecuritycompliance_v1.types.ReportSummary):
            Output only. The summary of the report.
    """

    cloud_control_group_id: str = proto.Field(
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
    responsibility_type: str = proto.Field(
        proto.STRING,
        number=4,
    )
    google_responsibility_description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    google_responsibility_implementation: str = proto.Field(
        proto.STRING,
        number=6,
    )
    customer_responsibility_description: str = proto.Field(
        proto.STRING,
        number=7,
    )
    customer_responsibility_implementation: str = proto.Field(
        proto.STRING,
        number=8,
    )
    compliance_state: "ComplianceState" = proto.Field(
        proto.ENUM,
        number=9,
        enum="ComplianceState",
    )
    control_id: str = proto.Field(
        proto.STRING,
        number=10,
    )
    control_family: common.ControlFamily = proto.Field(
        proto.MESSAGE,
        number=11,
        message=common.ControlFamily,
    )
    cloud_control_details: MutableSequence["CloudControlAuditDetails"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=12,
            message="CloudControlAuditDetails",
        )
    )
    report_summary: "ReportSummary" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="ReportSummary",
    )


class FindingDetails(proto.Message):
    r"""The details for a finding.

    Attributes:
        name (str):
            Output only. The name of the finding.
        compliance_state (google.cloud.cloudsecuritycompliance_v1.types.ComplianceState):
            Output only. The compliance state of the
            finding.
        observation (google.cloud.cloudsecuritycompliance_v1.types.ObservationDetails):
            Output only. The observation details for the
            finding.
        evidence (google.cloud.cloudsecuritycompliance_v1.types.EvidenceDetails):
            Output only. The evidence details for the
            finding.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    compliance_state: "ComplianceState" = proto.Field(
        proto.ENUM,
        number=2,
        enum="ComplianceState",
    )
    observation: "ObservationDetails" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ObservationDetails",
    )
    evidence: "EvidenceDetails" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="EvidenceDetails",
    )


class ObservationDetails(proto.Message):
    r"""The observation details for a finding.

    Attributes:
        current_value (str):
            Output only. The current value.
        expected_value (str):
            Optional. The expected value.
        guidance (str):
            Output only. Any guidance for the
            observation.
    """

    current_value: str = proto.Field(
        proto.STRING,
        number=1,
    )
    expected_value: str = proto.Field(
        proto.STRING,
        number=2,
    )
    guidance: str = proto.Field(
        proto.STRING,
        number=3,
    )


class EvidenceDetails(proto.Message):
    r"""The evidence details for a finding.

    Attributes:
        resource (str):
            Output only. The resource identifier.
        service (str):
            Output only. The service identifier.
        evidence_path (str):
            Output only. The path to the evidence.
    """

    resource: str = proto.Field(
        proto.STRING,
        number=1,
    )
    service: str = proto.Field(
        proto.STRING,
        number=2,
    )
    evidence_path: str = proto.Field(
        proto.STRING,
        number=3,
    )


class CloudControlAuditDetails(proto.Message):
    r"""The details for a cloud control audit.

    Attributes:
        cloud_control (str):
            Output only. The name of the cloud control.
        cloud_control_id (str):
            Output only. The ID of the cloud control.
        cloud_control_description (str):
            Output only. The description of the cloud
            control.
        compliance_state (google.cloud.cloudsecuritycompliance_v1.types.ComplianceState):
            Output only. The overall status of the
            findings for the control.
        report_summary (google.cloud.cloudsecuritycompliance_v1.types.ReportSummary):
            Output only. The summary of the report.
        findings (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.FindingDetails]):
            Output only. The findings for the control.
    """

    cloud_control: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cloud_control_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    cloud_control_description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    compliance_state: "ComplianceState" = proto.Field(
        proto.ENUM,
        number=4,
        enum="ComplianceState",
    )
    report_summary: "ReportSummary" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="ReportSummary",
    )
    findings: MutableSequence["FindingDetails"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="FindingDetails",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
