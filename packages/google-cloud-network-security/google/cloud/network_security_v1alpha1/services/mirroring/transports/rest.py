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
from google.cloud.network_security_v1alpha1.types import mirroring

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseMirroringRestTransport

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


class MirroringRestInterceptor:
    """Interceptor for Mirroring.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the MirroringRestTransport.

    .. code-block:: python
        class MyCustomMirroringInterceptor(MirroringRestInterceptor):
            def pre_create_mirroring_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_mirroring_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_mirroring_deployment_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_mirroring_deployment_group(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_mirroring_endpoint_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_mirroring_endpoint_group(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_mirroring_endpoint_group_association(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_mirroring_endpoint_group_association(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_mirroring_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_mirroring_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_mirroring_deployment_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_mirroring_deployment_group(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_mirroring_endpoint_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_mirroring_endpoint_group(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_mirroring_endpoint_group_association(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_mirroring_endpoint_group_association(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_mirroring_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_mirroring_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_mirroring_deployment_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_mirroring_deployment_group(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_mirroring_endpoint_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_mirroring_endpoint_group(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_mirroring_endpoint_group_association(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_mirroring_endpoint_group_association(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_mirroring_deployment_groups(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_mirroring_deployment_groups(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_mirroring_deployments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_mirroring_deployments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_mirroring_endpoint_group_associations(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_mirroring_endpoint_group_associations(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_mirroring_endpoint_groups(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_mirroring_endpoint_groups(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_mirroring_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_mirroring_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_mirroring_deployment_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_mirroring_deployment_group(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_mirroring_endpoint_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_mirroring_endpoint_group(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_mirroring_endpoint_group_association(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_mirroring_endpoint_group_association(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = MirroringRestTransport(interceptor=MyCustomMirroringInterceptor())
        client = MirroringClient(transport=transport)


    """

    def pre_create_mirroring_deployment(
        self,
        request: mirroring.CreateMirroringDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        mirroring.CreateMirroringDeploymentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_mirroring_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Mirroring server.
        """
        return request, metadata

    def post_create_mirroring_deployment(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_mirroring_deployment

        DEPRECATED. Please use the `post_create_mirroring_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Mirroring server but before
        it is returned to user code. This `post_create_mirroring_deployment` interceptor runs
        before the `post_create_mirroring_deployment_with_metadata` interceptor.
        """
        return response

    def post_create_mirroring_deployment_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_mirroring_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Mirroring server but before it is returned to user code.

        We recommend only using this `post_create_mirroring_deployment_with_metadata`
        interceptor in new development instead of the `post_create_mirroring_deployment` interceptor.
        When both interceptors are used, this `post_create_mirroring_deployment_with_metadata` interceptor runs after the
        `post_create_mirroring_deployment` interceptor. The (possibly modified) response returned by
        `post_create_mirroring_deployment` will be passed to
        `post_create_mirroring_deployment_with_metadata`.
        """
        return response, metadata

    def pre_create_mirroring_deployment_group(
        self,
        request: mirroring.CreateMirroringDeploymentGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        mirroring.CreateMirroringDeploymentGroupRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_mirroring_deployment_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Mirroring server.
        """
        return request, metadata

    def post_create_mirroring_deployment_group(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_mirroring_deployment_group

        DEPRECATED. Please use the `post_create_mirroring_deployment_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Mirroring server but before
        it is returned to user code. This `post_create_mirroring_deployment_group` interceptor runs
        before the `post_create_mirroring_deployment_group_with_metadata` interceptor.
        """
        return response

    def post_create_mirroring_deployment_group_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_mirroring_deployment_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Mirroring server but before it is returned to user code.

        We recommend only using this `post_create_mirroring_deployment_group_with_metadata`
        interceptor in new development instead of the `post_create_mirroring_deployment_group` interceptor.
        When both interceptors are used, this `post_create_mirroring_deployment_group_with_metadata` interceptor runs after the
        `post_create_mirroring_deployment_group` interceptor. The (possibly modified) response returned by
        `post_create_mirroring_deployment_group` will be passed to
        `post_create_mirroring_deployment_group_with_metadata`.
        """
        return response, metadata

    def pre_create_mirroring_endpoint_group(
        self,
        request: mirroring.CreateMirroringEndpointGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        mirroring.CreateMirroringEndpointGroupRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_mirroring_endpoint_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Mirroring server.
        """
        return request, metadata

    def post_create_mirroring_endpoint_group(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_mirroring_endpoint_group

        DEPRECATED. Please use the `post_create_mirroring_endpoint_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Mirroring server but before
        it is returned to user code. This `post_create_mirroring_endpoint_group` interceptor runs
        before the `post_create_mirroring_endpoint_group_with_metadata` interceptor.
        """
        return response

    def post_create_mirroring_endpoint_group_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_mirroring_endpoint_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Mirroring server but before it is returned to user code.

        We recommend only using this `post_create_mirroring_endpoint_group_with_metadata`
        interceptor in new development instead of the `post_create_mirroring_endpoint_group` interceptor.
        When both interceptors are used, this `post_create_mirroring_endpoint_group_with_metadata` interceptor runs after the
        `post_create_mirroring_endpoint_group` interceptor. The (possibly modified) response returned by
        `post_create_mirroring_endpoint_group` will be passed to
        `post_create_mirroring_endpoint_group_with_metadata`.
        """
        return response, metadata

    def pre_create_mirroring_endpoint_group_association(
        self,
        request: mirroring.CreateMirroringEndpointGroupAssociationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        mirroring.CreateMirroringEndpointGroupAssociationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_mirroring_endpoint_group_association

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Mirroring server.
        """
        return request, metadata

    def post_create_mirroring_endpoint_group_association(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_mirroring_endpoint_group_association

        DEPRECATED. Please use the `post_create_mirroring_endpoint_group_association_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Mirroring server but before
        it is returned to user code. This `post_create_mirroring_endpoint_group_association` interceptor runs
        before the `post_create_mirroring_endpoint_group_association_with_metadata` interceptor.
        """
        return response

    def post_create_mirroring_endpoint_group_association_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_mirroring_endpoint_group_association

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Mirroring server but before it is returned to user code.

        We recommend only using this `post_create_mirroring_endpoint_group_association_with_metadata`
        interceptor in new development instead of the `post_create_mirroring_endpoint_group_association` interceptor.
        When both interceptors are used, this `post_create_mirroring_endpoint_group_association_with_metadata` interceptor runs after the
        `post_create_mirroring_endpoint_group_association` interceptor. The (possibly modified) response returned by
        `post_create_mirroring_endpoint_group_association` will be passed to
        `post_create_mirroring_endpoint_group_association_with_metadata`.
        """
        return response, metadata

    def pre_delete_mirroring_deployment(
        self,
        request: mirroring.DeleteMirroringDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        mirroring.DeleteMirroringDeploymentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_mirroring_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Mirroring server.
        """
        return request, metadata

    def post_delete_mirroring_deployment(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_mirroring_deployment

        DEPRECATED. Please use the `post_delete_mirroring_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Mirroring server but before
        it is returned to user code. This `post_delete_mirroring_deployment` interceptor runs
        before the `post_delete_mirroring_deployment_with_metadata` interceptor.
        """
        return response

    def post_delete_mirroring_deployment_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_mirroring_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Mirroring server but before it is returned to user code.

        We recommend only using this `post_delete_mirroring_deployment_with_metadata`
        interceptor in new development instead of the `post_delete_mirroring_deployment` interceptor.
        When both interceptors are used, this `post_delete_mirroring_deployment_with_metadata` interceptor runs after the
        `post_delete_mirroring_deployment` interceptor. The (possibly modified) response returned by
        `post_delete_mirroring_deployment` will be passed to
        `post_delete_mirroring_deployment_with_metadata`.
        """
        return response, metadata

    def pre_delete_mirroring_deployment_group(
        self,
        request: mirroring.DeleteMirroringDeploymentGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        mirroring.DeleteMirroringDeploymentGroupRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_mirroring_deployment_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Mirroring server.
        """
        return request, metadata

    def post_delete_mirroring_deployment_group(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_mirroring_deployment_group

        DEPRECATED. Please use the `post_delete_mirroring_deployment_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Mirroring server but before
        it is returned to user code. This `post_delete_mirroring_deployment_group` interceptor runs
        before the `post_delete_mirroring_deployment_group_with_metadata` interceptor.
        """
        return response

    def post_delete_mirroring_deployment_group_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_mirroring_deployment_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Mirroring server but before it is returned to user code.

        We recommend only using this `post_delete_mirroring_deployment_group_with_metadata`
        interceptor in new development instead of the `post_delete_mirroring_deployment_group` interceptor.
        When both interceptors are used, this `post_delete_mirroring_deployment_group_with_metadata` interceptor runs after the
        `post_delete_mirroring_deployment_group` interceptor. The (possibly modified) response returned by
        `post_delete_mirroring_deployment_group` will be passed to
        `post_delete_mirroring_deployment_group_with_metadata`.
        """
        return response, metadata

    def pre_delete_mirroring_endpoint_group(
        self,
        request: mirroring.DeleteMirroringEndpointGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        mirroring.DeleteMirroringEndpointGroupRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_mirroring_endpoint_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Mirroring server.
        """
        return request, metadata

    def post_delete_mirroring_endpoint_group(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_mirroring_endpoint_group

        DEPRECATED. Please use the `post_delete_mirroring_endpoint_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Mirroring server but before
        it is returned to user code. This `post_delete_mirroring_endpoint_group` interceptor runs
        before the `post_delete_mirroring_endpoint_group_with_metadata` interceptor.
        """
        return response

    def post_delete_mirroring_endpoint_group_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_mirroring_endpoint_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Mirroring server but before it is returned to user code.

        We recommend only using this `post_delete_mirroring_endpoint_group_with_metadata`
        interceptor in new development instead of the `post_delete_mirroring_endpoint_group` interceptor.
        When both interceptors are used, this `post_delete_mirroring_endpoint_group_with_metadata` interceptor runs after the
        `post_delete_mirroring_endpoint_group` interceptor. The (possibly modified) response returned by
        `post_delete_mirroring_endpoint_group` will be passed to
        `post_delete_mirroring_endpoint_group_with_metadata`.
        """
        return response, metadata

    def pre_delete_mirroring_endpoint_group_association(
        self,
        request: mirroring.DeleteMirroringEndpointGroupAssociationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        mirroring.DeleteMirroringEndpointGroupAssociationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_mirroring_endpoint_group_association

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Mirroring server.
        """
        return request, metadata

    def post_delete_mirroring_endpoint_group_association(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_mirroring_endpoint_group_association

        DEPRECATED. Please use the `post_delete_mirroring_endpoint_group_association_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Mirroring server but before
        it is returned to user code. This `post_delete_mirroring_endpoint_group_association` interceptor runs
        before the `post_delete_mirroring_endpoint_group_association_with_metadata` interceptor.
        """
        return response

    def post_delete_mirroring_endpoint_group_association_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_mirroring_endpoint_group_association

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Mirroring server but before it is returned to user code.

        We recommend only using this `post_delete_mirroring_endpoint_group_association_with_metadata`
        interceptor in new development instead of the `post_delete_mirroring_endpoint_group_association` interceptor.
        When both interceptors are used, this `post_delete_mirroring_endpoint_group_association_with_metadata` interceptor runs after the
        `post_delete_mirroring_endpoint_group_association` interceptor. The (possibly modified) response returned by
        `post_delete_mirroring_endpoint_group_association` will be passed to
        `post_delete_mirroring_endpoint_group_association_with_metadata`.
        """
        return response, metadata

    def pre_get_mirroring_deployment(
        self,
        request: mirroring.GetMirroringDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        mirroring.GetMirroringDeploymentRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_mirroring_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Mirroring server.
        """
        return request, metadata

    def post_get_mirroring_deployment(
        self, response: mirroring.MirroringDeployment
    ) -> mirroring.MirroringDeployment:
        """Post-rpc interceptor for get_mirroring_deployment

        DEPRECATED. Please use the `post_get_mirroring_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Mirroring server but before
        it is returned to user code. This `post_get_mirroring_deployment` interceptor runs
        before the `post_get_mirroring_deployment_with_metadata` interceptor.
        """
        return response

    def post_get_mirroring_deployment_with_metadata(
        self,
        response: mirroring.MirroringDeployment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[mirroring.MirroringDeployment, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_mirroring_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Mirroring server but before it is returned to user code.

        We recommend only using this `post_get_mirroring_deployment_with_metadata`
        interceptor in new development instead of the `post_get_mirroring_deployment` interceptor.
        When both interceptors are used, this `post_get_mirroring_deployment_with_metadata` interceptor runs after the
        `post_get_mirroring_deployment` interceptor. The (possibly modified) response returned by
        `post_get_mirroring_deployment` will be passed to
        `post_get_mirroring_deployment_with_metadata`.
        """
        return response, metadata

    def pre_get_mirroring_deployment_group(
        self,
        request: mirroring.GetMirroringDeploymentGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        mirroring.GetMirroringDeploymentGroupRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_mirroring_deployment_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Mirroring server.
        """
        return request, metadata

    def post_get_mirroring_deployment_group(
        self, response: mirroring.MirroringDeploymentGroup
    ) -> mirroring.MirroringDeploymentGroup:
        """Post-rpc interceptor for get_mirroring_deployment_group

        DEPRECATED. Please use the `post_get_mirroring_deployment_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Mirroring server but before
        it is returned to user code. This `post_get_mirroring_deployment_group` interceptor runs
        before the `post_get_mirroring_deployment_group_with_metadata` interceptor.
        """
        return response

    def post_get_mirroring_deployment_group_with_metadata(
        self,
        response: mirroring.MirroringDeploymentGroup,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        mirroring.MirroringDeploymentGroup, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_mirroring_deployment_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Mirroring server but before it is returned to user code.

        We recommend only using this `post_get_mirroring_deployment_group_with_metadata`
        interceptor in new development instead of the `post_get_mirroring_deployment_group` interceptor.
        When both interceptors are used, this `post_get_mirroring_deployment_group_with_metadata` interceptor runs after the
        `post_get_mirroring_deployment_group` interceptor. The (possibly modified) response returned by
        `post_get_mirroring_deployment_group` will be passed to
        `post_get_mirroring_deployment_group_with_metadata`.
        """
        return response, metadata

    def pre_get_mirroring_endpoint_group(
        self,
        request: mirroring.GetMirroringEndpointGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        mirroring.GetMirroringEndpointGroupRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_mirroring_endpoint_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Mirroring server.
        """
        return request, metadata

    def post_get_mirroring_endpoint_group(
        self, response: mirroring.MirroringEndpointGroup
    ) -> mirroring.MirroringEndpointGroup:
        """Post-rpc interceptor for get_mirroring_endpoint_group

        DEPRECATED. Please use the `post_get_mirroring_endpoint_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Mirroring server but before
        it is returned to user code. This `post_get_mirroring_endpoint_group` interceptor runs
        before the `post_get_mirroring_endpoint_group_with_metadata` interceptor.
        """
        return response

    def post_get_mirroring_endpoint_group_with_metadata(
        self,
        response: mirroring.MirroringEndpointGroup,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        mirroring.MirroringEndpointGroup, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_mirroring_endpoint_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Mirroring server but before it is returned to user code.

        We recommend only using this `post_get_mirroring_endpoint_group_with_metadata`
        interceptor in new development instead of the `post_get_mirroring_endpoint_group` interceptor.
        When both interceptors are used, this `post_get_mirroring_endpoint_group_with_metadata` interceptor runs after the
        `post_get_mirroring_endpoint_group` interceptor. The (possibly modified) response returned by
        `post_get_mirroring_endpoint_group` will be passed to
        `post_get_mirroring_endpoint_group_with_metadata`.
        """
        return response, metadata

    def pre_get_mirroring_endpoint_group_association(
        self,
        request: mirroring.GetMirroringEndpointGroupAssociationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        mirroring.GetMirroringEndpointGroupAssociationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_mirroring_endpoint_group_association

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Mirroring server.
        """
        return request, metadata

    def post_get_mirroring_endpoint_group_association(
        self, response: mirroring.MirroringEndpointGroupAssociation
    ) -> mirroring.MirroringEndpointGroupAssociation:
        """Post-rpc interceptor for get_mirroring_endpoint_group_association

        DEPRECATED. Please use the `post_get_mirroring_endpoint_group_association_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Mirroring server but before
        it is returned to user code. This `post_get_mirroring_endpoint_group_association` interceptor runs
        before the `post_get_mirroring_endpoint_group_association_with_metadata` interceptor.
        """
        return response

    def post_get_mirroring_endpoint_group_association_with_metadata(
        self,
        response: mirroring.MirroringEndpointGroupAssociation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        mirroring.MirroringEndpointGroupAssociation,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_mirroring_endpoint_group_association

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Mirroring server but before it is returned to user code.

        We recommend only using this `post_get_mirroring_endpoint_group_association_with_metadata`
        interceptor in new development instead of the `post_get_mirroring_endpoint_group_association` interceptor.
        When both interceptors are used, this `post_get_mirroring_endpoint_group_association_with_metadata` interceptor runs after the
        `post_get_mirroring_endpoint_group_association` interceptor. The (possibly modified) response returned by
        `post_get_mirroring_endpoint_group_association` will be passed to
        `post_get_mirroring_endpoint_group_association_with_metadata`.
        """
        return response, metadata

    def pre_list_mirroring_deployment_groups(
        self,
        request: mirroring.ListMirroringDeploymentGroupsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        mirroring.ListMirroringDeploymentGroupsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_mirroring_deployment_groups

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Mirroring server.
        """
        return request, metadata

    def post_list_mirroring_deployment_groups(
        self, response: mirroring.ListMirroringDeploymentGroupsResponse
    ) -> mirroring.ListMirroringDeploymentGroupsResponse:
        """Post-rpc interceptor for list_mirroring_deployment_groups

        DEPRECATED. Please use the `post_list_mirroring_deployment_groups_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Mirroring server but before
        it is returned to user code. This `post_list_mirroring_deployment_groups` interceptor runs
        before the `post_list_mirroring_deployment_groups_with_metadata` interceptor.
        """
        return response

    def post_list_mirroring_deployment_groups_with_metadata(
        self,
        response: mirroring.ListMirroringDeploymentGroupsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        mirroring.ListMirroringDeploymentGroupsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_mirroring_deployment_groups

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Mirroring server but before it is returned to user code.

        We recommend only using this `post_list_mirroring_deployment_groups_with_metadata`
        interceptor in new development instead of the `post_list_mirroring_deployment_groups` interceptor.
        When both interceptors are used, this `post_list_mirroring_deployment_groups_with_metadata` interceptor runs after the
        `post_list_mirroring_deployment_groups` interceptor. The (possibly modified) response returned by
        `post_list_mirroring_deployment_groups` will be passed to
        `post_list_mirroring_deployment_groups_with_metadata`.
        """
        return response, metadata

    def pre_list_mirroring_deployments(
        self,
        request: mirroring.ListMirroringDeploymentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        mirroring.ListMirroringDeploymentsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_mirroring_deployments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Mirroring server.
        """
        return request, metadata

    def post_list_mirroring_deployments(
        self, response: mirroring.ListMirroringDeploymentsResponse
    ) -> mirroring.ListMirroringDeploymentsResponse:
        """Post-rpc interceptor for list_mirroring_deployments

        DEPRECATED. Please use the `post_list_mirroring_deployments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Mirroring server but before
        it is returned to user code. This `post_list_mirroring_deployments` interceptor runs
        before the `post_list_mirroring_deployments_with_metadata` interceptor.
        """
        return response

    def post_list_mirroring_deployments_with_metadata(
        self,
        response: mirroring.ListMirroringDeploymentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        mirroring.ListMirroringDeploymentsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_mirroring_deployments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Mirroring server but before it is returned to user code.

        We recommend only using this `post_list_mirroring_deployments_with_metadata`
        interceptor in new development instead of the `post_list_mirroring_deployments` interceptor.
        When both interceptors are used, this `post_list_mirroring_deployments_with_metadata` interceptor runs after the
        `post_list_mirroring_deployments` interceptor. The (possibly modified) response returned by
        `post_list_mirroring_deployments` will be passed to
        `post_list_mirroring_deployments_with_metadata`.
        """
        return response, metadata

    def pre_list_mirroring_endpoint_group_associations(
        self,
        request: mirroring.ListMirroringEndpointGroupAssociationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        mirroring.ListMirroringEndpointGroupAssociationsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_mirroring_endpoint_group_associations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Mirroring server.
        """
        return request, metadata

    def post_list_mirroring_endpoint_group_associations(
        self, response: mirroring.ListMirroringEndpointGroupAssociationsResponse
    ) -> mirroring.ListMirroringEndpointGroupAssociationsResponse:
        """Post-rpc interceptor for list_mirroring_endpoint_group_associations

        DEPRECATED. Please use the `post_list_mirroring_endpoint_group_associations_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Mirroring server but before
        it is returned to user code. This `post_list_mirroring_endpoint_group_associations` interceptor runs
        before the `post_list_mirroring_endpoint_group_associations_with_metadata` interceptor.
        """
        return response

    def post_list_mirroring_endpoint_group_associations_with_metadata(
        self,
        response: mirroring.ListMirroringEndpointGroupAssociationsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        mirroring.ListMirroringEndpointGroupAssociationsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_mirroring_endpoint_group_associations

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Mirroring server but before it is returned to user code.

        We recommend only using this `post_list_mirroring_endpoint_group_associations_with_metadata`
        interceptor in new development instead of the `post_list_mirroring_endpoint_group_associations` interceptor.
        When both interceptors are used, this `post_list_mirroring_endpoint_group_associations_with_metadata` interceptor runs after the
        `post_list_mirroring_endpoint_group_associations` interceptor. The (possibly modified) response returned by
        `post_list_mirroring_endpoint_group_associations` will be passed to
        `post_list_mirroring_endpoint_group_associations_with_metadata`.
        """
        return response, metadata

    def pre_list_mirroring_endpoint_groups(
        self,
        request: mirroring.ListMirroringEndpointGroupsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        mirroring.ListMirroringEndpointGroupsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_mirroring_endpoint_groups

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Mirroring server.
        """
        return request, metadata

    def post_list_mirroring_endpoint_groups(
        self, response: mirroring.ListMirroringEndpointGroupsResponse
    ) -> mirroring.ListMirroringEndpointGroupsResponse:
        """Post-rpc interceptor for list_mirroring_endpoint_groups

        DEPRECATED. Please use the `post_list_mirroring_endpoint_groups_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Mirroring server but before
        it is returned to user code. This `post_list_mirroring_endpoint_groups` interceptor runs
        before the `post_list_mirroring_endpoint_groups_with_metadata` interceptor.
        """
        return response

    def post_list_mirroring_endpoint_groups_with_metadata(
        self,
        response: mirroring.ListMirroringEndpointGroupsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        mirroring.ListMirroringEndpointGroupsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_mirroring_endpoint_groups

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Mirroring server but before it is returned to user code.

        We recommend only using this `post_list_mirroring_endpoint_groups_with_metadata`
        interceptor in new development instead of the `post_list_mirroring_endpoint_groups` interceptor.
        When both interceptors are used, this `post_list_mirroring_endpoint_groups_with_metadata` interceptor runs after the
        `post_list_mirroring_endpoint_groups` interceptor. The (possibly modified) response returned by
        `post_list_mirroring_endpoint_groups` will be passed to
        `post_list_mirroring_endpoint_groups_with_metadata`.
        """
        return response, metadata

    def pre_update_mirroring_deployment(
        self,
        request: mirroring.UpdateMirroringDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        mirroring.UpdateMirroringDeploymentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_mirroring_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Mirroring server.
        """
        return request, metadata

    def post_update_mirroring_deployment(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_mirroring_deployment

        DEPRECATED. Please use the `post_update_mirroring_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Mirroring server but before
        it is returned to user code. This `post_update_mirroring_deployment` interceptor runs
        before the `post_update_mirroring_deployment_with_metadata` interceptor.
        """
        return response

    def post_update_mirroring_deployment_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_mirroring_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Mirroring server but before it is returned to user code.

        We recommend only using this `post_update_mirroring_deployment_with_metadata`
        interceptor in new development instead of the `post_update_mirroring_deployment` interceptor.
        When both interceptors are used, this `post_update_mirroring_deployment_with_metadata` interceptor runs after the
        `post_update_mirroring_deployment` interceptor. The (possibly modified) response returned by
        `post_update_mirroring_deployment` will be passed to
        `post_update_mirroring_deployment_with_metadata`.
        """
        return response, metadata

    def pre_update_mirroring_deployment_group(
        self,
        request: mirroring.UpdateMirroringDeploymentGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        mirroring.UpdateMirroringDeploymentGroupRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_mirroring_deployment_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Mirroring server.
        """
        return request, metadata

    def post_update_mirroring_deployment_group(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_mirroring_deployment_group

        DEPRECATED. Please use the `post_update_mirroring_deployment_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Mirroring server but before
        it is returned to user code. This `post_update_mirroring_deployment_group` interceptor runs
        before the `post_update_mirroring_deployment_group_with_metadata` interceptor.
        """
        return response

    def post_update_mirroring_deployment_group_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_mirroring_deployment_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Mirroring server but before it is returned to user code.

        We recommend only using this `post_update_mirroring_deployment_group_with_metadata`
        interceptor in new development instead of the `post_update_mirroring_deployment_group` interceptor.
        When both interceptors are used, this `post_update_mirroring_deployment_group_with_metadata` interceptor runs after the
        `post_update_mirroring_deployment_group` interceptor. The (possibly modified) response returned by
        `post_update_mirroring_deployment_group` will be passed to
        `post_update_mirroring_deployment_group_with_metadata`.
        """
        return response, metadata

    def pre_update_mirroring_endpoint_group(
        self,
        request: mirroring.UpdateMirroringEndpointGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        mirroring.UpdateMirroringEndpointGroupRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_mirroring_endpoint_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Mirroring server.
        """
        return request, metadata

    def post_update_mirroring_endpoint_group(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_mirroring_endpoint_group

        DEPRECATED. Please use the `post_update_mirroring_endpoint_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Mirroring server but before
        it is returned to user code. This `post_update_mirroring_endpoint_group` interceptor runs
        before the `post_update_mirroring_endpoint_group_with_metadata` interceptor.
        """
        return response

    def post_update_mirroring_endpoint_group_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_mirroring_endpoint_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Mirroring server but before it is returned to user code.

        We recommend only using this `post_update_mirroring_endpoint_group_with_metadata`
        interceptor in new development instead of the `post_update_mirroring_endpoint_group` interceptor.
        When both interceptors are used, this `post_update_mirroring_endpoint_group_with_metadata` interceptor runs after the
        `post_update_mirroring_endpoint_group` interceptor. The (possibly modified) response returned by
        `post_update_mirroring_endpoint_group` will be passed to
        `post_update_mirroring_endpoint_group_with_metadata`.
        """
        return response, metadata

    def pre_update_mirroring_endpoint_group_association(
        self,
        request: mirroring.UpdateMirroringEndpointGroupAssociationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        mirroring.UpdateMirroringEndpointGroupAssociationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_mirroring_endpoint_group_association

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Mirroring server.
        """
        return request, metadata

    def post_update_mirroring_endpoint_group_association(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_mirroring_endpoint_group_association

        DEPRECATED. Please use the `post_update_mirroring_endpoint_group_association_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Mirroring server but before
        it is returned to user code. This `post_update_mirroring_endpoint_group_association` interceptor runs
        before the `post_update_mirroring_endpoint_group_association_with_metadata` interceptor.
        """
        return response

    def post_update_mirroring_endpoint_group_association_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_mirroring_endpoint_group_association

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Mirroring server but before it is returned to user code.

        We recommend only using this `post_update_mirroring_endpoint_group_association_with_metadata`
        interceptor in new development instead of the `post_update_mirroring_endpoint_group_association` interceptor.
        When both interceptors are used, this `post_update_mirroring_endpoint_group_association_with_metadata` interceptor runs after the
        `post_update_mirroring_endpoint_group_association` interceptor. The (possibly modified) response returned by
        `post_update_mirroring_endpoint_group_association` will be passed to
        `post_update_mirroring_endpoint_group_association_with_metadata`.
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
        before they are sent to the Mirroring server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the Mirroring server but before
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
        before they are sent to the Mirroring server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the Mirroring server but before
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
        before they are sent to the Mirroring server.
        """
        return request, metadata

    def post_get_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the Mirroring server but before
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
        before they are sent to the Mirroring server.
        """
        return request, metadata

    def post_set_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the Mirroring server but before
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
        before they are sent to the Mirroring server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the response
        after it is returned by the Mirroring server but before
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
        before they are sent to the Mirroring server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the Mirroring server but before
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
        before they are sent to the Mirroring server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the Mirroring server but before
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
        before they are sent to the Mirroring server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the Mirroring server but before
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
        before they are sent to the Mirroring server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the Mirroring server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class MirroringRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: MirroringRestInterceptor


class MirroringRestTransport(_BaseMirroringRestTransport):
    """REST backend synchronous transport for Mirroring.

    PM2 is the "out-of-band" flavor of the Network Security
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
        interceptor: Optional[MirroringRestInterceptor] = None,
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
            interceptor (Optional[MirroringRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or MirroringRestInterceptor()
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

    class _CreateMirroringDeployment(
        _BaseMirroringRestTransport._BaseCreateMirroringDeployment, MirroringRestStub
    ):
        def __hash__(self):
            return hash("MirroringRestTransport.CreateMirroringDeployment")

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
            request: mirroring.CreateMirroringDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create mirroring
            deployment method over HTTP.

                Args:
                    request (~.mirroring.CreateMirroringDeploymentRequest):
                        The request object. Request message for
                    CreateMirroringDeployment.
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

            http_options = _BaseMirroringRestTransport._BaseCreateMirroringDeployment._get_http_options()
            request, metadata = self._interceptor.pre_create_mirroring_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMirroringRestTransport._BaseCreateMirroringDeployment,
                    "_BaseCreateMirroringDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.MirroringClient.CreateMirroringDeployment",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "CreateMirroringDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MirroringRestTransport._CreateMirroringDeployment._get_response(
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

            resp = self._interceptor.post_create_mirroring_deployment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_mirroring_deployment_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.MirroringClient.create_mirroring_deployment",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "CreateMirroringDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateMirroringDeploymentGroup(
        _BaseMirroringRestTransport._BaseCreateMirroringDeploymentGroup,
        MirroringRestStub,
    ):
        def __hash__(self):
            return hash("MirroringRestTransport.CreateMirroringDeploymentGroup")

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
            request: mirroring.CreateMirroringDeploymentGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create mirroring
            deployment group method over HTTP.

                Args:
                    request (~.mirroring.CreateMirroringDeploymentGroupRequest):
                        The request object. Request message for
                    CreateMirroringDeploymentGroup.
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

            http_options = _BaseMirroringRestTransport._BaseCreateMirroringDeploymentGroup._get_http_options()
            request, metadata = self._interceptor.pre_create_mirroring_deployment_group(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMirroringRestTransport._BaseCreateMirroringDeploymentGroup,
                    "_BaseCreateMirroringDeploymentGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.MirroringClient.CreateMirroringDeploymentGroup",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "CreateMirroringDeploymentGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                MirroringRestTransport._CreateMirroringDeploymentGroup._get_response(
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

            resp = self._interceptor.post_create_mirroring_deployment_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_create_mirroring_deployment_group_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.MirroringClient.create_mirroring_deployment_group",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "CreateMirroringDeploymentGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateMirroringEndpointGroup(
        _BaseMirroringRestTransport._BaseCreateMirroringEndpointGroup, MirroringRestStub
    ):
        def __hash__(self):
            return hash("MirroringRestTransport.CreateMirroringEndpointGroup")

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
            request: mirroring.CreateMirroringEndpointGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create mirroring endpoint
            group method over HTTP.

                Args:
                    request (~.mirroring.CreateMirroringEndpointGroupRequest):
                        The request object. Request message for
                    CreateMirroringEndpointGroup.
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

            http_options = _BaseMirroringRestTransport._BaseCreateMirroringEndpointGroup._get_http_options()
            request, metadata = self._interceptor.pre_create_mirroring_endpoint_group(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMirroringRestTransport._BaseCreateMirroringEndpointGroup,
                    "_BaseCreateMirroringEndpointGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.MirroringClient.CreateMirroringEndpointGroup",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "CreateMirroringEndpointGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                MirroringRestTransport._CreateMirroringEndpointGroup._get_response(
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

            resp = self._interceptor.post_create_mirroring_endpoint_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_create_mirroring_endpoint_group_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.MirroringClient.create_mirroring_endpoint_group",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "CreateMirroringEndpointGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateMirroringEndpointGroupAssociation(
        _BaseMirroringRestTransport._BaseCreateMirroringEndpointGroupAssociation,
        MirroringRestStub,
    ):
        def __hash__(self):
            return hash(
                "MirroringRestTransport.CreateMirroringEndpointGroupAssociation"
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
            request: mirroring.CreateMirroringEndpointGroupAssociationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create mirroring endpoint
            group association method over HTTP.

                Args:
                    request (~.mirroring.CreateMirroringEndpointGroupAssociationRequest):
                        The request object. Request message for
                    CreateMirroringEndpointGroupAssociation.
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

            http_options = _BaseMirroringRestTransport._BaseCreateMirroringEndpointGroupAssociation._get_http_options()
            request, metadata = (
                self._interceptor.pre_create_mirroring_endpoint_group_association(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMirroringRestTransport._BaseCreateMirroringEndpointGroupAssociation,
                    "_BaseCreateMirroringEndpointGroupAssociation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.MirroringClient.CreateMirroringEndpointGroupAssociation",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "CreateMirroringEndpointGroupAssociation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MirroringRestTransport._CreateMirroringEndpointGroupAssociation._get_response(
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

            resp = self._interceptor.post_create_mirroring_endpoint_group_association(
                resp
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_create_mirroring_endpoint_group_association_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.MirroringClient.create_mirroring_endpoint_group_association",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "CreateMirroringEndpointGroupAssociation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteMirroringDeployment(
        _BaseMirroringRestTransport._BaseDeleteMirroringDeployment, MirroringRestStub
    ):
        def __hash__(self):
            return hash("MirroringRestTransport.DeleteMirroringDeployment")

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
            request: mirroring.DeleteMirroringDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete mirroring
            deployment method over HTTP.

                Args:
                    request (~.mirroring.DeleteMirroringDeploymentRequest):
                        The request object. Request message for
                    DeleteMirroringDeployment.
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

            http_options = _BaseMirroringRestTransport._BaseDeleteMirroringDeployment._get_http_options()
            request, metadata = self._interceptor.pre_delete_mirroring_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMirroringRestTransport._BaseDeleteMirroringDeployment,
                    "_BaseDeleteMirroringDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.MirroringClient.DeleteMirroringDeployment",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "DeleteMirroringDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MirroringRestTransport._DeleteMirroringDeployment._get_response(
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

            resp = self._interceptor.post_delete_mirroring_deployment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_mirroring_deployment_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.MirroringClient.delete_mirroring_deployment",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "DeleteMirroringDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteMirroringDeploymentGroup(
        _BaseMirroringRestTransport._BaseDeleteMirroringDeploymentGroup,
        MirroringRestStub,
    ):
        def __hash__(self):
            return hash("MirroringRestTransport.DeleteMirroringDeploymentGroup")

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
            request: mirroring.DeleteMirroringDeploymentGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete mirroring
            deployment group method over HTTP.

                Args:
                    request (~.mirroring.DeleteMirroringDeploymentGroupRequest):
                        The request object. Request message for
                    DeleteMirroringDeploymentGroup.
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

            http_options = _BaseMirroringRestTransport._BaseDeleteMirroringDeploymentGroup._get_http_options()
            request, metadata = self._interceptor.pre_delete_mirroring_deployment_group(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMirroringRestTransport._BaseDeleteMirroringDeploymentGroup,
                    "_BaseDeleteMirroringDeploymentGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.MirroringClient.DeleteMirroringDeploymentGroup",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "DeleteMirroringDeploymentGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                MirroringRestTransport._DeleteMirroringDeploymentGroup._get_response(
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

            resp = self._interceptor.post_delete_mirroring_deployment_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_delete_mirroring_deployment_group_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.MirroringClient.delete_mirroring_deployment_group",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "DeleteMirroringDeploymentGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteMirroringEndpointGroup(
        _BaseMirroringRestTransport._BaseDeleteMirroringEndpointGroup, MirroringRestStub
    ):
        def __hash__(self):
            return hash("MirroringRestTransport.DeleteMirroringEndpointGroup")

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
            request: mirroring.DeleteMirroringEndpointGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete mirroring endpoint
            group method over HTTP.

                Args:
                    request (~.mirroring.DeleteMirroringEndpointGroupRequest):
                        The request object. Request message for
                    DeleteMirroringEndpointGroup.
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

            http_options = _BaseMirroringRestTransport._BaseDeleteMirroringEndpointGroup._get_http_options()
            request, metadata = self._interceptor.pre_delete_mirroring_endpoint_group(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMirroringRestTransport._BaseDeleteMirroringEndpointGroup,
                    "_BaseDeleteMirroringEndpointGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.MirroringClient.DeleteMirroringEndpointGroup",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "DeleteMirroringEndpointGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                MirroringRestTransport._DeleteMirroringEndpointGroup._get_response(
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

            resp = self._interceptor.post_delete_mirroring_endpoint_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_delete_mirroring_endpoint_group_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.MirroringClient.delete_mirroring_endpoint_group",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "DeleteMirroringEndpointGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteMirroringEndpointGroupAssociation(
        _BaseMirroringRestTransport._BaseDeleteMirroringEndpointGroupAssociation,
        MirroringRestStub,
    ):
        def __hash__(self):
            return hash(
                "MirroringRestTransport.DeleteMirroringEndpointGroupAssociation"
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
            request: mirroring.DeleteMirroringEndpointGroupAssociationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete mirroring endpoint
            group association method over HTTP.

                Args:
                    request (~.mirroring.DeleteMirroringEndpointGroupAssociationRequest):
                        The request object. Request message for
                    DeleteMirroringEndpointGroupAssociation.
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

            http_options = _BaseMirroringRestTransport._BaseDeleteMirroringEndpointGroupAssociation._get_http_options()
            request, metadata = (
                self._interceptor.pre_delete_mirroring_endpoint_group_association(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMirroringRestTransport._BaseDeleteMirroringEndpointGroupAssociation,
                    "_BaseDeleteMirroringEndpointGroupAssociation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.MirroringClient.DeleteMirroringEndpointGroupAssociation",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "DeleteMirroringEndpointGroupAssociation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MirroringRestTransport._DeleteMirroringEndpointGroupAssociation._get_response(
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

            resp = self._interceptor.post_delete_mirroring_endpoint_group_association(
                resp
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_delete_mirroring_endpoint_group_association_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.MirroringClient.delete_mirroring_endpoint_group_association",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "DeleteMirroringEndpointGroupAssociation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetMirroringDeployment(
        _BaseMirroringRestTransport._BaseGetMirroringDeployment, MirroringRestStub
    ):
        def __hash__(self):
            return hash("MirroringRestTransport.GetMirroringDeployment")

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
            request: mirroring.GetMirroringDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> mirroring.MirroringDeployment:
            r"""Call the get mirroring deployment method over HTTP.

            Args:
                request (~.mirroring.GetMirroringDeploymentRequest):
                    The request object. Request message for
                GetMirroringDeployment.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.mirroring.MirroringDeployment:
                    A deployment represents a zonal
                mirroring backend ready to accept
                GENEVE-encapsulated replica traffic,
                e.g. a zonal instance group fronted by
                an internal passthrough load balancer.
                Deployments are always part of a global
                deployment group which represents a
                global mirroring service.

            """

            http_options = _BaseMirroringRestTransport._BaseGetMirroringDeployment._get_http_options()
            request, metadata = self._interceptor.pre_get_mirroring_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMirroringRestTransport._BaseGetMirroringDeployment,
                    "_BaseGetMirroringDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.MirroringClient.GetMirroringDeployment",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "GetMirroringDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MirroringRestTransport._GetMirroringDeployment._get_response(
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
            resp = mirroring.MirroringDeployment()
            pb_resp = mirroring.MirroringDeployment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_mirroring_deployment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_mirroring_deployment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = mirroring.MirroringDeployment.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.networksecurity_v1alpha1.MirroringClient.get_mirroring_deployment",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "GetMirroringDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetMirroringDeploymentGroup(
        _BaseMirroringRestTransport._BaseGetMirroringDeploymentGroup, MirroringRestStub
    ):
        def __hash__(self):
            return hash("MirroringRestTransport.GetMirroringDeploymentGroup")

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
            request: mirroring.GetMirroringDeploymentGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> mirroring.MirroringDeploymentGroup:
            r"""Call the get mirroring deployment
            group method over HTTP.

                Args:
                    request (~.mirroring.GetMirroringDeploymentGroupRequest):
                        The request object. Request message for
                    GetMirroringDeploymentGroup.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.mirroring.MirroringDeploymentGroup:
                        A deployment group aggregates many
                    zonal mirroring backends (deployments)
                    into a single global mirroring service.
                    Consumers can connect this service using
                    an endpoint group.

            """

            http_options = _BaseMirroringRestTransport._BaseGetMirroringDeploymentGroup._get_http_options()
            request, metadata = self._interceptor.pre_get_mirroring_deployment_group(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMirroringRestTransport._BaseGetMirroringDeploymentGroup,
                    "_BaseGetMirroringDeploymentGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.MirroringClient.GetMirroringDeploymentGroup",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "GetMirroringDeploymentGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                MirroringRestTransport._GetMirroringDeploymentGroup._get_response(
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
            resp = mirroring.MirroringDeploymentGroup()
            pb_resp = mirroring.MirroringDeploymentGroup.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_mirroring_deployment_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_get_mirroring_deployment_group_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = mirroring.MirroringDeploymentGroup.to_json(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.MirroringClient.get_mirroring_deployment_group",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "GetMirroringDeploymentGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetMirroringEndpointGroup(
        _BaseMirroringRestTransport._BaseGetMirroringEndpointGroup, MirroringRestStub
    ):
        def __hash__(self):
            return hash("MirroringRestTransport.GetMirroringEndpointGroup")

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
            request: mirroring.GetMirroringEndpointGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> mirroring.MirroringEndpointGroup:
            r"""Call the get mirroring endpoint
            group method over HTTP.

                Args:
                    request (~.mirroring.GetMirroringEndpointGroupRequest):
                        The request object. Request message for
                    GetMirroringEndpointGroup.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.mirroring.MirroringEndpointGroup:
                        An endpoint group is a consumer
                    frontend for a deployment group
                    (backend). In order to configure
                    mirroring for a network, consumers must
                    create:

                    - An association between their network
                      and the endpoint group.
                    - A security profile that points to the
                      endpoint group.
                    - A mirroring rule that references the
                      security profile (group).

            """

            http_options = _BaseMirroringRestTransport._BaseGetMirroringEndpointGroup._get_http_options()
            request, metadata = self._interceptor.pre_get_mirroring_endpoint_group(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMirroringRestTransport._BaseGetMirroringEndpointGroup,
                    "_BaseGetMirroringEndpointGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.MirroringClient.GetMirroringEndpointGroup",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "GetMirroringEndpointGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MirroringRestTransport._GetMirroringEndpointGroup._get_response(
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
            resp = mirroring.MirroringEndpointGroup()
            pb_resp = mirroring.MirroringEndpointGroup.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_mirroring_endpoint_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_mirroring_endpoint_group_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = mirroring.MirroringEndpointGroup.to_json(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.MirroringClient.get_mirroring_endpoint_group",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "GetMirroringEndpointGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetMirroringEndpointGroupAssociation(
        _BaseMirroringRestTransport._BaseGetMirroringEndpointGroupAssociation,
        MirroringRestStub,
    ):
        def __hash__(self):
            return hash("MirroringRestTransport.GetMirroringEndpointGroupAssociation")

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
            request: mirroring.GetMirroringEndpointGroupAssociationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> mirroring.MirroringEndpointGroupAssociation:
            r"""Call the get mirroring endpoint
            group association method over HTTP.

                Args:
                    request (~.mirroring.GetMirroringEndpointGroupAssociationRequest):
                        The request object. Request message for
                    GetMirroringEndpointGroupAssociation.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.mirroring.MirroringEndpointGroupAssociation:
                        An endpoint group association
                    represents a link between a network and
                    an endpoint group in the organization.

                    Creating an association creates the
                    networking infrastructure linking the
                    network to the endpoint group, but does
                    not enable mirroring by itself. To
                    enable mirroring, the user must also
                    create a network firewall policy
                    containing mirroring rules and associate
                    it with the network.

            """

            http_options = _BaseMirroringRestTransport._BaseGetMirroringEndpointGroupAssociation._get_http_options()
            request, metadata = (
                self._interceptor.pre_get_mirroring_endpoint_group_association(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMirroringRestTransport._BaseGetMirroringEndpointGroupAssociation,
                    "_BaseGetMirroringEndpointGroupAssociation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.MirroringClient.GetMirroringEndpointGroupAssociation",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "GetMirroringEndpointGroupAssociation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MirroringRestTransport._GetMirroringEndpointGroupAssociation._get_response(
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
            resp = mirroring.MirroringEndpointGroupAssociation()
            pb_resp = mirroring.MirroringEndpointGroupAssociation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_mirroring_endpoint_group_association(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_get_mirroring_endpoint_group_association_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        mirroring.MirroringEndpointGroupAssociation.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.networksecurity_v1alpha1.MirroringClient.get_mirroring_endpoint_group_association",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "GetMirroringEndpointGroupAssociation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListMirroringDeploymentGroups(
        _BaseMirroringRestTransport._BaseListMirroringDeploymentGroups,
        MirroringRestStub,
    ):
        def __hash__(self):
            return hash("MirroringRestTransport.ListMirroringDeploymentGroups")

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
            request: mirroring.ListMirroringDeploymentGroupsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> mirroring.ListMirroringDeploymentGroupsResponse:
            r"""Call the list mirroring deployment
            groups method over HTTP.

                Args:
                    request (~.mirroring.ListMirroringDeploymentGroupsRequest):
                        The request object. Request message for
                    ListMirroringDeploymentGroups.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.mirroring.ListMirroringDeploymentGroupsResponse:
                        Response message for
                    ListMirroringDeploymentGroups.

            """

            http_options = _BaseMirroringRestTransport._BaseListMirroringDeploymentGroups._get_http_options()
            request, metadata = self._interceptor.pre_list_mirroring_deployment_groups(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMirroringRestTransport._BaseListMirroringDeploymentGroups,
                    "_BaseListMirroringDeploymentGroups__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.MirroringClient.ListMirroringDeploymentGroups",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "ListMirroringDeploymentGroups",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                MirroringRestTransport._ListMirroringDeploymentGroups._get_response(
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
            resp = mirroring.ListMirroringDeploymentGroupsResponse()
            pb_resp = mirroring.ListMirroringDeploymentGroupsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_mirroring_deployment_groups(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_mirroring_deployment_groups_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        mirroring.ListMirroringDeploymentGroupsResponse.to_json(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.MirroringClient.list_mirroring_deployment_groups",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "ListMirroringDeploymentGroups",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListMirroringDeployments(
        _BaseMirroringRestTransport._BaseListMirroringDeployments, MirroringRestStub
    ):
        def __hash__(self):
            return hash("MirroringRestTransport.ListMirroringDeployments")

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
            request: mirroring.ListMirroringDeploymentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> mirroring.ListMirroringDeploymentsResponse:
            r"""Call the list mirroring
            deployments method over HTTP.

                Args:
                    request (~.mirroring.ListMirroringDeploymentsRequest):
                        The request object. Request message for
                    ListMirroringDeployments.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.mirroring.ListMirroringDeploymentsResponse:
                        Response message for
                    ListMirroringDeployments.

            """

            http_options = _BaseMirroringRestTransport._BaseListMirroringDeployments._get_http_options()
            request, metadata = self._interceptor.pre_list_mirroring_deployments(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMirroringRestTransport._BaseListMirroringDeployments,
                    "_BaseListMirroringDeployments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.MirroringClient.ListMirroringDeployments",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "ListMirroringDeployments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MirroringRestTransport._ListMirroringDeployments._get_response(
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
            resp = mirroring.ListMirroringDeploymentsResponse()
            pb_resp = mirroring.ListMirroringDeploymentsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_mirroring_deployments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_mirroring_deployments_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        mirroring.ListMirroringDeploymentsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.networksecurity_v1alpha1.MirroringClient.list_mirroring_deployments",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "ListMirroringDeployments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListMirroringEndpointGroupAssociations(
        _BaseMirroringRestTransport._BaseListMirroringEndpointGroupAssociations,
        MirroringRestStub,
    ):
        def __hash__(self):
            return hash("MirroringRestTransport.ListMirroringEndpointGroupAssociations")

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
            request: mirroring.ListMirroringEndpointGroupAssociationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> mirroring.ListMirroringEndpointGroupAssociationsResponse:
            r"""Call the list mirroring endpoint
            group associations method over HTTP.

                Args:
                    request (~.mirroring.ListMirroringEndpointGroupAssociationsRequest):
                        The request object. Request message for
                    ListMirroringEndpointGroupAssociations.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.mirroring.ListMirroringEndpointGroupAssociationsResponse:
                        Response message for
                    ListMirroringEndpointGroupAssociations.

            """

            http_options = _BaseMirroringRestTransport._BaseListMirroringEndpointGroupAssociations._get_http_options()
            request, metadata = (
                self._interceptor.pre_list_mirroring_endpoint_group_associations(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMirroringRestTransport._BaseListMirroringEndpointGroupAssociations,
                    "_BaseListMirroringEndpointGroupAssociations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.MirroringClient.ListMirroringEndpointGroupAssociations",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "ListMirroringEndpointGroupAssociations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MirroringRestTransport._ListMirroringEndpointGroupAssociations._get_response(
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
            resp = mirroring.ListMirroringEndpointGroupAssociationsResponse()
            pb_resp = mirroring.ListMirroringEndpointGroupAssociationsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_mirroring_endpoint_group_associations(
                resp
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_mirroring_endpoint_group_associations_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = mirroring.ListMirroringEndpointGroupAssociationsResponse.to_json(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.MirroringClient.list_mirroring_endpoint_group_associations",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "ListMirroringEndpointGroupAssociations",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListMirroringEndpointGroups(
        _BaseMirroringRestTransport._BaseListMirroringEndpointGroups, MirroringRestStub
    ):
        def __hash__(self):
            return hash("MirroringRestTransport.ListMirroringEndpointGroups")

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
            request: mirroring.ListMirroringEndpointGroupsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> mirroring.ListMirroringEndpointGroupsResponse:
            r"""Call the list mirroring endpoint
            groups method over HTTP.

                Args:
                    request (~.mirroring.ListMirroringEndpointGroupsRequest):
                        The request object. Request message for
                    ListMirroringEndpointGroups.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.mirroring.ListMirroringEndpointGroupsResponse:
                        Response message for
                    ListMirroringEndpointGroups.

            """

            http_options = _BaseMirroringRestTransport._BaseListMirroringEndpointGroups._get_http_options()
            request, metadata = self._interceptor.pre_list_mirroring_endpoint_groups(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMirroringRestTransport._BaseListMirroringEndpointGroups,
                    "_BaseListMirroringEndpointGroups__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.MirroringClient.ListMirroringEndpointGroups",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "ListMirroringEndpointGroups",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                MirroringRestTransport._ListMirroringEndpointGroups._get_response(
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
            resp = mirroring.ListMirroringEndpointGroupsResponse()
            pb_resp = mirroring.ListMirroringEndpointGroupsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_mirroring_endpoint_groups(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_mirroring_endpoint_groups_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        mirroring.ListMirroringEndpointGroupsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.networksecurity_v1alpha1.MirroringClient.list_mirroring_endpoint_groups",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "ListMirroringEndpointGroups",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateMirroringDeployment(
        _BaseMirroringRestTransport._BaseUpdateMirroringDeployment, MirroringRestStub
    ):
        def __hash__(self):
            return hash("MirroringRestTransport.UpdateMirroringDeployment")

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
            request: mirroring.UpdateMirroringDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update mirroring
            deployment method over HTTP.

                Args:
                    request (~.mirroring.UpdateMirroringDeploymentRequest):
                        The request object. Request message for
                    UpdateMirroringDeployment.
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

            http_options = _BaseMirroringRestTransport._BaseUpdateMirroringDeployment._get_http_options()
            request, metadata = self._interceptor.pre_update_mirroring_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMirroringRestTransport._BaseUpdateMirroringDeployment,
                    "_BaseUpdateMirroringDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.MirroringClient.UpdateMirroringDeployment",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "UpdateMirroringDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MirroringRestTransport._UpdateMirroringDeployment._get_response(
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

            resp = self._interceptor.post_update_mirroring_deployment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_mirroring_deployment_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.MirroringClient.update_mirroring_deployment",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "UpdateMirroringDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateMirroringDeploymentGroup(
        _BaseMirroringRestTransport._BaseUpdateMirroringDeploymentGroup,
        MirroringRestStub,
    ):
        def __hash__(self):
            return hash("MirroringRestTransport.UpdateMirroringDeploymentGroup")

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
            request: mirroring.UpdateMirroringDeploymentGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update mirroring
            deployment group method over HTTP.

                Args:
                    request (~.mirroring.UpdateMirroringDeploymentGroupRequest):
                        The request object. Request message for
                    UpdateMirroringDeploymentGroup.
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

            http_options = _BaseMirroringRestTransport._BaseUpdateMirroringDeploymentGroup._get_http_options()
            request, metadata = self._interceptor.pre_update_mirroring_deployment_group(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMirroringRestTransport._BaseUpdateMirroringDeploymentGroup,
                    "_BaseUpdateMirroringDeploymentGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.MirroringClient.UpdateMirroringDeploymentGroup",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "UpdateMirroringDeploymentGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                MirroringRestTransport._UpdateMirroringDeploymentGroup._get_response(
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

            resp = self._interceptor.post_update_mirroring_deployment_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_update_mirroring_deployment_group_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.MirroringClient.update_mirroring_deployment_group",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "UpdateMirroringDeploymentGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateMirroringEndpointGroup(
        _BaseMirroringRestTransport._BaseUpdateMirroringEndpointGroup, MirroringRestStub
    ):
        def __hash__(self):
            return hash("MirroringRestTransport.UpdateMirroringEndpointGroup")

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
            request: mirroring.UpdateMirroringEndpointGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update mirroring endpoint
            group method over HTTP.

                Args:
                    request (~.mirroring.UpdateMirroringEndpointGroupRequest):
                        The request object. Request message for
                    UpdateMirroringEndpointGroup.
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

            http_options = _BaseMirroringRestTransport._BaseUpdateMirroringEndpointGroup._get_http_options()
            request, metadata = self._interceptor.pre_update_mirroring_endpoint_group(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMirroringRestTransport._BaseUpdateMirroringEndpointGroup,
                    "_BaseUpdateMirroringEndpointGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.MirroringClient.UpdateMirroringEndpointGroup",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "UpdateMirroringEndpointGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                MirroringRestTransport._UpdateMirroringEndpointGroup._get_response(
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

            resp = self._interceptor.post_update_mirroring_endpoint_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_update_mirroring_endpoint_group_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.MirroringClient.update_mirroring_endpoint_group",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "UpdateMirroringEndpointGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateMirroringEndpointGroupAssociation(
        _BaseMirroringRestTransport._BaseUpdateMirroringEndpointGroupAssociation,
        MirroringRestStub,
    ):
        def __hash__(self):
            return hash(
                "MirroringRestTransport.UpdateMirroringEndpointGroupAssociation"
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
            request: mirroring.UpdateMirroringEndpointGroupAssociationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update mirroring endpoint
            group association method over HTTP.

                Args:
                    request (~.mirroring.UpdateMirroringEndpointGroupAssociationRequest):
                        The request object. Request message for
                    UpdateMirroringEndpointGroupAssociation.
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

            http_options = _BaseMirroringRestTransport._BaseUpdateMirroringEndpointGroupAssociation._get_http_options()
            request, metadata = (
                self._interceptor.pre_update_mirroring_endpoint_group_association(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMirroringRestTransport._BaseUpdateMirroringEndpointGroupAssociation,
                    "_BaseUpdateMirroringEndpointGroupAssociation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.MirroringClient.UpdateMirroringEndpointGroupAssociation",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "UpdateMirroringEndpointGroupAssociation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MirroringRestTransport._UpdateMirroringEndpointGroupAssociation._get_response(
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

            resp = self._interceptor.post_update_mirroring_endpoint_group_association(
                resp
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_update_mirroring_endpoint_group_association_with_metadata(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.MirroringClient.update_mirroring_endpoint_group_association",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "UpdateMirroringEndpointGroupAssociation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_mirroring_deployment(
        self,
    ) -> Callable[
        [mirroring.CreateMirroringDeploymentRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateMirroringDeployment(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_mirroring_deployment_group(
        self,
    ) -> Callable[
        [mirroring.CreateMirroringDeploymentGroupRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateMirroringDeploymentGroup(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_mirroring_endpoint_group(
        self,
    ) -> Callable[
        [mirroring.CreateMirroringEndpointGroupRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateMirroringEndpointGroup(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_mirroring_endpoint_group_association(
        self,
    ) -> Callable[
        [mirroring.CreateMirroringEndpointGroupAssociationRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateMirroringEndpointGroupAssociation(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_mirroring_deployment(
        self,
    ) -> Callable[
        [mirroring.DeleteMirroringDeploymentRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteMirroringDeployment(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_mirroring_deployment_group(
        self,
    ) -> Callable[
        [mirroring.DeleteMirroringDeploymentGroupRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteMirroringDeploymentGroup(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_mirroring_endpoint_group(
        self,
    ) -> Callable[
        [mirroring.DeleteMirroringEndpointGroupRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteMirroringEndpointGroup(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_mirroring_endpoint_group_association(
        self,
    ) -> Callable[
        [mirroring.DeleteMirroringEndpointGroupAssociationRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteMirroringEndpointGroupAssociation(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_mirroring_deployment(
        self,
    ) -> Callable[
        [mirroring.GetMirroringDeploymentRequest], mirroring.MirroringDeployment
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetMirroringDeployment(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_mirroring_deployment_group(
        self,
    ) -> Callable[
        [mirroring.GetMirroringDeploymentGroupRequest],
        mirroring.MirroringDeploymentGroup,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetMirroringDeploymentGroup(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_mirroring_endpoint_group(
        self,
    ) -> Callable[
        [mirroring.GetMirroringEndpointGroupRequest], mirroring.MirroringEndpointGroup
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetMirroringEndpointGroup(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_mirroring_endpoint_group_association(
        self,
    ) -> Callable[
        [mirroring.GetMirroringEndpointGroupAssociationRequest],
        mirroring.MirroringEndpointGroupAssociation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetMirroringEndpointGroupAssociation(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_mirroring_deployment_groups(
        self,
    ) -> Callable[
        [mirroring.ListMirroringDeploymentGroupsRequest],
        mirroring.ListMirroringDeploymentGroupsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListMirroringDeploymentGroups(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_mirroring_deployments(
        self,
    ) -> Callable[
        [mirroring.ListMirroringDeploymentsRequest],
        mirroring.ListMirroringDeploymentsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListMirroringDeployments(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_mirroring_endpoint_group_associations(
        self,
    ) -> Callable[
        [mirroring.ListMirroringEndpointGroupAssociationsRequest],
        mirroring.ListMirroringEndpointGroupAssociationsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListMirroringEndpointGroupAssociations(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_mirroring_endpoint_groups(
        self,
    ) -> Callable[
        [mirroring.ListMirroringEndpointGroupsRequest],
        mirroring.ListMirroringEndpointGroupsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListMirroringEndpointGroups(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_mirroring_deployment(
        self,
    ) -> Callable[
        [mirroring.UpdateMirroringDeploymentRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateMirroringDeployment(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_mirroring_deployment_group(
        self,
    ) -> Callable[
        [mirroring.UpdateMirroringDeploymentGroupRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateMirroringDeploymentGroup(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_mirroring_endpoint_group(
        self,
    ) -> Callable[
        [mirroring.UpdateMirroringEndpointGroupRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateMirroringEndpointGroup(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_mirroring_endpoint_group_association(
        self,
    ) -> Callable[
        [mirroring.UpdateMirroringEndpointGroupAssociationRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateMirroringEndpointGroupAssociation(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(_BaseMirroringRestTransport._BaseGetLocation, MirroringRestStub):
        def __hash__(self):
            return hash("MirroringRestTransport.GetLocation")

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
                _BaseMirroringRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMirroringRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.MirroringClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MirroringRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.MirroringAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
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
        _BaseMirroringRestTransport._BaseListLocations, MirroringRestStub
    ):
        def __hash__(self):
            return hash("MirroringRestTransport.ListLocations")

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
                _BaseMirroringRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMirroringRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.MirroringClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MirroringRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.MirroringAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
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
        _BaseMirroringRestTransport._BaseGetIamPolicy, MirroringRestStub
    ):
        def __hash__(self):
            return hash("MirroringRestTransport.GetIamPolicy")

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
                _BaseMirroringRestTransport._BaseGetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMirroringRestTransport._BaseGetIamPolicy,
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.MirroringClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "GetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MirroringRestTransport._GetIamPolicy._get_response(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.MirroringAsyncClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
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
        _BaseMirroringRestTransport._BaseSetIamPolicy, MirroringRestStub
    ):
        def __hash__(self):
            return hash("MirroringRestTransport.SetIamPolicy")

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
                _BaseMirroringRestTransport._BaseSetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMirroringRestTransport._BaseSetIamPolicy,
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.MirroringClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "SetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MirroringRestTransport._SetIamPolicy._get_response(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.MirroringAsyncClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
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
        _BaseMirroringRestTransport._BaseTestIamPermissions, MirroringRestStub
    ):
        def __hash__(self):
            return hash("MirroringRestTransport.TestIamPermissions")

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
                _BaseMirroringRestTransport._BaseTestIamPermissions._get_http_options()
            )
            request, metadata = self._interceptor.pre_test_iam_permissions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMirroringRestTransport._BaseTestIamPermissions,
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.MirroringClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "TestIamPermissions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MirroringRestTransport._TestIamPermissions._get_response(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.MirroringAsyncClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
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
        _BaseMirroringRestTransport._BaseCancelOperation, MirroringRestStub
    ):
        def __hash__(self):
            return hash("MirroringRestTransport.CancelOperation")

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
                _BaseMirroringRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMirroringRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.MirroringClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MirroringRestTransport._CancelOperation._get_response(
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
        _BaseMirroringRestTransport._BaseDeleteOperation, MirroringRestStub
    ):
        def __hash__(self):
            return hash("MirroringRestTransport.DeleteOperation")

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
                _BaseMirroringRestTransport._BaseDeleteOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMirroringRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.MirroringClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MirroringRestTransport._DeleteOperation._get_response(
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
        _BaseMirroringRestTransport._BaseGetOperation, MirroringRestStub
    ):
        def __hash__(self):
            return hash("MirroringRestTransport.GetOperation")

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
                _BaseMirroringRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMirroringRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.MirroringClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MirroringRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.MirroringAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
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
        _BaseMirroringRestTransport._BaseListOperations, MirroringRestStub
    ):
        def __hash__(self):
            return hash("MirroringRestTransport.ListOperations")

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
                _BaseMirroringRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMirroringRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.networksecurity_v1alpha1.MirroringClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MirroringRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.networksecurity_v1alpha1.MirroringAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.networksecurity.v1alpha1.Mirroring",
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


__all__ = ("MirroringRestTransport",)
