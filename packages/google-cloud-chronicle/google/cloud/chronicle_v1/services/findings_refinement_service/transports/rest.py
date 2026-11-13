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
from google.api_core import gapic_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.chronicle_v1._compat import transcode_request
from google.cloud.chronicle_v1.types import findings_refinement
from google.cloud.chronicle_v1.types import (
    findings_refinement as gcc_findings_refinement,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseFindingsRefinementServiceRestTransport

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


class FindingsRefinementServiceRestInterceptor:
    """Interceptor for FindingsRefinementService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the FindingsRefinementServiceRestTransport.

    .. code-block:: python
        class MyCustomFindingsRefinementServiceInterceptor(FindingsRefinementServiceRestInterceptor):
            def pre_compute_all_findings_refinement_activities(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_compute_all_findings_refinement_activities(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_compute_findings_refinement_activity(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_compute_findings_refinement_activity(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_findings_refinement(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_findings_refinement(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_findings_refinement(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_findings_refinement(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_findings_refinement_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_findings_refinement_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_all_findings_refinement_deployments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_all_findings_refinement_deployments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_findings_refinements(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_findings_refinements(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_findings_refinement(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_findings_refinement(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_findings_refinement_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_findings_refinement_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = FindingsRefinementServiceRestTransport(interceptor=MyCustomFindingsRefinementServiceInterceptor())
        client = FindingsRefinementServiceClient(transport=transport)


    """

    def pre_compute_all_findings_refinement_activities(
        self,
        request: findings_refinement.ComputeAllFindingsRefinementActivitiesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        findings_refinement.ComputeAllFindingsRefinementActivitiesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for compute_all_findings_refinement_activities

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FindingsRefinementService server.
        """
        return request, metadata

    def post_compute_all_findings_refinement_activities(
        self,
        response: findings_refinement.ComputeAllFindingsRefinementActivitiesResponse,
    ) -> findings_refinement.ComputeAllFindingsRefinementActivitiesResponse:
        """Post-rpc interceptor for compute_all_findings_refinement_activities

        DEPRECATED. Please use the `post_compute_all_findings_refinement_activities_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the FindingsRefinementService server but before
        it is returned to user code. This `post_compute_all_findings_refinement_activities` interceptor runs
        before the `post_compute_all_findings_refinement_activities_with_metadata` interceptor.
        """
        return response

    def post_compute_all_findings_refinement_activities_with_metadata(
        self,
        response: findings_refinement.ComputeAllFindingsRefinementActivitiesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        findings_refinement.ComputeAllFindingsRefinementActivitiesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for compute_all_findings_refinement_activities

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the FindingsRefinementService server but before it is returned to user code.

        We recommend only using this `post_compute_all_findings_refinement_activities_with_metadata`
        interceptor in new development instead of the `post_compute_all_findings_refinement_activities` interceptor.
        When both interceptors are used, this `post_compute_all_findings_refinement_activities_with_metadata` interceptor runs after the
        `post_compute_all_findings_refinement_activities` interceptor. The (possibly modified) response returned by
        `post_compute_all_findings_refinement_activities` will be passed to
        `post_compute_all_findings_refinement_activities_with_metadata`.
        """
        return response, metadata

    def pre_compute_findings_refinement_activity(
        self,
        request: findings_refinement.ComputeFindingsRefinementActivityRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        findings_refinement.ComputeFindingsRefinementActivityRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for compute_findings_refinement_activity

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FindingsRefinementService server.
        """
        return request, metadata

    def post_compute_findings_refinement_activity(
        self, response: findings_refinement.ComputeFindingsRefinementActivityResponse
    ) -> findings_refinement.ComputeFindingsRefinementActivityResponse:
        """Post-rpc interceptor for compute_findings_refinement_activity

        DEPRECATED. Please use the `post_compute_findings_refinement_activity_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the FindingsRefinementService server but before
        it is returned to user code. This `post_compute_findings_refinement_activity` interceptor runs
        before the `post_compute_findings_refinement_activity_with_metadata` interceptor.
        """
        return response

    def post_compute_findings_refinement_activity_with_metadata(
        self,
        response: findings_refinement.ComputeFindingsRefinementActivityResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        findings_refinement.ComputeFindingsRefinementActivityResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for compute_findings_refinement_activity

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the FindingsRefinementService server but before it is returned to user code.

        We recommend only using this `post_compute_findings_refinement_activity_with_metadata`
        interceptor in new development instead of the `post_compute_findings_refinement_activity` interceptor.
        When both interceptors are used, this `post_compute_findings_refinement_activity_with_metadata` interceptor runs after the
        `post_compute_findings_refinement_activity` interceptor. The (possibly modified) response returned by
        `post_compute_findings_refinement_activity` will be passed to
        `post_compute_findings_refinement_activity_with_metadata`.
        """
        return response, metadata

    def pre_create_findings_refinement(
        self,
        request: gcc_findings_refinement.CreateFindingsRefinementRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcc_findings_refinement.CreateFindingsRefinementRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_findings_refinement

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FindingsRefinementService server.
        """
        return request, metadata

    def post_create_findings_refinement(
        self, response: gcc_findings_refinement.FindingsRefinement
    ) -> gcc_findings_refinement.FindingsRefinement:
        """Post-rpc interceptor for create_findings_refinement

        DEPRECATED. Please use the `post_create_findings_refinement_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the FindingsRefinementService server but before
        it is returned to user code. This `post_create_findings_refinement` interceptor runs
        before the `post_create_findings_refinement_with_metadata` interceptor.
        """
        return response

    def post_create_findings_refinement_with_metadata(
        self,
        response: gcc_findings_refinement.FindingsRefinement,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcc_findings_refinement.FindingsRefinement,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for create_findings_refinement

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the FindingsRefinementService server but before it is returned to user code.

        We recommend only using this `post_create_findings_refinement_with_metadata`
        interceptor in new development instead of the `post_create_findings_refinement` interceptor.
        When both interceptors are used, this `post_create_findings_refinement_with_metadata` interceptor runs after the
        `post_create_findings_refinement` interceptor. The (possibly modified) response returned by
        `post_create_findings_refinement` will be passed to
        `post_create_findings_refinement_with_metadata`.
        """
        return response, metadata

    def pre_get_findings_refinement(
        self,
        request: findings_refinement.GetFindingsRefinementRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        findings_refinement.GetFindingsRefinementRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_findings_refinement

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FindingsRefinementService server.
        """
        return request, metadata

    def post_get_findings_refinement(
        self, response: findings_refinement.FindingsRefinement
    ) -> findings_refinement.FindingsRefinement:
        """Post-rpc interceptor for get_findings_refinement

        DEPRECATED. Please use the `post_get_findings_refinement_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the FindingsRefinementService server but before
        it is returned to user code. This `post_get_findings_refinement` interceptor runs
        before the `post_get_findings_refinement_with_metadata` interceptor.
        """
        return response

    def post_get_findings_refinement_with_metadata(
        self,
        response: findings_refinement.FindingsRefinement,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        findings_refinement.FindingsRefinement, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_findings_refinement

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the FindingsRefinementService server but before it is returned to user code.

        We recommend only using this `post_get_findings_refinement_with_metadata`
        interceptor in new development instead of the `post_get_findings_refinement` interceptor.
        When both interceptors are used, this `post_get_findings_refinement_with_metadata` interceptor runs after the
        `post_get_findings_refinement` interceptor. The (possibly modified) response returned by
        `post_get_findings_refinement` will be passed to
        `post_get_findings_refinement_with_metadata`.
        """
        return response, metadata

    def pre_get_findings_refinement_deployment(
        self,
        request: findings_refinement.GetFindingsRefinementDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        findings_refinement.GetFindingsRefinementDeploymentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_findings_refinement_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FindingsRefinementService server.
        """
        return request, metadata

    def post_get_findings_refinement_deployment(
        self, response: findings_refinement.FindingsRefinementDeployment
    ) -> findings_refinement.FindingsRefinementDeployment:
        """Post-rpc interceptor for get_findings_refinement_deployment

        DEPRECATED. Please use the `post_get_findings_refinement_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the FindingsRefinementService server but before
        it is returned to user code. This `post_get_findings_refinement_deployment` interceptor runs
        before the `post_get_findings_refinement_deployment_with_metadata` interceptor.
        """
        return response

    def post_get_findings_refinement_deployment_with_metadata(
        self,
        response: findings_refinement.FindingsRefinementDeployment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        findings_refinement.FindingsRefinementDeployment,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_findings_refinement_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the FindingsRefinementService server but before it is returned to user code.

        We recommend only using this `post_get_findings_refinement_deployment_with_metadata`
        interceptor in new development instead of the `post_get_findings_refinement_deployment` interceptor.
        When both interceptors are used, this `post_get_findings_refinement_deployment_with_metadata` interceptor runs after the
        `post_get_findings_refinement_deployment` interceptor. The (possibly modified) response returned by
        `post_get_findings_refinement_deployment` will be passed to
        `post_get_findings_refinement_deployment_with_metadata`.
        """
        return response, metadata

    def pre_list_all_findings_refinement_deployments(
        self,
        request: findings_refinement.ListAllFindingsRefinementDeploymentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        findings_refinement.ListAllFindingsRefinementDeploymentsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_all_findings_refinement_deployments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FindingsRefinementService server.
        """
        return request, metadata

    def post_list_all_findings_refinement_deployments(
        self, response: findings_refinement.ListAllFindingsRefinementDeploymentsResponse
    ) -> findings_refinement.ListAllFindingsRefinementDeploymentsResponse:
        """Post-rpc interceptor for list_all_findings_refinement_deployments

        DEPRECATED. Please use the `post_list_all_findings_refinement_deployments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the FindingsRefinementService server but before
        it is returned to user code. This `post_list_all_findings_refinement_deployments` interceptor runs
        before the `post_list_all_findings_refinement_deployments_with_metadata` interceptor.
        """
        return response

    def post_list_all_findings_refinement_deployments_with_metadata(
        self,
        response: findings_refinement.ListAllFindingsRefinementDeploymentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        findings_refinement.ListAllFindingsRefinementDeploymentsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_all_findings_refinement_deployments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the FindingsRefinementService server but before it is returned to user code.

        We recommend only using this `post_list_all_findings_refinement_deployments_with_metadata`
        interceptor in new development instead of the `post_list_all_findings_refinement_deployments` interceptor.
        When both interceptors are used, this `post_list_all_findings_refinement_deployments_with_metadata` interceptor runs after the
        `post_list_all_findings_refinement_deployments` interceptor. The (possibly modified) response returned by
        `post_list_all_findings_refinement_deployments` will be passed to
        `post_list_all_findings_refinement_deployments_with_metadata`.
        """
        return response, metadata

    def pre_list_findings_refinements(
        self,
        request: findings_refinement.ListFindingsRefinementsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        findings_refinement.ListFindingsRefinementsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_findings_refinements

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FindingsRefinementService server.
        """
        return request, metadata

    def post_list_findings_refinements(
        self, response: findings_refinement.ListFindingsRefinementsResponse
    ) -> findings_refinement.ListFindingsRefinementsResponse:
        """Post-rpc interceptor for list_findings_refinements

        DEPRECATED. Please use the `post_list_findings_refinements_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the FindingsRefinementService server but before
        it is returned to user code. This `post_list_findings_refinements` interceptor runs
        before the `post_list_findings_refinements_with_metadata` interceptor.
        """
        return response

    def post_list_findings_refinements_with_metadata(
        self,
        response: findings_refinement.ListFindingsRefinementsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        findings_refinement.ListFindingsRefinementsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_findings_refinements

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the FindingsRefinementService server but before it is returned to user code.

        We recommend only using this `post_list_findings_refinements_with_metadata`
        interceptor in new development instead of the `post_list_findings_refinements` interceptor.
        When both interceptors are used, this `post_list_findings_refinements_with_metadata` interceptor runs after the
        `post_list_findings_refinements` interceptor. The (possibly modified) response returned by
        `post_list_findings_refinements` will be passed to
        `post_list_findings_refinements_with_metadata`.
        """
        return response, metadata

    def pre_update_findings_refinement(
        self,
        request: gcc_findings_refinement.UpdateFindingsRefinementRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcc_findings_refinement.UpdateFindingsRefinementRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_findings_refinement

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FindingsRefinementService server.
        """
        return request, metadata

    def post_update_findings_refinement(
        self, response: gcc_findings_refinement.FindingsRefinement
    ) -> gcc_findings_refinement.FindingsRefinement:
        """Post-rpc interceptor for update_findings_refinement

        DEPRECATED. Please use the `post_update_findings_refinement_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the FindingsRefinementService server but before
        it is returned to user code. This `post_update_findings_refinement` interceptor runs
        before the `post_update_findings_refinement_with_metadata` interceptor.
        """
        return response

    def post_update_findings_refinement_with_metadata(
        self,
        response: gcc_findings_refinement.FindingsRefinement,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcc_findings_refinement.FindingsRefinement,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for update_findings_refinement

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the FindingsRefinementService server but before it is returned to user code.

        We recommend only using this `post_update_findings_refinement_with_metadata`
        interceptor in new development instead of the `post_update_findings_refinement` interceptor.
        When both interceptors are used, this `post_update_findings_refinement_with_metadata` interceptor runs after the
        `post_update_findings_refinement` interceptor. The (possibly modified) response returned by
        `post_update_findings_refinement` will be passed to
        `post_update_findings_refinement_with_metadata`.
        """
        return response, metadata

    def pre_update_findings_refinement_deployment(
        self,
        request: findings_refinement.UpdateFindingsRefinementDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        findings_refinement.UpdateFindingsRefinementDeploymentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_findings_refinement_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FindingsRefinementService server.
        """
        return request, metadata

    def post_update_findings_refinement_deployment(
        self, response: findings_refinement.FindingsRefinementDeployment
    ) -> findings_refinement.FindingsRefinementDeployment:
        """Post-rpc interceptor for update_findings_refinement_deployment

        DEPRECATED. Please use the `post_update_findings_refinement_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the FindingsRefinementService server but before
        it is returned to user code. This `post_update_findings_refinement_deployment` interceptor runs
        before the `post_update_findings_refinement_deployment_with_metadata` interceptor.
        """
        return response

    def post_update_findings_refinement_deployment_with_metadata(
        self,
        response: findings_refinement.FindingsRefinementDeployment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        findings_refinement.FindingsRefinementDeployment,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for update_findings_refinement_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the FindingsRefinementService server but before it is returned to user code.

        We recommend only using this `post_update_findings_refinement_deployment_with_metadata`
        interceptor in new development instead of the `post_update_findings_refinement_deployment` interceptor.
        When both interceptors are used, this `post_update_findings_refinement_deployment_with_metadata` interceptor runs after the
        `post_update_findings_refinement_deployment` interceptor. The (possibly modified) response returned by
        `post_update_findings_refinement_deployment` will be passed to
        `post_update_findings_refinement_deployment_with_metadata`.
        """
        return response, metadata

    def pre_cancel_operation(
        self,
        request: operations_pb2.CancelOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.CancelOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FindingsRefinementService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the FindingsRefinementService server but before
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
        before they are sent to the FindingsRefinementService server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the FindingsRefinementService server but before
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
        before they are sent to the FindingsRefinementService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the FindingsRefinementService server but before
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
        before they are sent to the FindingsRefinementService server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the FindingsRefinementService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class FindingsRefinementServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: FindingsRefinementServiceRestInterceptor


class FindingsRefinementServiceRestTransport(
    _BaseFindingsRefinementServiceRestTransport
):
    """REST backend synchronous transport for FindingsRefinementService.

    FindingsRefinementService provides an interface for filtering
    out findings that are unlikely to be real threats to prevent
    them from triggering alerts or notifications.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "chronicle.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[FindingsRefinementServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'chronicle.googleapis.com').
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
            interceptor (Optional[FindingsRefinementServiceRestInterceptor]): Interceptor used
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
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or FindingsRefinementServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _ComputeAllFindingsRefinementActivities(
        _BaseFindingsRefinementServiceRestTransport._BaseComputeAllFindingsRefinementActivities,
        FindingsRefinementServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "FindingsRefinementServiceRestTransport.ComputeAllFindingsRefinementActivities"
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
            request: findings_refinement.ComputeAllFindingsRefinementActivitiesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> findings_refinement.ComputeAllFindingsRefinementActivitiesResponse:
            r"""Call the compute all findings
            refinement activities method over HTTP.

                Args:
                    request (~.findings_refinement.ComputeAllFindingsRefinementActivitiesRequest):
                        The request object. Request message for
                    ComputeAllFindingsRefinementActivities
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.findings_refinement.ComputeAllFindingsRefinementActivitiesResponse:
                        Response message for
                    ComputeAllFindingsRefinementActivities
                    method.

            """

            http_options = _BaseFindingsRefinementServiceRestTransport._BaseComputeAllFindingsRefinementActivities._get_http_options()
            request, metadata = (
                self._interceptor.pre_compute_all_findings_refinement_activities(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFindingsRefinementServiceRestTransport._BaseComputeAllFindingsRefinementActivities,
                    "_BaseComputeAllFindingsRefinementActivities__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.FindingsRefinementServiceClient.ComputeAllFindingsRefinementActivities",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FindingsRefinementService",
                        "rpcName": "ComputeAllFindingsRefinementActivities",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FindingsRefinementServiceRestTransport._ComputeAllFindingsRefinementActivities._get_response(
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
            resp = findings_refinement.ComputeAllFindingsRefinementActivitiesResponse()
            pb_resp = (
                findings_refinement.ComputeAllFindingsRefinementActivitiesResponse.pb(
                    resp
                )
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_compute_all_findings_refinement_activities(
                resp
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_compute_all_findings_refinement_activities_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = findings_refinement.ComputeAllFindingsRefinementActivitiesResponse.to_json(
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
                    "Received response for google.cloud.chronicle_v1.FindingsRefinementServiceClient.compute_all_findings_refinement_activities",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FindingsRefinementService",
                        "rpcName": "ComputeAllFindingsRefinementActivities",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ComputeFindingsRefinementActivity(
        _BaseFindingsRefinementServiceRestTransport._BaseComputeFindingsRefinementActivity,
        FindingsRefinementServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "FindingsRefinementServiceRestTransport.ComputeFindingsRefinementActivity"
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
            request: findings_refinement.ComputeFindingsRefinementActivityRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> findings_refinement.ComputeFindingsRefinementActivityResponse:
            r"""Call the compute findings
            refinement activity method over HTTP.

                Args:
                    request (~.findings_refinement.ComputeFindingsRefinementActivityRequest):
                        The request object. Request message for
                    ComputeFindingsRefinementActivity
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.findings_refinement.ComputeFindingsRefinementActivityResponse:
                        Response message for
                    ComputeFindingsRefinementActivity
                    method.

            """

            http_options = _BaseFindingsRefinementServiceRestTransport._BaseComputeFindingsRefinementActivity._get_http_options()
            request, metadata = (
                self._interceptor.pre_compute_findings_refinement_activity(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFindingsRefinementServiceRestTransport._BaseComputeFindingsRefinementActivity,
                    "_BaseComputeFindingsRefinementActivity__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.FindingsRefinementServiceClient.ComputeFindingsRefinementActivity",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FindingsRefinementService",
                        "rpcName": "ComputeFindingsRefinementActivity",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FindingsRefinementServiceRestTransport._ComputeFindingsRefinementActivity._get_response(
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
            resp = findings_refinement.ComputeFindingsRefinementActivityResponse()
            pb_resp = findings_refinement.ComputeFindingsRefinementActivityResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_compute_findings_refinement_activity(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_compute_findings_refinement_activity_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = findings_refinement.ComputeFindingsRefinementActivityResponse.to_json(
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
                    "Received response for google.cloud.chronicle_v1.FindingsRefinementServiceClient.compute_findings_refinement_activity",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FindingsRefinementService",
                        "rpcName": "ComputeFindingsRefinementActivity",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateFindingsRefinement(
        _BaseFindingsRefinementServiceRestTransport._BaseCreateFindingsRefinement,
        FindingsRefinementServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "FindingsRefinementServiceRestTransport.CreateFindingsRefinement"
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
            request: gcc_findings_refinement.CreateFindingsRefinementRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcc_findings_refinement.FindingsRefinement:
            r"""Call the create findings
            refinement method over HTTP.

                Args:
                    request (~.gcc_findings_refinement.CreateFindingsRefinementRequest):
                        The request object. Request message for
                    CreateFindingsRefinement method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.gcc_findings_refinement.FindingsRefinement:
                        Represents a set of logic conditions
                    used to refine various types of findings
                    such as curated rule detections.

            """

            http_options = _BaseFindingsRefinementServiceRestTransport._BaseCreateFindingsRefinement._get_http_options()
            request, metadata = self._interceptor.pre_create_findings_refinement(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFindingsRefinementServiceRestTransport._BaseCreateFindingsRefinement,
                    "_BaseCreateFindingsRefinement__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.FindingsRefinementServiceClient.CreateFindingsRefinement",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FindingsRefinementService",
                        "rpcName": "CreateFindingsRefinement",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FindingsRefinementServiceRestTransport._CreateFindingsRefinement._get_response(
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
            resp = gcc_findings_refinement.FindingsRefinement()
            pb_resp = gcc_findings_refinement.FindingsRefinement.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_findings_refinement(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_findings_refinement_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        gcc_findings_refinement.FindingsRefinement.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.chronicle_v1.FindingsRefinementServiceClient.create_findings_refinement",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FindingsRefinementService",
                        "rpcName": "CreateFindingsRefinement",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetFindingsRefinement(
        _BaseFindingsRefinementServiceRestTransport._BaseGetFindingsRefinement,
        FindingsRefinementServiceRestStub,
    ):
        def __hash__(self):
            return hash("FindingsRefinementServiceRestTransport.GetFindingsRefinement")

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
            request: findings_refinement.GetFindingsRefinementRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> findings_refinement.FindingsRefinement:
            r"""Call the get findings refinement method over HTTP.

            Args:
                request (~.findings_refinement.GetFindingsRefinementRequest):
                    The request object. Request message for
                GetFindingsRefinement method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.findings_refinement.FindingsRefinement:
                    Represents a set of logic conditions
                used to refine various types of findings
                such as curated rule detections.

            """

            http_options = _BaseFindingsRefinementServiceRestTransport._BaseGetFindingsRefinement._get_http_options()
            request, metadata = self._interceptor.pre_get_findings_refinement(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFindingsRefinementServiceRestTransport._BaseGetFindingsRefinement,
                    "_BaseGetFindingsRefinement__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.FindingsRefinementServiceClient.GetFindingsRefinement",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FindingsRefinementService",
                        "rpcName": "GetFindingsRefinement",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FindingsRefinementServiceRestTransport._GetFindingsRefinement._get_response(
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
            resp = findings_refinement.FindingsRefinement()
            pb_resp = findings_refinement.FindingsRefinement.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_findings_refinement(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_findings_refinement_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = findings_refinement.FindingsRefinement.to_json(
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
                    "Received response for google.cloud.chronicle_v1.FindingsRefinementServiceClient.get_findings_refinement",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FindingsRefinementService",
                        "rpcName": "GetFindingsRefinement",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetFindingsRefinementDeployment(
        _BaseFindingsRefinementServiceRestTransport._BaseGetFindingsRefinementDeployment,
        FindingsRefinementServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "FindingsRefinementServiceRestTransport.GetFindingsRefinementDeployment"
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
            request: findings_refinement.GetFindingsRefinementDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> findings_refinement.FindingsRefinementDeployment:
            r"""Call the get findings refinement
            deployment method over HTTP.

                Args:
                    request (~.findings_refinement.GetFindingsRefinementDeploymentRequest):
                        The request object. Request message for
                    GetFindingsRefinementDeployment method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.findings_refinement.FindingsRefinementDeployment:
                        The FindingsRefinementDeployment
                    resource represents the deployment state
                    of a findings refinement.

            """

            http_options = _BaseFindingsRefinementServiceRestTransport._BaseGetFindingsRefinementDeployment._get_http_options()
            request, metadata = (
                self._interceptor.pre_get_findings_refinement_deployment(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFindingsRefinementServiceRestTransport._BaseGetFindingsRefinementDeployment,
                    "_BaseGetFindingsRefinementDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.FindingsRefinementServiceClient.GetFindingsRefinementDeployment",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FindingsRefinementService",
                        "rpcName": "GetFindingsRefinementDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FindingsRefinementServiceRestTransport._GetFindingsRefinementDeployment._get_response(
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
            resp = findings_refinement.FindingsRefinementDeployment()
            pb_resp = findings_refinement.FindingsRefinementDeployment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_findings_refinement_deployment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_get_findings_refinement_deployment_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        findings_refinement.FindingsRefinementDeployment.to_json(
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
                    "Received response for google.cloud.chronicle_v1.FindingsRefinementServiceClient.get_findings_refinement_deployment",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FindingsRefinementService",
                        "rpcName": "GetFindingsRefinementDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAllFindingsRefinementDeployments(
        _BaseFindingsRefinementServiceRestTransport._BaseListAllFindingsRefinementDeployments,
        FindingsRefinementServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "FindingsRefinementServiceRestTransport.ListAllFindingsRefinementDeployments"
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
            request: findings_refinement.ListAllFindingsRefinementDeploymentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> findings_refinement.ListAllFindingsRefinementDeploymentsResponse:
            r"""Call the list all findings
            refinement deployments method over HTTP.

                Args:
                    request (~.findings_refinement.ListAllFindingsRefinementDeploymentsRequest):
                        The request object. Request message for
                    ListAllFindingsRefinementDeployments
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.findings_refinement.ListAllFindingsRefinementDeploymentsResponse:
                        Response message for
                    ListAllFindingsRefinementDeployments
                    method.

            """

            http_options = _BaseFindingsRefinementServiceRestTransport._BaseListAllFindingsRefinementDeployments._get_http_options()
            request, metadata = (
                self._interceptor.pre_list_all_findings_refinement_deployments(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFindingsRefinementServiceRestTransport._BaseListAllFindingsRefinementDeployments,
                    "_BaseListAllFindingsRefinementDeployments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.FindingsRefinementServiceClient.ListAllFindingsRefinementDeployments",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FindingsRefinementService",
                        "rpcName": "ListAllFindingsRefinementDeployments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FindingsRefinementServiceRestTransport._ListAllFindingsRefinementDeployments._get_response(
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
            resp = findings_refinement.ListAllFindingsRefinementDeploymentsResponse()
            pb_resp = (
                findings_refinement.ListAllFindingsRefinementDeploymentsResponse.pb(
                    resp
                )
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_all_findings_refinement_deployments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_all_findings_refinement_deployments_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = findings_refinement.ListAllFindingsRefinementDeploymentsResponse.to_json(
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
                    "Received response for google.cloud.chronicle_v1.FindingsRefinementServiceClient.list_all_findings_refinement_deployments",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FindingsRefinementService",
                        "rpcName": "ListAllFindingsRefinementDeployments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListFindingsRefinements(
        _BaseFindingsRefinementServiceRestTransport._BaseListFindingsRefinements,
        FindingsRefinementServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "FindingsRefinementServiceRestTransport.ListFindingsRefinements"
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
            request: findings_refinement.ListFindingsRefinementsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> findings_refinement.ListFindingsRefinementsResponse:
            r"""Call the list findings refinements method over HTTP.

            Args:
                request (~.findings_refinement.ListFindingsRefinementsRequest):
                    The request object. Request message for
                ListFindingsRefinements method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.findings_refinement.ListFindingsRefinementsResponse:
                    Response message for
                ListFindingsRefinements method.

            """

            http_options = _BaseFindingsRefinementServiceRestTransport._BaseListFindingsRefinements._get_http_options()
            request, metadata = self._interceptor.pre_list_findings_refinements(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFindingsRefinementServiceRestTransport._BaseListFindingsRefinements,
                    "_BaseListFindingsRefinements__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.FindingsRefinementServiceClient.ListFindingsRefinements",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FindingsRefinementService",
                        "rpcName": "ListFindingsRefinements",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FindingsRefinementServiceRestTransport._ListFindingsRefinements._get_response(
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
            resp = findings_refinement.ListFindingsRefinementsResponse()
            pb_resp = findings_refinement.ListFindingsRefinementsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_findings_refinements(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_findings_refinements_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        findings_refinement.ListFindingsRefinementsResponse.to_json(
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
                    "Received response for google.cloud.chronicle_v1.FindingsRefinementServiceClient.list_findings_refinements",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FindingsRefinementService",
                        "rpcName": "ListFindingsRefinements",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateFindingsRefinement(
        _BaseFindingsRefinementServiceRestTransport._BaseUpdateFindingsRefinement,
        FindingsRefinementServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "FindingsRefinementServiceRestTransport.UpdateFindingsRefinement"
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
            request: gcc_findings_refinement.UpdateFindingsRefinementRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcc_findings_refinement.FindingsRefinement:
            r"""Call the update findings
            refinement method over HTTP.

                Args:
                    request (~.gcc_findings_refinement.UpdateFindingsRefinementRequest):
                        The request object. Request message for
                    UpdateFindingsRefinement method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.gcc_findings_refinement.FindingsRefinement:
                        Represents a set of logic conditions
                    used to refine various types of findings
                    such as curated rule detections.

            """

            http_options = _BaseFindingsRefinementServiceRestTransport._BaseUpdateFindingsRefinement._get_http_options()
            request, metadata = self._interceptor.pre_update_findings_refinement(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFindingsRefinementServiceRestTransport._BaseUpdateFindingsRefinement,
                    "_BaseUpdateFindingsRefinement__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.FindingsRefinementServiceClient.UpdateFindingsRefinement",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FindingsRefinementService",
                        "rpcName": "UpdateFindingsRefinement",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FindingsRefinementServiceRestTransport._UpdateFindingsRefinement._get_response(
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
            resp = gcc_findings_refinement.FindingsRefinement()
            pb_resp = gcc_findings_refinement.FindingsRefinement.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_findings_refinement(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_findings_refinement_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        gcc_findings_refinement.FindingsRefinement.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.chronicle_v1.FindingsRefinementServiceClient.update_findings_refinement",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FindingsRefinementService",
                        "rpcName": "UpdateFindingsRefinement",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateFindingsRefinementDeployment(
        _BaseFindingsRefinementServiceRestTransport._BaseUpdateFindingsRefinementDeployment,
        FindingsRefinementServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "FindingsRefinementServiceRestTransport.UpdateFindingsRefinementDeployment"
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
            request: findings_refinement.UpdateFindingsRefinementDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> findings_refinement.FindingsRefinementDeployment:
            r"""Call the update findings
            refinement deployment method over HTTP.

                Args:
                    request (~.findings_refinement.UpdateFindingsRefinementDeploymentRequest):
                        The request object. Request message for
                    UpdateFindingsRefinementDeployment
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.findings_refinement.FindingsRefinementDeployment:
                        The FindingsRefinementDeployment
                    resource represents the deployment state
                    of a findings refinement.

            """

            http_options = _BaseFindingsRefinementServiceRestTransport._BaseUpdateFindingsRefinementDeployment._get_http_options()
            request, metadata = (
                self._interceptor.pre_update_findings_refinement_deployment(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFindingsRefinementServiceRestTransport._BaseUpdateFindingsRefinementDeployment,
                    "_BaseUpdateFindingsRefinementDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.FindingsRefinementServiceClient.UpdateFindingsRefinementDeployment",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FindingsRefinementService",
                        "rpcName": "UpdateFindingsRefinementDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FindingsRefinementServiceRestTransport._UpdateFindingsRefinementDeployment._get_response(
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
            resp = findings_refinement.FindingsRefinementDeployment()
            pb_resp = findings_refinement.FindingsRefinementDeployment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_findings_refinement_deployment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_update_findings_refinement_deployment_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        findings_refinement.FindingsRefinementDeployment.to_json(
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
                    "Received response for google.cloud.chronicle_v1.FindingsRefinementServiceClient.update_findings_refinement_deployment",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FindingsRefinementService",
                        "rpcName": "UpdateFindingsRefinementDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def compute_all_findings_refinement_activities(
        self,
    ) -> Callable[
        [findings_refinement.ComputeAllFindingsRefinementActivitiesRequest],
        findings_refinement.ComputeAllFindingsRefinementActivitiesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ComputeAllFindingsRefinementActivities(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def compute_findings_refinement_activity(
        self,
    ) -> Callable[
        [findings_refinement.ComputeFindingsRefinementActivityRequest],
        findings_refinement.ComputeFindingsRefinementActivityResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ComputeFindingsRefinementActivity(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_findings_refinement(
        self,
    ) -> Callable[
        [gcc_findings_refinement.CreateFindingsRefinementRequest],
        gcc_findings_refinement.FindingsRefinement,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateFindingsRefinement(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_findings_refinement(
        self,
    ) -> Callable[
        [findings_refinement.GetFindingsRefinementRequest],
        findings_refinement.FindingsRefinement,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetFindingsRefinement(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_findings_refinement_deployment(
        self,
    ) -> Callable[
        [findings_refinement.GetFindingsRefinementDeploymentRequest],
        findings_refinement.FindingsRefinementDeployment,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetFindingsRefinementDeployment(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_all_findings_refinement_deployments(
        self,
    ) -> Callable[
        [findings_refinement.ListAllFindingsRefinementDeploymentsRequest],
        findings_refinement.ListAllFindingsRefinementDeploymentsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAllFindingsRefinementDeployments(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_findings_refinements(
        self,
    ) -> Callable[
        [findings_refinement.ListFindingsRefinementsRequest],
        findings_refinement.ListFindingsRefinementsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListFindingsRefinements(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_findings_refinement(
        self,
    ) -> Callable[
        [gcc_findings_refinement.UpdateFindingsRefinementRequest],
        gcc_findings_refinement.FindingsRefinement,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateFindingsRefinement(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_findings_refinement_deployment(
        self,
    ) -> Callable[
        [findings_refinement.UpdateFindingsRefinementDeploymentRequest],
        findings_refinement.FindingsRefinementDeployment,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateFindingsRefinementDeployment(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseFindingsRefinementServiceRestTransport._BaseCancelOperation,
        FindingsRefinementServiceRestStub,
    ):
        def __hash__(self):
            return hash("FindingsRefinementServiceRestTransport.CancelOperation")

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

            http_options = _BaseFindingsRefinementServiceRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFindingsRefinementServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.chronicle_v1.FindingsRefinementServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FindingsRefinementService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                FindingsRefinementServiceRestTransport._CancelOperation._get_response(
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

            return self._interceptor.post_cancel_operation(None)

    @property
    def delete_operation(self):
        return self._DeleteOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _DeleteOperation(
        _BaseFindingsRefinementServiceRestTransport._BaseDeleteOperation,
        FindingsRefinementServiceRestStub,
    ):
        def __hash__(self):
            return hash("FindingsRefinementServiceRestTransport.DeleteOperation")

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

            http_options = _BaseFindingsRefinementServiceRestTransport._BaseDeleteOperation._get_http_options()
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFindingsRefinementServiceRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.chronicle_v1.FindingsRefinementServiceClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FindingsRefinementService",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                FindingsRefinementServiceRestTransport._DeleteOperation._get_response(
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

            return self._interceptor.post_delete_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseFindingsRefinementServiceRestTransport._BaseGetOperation,
        FindingsRefinementServiceRestStub,
    ):
        def __hash__(self):
            return hash("FindingsRefinementServiceRestTransport.GetOperation")

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

            http_options = _BaseFindingsRefinementServiceRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFindingsRefinementServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.chronicle_v1.FindingsRefinementServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FindingsRefinementService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                FindingsRefinementServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.chronicle_v1.FindingsRefinementServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FindingsRefinementService",
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
        _BaseFindingsRefinementServiceRestTransport._BaseListOperations,
        FindingsRefinementServiceRestStub,
    ):
        def __hash__(self):
            return hash("FindingsRefinementServiceRestTransport.ListOperations")

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

            http_options = _BaseFindingsRefinementServiceRestTransport._BaseListOperations._get_http_options()
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFindingsRefinementServiceRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.chronicle_v1.FindingsRefinementServiceClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FindingsRefinementService",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                FindingsRefinementServiceRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.chronicle_v1.FindingsRefinementServiceAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FindingsRefinementService",
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


__all__ = ("FindingsRefinementServiceRestTransport",)
