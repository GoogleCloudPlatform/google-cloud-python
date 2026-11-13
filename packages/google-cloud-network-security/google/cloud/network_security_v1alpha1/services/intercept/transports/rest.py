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

from google.cloud.network_security_v1alpha1._compat import transcode_request
from google.cloud.network_security_v1alpha1.types import intercept

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseInterceptRestTransport

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


class InterceptRestInterceptor:
    """Interceptor for Intercept.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the InterceptRestTransport.

    .. code-block:: python
        class MyCustomInterceptInterceptor(InterceptRestInterceptor):
            def pre_create_intercept_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_intercept_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_intercept_deployment_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_intercept_deployment_group(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_intercept_endpoint_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_intercept_endpoint_group(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_intercept_endpoint_group_association(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_intercept_endpoint_group_association(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_intercept_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_intercept_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_intercept_deployment_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_intercept_deployment_group(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_intercept_endpoint_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_intercept_endpoint_group(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_intercept_endpoint_group_association(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_intercept_endpoint_group_association(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_intercept_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_intercept_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_intercept_deployment_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_intercept_deployment_group(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_intercept_endpoint_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_intercept_endpoint_group(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_intercept_endpoint_group_association(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_intercept_endpoint_group_association(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_intercept_deployment_groups(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_intercept_deployment_groups(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_intercept_deployments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_intercept_deployments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_intercept_endpoint_group_associations(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_intercept_endpoint_group_associations(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_intercept_endpoint_groups(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_intercept_endpoint_groups(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_intercept_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_intercept_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_intercept_deployment_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_intercept_deployment_group(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_intercept_endpoint_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_intercept_endpoint_group(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_intercept_endpoint_group_association(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_intercept_endpoint_group_association(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = InterceptRestTransport(interceptor=MyCustomInterceptInterceptor())
        client = InterceptClient(transport=transport)


    """

    def pre_create_intercept_deployment(
        self,
        request: intercept.CreateInterceptDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        intercept.CreateInterceptDeploymentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_intercept_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Intercept server.
        """
        return request, metadata

    def post_create_intercept_deployment(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_intercept_deployment

        DEPRECATED. Please use the `post_create_intercept_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Intercept server but before
        it is returned to user code. This `post_create_intercept_deployment` interceptor runs
        before the `post_create_intercept_deployment_with_metadata` interceptor.
        """
        return response

    def post_create_intercept_deployment_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_intercept_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Intercept server but before it is returned to user code.

        We recommend only using this `post_create_intercept_deployment_with_metadata`
        interceptor in new development instead of the `post_create_intercept_deployment` interceptor.
        When both interceptors are used, this `post_create_intercept_deployment_with_metadata` interceptor runs after the
        `post_create_intercept_deployment` interceptor. The (possibly modified) response returned by
        `post_create_intercept_deployment` will be passed to
        `post_create_intercept_deployment_with_metadata`.
        """
        return response, metadata

    def pre_create_intercept_deployment_group(
        self,
        request: intercept.CreateInterceptDeploymentGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        intercept.CreateInterceptDeploymentGroupRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_intercept_deployment_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Intercept server.
        """
        return request, metadata

    def post_create_intercept_deployment_group(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_intercept_deployment_group

        DEPRECATED. Please use the `post_create_intercept_deployment_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Intercept server but before
        it is returned to user code. This `post_create_intercept_deployment_group` interceptor runs
        before the `post_create_intercept_deployment_group_with_metadata` interceptor.
        """
        return response

    def post_create_intercept_deployment_group_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_intercept_deployment_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Intercept server but before it is returned to user code.

        We recommend only using this `post_create_intercept_deployment_group_with_metadata`
        interceptor in new development instead of the `post_create_intercept_deployment_group` interceptor.
        When both interceptors are used, this `post_create_intercept_deployment_group_with_metadata` interceptor runs after the
        `post_create_intercept_deployment_group` interceptor. The (possibly modified) response returned by
        `post_create_intercept_deployment_group` will be passed to
        `post_create_intercept_deployment_group_with_metadata`.
        """
        return response, metadata

    def pre_create_intercept_endpoint_group(
        self,
        request: intercept.CreateInterceptEndpointGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        intercept.CreateInterceptEndpointGroupRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_intercept_endpoint_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Intercept server.
        """
        return request, metadata

    def post_create_intercept_endpoint_group(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_intercept_endpoint_group

        DEPRECATED. Please use the `post_create_intercept_endpoint_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Intercept server but before
        it is returned to user code. This `post_create_intercept_endpoint_group` interceptor runs
        before the `post_create_intercept_endpoint_group_with_metadata` interceptor.
        """
        return response

    def post_create_intercept_endpoint_group_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_intercept_endpoint_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Intercept server but before it is returned to user code.

        We recommend only using this `post_create_intercept_endpoint_group_with_metadata`
        interceptor in new development instead of the `post_create_intercept_endpoint_group` interceptor.
        When both interceptors are used, this `post_create_intercept_endpoint_group_with_metadata` interceptor runs after the
        `post_create_intercept_endpoint_group` interceptor. The (possibly modified) response returned by
        `post_create_intercept_endpoint_group` will be passed to
        `post_create_intercept_endpoint_group_with_metadata`.
        """
        return response, metadata

    def pre_create_intercept_endpoint_group_association(
        self,
        request: intercept.CreateInterceptEndpointGroupAssociationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        intercept.CreateInterceptEndpointGroupAssociationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_intercept_endpoint_group_association

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Intercept server.
        """
        return request, metadata

    def post_create_intercept_endpoint_group_association(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_intercept_endpoint_group_association

        DEPRECATED. Please use the `post_create_intercept_endpoint_group_association_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Intercept server but before
        it is returned to user code. This `post_create_intercept_endpoint_group_association` interceptor runs
        before the `post_create_intercept_endpoint_group_association_with_metadata` interceptor.
        """
        return response

    def post_create_intercept_endpoint_group_association_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_intercept_endpoint_group_association

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Intercept server but before it is returned to user code.

        We recommend only using this `post_create_intercept_endpoint_group_association_with_metadata`
        interceptor in new development instead of the `post_create_intercept_endpoint_group_association` interceptor.
        When both interceptors are used, this `post_create_intercept_endpoint_group_association_with_metadata` interceptor runs after the
        `post_create_intercept_endpoint_group_association` interceptor. The (possibly modified) response returned by
        `post_create_intercept_endpoint_group_association` will be passed to
        `post_create_intercept_endpoint_group_association_with_metadata`.
        """
        return response, metadata

    def pre_delete_intercept_deployment(
        self,
        request: intercept.DeleteInterceptDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        intercept.DeleteInterceptDeploymentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_intercept_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Intercept server.
        """
        return request, metadata

    def post_delete_intercept_deployment(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_intercept_deployment

        DEPRECATED. Please use the `post_delete_intercept_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Intercept server but before
        it is returned to user code. This `post_delete_intercept_deployment` interceptor runs
        before the `post_delete_intercept_deployment_with_metadata` interceptor.
        """
        return response

    def post_delete_intercept_deployment_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_intercept_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Intercept server but before it is returned to user code.

        We recommend only using this `post_delete_intercept_deployment_with_metadata`
        interceptor in new development instead of the `post_delete_intercept_deployment` interceptor.
        When both interceptors are used, this `post_delete_intercept_deployment_with_metadata` interceptor runs after the
        `post_delete_intercept_deployment` interceptor. The (possibly modified) response returned by
        `post_delete_intercept_deployment` will be passed to
        `post_delete_intercept_deployment_with_metadata`.
        """
        return response, metadata

    def pre_delete_intercept_deployment_group(
        self,
        request: intercept.DeleteInterceptDeploymentGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        intercept.DeleteInterceptDeploymentGroupRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_intercept_deployment_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Intercept server.
        """
        return request, metadata

    def post_delete_intercept_deployment_group(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_intercept_deployment_group

        DEPRECATED. Please use the `post_delete_intercept_deployment_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Intercept server but before
        it is returned to user code. This `post_delete_intercept_deployment_group` interceptor runs
        before the `post_delete_intercept_deployment_group_with_metadata` interceptor.
        """
        return response

    def post_delete_intercept_deployment_group_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_intercept_deployment_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Intercept server but before it is returned to user code.

        We recommend only using this `post_delete_intercept_deployment_group_with_metadata`
        interceptor in new development instead of the `post_delete_intercept_deployment_group` interceptor.
        When both interceptors are used, this `post_delete_intercept_deployment_group_with_metadata` interceptor runs after the
        `post_delete_intercept_deployment_group` interceptor. The (possibly modified) response returned by
        `post_delete_intercept_deployment_group` will be passed to
        `post_delete_intercept_deployment_group_with_metadata`.
        """
        return response, metadata

    def pre_delete_intercept_endpoint_group(
        self,
        request: intercept.DeleteInterceptEndpointGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        intercept.DeleteInterceptEndpointGroupRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_intercept_endpoint_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Intercept server.
        """
        return request, metadata

    def post_delete_intercept_endpoint_group(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_intercept_endpoint_group

        DEPRECATED. Please use the `post_delete_intercept_endpoint_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Intercept server but before
        it is returned to user code. This `post_delete_intercept_endpoint_group` interceptor runs
        before the `post_delete_intercept_endpoint_group_with_metadata` interceptor.
        """
        return response

    def post_delete_intercept_endpoint_group_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_intercept_endpoint_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Intercept server but before it is returned to user code.

        We recommend only using this `post_delete_intercept_endpoint_group_with_metadata`
        interceptor in new development instead of the `post_delete_intercept_endpoint_group` interceptor.
        When both interceptors are used, this `post_delete_intercept_endpoint_group_with_metadata` interceptor runs after the
        `post_delete_intercept_endpoint_group` interceptor. The (possibly modified) response returned by
        `post_delete_intercept_endpoint_group` will be passed to
        `post_delete_intercept_endpoint_group_with_metadata`.
        """
        return response, metadata

    def pre_delete_intercept_endpoint_group_association(
        self,
        request: intercept.DeleteInterceptEndpointGroupAssociationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        intercept.DeleteInterceptEndpointGroupAssociationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_intercept_endpoint_group_association

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Intercept server.
        """
        return request, metadata

    def post_delete_intercept_endpoint_group_association(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_intercept_endpoint_group_association

        DEPRECATED. Please use the `post_delete_intercept_endpoint_group_association_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Intercept server but before
        it is returned to user code. This `post_delete_intercept_endpoint_group_association` interceptor runs
        before the `post_delete_intercept_endpoint_group_association_with_metadata` interceptor.
        """
        return response

    def post_delete_intercept_endpoint_group_association_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_intercept_endpoint_group_association

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Intercept server but before it is returned to user code.

        We recommend only using this `post_delete_intercept_endpoint_group_association_with_metadata`
        interceptor in new development instead of the `post_delete_intercept_endpoint_group_association` interceptor.
        When both interceptors are used, this `post_delete_intercept_endpoint_group_association_with_metadata` interceptor runs after the
        `post_delete_intercept_endpoint_group_association` interceptor. The (possibly modified) response returned by
        `post_delete_intercept_endpoint_group_association` will be passed to
        `post_delete_intercept_endpoint_group_association_with_metadata`.
        """
        return response, metadata

    def pre_get_intercept_deployment(
        self,
        request: intercept.GetInterceptDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        intercept.GetInterceptDeploymentRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_intercept_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Intercept server.
        """
        return request, metadata

    def post_get_intercept_deployment(
        self, response: intercept.InterceptDeployment
    ) -> intercept.InterceptDeployment:
        """Post-rpc interceptor for get_intercept_deployment

        DEPRECATED. Please use the `post_get_intercept_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Intercept server but before
        it is returned to user code. This `post_get_intercept_deployment` interceptor runs
        before the `post_get_intercept_deployment_with_metadata` interceptor.
        """
        return response

    def post_get_intercept_deployment_with_metadata(
        self,
        response: intercept.InterceptDeployment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[intercept.InterceptDeployment, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_intercept_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Intercept server but before it is returned to user code.

        We recommend only using this `post_get_intercept_deployment_with_metadata`
        interceptor in new development instead of the `post_get_intercept_deployment` interceptor.
        When both interceptors are used, this `post_get_intercept_deployment_with_metadata` interceptor runs after the
        `post_get_intercept_deployment` interceptor. The (possibly modified) response returned by
        `post_get_intercept_deployment` will be passed to
        `post_get_intercept_deployment_with_metadata`.
        """
        return response, metadata

    def pre_get_intercept_deployment_group(
        self,
        request: intercept.GetInterceptDeploymentGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        intercept.GetInterceptDeploymentGroupRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_intercept_deployment_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Intercept server.
        """
        return request, metadata

    def post_get_intercept_deployment_group(
        self, response: intercept.InterceptDeploymentGroup
    ) -> intercept.InterceptDeploymentGroup:
        """Post-rpc interceptor for get_intercept_deployment_group

        DEPRECATED. Please use the `post_get_intercept_deployment_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Intercept server but before
        it is returned to user code. This `post_get_intercept_deployment_group` interceptor runs
        before the `post_get_intercept_deployment_group_with_metadata` interceptor.
        """
        return response

    def post_get_intercept_deployment_group_with_metadata(
        self,
        response: intercept.InterceptDeploymentGroup,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        intercept.InterceptDeploymentGroup, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_intercept_deployment_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Intercept server but before it is returned to user code.

        We recommend only using this `post_get_intercept_deployment_group_with_metadata`
        interceptor in new development instead of the `post_get_intercept_deployment_group` interceptor.
        When both interceptors are used, this `post_get_intercept_deployment_group_with_metadata` interceptor runs after the
        `post_get_intercept_deployment_group` interceptor. The (possibly modified) response returned by
        `post_get_intercept_deployment_group` will be passed to
        `post_get_intercept_deployment_group_with_metadata`.
        """
        return response, metadata

    def pre_get_intercept_endpoint_group(
        self,
        request: intercept.GetInterceptEndpointGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        intercept.GetInterceptEndpointGroupRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_intercept_endpoint_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Intercept server.
        """
        return request, metadata

    def post_get_intercept_endpoint_group(
        self, response: intercept.InterceptEndpointGroup
    ) -> intercept.InterceptEndpointGroup:
        """Post-rpc interceptor for get_intercept_endpoint_group

        DEPRECATED. Please use the `post_get_intercept_endpoint_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Intercept server but before
        it is returned to user code. This `post_get_intercept_endpoint_group` interceptor runs
        before the `post_get_intercept_endpoint_group_with_metadata` interceptor.
        """
        return response

    def post_get_intercept_endpoint_group_with_metadata(
        self,
        response: intercept.InterceptEndpointGroup,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        intercept.InterceptEndpointGroup, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_intercept_endpoint_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Intercept server but before it is returned to user code.

        We recommend only using this `post_get_intercept_endpoint_group_with_metadata`
        interceptor in new development instead of the `post_get_intercept_endpoint_group` interceptor.
        When both interceptors are used, this `post_get_intercept_endpoint_group_with_metadata` interceptor runs after the
        `post_get_intercept_endpoint_group` interceptor. The (possibly modified) response returned by
        `post_get_intercept_endpoint_group` will be passed to
        `post_get_intercept_endpoint_group_with_metadata`.
        """
        return response, metadata

    def pre_get_intercept_endpoint_group_association(
        self,
        request: intercept.GetInterceptEndpointGroupAssociationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        intercept.GetInterceptEndpointGroupAssociationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_intercept_endpoint_group_association

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Intercept server.
        """
        return request, metadata

    def post_get_intercept_endpoint_group_association(
        self, response: intercept.InterceptEndpointGroupAssociation
    ) -> intercept.InterceptEndpointGroupAssociation:
        """Post-rpc interceptor for get_intercept_endpoint_group_association

        DEPRECATED. Please use the `post_get_intercept_endpoint_group_association_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Intercept server but before
        it is returned to user code. This `post_get_intercept_endpoint_group_association` interceptor runs
        before the `post_get_intercept_endpoint_group_association_with_metadata` interceptor.
        """
        return response

    def post_get_intercept_endpoint_group_association_with_metadata(
        self,
        response: intercept.InterceptEndpointGroupAssociation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        intercept.InterceptEndpointGroupAssociation,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_intercept_endpoint_group_association

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Intercept server but before it is returned to user code.

        We recommend only using this `post_get_intercept_endpoint_group_association_with_metadata`
        interceptor in new development instead of the `post_get_intercept_endpoint_group_association` interceptor.
        When both interceptors are used, this `post_get_intercept_endpoint_group_association_with_metadata` interceptor runs after the
        `post_get_intercept_endpoint_group_association` interceptor. The (possibly modified) response returned by
        `post_get_intercept_endpoint_group_association` will be passed to
        `post_get_intercept_endpoint_group_association_with_metadata`.
        """
        return response, metadata

    def pre_list_intercept_deployment_groups(
        self,
        request: intercept.ListInterceptDeploymentGroupsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        intercept.ListInterceptDeploymentGroupsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_intercept_deployment_groups

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Intercept server.
        """
        return request, metadata

    def post_list_intercept_deployment_groups(
        self, response: intercept.ListInterceptDeploymentGroupsResponse
    ) -> intercept.ListInterceptDeploymentGroupsResponse:
        """Post-rpc interceptor for list_intercept_deployment_groups

        DEPRECATED. Please use the `post_list_intercept_deployment_groups_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Intercept server but before
        it is returned to user code. This `post_list_intercept_deployment_groups` interceptor runs
        before the `post_list_intercept_deployment_groups_with_metadata` interceptor.
        """
        return response

    def post_list_intercept_deployment_groups_with_metadata(
        self,
        response: intercept.ListInterceptDeploymentGroupsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        intercept.ListInterceptDeploymentGroupsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_intercept_deployment_groups

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Intercept server but before it is returned to user code.

        We recommend only using this `post_list_intercept_deployment_groups_with_metadata`
        interceptor in new development instead of the `post_list_intercept_deployment_groups` interceptor.
        When both interceptors are used, this `post_list_intercept_deployment_groups_with_metadata` interceptor runs after the
        `post_list_intercept_deployment_groups` interceptor. The (possibly modified) response returned by
        `post_list_intercept_deployment_groups` will be passed to
        `post_list_intercept_deployment_groups_with_metadata`.
        """
        return response, metadata

    def pre_list_intercept_deployments(
        self,
        request: intercept.ListInterceptDeploymentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        intercept.ListInterceptDeploymentsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_intercept_deployments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Intercept server.
        """
        return request, metadata

    def post_list_intercept_deployments(
        self, response: intercept.ListInterceptDeploymentsResponse
    ) -> intercept.ListInterceptDeploymentsResponse:
        """Post-rpc interceptor for list_intercept_deployments

        DEPRECATED. Please use the `post_list_intercept_deployments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Intercept server but before
        it is returned to user code. This `post_list_intercept_deployments` interceptor runs
        before the `post_list_intercept_deployments_with_metadata` interceptor.
        """
        return response

    def post_list_intercept_deployments_with_metadata(
        self,
        response: intercept.ListInterceptDeploymentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        intercept.ListInterceptDeploymentsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_intercept_deployments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Intercept server but before it is returned to user code.

        We recommend only using this `post_list_intercept_deployments_with_metadata`
        interceptor in new development instead of the `post_list_intercept_deployments` interceptor.
        When both interceptors are used, this `post_list_intercept_deployments_with_metadata` interceptor runs after the
        `post_list_intercept_deployments` interceptor. The (possibly modified) response returned by
        `post_list_intercept_deployments` will be passed to
        `post_list_intercept_deployments_with_metadata`.
        """
        return response, metadata

    def pre_list_intercept_endpoint_group_associations(
        self,
        request: intercept.ListInterceptEndpointGroupAssociationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        intercept.ListInterceptEndpointGroupAssociationsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_intercept_endpoint_group_associations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Intercept server.
        """
        return request, metadata

    def post_list_intercept_endpoint_group_associations(
        self, response: intercept.ListInterceptEndpointGroupAssociationsResponse
    ) -> intercept.ListInterceptEndpointGroupAssociationsResponse:
        """Post-rpc interceptor for list_intercept_endpoint_group_associations

        DEPRECATED. Please use the `post_list_intercept_endpoint_group_associations_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Intercept server but before
        it is returned to user code. This `post_list_intercept_endpoint_group_associations` interceptor runs
        before the `post_list_intercept_endpoint_group_associations_with_metadata` interceptor.
        """
        return response

    def post_list_intercept_endpoint_group_associations_with_metadata(
        self,
        response: intercept.ListInterceptEndpointGroupAssociationsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        intercept.ListInterceptEndpointGroupAssociationsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_intercept_endpoint_group_associations

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Intercept server but before it is returned to user code.

        We recommend only using this `post_list_intercept_endpoint_group_associations_with_metadata`
        interceptor in new development instead of the `post_list_intercept_endpoint_group_associations` interceptor.
        When both interceptors are used, this `post_list_intercept_endpoint_group_associations_with_metadata` interceptor runs after the
        `post_list_intercept_endpoint_group_associations` interceptor. The (possibly modified) response returned by
        `post_list_intercept_endpoint_group_associations` will be passed to
        `post_list_intercept_endpoint_group_associations_with_metadata`.
        """
        return response, metadata

    def pre_list_intercept_endpoint_groups(
        self,
        request: intercept.ListInterceptEndpointGroupsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        intercept.ListInterceptEndpointGroupsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_intercept_endpoint_groups

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Intercept server.
        """
        return request, metadata

    def post_list_intercept_endpoint_groups(
        self, response: intercept.ListInterceptEndpointGroupsResponse
    ) -> intercept.ListInterceptEndpointGroupsResponse:
        """Post-rpc interceptor for list_intercept_endpoint_groups

        DEPRECATED. Please use the `post_list_intercept_endpoint_groups_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Intercept server but before
        it is returned to user code. This `post_list_intercept_endpoint_groups` interceptor runs
        before the `post_list_intercept_endpoint_groups_with_metadata` interceptor.
        """
        return response

    def post_list_intercept_endpoint_groups_with_metadata(
        self,
        response: intercept.ListInterceptEndpointGroupsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        intercept.ListInterceptEndpointGroupsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_intercept_endpoint_groups

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Intercept server but before it is returned to user code.

        We recommend only using this `post_list_intercept_endpoint_groups_with_metadata`
        interceptor in new development instead of the `post_list_intercept_endpoint_groups` interceptor.
        When both interceptors are used, this `post_list_intercept_endpoint_groups_with_metadata` interceptor runs after the
        `post_list_intercept_endpoint_groups` interceptor. The (possibly modified) response returned by
        `post_list_intercept_endpoint_groups` will be passed to
        `post_list_intercept_endpoint_groups_with_metadata`.
        """
        return response, metadata

    def pre_update_intercept_deployment(
        self,
        request: intercept.UpdateInterceptDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        intercept.UpdateInterceptDeploymentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_intercept_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Intercept server.
        """
        return request, metadata

    def post_update_intercept_deployment(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_intercept_deployment

        DEPRECATED. Please use the `post_update_intercept_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Intercept server but before
        it is returned to user code. This `post_update_intercept_deployment` interceptor runs
        before the `post_update_intercept_deployment_with_metadata` interceptor.
        """
        return response

    def post_update_intercept_deployment_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_intercept_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Intercept server but before it is returned to user code.

        We recommend only using this `post_update_intercept_deployment_with_metadata`
        interceptor in new development instead of the `post_update_intercept_deployment` interceptor.
        When both interceptors are used, this `post_update_intercept_deployment_with_metadata` interceptor runs after the
        `post_update_intercept_deployment` interceptor. The (possibly modified) response returned by
        `post_update_intercept_deployment` will be passed to
        `post_update_intercept_deployment_with_metadata`.
        """
        return response, metadata

    def pre_update_intercept_deployment_group(
        self,
        request: intercept.UpdateInterceptDeploymentGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        intercept.UpdateInterceptDeploymentGroupRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_intercept_deployment_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Intercept server.
        """
        return request, metadata

    def post_update_intercept_deployment_group(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_intercept_deployment_group

        DEPRECATED. Please use the `post_update_intercept_deployment_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Intercept server but before
        it is returned to user code. This `post_update_intercept_deployment_group` interceptor runs
        before the `post_update_intercept_deployment_group_with_metadata` interceptor.
        """
        return response

    def post_update_intercept_deployment_group_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_intercept_deployment_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Intercept server but before it is returned to user code.

        We recommend only using this `post_update_intercept_deployment_group_with_metadata`
        interceptor in new development instead of the `post_update_intercept_deployment_group` interceptor.
        When both interceptors are used, this `post_update_intercept_deployment_group_with_metadata` interceptor runs after the
        `post_update_intercept_deployment_group` interceptor. The (possibly modified) response returned by
        `post_update_intercept_deployment_group` will be passed to
        `post_update_intercept_deployment_group_with_metadata`.
        """
        return response, metadata

    def pre_update_intercept_endpoint_group(
        self,
        request: intercept.UpdateInterceptEndpointGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        intercept.UpdateInterceptEndpointGroupRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_intercept_endpoint_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Intercept server.
        """
        return request, metadata

    def post_update_intercept_endpoint_group(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_intercept_endpoint_group

        DEPRECATED. Please use the `post_update_intercept_endpoint_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Intercept server but before
        it is returned to user code. This `post_update_intercept_endpoint_group` interceptor runs
        before the `post_update_intercept_endpoint_group_with_metadata` interceptor.
        """
        return response

    def post_update_intercept_endpoint_group_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_intercept_endpoint_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Intercept server but before it is returned to user code.

        We recommend only using this `post_update_intercept_endpoint_group_with_metadata`
        interceptor in new development instead of the `post_update_intercept_endpoint_group` interceptor.
        When both interceptors are used, this `post_update_intercept_endpoint_group_with_metadata` interceptor runs after the
        `post_update_intercept_endpoint_group` interceptor. The (possibly modified) response returned by
        `post_update_intercept_endpoint_group` will be passed to
        `post_update_intercept_endpoint_group_with_metadata`.
        """
        return response, metadata

    def pre_update_intercept_endpoint_group_association(
        self,
        request: intercept.UpdateInterceptEndpointGroupAssociationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        intercept.UpdateInterceptEndpointGroupAssociationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_intercept_endpoint_group_association

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Intercept server.
        """
        return request, metadata

    def post_update_intercept_endpoint_group_association(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_intercept_endpoint_group_association

        DEPRECATED. Please use the `post_update_intercept_endpoint_group_association_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Intercept server but before
        it is returned to user code. This `post_update_intercept_endpoint_group_association` interceptor runs
        before the `post_update_intercept_endpoint_group_association_with_metadata` interceptor.
        """
        return response

    def post_update_intercept_endpoint_group_association_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_intercept_endpoint_group_association

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Intercept server but before it is returned to user code.

        We recommend only using this `post_update_intercept_endpoint_group_association_with_metadata`
        interceptor in new development instead of the `post_update_intercept_endpoint_group_association` interceptor.
        When both interceptors are used, this `post_update_intercept_endpoint_group_association_with_metadata` interceptor runs after the
        `post_update_intercept_endpoint_group_association` interceptor. The (possibly modified) response returned by
        `post_update_intercept_endpoint_group_association` will be passed to
        `post_update_intercept_endpoint_group_association_with_metadata`.
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
        before they are sent to the Intercept server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the Intercept server but before
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
        before they are sent to the Intercept server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the Intercept server but before
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
        before they are sent to the Intercept server.
        """
        return request, metadata

    def post_get_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the Intercept server but before
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
        before they are sent to the Intercept server.
        """
        return request, metadata

    def post_set_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the Intercept server but before
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
        before they are sent to the Intercept server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the response
        after it is returned by the Intercept server but before
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
        before they are sent to the Intercept server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the Intercept server but before
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
        before they are sent to the Intercept server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the Intercept server but before
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
        before they are sent to the Intercept server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the Intercept server but before
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
        before they are sent to the Intercept server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the Intercept server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class InterceptRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: InterceptRestInterceptor


class InterceptRestTransport(_BaseInterceptRestTransport):
    """REST backend synchronous transport for Intercept.

    Service for Third-Party Packet Intercept (TPPI).
    TPPI is the "in-band" flavor of the Network Security
    Integrations product.

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
        interceptor: Optional[InterceptRestInterceptor] = None,
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
            interceptor (Optional[InterceptRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or InterceptRestInterceptor()
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
                        "uri": "/v1alpha1/{name=projects/*/locations/*/operations/*}:cancel",
                        "body": "*",
                    },
                    {
                        "method": "post",
                        "uri": "/v1alpha1/{name=organizations/*/locations/*/operations/*}:cancel",
                        "body": "*",
                    },
                ],
                "google.longrunning.Operations.DeleteOperation": [
                    {
                        "method": "delete",
                        "uri": "/v1alpha1/{name=projects/*/locations/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1alpha1/{name=organizations/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v1alpha1/{name=projects/*/locations/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1alpha1/{name=organizations/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.ListOperations": [
                    {
                        "method": "get",
                        "uri": "/v1alpha1/{name=projects/*/locations/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1alpha1/{name=organizations/*/locations/*}/operations",
                    },
                ],
            }

            rest_transport = operations_v1.OperationsRestTransport(
                host=self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                scopes=self._scopes,
                http_options=http_options,
                path_prefix="v1alpha1",
            )

            self._operations_client = operations_v1.AbstractOperationsClient(
                transport=rest_transport
            )

        # Return the client from cache.
        return self._operations_client

    class _CreateInterceptDeployment(
        _BaseInterceptRestTransport._BaseCreateInterceptDeployment, InterceptRestStub
    ):
        def __hash__(self):
            return hash("InterceptRestTransport.CreateInterceptDeployment")

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
            request: intercept.CreateInterceptDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create intercept
            deployment method over HTTP.

                Args:
                    request (~.intercept.CreateInterceptDeploymentRequest):
                        The request object. Request message for
                    CreateInterceptDeployment.
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

            http_options = _BaseInterceptRestTransport._BaseCreateInterceptDeployment._get_http_options()
            request, metadata = self._interceptor.pre_create_intercept_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInterceptRestTransport._BaseCreateInterceptDeployment,
                    "_BaseCreateInterceptDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.InterceptClient.CreateInterceptDeployment",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "CreateInterceptDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InterceptRestTransport._CreateInterceptDeployment._get_response(
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

            resp = self._interceptor.post_create_intercept_deployment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_intercept_deployment_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.InterceptClient.create_intercept_deployment",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "CreateInterceptDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateInterceptDeploymentGroup(
        _BaseInterceptRestTransport._BaseCreateInterceptDeploymentGroup,
        InterceptRestStub,
    ):
        def __hash__(self):
            return hash("InterceptRestTransport.CreateInterceptDeploymentGroup")

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
            request: intercept.CreateInterceptDeploymentGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create intercept
            deployment group method over HTTP.

                Args:
                    request (~.intercept.CreateInterceptDeploymentGroupRequest):
                        The request object. Request message for
                    CreateInterceptDeploymentGroup.
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

            http_options = _BaseInterceptRestTransport._BaseCreateInterceptDeploymentGroup._get_http_options()
            request, metadata = self._interceptor.pre_create_intercept_deployment_group(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInterceptRestTransport._BaseCreateInterceptDeploymentGroup,
                    "_BaseCreateInterceptDeploymentGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.InterceptClient.CreateInterceptDeploymentGroup",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "CreateInterceptDeploymentGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                InterceptRestTransport._CreateInterceptDeploymentGroup._get_response(
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

            resp = self._interceptor.post_create_intercept_deployment_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_create_intercept_deployment_group_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.InterceptClient.create_intercept_deployment_group",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "CreateInterceptDeploymentGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateInterceptEndpointGroup(
        _BaseInterceptRestTransport._BaseCreateInterceptEndpointGroup, InterceptRestStub
    ):
        def __hash__(self):
            return hash("InterceptRestTransport.CreateInterceptEndpointGroup")

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
            request: intercept.CreateInterceptEndpointGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create intercept endpoint
            group method over HTTP.

                Args:
                    request (~.intercept.CreateInterceptEndpointGroupRequest):
                        The request object. Request message for
                    CreateInterceptEndpointGroup.
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

            http_options = _BaseInterceptRestTransport._BaseCreateInterceptEndpointGroup._get_http_options()
            request, metadata = self._interceptor.pre_create_intercept_endpoint_group(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInterceptRestTransport._BaseCreateInterceptEndpointGroup,
                    "_BaseCreateInterceptEndpointGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.InterceptClient.CreateInterceptEndpointGroup",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "CreateInterceptEndpointGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                InterceptRestTransport._CreateInterceptEndpointGroup._get_response(
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

            resp = self._interceptor.post_create_intercept_endpoint_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_create_intercept_endpoint_group_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.InterceptClient.create_intercept_endpoint_group",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "CreateInterceptEndpointGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateInterceptEndpointGroupAssociation(
        _BaseInterceptRestTransport._BaseCreateInterceptEndpointGroupAssociation,
        InterceptRestStub,
    ):
        def __hash__(self):
            return hash(
                "InterceptRestTransport.CreateInterceptEndpointGroupAssociation"
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
            request: intercept.CreateInterceptEndpointGroupAssociationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create intercept endpoint
            group association method over HTTP.

                Args:
                    request (~.intercept.CreateInterceptEndpointGroupAssociationRequest):
                        The request object. Request message for
                    CreateInterceptEndpointGroupAssociation.
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

            http_options = _BaseInterceptRestTransport._BaseCreateInterceptEndpointGroupAssociation._get_http_options()
            request, metadata = (
                self._interceptor.pre_create_intercept_endpoint_group_association(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInterceptRestTransport._BaseCreateInterceptEndpointGroupAssociation,
                    "_BaseCreateInterceptEndpointGroupAssociation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.InterceptClient.CreateInterceptEndpointGroupAssociation",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "CreateInterceptEndpointGroupAssociation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InterceptRestTransport._CreateInterceptEndpointGroupAssociation._get_response(
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

            resp = self._interceptor.post_create_intercept_endpoint_group_association(
                resp
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_create_intercept_endpoint_group_association_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.InterceptClient.create_intercept_endpoint_group_association",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "CreateInterceptEndpointGroupAssociation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteInterceptDeployment(
        _BaseInterceptRestTransport._BaseDeleteInterceptDeployment, InterceptRestStub
    ):
        def __hash__(self):
            return hash("InterceptRestTransport.DeleteInterceptDeployment")

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
            request: intercept.DeleteInterceptDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete intercept
            deployment method over HTTP.

                Args:
                    request (~.intercept.DeleteInterceptDeploymentRequest):
                        The request object. Request message for
                    DeleteInterceptDeployment.
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

            http_options = _BaseInterceptRestTransport._BaseDeleteInterceptDeployment._get_http_options()
            request, metadata = self._interceptor.pre_delete_intercept_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInterceptRestTransport._BaseDeleteInterceptDeployment,
                    "_BaseDeleteInterceptDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.InterceptClient.DeleteInterceptDeployment",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "DeleteInterceptDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InterceptRestTransport._DeleteInterceptDeployment._get_response(
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

            resp = self._interceptor.post_delete_intercept_deployment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_intercept_deployment_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.InterceptClient.delete_intercept_deployment",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "DeleteInterceptDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteInterceptDeploymentGroup(
        _BaseInterceptRestTransport._BaseDeleteInterceptDeploymentGroup,
        InterceptRestStub,
    ):
        def __hash__(self):
            return hash("InterceptRestTransport.DeleteInterceptDeploymentGroup")

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
            request: intercept.DeleteInterceptDeploymentGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete intercept
            deployment group method over HTTP.

                Args:
                    request (~.intercept.DeleteInterceptDeploymentGroupRequest):
                        The request object. Request message for
                    DeleteInterceptDeploymentGroup.
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

            http_options = _BaseInterceptRestTransport._BaseDeleteInterceptDeploymentGroup._get_http_options()
            request, metadata = self._interceptor.pre_delete_intercept_deployment_group(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInterceptRestTransport._BaseDeleteInterceptDeploymentGroup,
                    "_BaseDeleteInterceptDeploymentGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.InterceptClient.DeleteInterceptDeploymentGroup",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "DeleteInterceptDeploymentGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                InterceptRestTransport._DeleteInterceptDeploymentGroup._get_response(
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

            resp = self._interceptor.post_delete_intercept_deployment_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_delete_intercept_deployment_group_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.InterceptClient.delete_intercept_deployment_group",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "DeleteInterceptDeploymentGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteInterceptEndpointGroup(
        _BaseInterceptRestTransport._BaseDeleteInterceptEndpointGroup, InterceptRestStub
    ):
        def __hash__(self):
            return hash("InterceptRestTransport.DeleteInterceptEndpointGroup")

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
            request: intercept.DeleteInterceptEndpointGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete intercept endpoint
            group method over HTTP.

                Args:
                    request (~.intercept.DeleteInterceptEndpointGroupRequest):
                        The request object. Request message for
                    DeleteInterceptEndpointGroup.
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

            http_options = _BaseInterceptRestTransport._BaseDeleteInterceptEndpointGroup._get_http_options()
            request, metadata = self._interceptor.pre_delete_intercept_endpoint_group(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInterceptRestTransport._BaseDeleteInterceptEndpointGroup,
                    "_BaseDeleteInterceptEndpointGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.InterceptClient.DeleteInterceptEndpointGroup",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "DeleteInterceptEndpointGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                InterceptRestTransport._DeleteInterceptEndpointGroup._get_response(
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

            resp = self._interceptor.post_delete_intercept_endpoint_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_delete_intercept_endpoint_group_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.InterceptClient.delete_intercept_endpoint_group",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "DeleteInterceptEndpointGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteInterceptEndpointGroupAssociation(
        _BaseInterceptRestTransport._BaseDeleteInterceptEndpointGroupAssociation,
        InterceptRestStub,
    ):
        def __hash__(self):
            return hash(
                "InterceptRestTransport.DeleteInterceptEndpointGroupAssociation"
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
            request: intercept.DeleteInterceptEndpointGroupAssociationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete intercept endpoint
            group association method over HTTP.

                Args:
                    request (~.intercept.DeleteInterceptEndpointGroupAssociationRequest):
                        The request object. Request message for
                    DeleteInterceptEndpointGroupAssociation.
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

            http_options = _BaseInterceptRestTransport._BaseDeleteInterceptEndpointGroupAssociation._get_http_options()
            request, metadata = (
                self._interceptor.pre_delete_intercept_endpoint_group_association(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInterceptRestTransport._BaseDeleteInterceptEndpointGroupAssociation,
                    "_BaseDeleteInterceptEndpointGroupAssociation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.InterceptClient.DeleteInterceptEndpointGroupAssociation",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "DeleteInterceptEndpointGroupAssociation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InterceptRestTransport._DeleteInterceptEndpointGroupAssociation._get_response(
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

            resp = self._interceptor.post_delete_intercept_endpoint_group_association(
                resp
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_delete_intercept_endpoint_group_association_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.InterceptClient.delete_intercept_endpoint_group_association",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "DeleteInterceptEndpointGroupAssociation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetInterceptDeployment(
        _BaseInterceptRestTransport._BaseGetInterceptDeployment, InterceptRestStub
    ):
        def __hash__(self):
            return hash("InterceptRestTransport.GetInterceptDeployment")

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
            request: intercept.GetInterceptDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> intercept.InterceptDeployment:
            r"""Call the get intercept deployment method over HTTP.

            Args:
                request (~.intercept.GetInterceptDeploymentRequest):
                    The request object. Request message for
                GetInterceptDeployment.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.intercept.InterceptDeployment:
                    A deployment represents a zonal
                intercept backend ready to accept
                GENEVE-encapsulated traffic, e.g. a
                zonal instance group fronted by an
                internal passthrough load balancer.
                Deployments are always part of a global
                deployment group which represents a
                global intercept service.

            """

            http_options = _BaseInterceptRestTransport._BaseGetInterceptDeployment._get_http_options()
            request, metadata = self._interceptor.pre_get_intercept_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInterceptRestTransport._BaseGetInterceptDeployment,
                    "_BaseGetInterceptDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.InterceptClient.GetInterceptDeployment",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "GetInterceptDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InterceptRestTransport._GetInterceptDeployment._get_response(
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
            resp = intercept.InterceptDeployment()
            pb_resp = intercept.InterceptDeployment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_intercept_deployment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_intercept_deployment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = intercept.InterceptDeployment.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.networksecurity_v1alpha1.InterceptClient.get_intercept_deployment",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "GetInterceptDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetInterceptDeploymentGroup(
        _BaseInterceptRestTransport._BaseGetInterceptDeploymentGroup, InterceptRestStub
    ):
        def __hash__(self):
            return hash("InterceptRestTransport.GetInterceptDeploymentGroup")

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
            request: intercept.GetInterceptDeploymentGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> intercept.InterceptDeploymentGroup:
            r"""Call the get intercept deployment
            group method over HTTP.

                Args:
                    request (~.intercept.GetInterceptDeploymentGroupRequest):
                        The request object. Request message for
                    GetInterceptDeploymentGroup.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.intercept.InterceptDeploymentGroup:
                        A deployment group aggregates many
                    zonal intercept backends (deployments)
                    into a single global intercept service.
                    Consumers can connect this service using
                    an endpoint group.

            """

            http_options = _BaseInterceptRestTransport._BaseGetInterceptDeploymentGroup._get_http_options()
            request, metadata = self._interceptor.pre_get_intercept_deployment_group(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInterceptRestTransport._BaseGetInterceptDeploymentGroup,
                    "_BaseGetInterceptDeploymentGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.InterceptClient.GetInterceptDeploymentGroup",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "GetInterceptDeploymentGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                InterceptRestTransport._GetInterceptDeploymentGroup._get_response(
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
            resp = intercept.InterceptDeploymentGroup()
            pb_resp = intercept.InterceptDeploymentGroup.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_intercept_deployment_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_get_intercept_deployment_group_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = intercept.InterceptDeploymentGroup.to_json(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.InterceptClient.get_intercept_deployment_group",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "GetInterceptDeploymentGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetInterceptEndpointGroup(
        _BaseInterceptRestTransport._BaseGetInterceptEndpointGroup, InterceptRestStub
    ):
        def __hash__(self):
            return hash("InterceptRestTransport.GetInterceptEndpointGroup")

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
            request: intercept.GetInterceptEndpointGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> intercept.InterceptEndpointGroup:
            r"""Call the get intercept endpoint
            group method over HTTP.

                Args:
                    request (~.intercept.GetInterceptEndpointGroupRequest):
                        The request object. Request message for
                    GetInterceptEndpointGroup.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.intercept.InterceptEndpointGroup:
                        An endpoint group is a consumer
                    frontend for a deployment group
                    (backend). In order to configure
                    intercept for a network, consumers must
                    create:

                    - An association between their network
                      and the endpoint group.
                    - A security profile that points to the
                      endpoint group.
                    - A firewall rule that references the
                      security profile (group).

            """

            http_options = _BaseInterceptRestTransport._BaseGetInterceptEndpointGroup._get_http_options()
            request, metadata = self._interceptor.pre_get_intercept_endpoint_group(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInterceptRestTransport._BaseGetInterceptEndpointGroup,
                    "_BaseGetInterceptEndpointGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.InterceptClient.GetInterceptEndpointGroup",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "GetInterceptEndpointGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InterceptRestTransport._GetInterceptEndpointGroup._get_response(
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
            resp = intercept.InterceptEndpointGroup()
            pb_resp = intercept.InterceptEndpointGroup.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_intercept_endpoint_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_intercept_endpoint_group_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = intercept.InterceptEndpointGroup.to_json(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.InterceptClient.get_intercept_endpoint_group",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "GetInterceptEndpointGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetInterceptEndpointGroupAssociation(
        _BaseInterceptRestTransport._BaseGetInterceptEndpointGroupAssociation,
        InterceptRestStub,
    ):
        def __hash__(self):
            return hash("InterceptRestTransport.GetInterceptEndpointGroupAssociation")

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
            request: intercept.GetInterceptEndpointGroupAssociationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> intercept.InterceptEndpointGroupAssociation:
            r"""Call the get intercept endpoint
            group association method over HTTP.

                Args:
                    request (~.intercept.GetInterceptEndpointGroupAssociationRequest):
                        The request object. Request message for
                    GetInterceptEndpointGroupAssociation.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.intercept.InterceptEndpointGroupAssociation:
                        An endpoint group association
                    represents a link between a network and
                    an endpoint group in the organization.

                    Creating an association creates the
                    networking infrastructure linking the
                    network to the endpoint group, but does
                    not enable intercept by itself. To
                    enable intercept, the user must also
                    create a network firewall policy
                    containing intercept rules and associate
                    it with the network.

            """

            http_options = _BaseInterceptRestTransport._BaseGetInterceptEndpointGroupAssociation._get_http_options()
            request, metadata = (
                self._interceptor.pre_get_intercept_endpoint_group_association(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInterceptRestTransport._BaseGetInterceptEndpointGroupAssociation,
                    "_BaseGetInterceptEndpointGroupAssociation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.InterceptClient.GetInterceptEndpointGroupAssociation",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "GetInterceptEndpointGroupAssociation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InterceptRestTransport._GetInterceptEndpointGroupAssociation._get_response(
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
            resp = intercept.InterceptEndpointGroupAssociation()
            pb_resp = intercept.InterceptEndpointGroupAssociation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_intercept_endpoint_group_association(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_get_intercept_endpoint_group_association_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        intercept.InterceptEndpointGroupAssociation.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.networksecurity_v1alpha1.InterceptClient.get_intercept_endpoint_group_association",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "GetInterceptEndpointGroupAssociation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListInterceptDeploymentGroups(
        _BaseInterceptRestTransport._BaseListInterceptDeploymentGroups,
        InterceptRestStub,
    ):
        def __hash__(self):
            return hash("InterceptRestTransport.ListInterceptDeploymentGroups")

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
            request: intercept.ListInterceptDeploymentGroupsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> intercept.ListInterceptDeploymentGroupsResponse:
            r"""Call the list intercept deployment
            groups method over HTTP.

                Args:
                    request (~.intercept.ListInterceptDeploymentGroupsRequest):
                        The request object. Request message for
                    ListInterceptDeploymentGroups.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.intercept.ListInterceptDeploymentGroupsResponse:
                        Response message for
                    ListInterceptDeploymentGroups.

            """

            http_options = _BaseInterceptRestTransport._BaseListInterceptDeploymentGroups._get_http_options()
            request, metadata = self._interceptor.pre_list_intercept_deployment_groups(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInterceptRestTransport._BaseListInterceptDeploymentGroups,
                    "_BaseListInterceptDeploymentGroups__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.InterceptClient.ListInterceptDeploymentGroups",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "ListInterceptDeploymentGroups",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                InterceptRestTransport._ListInterceptDeploymentGroups._get_response(
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
            resp = intercept.ListInterceptDeploymentGroupsResponse()
            pb_resp = intercept.ListInterceptDeploymentGroupsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_intercept_deployment_groups(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_intercept_deployment_groups_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        intercept.ListInterceptDeploymentGroupsResponse.to_json(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.InterceptClient.list_intercept_deployment_groups",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "ListInterceptDeploymentGroups",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListInterceptDeployments(
        _BaseInterceptRestTransport._BaseListInterceptDeployments, InterceptRestStub
    ):
        def __hash__(self):
            return hash("InterceptRestTransport.ListInterceptDeployments")

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
            request: intercept.ListInterceptDeploymentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> intercept.ListInterceptDeploymentsResponse:
            r"""Call the list intercept
            deployments method over HTTP.

                Args:
                    request (~.intercept.ListInterceptDeploymentsRequest):
                        The request object. Request message for
                    ListInterceptDeployments.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.intercept.ListInterceptDeploymentsResponse:
                        Response message for
                    ListInterceptDeployments.

            """

            http_options = _BaseInterceptRestTransport._BaseListInterceptDeployments._get_http_options()
            request, metadata = self._interceptor.pre_list_intercept_deployments(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInterceptRestTransport._BaseListInterceptDeployments,
                    "_BaseListInterceptDeployments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.InterceptClient.ListInterceptDeployments",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "ListInterceptDeployments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InterceptRestTransport._ListInterceptDeployments._get_response(
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
            resp = intercept.ListInterceptDeploymentsResponse()
            pb_resp = intercept.ListInterceptDeploymentsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_intercept_deployments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_intercept_deployments_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        intercept.ListInterceptDeploymentsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.networksecurity_v1alpha1.InterceptClient.list_intercept_deployments",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "ListInterceptDeployments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListInterceptEndpointGroupAssociations(
        _BaseInterceptRestTransport._BaseListInterceptEndpointGroupAssociations,
        InterceptRestStub,
    ):
        def __hash__(self):
            return hash("InterceptRestTransport.ListInterceptEndpointGroupAssociations")

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
            request: intercept.ListInterceptEndpointGroupAssociationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> intercept.ListInterceptEndpointGroupAssociationsResponse:
            r"""Call the list intercept endpoint
            group associations method over HTTP.

                Args:
                    request (~.intercept.ListInterceptEndpointGroupAssociationsRequest):
                        The request object. Request message for
                    ListInterceptEndpointGroupAssociations.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.intercept.ListInterceptEndpointGroupAssociationsResponse:
                        Response message for
                    ListInterceptEndpointGroupAssociations.

            """

            http_options = _BaseInterceptRestTransport._BaseListInterceptEndpointGroupAssociations._get_http_options()
            request, metadata = (
                self._interceptor.pre_list_intercept_endpoint_group_associations(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInterceptRestTransport._BaseListInterceptEndpointGroupAssociations,
                    "_BaseListInterceptEndpointGroupAssociations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.InterceptClient.ListInterceptEndpointGroupAssociations",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "ListInterceptEndpointGroupAssociations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InterceptRestTransport._ListInterceptEndpointGroupAssociations._get_response(
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
            resp = intercept.ListInterceptEndpointGroupAssociationsResponse()
            pb_resp = intercept.ListInterceptEndpointGroupAssociationsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_intercept_endpoint_group_associations(
                resp
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_intercept_endpoint_group_associations_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = intercept.ListInterceptEndpointGroupAssociationsResponse.to_json(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.InterceptClient.list_intercept_endpoint_group_associations",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "ListInterceptEndpointGroupAssociations",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListInterceptEndpointGroups(
        _BaseInterceptRestTransport._BaseListInterceptEndpointGroups, InterceptRestStub
    ):
        def __hash__(self):
            return hash("InterceptRestTransport.ListInterceptEndpointGroups")

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
            request: intercept.ListInterceptEndpointGroupsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> intercept.ListInterceptEndpointGroupsResponse:
            r"""Call the list intercept endpoint
            groups method over HTTP.

                Args:
                    request (~.intercept.ListInterceptEndpointGroupsRequest):
                        The request object. Request message for
                    ListInterceptEndpointGroups.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.intercept.ListInterceptEndpointGroupsResponse:
                        Response message for
                    ListInterceptEndpointGroups.

            """

            http_options = _BaseInterceptRestTransport._BaseListInterceptEndpointGroups._get_http_options()
            request, metadata = self._interceptor.pre_list_intercept_endpoint_groups(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInterceptRestTransport._BaseListInterceptEndpointGroups,
                    "_BaseListInterceptEndpointGroups__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.InterceptClient.ListInterceptEndpointGroups",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "ListInterceptEndpointGroups",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                InterceptRestTransport._ListInterceptEndpointGroups._get_response(
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
            resp = intercept.ListInterceptEndpointGroupsResponse()
            pb_resp = intercept.ListInterceptEndpointGroupsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_intercept_endpoint_groups(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_intercept_endpoint_groups_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        intercept.ListInterceptEndpointGroupsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.networksecurity_v1alpha1.InterceptClient.list_intercept_endpoint_groups",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "ListInterceptEndpointGroups",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateInterceptDeployment(
        _BaseInterceptRestTransport._BaseUpdateInterceptDeployment, InterceptRestStub
    ):
        def __hash__(self):
            return hash("InterceptRestTransport.UpdateInterceptDeployment")

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
            request: intercept.UpdateInterceptDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update intercept
            deployment method over HTTP.

                Args:
                    request (~.intercept.UpdateInterceptDeploymentRequest):
                        The request object. Request message for
                    UpdateInterceptDeployment.
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

            http_options = _BaseInterceptRestTransport._BaseUpdateInterceptDeployment._get_http_options()
            request, metadata = self._interceptor.pre_update_intercept_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInterceptRestTransport._BaseUpdateInterceptDeployment,
                    "_BaseUpdateInterceptDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.InterceptClient.UpdateInterceptDeployment",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "UpdateInterceptDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InterceptRestTransport._UpdateInterceptDeployment._get_response(
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

            resp = self._interceptor.post_update_intercept_deployment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_intercept_deployment_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.InterceptClient.update_intercept_deployment",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "UpdateInterceptDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateInterceptDeploymentGroup(
        _BaseInterceptRestTransport._BaseUpdateInterceptDeploymentGroup,
        InterceptRestStub,
    ):
        def __hash__(self):
            return hash("InterceptRestTransport.UpdateInterceptDeploymentGroup")

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
            request: intercept.UpdateInterceptDeploymentGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update intercept
            deployment group method over HTTP.

                Args:
                    request (~.intercept.UpdateInterceptDeploymentGroupRequest):
                        The request object. Request message for
                    UpdateInterceptDeploymentGroup.
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

            http_options = _BaseInterceptRestTransport._BaseUpdateInterceptDeploymentGroup._get_http_options()
            request, metadata = self._interceptor.pre_update_intercept_deployment_group(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInterceptRestTransport._BaseUpdateInterceptDeploymentGroup,
                    "_BaseUpdateInterceptDeploymentGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.InterceptClient.UpdateInterceptDeploymentGroup",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "UpdateInterceptDeploymentGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                InterceptRestTransport._UpdateInterceptDeploymentGroup._get_response(
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

            resp = self._interceptor.post_update_intercept_deployment_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_update_intercept_deployment_group_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.InterceptClient.update_intercept_deployment_group",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "UpdateInterceptDeploymentGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateInterceptEndpointGroup(
        _BaseInterceptRestTransport._BaseUpdateInterceptEndpointGroup, InterceptRestStub
    ):
        def __hash__(self):
            return hash("InterceptRestTransport.UpdateInterceptEndpointGroup")

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
            request: intercept.UpdateInterceptEndpointGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update intercept endpoint
            group method over HTTP.

                Args:
                    request (~.intercept.UpdateInterceptEndpointGroupRequest):
                        The request object. Request message for
                    UpdateInterceptEndpointGroup.
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

            http_options = _BaseInterceptRestTransport._BaseUpdateInterceptEndpointGroup._get_http_options()
            request, metadata = self._interceptor.pre_update_intercept_endpoint_group(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInterceptRestTransport._BaseUpdateInterceptEndpointGroup,
                    "_BaseUpdateInterceptEndpointGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.InterceptClient.UpdateInterceptEndpointGroup",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "UpdateInterceptEndpointGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                InterceptRestTransport._UpdateInterceptEndpointGroup._get_response(
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

            resp = self._interceptor.post_update_intercept_endpoint_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_update_intercept_endpoint_group_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.InterceptClient.update_intercept_endpoint_group",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "UpdateInterceptEndpointGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateInterceptEndpointGroupAssociation(
        _BaseInterceptRestTransport._BaseUpdateInterceptEndpointGroupAssociation,
        InterceptRestStub,
    ):
        def __hash__(self):
            return hash(
                "InterceptRestTransport.UpdateInterceptEndpointGroupAssociation"
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
            request: intercept.UpdateInterceptEndpointGroupAssociationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update intercept endpoint
            group association method over HTTP.

                Args:
                    request (~.intercept.UpdateInterceptEndpointGroupAssociationRequest):
                        The request object. Request message for
                    UpdateInterceptEndpointGroupAssociation.
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

            http_options = _BaseInterceptRestTransport._BaseUpdateInterceptEndpointGroupAssociation._get_http_options()
            request, metadata = (
                self._interceptor.pre_update_intercept_endpoint_group_association(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInterceptRestTransport._BaseUpdateInterceptEndpointGroupAssociation,
                    "_BaseUpdateInterceptEndpointGroupAssociation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.InterceptClient.UpdateInterceptEndpointGroupAssociation",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "UpdateInterceptEndpointGroupAssociation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InterceptRestTransport._UpdateInterceptEndpointGroupAssociation._get_response(
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

            resp = self._interceptor.post_update_intercept_endpoint_group_association(
                resp
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_update_intercept_endpoint_group_association_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.InterceptClient.update_intercept_endpoint_group_association",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "UpdateInterceptEndpointGroupAssociation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_intercept_deployment(
        self,
    ) -> Callable[
        [intercept.CreateInterceptDeploymentRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateInterceptDeployment(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_intercept_deployment_group(
        self,
    ) -> Callable[
        [intercept.CreateInterceptDeploymentGroupRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateInterceptDeploymentGroup(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_intercept_endpoint_group(
        self,
    ) -> Callable[
        [intercept.CreateInterceptEndpointGroupRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateInterceptEndpointGroup(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_intercept_endpoint_group_association(
        self,
    ) -> Callable[
        [intercept.CreateInterceptEndpointGroupAssociationRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateInterceptEndpointGroupAssociation(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_intercept_deployment(
        self,
    ) -> Callable[
        [intercept.DeleteInterceptDeploymentRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteInterceptDeployment(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_intercept_deployment_group(
        self,
    ) -> Callable[
        [intercept.DeleteInterceptDeploymentGroupRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteInterceptDeploymentGroup(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_intercept_endpoint_group(
        self,
    ) -> Callable[
        [intercept.DeleteInterceptEndpointGroupRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteInterceptEndpointGroup(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_intercept_endpoint_group_association(
        self,
    ) -> Callable[
        [intercept.DeleteInterceptEndpointGroupAssociationRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteInterceptEndpointGroupAssociation(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_intercept_deployment(
        self,
    ) -> Callable[
        [intercept.GetInterceptDeploymentRequest], intercept.InterceptDeployment
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetInterceptDeployment(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_intercept_deployment_group(
        self,
    ) -> Callable[
        [intercept.GetInterceptDeploymentGroupRequest],
        intercept.InterceptDeploymentGroup,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetInterceptDeploymentGroup(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_intercept_endpoint_group(
        self,
    ) -> Callable[
        [intercept.GetInterceptEndpointGroupRequest], intercept.InterceptEndpointGroup
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetInterceptEndpointGroup(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_intercept_endpoint_group_association(
        self,
    ) -> Callable[
        [intercept.GetInterceptEndpointGroupAssociationRequest],
        intercept.InterceptEndpointGroupAssociation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetInterceptEndpointGroupAssociation(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_intercept_deployment_groups(
        self,
    ) -> Callable[
        [intercept.ListInterceptDeploymentGroupsRequest],
        intercept.ListInterceptDeploymentGroupsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListInterceptDeploymentGroups(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_intercept_deployments(
        self,
    ) -> Callable[
        [intercept.ListInterceptDeploymentsRequest],
        intercept.ListInterceptDeploymentsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListInterceptDeployments(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_intercept_endpoint_group_associations(
        self,
    ) -> Callable[
        [intercept.ListInterceptEndpointGroupAssociationsRequest],
        intercept.ListInterceptEndpointGroupAssociationsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListInterceptEndpointGroupAssociations(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_intercept_endpoint_groups(
        self,
    ) -> Callable[
        [intercept.ListInterceptEndpointGroupsRequest],
        intercept.ListInterceptEndpointGroupsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListInterceptEndpointGroups(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_intercept_deployment(
        self,
    ) -> Callable[
        [intercept.UpdateInterceptDeploymentRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateInterceptDeployment(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_intercept_deployment_group(
        self,
    ) -> Callable[
        [intercept.UpdateInterceptDeploymentGroupRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateInterceptDeploymentGroup(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_intercept_endpoint_group(
        self,
    ) -> Callable[
        [intercept.UpdateInterceptEndpointGroupRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateInterceptEndpointGroup(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_intercept_endpoint_group_association(
        self,
    ) -> Callable[
        [intercept.UpdateInterceptEndpointGroupAssociationRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateInterceptEndpointGroupAssociation(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(_BaseInterceptRestTransport._BaseGetLocation, InterceptRestStub):
        def __hash__(self):
            return hash("InterceptRestTransport.GetLocation")

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
                _BaseInterceptRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInterceptRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.InterceptClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InterceptRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.InterceptAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
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
        _BaseInterceptRestTransport._BaseListLocations, InterceptRestStub
    ):
        def __hash__(self):
            return hash("InterceptRestTransport.ListLocations")

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
                _BaseInterceptRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInterceptRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.InterceptClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InterceptRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.InterceptAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
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
        _BaseInterceptRestTransport._BaseGetIamPolicy, InterceptRestStub
    ):
        def __hash__(self):
            return hash("InterceptRestTransport.GetIamPolicy")

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
                _BaseInterceptRestTransport._BaseGetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInterceptRestTransport._BaseGetIamPolicy,
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.InterceptClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "GetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InterceptRestTransport._GetIamPolicy._get_response(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.InterceptAsyncClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
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
        _BaseInterceptRestTransport._BaseSetIamPolicy, InterceptRestStub
    ):
        def __hash__(self):
            return hash("InterceptRestTransport.SetIamPolicy")

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
                _BaseInterceptRestTransport._BaseSetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInterceptRestTransport._BaseSetIamPolicy,
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.InterceptClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "SetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InterceptRestTransport._SetIamPolicy._get_response(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.InterceptAsyncClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
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
        _BaseInterceptRestTransport._BaseTestIamPermissions, InterceptRestStub
    ):
        def __hash__(self):
            return hash("InterceptRestTransport.TestIamPermissions")

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

            http_options = (
                _BaseInterceptRestTransport._BaseTestIamPermissions._get_http_options()
            )
            request, metadata = self._interceptor.pre_test_iam_permissions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInterceptRestTransport._BaseTestIamPermissions,
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.InterceptClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "TestIamPermissions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InterceptRestTransport._TestIamPermissions._get_response(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.InterceptAsyncClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
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
        _BaseInterceptRestTransport._BaseCancelOperation, InterceptRestStub
    ):
        def __hash__(self):
            return hash("InterceptRestTransport.CancelOperation")

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
                _BaseInterceptRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInterceptRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.InterceptClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InterceptRestTransport._CancelOperation._get_response(
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
        _BaseInterceptRestTransport._BaseDeleteOperation, InterceptRestStub
    ):
        def __hash__(self):
            return hash("InterceptRestTransport.DeleteOperation")

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
                _BaseInterceptRestTransport._BaseDeleteOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInterceptRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.InterceptClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InterceptRestTransport._DeleteOperation._get_response(
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
        _BaseInterceptRestTransport._BaseGetOperation, InterceptRestStub
    ):
        def __hash__(self):
            return hash("InterceptRestTransport.GetOperation")

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
                _BaseInterceptRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInterceptRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.InterceptClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InterceptRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.InterceptAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
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
        _BaseInterceptRestTransport._BaseListOperations, InterceptRestStub
    ):
        def __hash__(self):
            return hash("InterceptRestTransport.ListOperations")

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
                _BaseInterceptRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseInterceptRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.InterceptClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = InterceptRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.InterceptAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Intercept",
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


__all__ = ("InterceptRestTransport",)
