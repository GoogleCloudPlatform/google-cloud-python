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
import dataclasses
import json  # type: ignore
import logging
import warnings
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union

import google.protobuf
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, operations_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.auditmanager_v1._compat import transcode_request
from google.cloud.auditmanager_v1.types import auditmanager

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseAuditManagerRestTransport

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object, None]  # type: ignore

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = logging.getLogger(__name__)

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=f"requests@{requests_version}",
)

DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class AuditManagerRestInterceptor:
    """Interceptor for AuditManager.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the AuditManagerRestTransport.

    .. code-block:: python
        class MyCustomAuditManagerInterceptor(AuditManagerRestInterceptor):
            def pre_create_audit_schedule(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_audit_schedule(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_enroll_resource(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_enroll_resource(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_generate_audit_report(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_generate_audit_report(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_generate_audit_scope_report(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_generate_audit_scope_report(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_audit_report(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_audit_report(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_audit_schedule(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_audit_schedule(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_resource_enrollment_status(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_resource_enrollment_status(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_audit_reports(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_audit_reports(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_audit_schedules(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_audit_schedules(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_controls(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_controls(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_resource_enrollment_statuses(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_resource_enrollment_statuses(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_audit_schedule(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_audit_schedule(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = AuditManagerRestTransport(interceptor=MyCustomAuditManagerInterceptor())
        client = AuditManagerClient(transport=transport)


    """

    def pre_create_audit_schedule(
        self,
        request: auditmanager.CreateAuditScheduleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auditmanager.CreateAuditScheduleRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_audit_schedule

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AuditManager server.
        """
        return request, metadata

    def post_create_audit_schedule(
        self, response: auditmanager.AuditSchedule
    ) -> auditmanager.AuditSchedule:
        """Post-rpc interceptor for create_audit_schedule

        DEPRECATED. Please use the `post_create_audit_schedule_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AuditManager server but before
        it is returned to user code. This `post_create_audit_schedule` interceptor runs
        before the `post_create_audit_schedule_with_metadata` interceptor.
        """
        return response

    def post_create_audit_schedule_with_metadata(
        self,
        response: auditmanager.AuditSchedule,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[auditmanager.AuditSchedule, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_audit_schedule

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AuditManager server but before it is returned to user code.

        We recommend only using this `post_create_audit_schedule_with_metadata`
        interceptor in new development instead of the `post_create_audit_schedule` interceptor.
        When both interceptors are used, this `post_create_audit_schedule_with_metadata` interceptor runs after the
        `post_create_audit_schedule` interceptor. The (possibly modified) response returned by
        `post_create_audit_schedule` will be passed to
        `post_create_audit_schedule_with_metadata`.
        """
        return response, metadata

    def pre_enroll_resource(
        self,
        request: auditmanager.EnrollResourceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auditmanager.EnrollResourceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for enroll_resource

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AuditManager server.
        """
        return request, metadata

    def post_enroll_resource(
        self, response: auditmanager.Enrollment
    ) -> auditmanager.Enrollment:
        """Post-rpc interceptor for enroll_resource

        DEPRECATED. Please use the `post_enroll_resource_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AuditManager server but before
        it is returned to user code. This `post_enroll_resource` interceptor runs
        before the `post_enroll_resource_with_metadata` interceptor.
        """
        return response

    def post_enroll_resource_with_metadata(
        self,
        response: auditmanager.Enrollment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[auditmanager.Enrollment, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for enroll_resource

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AuditManager server but before it is returned to user code.

        We recommend only using this `post_enroll_resource_with_metadata`
        interceptor in new development instead of the `post_enroll_resource` interceptor.
        When both interceptors are used, this `post_enroll_resource_with_metadata` interceptor runs after the
        `post_enroll_resource` interceptor. The (possibly modified) response returned by
        `post_enroll_resource` will be passed to
        `post_enroll_resource_with_metadata`.
        """
        return response, metadata

    def pre_generate_audit_report(
        self,
        request: auditmanager.GenerateAuditReportRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auditmanager.GenerateAuditReportRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for generate_audit_report

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AuditManager server.
        """
        return request, metadata

    def post_generate_audit_report(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for generate_audit_report

        DEPRECATED. Please use the `post_generate_audit_report_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AuditManager server but before
        it is returned to user code. This `post_generate_audit_report` interceptor runs
        before the `post_generate_audit_report_with_metadata` interceptor.
        """
        return response

    def post_generate_audit_report_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for generate_audit_report

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AuditManager server but before it is returned to user code.

        We recommend only using this `post_generate_audit_report_with_metadata`
        interceptor in new development instead of the `post_generate_audit_report` interceptor.
        When both interceptors are used, this `post_generate_audit_report_with_metadata` interceptor runs after the
        `post_generate_audit_report` interceptor. The (possibly modified) response returned by
        `post_generate_audit_report` will be passed to
        `post_generate_audit_report_with_metadata`.
        """
        return response, metadata

    def pre_generate_audit_scope_report(
        self,
        request: auditmanager.GenerateAuditScopeReportRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auditmanager.GenerateAuditScopeReportRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for generate_audit_scope_report

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AuditManager server.
        """
        return request, metadata

    def post_generate_audit_scope_report(
        self, response: auditmanager.AuditScopeReport
    ) -> auditmanager.AuditScopeReport:
        """Post-rpc interceptor for generate_audit_scope_report

        DEPRECATED. Please use the `post_generate_audit_scope_report_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AuditManager server but before
        it is returned to user code. This `post_generate_audit_scope_report` interceptor runs
        before the `post_generate_audit_scope_report_with_metadata` interceptor.
        """
        return response

    def post_generate_audit_scope_report_with_metadata(
        self,
        response: auditmanager.AuditScopeReport,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[auditmanager.AuditScopeReport, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for generate_audit_scope_report

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AuditManager server but before it is returned to user code.

        We recommend only using this `post_generate_audit_scope_report_with_metadata`
        interceptor in new development instead of the `post_generate_audit_scope_report` interceptor.
        When both interceptors are used, this `post_generate_audit_scope_report_with_metadata` interceptor runs after the
        `post_generate_audit_scope_report` interceptor. The (possibly modified) response returned by
        `post_generate_audit_scope_report` will be passed to
        `post_generate_audit_scope_report_with_metadata`.
        """
        return response, metadata

    def pre_get_audit_report(
        self,
        request: auditmanager.GetAuditReportRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auditmanager.GetAuditReportRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_audit_report

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AuditManager server.
        """
        return request, metadata

    def post_get_audit_report(
        self, response: auditmanager.AuditReport
    ) -> auditmanager.AuditReport:
        """Post-rpc interceptor for get_audit_report

        DEPRECATED. Please use the `post_get_audit_report_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AuditManager server but before
        it is returned to user code. This `post_get_audit_report` interceptor runs
        before the `post_get_audit_report_with_metadata` interceptor.
        """
        return response

    def post_get_audit_report_with_metadata(
        self,
        response: auditmanager.AuditReport,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[auditmanager.AuditReport, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_audit_report

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AuditManager server but before it is returned to user code.

        We recommend only using this `post_get_audit_report_with_metadata`
        interceptor in new development instead of the `post_get_audit_report` interceptor.
        When both interceptors are used, this `post_get_audit_report_with_metadata` interceptor runs after the
        `post_get_audit_report` interceptor. The (possibly modified) response returned by
        `post_get_audit_report` will be passed to
        `post_get_audit_report_with_metadata`.
        """
        return response, metadata

    def pre_get_audit_schedule(
        self,
        request: auditmanager.GetAuditScheduleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auditmanager.GetAuditScheduleRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_audit_schedule

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AuditManager server.
        """
        return request, metadata

    def post_get_audit_schedule(
        self, response: auditmanager.AuditSchedule
    ) -> auditmanager.AuditSchedule:
        """Post-rpc interceptor for get_audit_schedule

        DEPRECATED. Please use the `post_get_audit_schedule_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AuditManager server but before
        it is returned to user code. This `post_get_audit_schedule` interceptor runs
        before the `post_get_audit_schedule_with_metadata` interceptor.
        """
        return response

    def post_get_audit_schedule_with_metadata(
        self,
        response: auditmanager.AuditSchedule,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[auditmanager.AuditSchedule, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_audit_schedule

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AuditManager server but before it is returned to user code.

        We recommend only using this `post_get_audit_schedule_with_metadata`
        interceptor in new development instead of the `post_get_audit_schedule` interceptor.
        When both interceptors are used, this `post_get_audit_schedule_with_metadata` interceptor runs after the
        `post_get_audit_schedule` interceptor. The (possibly modified) response returned by
        `post_get_audit_schedule` will be passed to
        `post_get_audit_schedule_with_metadata`.
        """
        return response, metadata

    def pre_get_resource_enrollment_status(
        self,
        request: auditmanager.GetResourceEnrollmentStatusRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auditmanager.GetResourceEnrollmentStatusRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_resource_enrollment_status

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AuditManager server.
        """
        return request, metadata

    def post_get_resource_enrollment_status(
        self, response: auditmanager.ResourceEnrollmentStatus
    ) -> auditmanager.ResourceEnrollmentStatus:
        """Post-rpc interceptor for get_resource_enrollment_status

        DEPRECATED. Please use the `post_get_resource_enrollment_status_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AuditManager server but before
        it is returned to user code. This `post_get_resource_enrollment_status` interceptor runs
        before the `post_get_resource_enrollment_status_with_metadata` interceptor.
        """
        return response

    def post_get_resource_enrollment_status_with_metadata(
        self,
        response: auditmanager.ResourceEnrollmentStatus,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auditmanager.ResourceEnrollmentStatus, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_resource_enrollment_status

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AuditManager server but before it is returned to user code.

        We recommend only using this `post_get_resource_enrollment_status_with_metadata`
        interceptor in new development instead of the `post_get_resource_enrollment_status` interceptor.
        When both interceptors are used, this `post_get_resource_enrollment_status_with_metadata` interceptor runs after the
        `post_get_resource_enrollment_status` interceptor. The (possibly modified) response returned by
        `post_get_resource_enrollment_status` will be passed to
        `post_get_resource_enrollment_status_with_metadata`.
        """
        return response, metadata

    def pre_list_audit_reports(
        self,
        request: auditmanager.ListAuditReportsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auditmanager.ListAuditReportsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_audit_reports

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AuditManager server.
        """
        return request, metadata

    def post_list_audit_reports(
        self, response: auditmanager.ListAuditReportsResponse
    ) -> auditmanager.ListAuditReportsResponse:
        """Post-rpc interceptor for list_audit_reports

        DEPRECATED. Please use the `post_list_audit_reports_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AuditManager server but before
        it is returned to user code. This `post_list_audit_reports` interceptor runs
        before the `post_list_audit_reports_with_metadata` interceptor.
        """
        return response

    def post_list_audit_reports_with_metadata(
        self,
        response: auditmanager.ListAuditReportsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auditmanager.ListAuditReportsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_audit_reports

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AuditManager server but before it is returned to user code.

        We recommend only using this `post_list_audit_reports_with_metadata`
        interceptor in new development instead of the `post_list_audit_reports` interceptor.
        When both interceptors are used, this `post_list_audit_reports_with_metadata` interceptor runs after the
        `post_list_audit_reports` interceptor. The (possibly modified) response returned by
        `post_list_audit_reports` will be passed to
        `post_list_audit_reports_with_metadata`.
        """
        return response, metadata

    def pre_list_audit_schedules(
        self,
        request: auditmanager.ListAuditSchedulesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auditmanager.ListAuditSchedulesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_audit_schedules

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AuditManager server.
        """
        return request, metadata

    def post_list_audit_schedules(
        self, response: auditmanager.ListAuditSchedulesResponse
    ) -> auditmanager.ListAuditSchedulesResponse:
        """Post-rpc interceptor for list_audit_schedules

        DEPRECATED. Please use the `post_list_audit_schedules_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AuditManager server but before
        it is returned to user code. This `post_list_audit_schedules` interceptor runs
        before the `post_list_audit_schedules_with_metadata` interceptor.
        """
        return response

    def post_list_audit_schedules_with_metadata(
        self,
        response: auditmanager.ListAuditSchedulesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auditmanager.ListAuditSchedulesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_audit_schedules

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AuditManager server but before it is returned to user code.

        We recommend only using this `post_list_audit_schedules_with_metadata`
        interceptor in new development instead of the `post_list_audit_schedules` interceptor.
        When both interceptors are used, this `post_list_audit_schedules_with_metadata` interceptor runs after the
        `post_list_audit_schedules` interceptor. The (possibly modified) response returned by
        `post_list_audit_schedules` will be passed to
        `post_list_audit_schedules_with_metadata`.
        """
        return response, metadata

    def pre_list_controls(
        self,
        request: auditmanager.ListControlsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auditmanager.ListControlsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_controls

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AuditManager server.
        """
        return request, metadata

    def post_list_controls(
        self, response: auditmanager.ListControlsResponse
    ) -> auditmanager.ListControlsResponse:
        """Post-rpc interceptor for list_controls

        DEPRECATED. Please use the `post_list_controls_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AuditManager server but before
        it is returned to user code. This `post_list_controls` interceptor runs
        before the `post_list_controls_with_metadata` interceptor.
        """
        return response

    def post_list_controls_with_metadata(
        self,
        response: auditmanager.ListControlsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auditmanager.ListControlsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_controls

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AuditManager server but before it is returned to user code.

        We recommend only using this `post_list_controls_with_metadata`
        interceptor in new development instead of the `post_list_controls` interceptor.
        When both interceptors are used, this `post_list_controls_with_metadata` interceptor runs after the
        `post_list_controls` interceptor. The (possibly modified) response returned by
        `post_list_controls` will be passed to
        `post_list_controls_with_metadata`.
        """
        return response, metadata

    def pre_list_resource_enrollment_statuses(
        self,
        request: auditmanager.ListResourceEnrollmentStatusesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auditmanager.ListResourceEnrollmentStatusesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_resource_enrollment_statuses

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AuditManager server.
        """
        return request, metadata

    def post_list_resource_enrollment_statuses(
        self, response: auditmanager.ListResourceEnrollmentStatusesResponse
    ) -> auditmanager.ListResourceEnrollmentStatusesResponse:
        """Post-rpc interceptor for list_resource_enrollment_statuses

        DEPRECATED. Please use the `post_list_resource_enrollment_statuses_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AuditManager server but before
        it is returned to user code. This `post_list_resource_enrollment_statuses` interceptor runs
        before the `post_list_resource_enrollment_statuses_with_metadata` interceptor.
        """
        return response

    def post_list_resource_enrollment_statuses_with_metadata(
        self,
        response: auditmanager.ListResourceEnrollmentStatusesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auditmanager.ListResourceEnrollmentStatusesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_resource_enrollment_statuses

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AuditManager server but before it is returned to user code.

        We recommend only using this `post_list_resource_enrollment_statuses_with_metadata`
        interceptor in new development instead of the `post_list_resource_enrollment_statuses` interceptor.
        When both interceptors are used, this `post_list_resource_enrollment_statuses_with_metadata` interceptor runs after the
        `post_list_resource_enrollment_statuses` interceptor. The (possibly modified) response returned by
        `post_list_resource_enrollment_statuses` will be passed to
        `post_list_resource_enrollment_statuses_with_metadata`.
        """
        return response, metadata

    def pre_update_audit_schedule(
        self,
        request: auditmanager.UpdateAuditScheduleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        auditmanager.UpdateAuditScheduleRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_audit_schedule

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AuditManager server.
        """
        return request, metadata

    def post_update_audit_schedule(
        self, response: auditmanager.AuditSchedule
    ) -> auditmanager.AuditSchedule:
        """Post-rpc interceptor for update_audit_schedule

        DEPRECATED. Please use the `post_update_audit_schedule_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AuditManager server but before
        it is returned to user code. This `post_update_audit_schedule` interceptor runs
        before the `post_update_audit_schedule_with_metadata` interceptor.
        """
        return response

    def post_update_audit_schedule_with_metadata(
        self,
        response: auditmanager.AuditSchedule,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[auditmanager.AuditSchedule, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_audit_schedule

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AuditManager server but before it is returned to user code.

        We recommend only using this `post_update_audit_schedule_with_metadata`
        interceptor in new development instead of the `post_update_audit_schedule` interceptor.
        When both interceptors are used, this `post_update_audit_schedule_with_metadata` interceptor runs after the
        `post_update_audit_schedule` interceptor. The (possibly modified) response returned by
        `post_update_audit_schedule` will be passed to
        `post_update_audit_schedule_with_metadata`.
        """
        return response, metadata

    def pre_get_location(
        self,
        request: locations_pb2.GetLocationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        locations_pb2.GetLocationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_location

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AuditManager server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the AuditManager server but before
        it is returned to user code.
        """
        return response

    def pre_list_locations(
        self,
        request: locations_pb2.ListLocationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        locations_pb2.ListLocationsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_locations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AuditManager server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the AuditManager server but before
        it is returned to user code.
        """
        return response

    def pre_cancel_operation(
        self,
        request: operations_pb2.CancelOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.CancelOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AuditManager server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the AuditManager server but before
        it is returned to user code.
        """
        return response

    def pre_delete_operation(
        self,
        request: operations_pb2.DeleteOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.DeleteOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AuditManager server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the AuditManager server but before
        it is returned to user code.
        """
        return response

    def pre_get_operation(
        self,
        request: operations_pb2.GetOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.GetOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AuditManager server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the AuditManager server but before
        it is returned to user code.
        """
        return response

    def pre_list_operations(
        self,
        request: operations_pb2.ListOperationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.ListOperationsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_operations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AuditManager server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the AuditManager server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class AuditManagerRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: AuditManagerRestInterceptor


class AuditManagerRestTransport(_BaseAuditManagerRestTransport):
    """REST backend synchronous transport for AuditManager.

    Service describing handlers for resources

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "auditmanager.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[AuditManagerRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'auditmanager.googleapis.com').
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.

            credentials_file (Optional[str]): Deprecated. A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided. This argument will be
                removed in the next major version of this library.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Callable[[], Tuple[bytes, bytes]]): Client
                certificate to configure mutual TLS HTTP channel. It is ignored
                if ``channel`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you are developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            url_scheme: the protocol scheme for the API endpoint.  Normally
                "https", but for testing or local servers,
                "http" can be specified.
            interceptor (Optional[AuditManagerRestInterceptor]): Interceptor used
                to manipulate requests, request metadata, and responses.
            api_audience (Optional[str]): The intended audience for the API calls
                to the service that will be set when using certain 3rd party
                authentication flows. Audience is typically a resource identifier.
                If not set, the host value will be used as a default.
        """
        # Run the base constructor
        # TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.
        # TODO: When custom host (api_endpoint) is set, `scopes` must *also* be set on the
        # credentials object
        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            url_scheme=url_scheme,
            api_audience=api_audience,
        )
        self._session = AuthorizedSession(
            self._credentials, default_host=self.DEFAULT_HOST
        )
        self._operations_client: Optional[operations_v1.AbstractOperationsClient] = None
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or AuditManagerRestInterceptor()
        self._prep_wrapped_messages(client_info)

    @property
    def operations_client(self) -> operations_v1.AbstractOperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Only create a new client if we do not already have one.
        if self._operations_client is None:
            http_options: Dict[str, List[Dict[str, str]]] = {
                "google.longrunning.Operations.CancelOperation": [
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}:cancel",
                        "body": "*",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=organizations/*/locations/*/operations/*}:cancel",
                        "body": "*",
                    },
                ],
                "google.longrunning.Operations.DeleteOperation": [
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=organizations/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=organizations/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.ListOperations": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=organizations/*/locations/*}/operations",
                    },
                ],
            }

            rest_transport = operations_v1.OperationsRestTransport(
                host=self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                scopes=self._scopes,
                http_options=http_options,
                path_prefix="v1",
            )

            self._operations_client = operations_v1.AbstractOperationsClient(
                transport=rest_transport
            )

        # Return the client from cache.
        return self._operations_client

    class _CreateAuditSchedule(
        _BaseAuditManagerRestTransport._BaseCreateAuditSchedule, AuditManagerRestStub
    ):
        def __hash__(self):
            return hash("AuditManagerRestTransport.CreateAuditSchedule")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: auditmanager.CreateAuditScheduleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> auditmanager.AuditSchedule:
            r"""Call the create audit schedule method over HTTP.

            Args:
                request (~.auditmanager.CreateAuditScheduleRequest):
                    The request object. Request message for
                [CreateAuditSchedule][google.cloud.auditmanager.v1.AuditManager.CreateAuditSchedule].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.auditmanager.AuditSchedule:
                    An audit schedule, in one of the following formats:

                - ``projects/{project}/locations/{location}/auditSchedules/{audit_schedule}``
                - ``folders/{folder}/locations/{location}/auditSchedules/{audit_schedule}``

            """

            http_options = _BaseAuditManagerRestTransport._BaseCreateAuditSchedule._get_http_options()
            request, metadata = self._interceptor.pre_create_audit_schedule(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAuditManagerRestTransport._BaseCreateAuditSchedule,
                    "_BaseCreateAuditSchedule__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.auditmanager_v1.AuditManagerClient.CreateAuditSchedule",
                    extra={
                        "serviceName": "google.cloud.auditmanager.v1.AuditManager",
                        "rpcName": "CreateAuditSchedule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AuditManagerRestTransport._CreateAuditSchedule._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = auditmanager.AuditSchedule()
            pb_resp = auditmanager.AuditSchedule.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_audit_schedule(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_audit_schedule_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = auditmanager.AuditSchedule.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.auditmanager_v1.AuditManagerClient.create_audit_schedule",
                    extra={
                        "serviceName": "google.cloud.auditmanager.v1.AuditManager",
                        "rpcName": "CreateAuditSchedule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _EnrollResource(
        _BaseAuditManagerRestTransport._BaseEnrollResource, AuditManagerRestStub
    ):
        def __hash__(self):
            return hash("AuditManagerRestTransport.EnrollResource")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: auditmanager.EnrollResourceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> auditmanager.Enrollment:
            r"""Call the enroll resource method over HTTP.

            Args:
                request (~.auditmanager.EnrollResourceRequest):
                    The request object. Request message for
                [EnrollResource][google.cloud.auditmanager.v1.AuditManager.EnrollResource].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.auditmanager.Enrollment:
                    Organization, folder, or project to
                enroll for audit reports.

            """

            http_options = (
                _BaseAuditManagerRestTransport._BaseEnrollResource._get_http_options()
            )
            request, metadata = self._interceptor.pre_enroll_resource(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAuditManagerRestTransport._BaseEnrollResource,
                    "_BaseEnrollResource__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.auditmanager_v1.AuditManagerClient.EnrollResource",
                    extra={
                        "serviceName": "google.cloud.auditmanager.v1.AuditManager",
                        "rpcName": "EnrollResource",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AuditManagerRestTransport._EnrollResource._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = auditmanager.Enrollment()
            pb_resp = auditmanager.Enrollment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_enroll_resource(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_enroll_resource_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = auditmanager.Enrollment.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.auditmanager_v1.AuditManagerClient.enroll_resource",
                    extra={
                        "serviceName": "google.cloud.auditmanager.v1.AuditManager",
                        "rpcName": "EnrollResource",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GenerateAuditReport(
        _BaseAuditManagerRestTransport._BaseGenerateAuditReport, AuditManagerRestStub
    ):
        def __hash__(self):
            return hash("AuditManagerRestTransport.GenerateAuditReport")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: auditmanager.GenerateAuditReportRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the generate audit report method over HTTP.

            Args:
                request (~.auditmanager.GenerateAuditReportRequest):
                    The request object. Request message for
                [GenerateAuditReport][google.cloud.auditmanager.v1.AuditManager.GenerateAuditReport].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = _BaseAuditManagerRestTransport._BaseGenerateAuditReport._get_http_options()
            request, metadata = self._interceptor.pre_generate_audit_report(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAuditManagerRestTransport._BaseGenerateAuditReport,
                    "_BaseGenerateAuditReport__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.auditmanager_v1.AuditManagerClient.GenerateAuditReport",
                    extra={
                        "serviceName": "google.cloud.auditmanager.v1.AuditManager",
                        "rpcName": "GenerateAuditReport",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AuditManagerRestTransport._GenerateAuditReport._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_generate_audit_report(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_generate_audit_report_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.auditmanager_v1.AuditManagerClient.generate_audit_report",
                    extra={
                        "serviceName": "google.cloud.auditmanager.v1.AuditManager",
                        "rpcName": "GenerateAuditReport",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GenerateAuditScopeReport(
        _BaseAuditManagerRestTransport._BaseGenerateAuditScopeReport,
        AuditManagerRestStub,
    ):
        def __hash__(self):
            return hash("AuditManagerRestTransport.GenerateAuditScopeReport")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: auditmanager.GenerateAuditScopeReportRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> auditmanager.AuditScopeReport:
            r"""Call the generate audit scope
            report method over HTTP.

                Args:
                    request (~.auditmanager.GenerateAuditScopeReportRequest):
                        The request object. Request message for
                    [GenerateAuditScopeReport][google.cloud.auditmanager.v1.AuditManager.GenerateAuditScopeReport].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.auditmanager.AuditScopeReport:
                        Audit scope report.
            """

            http_options = _BaseAuditManagerRestTransport._BaseGenerateAuditScopeReport._get_http_options()
            request, metadata = self._interceptor.pre_generate_audit_scope_report(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAuditManagerRestTransport._BaseGenerateAuditScopeReport,
                    "_BaseGenerateAuditScopeReport__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.auditmanager_v1.AuditManagerClient.GenerateAuditScopeReport",
                    extra={
                        "serviceName": "google.cloud.auditmanager.v1.AuditManager",
                        "rpcName": "GenerateAuditScopeReport",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AuditManagerRestTransport._GenerateAuditScopeReport._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    body,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = auditmanager.AuditScopeReport()
            pb_resp = auditmanager.AuditScopeReport.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_generate_audit_scope_report(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_generate_audit_scope_report_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = auditmanager.AuditScopeReport.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.auditmanager_v1.AuditManagerClient.generate_audit_scope_report",
                    extra={
                        "serviceName": "google.cloud.auditmanager.v1.AuditManager",
                        "rpcName": "GenerateAuditScopeReport",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAuditReport(
        _BaseAuditManagerRestTransport._BaseGetAuditReport, AuditManagerRestStub
    ):
        def __hash__(self):
            return hash("AuditManagerRestTransport.GetAuditReport")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: auditmanager.GetAuditReportRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> auditmanager.AuditReport:
            r"""Call the get audit report method over HTTP.

            Args:
                request (~.auditmanager.GetAuditReportRequest):
                    The request object. Request message for
                [GetAuditReport][google.cloud.auditmanager.v1.AuditManager.GetAuditReport].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.auditmanager.AuditReport:
                    An audit report.
            """

            http_options = (
                _BaseAuditManagerRestTransport._BaseGetAuditReport._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_audit_report(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAuditManagerRestTransport._BaseGetAuditReport,
                    "_BaseGetAuditReport__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.auditmanager_v1.AuditManagerClient.GetAuditReport",
                    extra={
                        "serviceName": "google.cloud.auditmanager.v1.AuditManager",
                        "rpcName": "GetAuditReport",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AuditManagerRestTransport._GetAuditReport._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = auditmanager.AuditReport()
            pb_resp = auditmanager.AuditReport.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_audit_report(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_audit_report_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = auditmanager.AuditReport.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.auditmanager_v1.AuditManagerClient.get_audit_report",
                    extra={
                        "serviceName": "google.cloud.auditmanager.v1.AuditManager",
                        "rpcName": "GetAuditReport",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAuditSchedule(
        _BaseAuditManagerRestTransport._BaseGetAuditSchedule, AuditManagerRestStub
    ):
        def __hash__(self):
            return hash("AuditManagerRestTransport.GetAuditSchedule")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: auditmanager.GetAuditScheduleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> auditmanager.AuditSchedule:
            r"""Call the get audit schedule method over HTTP.

            Args:
                request (~.auditmanager.GetAuditScheduleRequest):
                    The request object. Request message for
                [GetAuditSchedule][google.cloud.auditmanager.v1.AuditManager.GetAuditSchedule].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.auditmanager.AuditSchedule:
                    An audit schedule, in one of the following formats:

                - ``projects/{project}/locations/{location}/auditSchedules/{audit_schedule}``
                - ``folders/{folder}/locations/{location}/auditSchedules/{audit_schedule}``

            """

            http_options = (
                _BaseAuditManagerRestTransport._BaseGetAuditSchedule._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_audit_schedule(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAuditManagerRestTransport._BaseGetAuditSchedule,
                    "_BaseGetAuditSchedule__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.auditmanager_v1.AuditManagerClient.GetAuditSchedule",
                    extra={
                        "serviceName": "google.cloud.auditmanager.v1.AuditManager",
                        "rpcName": "GetAuditSchedule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AuditManagerRestTransport._GetAuditSchedule._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = auditmanager.AuditSchedule()
            pb_resp = auditmanager.AuditSchedule.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_audit_schedule(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_audit_schedule_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = auditmanager.AuditSchedule.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.auditmanager_v1.AuditManagerClient.get_audit_schedule",
                    extra={
                        "serviceName": "google.cloud.auditmanager.v1.AuditManager",
                        "rpcName": "GetAuditSchedule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetResourceEnrollmentStatus(
        _BaseAuditManagerRestTransport._BaseGetResourceEnrollmentStatus,
        AuditManagerRestStub,
    ):
        def __hash__(self):
            return hash("AuditManagerRestTransport.GetResourceEnrollmentStatus")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: auditmanager.GetResourceEnrollmentStatusRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> auditmanager.ResourceEnrollmentStatus:
            r"""Call the get resource enrollment
            status method over HTTP.

                Args:
                    request (~.auditmanager.GetResourceEnrollmentStatusRequest):
                        The request object. Request message for
                    [GetResourceEnrollmentStatus][google.cloud.auditmanager.v1.AuditManager.GetResourceEnrollmentStatus].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.auditmanager.ResourceEnrollmentStatus:
                        An organization, folder, or project
                    with its enrollment status.

            """

            http_options = _BaseAuditManagerRestTransport._BaseGetResourceEnrollmentStatus._get_http_options()
            request, metadata = self._interceptor.pre_get_resource_enrollment_status(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAuditManagerRestTransport._BaseGetResourceEnrollmentStatus,
                    "_BaseGetResourceEnrollmentStatus__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.auditmanager_v1.AuditManagerClient.GetResourceEnrollmentStatus",
                    extra={
                        "serviceName": "google.cloud.auditmanager.v1.AuditManager",
                        "rpcName": "GetResourceEnrollmentStatus",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AuditManagerRestTransport._GetResourceEnrollmentStatus._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = auditmanager.ResourceEnrollmentStatus()
            pb_resp = auditmanager.ResourceEnrollmentStatus.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_resource_enrollment_status(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_get_resource_enrollment_status_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = auditmanager.ResourceEnrollmentStatus.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.auditmanager_v1.AuditManagerClient.get_resource_enrollment_status",
                    extra={
                        "serviceName": "google.cloud.auditmanager.v1.AuditManager",
                        "rpcName": "GetResourceEnrollmentStatus",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAuditReports(
        _BaseAuditManagerRestTransport._BaseListAuditReports, AuditManagerRestStub
    ):
        def __hash__(self):
            return hash("AuditManagerRestTransport.ListAuditReports")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: auditmanager.ListAuditReportsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> auditmanager.ListAuditReportsResponse:
            r"""Call the list audit reports method over HTTP.

            Args:
                request (~.auditmanager.ListAuditReportsRequest):
                    The request object. Request message for
                [ListAuditReports][google.cloud.auditmanager.v1.AuditManager.ListAuditReports].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.auditmanager.ListAuditReportsResponse:
                    Response message for
                [ListAuditReports][google.cloud.auditmanager.v1.AuditManager.ListAuditReports].

            """

            http_options = (
                _BaseAuditManagerRestTransport._BaseListAuditReports._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_audit_reports(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAuditManagerRestTransport._BaseListAuditReports,
                    "_BaseListAuditReports__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.auditmanager_v1.AuditManagerClient.ListAuditReports",
                    extra={
                        "serviceName": "google.cloud.auditmanager.v1.AuditManager",
                        "rpcName": "ListAuditReports",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AuditManagerRestTransport._ListAuditReports._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = auditmanager.ListAuditReportsResponse()
            pb_resp = auditmanager.ListAuditReportsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_audit_reports(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_audit_reports_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = auditmanager.ListAuditReportsResponse.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.auditmanager_v1.AuditManagerClient.list_audit_reports",
                    extra={
                        "serviceName": "google.cloud.auditmanager.v1.AuditManager",
                        "rpcName": "ListAuditReports",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAuditSchedules(
        _BaseAuditManagerRestTransport._BaseListAuditSchedules, AuditManagerRestStub
    ):
        def __hash__(self):
            return hash("AuditManagerRestTransport.ListAuditSchedules")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: auditmanager.ListAuditSchedulesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> auditmanager.ListAuditSchedulesResponse:
            r"""Call the list audit schedules method over HTTP.

            Args:
                request (~.auditmanager.ListAuditSchedulesRequest):
                    The request object. Request message for
                [ListAuditSchedules][google.cloud.auditmanager.v1.AuditManager.ListAuditSchedules].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.auditmanager.ListAuditSchedulesResponse:
                    Response message for
                [ListAuditSchedules][google.cloud.auditmanager.v1.AuditManager.ListAuditSchedules].

            """

            http_options = _BaseAuditManagerRestTransport._BaseListAuditSchedules._get_http_options()
            request, metadata = self._interceptor.pre_list_audit_schedules(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAuditManagerRestTransport._BaseListAuditSchedules,
                    "_BaseListAuditSchedules__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.auditmanager_v1.AuditManagerClient.ListAuditSchedules",
                    extra={
                        "serviceName": "google.cloud.auditmanager.v1.AuditManager",
                        "rpcName": "ListAuditSchedules",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AuditManagerRestTransport._ListAuditSchedules._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = auditmanager.ListAuditSchedulesResponse()
            pb_resp = auditmanager.ListAuditSchedulesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_audit_schedules(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_audit_schedules_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = auditmanager.ListAuditSchedulesResponse.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.auditmanager_v1.AuditManagerClient.list_audit_schedules",
                    extra={
                        "serviceName": "google.cloud.auditmanager.v1.AuditManager",
                        "rpcName": "ListAuditSchedules",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListControls(
        _BaseAuditManagerRestTransport._BaseListControls, AuditManagerRestStub
    ):
        def __hash__(self):
            return hash("AuditManagerRestTransport.ListControls")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: auditmanager.ListControlsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> auditmanager.ListControlsResponse:
            r"""Call the list controls method over HTTP.

            Args:
                request (~.auditmanager.ListControlsRequest):
                    The request object. Request message for
                [ListControls][google.cloud.auditmanager.v1.AuditManager.ListControls].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.auditmanager.ListControlsResponse:
                    Response message for
                [ListControls][google.cloud.auditmanager.v1.AuditManager.ListControls].

            """

            http_options = (
                _BaseAuditManagerRestTransport._BaseListControls._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_controls(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAuditManagerRestTransport._BaseListControls,
                    "_BaseListControls__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.auditmanager_v1.AuditManagerClient.ListControls",
                    extra={
                        "serviceName": "google.cloud.auditmanager.v1.AuditManager",
                        "rpcName": "ListControls",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AuditManagerRestTransport._ListControls._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = auditmanager.ListControlsResponse()
            pb_resp = auditmanager.ListControlsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_controls(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_controls_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = auditmanager.ListControlsResponse.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.auditmanager_v1.AuditManagerClient.list_controls",
                    extra={
                        "serviceName": "google.cloud.auditmanager.v1.AuditManager",
                        "rpcName": "ListControls",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListResourceEnrollmentStatuses(
        _BaseAuditManagerRestTransport._BaseListResourceEnrollmentStatuses,
        AuditManagerRestStub,
    ):
        def __hash__(self):
            return hash("AuditManagerRestTransport.ListResourceEnrollmentStatuses")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: auditmanager.ListResourceEnrollmentStatusesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> auditmanager.ListResourceEnrollmentStatusesResponse:
            r"""Call the list resource enrollment
            statuses method over HTTP.

                Args:
                    request (~.auditmanager.ListResourceEnrollmentStatusesRequest):
                        The request object. Request message for
                    [ListResourceEnrollmentStatuses][google.cloud.auditmanager.v1.AuditManager.ListResourceEnrollmentStatuses].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.auditmanager.ListResourceEnrollmentStatusesResponse:
                        Response message for
                    [ListResourceEnrollmentStatuses][google.cloud.auditmanager.v1.AuditManager.ListResourceEnrollmentStatuses].

            """

            http_options = _BaseAuditManagerRestTransport._BaseListResourceEnrollmentStatuses._get_http_options()
            request, metadata = self._interceptor.pre_list_resource_enrollment_statuses(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAuditManagerRestTransport._BaseListResourceEnrollmentStatuses,
                    "_BaseListResourceEnrollmentStatuses__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.auditmanager_v1.AuditManagerClient.ListResourceEnrollmentStatuses",
                    extra={
                        "serviceName": "google.cloud.auditmanager.v1.AuditManager",
                        "rpcName": "ListResourceEnrollmentStatuses",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AuditManagerRestTransport._ListResourceEnrollmentStatuses._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = auditmanager.ListResourceEnrollmentStatusesResponse()
            pb_resp = auditmanager.ListResourceEnrollmentStatusesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_resource_enrollment_statuses(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_resource_enrollment_statuses_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        auditmanager.ListResourceEnrollmentStatusesResponse.to_json(
                            response
                        )
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.auditmanager_v1.AuditManagerClient.list_resource_enrollment_statuses",
                    extra={
                        "serviceName": "google.cloud.auditmanager.v1.AuditManager",
                        "rpcName": "ListResourceEnrollmentStatuses",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateAuditSchedule(
        _BaseAuditManagerRestTransport._BaseUpdateAuditSchedule, AuditManagerRestStub
    ):
        def __hash__(self):
            return hash("AuditManagerRestTransport.UpdateAuditSchedule")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: auditmanager.UpdateAuditScheduleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> auditmanager.AuditSchedule:
            r"""Call the update audit schedule method over HTTP.

            Args:
                request (~.auditmanager.UpdateAuditScheduleRequest):
                    The request object. Request message for
                [UpdateAuditSchedule][google.cloud.auditmanager.v1.AuditManager.UpdateAuditSchedule].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.auditmanager.AuditSchedule:
                    An audit schedule, in one of the following formats:

                - ``projects/{project}/locations/{location}/auditSchedules/{audit_schedule}``
                - ``folders/{folder}/locations/{location}/auditSchedules/{audit_schedule}``

            """

            http_options = _BaseAuditManagerRestTransport._BaseUpdateAuditSchedule._get_http_options()
            request, metadata = self._interceptor.pre_update_audit_schedule(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAuditManagerRestTransport._BaseUpdateAuditSchedule,
                    "_BaseUpdateAuditSchedule__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.auditmanager_v1.AuditManagerClient.UpdateAuditSchedule",
                    extra={
                        "serviceName": "google.cloud.auditmanager.v1.AuditManager",
                        "rpcName": "UpdateAuditSchedule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AuditManagerRestTransport._UpdateAuditSchedule._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = auditmanager.AuditSchedule()
            pb_resp = auditmanager.AuditSchedule.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_audit_schedule(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_audit_schedule_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = auditmanager.AuditSchedule.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.auditmanager_v1.AuditManagerClient.update_audit_schedule",
                    extra={
                        "serviceName": "google.cloud.auditmanager.v1.AuditManager",
                        "rpcName": "UpdateAuditSchedule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_audit_schedule(
        self,
    ) -> Callable[
        [auditmanager.CreateAuditScheduleRequest], auditmanager.AuditSchedule
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateAuditSchedule(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def enroll_resource(
        self,
    ) -> Callable[[auditmanager.EnrollResourceRequest], auditmanager.Enrollment]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._EnrollResource(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def generate_audit_report(
        self,
    ) -> Callable[[auditmanager.GenerateAuditReportRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GenerateAuditReport(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def generate_audit_scope_report(
        self,
    ) -> Callable[
        [auditmanager.GenerateAuditScopeReportRequest], auditmanager.AuditScopeReport
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GenerateAuditScopeReport(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_audit_report(
        self,
    ) -> Callable[[auditmanager.GetAuditReportRequest], auditmanager.AuditReport]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAuditReport(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_audit_schedule(
        self,
    ) -> Callable[[auditmanager.GetAuditScheduleRequest], auditmanager.AuditSchedule]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAuditSchedule(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_resource_enrollment_status(
        self,
    ) -> Callable[
        [auditmanager.GetResourceEnrollmentStatusRequest],
        auditmanager.ResourceEnrollmentStatus,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetResourceEnrollmentStatus(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_audit_reports(
        self,
    ) -> Callable[
        [auditmanager.ListAuditReportsRequest], auditmanager.ListAuditReportsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAuditReports(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_audit_schedules(
        self,
    ) -> Callable[
        [auditmanager.ListAuditSchedulesRequest],
        auditmanager.ListAuditSchedulesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAuditSchedules(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_controls(
        self,
    ) -> Callable[
        [auditmanager.ListControlsRequest], auditmanager.ListControlsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListControls(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_resource_enrollment_statuses(
        self,
    ) -> Callable[
        [auditmanager.ListResourceEnrollmentStatusesRequest],
        auditmanager.ListResourceEnrollmentStatusesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListResourceEnrollmentStatuses(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_audit_schedule(
        self,
    ) -> Callable[
        [auditmanager.UpdateAuditScheduleRequest], auditmanager.AuditSchedule
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateAuditSchedule(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseAuditManagerRestTransport._BaseGetLocation, AuditManagerRestStub
    ):
        def __hash__(self):
            return hash("AuditManagerRestTransport.GetLocation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: locations_pb2.GetLocationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> locations_pb2.Location:
            r"""Call the get location method over HTTP.

            Args:
                request (locations_pb2.GetLocationRequest):
                    The request object for GetLocation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                locations_pb2.Location: Response from GetLocation method.
            """

            http_options = (
                _BaseAuditManagerRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAuditManagerRestTransport._BaseGetLocation,
                    "_BaseGetLocation__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.auditmanager_v1.AuditManagerClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.auditmanager.v1.AuditManager",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AuditManagerRestTransport._GetLocation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = locations_pb2.Location()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_location(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.auditmanager_v1.AuditManagerAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.auditmanager.v1.AuditManager",
                        "rpcName": "GetLocation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_locations(self):
        return self._ListLocations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListLocations(
        _BaseAuditManagerRestTransport._BaseListLocations, AuditManagerRestStub
    ):
        def __hash__(self):
            return hash("AuditManagerRestTransport.ListLocations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: locations_pb2.ListLocationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> locations_pb2.ListLocationsResponse:
            r"""Call the list locations method over HTTP.

            Args:
                request (locations_pb2.ListLocationsRequest):
                    The request object for ListLocations method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                locations_pb2.ListLocationsResponse: Response from ListLocations method.
            """

            http_options = (
                _BaseAuditManagerRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAuditManagerRestTransport._BaseListLocations,
                    "_BaseListLocations__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.auditmanager_v1.AuditManagerClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.auditmanager.v1.AuditManager",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AuditManagerRestTransport._ListLocations._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = locations_pb2.ListLocationsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_list_locations(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.auditmanager_v1.AuditManagerAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.auditmanager.v1.AuditManager",
                        "rpcName": "ListLocations",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseAuditManagerRestTransport._BaseCancelOperation, AuditManagerRestStub
    ):
        def __hash__(self):
            return hash("AuditManagerRestTransport.CancelOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: operations_pb2.CancelOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> None:
            r"""Call the cancel operation method over HTTP.

            Args:
                request (operations_pb2.CancelOperationRequest):
                    The request object for CancelOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseAuditManagerRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAuditManagerRestTransport._BaseCancelOperation,
                    "_BaseCancelOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.auditmanager_v1.AuditManagerClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.auditmanager.v1.AuditManager",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AuditManagerRestTransport._CancelOperation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            return self._interceptor.post_cancel_operation(None)

    @property
    def delete_operation(self):
        return self._DeleteOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _DeleteOperation(
        _BaseAuditManagerRestTransport._BaseDeleteOperation, AuditManagerRestStub
    ):
        def __hash__(self):
            return hash("AuditManagerRestTransport.DeleteOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: operations_pb2.DeleteOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> None:
            r"""Call the delete operation method over HTTP.

            Args:
                request (operations_pb2.DeleteOperationRequest):
                    The request object for DeleteOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseAuditManagerRestTransport._BaseDeleteOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAuditManagerRestTransport._BaseDeleteOperation,
                    "_BaseDeleteOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.auditmanager_v1.AuditManagerClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.auditmanager.v1.AuditManager",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AuditManagerRestTransport._DeleteOperation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            return self._interceptor.post_delete_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseAuditManagerRestTransport._BaseGetOperation, AuditManagerRestStub
    ):
        def __hash__(self):
            return hash("AuditManagerRestTransport.GetOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: operations_pb2.GetOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the get operation method over HTTP.

            Args:
                request (operations_pb2.GetOperationRequest):
                    The request object for GetOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                operations_pb2.Operation: Response from GetOperation method.
            """

            http_options = (
                _BaseAuditManagerRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAuditManagerRestTransport._BaseGetOperation,
                    "_BaseGetOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.auditmanager_v1.AuditManagerClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.auditmanager.v1.AuditManager",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AuditManagerRestTransport._GetOperation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = operations_pb2.Operation()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_operation(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.auditmanager_v1.AuditManagerAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.auditmanager.v1.AuditManager",
                        "rpcName": "GetOperation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_operations(self):
        return self._ListOperations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListOperations(
        _BaseAuditManagerRestTransport._BaseListOperations, AuditManagerRestStub
    ):
        def __hash__(self):
            return hash("AuditManagerRestTransport.ListOperations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: operations_pb2.ListOperationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.ListOperationsResponse:
            r"""Call the list operations method over HTTP.

            Args:
                request (operations_pb2.ListOperationsRequest):
                    The request object for ListOperations method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                operations_pb2.ListOperationsResponse: Response from ListOperations method.
            """

            http_options = (
                _BaseAuditManagerRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAuditManagerRestTransport._BaseListOperations,
                    "_BaseListOperations__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.auditmanager_v1.AuditManagerClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.auditmanager.v1.AuditManager",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AuditManagerRestTransport._ListOperations._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = operations_pb2.ListOperationsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_list_operations(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.auditmanager_v1.AuditManagerAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.auditmanager.v1.AuditManager",
                        "rpcName": "ListOperations",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("AuditManagerRestTransport",)
