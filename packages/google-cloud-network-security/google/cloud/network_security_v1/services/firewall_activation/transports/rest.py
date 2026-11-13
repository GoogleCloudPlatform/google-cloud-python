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
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.network_security_v1._compat import transcode_request
from google.cloud.network_security_v1.types import firewall_activation

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseFirewallActivationRestTransport

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


class FirewallActivationRestInterceptor:
    """Interceptor for FirewallActivation.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the FirewallActivationRestTransport.

    .. code-block:: python
        class MyCustomFirewallActivationInterceptor(FirewallActivationRestInterceptor):
            def pre_create_firewall_endpoint(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_firewall_endpoint(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_firewall_endpoint_association(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_firewall_endpoint_association(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_project_firewall_endpoint(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_project_firewall_endpoint(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_firewall_endpoint(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_firewall_endpoint(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_firewall_endpoint_association(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_firewall_endpoint_association(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_project_firewall_endpoint(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_project_firewall_endpoint(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_firewall_endpoint(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_firewall_endpoint(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_firewall_endpoint_association(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_firewall_endpoint_association(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_project_firewall_endpoint(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_project_firewall_endpoint(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_firewall_endpoint_associations(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_firewall_endpoint_associations(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_firewall_endpoints(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_firewall_endpoints(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_project_firewall_endpoints(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_project_firewall_endpoints(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_firewall_endpoint(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_firewall_endpoint(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_firewall_endpoint_association(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_firewall_endpoint_association(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_project_firewall_endpoint(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_project_firewall_endpoint(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = FirewallActivationRestTransport(interceptor=MyCustomFirewallActivationInterceptor())
        client = FirewallActivationClient(transport=transport)


    """

    def pre_create_firewall_endpoint(
        self,
        request: firewall_activation.CreateFirewallEndpointRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        firewall_activation.CreateFirewallEndpointRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_firewall_endpoint

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FirewallActivation server.
        """
        return request, metadata

    def post_create_firewall_endpoint(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_firewall_endpoint

        DEPRECATED. Please use the `post_create_firewall_endpoint_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the FirewallActivation server but before
        it is returned to user code. This `post_create_firewall_endpoint` interceptor runs
        before the `post_create_firewall_endpoint_with_metadata` interceptor.
        """
        return response

    def post_create_firewall_endpoint_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_firewall_endpoint

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the FirewallActivation server but before it is returned to user code.

        We recommend only using this `post_create_firewall_endpoint_with_metadata`
        interceptor in new development instead of the `post_create_firewall_endpoint` interceptor.
        When both interceptors are used, this `post_create_firewall_endpoint_with_metadata` interceptor runs after the
        `post_create_firewall_endpoint` interceptor. The (possibly modified) response returned by
        `post_create_firewall_endpoint` will be passed to
        `post_create_firewall_endpoint_with_metadata`.
        """
        return response, metadata

    def pre_create_firewall_endpoint_association(
        self,
        request: firewall_activation.CreateFirewallEndpointAssociationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        firewall_activation.CreateFirewallEndpointAssociationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_firewall_endpoint_association

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FirewallActivation server.
        """
        return request, metadata

    def post_create_firewall_endpoint_association(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_firewall_endpoint_association

        DEPRECATED. Please use the `post_create_firewall_endpoint_association_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the FirewallActivation server but before
        it is returned to user code. This `post_create_firewall_endpoint_association` interceptor runs
        before the `post_create_firewall_endpoint_association_with_metadata` interceptor.
        """
        return response

    def post_create_firewall_endpoint_association_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_firewall_endpoint_association

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the FirewallActivation server but before it is returned to user code.

        We recommend only using this `post_create_firewall_endpoint_association_with_metadata`
        interceptor in new development instead of the `post_create_firewall_endpoint_association` interceptor.
        When both interceptors are used, this `post_create_firewall_endpoint_association_with_metadata` interceptor runs after the
        `post_create_firewall_endpoint_association` interceptor. The (possibly modified) response returned by
        `post_create_firewall_endpoint_association` will be passed to
        `post_create_firewall_endpoint_association_with_metadata`.
        """
        return response, metadata

    def pre_create_project_firewall_endpoint(
        self,
        request: firewall_activation.CreateFirewallEndpointRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        firewall_activation.CreateFirewallEndpointRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_project_firewall_endpoint

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FirewallActivation server.
        """
        return request, metadata

    def post_create_project_firewall_endpoint(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_project_firewall_endpoint

        DEPRECATED. Please use the `post_create_project_firewall_endpoint_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the FirewallActivation server but before
        it is returned to user code. This `post_create_project_firewall_endpoint` interceptor runs
        before the `post_create_project_firewall_endpoint_with_metadata` interceptor.
        """
        return response

    def post_create_project_firewall_endpoint_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_project_firewall_endpoint

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the FirewallActivation server but before it is returned to user code.

        We recommend only using this `post_create_project_firewall_endpoint_with_metadata`
        interceptor in new development instead of the `post_create_project_firewall_endpoint` interceptor.
        When both interceptors are used, this `post_create_project_firewall_endpoint_with_metadata` interceptor runs after the
        `post_create_project_firewall_endpoint` interceptor. The (possibly modified) response returned by
        `post_create_project_firewall_endpoint` will be passed to
        `post_create_project_firewall_endpoint_with_metadata`.
        """
        return response, metadata

    def pre_delete_firewall_endpoint(
        self,
        request: firewall_activation.DeleteFirewallEndpointRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        firewall_activation.DeleteFirewallEndpointRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_firewall_endpoint

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FirewallActivation server.
        """
        return request, metadata

    def post_delete_firewall_endpoint(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_firewall_endpoint

        DEPRECATED. Please use the `post_delete_firewall_endpoint_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the FirewallActivation server but before
        it is returned to user code. This `post_delete_firewall_endpoint` interceptor runs
        before the `post_delete_firewall_endpoint_with_metadata` interceptor.
        """
        return response

    def post_delete_firewall_endpoint_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_firewall_endpoint

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the FirewallActivation server but before it is returned to user code.

        We recommend only using this `post_delete_firewall_endpoint_with_metadata`
        interceptor in new development instead of the `post_delete_firewall_endpoint` interceptor.
        When both interceptors are used, this `post_delete_firewall_endpoint_with_metadata` interceptor runs after the
        `post_delete_firewall_endpoint` interceptor. The (possibly modified) response returned by
        `post_delete_firewall_endpoint` will be passed to
        `post_delete_firewall_endpoint_with_metadata`.
        """
        return response, metadata

    def pre_delete_firewall_endpoint_association(
        self,
        request: firewall_activation.DeleteFirewallEndpointAssociationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        firewall_activation.DeleteFirewallEndpointAssociationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_firewall_endpoint_association

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FirewallActivation server.
        """
        return request, metadata

    def post_delete_firewall_endpoint_association(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_firewall_endpoint_association

        DEPRECATED. Please use the `post_delete_firewall_endpoint_association_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the FirewallActivation server but before
        it is returned to user code. This `post_delete_firewall_endpoint_association` interceptor runs
        before the `post_delete_firewall_endpoint_association_with_metadata` interceptor.
        """
        return response

    def post_delete_firewall_endpoint_association_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_firewall_endpoint_association

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the FirewallActivation server but before it is returned to user code.

        We recommend only using this `post_delete_firewall_endpoint_association_with_metadata`
        interceptor in new development instead of the `post_delete_firewall_endpoint_association` interceptor.
        When both interceptors are used, this `post_delete_firewall_endpoint_association_with_metadata` interceptor runs after the
        `post_delete_firewall_endpoint_association` interceptor. The (possibly modified) response returned by
        `post_delete_firewall_endpoint_association` will be passed to
        `post_delete_firewall_endpoint_association_with_metadata`.
        """
        return response, metadata

    def pre_delete_project_firewall_endpoint(
        self,
        request: firewall_activation.DeleteFirewallEndpointRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        firewall_activation.DeleteFirewallEndpointRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_project_firewall_endpoint

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FirewallActivation server.
        """
        return request, metadata

    def post_delete_project_firewall_endpoint(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_project_firewall_endpoint

        DEPRECATED. Please use the `post_delete_project_firewall_endpoint_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the FirewallActivation server but before
        it is returned to user code. This `post_delete_project_firewall_endpoint` interceptor runs
        before the `post_delete_project_firewall_endpoint_with_metadata` interceptor.
        """
        return response

    def post_delete_project_firewall_endpoint_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_project_firewall_endpoint

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the FirewallActivation server but before it is returned to user code.

        We recommend only using this `post_delete_project_firewall_endpoint_with_metadata`
        interceptor in new development instead of the `post_delete_project_firewall_endpoint` interceptor.
        When both interceptors are used, this `post_delete_project_firewall_endpoint_with_metadata` interceptor runs after the
        `post_delete_project_firewall_endpoint` interceptor. The (possibly modified) response returned by
        `post_delete_project_firewall_endpoint` will be passed to
        `post_delete_project_firewall_endpoint_with_metadata`.
        """
        return response, metadata

    def pre_get_firewall_endpoint(
        self,
        request: firewall_activation.GetFirewallEndpointRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        firewall_activation.GetFirewallEndpointRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_firewall_endpoint

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FirewallActivation server.
        """
        return request, metadata

    def post_get_firewall_endpoint(
        self, response: firewall_activation.FirewallEndpoint
    ) -> firewall_activation.FirewallEndpoint:
        """Post-rpc interceptor for get_firewall_endpoint

        DEPRECATED. Please use the `post_get_firewall_endpoint_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the FirewallActivation server but before
        it is returned to user code. This `post_get_firewall_endpoint` interceptor runs
        before the `post_get_firewall_endpoint_with_metadata` interceptor.
        """
        return response

    def post_get_firewall_endpoint_with_metadata(
        self,
        response: firewall_activation.FirewallEndpoint,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        firewall_activation.FirewallEndpoint, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_firewall_endpoint

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the FirewallActivation server but before it is returned to user code.

        We recommend only using this `post_get_firewall_endpoint_with_metadata`
        interceptor in new development instead of the `post_get_firewall_endpoint` interceptor.
        When both interceptors are used, this `post_get_firewall_endpoint_with_metadata` interceptor runs after the
        `post_get_firewall_endpoint` interceptor. The (possibly modified) response returned by
        `post_get_firewall_endpoint` will be passed to
        `post_get_firewall_endpoint_with_metadata`.
        """
        return response, metadata

    def pre_get_firewall_endpoint_association(
        self,
        request: firewall_activation.GetFirewallEndpointAssociationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        firewall_activation.GetFirewallEndpointAssociationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_firewall_endpoint_association

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FirewallActivation server.
        """
        return request, metadata

    def post_get_firewall_endpoint_association(
        self, response: firewall_activation.FirewallEndpointAssociation
    ) -> firewall_activation.FirewallEndpointAssociation:
        """Post-rpc interceptor for get_firewall_endpoint_association

        DEPRECATED. Please use the `post_get_firewall_endpoint_association_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the FirewallActivation server but before
        it is returned to user code. This `post_get_firewall_endpoint_association` interceptor runs
        before the `post_get_firewall_endpoint_association_with_metadata` interceptor.
        """
        return response

    def post_get_firewall_endpoint_association_with_metadata(
        self,
        response: firewall_activation.FirewallEndpointAssociation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        firewall_activation.FirewallEndpointAssociation,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_firewall_endpoint_association

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the FirewallActivation server but before it is returned to user code.

        We recommend only using this `post_get_firewall_endpoint_association_with_metadata`
        interceptor in new development instead of the `post_get_firewall_endpoint_association` interceptor.
        When both interceptors are used, this `post_get_firewall_endpoint_association_with_metadata` interceptor runs after the
        `post_get_firewall_endpoint_association` interceptor. The (possibly modified) response returned by
        `post_get_firewall_endpoint_association` will be passed to
        `post_get_firewall_endpoint_association_with_metadata`.
        """
        return response, metadata

    def pre_get_project_firewall_endpoint(
        self,
        request: firewall_activation.GetFirewallEndpointRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        firewall_activation.GetFirewallEndpointRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_project_firewall_endpoint

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FirewallActivation server.
        """
        return request, metadata

    def post_get_project_firewall_endpoint(
        self, response: firewall_activation.FirewallEndpoint
    ) -> firewall_activation.FirewallEndpoint:
        """Post-rpc interceptor for get_project_firewall_endpoint

        DEPRECATED. Please use the `post_get_project_firewall_endpoint_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the FirewallActivation server but before
        it is returned to user code. This `post_get_project_firewall_endpoint` interceptor runs
        before the `post_get_project_firewall_endpoint_with_metadata` interceptor.
        """
        return response

    def post_get_project_firewall_endpoint_with_metadata(
        self,
        response: firewall_activation.FirewallEndpoint,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        firewall_activation.FirewallEndpoint, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_project_firewall_endpoint

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the FirewallActivation server but before it is returned to user code.

        We recommend only using this `post_get_project_firewall_endpoint_with_metadata`
        interceptor in new development instead of the `post_get_project_firewall_endpoint` interceptor.
        When both interceptors are used, this `post_get_project_firewall_endpoint_with_metadata` interceptor runs after the
        `post_get_project_firewall_endpoint` interceptor. The (possibly modified) response returned by
        `post_get_project_firewall_endpoint` will be passed to
        `post_get_project_firewall_endpoint_with_metadata`.
        """
        return response, metadata

    def pre_list_firewall_endpoint_associations(
        self,
        request: firewall_activation.ListFirewallEndpointAssociationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        firewall_activation.ListFirewallEndpointAssociationsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_firewall_endpoint_associations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FirewallActivation server.
        """
        return request, metadata

    def post_list_firewall_endpoint_associations(
        self, response: firewall_activation.ListFirewallEndpointAssociationsResponse
    ) -> firewall_activation.ListFirewallEndpointAssociationsResponse:
        """Post-rpc interceptor for list_firewall_endpoint_associations

        DEPRECATED. Please use the `post_list_firewall_endpoint_associations_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the FirewallActivation server but before
        it is returned to user code. This `post_list_firewall_endpoint_associations` interceptor runs
        before the `post_list_firewall_endpoint_associations_with_metadata` interceptor.
        """
        return response

    def post_list_firewall_endpoint_associations_with_metadata(
        self,
        response: firewall_activation.ListFirewallEndpointAssociationsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        firewall_activation.ListFirewallEndpointAssociationsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_firewall_endpoint_associations

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the FirewallActivation server but before it is returned to user code.

        We recommend only using this `post_list_firewall_endpoint_associations_with_metadata`
        interceptor in new development instead of the `post_list_firewall_endpoint_associations` interceptor.
        When both interceptors are used, this `post_list_firewall_endpoint_associations_with_metadata` interceptor runs after the
        `post_list_firewall_endpoint_associations` interceptor. The (possibly modified) response returned by
        `post_list_firewall_endpoint_associations` will be passed to
        `post_list_firewall_endpoint_associations_with_metadata`.
        """
        return response, metadata

    def pre_list_firewall_endpoints(
        self,
        request: firewall_activation.ListFirewallEndpointsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        firewall_activation.ListFirewallEndpointsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_firewall_endpoints

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FirewallActivation server.
        """
        return request, metadata

    def post_list_firewall_endpoints(
        self, response: firewall_activation.ListFirewallEndpointsResponse
    ) -> firewall_activation.ListFirewallEndpointsResponse:
        """Post-rpc interceptor for list_firewall_endpoints

        DEPRECATED. Please use the `post_list_firewall_endpoints_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the FirewallActivation server but before
        it is returned to user code. This `post_list_firewall_endpoints` interceptor runs
        before the `post_list_firewall_endpoints_with_metadata` interceptor.
        """
        return response

    def post_list_firewall_endpoints_with_metadata(
        self,
        response: firewall_activation.ListFirewallEndpointsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        firewall_activation.ListFirewallEndpointsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_firewall_endpoints

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the FirewallActivation server but before it is returned to user code.

        We recommend only using this `post_list_firewall_endpoints_with_metadata`
        interceptor in new development instead of the `post_list_firewall_endpoints` interceptor.
        When both interceptors are used, this `post_list_firewall_endpoints_with_metadata` interceptor runs after the
        `post_list_firewall_endpoints` interceptor. The (possibly modified) response returned by
        `post_list_firewall_endpoints` will be passed to
        `post_list_firewall_endpoints_with_metadata`.
        """
        return response, metadata

    def pre_list_project_firewall_endpoints(
        self,
        request: firewall_activation.ListFirewallEndpointsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        firewall_activation.ListFirewallEndpointsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_project_firewall_endpoints

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FirewallActivation server.
        """
        return request, metadata

    def post_list_project_firewall_endpoints(
        self, response: firewall_activation.ListFirewallEndpointsResponse
    ) -> firewall_activation.ListFirewallEndpointsResponse:
        """Post-rpc interceptor for list_project_firewall_endpoints

        DEPRECATED. Please use the `post_list_project_firewall_endpoints_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the FirewallActivation server but before
        it is returned to user code. This `post_list_project_firewall_endpoints` interceptor runs
        before the `post_list_project_firewall_endpoints_with_metadata` interceptor.
        """
        return response

    def post_list_project_firewall_endpoints_with_metadata(
        self,
        response: firewall_activation.ListFirewallEndpointsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        firewall_activation.ListFirewallEndpointsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_project_firewall_endpoints

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the FirewallActivation server but before it is returned to user code.

        We recommend only using this `post_list_project_firewall_endpoints_with_metadata`
        interceptor in new development instead of the `post_list_project_firewall_endpoints` interceptor.
        When both interceptors are used, this `post_list_project_firewall_endpoints_with_metadata` interceptor runs after the
        `post_list_project_firewall_endpoints` interceptor. The (possibly modified) response returned by
        `post_list_project_firewall_endpoints` will be passed to
        `post_list_project_firewall_endpoints_with_metadata`.
        """
        return response, metadata

    def pre_update_firewall_endpoint(
        self,
        request: firewall_activation.UpdateFirewallEndpointRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        firewall_activation.UpdateFirewallEndpointRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_firewall_endpoint

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FirewallActivation server.
        """
        return request, metadata

    def post_update_firewall_endpoint(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_firewall_endpoint

        DEPRECATED. Please use the `post_update_firewall_endpoint_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the FirewallActivation server but before
        it is returned to user code. This `post_update_firewall_endpoint` interceptor runs
        before the `post_update_firewall_endpoint_with_metadata` interceptor.
        """
        return response

    def post_update_firewall_endpoint_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_firewall_endpoint

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the FirewallActivation server but before it is returned to user code.

        We recommend only using this `post_update_firewall_endpoint_with_metadata`
        interceptor in new development instead of the `post_update_firewall_endpoint` interceptor.
        When both interceptors are used, this `post_update_firewall_endpoint_with_metadata` interceptor runs after the
        `post_update_firewall_endpoint` interceptor. The (possibly modified) response returned by
        `post_update_firewall_endpoint` will be passed to
        `post_update_firewall_endpoint_with_metadata`.
        """
        return response, metadata

    def pre_update_firewall_endpoint_association(
        self,
        request: firewall_activation.UpdateFirewallEndpointAssociationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        firewall_activation.UpdateFirewallEndpointAssociationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_firewall_endpoint_association

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FirewallActivation server.
        """
        return request, metadata

    def post_update_firewall_endpoint_association(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_firewall_endpoint_association

        DEPRECATED. Please use the `post_update_firewall_endpoint_association_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the FirewallActivation server but before
        it is returned to user code. This `post_update_firewall_endpoint_association` interceptor runs
        before the `post_update_firewall_endpoint_association_with_metadata` interceptor.
        """
        return response

    def post_update_firewall_endpoint_association_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_firewall_endpoint_association

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the FirewallActivation server but before it is returned to user code.

        We recommend only using this `post_update_firewall_endpoint_association_with_metadata`
        interceptor in new development instead of the `post_update_firewall_endpoint_association` interceptor.
        When both interceptors are used, this `post_update_firewall_endpoint_association_with_metadata` interceptor runs after the
        `post_update_firewall_endpoint_association` interceptor. The (possibly modified) response returned by
        `post_update_firewall_endpoint_association` will be passed to
        `post_update_firewall_endpoint_association_with_metadata`.
        """
        return response, metadata

    def pre_update_project_firewall_endpoint(
        self,
        request: firewall_activation.UpdateFirewallEndpointRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        firewall_activation.UpdateFirewallEndpointRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_project_firewall_endpoint

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FirewallActivation server.
        """
        return request, metadata

    def post_update_project_firewall_endpoint(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_project_firewall_endpoint

        DEPRECATED. Please use the `post_update_project_firewall_endpoint_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the FirewallActivation server but before
        it is returned to user code. This `post_update_project_firewall_endpoint` interceptor runs
        before the `post_update_project_firewall_endpoint_with_metadata` interceptor.
        """
        return response

    def post_update_project_firewall_endpoint_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_project_firewall_endpoint

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the FirewallActivation server but before it is returned to user code.

        We recommend only using this `post_update_project_firewall_endpoint_with_metadata`
        interceptor in new development instead of the `post_update_project_firewall_endpoint` interceptor.
        When both interceptors are used, this `post_update_project_firewall_endpoint_with_metadata` interceptor runs after the
        `post_update_project_firewall_endpoint` interceptor. The (possibly modified) response returned by
        `post_update_project_firewall_endpoint` will be passed to
        `post_update_project_firewall_endpoint_with_metadata`.
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
        before they are sent to the FirewallActivation server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the FirewallActivation server but before
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
        before they are sent to the FirewallActivation server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the FirewallActivation server but before
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
        before they are sent to the FirewallActivation server.
        """
        return request, metadata

    def post_get_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the FirewallActivation server but before
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
        before they are sent to the FirewallActivation server.
        """
        return request, metadata

    def post_set_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the FirewallActivation server but before
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
        before they are sent to the FirewallActivation server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the response
        after it is returned by the FirewallActivation server but before
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
        before they are sent to the FirewallActivation server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the FirewallActivation server but before
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
        before they are sent to the FirewallActivation server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the FirewallActivation server but before
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
        before they are sent to the FirewallActivation server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the FirewallActivation server but before
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
        before they are sent to the FirewallActivation server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the FirewallActivation server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class FirewallActivationRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: FirewallActivationRestInterceptor


class FirewallActivationRestTransport(_BaseFirewallActivationRestTransport):
    """REST backend synchronous transport for FirewallActivation.

    Service for managing Firewall Endpoints and Associations.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "networksecurity.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[FirewallActivationRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'networksecurity.googleapis.com').
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
            interceptor (Optional[FirewallActivationRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or FirewallActivationRestInterceptor()
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

    class _CreateFirewallEndpoint(
        _BaseFirewallActivationRestTransport._BaseCreateFirewallEndpoint,
        FirewallActivationRestStub,
    ):
        def __hash__(self):
            return hash("FirewallActivationRestTransport.CreateFirewallEndpoint")

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
            request: firewall_activation.CreateFirewallEndpointRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create firewall endpoint method over HTTP.

            Args:
                request (~.firewall_activation.CreateFirewallEndpointRequest):
                    The request object. Message for creating a Endpoint
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

            http_options = _BaseFirewallActivationRestTransport._BaseCreateFirewallEndpoint._get_http_options()
            request, metadata = self._interceptor.pre_create_firewall_endpoint(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFirewallActivationRestTransport._BaseCreateFirewallEndpoint,
                    "_BaseCreateFirewallEndpoint__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.FirewallActivationClient.CreateFirewallEndpoint",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
                        "rpcName": "CreateFirewallEndpoint",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                FirewallActivationRestTransport._CreateFirewallEndpoint._get_response(
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

            resp = self._interceptor.post_create_firewall_endpoint(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_firewall_endpoint_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1.FirewallActivationClient.create_firewall_endpoint",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
                        "rpcName": "CreateFirewallEndpoint",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateFirewallEndpointAssociation(
        _BaseFirewallActivationRestTransport._BaseCreateFirewallEndpointAssociation,
        FirewallActivationRestStub,
    ):
        def __hash__(self):
            return hash(
                "FirewallActivationRestTransport.CreateFirewallEndpointAssociation"
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
            request: firewall_activation.CreateFirewallEndpointAssociationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create firewall endpoint
            association method over HTTP.

                Args:
                    request (~.firewall_activation.CreateFirewallEndpointAssociationRequest):
                        The request object. Message for creating a Association
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

            http_options = _BaseFirewallActivationRestTransport._BaseCreateFirewallEndpointAssociation._get_http_options()
            request, metadata = (
                self._interceptor.pre_create_firewall_endpoint_association(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFirewallActivationRestTransport._BaseCreateFirewallEndpointAssociation,
                    "_BaseCreateFirewallEndpointAssociation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.FirewallActivationClient.CreateFirewallEndpointAssociation",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
                        "rpcName": "CreateFirewallEndpointAssociation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FirewallActivationRestTransport._CreateFirewallEndpointAssociation._get_response(
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

            resp = self._interceptor.post_create_firewall_endpoint_association(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_create_firewall_endpoint_association_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1.FirewallActivationClient.create_firewall_endpoint_association",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
                        "rpcName": "CreateFirewallEndpointAssociation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateProjectFirewallEndpoint(
        _BaseFirewallActivationRestTransport._BaseCreateProjectFirewallEndpoint,
        FirewallActivationRestStub,
    ):
        def __hash__(self):
            return hash("FirewallActivationRestTransport.CreateProjectFirewallEndpoint")

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
            request: firewall_activation.CreateFirewallEndpointRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create project firewall
            endpoint method over HTTP.

                Args:
                    request (~.firewall_activation.CreateFirewallEndpointRequest):
                        The request object. Message for creating a Endpoint
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

            http_options = _BaseFirewallActivationRestTransport._BaseCreateProjectFirewallEndpoint._get_http_options()
            request, metadata = self._interceptor.pre_create_project_firewall_endpoint(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFirewallActivationRestTransport._BaseCreateProjectFirewallEndpoint,
                    "_BaseCreateProjectFirewallEndpoint__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.FirewallActivationClient.CreateProjectFirewallEndpoint",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
                        "rpcName": "CreateProjectFirewallEndpoint",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FirewallActivationRestTransport._CreateProjectFirewallEndpoint._get_response(
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

            resp = self._interceptor.post_create_project_firewall_endpoint(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_create_project_firewall_endpoint_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1.FirewallActivationClient.create_project_firewall_endpoint",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
                        "rpcName": "CreateProjectFirewallEndpoint",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteFirewallEndpoint(
        _BaseFirewallActivationRestTransport._BaseDeleteFirewallEndpoint,
        FirewallActivationRestStub,
    ):
        def __hash__(self):
            return hash("FirewallActivationRestTransport.DeleteFirewallEndpoint")

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
            request: firewall_activation.DeleteFirewallEndpointRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete firewall endpoint method over HTTP.

            Args:
                request (~.firewall_activation.DeleteFirewallEndpointRequest):
                    The request object. Message for deleting a Endpoint
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

            http_options = _BaseFirewallActivationRestTransport._BaseDeleteFirewallEndpoint._get_http_options()
            request, metadata = self._interceptor.pre_delete_firewall_endpoint(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFirewallActivationRestTransport._BaseDeleteFirewallEndpoint,
                    "_BaseDeleteFirewallEndpoint__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.FirewallActivationClient.DeleteFirewallEndpoint",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
                        "rpcName": "DeleteFirewallEndpoint",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                FirewallActivationRestTransport._DeleteFirewallEndpoint._get_response(
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

            resp = self._interceptor.post_delete_firewall_endpoint(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_firewall_endpoint_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1.FirewallActivationClient.delete_firewall_endpoint",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
                        "rpcName": "DeleteFirewallEndpoint",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteFirewallEndpointAssociation(
        _BaseFirewallActivationRestTransport._BaseDeleteFirewallEndpointAssociation,
        FirewallActivationRestStub,
    ):
        def __hash__(self):
            return hash(
                "FirewallActivationRestTransport.DeleteFirewallEndpointAssociation"
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
            request: firewall_activation.DeleteFirewallEndpointAssociationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete firewall endpoint
            association method over HTTP.

                Args:
                    request (~.firewall_activation.DeleteFirewallEndpointAssociationRequest):
                        The request object. Message for deleting a Association
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

            http_options = _BaseFirewallActivationRestTransport._BaseDeleteFirewallEndpointAssociation._get_http_options()
            request, metadata = (
                self._interceptor.pre_delete_firewall_endpoint_association(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFirewallActivationRestTransport._BaseDeleteFirewallEndpointAssociation,
                    "_BaseDeleteFirewallEndpointAssociation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.FirewallActivationClient.DeleteFirewallEndpointAssociation",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
                        "rpcName": "DeleteFirewallEndpointAssociation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FirewallActivationRestTransport._DeleteFirewallEndpointAssociation._get_response(
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

            resp = self._interceptor.post_delete_firewall_endpoint_association(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_delete_firewall_endpoint_association_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1.FirewallActivationClient.delete_firewall_endpoint_association",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
                        "rpcName": "DeleteFirewallEndpointAssociation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteProjectFirewallEndpoint(
        _BaseFirewallActivationRestTransport._BaseDeleteProjectFirewallEndpoint,
        FirewallActivationRestStub,
    ):
        def __hash__(self):
            return hash("FirewallActivationRestTransport.DeleteProjectFirewallEndpoint")

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
            request: firewall_activation.DeleteFirewallEndpointRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete project firewall
            endpoint method over HTTP.

                Args:
                    request (~.firewall_activation.DeleteFirewallEndpointRequest):
                        The request object. Message for deleting a Endpoint
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

            http_options = _BaseFirewallActivationRestTransport._BaseDeleteProjectFirewallEndpoint._get_http_options()
            request, metadata = self._interceptor.pre_delete_project_firewall_endpoint(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFirewallActivationRestTransport._BaseDeleteProjectFirewallEndpoint,
                    "_BaseDeleteProjectFirewallEndpoint__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.FirewallActivationClient.DeleteProjectFirewallEndpoint",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
                        "rpcName": "DeleteProjectFirewallEndpoint",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FirewallActivationRestTransport._DeleteProjectFirewallEndpoint._get_response(
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

            resp = self._interceptor.post_delete_project_firewall_endpoint(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_delete_project_firewall_endpoint_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1.FirewallActivationClient.delete_project_firewall_endpoint",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
                        "rpcName": "DeleteProjectFirewallEndpoint",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetFirewallEndpoint(
        _BaseFirewallActivationRestTransport._BaseGetFirewallEndpoint,
        FirewallActivationRestStub,
    ):
        def __hash__(self):
            return hash("FirewallActivationRestTransport.GetFirewallEndpoint")

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
            request: firewall_activation.GetFirewallEndpointRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> firewall_activation.FirewallEndpoint:
            r"""Call the get firewall endpoint method over HTTP.

            Args:
                request (~.firewall_activation.GetFirewallEndpointRequest):
                    The request object. Message for getting a Endpoint
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.firewall_activation.FirewallEndpoint:
                    Message describing Endpoint object.
            """

            http_options = _BaseFirewallActivationRestTransport._BaseGetFirewallEndpoint._get_http_options()
            request, metadata = self._interceptor.pre_get_firewall_endpoint(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFirewallActivationRestTransport._BaseGetFirewallEndpoint,
                    "_BaseGetFirewallEndpoint__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.FirewallActivationClient.GetFirewallEndpoint",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
                        "rpcName": "GetFirewallEndpoint",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                FirewallActivationRestTransport._GetFirewallEndpoint._get_response(
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
            resp = firewall_activation.FirewallEndpoint()
            pb_resp = firewall_activation.FirewallEndpoint.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_firewall_endpoint(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_firewall_endpoint_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = firewall_activation.FirewallEndpoint.to_json(
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
                    "Received response for google.cloud.networksecurity_v1.FirewallActivationClient.get_firewall_endpoint",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
                        "rpcName": "GetFirewallEndpoint",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetFirewallEndpointAssociation(
        _BaseFirewallActivationRestTransport._BaseGetFirewallEndpointAssociation,
        FirewallActivationRestStub,
    ):
        def __hash__(self):
            return hash(
                "FirewallActivationRestTransport.GetFirewallEndpointAssociation"
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
            request: firewall_activation.GetFirewallEndpointAssociationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> firewall_activation.FirewallEndpointAssociation:
            r"""Call the get firewall endpoint
            association method over HTTP.

                Args:
                    request (~.firewall_activation.GetFirewallEndpointAssociationRequest):
                        The request object. Message for getting a Association
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.firewall_activation.FirewallEndpointAssociation:
                        Message describing Association object
            """

            http_options = _BaseFirewallActivationRestTransport._BaseGetFirewallEndpointAssociation._get_http_options()
            request, metadata = self._interceptor.pre_get_firewall_endpoint_association(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFirewallActivationRestTransport._BaseGetFirewallEndpointAssociation,
                    "_BaseGetFirewallEndpointAssociation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.FirewallActivationClient.GetFirewallEndpointAssociation",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
                        "rpcName": "GetFirewallEndpointAssociation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FirewallActivationRestTransport._GetFirewallEndpointAssociation._get_response(
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
            resp = firewall_activation.FirewallEndpointAssociation()
            pb_resp = firewall_activation.FirewallEndpointAssociation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_firewall_endpoint_association(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_get_firewall_endpoint_association_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        firewall_activation.FirewallEndpointAssociation.to_json(
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
                    "Received response for google.cloud.networksecurity_v1.FirewallActivationClient.get_firewall_endpoint_association",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
                        "rpcName": "GetFirewallEndpointAssociation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetProjectFirewallEndpoint(
        _BaseFirewallActivationRestTransport._BaseGetProjectFirewallEndpoint,
        FirewallActivationRestStub,
    ):
        def __hash__(self):
            return hash("FirewallActivationRestTransport.GetProjectFirewallEndpoint")

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
            request: firewall_activation.GetFirewallEndpointRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> firewall_activation.FirewallEndpoint:
            r"""Call the get project firewall
            endpoint method over HTTP.

                Args:
                    request (~.firewall_activation.GetFirewallEndpointRequest):
                        The request object. Message for getting a Endpoint
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.firewall_activation.FirewallEndpoint:
                        Message describing Endpoint object.
            """

            http_options = _BaseFirewallActivationRestTransport._BaseGetProjectFirewallEndpoint._get_http_options()
            request, metadata = self._interceptor.pre_get_project_firewall_endpoint(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFirewallActivationRestTransport._BaseGetProjectFirewallEndpoint,
                    "_BaseGetProjectFirewallEndpoint__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.FirewallActivationClient.GetProjectFirewallEndpoint",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
                        "rpcName": "GetProjectFirewallEndpoint",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FirewallActivationRestTransport._GetProjectFirewallEndpoint._get_response(
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
            resp = firewall_activation.FirewallEndpoint()
            pb_resp = firewall_activation.FirewallEndpoint.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_project_firewall_endpoint(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_get_project_firewall_endpoint_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = firewall_activation.FirewallEndpoint.to_json(
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
                    "Received response for google.cloud.networksecurity_v1.FirewallActivationClient.get_project_firewall_endpoint",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
                        "rpcName": "GetProjectFirewallEndpoint",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListFirewallEndpointAssociations(
        _BaseFirewallActivationRestTransport._BaseListFirewallEndpointAssociations,
        FirewallActivationRestStub,
    ):
        def __hash__(self):
            return hash(
                "FirewallActivationRestTransport.ListFirewallEndpointAssociations"
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
            request: firewall_activation.ListFirewallEndpointAssociationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> firewall_activation.ListFirewallEndpointAssociationsResponse:
            r"""Call the list firewall endpoint
            associations method over HTTP.

                Args:
                    request (~.firewall_activation.ListFirewallEndpointAssociationsRequest):
                        The request object. Message for requesting list of
                    Associations
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.firewall_activation.ListFirewallEndpointAssociationsResponse:
                        Message for response to listing
                    Associations

            """

            http_options = _BaseFirewallActivationRestTransport._BaseListFirewallEndpointAssociations._get_http_options()
            request, metadata = (
                self._interceptor.pre_list_firewall_endpoint_associations(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFirewallActivationRestTransport._BaseListFirewallEndpointAssociations,
                    "_BaseListFirewallEndpointAssociations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.FirewallActivationClient.ListFirewallEndpointAssociations",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
                        "rpcName": "ListFirewallEndpointAssociations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FirewallActivationRestTransport._ListFirewallEndpointAssociations._get_response(
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
            resp = firewall_activation.ListFirewallEndpointAssociationsResponse()
            pb_resp = firewall_activation.ListFirewallEndpointAssociationsResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_firewall_endpoint_associations(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_firewall_endpoint_associations_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = firewall_activation.ListFirewallEndpointAssociationsResponse.to_json(
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
                    "Received response for google.cloud.networksecurity_v1.FirewallActivationClient.list_firewall_endpoint_associations",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
                        "rpcName": "ListFirewallEndpointAssociations",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListFirewallEndpoints(
        _BaseFirewallActivationRestTransport._BaseListFirewallEndpoints,
        FirewallActivationRestStub,
    ):
        def __hash__(self):
            return hash("FirewallActivationRestTransport.ListFirewallEndpoints")

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
            request: firewall_activation.ListFirewallEndpointsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> firewall_activation.ListFirewallEndpointsResponse:
            r"""Call the list firewall endpoints method over HTTP.

            Args:
                request (~.firewall_activation.ListFirewallEndpointsRequest):
                    The request object. Message for requesting list of
                Endpoints
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.firewall_activation.ListFirewallEndpointsResponse:
                    Message for response to listing
                Endpoints

            """

            http_options = _BaseFirewallActivationRestTransport._BaseListFirewallEndpoints._get_http_options()
            request, metadata = self._interceptor.pre_list_firewall_endpoints(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFirewallActivationRestTransport._BaseListFirewallEndpoints,
                    "_BaseListFirewallEndpoints__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.FirewallActivationClient.ListFirewallEndpoints",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
                        "rpcName": "ListFirewallEndpoints",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                FirewallActivationRestTransport._ListFirewallEndpoints._get_response(
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
            resp = firewall_activation.ListFirewallEndpointsResponse()
            pb_resp = firewall_activation.ListFirewallEndpointsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_firewall_endpoints(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_firewall_endpoints_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        firewall_activation.ListFirewallEndpointsResponse.to_json(
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
                    "Received response for google.cloud.networksecurity_v1.FirewallActivationClient.list_firewall_endpoints",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
                        "rpcName": "ListFirewallEndpoints",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListProjectFirewallEndpoints(
        _BaseFirewallActivationRestTransport._BaseListProjectFirewallEndpoints,
        FirewallActivationRestStub,
    ):
        def __hash__(self):
            return hash("FirewallActivationRestTransport.ListProjectFirewallEndpoints")

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
            request: firewall_activation.ListFirewallEndpointsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> firewall_activation.ListFirewallEndpointsResponse:
            r"""Call the list project firewall
            endpoints method over HTTP.

                Args:
                    request (~.firewall_activation.ListFirewallEndpointsRequest):
                        The request object. Message for requesting list of
                    Endpoints
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.firewall_activation.ListFirewallEndpointsResponse:
                        Message for response to listing
                    Endpoints

            """

            http_options = _BaseFirewallActivationRestTransport._BaseListProjectFirewallEndpoints._get_http_options()
            request, metadata = self._interceptor.pre_list_project_firewall_endpoints(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFirewallActivationRestTransport._BaseListProjectFirewallEndpoints,
                    "_BaseListProjectFirewallEndpoints__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.FirewallActivationClient.ListProjectFirewallEndpoints",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
                        "rpcName": "ListProjectFirewallEndpoints",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FirewallActivationRestTransport._ListProjectFirewallEndpoints._get_response(
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
            resp = firewall_activation.ListFirewallEndpointsResponse()
            pb_resp = firewall_activation.ListFirewallEndpointsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_project_firewall_endpoints(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_project_firewall_endpoints_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        firewall_activation.ListFirewallEndpointsResponse.to_json(
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
                    "Received response for google.cloud.networksecurity_v1.FirewallActivationClient.list_project_firewall_endpoints",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
                        "rpcName": "ListProjectFirewallEndpoints",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateFirewallEndpoint(
        _BaseFirewallActivationRestTransport._BaseUpdateFirewallEndpoint,
        FirewallActivationRestStub,
    ):
        def __hash__(self):
            return hash("FirewallActivationRestTransport.UpdateFirewallEndpoint")

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
            request: firewall_activation.UpdateFirewallEndpointRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update firewall endpoint method over HTTP.

            Args:
                request (~.firewall_activation.UpdateFirewallEndpointRequest):
                    The request object. Message for updating a Endpoint
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

            http_options = _BaseFirewallActivationRestTransport._BaseUpdateFirewallEndpoint._get_http_options()
            request, metadata = self._interceptor.pre_update_firewall_endpoint(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFirewallActivationRestTransport._BaseUpdateFirewallEndpoint,
                    "_BaseUpdateFirewallEndpoint__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.FirewallActivationClient.UpdateFirewallEndpoint",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
                        "rpcName": "UpdateFirewallEndpoint",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                FirewallActivationRestTransport._UpdateFirewallEndpoint._get_response(
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

            resp = self._interceptor.post_update_firewall_endpoint(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_firewall_endpoint_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1.FirewallActivationClient.update_firewall_endpoint",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
                        "rpcName": "UpdateFirewallEndpoint",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateFirewallEndpointAssociation(
        _BaseFirewallActivationRestTransport._BaseUpdateFirewallEndpointAssociation,
        FirewallActivationRestStub,
    ):
        def __hash__(self):
            return hash(
                "FirewallActivationRestTransport.UpdateFirewallEndpointAssociation"
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
            request: firewall_activation.UpdateFirewallEndpointAssociationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update firewall endpoint
            association method over HTTP.

                Args:
                    request (~.firewall_activation.UpdateFirewallEndpointAssociationRequest):
                        The request object. Message for updating an Association
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

            http_options = _BaseFirewallActivationRestTransport._BaseUpdateFirewallEndpointAssociation._get_http_options()
            request, metadata = (
                self._interceptor.pre_update_firewall_endpoint_association(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFirewallActivationRestTransport._BaseUpdateFirewallEndpointAssociation,
                    "_BaseUpdateFirewallEndpointAssociation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.FirewallActivationClient.UpdateFirewallEndpointAssociation",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
                        "rpcName": "UpdateFirewallEndpointAssociation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FirewallActivationRestTransport._UpdateFirewallEndpointAssociation._get_response(
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

            resp = self._interceptor.post_update_firewall_endpoint_association(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_update_firewall_endpoint_association_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1.FirewallActivationClient.update_firewall_endpoint_association",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
                        "rpcName": "UpdateFirewallEndpointAssociation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateProjectFirewallEndpoint(
        _BaseFirewallActivationRestTransport._BaseUpdateProjectFirewallEndpoint,
        FirewallActivationRestStub,
    ):
        def __hash__(self):
            return hash("FirewallActivationRestTransport.UpdateProjectFirewallEndpoint")

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
            request: firewall_activation.UpdateFirewallEndpointRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update project firewall
            endpoint method over HTTP.

                Args:
                    request (~.firewall_activation.UpdateFirewallEndpointRequest):
                        The request object. Message for updating a Endpoint
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

            http_options = _BaseFirewallActivationRestTransport._BaseUpdateProjectFirewallEndpoint._get_http_options()
            request, metadata = self._interceptor.pre_update_project_firewall_endpoint(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFirewallActivationRestTransport._BaseUpdateProjectFirewallEndpoint,
                    "_BaseUpdateProjectFirewallEndpoint__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1.FirewallActivationClient.UpdateProjectFirewallEndpoint",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
                        "rpcName": "UpdateProjectFirewallEndpoint",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FirewallActivationRestTransport._UpdateProjectFirewallEndpoint._get_response(
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

            resp = self._interceptor.post_update_project_firewall_endpoint(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_update_project_firewall_endpoint_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1.FirewallActivationClient.update_project_firewall_endpoint",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
                        "rpcName": "UpdateProjectFirewallEndpoint",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_firewall_endpoint(
        self,
    ) -> Callable[
        [firewall_activation.CreateFirewallEndpointRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateFirewallEndpoint(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_firewall_endpoint_association(
        self,
    ) -> Callable[
        [firewall_activation.CreateFirewallEndpointAssociationRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateFirewallEndpointAssociation(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_project_firewall_endpoint(
        self,
    ) -> Callable[
        [firewall_activation.CreateFirewallEndpointRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateProjectFirewallEndpoint(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_firewall_endpoint(
        self,
    ) -> Callable[
        [firewall_activation.DeleteFirewallEndpointRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteFirewallEndpoint(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_firewall_endpoint_association(
        self,
    ) -> Callable[
        [firewall_activation.DeleteFirewallEndpointAssociationRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteFirewallEndpointAssociation(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_project_firewall_endpoint(
        self,
    ) -> Callable[
        [firewall_activation.DeleteFirewallEndpointRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteProjectFirewallEndpoint(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_firewall_endpoint(
        self,
    ) -> Callable[
        [firewall_activation.GetFirewallEndpointRequest],
        firewall_activation.FirewallEndpoint,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetFirewallEndpoint(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_firewall_endpoint_association(
        self,
    ) -> Callable[
        [firewall_activation.GetFirewallEndpointAssociationRequest],
        firewall_activation.FirewallEndpointAssociation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetFirewallEndpointAssociation(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_project_firewall_endpoint(
        self,
    ) -> Callable[
        [firewall_activation.GetFirewallEndpointRequest],
        firewall_activation.FirewallEndpoint,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetProjectFirewallEndpoint(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_firewall_endpoint_associations(
        self,
    ) -> Callable[
        [firewall_activation.ListFirewallEndpointAssociationsRequest],
        firewall_activation.ListFirewallEndpointAssociationsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListFirewallEndpointAssociations(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_firewall_endpoints(
        self,
    ) -> Callable[
        [firewall_activation.ListFirewallEndpointsRequest],
        firewall_activation.ListFirewallEndpointsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListFirewallEndpoints(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_project_firewall_endpoints(
        self,
    ) -> Callable[
        [firewall_activation.ListFirewallEndpointsRequest],
        firewall_activation.ListFirewallEndpointsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListProjectFirewallEndpoints(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_firewall_endpoint(
        self,
    ) -> Callable[
        [firewall_activation.UpdateFirewallEndpointRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateFirewallEndpoint(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_firewall_endpoint_association(
        self,
    ) -> Callable[
        [firewall_activation.UpdateFirewallEndpointAssociationRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateFirewallEndpointAssociation(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_project_firewall_endpoint(
        self,
    ) -> Callable[
        [firewall_activation.UpdateFirewallEndpointRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateProjectFirewallEndpoint(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseFirewallActivationRestTransport._BaseGetLocation,
        FirewallActivationRestStub,
    ):
        def __hash__(self):
            return hash("FirewallActivationRestTransport.GetLocation")

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

            http_options = _BaseFirewallActivationRestTransport._BaseGetLocation._get_http_options()
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFirewallActivationRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.networksecurity_v1.FirewallActivationClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FirewallActivationRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.networksecurity_v1.FirewallActivationAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
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
        _BaseFirewallActivationRestTransport._BaseListLocations,
        FirewallActivationRestStub,
    ):
        def __hash__(self):
            return hash("FirewallActivationRestTransport.ListLocations")

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

            http_options = _BaseFirewallActivationRestTransport._BaseListLocations._get_http_options()
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFirewallActivationRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.networksecurity_v1.FirewallActivationClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FirewallActivationRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.networksecurity_v1.FirewallActivationAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
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
        _BaseFirewallActivationRestTransport._BaseGetIamPolicy,
        FirewallActivationRestStub,
    ):
        def __hash__(self):
            return hash("FirewallActivationRestTransport.GetIamPolicy")

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

            http_options = _BaseFirewallActivationRestTransport._BaseGetIamPolicy._get_http_options()
            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFirewallActivationRestTransport._BaseGetIamPolicy,
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
                    f"Sending request for google.cloud.networksecurity_v1.FirewallActivationClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
                        "rpcName": "GetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FirewallActivationRestTransport._GetIamPolicy._get_response(
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
                    "Received response for google.cloud.networksecurity_v1.FirewallActivationAsyncClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
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
        _BaseFirewallActivationRestTransport._BaseSetIamPolicy,
        FirewallActivationRestStub,
    ):
        def __hash__(self):
            return hash("FirewallActivationRestTransport.SetIamPolicy")

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

            http_options = _BaseFirewallActivationRestTransport._BaseSetIamPolicy._get_http_options()
            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFirewallActivationRestTransport._BaseSetIamPolicy,
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
                    f"Sending request for google.cloud.networksecurity_v1.FirewallActivationClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
                        "rpcName": "SetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FirewallActivationRestTransport._SetIamPolicy._get_response(
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
                    "Received response for google.cloud.networksecurity_v1.FirewallActivationAsyncClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
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
        _BaseFirewallActivationRestTransport._BaseTestIamPermissions,
        FirewallActivationRestStub,
    ):
        def __hash__(self):
            return hash("FirewallActivationRestTransport.TestIamPermissions")

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

            http_options = _BaseFirewallActivationRestTransport._BaseTestIamPermissions._get_http_options()
            request, metadata = self._interceptor.pre_test_iam_permissions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFirewallActivationRestTransport._BaseTestIamPermissions,
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
                    f"Sending request for google.cloud.networksecurity_v1.FirewallActivationClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
                        "rpcName": "TestIamPermissions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                FirewallActivationRestTransport._TestIamPermissions._get_response(
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
                    "Received response for google.cloud.networksecurity_v1.FirewallActivationAsyncClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
                        "rpcName": "TestIamPermissions",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseFirewallActivationRestTransport._BaseCancelOperation,
        FirewallActivationRestStub,
    ):
        def __hash__(self):
            return hash("FirewallActivationRestTransport.CancelOperation")

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

            http_options = _BaseFirewallActivationRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFirewallActivationRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.networksecurity_v1.FirewallActivationClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FirewallActivationRestTransport._CancelOperation._get_response(
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
        _BaseFirewallActivationRestTransport._BaseDeleteOperation,
        FirewallActivationRestStub,
    ):
        def __hash__(self):
            return hash("FirewallActivationRestTransport.DeleteOperation")

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

            http_options = _BaseFirewallActivationRestTransport._BaseDeleteOperation._get_http_options()
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFirewallActivationRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.networksecurity_v1.FirewallActivationClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FirewallActivationRestTransport._DeleteOperation._get_response(
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
        _BaseFirewallActivationRestTransport._BaseGetOperation,
        FirewallActivationRestStub,
    ):
        def __hash__(self):
            return hash("FirewallActivationRestTransport.GetOperation")

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

            http_options = _BaseFirewallActivationRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFirewallActivationRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.networksecurity_v1.FirewallActivationClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FirewallActivationRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.networksecurity_v1.FirewallActivationAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
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
        _BaseFirewallActivationRestTransport._BaseListOperations,
        FirewallActivationRestStub,
    ):
        def __hash__(self):
            return hash("FirewallActivationRestTransport.ListOperations")

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

            http_options = _BaseFirewallActivationRestTransport._BaseListOperations._get_http_options()
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFirewallActivationRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.networksecurity_v1.FirewallActivationClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FirewallActivationRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.networksecurity_v1.FirewallActivationAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1.FirewallActivation",
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


__all__ = ("FirewallActivationRestTransport",)
