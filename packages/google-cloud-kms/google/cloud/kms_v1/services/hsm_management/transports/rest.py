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
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, operations_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.kms_v1._compat import transcode_request
from google.cloud.kms_v1.types import hsm_management

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseHsmManagementRestTransport

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


class HsmManagementRestInterceptor:
    """Interceptor for HsmManagement.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the HsmManagementRestTransport.

    .. code-block:: python
        class MyCustomHsmManagementInterceptor(HsmManagementRestInterceptor):
            def pre_approve_single_tenant_hsm_instance_proposal(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_approve_single_tenant_hsm_instance_proposal(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_single_tenant_hsm_instance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_single_tenant_hsm_instance(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_single_tenant_hsm_instance_proposal(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_single_tenant_hsm_instance_proposal(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_single_tenant_hsm_instance_proposal(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_execute_single_tenant_hsm_instance_proposal(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_execute_single_tenant_hsm_instance_proposal(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_single_tenant_hsm_instance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_single_tenant_hsm_instance(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_single_tenant_hsm_instance_proposal(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_single_tenant_hsm_instance_proposal(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_single_tenant_hsm_instance_proposals(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_single_tenant_hsm_instance_proposals(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_single_tenant_hsm_instances(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_single_tenant_hsm_instances(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = HsmManagementRestTransport(interceptor=MyCustomHsmManagementInterceptor())
        client = HsmManagementClient(transport=transport)


    """

    def pre_approve_single_tenant_hsm_instance_proposal(
        self,
        request: hsm_management.ApproveSingleTenantHsmInstanceProposalRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        hsm_management.ApproveSingleTenantHsmInstanceProposalRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for approve_single_tenant_hsm_instance_proposal

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HsmManagement server.
        """
        return request, metadata

    def post_approve_single_tenant_hsm_instance_proposal(
        self, response: hsm_management.ApproveSingleTenantHsmInstanceProposalResponse
    ) -> hsm_management.ApproveSingleTenantHsmInstanceProposalResponse:
        """Post-rpc interceptor for approve_single_tenant_hsm_instance_proposal

        DEPRECATED. Please use the `post_approve_single_tenant_hsm_instance_proposal_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the HsmManagement server but before
        it is returned to user code. This `post_approve_single_tenant_hsm_instance_proposal` interceptor runs
        before the `post_approve_single_tenant_hsm_instance_proposal_with_metadata` interceptor.
        """
        return response

    def post_approve_single_tenant_hsm_instance_proposal_with_metadata(
        self,
        response: hsm_management.ApproveSingleTenantHsmInstanceProposalResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        hsm_management.ApproveSingleTenantHsmInstanceProposalResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for approve_single_tenant_hsm_instance_proposal

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the HsmManagement server but before it is returned to user code.

        We recommend only using this `post_approve_single_tenant_hsm_instance_proposal_with_metadata`
        interceptor in new development instead of the `post_approve_single_tenant_hsm_instance_proposal` interceptor.
        When both interceptors are used, this `post_approve_single_tenant_hsm_instance_proposal_with_metadata` interceptor runs after the
        `post_approve_single_tenant_hsm_instance_proposal` interceptor. The (possibly modified) response returned by
        `post_approve_single_tenant_hsm_instance_proposal` will be passed to
        `post_approve_single_tenant_hsm_instance_proposal_with_metadata`.
        """
        return response, metadata

    def pre_create_single_tenant_hsm_instance(
        self,
        request: hsm_management.CreateSingleTenantHsmInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        hsm_management.CreateSingleTenantHsmInstanceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_single_tenant_hsm_instance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HsmManagement server.
        """
        return request, metadata

    def post_create_single_tenant_hsm_instance(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_single_tenant_hsm_instance

        DEPRECATED. Please use the `post_create_single_tenant_hsm_instance_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the HsmManagement server but before
        it is returned to user code. This `post_create_single_tenant_hsm_instance` interceptor runs
        before the `post_create_single_tenant_hsm_instance_with_metadata` interceptor.
        """
        return response

    def post_create_single_tenant_hsm_instance_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_single_tenant_hsm_instance

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the HsmManagement server but before it is returned to user code.

        We recommend only using this `post_create_single_tenant_hsm_instance_with_metadata`
        interceptor in new development instead of the `post_create_single_tenant_hsm_instance` interceptor.
        When both interceptors are used, this `post_create_single_tenant_hsm_instance_with_metadata` interceptor runs after the
        `post_create_single_tenant_hsm_instance` interceptor. The (possibly modified) response returned by
        `post_create_single_tenant_hsm_instance` will be passed to
        `post_create_single_tenant_hsm_instance_with_metadata`.
        """
        return response, metadata

    def pre_create_single_tenant_hsm_instance_proposal(
        self,
        request: hsm_management.CreateSingleTenantHsmInstanceProposalRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        hsm_management.CreateSingleTenantHsmInstanceProposalRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_single_tenant_hsm_instance_proposal

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HsmManagement server.
        """
        return request, metadata

    def post_create_single_tenant_hsm_instance_proposal(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_single_tenant_hsm_instance_proposal

        DEPRECATED. Please use the `post_create_single_tenant_hsm_instance_proposal_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the HsmManagement server but before
        it is returned to user code. This `post_create_single_tenant_hsm_instance_proposal` interceptor runs
        before the `post_create_single_tenant_hsm_instance_proposal_with_metadata` interceptor.
        """
        return response

    def post_create_single_tenant_hsm_instance_proposal_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_single_tenant_hsm_instance_proposal

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the HsmManagement server but before it is returned to user code.

        We recommend only using this `post_create_single_tenant_hsm_instance_proposal_with_metadata`
        interceptor in new development instead of the `post_create_single_tenant_hsm_instance_proposal` interceptor.
        When both interceptors are used, this `post_create_single_tenant_hsm_instance_proposal_with_metadata` interceptor runs after the
        `post_create_single_tenant_hsm_instance_proposal` interceptor. The (possibly modified) response returned by
        `post_create_single_tenant_hsm_instance_proposal` will be passed to
        `post_create_single_tenant_hsm_instance_proposal_with_metadata`.
        """
        return response, metadata

    def pre_delete_single_tenant_hsm_instance_proposal(
        self,
        request: hsm_management.DeleteSingleTenantHsmInstanceProposalRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        hsm_management.DeleteSingleTenantHsmInstanceProposalRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_single_tenant_hsm_instance_proposal

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HsmManagement server.
        """
        return request, metadata

    def pre_execute_single_tenant_hsm_instance_proposal(
        self,
        request: hsm_management.ExecuteSingleTenantHsmInstanceProposalRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        hsm_management.ExecuteSingleTenantHsmInstanceProposalRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for execute_single_tenant_hsm_instance_proposal

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HsmManagement server.
        """
        return request, metadata

    def post_execute_single_tenant_hsm_instance_proposal(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for execute_single_tenant_hsm_instance_proposal

        DEPRECATED. Please use the `post_execute_single_tenant_hsm_instance_proposal_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the HsmManagement server but before
        it is returned to user code. This `post_execute_single_tenant_hsm_instance_proposal` interceptor runs
        before the `post_execute_single_tenant_hsm_instance_proposal_with_metadata` interceptor.
        """
        return response

    def post_execute_single_tenant_hsm_instance_proposal_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for execute_single_tenant_hsm_instance_proposal

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the HsmManagement server but before it is returned to user code.

        We recommend only using this `post_execute_single_tenant_hsm_instance_proposal_with_metadata`
        interceptor in new development instead of the `post_execute_single_tenant_hsm_instance_proposal` interceptor.
        When both interceptors are used, this `post_execute_single_tenant_hsm_instance_proposal_with_metadata` interceptor runs after the
        `post_execute_single_tenant_hsm_instance_proposal` interceptor. The (possibly modified) response returned by
        `post_execute_single_tenant_hsm_instance_proposal` will be passed to
        `post_execute_single_tenant_hsm_instance_proposal_with_metadata`.
        """
        return response, metadata

    def pre_get_single_tenant_hsm_instance(
        self,
        request: hsm_management.GetSingleTenantHsmInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        hsm_management.GetSingleTenantHsmInstanceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_single_tenant_hsm_instance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HsmManagement server.
        """
        return request, metadata

    def post_get_single_tenant_hsm_instance(
        self, response: hsm_management.SingleTenantHsmInstance
    ) -> hsm_management.SingleTenantHsmInstance:
        """Post-rpc interceptor for get_single_tenant_hsm_instance

        DEPRECATED. Please use the `post_get_single_tenant_hsm_instance_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the HsmManagement server but before
        it is returned to user code. This `post_get_single_tenant_hsm_instance` interceptor runs
        before the `post_get_single_tenant_hsm_instance_with_metadata` interceptor.
        """
        return response

    def post_get_single_tenant_hsm_instance_with_metadata(
        self,
        response: hsm_management.SingleTenantHsmInstance,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        hsm_management.SingleTenantHsmInstance, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_single_tenant_hsm_instance

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the HsmManagement server but before it is returned to user code.

        We recommend only using this `post_get_single_tenant_hsm_instance_with_metadata`
        interceptor in new development instead of the `post_get_single_tenant_hsm_instance` interceptor.
        When both interceptors are used, this `post_get_single_tenant_hsm_instance_with_metadata` interceptor runs after the
        `post_get_single_tenant_hsm_instance` interceptor. The (possibly modified) response returned by
        `post_get_single_tenant_hsm_instance` will be passed to
        `post_get_single_tenant_hsm_instance_with_metadata`.
        """
        return response, metadata

    def pre_get_single_tenant_hsm_instance_proposal(
        self,
        request: hsm_management.GetSingleTenantHsmInstanceProposalRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        hsm_management.GetSingleTenantHsmInstanceProposalRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_single_tenant_hsm_instance_proposal

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HsmManagement server.
        """
        return request, metadata

    def post_get_single_tenant_hsm_instance_proposal(
        self, response: hsm_management.SingleTenantHsmInstanceProposal
    ) -> hsm_management.SingleTenantHsmInstanceProposal:
        """Post-rpc interceptor for get_single_tenant_hsm_instance_proposal

        DEPRECATED. Please use the `post_get_single_tenant_hsm_instance_proposal_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the HsmManagement server but before
        it is returned to user code. This `post_get_single_tenant_hsm_instance_proposal` interceptor runs
        before the `post_get_single_tenant_hsm_instance_proposal_with_metadata` interceptor.
        """
        return response

    def post_get_single_tenant_hsm_instance_proposal_with_metadata(
        self,
        response: hsm_management.SingleTenantHsmInstanceProposal,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        hsm_management.SingleTenantHsmInstanceProposal,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_single_tenant_hsm_instance_proposal

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the HsmManagement server but before it is returned to user code.

        We recommend only using this `post_get_single_tenant_hsm_instance_proposal_with_metadata`
        interceptor in new development instead of the `post_get_single_tenant_hsm_instance_proposal` interceptor.
        When both interceptors are used, this `post_get_single_tenant_hsm_instance_proposal_with_metadata` interceptor runs after the
        `post_get_single_tenant_hsm_instance_proposal` interceptor. The (possibly modified) response returned by
        `post_get_single_tenant_hsm_instance_proposal` will be passed to
        `post_get_single_tenant_hsm_instance_proposal_with_metadata`.
        """
        return response, metadata

    def pre_list_single_tenant_hsm_instance_proposals(
        self,
        request: hsm_management.ListSingleTenantHsmInstanceProposalsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        hsm_management.ListSingleTenantHsmInstanceProposalsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_single_tenant_hsm_instance_proposals

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HsmManagement server.
        """
        return request, metadata

    def post_list_single_tenant_hsm_instance_proposals(
        self, response: hsm_management.ListSingleTenantHsmInstanceProposalsResponse
    ) -> hsm_management.ListSingleTenantHsmInstanceProposalsResponse:
        """Post-rpc interceptor for list_single_tenant_hsm_instance_proposals

        DEPRECATED. Please use the `post_list_single_tenant_hsm_instance_proposals_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the HsmManagement server but before
        it is returned to user code. This `post_list_single_tenant_hsm_instance_proposals` interceptor runs
        before the `post_list_single_tenant_hsm_instance_proposals_with_metadata` interceptor.
        """
        return response

    def post_list_single_tenant_hsm_instance_proposals_with_metadata(
        self,
        response: hsm_management.ListSingleTenantHsmInstanceProposalsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        hsm_management.ListSingleTenantHsmInstanceProposalsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_single_tenant_hsm_instance_proposals

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the HsmManagement server but before it is returned to user code.

        We recommend only using this `post_list_single_tenant_hsm_instance_proposals_with_metadata`
        interceptor in new development instead of the `post_list_single_tenant_hsm_instance_proposals` interceptor.
        When both interceptors are used, this `post_list_single_tenant_hsm_instance_proposals_with_metadata` interceptor runs after the
        `post_list_single_tenant_hsm_instance_proposals` interceptor. The (possibly modified) response returned by
        `post_list_single_tenant_hsm_instance_proposals` will be passed to
        `post_list_single_tenant_hsm_instance_proposals_with_metadata`.
        """
        return response, metadata

    def pre_list_single_tenant_hsm_instances(
        self,
        request: hsm_management.ListSingleTenantHsmInstancesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        hsm_management.ListSingleTenantHsmInstancesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_single_tenant_hsm_instances

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HsmManagement server.
        """
        return request, metadata

    def post_list_single_tenant_hsm_instances(
        self, response: hsm_management.ListSingleTenantHsmInstancesResponse
    ) -> hsm_management.ListSingleTenantHsmInstancesResponse:
        """Post-rpc interceptor for list_single_tenant_hsm_instances

        DEPRECATED. Please use the `post_list_single_tenant_hsm_instances_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the HsmManagement server but before
        it is returned to user code. This `post_list_single_tenant_hsm_instances` interceptor runs
        before the `post_list_single_tenant_hsm_instances_with_metadata` interceptor.
        """
        return response

    def post_list_single_tenant_hsm_instances_with_metadata(
        self,
        response: hsm_management.ListSingleTenantHsmInstancesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        hsm_management.ListSingleTenantHsmInstancesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_single_tenant_hsm_instances

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the HsmManagement server but before it is returned to user code.

        We recommend only using this `post_list_single_tenant_hsm_instances_with_metadata`
        interceptor in new development instead of the `post_list_single_tenant_hsm_instances` interceptor.
        When both interceptors are used, this `post_list_single_tenant_hsm_instances_with_metadata` interceptor runs after the
        `post_list_single_tenant_hsm_instances` interceptor. The (possibly modified) response returned by
        `post_list_single_tenant_hsm_instances` will be passed to
        `post_list_single_tenant_hsm_instances_with_metadata`.
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
        before they are sent to the HsmManagement server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the HsmManagement server but before
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
        before they are sent to the HsmManagement server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the HsmManagement server but before
        it is returned to user code.
        """
        return response

    def pre_get_iam_policy(
        self,
        request: iam_policy_pb2.GetIamPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.GetIamPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HsmManagement server.
        """
        return request, metadata

    def post_get_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the HsmManagement server but before
        it is returned to user code.
        """
        return response

    def pre_set_iam_policy(
        self,
        request: iam_policy_pb2.SetIamPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.SetIamPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HsmManagement server.
        """
        return request, metadata

    def post_set_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the HsmManagement server but before
        it is returned to user code.
        """
        return response

    def pre_test_iam_permissions(
        self,
        request: iam_policy_pb2.TestIamPermissionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.TestIamPermissionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HsmManagement server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the response
        after it is returned by the HsmManagement server but before
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
        before they are sent to the HsmManagement server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the HsmManagement server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class HsmManagementRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: HsmManagementRestInterceptor


class HsmManagementRestTransport(_BaseHsmManagementRestTransport):
    """REST backend synchronous transport for HsmManagement.

    Google Cloud HSM Management Service

    Provides interfaces for managing HSM instances.

    Implements a REST model with the following objects:

    - [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]
    - [SingleTenantHsmInstanceProposal][google.cloud.kms.v1.SingleTenantHsmInstanceProposal]

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "cloudkms.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[HsmManagementRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'cloudkms.googleapis.com').
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
            interceptor (Optional[HsmManagementRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or HsmManagementRestInterceptor()
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
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}",
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

    class _ApproveSingleTenantHsmInstanceProposal(
        _BaseHsmManagementRestTransport._BaseApproveSingleTenantHsmInstanceProposal,
        HsmManagementRestStub,
    ):
        def __hash__(self):
            return hash(
                "HsmManagementRestTransport.ApproveSingleTenantHsmInstanceProposal"
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
                data=body,
            )
            return response

        def __call__(
            self,
            request: hsm_management.ApproveSingleTenantHsmInstanceProposalRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> hsm_management.ApproveSingleTenantHsmInstanceProposalResponse:
            r"""Call the approve single tenant hsm
            instance proposal method over HTTP.

                Args:
                    request (~.hsm_management.ApproveSingleTenantHsmInstanceProposalRequest):
                        The request object. Request message for
                    [HsmManagement.ApproveSingleTenantHsmInstanceProposal][google.cloud.kms.v1.HsmManagement.ApproveSingleTenantHsmInstanceProposal].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.hsm_management.ApproveSingleTenantHsmInstanceProposalResponse:
                        Response message for
                    [HsmManagement.ApproveSingleTenantHsmInstanceProposal][google.cloud.kms.v1.HsmManagement.ApproveSingleTenantHsmInstanceProposal].

            """

            http_options = _BaseHsmManagementRestTransport._BaseApproveSingleTenantHsmInstanceProposal._get_http_options()
            request, metadata = (
                self._interceptor.pre_approve_single_tenant_hsm_instance_proposal(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHsmManagementRestTransport._BaseApproveSingleTenantHsmInstanceProposal,
                    "_BaseApproveSingleTenantHsmInstanceProposal__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.HsmManagementClient.ApproveSingleTenantHsmInstanceProposal",
                    extra={
                        "serviceName": "google.cloud.kms.v1.HsmManagement",
                        "rpcName": "ApproveSingleTenantHsmInstanceProposal",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = HsmManagementRestTransport._ApproveSingleTenantHsmInstanceProposal._get_response(
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
            resp = hsm_management.ApproveSingleTenantHsmInstanceProposalResponse()
            pb_resp = hsm_management.ApproveSingleTenantHsmInstanceProposalResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_approve_single_tenant_hsm_instance_proposal(
                resp
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_approve_single_tenant_hsm_instance_proposal_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = hsm_management.ApproveSingleTenantHsmInstanceProposalResponse.to_json(
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
                    "Received response for google.cloud.kms_v1.HsmManagementClient.approve_single_tenant_hsm_instance_proposal",
                    extra={
                        "serviceName": "google.cloud.kms.v1.HsmManagement",
                        "rpcName": "ApproveSingleTenantHsmInstanceProposal",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateSingleTenantHsmInstance(
        _BaseHsmManagementRestTransport._BaseCreateSingleTenantHsmInstance,
        HsmManagementRestStub,
    ):
        def __hash__(self):
            return hash("HsmManagementRestTransport.CreateSingleTenantHsmInstance")

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
            request: hsm_management.CreateSingleTenantHsmInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create single tenant hsm
            instance method over HTTP.

                Args:
                    request (~.hsm_management.CreateSingleTenantHsmInstanceRequest):
                        The request object. Request message for
                    [HsmManagement.CreateSingleTenantHsmInstance][google.cloud.kms.v1.HsmManagement.CreateSingleTenantHsmInstance].
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

            http_options = _BaseHsmManagementRestTransport._BaseCreateSingleTenantHsmInstance._get_http_options()
            request, metadata = self._interceptor.pre_create_single_tenant_hsm_instance(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHsmManagementRestTransport._BaseCreateSingleTenantHsmInstance,
                    "_BaseCreateSingleTenantHsmInstance__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.HsmManagementClient.CreateSingleTenantHsmInstance",
                    extra={
                        "serviceName": "google.cloud.kms.v1.HsmManagement",
                        "rpcName": "CreateSingleTenantHsmInstance",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                HsmManagementRestTransport._CreateSingleTenantHsmInstance._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_single_tenant_hsm_instance(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_create_single_tenant_hsm_instance_with_metadata(
                    resp, response_metadata
                )
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
                    "Received response for google.cloud.kms_v1.HsmManagementClient.create_single_tenant_hsm_instance",
                    extra={
                        "serviceName": "google.cloud.kms.v1.HsmManagement",
                        "rpcName": "CreateSingleTenantHsmInstance",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateSingleTenantHsmInstanceProposal(
        _BaseHsmManagementRestTransport._BaseCreateSingleTenantHsmInstanceProposal,
        HsmManagementRestStub,
    ):
        def __hash__(self):
            return hash(
                "HsmManagementRestTransport.CreateSingleTenantHsmInstanceProposal"
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
                data=body,
            )
            return response

        def __call__(
            self,
            request: hsm_management.CreateSingleTenantHsmInstanceProposalRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create single tenant hsm
            instance proposal method over HTTP.

                Args:
                    request (~.hsm_management.CreateSingleTenantHsmInstanceProposalRequest):
                        The request object. Request message for
                    [HsmManagement.CreateSingleTenantHsmInstanceProposal][google.cloud.kms.v1.HsmManagement.CreateSingleTenantHsmInstanceProposal].
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

            http_options = _BaseHsmManagementRestTransport._BaseCreateSingleTenantHsmInstanceProposal._get_http_options()
            request, metadata = (
                self._interceptor.pre_create_single_tenant_hsm_instance_proposal(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHsmManagementRestTransport._BaseCreateSingleTenantHsmInstanceProposal,
                    "_BaseCreateSingleTenantHsmInstanceProposal__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.HsmManagementClient.CreateSingleTenantHsmInstanceProposal",
                    extra={
                        "serviceName": "google.cloud.kms.v1.HsmManagement",
                        "rpcName": "CreateSingleTenantHsmInstanceProposal",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = HsmManagementRestTransport._CreateSingleTenantHsmInstanceProposal._get_response(
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

            resp = self._interceptor.post_create_single_tenant_hsm_instance_proposal(
                resp
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_create_single_tenant_hsm_instance_proposal_with_metadata(
                    resp, response_metadata
                )
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
                    "Received response for google.cloud.kms_v1.HsmManagementClient.create_single_tenant_hsm_instance_proposal",
                    extra={
                        "serviceName": "google.cloud.kms.v1.HsmManagement",
                        "rpcName": "CreateSingleTenantHsmInstanceProposal",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteSingleTenantHsmInstanceProposal(
        _BaseHsmManagementRestTransport._BaseDeleteSingleTenantHsmInstanceProposal,
        HsmManagementRestStub,
    ):
        def __hash__(self):
            return hash(
                "HsmManagementRestTransport.DeleteSingleTenantHsmInstanceProposal"
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
            request: hsm_management.DeleteSingleTenantHsmInstanceProposalRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete single tenant hsm
            instance proposal method over HTTP.

                Args:
                    request (~.hsm_management.DeleteSingleTenantHsmInstanceProposalRequest):
                        The request object. Request message for
                    [HsmManagement.DeleteSingleTenantHsmInstanceProposal][google.cloud.kms.v1.HsmManagement.DeleteSingleTenantHsmInstanceProposal].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.
            """

            http_options = _BaseHsmManagementRestTransport._BaseDeleteSingleTenantHsmInstanceProposal._get_http_options()
            request, metadata = (
                self._interceptor.pre_delete_single_tenant_hsm_instance_proposal(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHsmManagementRestTransport._BaseDeleteSingleTenantHsmInstanceProposal,
                    "_BaseDeleteSingleTenantHsmInstanceProposal__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.HsmManagementClient.DeleteSingleTenantHsmInstanceProposal",
                    extra={
                        "serviceName": "google.cloud.kms.v1.HsmManagement",
                        "rpcName": "DeleteSingleTenantHsmInstanceProposal",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = HsmManagementRestTransport._DeleteSingleTenantHsmInstanceProposal._get_response(
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

    class _ExecuteSingleTenantHsmInstanceProposal(
        _BaseHsmManagementRestTransport._BaseExecuteSingleTenantHsmInstanceProposal,
        HsmManagementRestStub,
    ):
        def __hash__(self):
            return hash(
                "HsmManagementRestTransport.ExecuteSingleTenantHsmInstanceProposal"
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
                data=body,
            )
            return response

        def __call__(
            self,
            request: hsm_management.ExecuteSingleTenantHsmInstanceProposalRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the execute single tenant hsm
            instance proposal method over HTTP.

                Args:
                    request (~.hsm_management.ExecuteSingleTenantHsmInstanceProposalRequest):
                        The request object. Request message for
                    [HsmManagement.ExecuteSingleTenantHsmInstanceProposal][google.cloud.kms.v1.HsmManagement.ExecuteSingleTenantHsmInstanceProposal].
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

            http_options = _BaseHsmManagementRestTransport._BaseExecuteSingleTenantHsmInstanceProposal._get_http_options()
            request, metadata = (
                self._interceptor.pre_execute_single_tenant_hsm_instance_proposal(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHsmManagementRestTransport._BaseExecuteSingleTenantHsmInstanceProposal,
                    "_BaseExecuteSingleTenantHsmInstanceProposal__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.HsmManagementClient.ExecuteSingleTenantHsmInstanceProposal",
                    extra={
                        "serviceName": "google.cloud.kms.v1.HsmManagement",
                        "rpcName": "ExecuteSingleTenantHsmInstanceProposal",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = HsmManagementRestTransport._ExecuteSingleTenantHsmInstanceProposal._get_response(
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

            resp = self._interceptor.post_execute_single_tenant_hsm_instance_proposal(
                resp
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_execute_single_tenant_hsm_instance_proposal_with_metadata(
                    resp, response_metadata
                )
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
                    "Received response for google.cloud.kms_v1.HsmManagementClient.execute_single_tenant_hsm_instance_proposal",
                    extra={
                        "serviceName": "google.cloud.kms.v1.HsmManagement",
                        "rpcName": "ExecuteSingleTenantHsmInstanceProposal",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetSingleTenantHsmInstance(
        _BaseHsmManagementRestTransport._BaseGetSingleTenantHsmInstance,
        HsmManagementRestStub,
    ):
        def __hash__(self):
            return hash("HsmManagementRestTransport.GetSingleTenantHsmInstance")

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
            request: hsm_management.GetSingleTenantHsmInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> hsm_management.SingleTenantHsmInstance:
            r"""Call the get single tenant hsm
            instance method over HTTP.

                Args:
                    request (~.hsm_management.GetSingleTenantHsmInstanceRequest):
                        The request object. Request message for
                    [HsmManagement.GetSingleTenantHsmInstance][google.cloud.kms.v1.HsmManagement.GetSingleTenantHsmInstance].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.hsm_management.SingleTenantHsmInstance:
                        A
                    [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]
                    represents a single-tenant HSM instance. It can be used
                    for creating [CryptoKeys][google.cloud.kms.v1.CryptoKey]
                    with a
                    [ProtectionLevel][google.cloud.kms.v1.ProtectionLevel]
                    of
                    [HSM_SINGLE_TENANT][CryptoKeyVersion.ProtectionLevel.HSM_SINGLE_TENANT],
                    as well as performing cryptographic operations using
                    keys created within the
                    [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance].

            """

            http_options = _BaseHsmManagementRestTransport._BaseGetSingleTenantHsmInstance._get_http_options()
            request, metadata = self._interceptor.pre_get_single_tenant_hsm_instance(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHsmManagementRestTransport._BaseGetSingleTenantHsmInstance,
                    "_BaseGetSingleTenantHsmInstance__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.HsmManagementClient.GetSingleTenantHsmInstance",
                    extra={
                        "serviceName": "google.cloud.kms.v1.HsmManagement",
                        "rpcName": "GetSingleTenantHsmInstance",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                HsmManagementRestTransport._GetSingleTenantHsmInstance._get_response(
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
            resp = hsm_management.SingleTenantHsmInstance()
            pb_resp = hsm_management.SingleTenantHsmInstance.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_single_tenant_hsm_instance(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_get_single_tenant_hsm_instance_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = hsm_management.SingleTenantHsmInstance.to_json(
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
                    "Received response for google.cloud.kms_v1.HsmManagementClient.get_single_tenant_hsm_instance",
                    extra={
                        "serviceName": "google.cloud.kms.v1.HsmManagement",
                        "rpcName": "GetSingleTenantHsmInstance",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetSingleTenantHsmInstanceProposal(
        _BaseHsmManagementRestTransport._BaseGetSingleTenantHsmInstanceProposal,
        HsmManagementRestStub,
    ):
        def __hash__(self):
            return hash("HsmManagementRestTransport.GetSingleTenantHsmInstanceProposal")

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
            request: hsm_management.GetSingleTenantHsmInstanceProposalRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> hsm_management.SingleTenantHsmInstanceProposal:
            r"""Call the get single tenant hsm
            instance proposal method over HTTP.

                Args:
                    request (~.hsm_management.GetSingleTenantHsmInstanceProposalRequest):
                        The request object. Request message for
                    [HsmManagement.GetSingleTenantHsmInstanceProposal][google.cloud.kms.v1.HsmManagement.GetSingleTenantHsmInstanceProposal].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.hsm_management.SingleTenantHsmInstanceProposal:
                        A
                    [SingleTenantHsmInstanceProposal][google.cloud.kms.v1.SingleTenantHsmInstanceProposal]
                    represents a proposal to perform an operation on a
                    [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance].

            """

            http_options = _BaseHsmManagementRestTransport._BaseGetSingleTenantHsmInstanceProposal._get_http_options()
            request, metadata = (
                self._interceptor.pre_get_single_tenant_hsm_instance_proposal(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHsmManagementRestTransport._BaseGetSingleTenantHsmInstanceProposal,
                    "_BaseGetSingleTenantHsmInstanceProposal__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.HsmManagementClient.GetSingleTenantHsmInstanceProposal",
                    extra={
                        "serviceName": "google.cloud.kms.v1.HsmManagement",
                        "rpcName": "GetSingleTenantHsmInstanceProposal",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = HsmManagementRestTransport._GetSingleTenantHsmInstanceProposal._get_response(
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
            resp = hsm_management.SingleTenantHsmInstanceProposal()
            pb_resp = hsm_management.SingleTenantHsmInstanceProposal.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_single_tenant_hsm_instance_proposal(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_get_single_tenant_hsm_instance_proposal_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        hsm_management.SingleTenantHsmInstanceProposal.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.kms_v1.HsmManagementClient.get_single_tenant_hsm_instance_proposal",
                    extra={
                        "serviceName": "google.cloud.kms.v1.HsmManagement",
                        "rpcName": "GetSingleTenantHsmInstanceProposal",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListSingleTenantHsmInstanceProposals(
        _BaseHsmManagementRestTransport._BaseListSingleTenantHsmInstanceProposals,
        HsmManagementRestStub,
    ):
        def __hash__(self):
            return hash(
                "HsmManagementRestTransport.ListSingleTenantHsmInstanceProposals"
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
            request: hsm_management.ListSingleTenantHsmInstanceProposalsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> hsm_management.ListSingleTenantHsmInstanceProposalsResponse:
            r"""Call the list single tenant hsm
            instance proposals method over HTTP.

                Args:
                    request (~.hsm_management.ListSingleTenantHsmInstanceProposalsRequest):
                        The request object. Request message for
                    [HsmManagement.ListSingleTenantHsmInstanceProposals][google.cloud.kms.v1.HsmManagement.ListSingleTenantHsmInstanceProposals].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.hsm_management.ListSingleTenantHsmInstanceProposalsResponse:
                        Response message for
                    [HsmManagement.ListSingleTenantHsmInstanceProposals][google.cloud.kms.v1.HsmManagement.ListSingleTenantHsmInstanceProposals].

            """

            http_options = _BaseHsmManagementRestTransport._BaseListSingleTenantHsmInstanceProposals._get_http_options()
            request, metadata = (
                self._interceptor.pre_list_single_tenant_hsm_instance_proposals(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHsmManagementRestTransport._BaseListSingleTenantHsmInstanceProposals,
                    "_BaseListSingleTenantHsmInstanceProposals__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.HsmManagementClient.ListSingleTenantHsmInstanceProposals",
                    extra={
                        "serviceName": "google.cloud.kms.v1.HsmManagement",
                        "rpcName": "ListSingleTenantHsmInstanceProposals",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = HsmManagementRestTransport._ListSingleTenantHsmInstanceProposals._get_response(
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
            resp = hsm_management.ListSingleTenantHsmInstanceProposalsResponse()
            pb_resp = hsm_management.ListSingleTenantHsmInstanceProposalsResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_single_tenant_hsm_instance_proposals(
                resp
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_single_tenant_hsm_instance_proposals_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = hsm_management.ListSingleTenantHsmInstanceProposalsResponse.to_json(
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
                    "Received response for google.cloud.kms_v1.HsmManagementClient.list_single_tenant_hsm_instance_proposals",
                    extra={
                        "serviceName": "google.cloud.kms.v1.HsmManagement",
                        "rpcName": "ListSingleTenantHsmInstanceProposals",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListSingleTenantHsmInstances(
        _BaseHsmManagementRestTransport._BaseListSingleTenantHsmInstances,
        HsmManagementRestStub,
    ):
        def __hash__(self):
            return hash("HsmManagementRestTransport.ListSingleTenantHsmInstances")

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
            request: hsm_management.ListSingleTenantHsmInstancesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> hsm_management.ListSingleTenantHsmInstancesResponse:
            r"""Call the list single tenant hsm
            instances method over HTTP.

                Args:
                    request (~.hsm_management.ListSingleTenantHsmInstancesRequest):
                        The request object. Request message for
                    [HsmManagement.ListSingleTenantHsmInstances][google.cloud.kms.v1.HsmManagement.ListSingleTenantHsmInstances].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.hsm_management.ListSingleTenantHsmInstancesResponse:
                        Response message for
                    [HsmManagement.ListSingleTenantHsmInstances][google.cloud.kms.v1.HsmManagement.ListSingleTenantHsmInstances].

            """

            http_options = _BaseHsmManagementRestTransport._BaseListSingleTenantHsmInstances._get_http_options()
            request, metadata = self._interceptor.pre_list_single_tenant_hsm_instances(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHsmManagementRestTransport._BaseListSingleTenantHsmInstances,
                    "_BaseListSingleTenantHsmInstances__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.HsmManagementClient.ListSingleTenantHsmInstances",
                    extra={
                        "serviceName": "google.cloud.kms.v1.HsmManagement",
                        "rpcName": "ListSingleTenantHsmInstances",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                HsmManagementRestTransport._ListSingleTenantHsmInstances._get_response(
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
            resp = hsm_management.ListSingleTenantHsmInstancesResponse()
            pb_resp = hsm_management.ListSingleTenantHsmInstancesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_single_tenant_hsm_instances(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_single_tenant_hsm_instances_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        hsm_management.ListSingleTenantHsmInstancesResponse.to_json(
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
                    "Received response for google.cloud.kms_v1.HsmManagementClient.list_single_tenant_hsm_instances",
                    extra={
                        "serviceName": "google.cloud.kms.v1.HsmManagement",
                        "rpcName": "ListSingleTenantHsmInstances",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def approve_single_tenant_hsm_instance_proposal(
        self,
    ) -> Callable[
        [hsm_management.ApproveSingleTenantHsmInstanceProposalRequest],
        hsm_management.ApproveSingleTenantHsmInstanceProposalResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ApproveSingleTenantHsmInstanceProposal(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_single_tenant_hsm_instance(
        self,
    ) -> Callable[
        [hsm_management.CreateSingleTenantHsmInstanceRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateSingleTenantHsmInstance(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_single_tenant_hsm_instance_proposal(
        self,
    ) -> Callable[
        [hsm_management.CreateSingleTenantHsmInstanceProposalRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateSingleTenantHsmInstanceProposal(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_single_tenant_hsm_instance_proposal(
        self,
    ) -> Callable[
        [hsm_management.DeleteSingleTenantHsmInstanceProposalRequest], empty_pb2.Empty
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteSingleTenantHsmInstanceProposal(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def execute_single_tenant_hsm_instance_proposal(
        self,
    ) -> Callable[
        [hsm_management.ExecuteSingleTenantHsmInstanceProposalRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExecuteSingleTenantHsmInstanceProposal(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_single_tenant_hsm_instance(
        self,
    ) -> Callable[
        [hsm_management.GetSingleTenantHsmInstanceRequest],
        hsm_management.SingleTenantHsmInstance,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSingleTenantHsmInstance(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_single_tenant_hsm_instance_proposal(
        self,
    ) -> Callable[
        [hsm_management.GetSingleTenantHsmInstanceProposalRequest],
        hsm_management.SingleTenantHsmInstanceProposal,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSingleTenantHsmInstanceProposal(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_single_tenant_hsm_instance_proposals(
        self,
    ) -> Callable[
        [hsm_management.ListSingleTenantHsmInstanceProposalsRequest],
        hsm_management.ListSingleTenantHsmInstanceProposalsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListSingleTenantHsmInstanceProposals(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_single_tenant_hsm_instances(
        self,
    ) -> Callable[
        [hsm_management.ListSingleTenantHsmInstancesRequest],
        hsm_management.ListSingleTenantHsmInstancesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListSingleTenantHsmInstances(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseHsmManagementRestTransport._BaseGetLocation, HsmManagementRestStub
    ):
        def __hash__(self):
            return hash("HsmManagementRestTransport.GetLocation")

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
                _BaseHsmManagementRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHsmManagementRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.kms_v1.HsmManagementClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.kms.v1.HsmManagement",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = HsmManagementRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.kms_v1.HsmManagementAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.kms.v1.HsmManagement",
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
        _BaseHsmManagementRestTransport._BaseListLocations, HsmManagementRestStub
    ):
        def __hash__(self):
            return hash("HsmManagementRestTransport.ListLocations")

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
                _BaseHsmManagementRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHsmManagementRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.kms_v1.HsmManagementClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.kms.v1.HsmManagement",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = HsmManagementRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.kms_v1.HsmManagementAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.kms.v1.HsmManagement",
                        "rpcName": "ListLocations",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def get_iam_policy(self):
        return self._GetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    class _GetIamPolicy(
        _BaseHsmManagementRestTransport._BaseGetIamPolicy, HsmManagementRestStub
    ):
        def __hash__(self):
            return hash("HsmManagementRestTransport.GetIamPolicy")

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
            request: iam_policy_pb2.GetIamPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> policy_pb2.Policy:
            r"""Call the get iam policy method over HTTP.

            Args:
                request (iam_policy_pb2.GetIamPolicyRequest):
                    The request object for GetIamPolicy method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                policy_pb2.Policy: Response from GetIamPolicy method.
            """

            http_options = (
                _BaseHsmManagementRestTransport._BaseGetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHsmManagementRestTransport._BaseGetIamPolicy,
                    "_BaseGetIamPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.HsmManagementClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.kms.v1.HsmManagement",
                        "rpcName": "GetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = HsmManagementRestTransport._GetIamPolicy._get_response(
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
            resp = policy_pb2.Policy()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_iam_policy(resp)
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
                    "Received response for google.cloud.kms_v1.HsmManagementAsyncClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.kms.v1.HsmManagement",
                        "rpcName": "GetIamPolicy",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def set_iam_policy(self):
        return self._SetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    class _SetIamPolicy(
        _BaseHsmManagementRestTransport._BaseSetIamPolicy, HsmManagementRestStub
    ):
        def __hash__(self):
            return hash("HsmManagementRestTransport.SetIamPolicy")

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
            request: iam_policy_pb2.SetIamPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> policy_pb2.Policy:
            r"""Call the set iam policy method over HTTP.

            Args:
                request (iam_policy_pb2.SetIamPolicyRequest):
                    The request object for SetIamPolicy method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                policy_pb2.Policy: Response from SetIamPolicy method.
            """

            http_options = (
                _BaseHsmManagementRestTransport._BaseSetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHsmManagementRestTransport._BaseSetIamPolicy,
                    "_BaseSetIamPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.HsmManagementClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.kms.v1.HsmManagement",
                        "rpcName": "SetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = HsmManagementRestTransport._SetIamPolicy._get_response(
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

            content = response.content.decode("utf-8")
            resp = policy_pb2.Policy()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_set_iam_policy(resp)
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
                    "Received response for google.cloud.kms_v1.HsmManagementAsyncClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.kms.v1.HsmManagement",
                        "rpcName": "SetIamPolicy",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def test_iam_permissions(self):
        return self._TestIamPermissions(self._session, self._host, self._interceptor)  # type: ignore

    class _TestIamPermissions(
        _BaseHsmManagementRestTransport._BaseTestIamPermissions, HsmManagementRestStub
    ):
        def __hash__(self):
            return hash("HsmManagementRestTransport.TestIamPermissions")

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
            request: iam_policy_pb2.TestIamPermissionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> iam_policy_pb2.TestIamPermissionsResponse:
            r"""Call the test iam permissions method over HTTP.

            Args:
                request (iam_policy_pb2.TestIamPermissionsRequest):
                    The request object for TestIamPermissions method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                iam_policy_pb2.TestIamPermissionsResponse: Response from TestIamPermissions method.
            """

            http_options = _BaseHsmManagementRestTransport._BaseTestIamPermissions._get_http_options()
            request, metadata = self._interceptor.pre_test_iam_permissions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHsmManagementRestTransport._BaseTestIamPermissions,
                    "_BaseTestIamPermissions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.HsmManagementClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.kms.v1.HsmManagement",
                        "rpcName": "TestIamPermissions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = HsmManagementRestTransport._TestIamPermissions._get_response(
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

            content = response.content.decode("utf-8")
            resp = iam_policy_pb2.TestIamPermissionsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_test_iam_permissions(resp)
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
                    "Received response for google.cloud.kms_v1.HsmManagementAsyncClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.kms.v1.HsmManagement",
                        "rpcName": "TestIamPermissions",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseHsmManagementRestTransport._BaseGetOperation, HsmManagementRestStub
    ):
        def __hash__(self):
            return hash("HsmManagementRestTransport.GetOperation")

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
                _BaseHsmManagementRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHsmManagementRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.kms_v1.HsmManagementClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.kms.v1.HsmManagement",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = HsmManagementRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.kms_v1.HsmManagementAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.kms.v1.HsmManagement",
                        "rpcName": "GetOperation",
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


__all__ = ("HsmManagementRestTransport",)
