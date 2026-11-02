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
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.telcoautomation_v1._compat import transcode_request
from google.cloud.telcoautomation_v1.types import telcoautomation

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseTelcoAutomationRestTransport

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


class TelcoAutomationRestInterceptor:
    """Interceptor for TelcoAutomation.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the TelcoAutomationRestTransport.

    .. code-block:: python
        class MyCustomTelcoAutomationInterceptor(TelcoAutomationRestInterceptor):
            def pre_apply_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_apply_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_apply_hydrated_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_apply_hydrated_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_approve_blueprint(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_approve_blueprint(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_compute_deployment_status(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_compute_deployment_status(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_blueprint(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_blueprint(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_edge_slm(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_edge_slm(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_orchestration_cluster(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_orchestration_cluster(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_blueprint(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_edge_slm(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_edge_slm(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_orchestration_cluster(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_orchestration_cluster(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_discard_blueprint_changes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_discard_blueprint_changes(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_discard_deployment_changes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_discard_deployment_changes(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_blueprint(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_blueprint(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_edge_slm(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_edge_slm(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_hydrated_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_hydrated_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_orchestration_cluster(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_orchestration_cluster(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_public_blueprint(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_public_blueprint(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_blueprint_revisions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_blueprint_revisions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_blueprints(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_blueprints(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_deployment_revisions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_deployment_revisions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_deployments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_deployments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_edge_slms(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_edge_slms(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_hydrated_deployments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_hydrated_deployments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_orchestration_clusters(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_orchestration_clusters(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_public_blueprints(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_public_blueprints(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_propose_blueprint(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_propose_blueprint(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_reject_blueprint(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_reject_blueprint(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_remove_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_rollback_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_rollback_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_search_blueprint_revisions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_search_blueprint_revisions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_search_deployment_revisions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_search_deployment_revisions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_blueprint(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_blueprint(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_hydrated_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_hydrated_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = TelcoAutomationRestTransport(interceptor=MyCustomTelcoAutomationInterceptor())
        client = TelcoAutomationClient(transport=transport)


    """

    def pre_apply_deployment(
        self,
        request: telcoautomation.ApplyDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.ApplyDeploymentRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for apply_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TelcoAutomation server.
        """
        return request, metadata

    def post_apply_deployment(
        self, response: telcoautomation.Deployment
    ) -> telcoautomation.Deployment:
        """Post-rpc interceptor for apply_deployment

        DEPRECATED. Please use the `post_apply_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TelcoAutomation server but before
        it is returned to user code. This `post_apply_deployment` interceptor runs
        before the `post_apply_deployment_with_metadata` interceptor.
        """
        return response

    def post_apply_deployment_with_metadata(
        self,
        response: telcoautomation.Deployment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[telcoautomation.Deployment, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for apply_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TelcoAutomation server but before it is returned to user code.

        We recommend only using this `post_apply_deployment_with_metadata`
        interceptor in new development instead of the `post_apply_deployment` interceptor.
        When both interceptors are used, this `post_apply_deployment_with_metadata` interceptor runs after the
        `post_apply_deployment` interceptor. The (possibly modified) response returned by
        `post_apply_deployment` will be passed to
        `post_apply_deployment_with_metadata`.
        """
        return response, metadata

    def pre_apply_hydrated_deployment(
        self,
        request: telcoautomation.ApplyHydratedDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.ApplyHydratedDeploymentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for apply_hydrated_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TelcoAutomation server.
        """
        return request, metadata

    def post_apply_hydrated_deployment(
        self, response: telcoautomation.HydratedDeployment
    ) -> telcoautomation.HydratedDeployment:
        """Post-rpc interceptor for apply_hydrated_deployment

        DEPRECATED. Please use the `post_apply_hydrated_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TelcoAutomation server but before
        it is returned to user code. This `post_apply_hydrated_deployment` interceptor runs
        before the `post_apply_hydrated_deployment_with_metadata` interceptor.
        """
        return response

    def post_apply_hydrated_deployment_with_metadata(
        self,
        response: telcoautomation.HydratedDeployment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.HydratedDeployment, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for apply_hydrated_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TelcoAutomation server but before it is returned to user code.

        We recommend only using this `post_apply_hydrated_deployment_with_metadata`
        interceptor in new development instead of the `post_apply_hydrated_deployment` interceptor.
        When both interceptors are used, this `post_apply_hydrated_deployment_with_metadata` interceptor runs after the
        `post_apply_hydrated_deployment` interceptor. The (possibly modified) response returned by
        `post_apply_hydrated_deployment` will be passed to
        `post_apply_hydrated_deployment_with_metadata`.
        """
        return response, metadata

    def pre_approve_blueprint(
        self,
        request: telcoautomation.ApproveBlueprintRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.ApproveBlueprintRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for approve_blueprint

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TelcoAutomation server.
        """
        return request, metadata

    def post_approve_blueprint(
        self, response: telcoautomation.Blueprint
    ) -> telcoautomation.Blueprint:
        """Post-rpc interceptor for approve_blueprint

        DEPRECATED. Please use the `post_approve_blueprint_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TelcoAutomation server but before
        it is returned to user code. This `post_approve_blueprint` interceptor runs
        before the `post_approve_blueprint_with_metadata` interceptor.
        """
        return response

    def post_approve_blueprint_with_metadata(
        self,
        response: telcoautomation.Blueprint,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[telcoautomation.Blueprint, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for approve_blueprint

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TelcoAutomation server but before it is returned to user code.

        We recommend only using this `post_approve_blueprint_with_metadata`
        interceptor in new development instead of the `post_approve_blueprint` interceptor.
        When both interceptors are used, this `post_approve_blueprint_with_metadata` interceptor runs after the
        `post_approve_blueprint` interceptor. The (possibly modified) response returned by
        `post_approve_blueprint` will be passed to
        `post_approve_blueprint_with_metadata`.
        """
        return response, metadata

    def pre_compute_deployment_status(
        self,
        request: telcoautomation.ComputeDeploymentStatusRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.ComputeDeploymentStatusRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for compute_deployment_status

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TelcoAutomation server.
        """
        return request, metadata

    def post_compute_deployment_status(
        self, response: telcoautomation.ComputeDeploymentStatusResponse
    ) -> telcoautomation.ComputeDeploymentStatusResponse:
        """Post-rpc interceptor for compute_deployment_status

        DEPRECATED. Please use the `post_compute_deployment_status_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TelcoAutomation server but before
        it is returned to user code. This `post_compute_deployment_status` interceptor runs
        before the `post_compute_deployment_status_with_metadata` interceptor.
        """
        return response

    def post_compute_deployment_status_with_metadata(
        self,
        response: telcoautomation.ComputeDeploymentStatusResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.ComputeDeploymentStatusResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for compute_deployment_status

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TelcoAutomation server but before it is returned to user code.

        We recommend only using this `post_compute_deployment_status_with_metadata`
        interceptor in new development instead of the `post_compute_deployment_status` interceptor.
        When both interceptors are used, this `post_compute_deployment_status_with_metadata` interceptor runs after the
        `post_compute_deployment_status` interceptor. The (possibly modified) response returned by
        `post_compute_deployment_status` will be passed to
        `post_compute_deployment_status_with_metadata`.
        """
        return response, metadata

    def pre_create_blueprint(
        self,
        request: telcoautomation.CreateBlueprintRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.CreateBlueprintRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_blueprint

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TelcoAutomation server.
        """
        return request, metadata

    def post_create_blueprint(
        self, response: telcoautomation.Blueprint
    ) -> telcoautomation.Blueprint:
        """Post-rpc interceptor for create_blueprint

        DEPRECATED. Please use the `post_create_blueprint_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TelcoAutomation server but before
        it is returned to user code. This `post_create_blueprint` interceptor runs
        before the `post_create_blueprint_with_metadata` interceptor.
        """
        return response

    def post_create_blueprint_with_metadata(
        self,
        response: telcoautomation.Blueprint,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[telcoautomation.Blueprint, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_blueprint

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TelcoAutomation server but before it is returned to user code.

        We recommend only using this `post_create_blueprint_with_metadata`
        interceptor in new development instead of the `post_create_blueprint` interceptor.
        When both interceptors are used, this `post_create_blueprint_with_metadata` interceptor runs after the
        `post_create_blueprint` interceptor. The (possibly modified) response returned by
        `post_create_blueprint` will be passed to
        `post_create_blueprint_with_metadata`.
        """
        return response, metadata

    def pre_create_deployment(
        self,
        request: telcoautomation.CreateDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.CreateDeploymentRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TelcoAutomation server.
        """
        return request, metadata

    def post_create_deployment(
        self, response: telcoautomation.Deployment
    ) -> telcoautomation.Deployment:
        """Post-rpc interceptor for create_deployment

        DEPRECATED. Please use the `post_create_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TelcoAutomation server but before
        it is returned to user code. This `post_create_deployment` interceptor runs
        before the `post_create_deployment_with_metadata` interceptor.
        """
        return response

    def post_create_deployment_with_metadata(
        self,
        response: telcoautomation.Deployment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[telcoautomation.Deployment, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TelcoAutomation server but before it is returned to user code.

        We recommend only using this `post_create_deployment_with_metadata`
        interceptor in new development instead of the `post_create_deployment` interceptor.
        When both interceptors are used, this `post_create_deployment_with_metadata` interceptor runs after the
        `post_create_deployment` interceptor. The (possibly modified) response returned by
        `post_create_deployment` will be passed to
        `post_create_deployment_with_metadata`.
        """
        return response, metadata

    def pre_create_edge_slm(
        self,
        request: telcoautomation.CreateEdgeSlmRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.CreateEdgeSlmRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_edge_slm

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TelcoAutomation server.
        """
        return request, metadata

    def post_create_edge_slm(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_edge_slm

        DEPRECATED. Please use the `post_create_edge_slm_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TelcoAutomation server but before
        it is returned to user code. This `post_create_edge_slm` interceptor runs
        before the `post_create_edge_slm_with_metadata` interceptor.
        """
        return response

    def post_create_edge_slm_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_edge_slm

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TelcoAutomation server but before it is returned to user code.

        We recommend only using this `post_create_edge_slm_with_metadata`
        interceptor in new development instead of the `post_create_edge_slm` interceptor.
        When both interceptors are used, this `post_create_edge_slm_with_metadata` interceptor runs after the
        `post_create_edge_slm` interceptor. The (possibly modified) response returned by
        `post_create_edge_slm` will be passed to
        `post_create_edge_slm_with_metadata`.
        """
        return response, metadata

    def pre_create_orchestration_cluster(
        self,
        request: telcoautomation.CreateOrchestrationClusterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.CreateOrchestrationClusterRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_orchestration_cluster

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TelcoAutomation server.
        """
        return request, metadata

    def post_create_orchestration_cluster(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_orchestration_cluster

        DEPRECATED. Please use the `post_create_orchestration_cluster_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TelcoAutomation server but before
        it is returned to user code. This `post_create_orchestration_cluster` interceptor runs
        before the `post_create_orchestration_cluster_with_metadata` interceptor.
        """
        return response

    def post_create_orchestration_cluster_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_orchestration_cluster

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TelcoAutomation server but before it is returned to user code.

        We recommend only using this `post_create_orchestration_cluster_with_metadata`
        interceptor in new development instead of the `post_create_orchestration_cluster` interceptor.
        When both interceptors are used, this `post_create_orchestration_cluster_with_metadata` interceptor runs after the
        `post_create_orchestration_cluster` interceptor. The (possibly modified) response returned by
        `post_create_orchestration_cluster` will be passed to
        `post_create_orchestration_cluster_with_metadata`.
        """
        return response, metadata

    def pre_delete_blueprint(
        self,
        request: telcoautomation.DeleteBlueprintRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.DeleteBlueprintRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_blueprint

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TelcoAutomation server.
        """
        return request, metadata

    def pre_delete_edge_slm(
        self,
        request: telcoautomation.DeleteEdgeSlmRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.DeleteEdgeSlmRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_edge_slm

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TelcoAutomation server.
        """
        return request, metadata

    def post_delete_edge_slm(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_edge_slm

        DEPRECATED. Please use the `post_delete_edge_slm_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TelcoAutomation server but before
        it is returned to user code. This `post_delete_edge_slm` interceptor runs
        before the `post_delete_edge_slm_with_metadata` interceptor.
        """
        return response

    def post_delete_edge_slm_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_edge_slm

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TelcoAutomation server but before it is returned to user code.

        We recommend only using this `post_delete_edge_slm_with_metadata`
        interceptor in new development instead of the `post_delete_edge_slm` interceptor.
        When both interceptors are used, this `post_delete_edge_slm_with_metadata` interceptor runs after the
        `post_delete_edge_slm` interceptor. The (possibly modified) response returned by
        `post_delete_edge_slm` will be passed to
        `post_delete_edge_slm_with_metadata`.
        """
        return response, metadata

    def pre_delete_orchestration_cluster(
        self,
        request: telcoautomation.DeleteOrchestrationClusterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.DeleteOrchestrationClusterRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_orchestration_cluster

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TelcoAutomation server.
        """
        return request, metadata

    def post_delete_orchestration_cluster(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_orchestration_cluster

        DEPRECATED. Please use the `post_delete_orchestration_cluster_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TelcoAutomation server but before
        it is returned to user code. This `post_delete_orchestration_cluster` interceptor runs
        before the `post_delete_orchestration_cluster_with_metadata` interceptor.
        """
        return response

    def post_delete_orchestration_cluster_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_orchestration_cluster

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TelcoAutomation server but before it is returned to user code.

        We recommend only using this `post_delete_orchestration_cluster_with_metadata`
        interceptor in new development instead of the `post_delete_orchestration_cluster` interceptor.
        When both interceptors are used, this `post_delete_orchestration_cluster_with_metadata` interceptor runs after the
        `post_delete_orchestration_cluster` interceptor. The (possibly modified) response returned by
        `post_delete_orchestration_cluster` will be passed to
        `post_delete_orchestration_cluster_with_metadata`.
        """
        return response, metadata

    def pre_discard_blueprint_changes(
        self,
        request: telcoautomation.DiscardBlueprintChangesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.DiscardBlueprintChangesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for discard_blueprint_changes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TelcoAutomation server.
        """
        return request, metadata

    def post_discard_blueprint_changes(
        self, response: telcoautomation.DiscardBlueprintChangesResponse
    ) -> telcoautomation.DiscardBlueprintChangesResponse:
        """Post-rpc interceptor for discard_blueprint_changes

        DEPRECATED. Please use the `post_discard_blueprint_changes_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TelcoAutomation server but before
        it is returned to user code. This `post_discard_blueprint_changes` interceptor runs
        before the `post_discard_blueprint_changes_with_metadata` interceptor.
        """
        return response

    def post_discard_blueprint_changes_with_metadata(
        self,
        response: telcoautomation.DiscardBlueprintChangesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.DiscardBlueprintChangesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for discard_blueprint_changes

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TelcoAutomation server but before it is returned to user code.

        We recommend only using this `post_discard_blueprint_changes_with_metadata`
        interceptor in new development instead of the `post_discard_blueprint_changes` interceptor.
        When both interceptors are used, this `post_discard_blueprint_changes_with_metadata` interceptor runs after the
        `post_discard_blueprint_changes` interceptor. The (possibly modified) response returned by
        `post_discard_blueprint_changes` will be passed to
        `post_discard_blueprint_changes_with_metadata`.
        """
        return response, metadata

    def pre_discard_deployment_changes(
        self,
        request: telcoautomation.DiscardDeploymentChangesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.DiscardDeploymentChangesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for discard_deployment_changes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TelcoAutomation server.
        """
        return request, metadata

    def post_discard_deployment_changes(
        self, response: telcoautomation.DiscardDeploymentChangesResponse
    ) -> telcoautomation.DiscardDeploymentChangesResponse:
        """Post-rpc interceptor for discard_deployment_changes

        DEPRECATED. Please use the `post_discard_deployment_changes_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TelcoAutomation server but before
        it is returned to user code. This `post_discard_deployment_changes` interceptor runs
        before the `post_discard_deployment_changes_with_metadata` interceptor.
        """
        return response

    def post_discard_deployment_changes_with_metadata(
        self,
        response: telcoautomation.DiscardDeploymentChangesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.DiscardDeploymentChangesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for discard_deployment_changes

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TelcoAutomation server but before it is returned to user code.

        We recommend only using this `post_discard_deployment_changes_with_metadata`
        interceptor in new development instead of the `post_discard_deployment_changes` interceptor.
        When both interceptors are used, this `post_discard_deployment_changes_with_metadata` interceptor runs after the
        `post_discard_deployment_changes` interceptor. The (possibly modified) response returned by
        `post_discard_deployment_changes` will be passed to
        `post_discard_deployment_changes_with_metadata`.
        """
        return response, metadata

    def pre_get_blueprint(
        self,
        request: telcoautomation.GetBlueprintRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.GetBlueprintRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_blueprint

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TelcoAutomation server.
        """
        return request, metadata

    def post_get_blueprint(
        self, response: telcoautomation.Blueprint
    ) -> telcoautomation.Blueprint:
        """Post-rpc interceptor for get_blueprint

        DEPRECATED. Please use the `post_get_blueprint_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TelcoAutomation server but before
        it is returned to user code. This `post_get_blueprint` interceptor runs
        before the `post_get_blueprint_with_metadata` interceptor.
        """
        return response

    def post_get_blueprint_with_metadata(
        self,
        response: telcoautomation.Blueprint,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[telcoautomation.Blueprint, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_blueprint

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TelcoAutomation server but before it is returned to user code.

        We recommend only using this `post_get_blueprint_with_metadata`
        interceptor in new development instead of the `post_get_blueprint` interceptor.
        When both interceptors are used, this `post_get_blueprint_with_metadata` interceptor runs after the
        `post_get_blueprint` interceptor. The (possibly modified) response returned by
        `post_get_blueprint` will be passed to
        `post_get_blueprint_with_metadata`.
        """
        return response, metadata

    def pre_get_deployment(
        self,
        request: telcoautomation.GetDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.GetDeploymentRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TelcoAutomation server.
        """
        return request, metadata

    def post_get_deployment(
        self, response: telcoautomation.Deployment
    ) -> telcoautomation.Deployment:
        """Post-rpc interceptor for get_deployment

        DEPRECATED. Please use the `post_get_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TelcoAutomation server but before
        it is returned to user code. This `post_get_deployment` interceptor runs
        before the `post_get_deployment_with_metadata` interceptor.
        """
        return response

    def post_get_deployment_with_metadata(
        self,
        response: telcoautomation.Deployment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[telcoautomation.Deployment, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TelcoAutomation server but before it is returned to user code.

        We recommend only using this `post_get_deployment_with_metadata`
        interceptor in new development instead of the `post_get_deployment` interceptor.
        When both interceptors are used, this `post_get_deployment_with_metadata` interceptor runs after the
        `post_get_deployment` interceptor. The (possibly modified) response returned by
        `post_get_deployment` will be passed to
        `post_get_deployment_with_metadata`.
        """
        return response, metadata

    def pre_get_edge_slm(
        self,
        request: telcoautomation.GetEdgeSlmRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.GetEdgeSlmRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_edge_slm

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TelcoAutomation server.
        """
        return request, metadata

    def post_get_edge_slm(
        self, response: telcoautomation.EdgeSlm
    ) -> telcoautomation.EdgeSlm:
        """Post-rpc interceptor for get_edge_slm

        DEPRECATED. Please use the `post_get_edge_slm_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TelcoAutomation server but before
        it is returned to user code. This `post_get_edge_slm` interceptor runs
        before the `post_get_edge_slm_with_metadata` interceptor.
        """
        return response

    def post_get_edge_slm_with_metadata(
        self,
        response: telcoautomation.EdgeSlm,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[telcoautomation.EdgeSlm, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_edge_slm

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TelcoAutomation server but before it is returned to user code.

        We recommend only using this `post_get_edge_slm_with_metadata`
        interceptor in new development instead of the `post_get_edge_slm` interceptor.
        When both interceptors are used, this `post_get_edge_slm_with_metadata` interceptor runs after the
        `post_get_edge_slm` interceptor. The (possibly modified) response returned by
        `post_get_edge_slm` will be passed to
        `post_get_edge_slm_with_metadata`.
        """
        return response, metadata

    def pre_get_hydrated_deployment(
        self,
        request: telcoautomation.GetHydratedDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.GetHydratedDeploymentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_hydrated_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TelcoAutomation server.
        """
        return request, metadata

    def post_get_hydrated_deployment(
        self, response: telcoautomation.HydratedDeployment
    ) -> telcoautomation.HydratedDeployment:
        """Post-rpc interceptor for get_hydrated_deployment

        DEPRECATED. Please use the `post_get_hydrated_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TelcoAutomation server but before
        it is returned to user code. This `post_get_hydrated_deployment` interceptor runs
        before the `post_get_hydrated_deployment_with_metadata` interceptor.
        """
        return response

    def post_get_hydrated_deployment_with_metadata(
        self,
        response: telcoautomation.HydratedDeployment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.HydratedDeployment, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_hydrated_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TelcoAutomation server but before it is returned to user code.

        We recommend only using this `post_get_hydrated_deployment_with_metadata`
        interceptor in new development instead of the `post_get_hydrated_deployment` interceptor.
        When both interceptors are used, this `post_get_hydrated_deployment_with_metadata` interceptor runs after the
        `post_get_hydrated_deployment` interceptor. The (possibly modified) response returned by
        `post_get_hydrated_deployment` will be passed to
        `post_get_hydrated_deployment_with_metadata`.
        """
        return response, metadata

    def pre_get_orchestration_cluster(
        self,
        request: telcoautomation.GetOrchestrationClusterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.GetOrchestrationClusterRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_orchestration_cluster

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TelcoAutomation server.
        """
        return request, metadata

    def post_get_orchestration_cluster(
        self, response: telcoautomation.OrchestrationCluster
    ) -> telcoautomation.OrchestrationCluster:
        """Post-rpc interceptor for get_orchestration_cluster

        DEPRECATED. Please use the `post_get_orchestration_cluster_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TelcoAutomation server but before
        it is returned to user code. This `post_get_orchestration_cluster` interceptor runs
        before the `post_get_orchestration_cluster_with_metadata` interceptor.
        """
        return response

    def post_get_orchestration_cluster_with_metadata(
        self,
        response: telcoautomation.OrchestrationCluster,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.OrchestrationCluster, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_orchestration_cluster

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TelcoAutomation server but before it is returned to user code.

        We recommend only using this `post_get_orchestration_cluster_with_metadata`
        interceptor in new development instead of the `post_get_orchestration_cluster` interceptor.
        When both interceptors are used, this `post_get_orchestration_cluster_with_metadata` interceptor runs after the
        `post_get_orchestration_cluster` interceptor. The (possibly modified) response returned by
        `post_get_orchestration_cluster` will be passed to
        `post_get_orchestration_cluster_with_metadata`.
        """
        return response, metadata

    def pre_get_public_blueprint(
        self,
        request: telcoautomation.GetPublicBlueprintRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.GetPublicBlueprintRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_public_blueprint

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TelcoAutomation server.
        """
        return request, metadata

    def post_get_public_blueprint(
        self, response: telcoautomation.PublicBlueprint
    ) -> telcoautomation.PublicBlueprint:
        """Post-rpc interceptor for get_public_blueprint

        DEPRECATED. Please use the `post_get_public_blueprint_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TelcoAutomation server but before
        it is returned to user code. This `post_get_public_blueprint` interceptor runs
        before the `post_get_public_blueprint_with_metadata` interceptor.
        """
        return response

    def post_get_public_blueprint_with_metadata(
        self,
        response: telcoautomation.PublicBlueprint,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.PublicBlueprint, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_public_blueprint

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TelcoAutomation server but before it is returned to user code.

        We recommend only using this `post_get_public_blueprint_with_metadata`
        interceptor in new development instead of the `post_get_public_blueprint` interceptor.
        When both interceptors are used, this `post_get_public_blueprint_with_metadata` interceptor runs after the
        `post_get_public_blueprint` interceptor. The (possibly modified) response returned by
        `post_get_public_blueprint` will be passed to
        `post_get_public_blueprint_with_metadata`.
        """
        return response, metadata

    def pre_list_blueprint_revisions(
        self,
        request: telcoautomation.ListBlueprintRevisionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.ListBlueprintRevisionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_blueprint_revisions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TelcoAutomation server.
        """
        return request, metadata

    def post_list_blueprint_revisions(
        self, response: telcoautomation.ListBlueprintRevisionsResponse
    ) -> telcoautomation.ListBlueprintRevisionsResponse:
        """Post-rpc interceptor for list_blueprint_revisions

        DEPRECATED. Please use the `post_list_blueprint_revisions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TelcoAutomation server but before
        it is returned to user code. This `post_list_blueprint_revisions` interceptor runs
        before the `post_list_blueprint_revisions_with_metadata` interceptor.
        """
        return response

    def post_list_blueprint_revisions_with_metadata(
        self,
        response: telcoautomation.ListBlueprintRevisionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.ListBlueprintRevisionsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_blueprint_revisions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TelcoAutomation server but before it is returned to user code.

        We recommend only using this `post_list_blueprint_revisions_with_metadata`
        interceptor in new development instead of the `post_list_blueprint_revisions` interceptor.
        When both interceptors are used, this `post_list_blueprint_revisions_with_metadata` interceptor runs after the
        `post_list_blueprint_revisions` interceptor. The (possibly modified) response returned by
        `post_list_blueprint_revisions` will be passed to
        `post_list_blueprint_revisions_with_metadata`.
        """
        return response, metadata

    def pre_list_blueprints(
        self,
        request: telcoautomation.ListBlueprintsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.ListBlueprintsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_blueprints

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TelcoAutomation server.
        """
        return request, metadata

    def post_list_blueprints(
        self, response: telcoautomation.ListBlueprintsResponse
    ) -> telcoautomation.ListBlueprintsResponse:
        """Post-rpc interceptor for list_blueprints

        DEPRECATED. Please use the `post_list_blueprints_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TelcoAutomation server but before
        it is returned to user code. This `post_list_blueprints` interceptor runs
        before the `post_list_blueprints_with_metadata` interceptor.
        """
        return response

    def post_list_blueprints_with_metadata(
        self,
        response: telcoautomation.ListBlueprintsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.ListBlueprintsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_blueprints

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TelcoAutomation server but before it is returned to user code.

        We recommend only using this `post_list_blueprints_with_metadata`
        interceptor in new development instead of the `post_list_blueprints` interceptor.
        When both interceptors are used, this `post_list_blueprints_with_metadata` interceptor runs after the
        `post_list_blueprints` interceptor. The (possibly modified) response returned by
        `post_list_blueprints` will be passed to
        `post_list_blueprints_with_metadata`.
        """
        return response, metadata

    def pre_list_deployment_revisions(
        self,
        request: telcoautomation.ListDeploymentRevisionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.ListDeploymentRevisionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_deployment_revisions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TelcoAutomation server.
        """
        return request, metadata

    def post_list_deployment_revisions(
        self, response: telcoautomation.ListDeploymentRevisionsResponse
    ) -> telcoautomation.ListDeploymentRevisionsResponse:
        """Post-rpc interceptor for list_deployment_revisions

        DEPRECATED. Please use the `post_list_deployment_revisions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TelcoAutomation server but before
        it is returned to user code. This `post_list_deployment_revisions` interceptor runs
        before the `post_list_deployment_revisions_with_metadata` interceptor.
        """
        return response

    def post_list_deployment_revisions_with_metadata(
        self,
        response: telcoautomation.ListDeploymentRevisionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.ListDeploymentRevisionsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_deployment_revisions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TelcoAutomation server but before it is returned to user code.

        We recommend only using this `post_list_deployment_revisions_with_metadata`
        interceptor in new development instead of the `post_list_deployment_revisions` interceptor.
        When both interceptors are used, this `post_list_deployment_revisions_with_metadata` interceptor runs after the
        `post_list_deployment_revisions` interceptor. The (possibly modified) response returned by
        `post_list_deployment_revisions` will be passed to
        `post_list_deployment_revisions_with_metadata`.
        """
        return response, metadata

    def pre_list_deployments(
        self,
        request: telcoautomation.ListDeploymentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.ListDeploymentsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_deployments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TelcoAutomation server.
        """
        return request, metadata

    def post_list_deployments(
        self, response: telcoautomation.ListDeploymentsResponse
    ) -> telcoautomation.ListDeploymentsResponse:
        """Post-rpc interceptor for list_deployments

        DEPRECATED. Please use the `post_list_deployments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TelcoAutomation server but before
        it is returned to user code. This `post_list_deployments` interceptor runs
        before the `post_list_deployments_with_metadata` interceptor.
        """
        return response

    def post_list_deployments_with_metadata(
        self,
        response: telcoautomation.ListDeploymentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.ListDeploymentsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_deployments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TelcoAutomation server but before it is returned to user code.

        We recommend only using this `post_list_deployments_with_metadata`
        interceptor in new development instead of the `post_list_deployments` interceptor.
        When both interceptors are used, this `post_list_deployments_with_metadata` interceptor runs after the
        `post_list_deployments` interceptor. The (possibly modified) response returned by
        `post_list_deployments` will be passed to
        `post_list_deployments_with_metadata`.
        """
        return response, metadata

    def pre_list_edge_slms(
        self,
        request: telcoautomation.ListEdgeSlmsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.ListEdgeSlmsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_edge_slms

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TelcoAutomation server.
        """
        return request, metadata

    def post_list_edge_slms(
        self, response: telcoautomation.ListEdgeSlmsResponse
    ) -> telcoautomation.ListEdgeSlmsResponse:
        """Post-rpc interceptor for list_edge_slms

        DEPRECATED. Please use the `post_list_edge_slms_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TelcoAutomation server but before
        it is returned to user code. This `post_list_edge_slms` interceptor runs
        before the `post_list_edge_slms_with_metadata` interceptor.
        """
        return response

    def post_list_edge_slms_with_metadata(
        self,
        response: telcoautomation.ListEdgeSlmsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.ListEdgeSlmsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_edge_slms

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TelcoAutomation server but before it is returned to user code.

        We recommend only using this `post_list_edge_slms_with_metadata`
        interceptor in new development instead of the `post_list_edge_slms` interceptor.
        When both interceptors are used, this `post_list_edge_slms_with_metadata` interceptor runs after the
        `post_list_edge_slms` interceptor. The (possibly modified) response returned by
        `post_list_edge_slms` will be passed to
        `post_list_edge_slms_with_metadata`.
        """
        return response, metadata

    def pre_list_hydrated_deployments(
        self,
        request: telcoautomation.ListHydratedDeploymentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.ListHydratedDeploymentsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_hydrated_deployments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TelcoAutomation server.
        """
        return request, metadata

    def post_list_hydrated_deployments(
        self, response: telcoautomation.ListHydratedDeploymentsResponse
    ) -> telcoautomation.ListHydratedDeploymentsResponse:
        """Post-rpc interceptor for list_hydrated_deployments

        DEPRECATED. Please use the `post_list_hydrated_deployments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TelcoAutomation server but before
        it is returned to user code. This `post_list_hydrated_deployments` interceptor runs
        before the `post_list_hydrated_deployments_with_metadata` interceptor.
        """
        return response

    def post_list_hydrated_deployments_with_metadata(
        self,
        response: telcoautomation.ListHydratedDeploymentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.ListHydratedDeploymentsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_hydrated_deployments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TelcoAutomation server but before it is returned to user code.

        We recommend only using this `post_list_hydrated_deployments_with_metadata`
        interceptor in new development instead of the `post_list_hydrated_deployments` interceptor.
        When both interceptors are used, this `post_list_hydrated_deployments_with_metadata` interceptor runs after the
        `post_list_hydrated_deployments` interceptor. The (possibly modified) response returned by
        `post_list_hydrated_deployments` will be passed to
        `post_list_hydrated_deployments_with_metadata`.
        """
        return response, metadata

    def pre_list_orchestration_clusters(
        self,
        request: telcoautomation.ListOrchestrationClustersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.ListOrchestrationClustersRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_orchestration_clusters

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TelcoAutomation server.
        """
        return request, metadata

    def post_list_orchestration_clusters(
        self, response: telcoautomation.ListOrchestrationClustersResponse
    ) -> telcoautomation.ListOrchestrationClustersResponse:
        """Post-rpc interceptor for list_orchestration_clusters

        DEPRECATED. Please use the `post_list_orchestration_clusters_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TelcoAutomation server but before
        it is returned to user code. This `post_list_orchestration_clusters` interceptor runs
        before the `post_list_orchestration_clusters_with_metadata` interceptor.
        """
        return response

    def post_list_orchestration_clusters_with_metadata(
        self,
        response: telcoautomation.ListOrchestrationClustersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.ListOrchestrationClustersResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_orchestration_clusters

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TelcoAutomation server but before it is returned to user code.

        We recommend only using this `post_list_orchestration_clusters_with_metadata`
        interceptor in new development instead of the `post_list_orchestration_clusters` interceptor.
        When both interceptors are used, this `post_list_orchestration_clusters_with_metadata` interceptor runs after the
        `post_list_orchestration_clusters` interceptor. The (possibly modified) response returned by
        `post_list_orchestration_clusters` will be passed to
        `post_list_orchestration_clusters_with_metadata`.
        """
        return response, metadata

    def pre_list_public_blueprints(
        self,
        request: telcoautomation.ListPublicBlueprintsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.ListPublicBlueprintsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_public_blueprints

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TelcoAutomation server.
        """
        return request, metadata

    def post_list_public_blueprints(
        self, response: telcoautomation.ListPublicBlueprintsResponse
    ) -> telcoautomation.ListPublicBlueprintsResponse:
        """Post-rpc interceptor for list_public_blueprints

        DEPRECATED. Please use the `post_list_public_blueprints_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TelcoAutomation server but before
        it is returned to user code. This `post_list_public_blueprints` interceptor runs
        before the `post_list_public_blueprints_with_metadata` interceptor.
        """
        return response

    def post_list_public_blueprints_with_metadata(
        self,
        response: telcoautomation.ListPublicBlueprintsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.ListPublicBlueprintsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_public_blueprints

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TelcoAutomation server but before it is returned to user code.

        We recommend only using this `post_list_public_blueprints_with_metadata`
        interceptor in new development instead of the `post_list_public_blueprints` interceptor.
        When both interceptors are used, this `post_list_public_blueprints_with_metadata` interceptor runs after the
        `post_list_public_blueprints` interceptor. The (possibly modified) response returned by
        `post_list_public_blueprints` will be passed to
        `post_list_public_blueprints_with_metadata`.
        """
        return response, metadata

    def pre_propose_blueprint(
        self,
        request: telcoautomation.ProposeBlueprintRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.ProposeBlueprintRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for propose_blueprint

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TelcoAutomation server.
        """
        return request, metadata

    def post_propose_blueprint(
        self, response: telcoautomation.Blueprint
    ) -> telcoautomation.Blueprint:
        """Post-rpc interceptor for propose_blueprint

        DEPRECATED. Please use the `post_propose_blueprint_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TelcoAutomation server but before
        it is returned to user code. This `post_propose_blueprint` interceptor runs
        before the `post_propose_blueprint_with_metadata` interceptor.
        """
        return response

    def post_propose_blueprint_with_metadata(
        self,
        response: telcoautomation.Blueprint,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[telcoautomation.Blueprint, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for propose_blueprint

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TelcoAutomation server but before it is returned to user code.

        We recommend only using this `post_propose_blueprint_with_metadata`
        interceptor in new development instead of the `post_propose_blueprint` interceptor.
        When both interceptors are used, this `post_propose_blueprint_with_metadata` interceptor runs after the
        `post_propose_blueprint` interceptor. The (possibly modified) response returned by
        `post_propose_blueprint` will be passed to
        `post_propose_blueprint_with_metadata`.
        """
        return response, metadata

    def pre_reject_blueprint(
        self,
        request: telcoautomation.RejectBlueprintRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.RejectBlueprintRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for reject_blueprint

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TelcoAutomation server.
        """
        return request, metadata

    def post_reject_blueprint(
        self, response: telcoautomation.Blueprint
    ) -> telcoautomation.Blueprint:
        """Post-rpc interceptor for reject_blueprint

        DEPRECATED. Please use the `post_reject_blueprint_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TelcoAutomation server but before
        it is returned to user code. This `post_reject_blueprint` interceptor runs
        before the `post_reject_blueprint_with_metadata` interceptor.
        """
        return response

    def post_reject_blueprint_with_metadata(
        self,
        response: telcoautomation.Blueprint,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[telcoautomation.Blueprint, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for reject_blueprint

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TelcoAutomation server but before it is returned to user code.

        We recommend only using this `post_reject_blueprint_with_metadata`
        interceptor in new development instead of the `post_reject_blueprint` interceptor.
        When both interceptors are used, this `post_reject_blueprint_with_metadata` interceptor runs after the
        `post_reject_blueprint` interceptor. The (possibly modified) response returned by
        `post_reject_blueprint` will be passed to
        `post_reject_blueprint_with_metadata`.
        """
        return response, metadata

    def pre_remove_deployment(
        self,
        request: telcoautomation.RemoveDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.RemoveDeploymentRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for remove_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TelcoAutomation server.
        """
        return request, metadata

    def pre_rollback_deployment(
        self,
        request: telcoautomation.RollbackDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.RollbackDeploymentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for rollback_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TelcoAutomation server.
        """
        return request, metadata

    def post_rollback_deployment(
        self, response: telcoautomation.Deployment
    ) -> telcoautomation.Deployment:
        """Post-rpc interceptor for rollback_deployment

        DEPRECATED. Please use the `post_rollback_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TelcoAutomation server but before
        it is returned to user code. This `post_rollback_deployment` interceptor runs
        before the `post_rollback_deployment_with_metadata` interceptor.
        """
        return response

    def post_rollback_deployment_with_metadata(
        self,
        response: telcoautomation.Deployment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[telcoautomation.Deployment, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for rollback_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TelcoAutomation server but before it is returned to user code.

        We recommend only using this `post_rollback_deployment_with_metadata`
        interceptor in new development instead of the `post_rollback_deployment` interceptor.
        When both interceptors are used, this `post_rollback_deployment_with_metadata` interceptor runs after the
        `post_rollback_deployment` interceptor. The (possibly modified) response returned by
        `post_rollback_deployment` will be passed to
        `post_rollback_deployment_with_metadata`.
        """
        return response, metadata

    def pre_search_blueprint_revisions(
        self,
        request: telcoautomation.SearchBlueprintRevisionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.SearchBlueprintRevisionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for search_blueprint_revisions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TelcoAutomation server.
        """
        return request, metadata

    def post_search_blueprint_revisions(
        self, response: telcoautomation.SearchBlueprintRevisionsResponse
    ) -> telcoautomation.SearchBlueprintRevisionsResponse:
        """Post-rpc interceptor for search_blueprint_revisions

        DEPRECATED. Please use the `post_search_blueprint_revisions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TelcoAutomation server but before
        it is returned to user code. This `post_search_blueprint_revisions` interceptor runs
        before the `post_search_blueprint_revisions_with_metadata` interceptor.
        """
        return response

    def post_search_blueprint_revisions_with_metadata(
        self,
        response: telcoautomation.SearchBlueprintRevisionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.SearchBlueprintRevisionsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for search_blueprint_revisions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TelcoAutomation server but before it is returned to user code.

        We recommend only using this `post_search_blueprint_revisions_with_metadata`
        interceptor in new development instead of the `post_search_blueprint_revisions` interceptor.
        When both interceptors are used, this `post_search_blueprint_revisions_with_metadata` interceptor runs after the
        `post_search_blueprint_revisions` interceptor. The (possibly modified) response returned by
        `post_search_blueprint_revisions` will be passed to
        `post_search_blueprint_revisions_with_metadata`.
        """
        return response, metadata

    def pre_search_deployment_revisions(
        self,
        request: telcoautomation.SearchDeploymentRevisionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.SearchDeploymentRevisionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for search_deployment_revisions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TelcoAutomation server.
        """
        return request, metadata

    def post_search_deployment_revisions(
        self, response: telcoautomation.SearchDeploymentRevisionsResponse
    ) -> telcoautomation.SearchDeploymentRevisionsResponse:
        """Post-rpc interceptor for search_deployment_revisions

        DEPRECATED. Please use the `post_search_deployment_revisions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TelcoAutomation server but before
        it is returned to user code. This `post_search_deployment_revisions` interceptor runs
        before the `post_search_deployment_revisions_with_metadata` interceptor.
        """
        return response

    def post_search_deployment_revisions_with_metadata(
        self,
        response: telcoautomation.SearchDeploymentRevisionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.SearchDeploymentRevisionsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for search_deployment_revisions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TelcoAutomation server but before it is returned to user code.

        We recommend only using this `post_search_deployment_revisions_with_metadata`
        interceptor in new development instead of the `post_search_deployment_revisions` interceptor.
        When both interceptors are used, this `post_search_deployment_revisions_with_metadata` interceptor runs after the
        `post_search_deployment_revisions` interceptor. The (possibly modified) response returned by
        `post_search_deployment_revisions` will be passed to
        `post_search_deployment_revisions_with_metadata`.
        """
        return response, metadata

    def pre_update_blueprint(
        self,
        request: telcoautomation.UpdateBlueprintRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.UpdateBlueprintRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_blueprint

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TelcoAutomation server.
        """
        return request, metadata

    def post_update_blueprint(
        self, response: telcoautomation.Blueprint
    ) -> telcoautomation.Blueprint:
        """Post-rpc interceptor for update_blueprint

        DEPRECATED. Please use the `post_update_blueprint_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TelcoAutomation server but before
        it is returned to user code. This `post_update_blueprint` interceptor runs
        before the `post_update_blueprint_with_metadata` interceptor.
        """
        return response

    def post_update_blueprint_with_metadata(
        self,
        response: telcoautomation.Blueprint,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[telcoautomation.Blueprint, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_blueprint

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TelcoAutomation server but before it is returned to user code.

        We recommend only using this `post_update_blueprint_with_metadata`
        interceptor in new development instead of the `post_update_blueprint` interceptor.
        When both interceptors are used, this `post_update_blueprint_with_metadata` interceptor runs after the
        `post_update_blueprint` interceptor. The (possibly modified) response returned by
        `post_update_blueprint` will be passed to
        `post_update_blueprint_with_metadata`.
        """
        return response, metadata

    def pre_update_deployment(
        self,
        request: telcoautomation.UpdateDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.UpdateDeploymentRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TelcoAutomation server.
        """
        return request, metadata

    def post_update_deployment(
        self, response: telcoautomation.Deployment
    ) -> telcoautomation.Deployment:
        """Post-rpc interceptor for update_deployment

        DEPRECATED. Please use the `post_update_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TelcoAutomation server but before
        it is returned to user code. This `post_update_deployment` interceptor runs
        before the `post_update_deployment_with_metadata` interceptor.
        """
        return response

    def post_update_deployment_with_metadata(
        self,
        response: telcoautomation.Deployment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[telcoautomation.Deployment, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TelcoAutomation server but before it is returned to user code.

        We recommend only using this `post_update_deployment_with_metadata`
        interceptor in new development instead of the `post_update_deployment` interceptor.
        When both interceptors are used, this `post_update_deployment_with_metadata` interceptor runs after the
        `post_update_deployment` interceptor. The (possibly modified) response returned by
        `post_update_deployment` will be passed to
        `post_update_deployment_with_metadata`.
        """
        return response, metadata

    def pre_update_hydrated_deployment(
        self,
        request: telcoautomation.UpdateHydratedDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.UpdateHydratedDeploymentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_hydrated_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TelcoAutomation server.
        """
        return request, metadata

    def post_update_hydrated_deployment(
        self, response: telcoautomation.HydratedDeployment
    ) -> telcoautomation.HydratedDeployment:
        """Post-rpc interceptor for update_hydrated_deployment

        DEPRECATED. Please use the `post_update_hydrated_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TelcoAutomation server but before
        it is returned to user code. This `post_update_hydrated_deployment` interceptor runs
        before the `post_update_hydrated_deployment_with_metadata` interceptor.
        """
        return response

    def post_update_hydrated_deployment_with_metadata(
        self,
        response: telcoautomation.HydratedDeployment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        telcoautomation.HydratedDeployment, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for update_hydrated_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TelcoAutomation server but before it is returned to user code.

        We recommend only using this `post_update_hydrated_deployment_with_metadata`
        interceptor in new development instead of the `post_update_hydrated_deployment` interceptor.
        When both interceptors are used, this `post_update_hydrated_deployment_with_metadata` interceptor runs after the
        `post_update_hydrated_deployment` interceptor. The (possibly modified) response returned by
        `post_update_hydrated_deployment` will be passed to
        `post_update_hydrated_deployment_with_metadata`.
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
        before they are sent to the TelcoAutomation server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the TelcoAutomation server but before
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
        before they are sent to the TelcoAutomation server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the TelcoAutomation server but before
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
        before they are sent to the TelcoAutomation server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the TelcoAutomation server but before
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
        before they are sent to the TelcoAutomation server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the TelcoAutomation server but before
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
        before they are sent to the TelcoAutomation server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the TelcoAutomation server but before
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
        before they are sent to the TelcoAutomation server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the TelcoAutomation server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class TelcoAutomationRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: TelcoAutomationRestInterceptor


class TelcoAutomationRestTransport(_BaseTelcoAutomationRestTransport):
    """REST backend synchronous transport for TelcoAutomation.

    TelcoAutomation Service manages the control plane cluster
    a.k.a. Orchestration Cluster (GKE cluster with config
    controller) of TNA. It also exposes blueprint APIs which manages
    the lifecycle of blueprints that control the infrastructure
    setup (e.g GDCE clusters) and deployment of network functions.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "telcoautomation.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[TelcoAutomationRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'telcoautomation.googleapis.com').
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
            interceptor (Optional[TelcoAutomationRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or TelcoAutomationRestInterceptor()
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
                ],
                "google.longrunning.Operations.DeleteOperation": [
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.ListOperations": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/operations}",
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

    class _ApplyDeployment(
        _BaseTelcoAutomationRestTransport._BaseApplyDeployment, TelcoAutomationRestStub
    ):
        def __hash__(self):
            return hash("TelcoAutomationRestTransport.ApplyDeployment")

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
            request: telcoautomation.ApplyDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> telcoautomation.Deployment:
            r"""Call the apply deployment method over HTTP.

            Args:
                request (~.telcoautomation.ApplyDeploymentRequest):
                    The request object. Request object for ``ApplyDeployment``. The resources in
                given deployment gets applied to Orchestration Cluster.
                A new revision is created when a deployment is applied.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.telcoautomation.Deployment:
                    Deployment contains a collection of
                YAML files (This collection is also
                known as package) that can to applied on
                an orchestration cluster (GKE cluster
                with TNA addons) or a workload cluster.

            """

            http_options = _BaseTelcoAutomationRestTransport._BaseApplyDeployment._get_http_options()
            request, metadata = self._interceptor.pre_apply_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTelcoAutomationRestTransport._BaseApplyDeployment,
                    "_BaseApplyDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.telcoautomation_v1.TelcoAutomationClient.ApplyDeployment",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "ApplyDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TelcoAutomationRestTransport._ApplyDeployment._get_response(
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
            resp = telcoautomation.Deployment()
            pb_resp = telcoautomation.Deployment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_apply_deployment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_apply_deployment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = telcoautomation.Deployment.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.telcoautomation_v1.TelcoAutomationClient.apply_deployment",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "ApplyDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ApplyHydratedDeployment(
        _BaseTelcoAutomationRestTransport._BaseApplyHydratedDeployment,
        TelcoAutomationRestStub,
    ):
        def __hash__(self):
            return hash("TelcoAutomationRestTransport.ApplyHydratedDeployment")

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
            request: telcoautomation.ApplyHydratedDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> telcoautomation.HydratedDeployment:
            r"""Call the apply hydrated deployment method over HTTP.

            Args:
                request (~.telcoautomation.ApplyHydratedDeploymentRequest):
                    The request object. Request for applying a hydrated
                deployment.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.telcoautomation.HydratedDeployment:
                    A collection of kubernetes yaml files
                which are deployed on a Workload
                Cluster. Hydrated Deployments are
                created by TNA intent based automation.

            """

            http_options = _BaseTelcoAutomationRestTransport._BaseApplyHydratedDeployment._get_http_options()
            request, metadata = self._interceptor.pre_apply_hydrated_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTelcoAutomationRestTransport._BaseApplyHydratedDeployment,
                    "_BaseApplyHydratedDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.telcoautomation_v1.TelcoAutomationClient.ApplyHydratedDeployment",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "ApplyHydratedDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                TelcoAutomationRestTransport._ApplyHydratedDeployment._get_response(
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
            resp = telcoautomation.HydratedDeployment()
            pb_resp = telcoautomation.HydratedDeployment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_apply_hydrated_deployment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_apply_hydrated_deployment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = telcoautomation.HydratedDeployment.to_json(
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
                    "Received response for google.cloud.telcoautomation_v1.TelcoAutomationClient.apply_hydrated_deployment",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "ApplyHydratedDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ApproveBlueprint(
        _BaseTelcoAutomationRestTransport._BaseApproveBlueprint, TelcoAutomationRestStub
    ):
        def __hash__(self):
            return hash("TelcoAutomationRestTransport.ApproveBlueprint")

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
            request: telcoautomation.ApproveBlueprintRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> telcoautomation.Blueprint:
            r"""Call the approve blueprint method over HTTP.

            Args:
                request (~.telcoautomation.ApproveBlueprintRequest):
                    The request object. Request object for ``ApproveBlueprint``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.telcoautomation.Blueprint:
                    A Blueprint contains a collection of
                kubernetes resources in the form of YAML
                files. The file contents of a blueprint
                are collectively known as package. A
                blueprint can be
                a) imported from TNA's public catalog
                b) modified as per a user's need
                c) proposed and approved.
                On approval, a revision of blueprint is
                created which can be used to create a
                deployment on Orchestration or Workload
                Cluster.

            """

            http_options = _BaseTelcoAutomationRestTransport._BaseApproveBlueprint._get_http_options()
            request, metadata = self._interceptor.pre_approve_blueprint(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTelcoAutomationRestTransport._BaseApproveBlueprint,
                    "_BaseApproveBlueprint__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.telcoautomation_v1.TelcoAutomationClient.ApproveBlueprint",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "ApproveBlueprint",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TelcoAutomationRestTransport._ApproveBlueprint._get_response(
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
            resp = telcoautomation.Blueprint()
            pb_resp = telcoautomation.Blueprint.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_approve_blueprint(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_approve_blueprint_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = telcoautomation.Blueprint.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.telcoautomation_v1.TelcoAutomationClient.approve_blueprint",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "ApproveBlueprint",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ComputeDeploymentStatus(
        _BaseTelcoAutomationRestTransport._BaseComputeDeploymentStatus,
        TelcoAutomationRestStub,
    ):
        def __hash__(self):
            return hash("TelcoAutomationRestTransport.ComputeDeploymentStatus")

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
            request: telcoautomation.ComputeDeploymentStatusRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> telcoautomation.ComputeDeploymentStatusResponse:
            r"""Call the compute deployment status method over HTTP.

            Args:
                request (~.telcoautomation.ComputeDeploymentStatusRequest):
                    The request object. Request object for ``ComputeDeploymentStatus``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.telcoautomation.ComputeDeploymentStatusResponse:
                    Response object for ``ComputeDeploymentStatus``.
            """

            http_options = _BaseTelcoAutomationRestTransport._BaseComputeDeploymentStatus._get_http_options()
            request, metadata = self._interceptor.pre_compute_deployment_status(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTelcoAutomationRestTransport._BaseComputeDeploymentStatus,
                    "_BaseComputeDeploymentStatus__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.telcoautomation_v1.TelcoAutomationClient.ComputeDeploymentStatus",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "ComputeDeploymentStatus",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                TelcoAutomationRestTransport._ComputeDeploymentStatus._get_response(
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
            resp = telcoautomation.ComputeDeploymentStatusResponse()
            pb_resp = telcoautomation.ComputeDeploymentStatusResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_compute_deployment_status(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_compute_deployment_status_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        telcoautomation.ComputeDeploymentStatusResponse.to_json(
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
                    "Received response for google.cloud.telcoautomation_v1.TelcoAutomationClient.compute_deployment_status",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "ComputeDeploymentStatus",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateBlueprint(
        _BaseTelcoAutomationRestTransport._BaseCreateBlueprint, TelcoAutomationRestStub
    ):
        def __hash__(self):
            return hash("TelcoAutomationRestTransport.CreateBlueprint")

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
            request: telcoautomation.CreateBlueprintRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> telcoautomation.Blueprint:
            r"""Call the create blueprint method over HTTP.

            Args:
                request (~.telcoautomation.CreateBlueprintRequest):
                    The request object. Request object for ``CreateBlueprint``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.telcoautomation.Blueprint:
                    A Blueprint contains a collection of
                kubernetes resources in the form of YAML
                files. The file contents of a blueprint
                are collectively known as package. A
                blueprint can be
                a) imported from TNA's public catalog
                b) modified as per a user's need
                c) proposed and approved.
                On approval, a revision of blueprint is
                created which can be used to create a
                deployment on Orchestration or Workload
                Cluster.

            """

            http_options = _BaseTelcoAutomationRestTransport._BaseCreateBlueprint._get_http_options()
            request, metadata = self._interceptor.pre_create_blueprint(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTelcoAutomationRestTransport._BaseCreateBlueprint,
                    "_BaseCreateBlueprint__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.telcoautomation_v1.TelcoAutomationClient.CreateBlueprint",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "CreateBlueprint",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TelcoAutomationRestTransport._CreateBlueprint._get_response(
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
            resp = telcoautomation.Blueprint()
            pb_resp = telcoautomation.Blueprint.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_blueprint(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_blueprint_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = telcoautomation.Blueprint.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.telcoautomation_v1.TelcoAutomationClient.create_blueprint",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "CreateBlueprint",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateDeployment(
        _BaseTelcoAutomationRestTransport._BaseCreateDeployment, TelcoAutomationRestStub
    ):
        def __hash__(self):
            return hash("TelcoAutomationRestTransport.CreateDeployment")

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
            request: telcoautomation.CreateDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> telcoautomation.Deployment:
            r"""Call the create deployment method over HTTP.

            Args:
                request (~.telcoautomation.CreateDeploymentRequest):
                    The request object. Request object for ``CreateDeployment``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.telcoautomation.Deployment:
                    Deployment contains a collection of
                YAML files (This collection is also
                known as package) that can to applied on
                an orchestration cluster (GKE cluster
                with TNA addons) or a workload cluster.

            """

            http_options = _BaseTelcoAutomationRestTransport._BaseCreateDeployment._get_http_options()
            request, metadata = self._interceptor.pre_create_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTelcoAutomationRestTransport._BaseCreateDeployment,
                    "_BaseCreateDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.telcoautomation_v1.TelcoAutomationClient.CreateDeployment",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "CreateDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TelcoAutomationRestTransport._CreateDeployment._get_response(
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
            resp = telcoautomation.Deployment()
            pb_resp = telcoautomation.Deployment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_deployment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_deployment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = telcoautomation.Deployment.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.telcoautomation_v1.TelcoAutomationClient.create_deployment",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "CreateDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateEdgeSlm(
        _BaseTelcoAutomationRestTransport._BaseCreateEdgeSlm, TelcoAutomationRestStub
    ):
        def __hash__(self):
            return hash("TelcoAutomationRestTransport.CreateEdgeSlm")

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
            request: telcoautomation.CreateEdgeSlmRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create edge slm method over HTTP.

            Args:
                request (~.telcoautomation.CreateEdgeSlmRequest):
                    The request object. Message for creating a EdgeSlm.
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

            http_options = (
                _BaseTelcoAutomationRestTransport._BaseCreateEdgeSlm._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_edge_slm(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTelcoAutomationRestTransport._BaseCreateEdgeSlm,
                    "_BaseCreateEdgeSlm__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.telcoautomation_v1.TelcoAutomationClient.CreateEdgeSlm",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "CreateEdgeSlm",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TelcoAutomationRestTransport._CreateEdgeSlm._get_response(
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

            resp = self._interceptor.post_create_edge_slm(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_edge_slm_with_metadata(
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
                    "Received response for google.cloud.telcoautomation_v1.TelcoAutomationClient.create_edge_slm",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "CreateEdgeSlm",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateOrchestrationCluster(
        _BaseTelcoAutomationRestTransport._BaseCreateOrchestrationCluster,
        TelcoAutomationRestStub,
    ):
        def __hash__(self):
            return hash("TelcoAutomationRestTransport.CreateOrchestrationCluster")

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
            request: telcoautomation.CreateOrchestrationClusterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create orchestration
            cluster method over HTTP.

                Args:
                    request (~.telcoautomation.CreateOrchestrationClusterRequest):
                        The request object. Message for creating a
                    OrchestrationCluster.
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

            http_options = _BaseTelcoAutomationRestTransport._BaseCreateOrchestrationCluster._get_http_options()
            request, metadata = self._interceptor.pre_create_orchestration_cluster(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTelcoAutomationRestTransport._BaseCreateOrchestrationCluster,
                    "_BaseCreateOrchestrationCluster__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.telcoautomation_v1.TelcoAutomationClient.CreateOrchestrationCluster",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "CreateOrchestrationCluster",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                TelcoAutomationRestTransport._CreateOrchestrationCluster._get_response(
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

            resp = self._interceptor.post_create_orchestration_cluster(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_orchestration_cluster_with_metadata(
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
                    "Received response for google.cloud.telcoautomation_v1.TelcoAutomationClient.create_orchestration_cluster",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "CreateOrchestrationCluster",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteBlueprint(
        _BaseTelcoAutomationRestTransport._BaseDeleteBlueprint, TelcoAutomationRestStub
    ):
        def __hash__(self):
            return hash("TelcoAutomationRestTransport.DeleteBlueprint")

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
            request: telcoautomation.DeleteBlueprintRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete blueprint method over HTTP.

            Args:
                request (~.telcoautomation.DeleteBlueprintRequest):
                    The request object. Request object for ``DeleteBlueprint``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseTelcoAutomationRestTransport._BaseDeleteBlueprint._get_http_options()
            request, metadata = self._interceptor.pre_delete_blueprint(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTelcoAutomationRestTransport._BaseDeleteBlueprint,
                    "_BaseDeleteBlueprint__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.telcoautomation_v1.TelcoAutomationClient.DeleteBlueprint",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "DeleteBlueprint",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TelcoAutomationRestTransport._DeleteBlueprint._get_response(
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

    class _DeleteEdgeSlm(
        _BaseTelcoAutomationRestTransport._BaseDeleteEdgeSlm, TelcoAutomationRestStub
    ):
        def __hash__(self):
            return hash("TelcoAutomationRestTransport.DeleteEdgeSlm")

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
            request: telcoautomation.DeleteEdgeSlmRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete edge slm method over HTTP.

            Args:
                request (~.telcoautomation.DeleteEdgeSlmRequest):
                    The request object. Message for deleting a EdgeSlm.
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

            http_options = (
                _BaseTelcoAutomationRestTransport._BaseDeleteEdgeSlm._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_edge_slm(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTelcoAutomationRestTransport._BaseDeleteEdgeSlm,
                    "_BaseDeleteEdgeSlm__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.telcoautomation_v1.TelcoAutomationClient.DeleteEdgeSlm",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "DeleteEdgeSlm",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TelcoAutomationRestTransport._DeleteEdgeSlm._get_response(
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

            resp = self._interceptor.post_delete_edge_slm(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_edge_slm_with_metadata(
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
                    "Received response for google.cloud.telcoautomation_v1.TelcoAutomationClient.delete_edge_slm",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "DeleteEdgeSlm",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteOrchestrationCluster(
        _BaseTelcoAutomationRestTransport._BaseDeleteOrchestrationCluster,
        TelcoAutomationRestStub,
    ):
        def __hash__(self):
            return hash("TelcoAutomationRestTransport.DeleteOrchestrationCluster")

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
            request: telcoautomation.DeleteOrchestrationClusterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete orchestration
            cluster method over HTTP.

                Args:
                    request (~.telcoautomation.DeleteOrchestrationClusterRequest):
                        The request object. Message for deleting a
                    OrchestrationCluster.
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

            http_options = _BaseTelcoAutomationRestTransport._BaseDeleteOrchestrationCluster._get_http_options()
            request, metadata = self._interceptor.pre_delete_orchestration_cluster(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTelcoAutomationRestTransport._BaseDeleteOrchestrationCluster,
                    "_BaseDeleteOrchestrationCluster__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.telcoautomation_v1.TelcoAutomationClient.DeleteOrchestrationCluster",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "DeleteOrchestrationCluster",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                TelcoAutomationRestTransport._DeleteOrchestrationCluster._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_orchestration_cluster(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_orchestration_cluster_with_metadata(
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
                    "Received response for google.cloud.telcoautomation_v1.TelcoAutomationClient.delete_orchestration_cluster",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "DeleteOrchestrationCluster",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DiscardBlueprintChanges(
        _BaseTelcoAutomationRestTransport._BaseDiscardBlueprintChanges,
        TelcoAutomationRestStub,
    ):
        def __hash__(self):
            return hash("TelcoAutomationRestTransport.DiscardBlueprintChanges")

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
            request: telcoautomation.DiscardBlueprintChangesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> telcoautomation.DiscardBlueprintChangesResponse:
            r"""Call the discard blueprint changes method over HTTP.

            Args:
                request (~.telcoautomation.DiscardBlueprintChangesRequest):
                    The request object. Request object for ``DiscardBlueprintChanges``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.telcoautomation.DiscardBlueprintChangesResponse:
                    Response object for ``DiscardBlueprintChanges``.
            """

            http_options = _BaseTelcoAutomationRestTransport._BaseDiscardBlueprintChanges._get_http_options()
            request, metadata = self._interceptor.pre_discard_blueprint_changes(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTelcoAutomationRestTransport._BaseDiscardBlueprintChanges,
                    "_BaseDiscardBlueprintChanges__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.telcoautomation_v1.TelcoAutomationClient.DiscardBlueprintChanges",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "DiscardBlueprintChanges",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                TelcoAutomationRestTransport._DiscardBlueprintChanges._get_response(
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
            resp = telcoautomation.DiscardBlueprintChangesResponse()
            pb_resp = telcoautomation.DiscardBlueprintChangesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_discard_blueprint_changes(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_discard_blueprint_changes_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        telcoautomation.DiscardBlueprintChangesResponse.to_json(
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
                    "Received response for google.cloud.telcoautomation_v1.TelcoAutomationClient.discard_blueprint_changes",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "DiscardBlueprintChanges",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DiscardDeploymentChanges(
        _BaseTelcoAutomationRestTransport._BaseDiscardDeploymentChanges,
        TelcoAutomationRestStub,
    ):
        def __hash__(self):
            return hash("TelcoAutomationRestTransport.DiscardDeploymentChanges")

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
            request: telcoautomation.DiscardDeploymentChangesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> telcoautomation.DiscardDeploymentChangesResponse:
            r"""Call the discard deployment
            changes method over HTTP.

                Args:
                    request (~.telcoautomation.DiscardDeploymentChangesRequest):
                        The request object. Request object for ``DiscardDeploymentChanges``.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.telcoautomation.DiscardDeploymentChangesResponse:
                        Response object for ``DiscardDeploymentChanges``.
            """

            http_options = _BaseTelcoAutomationRestTransport._BaseDiscardDeploymentChanges._get_http_options()
            request, metadata = self._interceptor.pre_discard_deployment_changes(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTelcoAutomationRestTransport._BaseDiscardDeploymentChanges,
                    "_BaseDiscardDeploymentChanges__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.telcoautomation_v1.TelcoAutomationClient.DiscardDeploymentChanges",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "DiscardDeploymentChanges",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                TelcoAutomationRestTransport._DiscardDeploymentChanges._get_response(
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
            resp = telcoautomation.DiscardDeploymentChangesResponse()
            pb_resp = telcoautomation.DiscardDeploymentChangesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_discard_deployment_changes(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_discard_deployment_changes_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        telcoautomation.DiscardDeploymentChangesResponse.to_json(
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
                    "Received response for google.cloud.telcoautomation_v1.TelcoAutomationClient.discard_deployment_changes",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "DiscardDeploymentChanges",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetBlueprint(
        _BaseTelcoAutomationRestTransport._BaseGetBlueprint, TelcoAutomationRestStub
    ):
        def __hash__(self):
            return hash("TelcoAutomationRestTransport.GetBlueprint")

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
            request: telcoautomation.GetBlueprintRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> telcoautomation.Blueprint:
            r"""Call the get blueprint method over HTTP.

            Args:
                request (~.telcoautomation.GetBlueprintRequest):
                    The request object. Request object for ``GetBlueprint``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.telcoautomation.Blueprint:
                    A Blueprint contains a collection of
                kubernetes resources in the form of YAML
                files. The file contents of a blueprint
                are collectively known as package. A
                blueprint can be
                a) imported from TNA's public catalog
                b) modified as per a user's need
                c) proposed and approved.
                On approval, a revision of blueprint is
                created which can be used to create a
                deployment on Orchestration or Workload
                Cluster.

            """

            http_options = (
                _BaseTelcoAutomationRestTransport._BaseGetBlueprint._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_blueprint(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTelcoAutomationRestTransport._BaseGetBlueprint,
                    "_BaseGetBlueprint__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.telcoautomation_v1.TelcoAutomationClient.GetBlueprint",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "GetBlueprint",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TelcoAutomationRestTransport._GetBlueprint._get_response(
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
            resp = telcoautomation.Blueprint()
            pb_resp = telcoautomation.Blueprint.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_blueprint(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_blueprint_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = telcoautomation.Blueprint.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.telcoautomation_v1.TelcoAutomationClient.get_blueprint",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "GetBlueprint",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDeployment(
        _BaseTelcoAutomationRestTransport._BaseGetDeployment, TelcoAutomationRestStub
    ):
        def __hash__(self):
            return hash("TelcoAutomationRestTransport.GetDeployment")

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
            request: telcoautomation.GetDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> telcoautomation.Deployment:
            r"""Call the get deployment method over HTTP.

            Args:
                request (~.telcoautomation.GetDeploymentRequest):
                    The request object. Request object for ``GetDeployment``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.telcoautomation.Deployment:
                    Deployment contains a collection of
                YAML files (This collection is also
                known as package) that can to applied on
                an orchestration cluster (GKE cluster
                with TNA addons) or a workload cluster.

            """

            http_options = (
                _BaseTelcoAutomationRestTransport._BaseGetDeployment._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_deployment(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTelcoAutomationRestTransport._BaseGetDeployment,
                    "_BaseGetDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.telcoautomation_v1.TelcoAutomationClient.GetDeployment",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "GetDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TelcoAutomationRestTransport._GetDeployment._get_response(
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
            resp = telcoautomation.Deployment()
            pb_resp = telcoautomation.Deployment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_deployment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_deployment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = telcoautomation.Deployment.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.telcoautomation_v1.TelcoAutomationClient.get_deployment",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "GetDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetEdgeSlm(
        _BaseTelcoAutomationRestTransport._BaseGetEdgeSlm, TelcoAutomationRestStub
    ):
        def __hash__(self):
            return hash("TelcoAutomationRestTransport.GetEdgeSlm")

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
            request: telcoautomation.GetEdgeSlmRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> telcoautomation.EdgeSlm:
            r"""Call the get edge slm method over HTTP.

            Args:
                request (~.telcoautomation.GetEdgeSlmRequest):
                    The request object. Message for getting a EdgeSlm.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.telcoautomation.EdgeSlm:
                    EdgeSlm represents an SLM instance
                which manages the lifecycle of edge
                components installed on Workload
                clusters managed by an Orchestration
                Cluster.

            """

            http_options = (
                _BaseTelcoAutomationRestTransport._BaseGetEdgeSlm._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_edge_slm(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTelcoAutomationRestTransport._BaseGetEdgeSlm,
                    "_BaseGetEdgeSlm__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.telcoautomation_v1.TelcoAutomationClient.GetEdgeSlm",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "GetEdgeSlm",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TelcoAutomationRestTransport._GetEdgeSlm._get_response(
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
            resp = telcoautomation.EdgeSlm()
            pb_resp = telcoautomation.EdgeSlm.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_edge_slm(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_edge_slm_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = telcoautomation.EdgeSlm.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.telcoautomation_v1.TelcoAutomationClient.get_edge_slm",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "GetEdgeSlm",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetHydratedDeployment(
        _BaseTelcoAutomationRestTransport._BaseGetHydratedDeployment,
        TelcoAutomationRestStub,
    ):
        def __hash__(self):
            return hash("TelcoAutomationRestTransport.GetHydratedDeployment")

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
            request: telcoautomation.GetHydratedDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> telcoautomation.HydratedDeployment:
            r"""Call the get hydrated deployment method over HTTP.

            Args:
                request (~.telcoautomation.GetHydratedDeploymentRequest):
                    The request object. Request object for ``GetHydratedDeployment``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.telcoautomation.HydratedDeployment:
                    A collection of kubernetes yaml files
                which are deployed on a Workload
                Cluster. Hydrated Deployments are
                created by TNA intent based automation.

            """

            http_options = _BaseTelcoAutomationRestTransport._BaseGetHydratedDeployment._get_http_options()
            request, metadata = self._interceptor.pre_get_hydrated_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTelcoAutomationRestTransport._BaseGetHydratedDeployment,
                    "_BaseGetHydratedDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.telcoautomation_v1.TelcoAutomationClient.GetHydratedDeployment",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "GetHydratedDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                TelcoAutomationRestTransport._GetHydratedDeployment._get_response(
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
            resp = telcoautomation.HydratedDeployment()
            pb_resp = telcoautomation.HydratedDeployment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_hydrated_deployment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_hydrated_deployment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = telcoautomation.HydratedDeployment.to_json(
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
                    "Received response for google.cloud.telcoautomation_v1.TelcoAutomationClient.get_hydrated_deployment",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "GetHydratedDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetOrchestrationCluster(
        _BaseTelcoAutomationRestTransport._BaseGetOrchestrationCluster,
        TelcoAutomationRestStub,
    ):
        def __hash__(self):
            return hash("TelcoAutomationRestTransport.GetOrchestrationCluster")

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
            request: telcoautomation.GetOrchestrationClusterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> telcoautomation.OrchestrationCluster:
            r"""Call the get orchestration cluster method over HTTP.

            Args:
                request (~.telcoautomation.GetOrchestrationClusterRequest):
                    The request object. Message for getting a
                OrchestrationCluster.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.telcoautomation.OrchestrationCluster:
                    Orchestration cluster represents a
                GKE cluster with config controller and
                TNA specific components installed on it.

            """

            http_options = _BaseTelcoAutomationRestTransport._BaseGetOrchestrationCluster._get_http_options()
            request, metadata = self._interceptor.pre_get_orchestration_cluster(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTelcoAutomationRestTransport._BaseGetOrchestrationCluster,
                    "_BaseGetOrchestrationCluster__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.telcoautomation_v1.TelcoAutomationClient.GetOrchestrationCluster",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "GetOrchestrationCluster",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                TelcoAutomationRestTransport._GetOrchestrationCluster._get_response(
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
            resp = telcoautomation.OrchestrationCluster()
            pb_resp = telcoautomation.OrchestrationCluster.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_orchestration_cluster(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_orchestration_cluster_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = telcoautomation.OrchestrationCluster.to_json(
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
                    "Received response for google.cloud.telcoautomation_v1.TelcoAutomationClient.get_orchestration_cluster",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "GetOrchestrationCluster",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetPublicBlueprint(
        _BaseTelcoAutomationRestTransport._BaseGetPublicBlueprint,
        TelcoAutomationRestStub,
    ):
        def __hash__(self):
            return hash("TelcoAutomationRestTransport.GetPublicBlueprint")

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
            request: telcoautomation.GetPublicBlueprintRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> telcoautomation.PublicBlueprint:
            r"""Call the get public blueprint method over HTTP.

            Args:
                request (~.telcoautomation.GetPublicBlueprintRequest):
                    The request object. Request object for ``GetPublicBlueprint``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.telcoautomation.PublicBlueprint:
                    A Blueprint contains a collection of
                kubernetes resources in the form of YAML
                files. The file contents of a blueprint
                are collectively known as package.
                Public blueprint is a TNA provided
                blueprint that in present in TNA's
                public catalog. A user can copy the
                public blueprint to their private
                catalog for further modifications.

            """

            http_options = _BaseTelcoAutomationRestTransport._BaseGetPublicBlueprint._get_http_options()
            request, metadata = self._interceptor.pre_get_public_blueprint(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTelcoAutomationRestTransport._BaseGetPublicBlueprint,
                    "_BaseGetPublicBlueprint__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.telcoautomation_v1.TelcoAutomationClient.GetPublicBlueprint",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "GetPublicBlueprint",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TelcoAutomationRestTransport._GetPublicBlueprint._get_response(
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
            resp = telcoautomation.PublicBlueprint()
            pb_resp = telcoautomation.PublicBlueprint.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_public_blueprint(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_public_blueprint_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = telcoautomation.PublicBlueprint.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.telcoautomation_v1.TelcoAutomationClient.get_public_blueprint",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "GetPublicBlueprint",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListBlueprintRevisions(
        _BaseTelcoAutomationRestTransport._BaseListBlueprintRevisions,
        TelcoAutomationRestStub,
    ):
        def __hash__(self):
            return hash("TelcoAutomationRestTransport.ListBlueprintRevisions")

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
            request: telcoautomation.ListBlueprintRevisionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> telcoautomation.ListBlueprintRevisionsResponse:
            r"""Call the list blueprint revisions method over HTTP.

            Args:
                request (~.telcoautomation.ListBlueprintRevisionsRequest):
                    The request object. Request object for ``ListBlueprintRevisions``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.telcoautomation.ListBlueprintRevisionsResponse:
                    Response object for ``ListBlueprintRevisions``.
            """

            http_options = _BaseTelcoAutomationRestTransport._BaseListBlueprintRevisions._get_http_options()
            request, metadata = self._interceptor.pre_list_blueprint_revisions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTelcoAutomationRestTransport._BaseListBlueprintRevisions,
                    "_BaseListBlueprintRevisions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.telcoautomation_v1.TelcoAutomationClient.ListBlueprintRevisions",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "ListBlueprintRevisions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                TelcoAutomationRestTransport._ListBlueprintRevisions._get_response(
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
            resp = telcoautomation.ListBlueprintRevisionsResponse()
            pb_resp = telcoautomation.ListBlueprintRevisionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_blueprint_revisions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_blueprint_revisions_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        telcoautomation.ListBlueprintRevisionsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.telcoautomation_v1.TelcoAutomationClient.list_blueprint_revisions",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "ListBlueprintRevisions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListBlueprints(
        _BaseTelcoAutomationRestTransport._BaseListBlueprints, TelcoAutomationRestStub
    ):
        def __hash__(self):
            return hash("TelcoAutomationRestTransport.ListBlueprints")

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
            request: telcoautomation.ListBlueprintsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> telcoautomation.ListBlueprintsResponse:
            r"""Call the list blueprints method over HTTP.

            Args:
                request (~.telcoautomation.ListBlueprintsRequest):
                    The request object. Request object for ``ListBlueprints``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.telcoautomation.ListBlueprintsResponse:
                    Response object for ``ListBlueprints``.
            """

            http_options = _BaseTelcoAutomationRestTransport._BaseListBlueprints._get_http_options()
            request, metadata = self._interceptor.pre_list_blueprints(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTelcoAutomationRestTransport._BaseListBlueprints,
                    "_BaseListBlueprints__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.telcoautomation_v1.TelcoAutomationClient.ListBlueprints",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "ListBlueprints",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TelcoAutomationRestTransport._ListBlueprints._get_response(
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
            resp = telcoautomation.ListBlueprintsResponse()
            pb_resp = telcoautomation.ListBlueprintsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_blueprints(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_blueprints_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = telcoautomation.ListBlueprintsResponse.to_json(
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
                    "Received response for google.cloud.telcoautomation_v1.TelcoAutomationClient.list_blueprints",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "ListBlueprints",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDeploymentRevisions(
        _BaseTelcoAutomationRestTransport._BaseListDeploymentRevisions,
        TelcoAutomationRestStub,
    ):
        def __hash__(self):
            return hash("TelcoAutomationRestTransport.ListDeploymentRevisions")

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
            request: telcoautomation.ListDeploymentRevisionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> telcoautomation.ListDeploymentRevisionsResponse:
            r"""Call the list deployment revisions method over HTTP.

            Args:
                request (~.telcoautomation.ListDeploymentRevisionsRequest):
                    The request object. Request for listing all revisions of
                a deployment.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.telcoautomation.ListDeploymentRevisionsResponse:
                    List of deployment revisions for a
                given deployment.

            """

            http_options = _BaseTelcoAutomationRestTransport._BaseListDeploymentRevisions._get_http_options()
            request, metadata = self._interceptor.pre_list_deployment_revisions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTelcoAutomationRestTransport._BaseListDeploymentRevisions,
                    "_BaseListDeploymentRevisions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.telcoautomation_v1.TelcoAutomationClient.ListDeploymentRevisions",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "ListDeploymentRevisions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                TelcoAutomationRestTransport._ListDeploymentRevisions._get_response(
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
            resp = telcoautomation.ListDeploymentRevisionsResponse()
            pb_resp = telcoautomation.ListDeploymentRevisionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_deployment_revisions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_deployment_revisions_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        telcoautomation.ListDeploymentRevisionsResponse.to_json(
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
                    "Received response for google.cloud.telcoautomation_v1.TelcoAutomationClient.list_deployment_revisions",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "ListDeploymentRevisions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDeployments(
        _BaseTelcoAutomationRestTransport._BaseListDeployments, TelcoAutomationRestStub
    ):
        def __hash__(self):
            return hash("TelcoAutomationRestTransport.ListDeployments")

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
            request: telcoautomation.ListDeploymentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> telcoautomation.ListDeploymentsResponse:
            r"""Call the list deployments method over HTTP.

            Args:
                request (~.telcoautomation.ListDeploymentsRequest):
                    The request object. Request object for ``ListDeployments``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.telcoautomation.ListDeploymentsResponse:
                    Response object for ``ListDeployments``.
            """

            http_options = _BaseTelcoAutomationRestTransport._BaseListDeployments._get_http_options()
            request, metadata = self._interceptor.pre_list_deployments(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTelcoAutomationRestTransport._BaseListDeployments,
                    "_BaseListDeployments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.telcoautomation_v1.TelcoAutomationClient.ListDeployments",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "ListDeployments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TelcoAutomationRestTransport._ListDeployments._get_response(
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
            resp = telcoautomation.ListDeploymentsResponse()
            pb_resp = telcoautomation.ListDeploymentsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_deployments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_deployments_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = telcoautomation.ListDeploymentsResponse.to_json(
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
                    "Received response for google.cloud.telcoautomation_v1.TelcoAutomationClient.list_deployments",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "ListDeployments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListEdgeSlms(
        _BaseTelcoAutomationRestTransport._BaseListEdgeSlms, TelcoAutomationRestStub
    ):
        def __hash__(self):
            return hash("TelcoAutomationRestTransport.ListEdgeSlms")

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
            request: telcoautomation.ListEdgeSlmsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> telcoautomation.ListEdgeSlmsResponse:
            r"""Call the list edge slms method over HTTP.

            Args:
                request (~.telcoautomation.ListEdgeSlmsRequest):
                    The request object. Message for requesting list of
                EdgeSlms
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.telcoautomation.ListEdgeSlmsResponse:
                    Message for response to listing
                EdgeSlms.

            """

            http_options = (
                _BaseTelcoAutomationRestTransport._BaseListEdgeSlms._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_edge_slms(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTelcoAutomationRestTransport._BaseListEdgeSlms,
                    "_BaseListEdgeSlms__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.telcoautomation_v1.TelcoAutomationClient.ListEdgeSlms",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "ListEdgeSlms",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TelcoAutomationRestTransport._ListEdgeSlms._get_response(
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
            resp = telcoautomation.ListEdgeSlmsResponse()
            pb_resp = telcoautomation.ListEdgeSlmsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_edge_slms(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_edge_slms_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = telcoautomation.ListEdgeSlmsResponse.to_json(
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
                    "Received response for google.cloud.telcoautomation_v1.TelcoAutomationClient.list_edge_slms",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "ListEdgeSlms",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListHydratedDeployments(
        _BaseTelcoAutomationRestTransport._BaseListHydratedDeployments,
        TelcoAutomationRestStub,
    ):
        def __hash__(self):
            return hash("TelcoAutomationRestTransport.ListHydratedDeployments")

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
            request: telcoautomation.ListHydratedDeploymentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> telcoautomation.ListHydratedDeploymentsResponse:
            r"""Call the list hydrated deployments method over HTTP.

            Args:
                request (~.telcoautomation.ListHydratedDeploymentsRequest):
                    The request object. Request object for ``ListHydratedDeployments``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.telcoautomation.ListHydratedDeploymentsResponse:
                    Response object for ``ListHydratedDeployments``.
            """

            http_options = _BaseTelcoAutomationRestTransport._BaseListHydratedDeployments._get_http_options()
            request, metadata = self._interceptor.pre_list_hydrated_deployments(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTelcoAutomationRestTransport._BaseListHydratedDeployments,
                    "_BaseListHydratedDeployments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.telcoautomation_v1.TelcoAutomationClient.ListHydratedDeployments",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "ListHydratedDeployments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                TelcoAutomationRestTransport._ListHydratedDeployments._get_response(
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
            resp = telcoautomation.ListHydratedDeploymentsResponse()
            pb_resp = telcoautomation.ListHydratedDeploymentsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_hydrated_deployments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_hydrated_deployments_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        telcoautomation.ListHydratedDeploymentsResponse.to_json(
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
                    "Received response for google.cloud.telcoautomation_v1.TelcoAutomationClient.list_hydrated_deployments",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "ListHydratedDeployments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListOrchestrationClusters(
        _BaseTelcoAutomationRestTransport._BaseListOrchestrationClusters,
        TelcoAutomationRestStub,
    ):
        def __hash__(self):
            return hash("TelcoAutomationRestTransport.ListOrchestrationClusters")

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
            request: telcoautomation.ListOrchestrationClustersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> telcoautomation.ListOrchestrationClustersResponse:
            r"""Call the list orchestration
            clusters method over HTTP.

                Args:
                    request (~.telcoautomation.ListOrchestrationClustersRequest):
                        The request object. Message for requesting list of
                    OrchestrationClusters.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.telcoautomation.ListOrchestrationClustersResponse:
                        Message for response to listing
                    OrchestrationClusters.

            """

            http_options = _BaseTelcoAutomationRestTransport._BaseListOrchestrationClusters._get_http_options()
            request, metadata = self._interceptor.pre_list_orchestration_clusters(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTelcoAutomationRestTransport._BaseListOrchestrationClusters,
                    "_BaseListOrchestrationClusters__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.telcoautomation_v1.TelcoAutomationClient.ListOrchestrationClusters",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "ListOrchestrationClusters",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                TelcoAutomationRestTransport._ListOrchestrationClusters._get_response(
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
            resp = telcoautomation.ListOrchestrationClustersResponse()
            pb_resp = telcoautomation.ListOrchestrationClustersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_orchestration_clusters(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_orchestration_clusters_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        telcoautomation.ListOrchestrationClustersResponse.to_json(
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
                    "Received response for google.cloud.telcoautomation_v1.TelcoAutomationClient.list_orchestration_clusters",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "ListOrchestrationClusters",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListPublicBlueprints(
        _BaseTelcoAutomationRestTransport._BaseListPublicBlueprints,
        TelcoAutomationRestStub,
    ):
        def __hash__(self):
            return hash("TelcoAutomationRestTransport.ListPublicBlueprints")

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
            request: telcoautomation.ListPublicBlueprintsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> telcoautomation.ListPublicBlueprintsResponse:
            r"""Call the list public blueprints method over HTTP.

            Args:
                request (~.telcoautomation.ListPublicBlueprintsRequest):
                    The request object. Request object for ``ListPublicBlueprints``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.telcoautomation.ListPublicBlueprintsResponse:
                    Response object for ``ListPublicBlueprints``.
            """

            http_options = _BaseTelcoAutomationRestTransport._BaseListPublicBlueprints._get_http_options()
            request, metadata = self._interceptor.pre_list_public_blueprints(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTelcoAutomationRestTransport._BaseListPublicBlueprints,
                    "_BaseListPublicBlueprints__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.telcoautomation_v1.TelcoAutomationClient.ListPublicBlueprints",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "ListPublicBlueprints",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TelcoAutomationRestTransport._ListPublicBlueprints._get_response(
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
            resp = telcoautomation.ListPublicBlueprintsResponse()
            pb_resp = telcoautomation.ListPublicBlueprintsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_public_blueprints(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_public_blueprints_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        telcoautomation.ListPublicBlueprintsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.telcoautomation_v1.TelcoAutomationClient.list_public_blueprints",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "ListPublicBlueprints",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ProposeBlueprint(
        _BaseTelcoAutomationRestTransport._BaseProposeBlueprint, TelcoAutomationRestStub
    ):
        def __hash__(self):
            return hash("TelcoAutomationRestTransport.ProposeBlueprint")

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
            request: telcoautomation.ProposeBlueprintRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> telcoautomation.Blueprint:
            r"""Call the propose blueprint method over HTTP.

            Args:
                request (~.telcoautomation.ProposeBlueprintRequest):
                    The request object. Request object for ``ProposeBlueprint``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.telcoautomation.Blueprint:
                    A Blueprint contains a collection of
                kubernetes resources in the form of YAML
                files. The file contents of a blueprint
                are collectively known as package. A
                blueprint can be
                a) imported from TNA's public catalog
                b) modified as per a user's need
                c) proposed and approved.
                On approval, a revision of blueprint is
                created which can be used to create a
                deployment on Orchestration or Workload
                Cluster.

            """

            http_options = _BaseTelcoAutomationRestTransport._BaseProposeBlueprint._get_http_options()
            request, metadata = self._interceptor.pre_propose_blueprint(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTelcoAutomationRestTransport._BaseProposeBlueprint,
                    "_BaseProposeBlueprint__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.telcoautomation_v1.TelcoAutomationClient.ProposeBlueprint",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "ProposeBlueprint",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TelcoAutomationRestTransport._ProposeBlueprint._get_response(
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
            resp = telcoautomation.Blueprint()
            pb_resp = telcoautomation.Blueprint.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_propose_blueprint(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_propose_blueprint_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = telcoautomation.Blueprint.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.telcoautomation_v1.TelcoAutomationClient.propose_blueprint",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "ProposeBlueprint",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RejectBlueprint(
        _BaseTelcoAutomationRestTransport._BaseRejectBlueprint, TelcoAutomationRestStub
    ):
        def __hash__(self):
            return hash("TelcoAutomationRestTransport.RejectBlueprint")

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
            request: telcoautomation.RejectBlueprintRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> telcoautomation.Blueprint:
            r"""Call the reject blueprint method over HTTP.

            Args:
                request (~.telcoautomation.RejectBlueprintRequest):
                    The request object. Request object for ``RejectBlueprint``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.telcoautomation.Blueprint:
                    A Blueprint contains a collection of
                kubernetes resources in the form of YAML
                files. The file contents of a blueprint
                are collectively known as package. A
                blueprint can be
                a) imported from TNA's public catalog
                b) modified as per a user's need
                c) proposed and approved.
                On approval, a revision of blueprint is
                created which can be used to create a
                deployment on Orchestration or Workload
                Cluster.

            """

            http_options = _BaseTelcoAutomationRestTransport._BaseRejectBlueprint._get_http_options()
            request, metadata = self._interceptor.pre_reject_blueprint(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTelcoAutomationRestTransport._BaseRejectBlueprint,
                    "_BaseRejectBlueprint__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.telcoautomation_v1.TelcoAutomationClient.RejectBlueprint",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "RejectBlueprint",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TelcoAutomationRestTransport._RejectBlueprint._get_response(
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
            resp = telcoautomation.Blueprint()
            pb_resp = telcoautomation.Blueprint.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_reject_blueprint(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_reject_blueprint_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = telcoautomation.Blueprint.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.telcoautomation_v1.TelcoAutomationClient.reject_blueprint",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "RejectBlueprint",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RemoveDeployment(
        _BaseTelcoAutomationRestTransport._BaseRemoveDeployment, TelcoAutomationRestStub
    ):
        def __hash__(self):
            return hash("TelcoAutomationRestTransport.RemoveDeployment")

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
            request: telcoautomation.RemoveDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the remove deployment method over HTTP.

            Args:
                request (~.telcoautomation.RemoveDeploymentRequest):
                    The request object. Request object for ``RemoveDeployment``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseTelcoAutomationRestTransport._BaseRemoveDeployment._get_http_options()
            request, metadata = self._interceptor.pre_remove_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTelcoAutomationRestTransport._BaseRemoveDeployment,
                    "_BaseRemoveDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.telcoautomation_v1.TelcoAutomationClient.RemoveDeployment",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "RemoveDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TelcoAutomationRestTransport._RemoveDeployment._get_response(
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

    class _RollbackDeployment(
        _BaseTelcoAutomationRestTransport._BaseRollbackDeployment,
        TelcoAutomationRestStub,
    ):
        def __hash__(self):
            return hash("TelcoAutomationRestTransport.RollbackDeployment")

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
            request: telcoautomation.RollbackDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> telcoautomation.Deployment:
            r"""Call the rollback deployment method over HTTP.

            Args:
                request (~.telcoautomation.RollbackDeploymentRequest):
                    The request object. Request object for ``RollbackDeployment``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.telcoautomation.Deployment:
                    Deployment contains a collection of
                YAML files (This collection is also
                known as package) that can to applied on
                an orchestration cluster (GKE cluster
                with TNA addons) or a workload cluster.

            """

            http_options = _BaseTelcoAutomationRestTransport._BaseRollbackDeployment._get_http_options()
            request, metadata = self._interceptor.pre_rollback_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTelcoAutomationRestTransport._BaseRollbackDeployment,
                    "_BaseRollbackDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.telcoautomation_v1.TelcoAutomationClient.RollbackDeployment",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "RollbackDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TelcoAutomationRestTransport._RollbackDeployment._get_response(
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
            resp = telcoautomation.Deployment()
            pb_resp = telcoautomation.Deployment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_rollback_deployment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_rollback_deployment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = telcoautomation.Deployment.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.telcoautomation_v1.TelcoAutomationClient.rollback_deployment",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "RollbackDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SearchBlueprintRevisions(
        _BaseTelcoAutomationRestTransport._BaseSearchBlueprintRevisions,
        TelcoAutomationRestStub,
    ):
        def __hash__(self):
            return hash("TelcoAutomationRestTransport.SearchBlueprintRevisions")

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
            request: telcoautomation.SearchBlueprintRevisionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> telcoautomation.SearchBlueprintRevisionsResponse:
            r"""Call the search blueprint
            revisions method over HTTP.

                Args:
                    request (~.telcoautomation.SearchBlueprintRevisionsRequest):
                        The request object. Request object for ``SearchBlueprintRevisions``.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.telcoautomation.SearchBlueprintRevisionsResponse:
                        Response object for ``SearchBlueprintRevisions``.
            """

            http_options = _BaseTelcoAutomationRestTransport._BaseSearchBlueprintRevisions._get_http_options()
            request, metadata = self._interceptor.pre_search_blueprint_revisions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTelcoAutomationRestTransport._BaseSearchBlueprintRevisions,
                    "_BaseSearchBlueprintRevisions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.telcoautomation_v1.TelcoAutomationClient.SearchBlueprintRevisions",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "SearchBlueprintRevisions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                TelcoAutomationRestTransport._SearchBlueprintRevisions._get_response(
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
            resp = telcoautomation.SearchBlueprintRevisionsResponse()
            pb_resp = telcoautomation.SearchBlueprintRevisionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_search_blueprint_revisions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_search_blueprint_revisions_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        telcoautomation.SearchBlueprintRevisionsResponse.to_json(
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
                    "Received response for google.cloud.telcoautomation_v1.TelcoAutomationClient.search_blueprint_revisions",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "SearchBlueprintRevisions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SearchDeploymentRevisions(
        _BaseTelcoAutomationRestTransport._BaseSearchDeploymentRevisions,
        TelcoAutomationRestStub,
    ):
        def __hash__(self):
            return hash("TelcoAutomationRestTransport.SearchDeploymentRevisions")

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
            request: telcoautomation.SearchDeploymentRevisionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> telcoautomation.SearchDeploymentRevisionsResponse:
            r"""Call the search deployment
            revisions method over HTTP.

                Args:
                    request (~.telcoautomation.SearchDeploymentRevisionsRequest):
                        The request object. Request object for ``SearchDeploymentRevisions``.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.telcoautomation.SearchDeploymentRevisionsResponse:
                        Response object for ``SearchDeploymentRevisions``.
            """

            http_options = _BaseTelcoAutomationRestTransport._BaseSearchDeploymentRevisions._get_http_options()
            request, metadata = self._interceptor.pre_search_deployment_revisions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTelcoAutomationRestTransport._BaseSearchDeploymentRevisions,
                    "_BaseSearchDeploymentRevisions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.telcoautomation_v1.TelcoAutomationClient.SearchDeploymentRevisions",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "SearchDeploymentRevisions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                TelcoAutomationRestTransport._SearchDeploymentRevisions._get_response(
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
            resp = telcoautomation.SearchDeploymentRevisionsResponse()
            pb_resp = telcoautomation.SearchDeploymentRevisionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_search_deployment_revisions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_search_deployment_revisions_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        telcoautomation.SearchDeploymentRevisionsResponse.to_json(
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
                    "Received response for google.cloud.telcoautomation_v1.TelcoAutomationClient.search_deployment_revisions",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "SearchDeploymentRevisions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateBlueprint(
        _BaseTelcoAutomationRestTransport._BaseUpdateBlueprint, TelcoAutomationRestStub
    ):
        def __hash__(self):
            return hash("TelcoAutomationRestTransport.UpdateBlueprint")

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
            request: telcoautomation.UpdateBlueprintRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> telcoautomation.Blueprint:
            r"""Call the update blueprint method over HTTP.

            Args:
                request (~.telcoautomation.UpdateBlueprintRequest):
                    The request object. Request object for ``UpdateBlueprint``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.telcoautomation.Blueprint:
                    A Blueprint contains a collection of
                kubernetes resources in the form of YAML
                files. The file contents of a blueprint
                are collectively known as package. A
                blueprint can be
                a) imported from TNA's public catalog
                b) modified as per a user's need
                c) proposed and approved.
                On approval, a revision of blueprint is
                created which can be used to create a
                deployment on Orchestration or Workload
                Cluster.

            """

            http_options = _BaseTelcoAutomationRestTransport._BaseUpdateBlueprint._get_http_options()
            request, metadata = self._interceptor.pre_update_blueprint(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTelcoAutomationRestTransport._BaseUpdateBlueprint,
                    "_BaseUpdateBlueprint__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.telcoautomation_v1.TelcoAutomationClient.UpdateBlueprint",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "UpdateBlueprint",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TelcoAutomationRestTransport._UpdateBlueprint._get_response(
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
            resp = telcoautomation.Blueprint()
            pb_resp = telcoautomation.Blueprint.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_blueprint(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_blueprint_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = telcoautomation.Blueprint.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.telcoautomation_v1.TelcoAutomationClient.update_blueprint",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "UpdateBlueprint",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateDeployment(
        _BaseTelcoAutomationRestTransport._BaseUpdateDeployment, TelcoAutomationRestStub
    ):
        def __hash__(self):
            return hash("TelcoAutomationRestTransport.UpdateDeployment")

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
            request: telcoautomation.UpdateDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> telcoautomation.Deployment:
            r"""Call the update deployment method over HTTP.

            Args:
                request (~.telcoautomation.UpdateDeploymentRequest):
                    The request object. Request object for ``UpdateDeployment``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.telcoautomation.Deployment:
                    Deployment contains a collection of
                YAML files (This collection is also
                known as package) that can to applied on
                an orchestration cluster (GKE cluster
                with TNA addons) or a workload cluster.

            """

            http_options = _BaseTelcoAutomationRestTransport._BaseUpdateDeployment._get_http_options()
            request, metadata = self._interceptor.pre_update_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTelcoAutomationRestTransport._BaseUpdateDeployment,
                    "_BaseUpdateDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.telcoautomation_v1.TelcoAutomationClient.UpdateDeployment",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "UpdateDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TelcoAutomationRestTransport._UpdateDeployment._get_response(
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
            resp = telcoautomation.Deployment()
            pb_resp = telcoautomation.Deployment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_deployment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_deployment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = telcoautomation.Deployment.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.telcoautomation_v1.TelcoAutomationClient.update_deployment",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "UpdateDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateHydratedDeployment(
        _BaseTelcoAutomationRestTransport._BaseUpdateHydratedDeployment,
        TelcoAutomationRestStub,
    ):
        def __hash__(self):
            return hash("TelcoAutomationRestTransport.UpdateHydratedDeployment")

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
            request: telcoautomation.UpdateHydratedDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> telcoautomation.HydratedDeployment:
            r"""Call the update hydrated
            deployment method over HTTP.

                Args:
                    request (~.telcoautomation.UpdateHydratedDeploymentRequest):
                        The request object. Request object for ``UpdateHydratedDeployment``.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.telcoautomation.HydratedDeployment:
                        A collection of kubernetes yaml files
                    which are deployed on a Workload
                    Cluster. Hydrated Deployments are
                    created by TNA intent based automation.

            """

            http_options = _BaseTelcoAutomationRestTransport._BaseUpdateHydratedDeployment._get_http_options()
            request, metadata = self._interceptor.pre_update_hydrated_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTelcoAutomationRestTransport._BaseUpdateHydratedDeployment,
                    "_BaseUpdateHydratedDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.telcoautomation_v1.TelcoAutomationClient.UpdateHydratedDeployment",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "UpdateHydratedDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                TelcoAutomationRestTransport._UpdateHydratedDeployment._get_response(
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
            resp = telcoautomation.HydratedDeployment()
            pb_resp = telcoautomation.HydratedDeployment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_hydrated_deployment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_hydrated_deployment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = telcoautomation.HydratedDeployment.to_json(
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
                    "Received response for google.cloud.telcoautomation_v1.TelcoAutomationClient.update_hydrated_deployment",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "UpdateHydratedDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def apply_deployment(
        self,
    ) -> Callable[[telcoautomation.ApplyDeploymentRequest], telcoautomation.Deployment]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ApplyDeployment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def apply_hydrated_deployment(
        self,
    ) -> Callable[
        [telcoautomation.ApplyHydratedDeploymentRequest],
        telcoautomation.HydratedDeployment,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ApplyHydratedDeployment(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def approve_blueprint(
        self,
    ) -> Callable[[telcoautomation.ApproveBlueprintRequest], telcoautomation.Blueprint]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ApproveBlueprint(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def compute_deployment_status(
        self,
    ) -> Callable[
        [telcoautomation.ComputeDeploymentStatusRequest],
        telcoautomation.ComputeDeploymentStatusResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ComputeDeploymentStatus(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_blueprint(
        self,
    ) -> Callable[[telcoautomation.CreateBlueprintRequest], telcoautomation.Blueprint]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateBlueprint(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_deployment(
        self,
    ) -> Callable[
        [telcoautomation.CreateDeploymentRequest], telcoautomation.Deployment
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateDeployment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_edge_slm(
        self,
    ) -> Callable[[telcoautomation.CreateEdgeSlmRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateEdgeSlm(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_orchestration_cluster(
        self,
    ) -> Callable[
        [telcoautomation.CreateOrchestrationClusterRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateOrchestrationCluster(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_blueprint(
        self,
    ) -> Callable[[telcoautomation.DeleteBlueprintRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteBlueprint(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_edge_slm(
        self,
    ) -> Callable[[telcoautomation.DeleteEdgeSlmRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteEdgeSlm(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_orchestration_cluster(
        self,
    ) -> Callable[
        [telcoautomation.DeleteOrchestrationClusterRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteOrchestrationCluster(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def discard_blueprint_changes(
        self,
    ) -> Callable[
        [telcoautomation.DiscardBlueprintChangesRequest],
        telcoautomation.DiscardBlueprintChangesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DiscardBlueprintChanges(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def discard_deployment_changes(
        self,
    ) -> Callable[
        [telcoautomation.DiscardDeploymentChangesRequest],
        telcoautomation.DiscardDeploymentChangesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DiscardDeploymentChanges(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_blueprint(
        self,
    ) -> Callable[[telcoautomation.GetBlueprintRequest], telcoautomation.Blueprint]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetBlueprint(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_deployment(
        self,
    ) -> Callable[[telcoautomation.GetDeploymentRequest], telcoautomation.Deployment]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDeployment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_edge_slm(
        self,
    ) -> Callable[[telcoautomation.GetEdgeSlmRequest], telcoautomation.EdgeSlm]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetEdgeSlm(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_hydrated_deployment(
        self,
    ) -> Callable[
        [telcoautomation.GetHydratedDeploymentRequest],
        telcoautomation.HydratedDeployment,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetHydratedDeployment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_orchestration_cluster(
        self,
    ) -> Callable[
        [telcoautomation.GetOrchestrationClusterRequest],
        telcoautomation.OrchestrationCluster,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetOrchestrationCluster(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_public_blueprint(
        self,
    ) -> Callable[
        [telcoautomation.GetPublicBlueprintRequest], telcoautomation.PublicBlueprint
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetPublicBlueprint(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_blueprint_revisions(
        self,
    ) -> Callable[
        [telcoautomation.ListBlueprintRevisionsRequest],
        telcoautomation.ListBlueprintRevisionsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListBlueprintRevisions(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_blueprints(
        self,
    ) -> Callable[
        [telcoautomation.ListBlueprintsRequest], telcoautomation.ListBlueprintsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListBlueprints(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_deployment_revisions(
        self,
    ) -> Callable[
        [telcoautomation.ListDeploymentRevisionsRequest],
        telcoautomation.ListDeploymentRevisionsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDeploymentRevisions(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_deployments(
        self,
    ) -> Callable[
        [telcoautomation.ListDeploymentsRequest],
        telcoautomation.ListDeploymentsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDeployments(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_edge_slms(
        self,
    ) -> Callable[
        [telcoautomation.ListEdgeSlmsRequest], telcoautomation.ListEdgeSlmsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListEdgeSlms(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_hydrated_deployments(
        self,
    ) -> Callable[
        [telcoautomation.ListHydratedDeploymentsRequest],
        telcoautomation.ListHydratedDeploymentsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListHydratedDeployments(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_orchestration_clusters(
        self,
    ) -> Callable[
        [telcoautomation.ListOrchestrationClustersRequest],
        telcoautomation.ListOrchestrationClustersResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListOrchestrationClusters(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_public_blueprints(
        self,
    ) -> Callable[
        [telcoautomation.ListPublicBlueprintsRequest],
        telcoautomation.ListPublicBlueprintsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListPublicBlueprints(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def propose_blueprint(
        self,
    ) -> Callable[[telcoautomation.ProposeBlueprintRequest], telcoautomation.Blueprint]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ProposeBlueprint(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def reject_blueprint(
        self,
    ) -> Callable[[telcoautomation.RejectBlueprintRequest], telcoautomation.Blueprint]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RejectBlueprint(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def remove_deployment(
        self,
    ) -> Callable[[telcoautomation.RemoveDeploymentRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RemoveDeployment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def rollback_deployment(
        self,
    ) -> Callable[
        [telcoautomation.RollbackDeploymentRequest], telcoautomation.Deployment
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RollbackDeployment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def search_blueprint_revisions(
        self,
    ) -> Callable[
        [telcoautomation.SearchBlueprintRevisionsRequest],
        telcoautomation.SearchBlueprintRevisionsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SearchBlueprintRevisions(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def search_deployment_revisions(
        self,
    ) -> Callable[
        [telcoautomation.SearchDeploymentRevisionsRequest],
        telcoautomation.SearchDeploymentRevisionsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SearchDeploymentRevisions(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_blueprint(
        self,
    ) -> Callable[[telcoautomation.UpdateBlueprintRequest], telcoautomation.Blueprint]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateBlueprint(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_deployment(
        self,
    ) -> Callable[
        [telcoautomation.UpdateDeploymentRequest], telcoautomation.Deployment
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateDeployment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_hydrated_deployment(
        self,
    ) -> Callable[
        [telcoautomation.UpdateHydratedDeploymentRequest],
        telcoautomation.HydratedDeployment,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateHydratedDeployment(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseTelcoAutomationRestTransport._BaseGetLocation, TelcoAutomationRestStub
    ):
        def __hash__(self):
            return hash("TelcoAutomationRestTransport.GetLocation")

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
                _BaseTelcoAutomationRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTelcoAutomationRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.telcoautomation_v1.TelcoAutomationClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TelcoAutomationRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.telcoautomation_v1.TelcoAutomationAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
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
        _BaseTelcoAutomationRestTransport._BaseListLocations, TelcoAutomationRestStub
    ):
        def __hash__(self):
            return hash("TelcoAutomationRestTransport.ListLocations")

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
                _BaseTelcoAutomationRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTelcoAutomationRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.telcoautomation_v1.TelcoAutomationClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TelcoAutomationRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.telcoautomation_v1.TelcoAutomationAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
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
        _BaseTelcoAutomationRestTransport._BaseCancelOperation, TelcoAutomationRestStub
    ):
        def __hash__(self):
            return hash("TelcoAutomationRestTransport.CancelOperation")

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

            http_options = _BaseTelcoAutomationRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTelcoAutomationRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.telcoautomation_v1.TelcoAutomationClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TelcoAutomationRestTransport._CancelOperation._get_response(
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
        _BaseTelcoAutomationRestTransport._BaseDeleteOperation, TelcoAutomationRestStub
    ):
        def __hash__(self):
            return hash("TelcoAutomationRestTransport.DeleteOperation")

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

            http_options = _BaseTelcoAutomationRestTransport._BaseDeleteOperation._get_http_options()
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTelcoAutomationRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.telcoautomation_v1.TelcoAutomationClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TelcoAutomationRestTransport._DeleteOperation._get_response(
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
        _BaseTelcoAutomationRestTransport._BaseGetOperation, TelcoAutomationRestStub
    ):
        def __hash__(self):
            return hash("TelcoAutomationRestTransport.GetOperation")

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
                _BaseTelcoAutomationRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTelcoAutomationRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.telcoautomation_v1.TelcoAutomationClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TelcoAutomationRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.telcoautomation_v1.TelcoAutomationAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
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
        _BaseTelcoAutomationRestTransport._BaseListOperations, TelcoAutomationRestStub
    ):
        def __hash__(self):
            return hash("TelcoAutomationRestTransport.ListOperations")

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

            http_options = _BaseTelcoAutomationRestTransport._BaseListOperations._get_http_options()
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTelcoAutomationRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.telcoautomation_v1.TelcoAutomationClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TelcoAutomationRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.telcoautomation_v1.TelcoAutomationAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
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


__all__ = ("TelcoAutomationRestTransport",)
