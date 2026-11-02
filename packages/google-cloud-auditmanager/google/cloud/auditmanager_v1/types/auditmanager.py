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
    package="google.cloud.auditmanager.v1",
    manifest={
        "OperationState",
        "ComplianceState",
        "ScheduleState",
        "EnrollResourceRequest",
        "GenerateAuditScopeReportRequest",
        "GenerateAuditReportRequest",
        "GetResourceEnrollmentStatusRequest",
        "ListResourceEnrollmentStatusesRequest",
        "ListResourceEnrollmentStatusesResponse",
        "ListAuditReportsRequest",
        "ListAuditReportsResponse",
        "GetAuditReportRequest",
        "ListControlsRequest",
        "ListControlsResponse",
        "ReportGenerationProgress",
        "Enrollment",
        "AuditScopeReport",
        "OperationMetadata",
        "ResourceEnrollmentStatus",
        "AuditReport",
        "ControlFamily",
        "Control",
        "DestinationDetails",
        "ReportSummary",
        "ControlDetails",
        "CreateAuditScheduleRequest",
        "UpdateAuditScheduleRequest",
        "GetAuditScheduleRequest",
        "ListAuditSchedulesRequest",
        "ListAuditSchedulesResponse",
        "AuditSchedule",
        "ScheduleConfig",
    },
)


class OperationState(proto.Enum):
    r"""Different execution states of the Audit Manager service.

    Values:
        OPERATION_STATE_UNSPECIFIED (0):
            Default value. This value is unused.
        OPERATION_STATE_NOT_STARTED (10):
            Audit generation process hasn't started.
        OPERATION_STATE_EVALUATION_IN_PROGRESS (20):
            Evaluation process is in progress.
        OPERATION_STATE_EVALUATION_DONE (21):
            Evaluation process is completed.
        OPERATION_STATE_EVIDENCE_REPORT_GENERATION_IN_PROGRESS (30):
            Report generation process is in progress.
        OPERATION_STATE_EVIDENCE_REPORT_GENERATION_DONE (31):
            Report generation process is completed.
        OPERATION_STATE_EVIDENCE_UPLOAD_IN_PROGRESS (40):
            The audit report and evidence are being
            uploaded to your bucket.
        OPERATION_STATE_DONE (50):
            The audit report and evidence are uploaded to
            your bucket.
        OPERATION_STATE_FAILED (60):
            Audit report generation process failed.
    """

    OPERATION_STATE_UNSPECIFIED = 0
    OPERATION_STATE_NOT_STARTED = 10
    OPERATION_STATE_EVALUATION_IN_PROGRESS = 20
    OPERATION_STATE_EVALUATION_DONE = 21
    OPERATION_STATE_EVIDENCE_REPORT_GENERATION_IN_PROGRESS = 30
    OPERATION_STATE_EVIDENCE_REPORT_GENERATION_DONE = 31
    OPERATION_STATE_EVIDENCE_UPLOAD_IN_PROGRESS = 40
    OPERATION_STATE_DONE = 50
    OPERATION_STATE_FAILED = 60


class ComplianceState(proto.Enum):
    r"""Compliance state after evaluation.

    Values:
        COMPLIANCE_STATE_UNSPECIFIED (0):
            Default value. This value is unused.
        COMPLIANT (1):
            The resource is compliant.
        VIOLATION (2):
            The resource isn't compliant.
        MANUAL_REVIEW_NEEDED (3):
            You must complete a manual review.
        ERROR (4):
            An error was encountered during the
            evaluation or evidence gathering process.
        AUDIT_NOT_SUPPORTED (5):
            The resource can't be audited.
    """

    COMPLIANCE_STATE_UNSPECIFIED = 0
    COMPLIANT = 1
    VIOLATION = 2
    MANUAL_REVIEW_NEEDED = 3
    ERROR = 4
    AUDIT_NOT_SUPPORTED = 5


class ScheduleState(proto.Enum):
    r"""State of an audit schedule.

    Values:
        SCHEDULE_STATE_UNSPECIFIED (0):
            Default value. This value is unused.
        SCHEDULE_STATE_ACTIVE (1):
            Schedule is active and will trigger runs.
        SCHEDULE_STATE_PAUSED (2):
            Schedule is paused and will not trigger runs.
        SCHEDULE_STATE_COMPLETED (3):
            Schedule end time has passed.
        SCHEDULE_STATE_FAILED_SETUP (4):
            Schedule setup failed during creation or
            update.
        SCHEDULE_STATE_ERROR (5):
            Schedule is in an error state due to
            persistent failure to trigger an audit. Manual
            intervention is required.
        SCHEDULE_STATE_DELETED (6):
            Schedule has been marked for deletion by the
            user.
    """

    SCHEDULE_STATE_UNSPECIFIED = 0
    SCHEDULE_STATE_ACTIVE = 1
    SCHEDULE_STATE_PAUSED = 2
    SCHEDULE_STATE_COMPLETED = 3
    SCHEDULE_STATE_FAILED_SETUP = 4
    SCHEDULE_STATE_ERROR = 5
    SCHEDULE_STATE_DELETED = 6


class EnrollResourceRequest(proto.Message):
    r"""Request message for
    [EnrollResource][google.cloud.auditmanager.v1.AuditManager.EnrollResource].

    Attributes:
        scope (str):
            Required. Organization, folder, or project to enroll in
            Audit Manager, in one of the following formats:

            - ``projects/{project}/locations/{location}``
            - ``folders/{folder}/locations/{location}``
            - ``organizations/{organization}/locations/{location}``
        destinations (MutableSequence[google.cloud.auditmanager_v1.types.EnrollResourceRequest.EligibleDestination]):
            Required. Cloud Storage buckets that you can
            upload your audit reports to during the audit
            process.

            When you enroll an organization or folder, you
            can choose a Cloud Storage bucket from any
            project in the organization or folder. If you
            run an audit at the project level using the
            service agent at the organization or folder
            level, all the buckets that are associated with
            the service agent are available.
        validate_only (bool):
            Optional. If ``true``, only validates the request and does
            not enroll the resource. This executes standard request
            validation (such as schema, IAM, and destination checks) and
            skips the apply phase.

            Use this field for the following purposes:

            - **Infrastructure as Code (IaC)**: Allow tools like
              Terraform to run dry-run mutations (e.g.,
              ``terraform plan``) without creating real resources or
              incurring costs.
            - **User Interface Validation**: Enable real-time form and
              permission validation in custom UIs before submitting
              requests.
            - **CI/CD & Automation**: Test your scripts, permissions,
              and parameters safely without consuming resource quotas.
    """

    class EligibleDestination(proto.Message):
        r"""Details about the bucket where you want to upload the audit
        report.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            eligible_gcs_bucket (str):
                The location of the Cloud Storage bucket where you want to
                upload the audit report and evidence during the
                [GenerateAuditReport][google.cloud.auditmanager.v1.AuditManager.GenerateAuditReport]
                API call.

                This field is a member of `oneof`_ ``eligible_destinations``.
        """

        eligible_gcs_bucket: str = proto.Field(
            proto.STRING,
            number=3,
            oneof="eligible_destinations",
        )

    scope: str = proto.Field(
        proto.STRING,
        number=1,
    )
    destinations: MutableSequence[EligibleDestination] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=EligibleDestination,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class GenerateAuditScopeReportRequest(proto.Message):
    r"""Request message for
    [GenerateAuditScopeReport][google.cloud.auditmanager.v1.AuditManager.GenerateAuditScopeReport].

    Attributes:
        scope (str):
            Required. Project or folder that the audit scope report is
            generated for, in one of the following formats:

            - ``projects/{project}/locations/{location}``
            - ``folders/{folder}/locations/{location}``
            - ``organizations/{organization}/locations/{location}``
        compliance_standard (str):
            Optional. Deprecated. The standard (industry or regulatory
            requirements) that the audit scope report is run against.

            Use the ``compliance_framework`` field instead.
        report_format (google.cloud.auditmanager_v1.types.GenerateAuditScopeReportRequest.AuditScopeReportFormat):
            Required. Format for the audit scope report.
        compliance_framework (str):
            Required. Framework (set of controls) that the audit scope
            report is generated against. For example, ``NIST_800_53``.
        validate_only (bool):
            Optional. If ``true``, only validates the request and does
            not generate the audit scope report. This executes standard
            request validation (such as schema, framework existence,
            scope, and IAM checks) and skips the apply phase.

            Use this field for the following purposes:

            - **Infrastructure as Code (IaC)**: Allow tools like
              Terraform to run dry-run mutations (e.g.,
              ``terraform plan``) without creating real resources or
              incurring costs.
            - **User Interface Validation**: Enable real-time form and
              permission validation in custom UIs before submitting
              requests.
            - **CI/CD & Automation**: Test your scripts, permissions,
              and parameters safely without consuming resource quotas.
    """

    class AuditScopeReportFormat(proto.Enum):
        r"""Format for the audit scope report.

        Values:
            AUDIT_SCOPE_REPORT_FORMAT_UNSPECIFIED (0):
                Default value. This value is unused.
            AUDIT_SCOPE_REPORT_FORMAT_ODF (1):
                Open Document format.
        """

        AUDIT_SCOPE_REPORT_FORMAT_UNSPECIFIED = 0
        AUDIT_SCOPE_REPORT_FORMAT_ODF = 1

    scope: str = proto.Field(
        proto.STRING,
        number=2,
    )
    compliance_standard: str = proto.Field(
        proto.STRING,
        number=3,
    )
    report_format: AuditScopeReportFormat = proto.Field(
        proto.ENUM,
        number=4,
        enum=AuditScopeReportFormat,
    )
    compliance_framework: str = proto.Field(
        proto.STRING,
        number=5,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


class GenerateAuditReportRequest(proto.Message):
    r"""Request message for
    [GenerateAuditReport][google.cloud.auditmanager.v1.AuditManager.GenerateAuditReport].


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_uri (str):
            URL for the Cloud Storage bucket where the
            report and evidence is uploaded. You must select
            a bucket that was provided during the enrollment
            process.

            This field is a member of `oneof`_ ``destination``.
        scope (str):
            Required. Organization, folder, or project that the audit
            applies to, in one of the following formats:

            - ``projects/{project}/locations/{location}``
            - ``folders/{folder}/locations/{location}``
            - ``organizations/{organization}/locations/{location}``
        compliance_standard (str):
            Optional. Deprecated. Compliance standard for the audit
            report.

            Use the ``compliance_framework`` field instead.
        report_format (google.cloud.auditmanager_v1.types.GenerateAuditReportRequest.AuditReportFormat):
            Required. Format for the audit report.
        compliance_framework (str):
            Required. The framework that's used for the audit report.
            For example, ``NIST_800_53``.
        validate_only (bool):
            Optional. If ``true``, only validates the request and does
            not generate the audit report. This executes standard
            request validation (such as schema, framework existence,
            scope, and IAM checks) and skips the apply phase.

            Use this field for the following purposes:

            - **Infrastructure as Code (IaC)**: Allow tools like
              Terraform to run dry-run mutations (e.g.,
              ``terraform plan``) without creating real resources or
              incurring costs.
            - **User Interface Validation**: Enable real-time form and
              permission validation in custom UIs before submitting
              requests.
            - **CI/CD & Automation**: Test your scripts, permissions,
              and parameters safely without triggering expensive
              Long-Running Operations (LROs) or consuming resource
              quotas.
    """

    class AuditReportFormat(proto.Enum):
        r"""Format for the audit report.

        Values:
            AUDIT_REPORT_FORMAT_UNSPECIFIED (0):
                Default value. This value is unused.
            AUDIT_REPORT_FORMAT_ODF (1):
                Open Document format.
        """

        AUDIT_REPORT_FORMAT_UNSPECIFIED = 0
        AUDIT_REPORT_FORMAT_ODF = 1

    gcs_uri: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="destination",
    )
    scope: str = proto.Field(
        proto.STRING,
        number=1,
    )
    compliance_standard: str = proto.Field(
        proto.STRING,
        number=3,
    )
    report_format: AuditReportFormat = proto.Field(
        proto.ENUM,
        number=4,
        enum=AuditReportFormat,
    )
    compliance_framework: str = proto.Field(
        proto.STRING,
        number=5,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=8,
    )


class GetResourceEnrollmentStatusRequest(proto.Message):
    r"""Request message for
    [GetResourceEnrollmentStatus][google.cloud.auditmanager.v1.AuditManager.GetResourceEnrollmentStatus].

    Attributes:
        name (str):
            Required. Name of the resource enrollment status, in one of
            the following formats:

            - ``folders/{folder}/locations/{location}/resourceEnrollmentStatuses/{resource_enrollment_status}``
            - ``projects/{project}/locations/{location}/resourceEnrollmentStatuses/{resource_enrollment_status}``
            - ``organizations/{organization}/locations/{location}/resourceEnrollmentStatuses/{resource_enrollment_status}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListResourceEnrollmentStatusesRequest(proto.Message):
    r"""Request message for
    [ListResourceEnrollmentStatuses][google.cloud.auditmanager.v1.AuditManager.ListResourceEnrollmentStatuses].

    Attributes:
        parent (str):
            Required. Parent organization or folder to list enrollment
            statuses for, in one of the following formats:

            - ``folders/{folder}/locations/{location}``
            - ``organizations/{organization}/locations/{location}``
        page_size (int):
            Optional. Maximum number of items to return
            in a single page. The service might return fewer
            items than this value. If unspecified, the
            service picks an appropriate default. The
            maximum value is 100; values above 100 are
            reduced to 100.
        page_token (str):
            Optional. A page token, received from a
            previous call, to retrieve the next page of
            results.
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


class ListResourceEnrollmentStatusesResponse(proto.Message):
    r"""Response message for
    [ListResourceEnrollmentStatuses][google.cloud.auditmanager.v1.AuditManager.ListResourceEnrollmentStatuses].

    Attributes:
        resource_enrollment_statuses (MutableSequence[google.cloud.auditmanager_v1.types.ResourceEnrollmentStatus]):
            Resources with their enrollment status.
        next_page_token (str):
            Output only. A token that you can send as the ``page_token``
            in a subsequent request to retrieve the next page of
            results. If this field is empty, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    resource_enrollment_statuses: MutableSequence["ResourceEnrollmentStatus"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="ResourceEnrollmentStatus",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListAuditReportsRequest(proto.Message):
    r"""Request message for
    [ListAuditReports][google.cloud.auditmanager.v1.AuditManager.ListAuditReports].

    Attributes:
        parent (str):
            Required. Parent organization, folder, or project to list
            reports for, in one of the following formats:

            - ``projects/{project}/locations/{location}``
            - ``folders/{folder}/locations/{location}``
            - ``organizations/{organization}/locations/{location}``
        page_size (int):
            Optional. Maximum number of items to return
            in a single page. The service might return fewer
            items than this value. If unspecified, the
            service picks an appropriate default. The
            maximum value is 100; values above 100 are
            reduced to 100.
        page_token (str):
            Optional. A page token, received from a
            previous call, to retrieve the next page of
            results.
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


class ListAuditReportsResponse(proto.Message):
    r"""Response message for
    [ListAuditReports][google.cloud.auditmanager.v1.AuditManager.ListAuditReports].

    Attributes:
        audit_reports (MutableSequence[google.cloud.auditmanager_v1.types.AuditReport]):
            Output only. Audit reports.
        next_page_token (str):
            Output only. A token that you can send as the ``page_token``
            in a subsequent request to retrieve the next page of
            results. If this field is empty, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    audit_reports: MutableSequence["AuditReport"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AuditReport",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetAuditReportRequest(proto.Message):
    r"""Request message for
    [GetAuditReport][google.cloud.auditmanager.v1.AuditManager.GetAuditReport].

    Attributes:
        name (str):
            Required. Name of the audit report, in one of the following
            formats:

            - ``projects/{project}/locations/{location}/auditReports/{audit_report}``
            - ``folders/{folder}/locations/{location}/auditReports/{audit_report}``
            - ``organizations/{organization}/locations/{location}/auditReports/{audit_report}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListControlsRequest(proto.Message):
    r"""Request message for
    [ListControls][google.cloud.auditmanager.v1.AuditManager.ListControls].

    Attributes:
        parent (str):
            Required. Standard to list controls for, in one of the
            following formats:

            - ``projects/{project}/locations/{location}/standards/{standard}``
            - ``folders/{folder}/locations/{location}/standards/{standard}``
            - ``organizations/{organization}/locations/{location}/standards/{standard}``
        page_size (int):
            Optional. Maximum number of items to return
            in a single page. The service might return fewer
            items than this value. If unspecified, the
            service picks an appropriate default. The
            maximum value is 100; values above 100 are
            reduced to 100.
        page_token (str):
            Optional. A page token, received from a
            previous call, to retrieve the next page of
            results.
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


class ListControlsResponse(proto.Message):
    r"""Response message for
    [ListControls][google.cloud.auditmanager.v1.AuditManager.ListControls].

    Attributes:
        controls (MutableSequence[google.cloud.auditmanager_v1.types.Control]):
            Output only. Controls for a given regulatory
            standard.
        next_page_token (str):
            Output only. A token that you can send as the ``page_token``
            in a subsequent request to retrieve the next page of
            results. If this field is empty, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    controls: MutableSequence["Control"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Control",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ReportGenerationProgress(proto.Message):
    r"""Details about the current status of the report-generation
    process.

    Attributes:
        state (google.cloud.auditmanager_v1.types.OperationState):
            Output only. Current state of execution for
            report generation.
        failure_reason (str):
            Output only. Reason for failure during the audit report
            generation process. This field is set only if the
            ``OperationState`` attribute is ``OPERATION_STATE_FAILED``.
        evaluation_percent_complete (float):
            Progress of the evaluation process. The
            progress is defined in terms of percentage
            complete.
        report_generation_percent_complete (float):
            Report generation progress, defined in terms of percentage
            complete. Until evaluation is complete, this value is always
            ``0``.
        report_uploading_percent_complete (float):
            Report uploading progress, defined in terms of percentage
            complete. Until evaluation and report generation are
            complete, this value is always ``0``.
        destination_gcs_bucket (str):
            Output only. Cloud Storage bucket where the
            audit report is uploaded to after the evaluation
            process is completed.
        audit_report (str):
            Output only. Name of the audit report.
    """

    state: "OperationState" = proto.Field(
        proto.ENUM,
        number=1,
        enum="OperationState",
    )
    failure_reason: str = proto.Field(
        proto.STRING,
        number=2,
    )
    evaluation_percent_complete: float = proto.Field(
        proto.DOUBLE,
        number=20,
    )
    report_generation_percent_complete: float = proto.Field(
        proto.DOUBLE,
        number=30,
    )
    report_uploading_percent_complete: float = proto.Field(
        proto.DOUBLE,
        number=40,
    )
    destination_gcs_bucket: str = proto.Field(
        proto.STRING,
        number=50,
    )
    audit_report: str = proto.Field(
        proto.STRING,
        number=51,
    )


class Enrollment(proto.Message):
    r"""Organization, folder, or project to enroll for audit reports.

    Attributes:
        name (str):
            Identifier. Name of the enrollment, in one of the following
            formats:

            - ``projects/{project}/locations/{location}/enrollments/{enrollment}``
            - ``folders/{folder}/locations/{location}/enrollments/{enrollment}``
            - ``organizations/{organization}/locations/{location}/enrollments/{enrollment}``
        destination_details (MutableSequence[google.cloud.auditmanager_v1.types.DestinationDetails]):
            Output only. Cloud Storage buckets where you
            want to upload the audit reports.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    destination_details: MutableSequence["DestinationDetails"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="DestinationDetails",
    )


class AuditScopeReport(proto.Message):
    r"""Audit scope report.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        scope_report_contents (bytes):
            Audit scope report content in byte format.

            This field is a member of `oneof`_ ``audit_report``.
        name (str):
            Identifier. Name for the audit scope report, in one of the
            following formats:

            - ``projects/{project}/locations/{location}/auditScopeReports/{audit_scope_report}``
            - ``folders/{folder}/locations/{location}/auditScopeReports/{audit_scope_report}``
            - ``organizations/{organization}/locations/{location}/auditScopeReports/{audit_scope_report}``
    """

    scope_report_contents: bytes = proto.Field(
        proto.BYTES,
        number=1,
        oneof="audit_report",
    )
    name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class OperationMetadata(proto.Message):
    r"""Metadata for the long-running operation.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time that the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time that the operation finished
            running.
        target (str):
            Output only. A server-defined resource path
            for the target of the operation.
        verb (str):
            Output only. The name of the verb that was
            executed by the operation.
        status_message (str):
            Output only. A human-readable status of the
            operation, if any.
        requested_cancellation (bool):
            Output only. Whether you requested that the operation be
            cancelled. Operations that were cancelled successfully have
            an [Operation.error][google.longrunning.Operation.error]
            value with a status code
            [Code.CANCELLED][google.rpc.Status.code.CANCELLED].
        api_version (str):
            Output only. The API version used to start the operation.
            For example, ``v1``.
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


class ResourceEnrollmentStatus(proto.Message):
    r"""An organization, folder, or project with its enrollment
    status.

    Attributes:
        name (str):
            Identifier. Name of the resource enrollment status, in one
            of the following formats:

            - ``folders/{folder}/locations/{location}/resourceEnrollmentStatuses/{resource_enrollment_status}``
            - ``projects/{project}/locations/{location}/resourceEnrollmentStatuses/{resource_enrollment_status}``
            - ``organizations/{organization}/locations/{location}/resourceEnrollmentStatuses/{resource_enrollment_status}``
        enrollment (google.cloud.auditmanager_v1.types.Enrollment):
            Output only. Enrolled destination details for
            the organization, folder, or project.
        enrolled (bool):
            Output only. Deprecated. Whether the organization, folder,
            or project is enrolled. Use ``enrollment_state`` instead.
        display_name (str):
            Output only. Display name for the
            organization, folder, or project.
        enrollment_state (google.cloud.auditmanager_v1.types.ResourceEnrollmentStatus.ResourceEnrollmentState):
            Output only. Enrollment state of the
            organization, folder, or project.
    """

    class ResourceEnrollmentState(proto.Enum):
        r"""Different enrollment states of the resource and its parent.

        Values:
            RESOURCE_ENROLLMENT_STATE_UNSPECIFIED (0):
                Default value. This value is unused.
            NOT_ENROLLED (1):
                The resource isn't enrolled.
            INHERITED (2):
                The resource isn't enrolled but the parent is
                enrolled.
            ENROLLED (3):
                The resource is enrolled.
        """

        RESOURCE_ENROLLMENT_STATE_UNSPECIFIED = 0
        NOT_ENROLLED = 1
        INHERITED = 2
        ENROLLED = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    enrollment: "Enrollment" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Enrollment",
    )
    enrolled: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    enrollment_state: ResourceEnrollmentState = proto.Field(
        proto.ENUM,
        number=5,
        enum=ResourceEnrollmentState,
    )


class AuditReport(proto.Message):
    r"""An audit report.

    Attributes:
        name (str):
            Identifier. Name of the audit report, in one of the
            following formats:

            - ``projects/{project}/locations/{location}/auditReports/{audit_report}``
            - ``folders/{folder}/locations/{location}/auditReports/{audit_report}``
            - ``organizations/{organization}/locations/{location}/auditReports/{audit_report}``
        report_summary (google.cloud.auditmanager_v1.types.ReportSummary):
            Output only. Report summary that includes
            information about compliance and violation
            counts.
        operation_id (str):
            Output only. Client operation ID for the
            audit report.
        destination_details (google.cloud.auditmanager_v1.types.DestinationDetails):
            Output only. Cloud Storage bucket where the
            audit report is uploaded to.
        compliance_standard (str):
            Output only. Deprecated. Compliance standard to be audited
            against.

            Use the ``compliance_framework`` field instead.
        scope (str):
            Output only. Organization, folder, or project that the
            report is generated for, in one of the following formats:

            - ``projects/{project}/locations/{location}``
            - ``folders/{folder}/locations/{location}``
            - ``organizations/{organization}/locations/{location}``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Creation time of the audit
            report.
        control_details (MutableSequence[google.cloud.auditmanager_v1.types.ControlDetails]):
            Output only. Overall status of the controls.
        report_generation_state (google.cloud.auditmanager_v1.types.AuditReport.ReportGenerationState):
            Output only. State of audit report
            generation.
        compliance_framework (str):
            Output only. Compliance framework to use for the audit
            report. For example, ``CIS_GCP_FOUNDATIONS_V1_2_0``.
        scope_id (str):
            Output only. Project number, folder ID, or
            organization ID that the audit report was
            generated for.
    """

    class ReportGenerationState(proto.Enum):
        r"""Different states of report generation.

        Values:
            REPORT_GENERATION_STATE_UNSPECIFIED (0):
                Default value. This value is unused.
            IN_PROGRESS (1):
                The process is in progress. The operation can have any state
                except for ``OPERATION_STATE_DONE`` or
                ``OPERATION_STATE_FAILED``.
            COMPLETED (2):
                The process is completed. The operation state is
                ``OPERATION_STATE_DONE``.
            FAILED (3):
                The process has failed. The operation state is
                ``OPERATION_STATE_FAILED``.
            SUMMARY_UNKNOWN (4):
                The process completed, but the report
                summary's status is unknown. This state isn't
                used for new reports.
        """

        REPORT_GENERATION_STATE_UNSPECIFIED = 0
        IN_PROGRESS = 1
        COMPLETED = 2
        FAILED = 3
        SUMMARY_UNKNOWN = 4

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    report_summary: "ReportSummary" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ReportSummary",
    )
    operation_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    destination_details: "DestinationDetails" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="DestinationDetails",
    )
    compliance_standard: str = proto.Field(
        proto.STRING,
        number=5,
    )
    scope: str = proto.Field(
        proto.STRING,
        number=6,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    control_details: MutableSequence["ControlDetails"] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message="ControlDetails",
    )
    report_generation_state: ReportGenerationState = proto.Field(
        proto.ENUM,
        number=9,
        enum=ReportGenerationState,
    )
    compliance_framework: str = proto.Field(
        proto.STRING,
        number=10,
    )
    scope_id: str = proto.Field(
        proto.STRING,
        number=11,
    )


class ControlFamily(proto.Message):
    r"""Regulatory family of the control.

    Attributes:
        family_id (str):
            ID of the regulatory control family. To find the list of
            supported control families, use the
            [ListControls][google.cloud.auditmanager.v1.AuditManager.ListControls]
            method and review the ``control_family`` field in the
            response.
        display_name (str):
            Display name of the regulatory control
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


class Control(proto.Message):
    r"""A control.

    Attributes:
        id (str):
            Output only. Control identifier that's used
            to fetch the findings. The identifier is the
            same as the control report name.
        display_name (str):
            Output only. Display name of the control.
        family (google.cloud.auditmanager_v1.types.Control.Family):
            Output only. Category that the control
            belongs to.
        control_family (google.cloud.auditmanager_v1.types.ControlFamily):
            Output only. Regulatory family of the
            control.
        description (str):
            Output only. Description of the control.
        responsibility_type (str):
            Output only. Who is responsible for implementing this
            control. Set to one of the following values: ``GOOGLE``,
            ``CUSTOMER``, or ``SHARED``.
        google_responsibility_description (str):
            Output only. A description of Google's
            responsibility for this control.
        google_responsibility_implementation (str):
            Output only. A description of how Google
            implements its responsibility for this control.
        customer_responsibility_description (str):
            Output only. A description of your
            responsibility for this control.
        customer_responsibility_implementation (str):
            Output only. A description of how you can
            implement your responsibility for this control.
    """

    class Family(proto.Enum):
        r"""Category of the control.

        Values:
            FAMILY_UNSPECIFIED (0):
                Default value. This value is unused.
            AC (1):
                Access control.
            AT (2):
                Awareness and training.
            AU (3):
                Audit and accountability.
            CA (4):
                Certification, accreditation and security
                assessments.
            CM (5):
                Configuration management and change control.
            CP (6):
                Contingency planning and disaster recovery.
            IA (7):
                Identification and authentication.
            IR (8):
                Incident response.
            MA (9):
                Maintenance.
            MP (10):
                Media protection.
            PE (11):
                Physical and environmental protection.
            PL (12):
                Security planning.
            PS (13):
                Personnel security.
            RA (14):
                Risk assessment.
            SA (15):
                System services and acquisition.
            SC (16):
                System and communications protection.
            SI (17):
                System and information integrity.
            SR (18):
                Supply chain risk management.
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

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    family: Family = proto.Field(
        proto.ENUM,
        number=3,
        enum=Family,
    )
    control_family: "ControlFamily" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="ControlFamily",
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    responsibility_type: str = proto.Field(
        proto.STRING,
        number=5,
    )
    google_responsibility_description: str = proto.Field(
        proto.STRING,
        number=6,
    )
    google_responsibility_implementation: str = proto.Field(
        proto.STRING,
        number=7,
    )
    customer_responsibility_description: str = proto.Field(
        proto.STRING,
        number=8,
    )
    customer_responsibility_implementation: str = proto.Field(
        proto.STRING,
        number=9,
    )


class DestinationDetails(proto.Message):
    r"""Cloud Storage bucket where the audit report is uploaded to.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_bucket_uri (str):
            URI for the Cloud Storage bucket, in the format
            ``gs://{bucket_name}``.

            This field is a member of `oneof`_ ``destination``.
    """

    gcs_bucket_uri: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="destination",
    )


class ReportSummary(proto.Message):
    r"""Additional information about the number of checks that were
    made during an audit operation.

    Attributes:
        total_count (int):
            Total number of evaluated checks.
        compliant_count (int):
            Number of compliant checks.
        violation_count (int):
            Number of checks with violations.
        manual_review_needed_count (int):
            Number of checks that require a manual
            review.
        error_count (int):
            Number of checks that can't be performed due
            to errors.
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


class ControlDetails(proto.Message):
    r"""Evaluation details for a control.

    Attributes:
        control (google.cloud.auditmanager_v1.types.Control):
            Control that the findings are being reported
            for.
        compliance_state (google.cloud.auditmanager_v1.types.ComplianceState):
            Output only. Overall status of the findings
            for the control.
        control_report_summary (google.cloud.auditmanager_v1.types.ReportSummary):
            A control report summary that provides a
            high-level overview of the compliance controls
            and the assessment status.
    """

    control: "Control" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Control",
    )
    compliance_state: "ComplianceState" = proto.Field(
        proto.ENUM,
        number=2,
        enum="ComplianceState",
    )
    control_report_summary: "ReportSummary" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ReportSummary",
    )


class CreateAuditScheduleRequest(proto.Message):
    r"""Request message for
    [CreateAuditSchedule][google.cloud.auditmanager.v1.AuditManager.CreateAuditSchedule].

    Attributes:
        parent (str):
            Required. Project or folder that this audit schedule is for,
            in one of the following formats:

            - ``projects/{project}/locations/{location}``
            - ``folders/{folder}/locations/{location}``
        audit_schedule (google.cloud.auditmanager_v1.types.AuditSchedule):
            Required. Audit schedule to create.
        audit_schedule_id (str):
            Required. ID to use for the audit schedule,
            which becomes the final component of the audit
            schedule's resource name.
        validate_only (bool):
            Optional. If ``true``, only validates the request and does
            not create the audit schedule. This executes standard
            request validation (such as schema, framework existence,
            scope, and IAM checks) and skips the apply phase.

            Use this field for the following purposes:

            - **Infrastructure as Code (IaC)**: Allow tools like
              Terraform to run dry-run mutations (e.g.,
              ``terraform plan``) without creating real resources or
              incurring costs.
            - **User Interface Validation**: Enable real-time form and
              permission validation in custom UIs before submitting
              requests.
            - **CI/CD & Automation**: Test your scripts, permissions,
              and parameters safely without consuming resource quotas.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    audit_schedule: "AuditSchedule" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="AuditSchedule",
    )
    audit_schedule_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class UpdateAuditScheduleRequest(proto.Message):
    r"""Request message for
    [UpdateAuditSchedule][google.cloud.auditmanager.v1.AuditManager.UpdateAuditSchedule].

    Attributes:
        audit_schedule (google.cloud.auditmanager_v1.types.AuditSchedule):
            Required. Audit schedule to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. List of fields to update.
        validate_only (bool):
            Optional. If ``true``, only validates the request and does
            not update the audit schedule. This executes standard
            request validation (such as schema, framework existence,
            scope, and IAM checks) and skips the apply phase.

            Use this field for the following purposes:

            - **Infrastructure as Code (IaC)**: Allow tools like
              Terraform to run dry-run mutations (e.g.,
              ``terraform plan``) without creating real resources or
              incurring costs.
            - **User Interface Validation**: Enable real-time form and
              permission validation in custom UIs before submitting
              requests.
            - **CI/CD & Automation**: Test your scripts, permissions,
              and parameters safely without consuming resource quotas.
    """

    audit_schedule: "AuditSchedule" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="AuditSchedule",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class GetAuditScheduleRequest(proto.Message):
    r"""Request message for
    [GetAuditSchedule][google.cloud.auditmanager.v1.AuditManager.GetAuditSchedule].

    Attributes:
        name (str):
            Required. Name of the audit schedule to retrieve, in one of
            the following formats:

            - ``projects/{project}/locations/{location}/auditSchedules/{audit_schedule}``
            - ``folders/{folder}/locations/{location}/auditSchedules/{audit_schedule}``
            - ``organizations/{organization}/locations/{location}/auditSchedules/{audit_schedule}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListAuditSchedulesRequest(proto.Message):
    r"""Request message for
    [ListAuditSchedules][google.cloud.auditmanager.v1.AuditManager.ListAuditSchedules].

    Attributes:
        parent (str):
            Required. Parent for the audit schedule, in one of the
            following formats:

            - ``projects/{project}/locations/{location}``
            - ``folders/{folder}/locations/{location}``
            - ``organizations/{organization}/locations/{location}``
        page_size (int):
            Optional. Maximum number of items to return
            in a single page. The service might return fewer
            items than this value. If unspecified, the
            service picks an appropriate default. The
            maximum value is 100; values above 100 are
            reduced to 100.
        page_token (str):
            Optional. A page token, received from a
            previous call, to retrieve the next page of
            results.
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


class ListAuditSchedulesResponse(proto.Message):
    r"""Response message for
    [ListAuditSchedules][google.cloud.auditmanager.v1.AuditManager.ListAuditSchedules].

    Attributes:
        audit_schedules (MutableSequence[google.cloud.auditmanager_v1.types.AuditSchedule]):
            List of audit schedules.
        next_page_token (str):
            A token that you can send as the ``page_token`` in a
            subsequent request to retrieve the next page of results. If
            this field is empty, there are no subsequent pages.
        unreachable (MutableSequence[str]):
            Locations that can't be reached.
    """

    @property
    def raw_page(self):
        return self

    audit_schedules: MutableSequence["AuditSchedule"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AuditSchedule",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class AuditSchedule(proto.Message):
    r"""An audit schedule, in one of the following formats:

    - ``projects/{project}/locations/{location}/auditSchedules/{audit_schedule}``
    - ``folders/{folder}/locations/{location}/auditSchedules/{audit_schedule}``

    Attributes:
        name (str):
            Identifier. Unique identifier for the audit schedule.
            Format:
            projects/{project}/locations/{location}/auditSchedules/{audit_schedule}
            folders/{folder}/locations/{location}/auditSchedules/{audit_schedule}
            organizations/{organization}/locations/{location}/auditSchedules/{audit_schedule}
        display_name (str):
            Optional. Display name for the audit
            schedule.
        gcs_uri (str):
            Required. Cloud Storage bucket where Audit Manager can
            upload the audit report and evidence. The format is
            ``gs://{bucket_name}``.
        compliance_framework (str):
            Required. Framework (set of controls) that the audit scope
            report is generated against. For example, ``NIST_800_53``.
        report_format (google.cloud.auditmanager_v1.types.AuditSchedule.AuditReportFormat):
            Required. Format for the audit report.
        schedule_config (google.cloud.auditmanager_v1.types.ScheduleConfig):
            Required. Configuration that defines when and
            how often audit runs are automatically triggered
            for this schedule.
        state (google.cloud.auditmanager_v1.types.ScheduleState):
            Optional. State of the audit schedule. While most states are
            managed by the system, you can use
            [UpdateAuditSchedule][google.cloud.auditmanager.v1.AuditManager.UpdateAuditSchedule]
            to start, pause, or delete the schedule.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the schedule was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the schedule was
            last updated.
        next_run_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Calculated timestamp for the
            next scheduled run.
        last_trigger_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the audit run was
            last triggered.
        error_message (str):
            Output only. Describes the error if the
            schedule is in an error state.
    """

    class AuditReportFormat(proto.Enum):
        r"""Format for the audit report.

        Values:
            AUDIT_REPORT_FORMAT_UNSPECIFIED (0):
                Default value. This value is unused.
            AUDIT_REPORT_FORMAT_ODF (1):
                Open Document Format (ODF).
        """

        AUDIT_REPORT_FORMAT_UNSPECIFIED = 0
        AUDIT_REPORT_FORMAT_ODF = 1

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    gcs_uri: str = proto.Field(
        proto.STRING,
        number=3,
    )
    compliance_framework: str = proto.Field(
        proto.STRING,
        number=4,
    )
    report_format: AuditReportFormat = proto.Field(
        proto.ENUM,
        number=5,
        enum=AuditReportFormat,
    )
    schedule_config: "ScheduleConfig" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="ScheduleConfig",
    )
    state: "ScheduleState" = proto.Field(
        proto.ENUM,
        number=7,
        enum="ScheduleState",
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
    next_run_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    last_trigger_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )
    error_message: str = proto.Field(
        proto.STRING,
        number=13,
    )


class ScheduleConfig(proto.Message):
    r"""Timing and frequency parameters for recurring audit runs.

    Attributes:
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Required. Date and time when the first audit
            run is triggered. Subsequent runs are based on
            this time and the chosen frequency.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. Date that the schedule stops.
            If not specified, the schedule runs
            indefinitely.
        frequency (google.cloud.auditmanager_v1.types.ScheduleConfig.Frequency):
            Required. Frequency of audit runs.
        time_zone (str):
            Optional. Time zone for the audit schedule in IANA format
            (for example, ``America/New_York``). The time zone is used
            to interpret the ``start_time`` and the ``end_time``, and to
            calculate subsequent run dates. If not specified, the time
            zone default is UTC.
    """

    class Frequency(proto.Enum):
        r"""Frequency of audit runs.

        Values:
            FREQUENCY_UNSPECIFIED (0):
                Default value. This value is unused.
            DAILY (1):
                The audit runs every day.
            WEEKLY (2):
                The audit runs weekly on the same day of the week as
                ``start_time``.
            MONTHLY (3):
                The audit runs monthly on the same day of the month as
                ``start_time``.
            QUARTERLY (4):
                The audit runs quarterly (every 3 months) on the same day of
                the month as ``start_time``.
            ANNUALLY (5):
                The audit runs annually on the same month and day as
                ``start_time``.
        """

        FREQUENCY_UNSPECIFIED = 0
        DAILY = 1
        WEEKLY = 2
        MONTHLY = 3
        QUARTERLY = 4
        ANNUALLY = 5

    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    frequency: Frequency = proto.Field(
        proto.ENUM,
        number=3,
        enum=Frequency,
    )
    time_zone: str = proto.Field(
        proto.STRING,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
