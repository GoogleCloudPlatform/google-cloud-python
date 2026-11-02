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
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.osconfig_v1alpha._compat import transcode_request
from google.cloud.osconfig_v1alpha.types import (
    instance_os_policies_compliance,
    inventory,
    os_policy_assignment_reports,
    os_policy_assignments,
    vulnerability,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseOsConfigZonalServiceRestTransport

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


class OsConfigZonalServiceRestInterceptor:
    """Interceptor for OsConfigZonalService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the OsConfigZonalServiceRestTransport.

    .. code-block:: python
        class MyCustomOsConfigZonalServiceInterceptor(OsConfigZonalServiceRestInterceptor):
            def pre_create_os_policy_assignment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_os_policy_assignment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_os_policy_assignment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_os_policy_assignment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_instance_os_policies_compliance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_instance_os_policies_compliance(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_inventory(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_inventory(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_os_policy_assignment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_os_policy_assignment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_os_policy_assignment_report(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_os_policy_assignment_report(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_vulnerability_report(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_vulnerability_report(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_instance_os_policies_compliances(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_instance_os_policies_compliances(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_inventories(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_inventories(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_os_policy_assignment_reports(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_os_policy_assignment_reports(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_os_policy_assignment_revisions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_os_policy_assignment_revisions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_os_policy_assignments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_os_policy_assignments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_vulnerability_reports(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_vulnerability_reports(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_os_policy_assignment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_os_policy_assignment(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = OsConfigZonalServiceRestTransport(interceptor=MyCustomOsConfigZonalServiceInterceptor())
        client = OsConfigZonalServiceClient(transport=transport)


    """

    def pre_create_os_policy_assignment(
        self,
        request: os_policy_assignments.CreateOSPolicyAssignmentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        os_policy_assignments.CreateOSPolicyAssignmentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_os_policy_assignment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OsConfigZonalService server.
        """
        return request, metadata

    def post_create_os_policy_assignment(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_os_policy_assignment

        DEPRECATED. Please use the `post_create_os_policy_assignment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OsConfigZonalService server but before
        it is returned to user code. This `post_create_os_policy_assignment` interceptor runs
        before the `post_create_os_policy_assignment_with_metadata` interceptor.
        """
        return response

    def post_create_os_policy_assignment_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_os_policy_assignment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OsConfigZonalService server but before it is returned to user code.

        We recommend only using this `post_create_os_policy_assignment_with_metadata`
        interceptor in new development instead of the `post_create_os_policy_assignment` interceptor.
        When both interceptors are used, this `post_create_os_policy_assignment_with_metadata` interceptor runs after the
        `post_create_os_policy_assignment` interceptor. The (possibly modified) response returned by
        `post_create_os_policy_assignment` will be passed to
        `post_create_os_policy_assignment_with_metadata`.
        """
        return response, metadata

    def pre_delete_os_policy_assignment(
        self,
        request: os_policy_assignments.DeleteOSPolicyAssignmentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        os_policy_assignments.DeleteOSPolicyAssignmentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_os_policy_assignment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OsConfigZonalService server.
        """
        return request, metadata

    def post_delete_os_policy_assignment(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_os_policy_assignment

        DEPRECATED. Please use the `post_delete_os_policy_assignment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OsConfigZonalService server but before
        it is returned to user code. This `post_delete_os_policy_assignment` interceptor runs
        before the `post_delete_os_policy_assignment_with_metadata` interceptor.
        """
        return response

    def post_delete_os_policy_assignment_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_os_policy_assignment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OsConfigZonalService server but before it is returned to user code.

        We recommend only using this `post_delete_os_policy_assignment_with_metadata`
        interceptor in new development instead of the `post_delete_os_policy_assignment` interceptor.
        When both interceptors are used, this `post_delete_os_policy_assignment_with_metadata` interceptor runs after the
        `post_delete_os_policy_assignment` interceptor. The (possibly modified) response returned by
        `post_delete_os_policy_assignment` will be passed to
        `post_delete_os_policy_assignment_with_metadata`.
        """
        return response, metadata

    def pre_get_instance_os_policies_compliance(
        self,
        request: instance_os_policies_compliance.GetInstanceOSPoliciesComplianceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        instance_os_policies_compliance.GetInstanceOSPoliciesComplianceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_instance_os_policies_compliance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OsConfigZonalService server.
        """
        return request, metadata

    def post_get_instance_os_policies_compliance(
        self, response: instance_os_policies_compliance.InstanceOSPoliciesCompliance
    ) -> instance_os_policies_compliance.InstanceOSPoliciesCompliance:
        """Post-rpc interceptor for get_instance_os_policies_compliance

        DEPRECATED. Please use the `post_get_instance_os_policies_compliance_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OsConfigZonalService server but before
        it is returned to user code. This `post_get_instance_os_policies_compliance` interceptor runs
        before the `post_get_instance_os_policies_compliance_with_metadata` interceptor.
        """
        return response

    def post_get_instance_os_policies_compliance_with_metadata(
        self,
        response: instance_os_policies_compliance.InstanceOSPoliciesCompliance,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        instance_os_policies_compliance.InstanceOSPoliciesCompliance,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_instance_os_policies_compliance

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OsConfigZonalService server but before it is returned to user code.

        We recommend only using this `post_get_instance_os_policies_compliance_with_metadata`
        interceptor in new development instead of the `post_get_instance_os_policies_compliance` interceptor.
        When both interceptors are used, this `post_get_instance_os_policies_compliance_with_metadata` interceptor runs after the
        `post_get_instance_os_policies_compliance` interceptor. The (possibly modified) response returned by
        `post_get_instance_os_policies_compliance` will be passed to
        `post_get_instance_os_policies_compliance_with_metadata`.
        """
        return response, metadata

    def pre_get_inventory(
        self,
        request: inventory.GetInventoryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[inventory.GetInventoryRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_inventory

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OsConfigZonalService server.
        """
        return request, metadata

    def post_get_inventory(self, response: inventory.Inventory) -> inventory.Inventory:
        """Post-rpc interceptor for get_inventory

        DEPRECATED. Please use the `post_get_inventory_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OsConfigZonalService server but before
        it is returned to user code. This `post_get_inventory` interceptor runs
        before the `post_get_inventory_with_metadata` interceptor.
        """
        return response

    def post_get_inventory_with_metadata(
        self,
        response: inventory.Inventory,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[inventory.Inventory, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_inventory

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OsConfigZonalService server but before it is returned to user code.

        We recommend only using this `post_get_inventory_with_metadata`
        interceptor in new development instead of the `post_get_inventory` interceptor.
        When both interceptors are used, this `post_get_inventory_with_metadata` interceptor runs after the
        `post_get_inventory` interceptor. The (possibly modified) response returned by
        `post_get_inventory` will be passed to
        `post_get_inventory_with_metadata`.
        """
        return response, metadata

    def pre_get_os_policy_assignment(
        self,
        request: os_policy_assignments.GetOSPolicyAssignmentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        os_policy_assignments.GetOSPolicyAssignmentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_os_policy_assignment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OsConfigZonalService server.
        """
        return request, metadata

    def post_get_os_policy_assignment(
        self, response: os_policy_assignments.OSPolicyAssignment
    ) -> os_policy_assignments.OSPolicyAssignment:
        """Post-rpc interceptor for get_os_policy_assignment

        DEPRECATED. Please use the `post_get_os_policy_assignment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OsConfigZonalService server but before
        it is returned to user code. This `post_get_os_policy_assignment` interceptor runs
        before the `post_get_os_policy_assignment_with_metadata` interceptor.
        """
        return response

    def post_get_os_policy_assignment_with_metadata(
        self,
        response: os_policy_assignments.OSPolicyAssignment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        os_policy_assignments.OSPolicyAssignment,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_os_policy_assignment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OsConfigZonalService server but before it is returned to user code.

        We recommend only using this `post_get_os_policy_assignment_with_metadata`
        interceptor in new development instead of the `post_get_os_policy_assignment` interceptor.
        When both interceptors are used, this `post_get_os_policy_assignment_with_metadata` interceptor runs after the
        `post_get_os_policy_assignment` interceptor. The (possibly modified) response returned by
        `post_get_os_policy_assignment` will be passed to
        `post_get_os_policy_assignment_with_metadata`.
        """
        return response, metadata

    def pre_get_os_policy_assignment_report(
        self,
        request: os_policy_assignment_reports.GetOSPolicyAssignmentReportRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        os_policy_assignment_reports.GetOSPolicyAssignmentReportRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_os_policy_assignment_report

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OsConfigZonalService server.
        """
        return request, metadata

    def post_get_os_policy_assignment_report(
        self, response: os_policy_assignment_reports.OSPolicyAssignmentReport
    ) -> os_policy_assignment_reports.OSPolicyAssignmentReport:
        """Post-rpc interceptor for get_os_policy_assignment_report

        DEPRECATED. Please use the `post_get_os_policy_assignment_report_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OsConfigZonalService server but before
        it is returned to user code. This `post_get_os_policy_assignment_report` interceptor runs
        before the `post_get_os_policy_assignment_report_with_metadata` interceptor.
        """
        return response

    def post_get_os_policy_assignment_report_with_metadata(
        self,
        response: os_policy_assignment_reports.OSPolicyAssignmentReport,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        os_policy_assignment_reports.OSPolicyAssignmentReport,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_os_policy_assignment_report

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OsConfigZonalService server but before it is returned to user code.

        We recommend only using this `post_get_os_policy_assignment_report_with_metadata`
        interceptor in new development instead of the `post_get_os_policy_assignment_report` interceptor.
        When both interceptors are used, this `post_get_os_policy_assignment_report_with_metadata` interceptor runs after the
        `post_get_os_policy_assignment_report` interceptor. The (possibly modified) response returned by
        `post_get_os_policy_assignment_report` will be passed to
        `post_get_os_policy_assignment_report_with_metadata`.
        """
        return response, metadata

    def pre_get_vulnerability_report(
        self,
        request: vulnerability.GetVulnerabilityReportRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vulnerability.GetVulnerabilityReportRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_vulnerability_report

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OsConfigZonalService server.
        """
        return request, metadata

    def post_get_vulnerability_report(
        self, response: vulnerability.VulnerabilityReport
    ) -> vulnerability.VulnerabilityReport:
        """Post-rpc interceptor for get_vulnerability_report

        DEPRECATED. Please use the `post_get_vulnerability_report_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OsConfigZonalService server but before
        it is returned to user code. This `post_get_vulnerability_report` interceptor runs
        before the `post_get_vulnerability_report_with_metadata` interceptor.
        """
        return response

    def post_get_vulnerability_report_with_metadata(
        self,
        response: vulnerability.VulnerabilityReport,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vulnerability.VulnerabilityReport, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_vulnerability_report

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OsConfigZonalService server but before it is returned to user code.

        We recommend only using this `post_get_vulnerability_report_with_metadata`
        interceptor in new development instead of the `post_get_vulnerability_report` interceptor.
        When both interceptors are used, this `post_get_vulnerability_report_with_metadata` interceptor runs after the
        `post_get_vulnerability_report` interceptor. The (possibly modified) response returned by
        `post_get_vulnerability_report` will be passed to
        `post_get_vulnerability_report_with_metadata`.
        """
        return response, metadata

    def pre_list_instance_os_policies_compliances(
        self,
        request: instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_instance_os_policies_compliances

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OsConfigZonalService server.
        """
        return request, metadata

    def post_list_instance_os_policies_compliances(
        self,
        response: instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse,
    ) -> instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse:
        """Post-rpc interceptor for list_instance_os_policies_compliances

        DEPRECATED. Please use the `post_list_instance_os_policies_compliances_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OsConfigZonalService server but before
        it is returned to user code. This `post_list_instance_os_policies_compliances` interceptor runs
        before the `post_list_instance_os_policies_compliances_with_metadata` interceptor.
        """
        return response

    def post_list_instance_os_policies_compliances_with_metadata(
        self,
        response: instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_instance_os_policies_compliances

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OsConfigZonalService server but before it is returned to user code.

        We recommend only using this `post_list_instance_os_policies_compliances_with_metadata`
        interceptor in new development instead of the `post_list_instance_os_policies_compliances` interceptor.
        When both interceptors are used, this `post_list_instance_os_policies_compliances_with_metadata` interceptor runs after the
        `post_list_instance_os_policies_compliances` interceptor. The (possibly modified) response returned by
        `post_list_instance_os_policies_compliances` will be passed to
        `post_list_instance_os_policies_compliances_with_metadata`.
        """
        return response, metadata

    def pre_list_inventories(
        self,
        request: inventory.ListInventoriesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        inventory.ListInventoriesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_inventories

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OsConfigZonalService server.
        """
        return request, metadata

    def post_list_inventories(
        self, response: inventory.ListInventoriesResponse
    ) -> inventory.ListInventoriesResponse:
        """Post-rpc interceptor for list_inventories

        DEPRECATED. Please use the `post_list_inventories_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OsConfigZonalService server but before
        it is returned to user code. This `post_list_inventories` interceptor runs
        before the `post_list_inventories_with_metadata` interceptor.
        """
        return response

    def post_list_inventories_with_metadata(
        self,
        response: inventory.ListInventoriesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        inventory.ListInventoriesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_inventories

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OsConfigZonalService server but before it is returned to user code.

        We recommend only using this `post_list_inventories_with_metadata`
        interceptor in new development instead of the `post_list_inventories` interceptor.
        When both interceptors are used, this `post_list_inventories_with_metadata` interceptor runs after the
        `post_list_inventories` interceptor. The (possibly modified) response returned by
        `post_list_inventories` will be passed to
        `post_list_inventories_with_metadata`.
        """
        return response, metadata

    def pre_list_os_policy_assignment_reports(
        self,
        request: os_policy_assignment_reports.ListOSPolicyAssignmentReportsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        os_policy_assignment_reports.ListOSPolicyAssignmentReportsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_os_policy_assignment_reports

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OsConfigZonalService server.
        """
        return request, metadata

    def post_list_os_policy_assignment_reports(
        self,
        response: os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse,
    ) -> os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse:
        """Post-rpc interceptor for list_os_policy_assignment_reports

        DEPRECATED. Please use the `post_list_os_policy_assignment_reports_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OsConfigZonalService server but before
        it is returned to user code. This `post_list_os_policy_assignment_reports` interceptor runs
        before the `post_list_os_policy_assignment_reports_with_metadata` interceptor.
        """
        return response

    def post_list_os_policy_assignment_reports_with_metadata(
        self,
        response: os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_os_policy_assignment_reports

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OsConfigZonalService server but before it is returned to user code.

        We recommend only using this `post_list_os_policy_assignment_reports_with_metadata`
        interceptor in new development instead of the `post_list_os_policy_assignment_reports` interceptor.
        When both interceptors are used, this `post_list_os_policy_assignment_reports_with_metadata` interceptor runs after the
        `post_list_os_policy_assignment_reports` interceptor. The (possibly modified) response returned by
        `post_list_os_policy_assignment_reports` will be passed to
        `post_list_os_policy_assignment_reports_with_metadata`.
        """
        return response, metadata

    def pre_list_os_policy_assignment_revisions(
        self,
        request: os_policy_assignments.ListOSPolicyAssignmentRevisionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        os_policy_assignments.ListOSPolicyAssignmentRevisionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_os_policy_assignment_revisions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OsConfigZonalService server.
        """
        return request, metadata

    def post_list_os_policy_assignment_revisions(
        self, response: os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse
    ) -> os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse:
        """Post-rpc interceptor for list_os_policy_assignment_revisions

        DEPRECATED. Please use the `post_list_os_policy_assignment_revisions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OsConfigZonalService server but before
        it is returned to user code. This `post_list_os_policy_assignment_revisions` interceptor runs
        before the `post_list_os_policy_assignment_revisions_with_metadata` interceptor.
        """
        return response

    def post_list_os_policy_assignment_revisions_with_metadata(
        self,
        response: os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_os_policy_assignment_revisions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OsConfigZonalService server but before it is returned to user code.

        We recommend only using this `post_list_os_policy_assignment_revisions_with_metadata`
        interceptor in new development instead of the `post_list_os_policy_assignment_revisions` interceptor.
        When both interceptors are used, this `post_list_os_policy_assignment_revisions_with_metadata` interceptor runs after the
        `post_list_os_policy_assignment_revisions` interceptor. The (possibly modified) response returned by
        `post_list_os_policy_assignment_revisions` will be passed to
        `post_list_os_policy_assignment_revisions_with_metadata`.
        """
        return response, metadata

    def pre_list_os_policy_assignments(
        self,
        request: os_policy_assignments.ListOSPolicyAssignmentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        os_policy_assignments.ListOSPolicyAssignmentsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_os_policy_assignments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OsConfigZonalService server.
        """
        return request, metadata

    def post_list_os_policy_assignments(
        self, response: os_policy_assignments.ListOSPolicyAssignmentsResponse
    ) -> os_policy_assignments.ListOSPolicyAssignmentsResponse:
        """Post-rpc interceptor for list_os_policy_assignments

        DEPRECATED. Please use the `post_list_os_policy_assignments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OsConfigZonalService server but before
        it is returned to user code. This `post_list_os_policy_assignments` interceptor runs
        before the `post_list_os_policy_assignments_with_metadata` interceptor.
        """
        return response

    def post_list_os_policy_assignments_with_metadata(
        self,
        response: os_policy_assignments.ListOSPolicyAssignmentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        os_policy_assignments.ListOSPolicyAssignmentsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_os_policy_assignments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OsConfigZonalService server but before it is returned to user code.

        We recommend only using this `post_list_os_policy_assignments_with_metadata`
        interceptor in new development instead of the `post_list_os_policy_assignments` interceptor.
        When both interceptors are used, this `post_list_os_policy_assignments_with_metadata` interceptor runs after the
        `post_list_os_policy_assignments` interceptor. The (possibly modified) response returned by
        `post_list_os_policy_assignments` will be passed to
        `post_list_os_policy_assignments_with_metadata`.
        """
        return response, metadata

    def pre_list_vulnerability_reports(
        self,
        request: vulnerability.ListVulnerabilityReportsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vulnerability.ListVulnerabilityReportsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_vulnerability_reports

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OsConfigZonalService server.
        """
        return request, metadata

    def post_list_vulnerability_reports(
        self, response: vulnerability.ListVulnerabilityReportsResponse
    ) -> vulnerability.ListVulnerabilityReportsResponse:
        """Post-rpc interceptor for list_vulnerability_reports

        DEPRECATED. Please use the `post_list_vulnerability_reports_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OsConfigZonalService server but before
        it is returned to user code. This `post_list_vulnerability_reports` interceptor runs
        before the `post_list_vulnerability_reports_with_metadata` interceptor.
        """
        return response

    def post_list_vulnerability_reports_with_metadata(
        self,
        response: vulnerability.ListVulnerabilityReportsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vulnerability.ListVulnerabilityReportsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_vulnerability_reports

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OsConfigZonalService server but before it is returned to user code.

        We recommend only using this `post_list_vulnerability_reports_with_metadata`
        interceptor in new development instead of the `post_list_vulnerability_reports` interceptor.
        When both interceptors are used, this `post_list_vulnerability_reports_with_metadata` interceptor runs after the
        `post_list_vulnerability_reports` interceptor. The (possibly modified) response returned by
        `post_list_vulnerability_reports` will be passed to
        `post_list_vulnerability_reports_with_metadata`.
        """
        return response, metadata

    def pre_update_os_policy_assignment(
        self,
        request: os_policy_assignments.UpdateOSPolicyAssignmentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        os_policy_assignments.UpdateOSPolicyAssignmentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_os_policy_assignment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the OsConfigZonalService server.
        """
        return request, metadata

    def post_update_os_policy_assignment(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_os_policy_assignment

        DEPRECATED. Please use the `post_update_os_policy_assignment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the OsConfigZonalService server but before
        it is returned to user code. This `post_update_os_policy_assignment` interceptor runs
        before the `post_update_os_policy_assignment_with_metadata` interceptor.
        """
        return response

    def post_update_os_policy_assignment_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_os_policy_assignment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the OsConfigZonalService server but before it is returned to user code.

        We recommend only using this `post_update_os_policy_assignment_with_metadata`
        interceptor in new development instead of the `post_update_os_policy_assignment` interceptor.
        When both interceptors are used, this `post_update_os_policy_assignment_with_metadata` interceptor runs after the
        `post_update_os_policy_assignment` interceptor. The (possibly modified) response returned by
        `post_update_os_policy_assignment` will be passed to
        `post_update_os_policy_assignment_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class OsConfigZonalServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: OsConfigZonalServiceRestInterceptor


class OsConfigZonalServiceRestTransport(_BaseOsConfigZonalServiceRestTransport):
    """REST backend synchronous transport for OsConfigZonalService.

    Zonal OS Config API

    The OS Config service is the server-side component that allows
    users to manage package installations and patch jobs for Compute
    Engine VM instances.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "osconfig.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[OsConfigZonalServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'osconfig.googleapis.com').
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
            interceptor (Optional[OsConfigZonalServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or OsConfigZonalServiceRestInterceptor()
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
                        "uri": "/v1alpha/{name=projects/*/locations/*/osPolicyAssignments/*/operations/*}:cancel",
                        "body": "*",
                    },
                ],
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v1alpha/{name=projects/*/locations/*/osPolicyAssignments/*/operations/*}",
                    },
                ],
            }

            rest_transport = operations_v1.OperationsRestTransport(
                host=self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                scopes=self._scopes,
                http_options=http_options,
                path_prefix="v1alpha",
            )

            self._operations_client = operations_v1.AbstractOperationsClient(
                transport=rest_transport
            )

        # Return the client from cache.
        return self._operations_client

    class _CreateOSPolicyAssignment(
        _BaseOsConfigZonalServiceRestTransport._BaseCreateOSPolicyAssignment,
        OsConfigZonalServiceRestStub,
    ):
        def __hash__(self):
            return hash("OsConfigZonalServiceRestTransport.CreateOSPolicyAssignment")

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
            request: os_policy_assignments.CreateOSPolicyAssignmentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create os policy
            assignment method over HTTP.

                Args:
                    request (~.os_policy_assignments.CreateOSPolicyAssignmentRequest):
                        The request object. A request message to create an OS
                    policy assignment
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

            http_options = _BaseOsConfigZonalServiceRestTransport._BaseCreateOSPolicyAssignment._get_http_options()
            request, metadata = self._interceptor.pre_create_os_policy_assignment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOsConfigZonalServiceRestTransport._BaseCreateOSPolicyAssignment,
                    "_BaseCreateOSPolicyAssignment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.osconfig_v1alpha.OsConfigZonalServiceClient.CreateOSPolicyAssignment",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1alpha.OsConfigZonalService",
                        "rpcName": "CreateOSPolicyAssignment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OsConfigZonalServiceRestTransport._CreateOSPolicyAssignment._get_response(
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

            resp = self._interceptor.post_create_os_policy_assignment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_os_policy_assignment_with_metadata(
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
                    "Received response for google.cloud.osconfig_v1alpha.OsConfigZonalServiceClient.create_os_policy_assignment",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1alpha.OsConfigZonalService",
                        "rpcName": "CreateOSPolicyAssignment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteOSPolicyAssignment(
        _BaseOsConfigZonalServiceRestTransport._BaseDeleteOSPolicyAssignment,
        OsConfigZonalServiceRestStub,
    ):
        def __hash__(self):
            return hash("OsConfigZonalServiceRestTransport.DeleteOSPolicyAssignment")

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
            request: os_policy_assignments.DeleteOSPolicyAssignmentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete os policy
            assignment method over HTTP.

                Args:
                    request (~.os_policy_assignments.DeleteOSPolicyAssignmentRequest):
                        The request object. A request message for deleting a OS
                    policy assignment.
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

            http_options = _BaseOsConfigZonalServiceRestTransport._BaseDeleteOSPolicyAssignment._get_http_options()
            request, metadata = self._interceptor.pre_delete_os_policy_assignment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOsConfigZonalServiceRestTransport._BaseDeleteOSPolicyAssignment,
                    "_BaseDeleteOSPolicyAssignment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.osconfig_v1alpha.OsConfigZonalServiceClient.DeleteOSPolicyAssignment",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1alpha.OsConfigZonalService",
                        "rpcName": "DeleteOSPolicyAssignment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OsConfigZonalServiceRestTransport._DeleteOSPolicyAssignment._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_os_policy_assignment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_os_policy_assignment_with_metadata(
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
                    "Received response for google.cloud.osconfig_v1alpha.OsConfigZonalServiceClient.delete_os_policy_assignment",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1alpha.OsConfigZonalService",
                        "rpcName": "DeleteOSPolicyAssignment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetInstanceOSPoliciesCompliance(
        _BaseOsConfigZonalServiceRestTransport._BaseGetInstanceOSPoliciesCompliance,
        OsConfigZonalServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "OsConfigZonalServiceRestTransport.GetInstanceOSPoliciesCompliance"
            )

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
            request: instance_os_policies_compliance.GetInstanceOSPoliciesComplianceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> instance_os_policies_compliance.InstanceOSPoliciesCompliance:
            r"""Call the get instance os policies
            compliance method over HTTP.

                Args:
                    request (~.instance_os_policies_compliance.GetInstanceOSPoliciesComplianceRequest):
                        The request object. A request message for getting OS
                    policies compliance data for the given
                    Compute Engine VM instance.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.instance_os_policies_compliance.InstanceOSPoliciesCompliance:
                        This API resource represents the OS policies compliance
                    data for a Compute Engine virtual machine (VM) instance
                    at a given point in time.

                    A Compute Engine VM can have multiple OS policy
                    assignments, and each assignment can have multiple OS
                    policies. As a result, multiple OS policies could be
                    applied to a single VM.

                    You can use this API resource to determine both the
                    compliance state of your VM as well as the compliance
                    state of an individual OS policy.

                    For more information, see `View
                    compliance <https://cloud.google.com/compute/docs/os-configuration-management/view-compliance>`__.

            """

            http_options = _BaseOsConfigZonalServiceRestTransport._BaseGetInstanceOSPoliciesCompliance._get_http_options()
            request, metadata = (
                self._interceptor.pre_get_instance_os_policies_compliance(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOsConfigZonalServiceRestTransport._BaseGetInstanceOSPoliciesCompliance,
                    "_BaseGetInstanceOSPoliciesCompliance__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.osconfig_v1alpha.OsConfigZonalServiceClient.GetInstanceOSPoliciesCompliance",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1alpha.OsConfigZonalService",
                        "rpcName": "GetInstanceOSPoliciesCompliance",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OsConfigZonalServiceRestTransport._GetInstanceOSPoliciesCompliance._get_response(
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
            resp = instance_os_policies_compliance.InstanceOSPoliciesCompliance()
            pb_resp = instance_os_policies_compliance.InstanceOSPoliciesCompliance.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_instance_os_policies_compliance(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_get_instance_os_policies_compliance_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = instance_os_policies_compliance.InstanceOSPoliciesCompliance.to_json(
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
                    "Received response for google.cloud.osconfig_v1alpha.OsConfigZonalServiceClient.get_instance_os_policies_compliance",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1alpha.OsConfigZonalService",
                        "rpcName": "GetInstanceOSPoliciesCompliance",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetInventory(
        _BaseOsConfigZonalServiceRestTransport._BaseGetInventory,
        OsConfigZonalServiceRestStub,
    ):
        def __hash__(self):
            return hash("OsConfigZonalServiceRestTransport.GetInventory")

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
            request: inventory.GetInventoryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> inventory.Inventory:
            r"""Call the get inventory method over HTTP.

            Args:
                request (~.inventory.GetInventoryRequest):
                    The request object. A request message for getting
                inventory data for the specified VM.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.inventory.Inventory:
                    This API resource represents the available inventory
                data for a Compute Engine virtual machine (VM) instance
                at a given point in time.

                You can use this API resource to determine the inventory
                data of your VM.

                For more information, see `Information provided by OS
                inventory
                management <https://cloud.google.com/compute/docs/instances/os-inventory-management#data-collected>`__.

            """

            http_options = _BaseOsConfigZonalServiceRestTransport._BaseGetInventory._get_http_options()
            request, metadata = self._interceptor.pre_get_inventory(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOsConfigZonalServiceRestTransport._BaseGetInventory,
                    "_BaseGetInventory__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.osconfig_v1alpha.OsConfigZonalServiceClient.GetInventory",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1alpha.OsConfigZonalService",
                        "rpcName": "GetInventory",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OsConfigZonalServiceRestTransport._GetInventory._get_response(
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
            resp = inventory.Inventory()
            pb_resp = inventory.Inventory.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_inventory(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_inventory_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = inventory.Inventory.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.osconfig_v1alpha.OsConfigZonalServiceClient.get_inventory",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1alpha.OsConfigZonalService",
                        "rpcName": "GetInventory",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetOSPolicyAssignment(
        _BaseOsConfigZonalServiceRestTransport._BaseGetOSPolicyAssignment,
        OsConfigZonalServiceRestStub,
    ):
        def __hash__(self):
            return hash("OsConfigZonalServiceRestTransport.GetOSPolicyAssignment")

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
            request: os_policy_assignments.GetOSPolicyAssignmentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> os_policy_assignments.OSPolicyAssignment:
            r"""Call the get os policy assignment method over HTTP.

            Args:
                request (~.os_policy_assignments.GetOSPolicyAssignmentRequest):
                    The request object. A request message to get an OS policy
                assignment
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.os_policy_assignments.OSPolicyAssignment:
                    OS policy assignment is an API resource that is used to
                apply a set of OS policies to a dynamically targeted
                group of Compute Engine VM instances.

                An OS policy is used to define the desired state
                configuration for a Compute Engine VM instance through a
                set of configuration resources that provide capabilities
                such as installing or removing software packages, or
                executing a script.

                For more information, see `OS policy and OS policy
                assignment <https://cloud.google.com/compute/docs/os-configuration-management/working-with-os-policies>`__.

            """

            http_options = _BaseOsConfigZonalServiceRestTransport._BaseGetOSPolicyAssignment._get_http_options()
            request, metadata = self._interceptor.pre_get_os_policy_assignment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOsConfigZonalServiceRestTransport._BaseGetOSPolicyAssignment,
                    "_BaseGetOSPolicyAssignment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.osconfig_v1alpha.OsConfigZonalServiceClient.GetOSPolicyAssignment",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1alpha.OsConfigZonalService",
                        "rpcName": "GetOSPolicyAssignment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                OsConfigZonalServiceRestTransport._GetOSPolicyAssignment._get_response(
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
            resp = os_policy_assignments.OSPolicyAssignment()
            pb_resp = os_policy_assignments.OSPolicyAssignment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_os_policy_assignment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_os_policy_assignment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = os_policy_assignments.OSPolicyAssignment.to_json(
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
                    "Received response for google.cloud.osconfig_v1alpha.OsConfigZonalServiceClient.get_os_policy_assignment",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1alpha.OsConfigZonalService",
                        "rpcName": "GetOSPolicyAssignment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetOSPolicyAssignmentReport(
        _BaseOsConfigZonalServiceRestTransport._BaseGetOSPolicyAssignmentReport,
        OsConfigZonalServiceRestStub,
    ):
        def __hash__(self):
            return hash("OsConfigZonalServiceRestTransport.GetOSPolicyAssignmentReport")

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
            request: os_policy_assignment_reports.GetOSPolicyAssignmentReportRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> os_policy_assignment_reports.OSPolicyAssignmentReport:
            r"""Call the get os policy assignment
            report method over HTTP.

                Args:
                    request (~.os_policy_assignment_reports.GetOSPolicyAssignmentReportRequest):
                        The request object. Get a report of the OS policy
                    assignment for a VM instance.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.os_policy_assignment_reports.OSPolicyAssignmentReport:
                        A report of the OS policy assignment
                    status for a given instance.

            """

            http_options = _BaseOsConfigZonalServiceRestTransport._BaseGetOSPolicyAssignmentReport._get_http_options()
            request, metadata = self._interceptor.pre_get_os_policy_assignment_report(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOsConfigZonalServiceRestTransport._BaseGetOSPolicyAssignmentReport,
                    "_BaseGetOSPolicyAssignmentReport__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.osconfig_v1alpha.OsConfigZonalServiceClient.GetOSPolicyAssignmentReport",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1alpha.OsConfigZonalService",
                        "rpcName": "GetOSPolicyAssignmentReport",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OsConfigZonalServiceRestTransport._GetOSPolicyAssignmentReport._get_response(
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
            resp = os_policy_assignment_reports.OSPolicyAssignmentReport()
            pb_resp = os_policy_assignment_reports.OSPolicyAssignmentReport.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_os_policy_assignment_report(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_get_os_policy_assignment_report_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        os_policy_assignment_reports.OSPolicyAssignmentReport.to_json(
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
                    "Received response for google.cloud.osconfig_v1alpha.OsConfigZonalServiceClient.get_os_policy_assignment_report",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1alpha.OsConfigZonalService",
                        "rpcName": "GetOSPolicyAssignmentReport",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetVulnerabilityReport(
        _BaseOsConfigZonalServiceRestTransport._BaseGetVulnerabilityReport,
        OsConfigZonalServiceRestStub,
    ):
        def __hash__(self):
            return hash("OsConfigZonalServiceRestTransport.GetVulnerabilityReport")

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
            request: vulnerability.GetVulnerabilityReportRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vulnerability.VulnerabilityReport:
            r"""Call the get vulnerability report method over HTTP.

            Args:
                request (~.vulnerability.GetVulnerabilityReportRequest):
                    The request object. A request message for getting the
                vulnerability report for the specified
                VM.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vulnerability.VulnerabilityReport:
                    This API resource represents the vulnerability report
                for a specified Compute Engine virtual machine (VM)
                instance at a given point in time.

                For more information, see `Vulnerability
                reports <https://cloud.google.com/compute/docs/instances/os-inventory-management#vulnerability-reports>`__.

            """

            http_options = _BaseOsConfigZonalServiceRestTransport._BaseGetVulnerabilityReport._get_http_options()
            request, metadata = self._interceptor.pre_get_vulnerability_report(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOsConfigZonalServiceRestTransport._BaseGetVulnerabilityReport,
                    "_BaseGetVulnerabilityReport__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.osconfig_v1alpha.OsConfigZonalServiceClient.GetVulnerabilityReport",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1alpha.OsConfigZonalService",
                        "rpcName": "GetVulnerabilityReport",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                OsConfigZonalServiceRestTransport._GetVulnerabilityReport._get_response(
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
            resp = vulnerability.VulnerabilityReport()
            pb_resp = vulnerability.VulnerabilityReport.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_vulnerability_report(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_vulnerability_report_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vulnerability.VulnerabilityReport.to_json(
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
                    "Received response for google.cloud.osconfig_v1alpha.OsConfigZonalServiceClient.get_vulnerability_report",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1alpha.OsConfigZonalService",
                        "rpcName": "GetVulnerabilityReport",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListInstanceOSPoliciesCompliances(
        _BaseOsConfigZonalServiceRestTransport._BaseListInstanceOSPoliciesCompliances,
        OsConfigZonalServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "OsConfigZonalServiceRestTransport.ListInstanceOSPoliciesCompliances"
            )

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
            request: instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse:
            r"""Call the list instance os policies
            compliances method over HTTP.

                Args:
                    request (~.instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesRequest):
                        The request object. A request message for listing OS
                    policies compliance data for all Compute
                    Engine VMs in the given location.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse:
                        A response message for listing OS
                    policies compliance data for all Compute
                    Engine VMs in the given location.

            """

            http_options = _BaseOsConfigZonalServiceRestTransport._BaseListInstanceOSPoliciesCompliances._get_http_options()
            request, metadata = (
                self._interceptor.pre_list_instance_os_policies_compliances(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOsConfigZonalServiceRestTransport._BaseListInstanceOSPoliciesCompliances,
                    "_BaseListInstanceOSPoliciesCompliances__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.osconfig_v1alpha.OsConfigZonalServiceClient.ListInstanceOSPoliciesCompliances",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1alpha.OsConfigZonalService",
                        "rpcName": "ListInstanceOSPoliciesCompliances",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OsConfigZonalServiceRestTransport._ListInstanceOSPoliciesCompliances._get_response(
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
            resp = instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse()
            pb_resp = instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_instance_os_policies_compliances(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_instance_os_policies_compliances_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse.to_json(
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
                    "Received response for google.cloud.osconfig_v1alpha.OsConfigZonalServiceClient.list_instance_os_policies_compliances",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1alpha.OsConfigZonalService",
                        "rpcName": "ListInstanceOSPoliciesCompliances",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListInventories(
        _BaseOsConfigZonalServiceRestTransport._BaseListInventories,
        OsConfigZonalServiceRestStub,
    ):
        def __hash__(self):
            return hash("OsConfigZonalServiceRestTransport.ListInventories")

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
            request: inventory.ListInventoriesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> inventory.ListInventoriesResponse:
            r"""Call the list inventories method over HTTP.

            Args:
                request (~.inventory.ListInventoriesRequest):
                    The request object. A request message for listing
                inventory data for all VMs in the
                specified location.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.inventory.ListInventoriesResponse:
                    A response message for listing
                inventory data for all VMs in a
                specified location.

            """

            http_options = _BaseOsConfigZonalServiceRestTransport._BaseListInventories._get_http_options()
            request, metadata = self._interceptor.pre_list_inventories(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOsConfigZonalServiceRestTransport._BaseListInventories,
                    "_BaseListInventories__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.osconfig_v1alpha.OsConfigZonalServiceClient.ListInventories",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1alpha.OsConfigZonalService",
                        "rpcName": "ListInventories",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OsConfigZonalServiceRestTransport._ListInventories._get_response(
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
            resp = inventory.ListInventoriesResponse()
            pb_resp = inventory.ListInventoriesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_inventories(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_inventories_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = inventory.ListInventoriesResponse.to_json(
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
                    "Received response for google.cloud.osconfig_v1alpha.OsConfigZonalServiceClient.list_inventories",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1alpha.OsConfigZonalService",
                        "rpcName": "ListInventories",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListOSPolicyAssignmentReports(
        _BaseOsConfigZonalServiceRestTransport._BaseListOSPolicyAssignmentReports,
        OsConfigZonalServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "OsConfigZonalServiceRestTransport.ListOSPolicyAssignmentReports"
            )

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
            request: os_policy_assignment_reports.ListOSPolicyAssignmentReportsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse:
            r"""Call the list os policy assignment
            reports method over HTTP.

                Args:
                    request (~.os_policy_assignment_reports.ListOSPolicyAssignmentReportsRequest):
                        The request object. List the OS policy assignment reports
                    for VM instances.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse:
                        A response message for listing OS
                    Policy assignment reports including the
                    page of results and page token.

            """

            http_options = _BaseOsConfigZonalServiceRestTransport._BaseListOSPolicyAssignmentReports._get_http_options()
            request, metadata = self._interceptor.pre_list_os_policy_assignment_reports(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOsConfigZonalServiceRestTransport._BaseListOSPolicyAssignmentReports,
                    "_BaseListOSPolicyAssignmentReports__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.osconfig_v1alpha.OsConfigZonalServiceClient.ListOSPolicyAssignmentReports",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1alpha.OsConfigZonalService",
                        "rpcName": "ListOSPolicyAssignmentReports",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OsConfigZonalServiceRestTransport._ListOSPolicyAssignmentReports._get_response(
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
            resp = os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse()
            pb_resp = (
                os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse.pb(
                    resp
                )
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_os_policy_assignment_reports(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_os_policy_assignment_reports_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse.to_json(
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
                    "Received response for google.cloud.osconfig_v1alpha.OsConfigZonalServiceClient.list_os_policy_assignment_reports",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1alpha.OsConfigZonalService",
                        "rpcName": "ListOSPolicyAssignmentReports",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListOSPolicyAssignmentRevisions(
        _BaseOsConfigZonalServiceRestTransport._BaseListOSPolicyAssignmentRevisions,
        OsConfigZonalServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "OsConfigZonalServiceRestTransport.ListOSPolicyAssignmentRevisions"
            )

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
            request: os_policy_assignments.ListOSPolicyAssignmentRevisionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse:
            r"""Call the list os policy assignment
            revisions method over HTTP.

                Args:
                    request (~.os_policy_assignments.ListOSPolicyAssignmentRevisionsRequest):
                        The request object. A request message to list revisions
                    for a OS policy assignment
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse:
                        A response message for listing all
                    revisions for a OS policy assignment.

            """

            http_options = _BaseOsConfigZonalServiceRestTransport._BaseListOSPolicyAssignmentRevisions._get_http_options()
            request, metadata = (
                self._interceptor.pre_list_os_policy_assignment_revisions(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOsConfigZonalServiceRestTransport._BaseListOSPolicyAssignmentRevisions,
                    "_BaseListOSPolicyAssignmentRevisions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.osconfig_v1alpha.OsConfigZonalServiceClient.ListOSPolicyAssignmentRevisions",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1alpha.OsConfigZonalService",
                        "rpcName": "ListOSPolicyAssignmentRevisions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OsConfigZonalServiceRestTransport._ListOSPolicyAssignmentRevisions._get_response(
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
            resp = os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse()
            pb_resp = os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_os_policy_assignment_revisions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_os_policy_assignment_revisions_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse.to_json(
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
                    "Received response for google.cloud.osconfig_v1alpha.OsConfigZonalServiceClient.list_os_policy_assignment_revisions",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1alpha.OsConfigZonalService",
                        "rpcName": "ListOSPolicyAssignmentRevisions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListOSPolicyAssignments(
        _BaseOsConfigZonalServiceRestTransport._BaseListOSPolicyAssignments,
        OsConfigZonalServiceRestStub,
    ):
        def __hash__(self):
            return hash("OsConfigZonalServiceRestTransport.ListOSPolicyAssignments")

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
            request: os_policy_assignments.ListOSPolicyAssignmentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> os_policy_assignments.ListOSPolicyAssignmentsResponse:
            r"""Call the list os policy
            assignments method over HTTP.

                Args:
                    request (~.os_policy_assignments.ListOSPolicyAssignmentsRequest):
                        The request object. A request message to list OS policy
                    assignments for a parent resource
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.os_policy_assignments.ListOSPolicyAssignmentsResponse:
                        A response message for listing all
                    assignments under given parent.

            """

            http_options = _BaseOsConfigZonalServiceRestTransport._BaseListOSPolicyAssignments._get_http_options()
            request, metadata = self._interceptor.pre_list_os_policy_assignments(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOsConfigZonalServiceRestTransport._BaseListOSPolicyAssignments,
                    "_BaseListOSPolicyAssignments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.osconfig_v1alpha.OsConfigZonalServiceClient.ListOSPolicyAssignments",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1alpha.OsConfigZonalService",
                        "rpcName": "ListOSPolicyAssignments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OsConfigZonalServiceRestTransport._ListOSPolicyAssignments._get_response(
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
            resp = os_policy_assignments.ListOSPolicyAssignmentsResponse()
            pb_resp = os_policy_assignments.ListOSPolicyAssignmentsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_os_policy_assignments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_os_policy_assignments_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        os_policy_assignments.ListOSPolicyAssignmentsResponse.to_json(
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
                    "Received response for google.cloud.osconfig_v1alpha.OsConfigZonalServiceClient.list_os_policy_assignments",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1alpha.OsConfigZonalService",
                        "rpcName": "ListOSPolicyAssignments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListVulnerabilityReports(
        _BaseOsConfigZonalServiceRestTransport._BaseListVulnerabilityReports,
        OsConfigZonalServiceRestStub,
    ):
        def __hash__(self):
            return hash("OsConfigZonalServiceRestTransport.ListVulnerabilityReports")

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
            request: vulnerability.ListVulnerabilityReportsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vulnerability.ListVulnerabilityReportsResponse:
            r"""Call the list vulnerability
            reports method over HTTP.

                Args:
                    request (~.vulnerability.ListVulnerabilityReportsRequest):
                        The request object. A request message for listing
                    vulnerability reports for all VM
                    instances in the specified location.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.vulnerability.ListVulnerabilityReportsResponse:
                        A response message for listing
                    vulnerability reports for all VM
                    instances in the specified location.

            """

            http_options = _BaseOsConfigZonalServiceRestTransport._BaseListVulnerabilityReports._get_http_options()
            request, metadata = self._interceptor.pre_list_vulnerability_reports(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOsConfigZonalServiceRestTransport._BaseListVulnerabilityReports,
                    "_BaseListVulnerabilityReports__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.osconfig_v1alpha.OsConfigZonalServiceClient.ListVulnerabilityReports",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1alpha.OsConfigZonalService",
                        "rpcName": "ListVulnerabilityReports",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OsConfigZonalServiceRestTransport._ListVulnerabilityReports._get_response(
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
            resp = vulnerability.ListVulnerabilityReportsResponse()
            pb_resp = vulnerability.ListVulnerabilityReportsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_vulnerability_reports(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_vulnerability_reports_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        vulnerability.ListVulnerabilityReportsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.osconfig_v1alpha.OsConfigZonalServiceClient.list_vulnerability_reports",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1alpha.OsConfigZonalService",
                        "rpcName": "ListVulnerabilityReports",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateOSPolicyAssignment(
        _BaseOsConfigZonalServiceRestTransport._BaseUpdateOSPolicyAssignment,
        OsConfigZonalServiceRestStub,
    ):
        def __hash__(self):
            return hash("OsConfigZonalServiceRestTransport.UpdateOSPolicyAssignment")

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
            request: os_policy_assignments.UpdateOSPolicyAssignmentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update os policy
            assignment method over HTTP.

                Args:
                    request (~.os_policy_assignments.UpdateOSPolicyAssignmentRequest):
                        The request object. A request message to update an OS
                    policy assignment
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

            http_options = _BaseOsConfigZonalServiceRestTransport._BaseUpdateOSPolicyAssignment._get_http_options()
            request, metadata = self._interceptor.pre_update_os_policy_assignment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseOsConfigZonalServiceRestTransport._BaseUpdateOSPolicyAssignment,
                    "_BaseUpdateOSPolicyAssignment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.osconfig_v1alpha.OsConfigZonalServiceClient.UpdateOSPolicyAssignment",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1alpha.OsConfigZonalService",
                        "rpcName": "UpdateOSPolicyAssignment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = OsConfigZonalServiceRestTransport._UpdateOSPolicyAssignment._get_response(
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

            resp = self._interceptor.post_update_os_policy_assignment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_os_policy_assignment_with_metadata(
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
                    "Received response for google.cloud.osconfig_v1alpha.OsConfigZonalServiceClient.update_os_policy_assignment",
                    extra={
                        "serviceName": "google.cloud.osconfig.v1alpha.OsConfigZonalService",
                        "rpcName": "UpdateOSPolicyAssignment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_os_policy_assignment(
        self,
    ) -> Callable[
        [os_policy_assignments.CreateOSPolicyAssignmentRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateOSPolicyAssignment(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_os_policy_assignment(
        self,
    ) -> Callable[
        [os_policy_assignments.DeleteOSPolicyAssignmentRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteOSPolicyAssignment(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_instance_os_policies_compliance(
        self,
    ) -> Callable[
        [instance_os_policies_compliance.GetInstanceOSPoliciesComplianceRequest],
        instance_os_policies_compliance.InstanceOSPoliciesCompliance,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetInstanceOSPoliciesCompliance(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_inventory(
        self,
    ) -> Callable[[inventory.GetInventoryRequest], inventory.Inventory]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetInventory(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_os_policy_assignment(
        self,
    ) -> Callable[
        [os_policy_assignments.GetOSPolicyAssignmentRequest],
        os_policy_assignments.OSPolicyAssignment,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetOSPolicyAssignment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_os_policy_assignment_report(
        self,
    ) -> Callable[
        [os_policy_assignment_reports.GetOSPolicyAssignmentReportRequest],
        os_policy_assignment_reports.OSPolicyAssignmentReport,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetOSPolicyAssignmentReport(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_vulnerability_report(
        self,
    ) -> Callable[
        [vulnerability.GetVulnerabilityReportRequest], vulnerability.VulnerabilityReport
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetVulnerabilityReport(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_instance_os_policies_compliances(
        self,
    ) -> Callable[
        [instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesRequest],
        instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListInstanceOSPoliciesCompliances(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_inventories(
        self,
    ) -> Callable[
        [inventory.ListInventoriesRequest], inventory.ListInventoriesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListInventories(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_os_policy_assignment_reports(
        self,
    ) -> Callable[
        [os_policy_assignment_reports.ListOSPolicyAssignmentReportsRequest],
        os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListOSPolicyAssignmentReports(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_os_policy_assignment_revisions(
        self,
    ) -> Callable[
        [os_policy_assignments.ListOSPolicyAssignmentRevisionsRequest],
        os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListOSPolicyAssignmentRevisions(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_os_policy_assignments(
        self,
    ) -> Callable[
        [os_policy_assignments.ListOSPolicyAssignmentsRequest],
        os_policy_assignments.ListOSPolicyAssignmentsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListOSPolicyAssignments(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_vulnerability_reports(
        self,
    ) -> Callable[
        [vulnerability.ListVulnerabilityReportsRequest],
        vulnerability.ListVulnerabilityReportsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListVulnerabilityReports(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_os_policy_assignment(
        self,
    ) -> Callable[
        [os_policy_assignments.UpdateOSPolicyAssignmentRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateOSPolicyAssignment(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("OsConfigZonalServiceRestTransport",)
