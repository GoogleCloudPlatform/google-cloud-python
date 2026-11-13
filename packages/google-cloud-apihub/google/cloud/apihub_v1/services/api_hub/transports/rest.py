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
from google.api_core import gapic_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.apihub_v1._compat import transcode_request
from google.cloud.apihub_v1.types import apihub_service, common_fields

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseApiHubRestTransport

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


class ApiHubRestInterceptor:
    """Interceptor for ApiHub.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the ApiHubRestTransport.

    .. code-block:: python
        class MyCustomApiHubInterceptor(ApiHubRestInterceptor):
            def pre_create_api(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_api(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_api_operation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_api_operation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_attribute(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_attribute(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_external_api(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_external_api(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_spec(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_spec(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_version(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_api(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_api_operation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_attribute(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_external_api(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_spec(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_api(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_api(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_api_operation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_api_operation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_attribute(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_attribute(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_definition(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_definition(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_external_api(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_external_api(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_spec(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_spec(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_spec_contents(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_spec_contents(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_version(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_api_operations(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_api_operations(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_apis(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_apis(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_attributes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_attributes(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_deployments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_deployments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_external_apis(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_external_apis(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_specs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_specs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_versions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_versions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_search_resources(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_search_resources(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_api(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_api(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_api_operation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_api_operation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_attribute(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_attribute(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_external_api(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_external_api(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_spec(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_spec(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_version(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = ApiHubRestTransport(interceptor=MyCustomApiHubInterceptor())
        client = ApiHubClient(transport=transport)


    """

    def pre_create_api(
        self,
        request: apihub_service.CreateApiRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.CreateApiRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_api

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def post_create_api(self, response: common_fields.Api) -> common_fields.Api:
        """Post-rpc interceptor for create_api

        DEPRECATED. Please use the `post_create_api_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHub server but before
        it is returned to user code. This `post_create_api` interceptor runs
        before the `post_create_api_with_metadata` interceptor.
        """
        return response

    def post_create_api_with_metadata(
        self,
        response: common_fields.Api,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[common_fields.Api, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_api

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHub server but before it is returned to user code.

        We recommend only using this `post_create_api_with_metadata`
        interceptor in new development instead of the `post_create_api` interceptor.
        When both interceptors are used, this `post_create_api_with_metadata` interceptor runs after the
        `post_create_api` interceptor. The (possibly modified) response returned by
        `post_create_api` will be passed to
        `post_create_api_with_metadata`.
        """
        return response, metadata

    def pre_create_api_operation(
        self,
        request: apihub_service.CreateApiOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.CreateApiOperationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_api_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def post_create_api_operation(
        self, response: common_fields.ApiOperation
    ) -> common_fields.ApiOperation:
        """Post-rpc interceptor for create_api_operation

        DEPRECATED. Please use the `post_create_api_operation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHub server but before
        it is returned to user code. This `post_create_api_operation` interceptor runs
        before the `post_create_api_operation_with_metadata` interceptor.
        """
        return response

    def post_create_api_operation_with_metadata(
        self,
        response: common_fields.ApiOperation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[common_fields.ApiOperation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_api_operation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHub server but before it is returned to user code.

        We recommend only using this `post_create_api_operation_with_metadata`
        interceptor in new development instead of the `post_create_api_operation` interceptor.
        When both interceptors are used, this `post_create_api_operation_with_metadata` interceptor runs after the
        `post_create_api_operation` interceptor. The (possibly modified) response returned by
        `post_create_api_operation` will be passed to
        `post_create_api_operation_with_metadata`.
        """
        return response, metadata

    def pre_create_attribute(
        self,
        request: apihub_service.CreateAttributeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.CreateAttributeRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_attribute

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def post_create_attribute(
        self, response: common_fields.Attribute
    ) -> common_fields.Attribute:
        """Post-rpc interceptor for create_attribute

        DEPRECATED. Please use the `post_create_attribute_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHub server but before
        it is returned to user code. This `post_create_attribute` interceptor runs
        before the `post_create_attribute_with_metadata` interceptor.
        """
        return response

    def post_create_attribute_with_metadata(
        self,
        response: common_fields.Attribute,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[common_fields.Attribute, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_attribute

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHub server but before it is returned to user code.

        We recommend only using this `post_create_attribute_with_metadata`
        interceptor in new development instead of the `post_create_attribute` interceptor.
        When both interceptors are used, this `post_create_attribute_with_metadata` interceptor runs after the
        `post_create_attribute` interceptor. The (possibly modified) response returned by
        `post_create_attribute` will be passed to
        `post_create_attribute_with_metadata`.
        """
        return response, metadata

    def pre_create_deployment(
        self,
        request: apihub_service.CreateDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.CreateDeploymentRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def post_create_deployment(
        self, response: common_fields.Deployment
    ) -> common_fields.Deployment:
        """Post-rpc interceptor for create_deployment

        DEPRECATED. Please use the `post_create_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHub server but before
        it is returned to user code. This `post_create_deployment` interceptor runs
        before the `post_create_deployment_with_metadata` interceptor.
        """
        return response

    def post_create_deployment_with_metadata(
        self,
        response: common_fields.Deployment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[common_fields.Deployment, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHub server but before it is returned to user code.

        We recommend only using this `post_create_deployment_with_metadata`
        interceptor in new development instead of the `post_create_deployment` interceptor.
        When both interceptors are used, this `post_create_deployment_with_metadata` interceptor runs after the
        `post_create_deployment` interceptor. The (possibly modified) response returned by
        `post_create_deployment` will be passed to
        `post_create_deployment_with_metadata`.
        """
        return response, metadata

    def pre_create_external_api(
        self,
        request: apihub_service.CreateExternalApiRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.CreateExternalApiRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_external_api

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def post_create_external_api(
        self, response: common_fields.ExternalApi
    ) -> common_fields.ExternalApi:
        """Post-rpc interceptor for create_external_api

        DEPRECATED. Please use the `post_create_external_api_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHub server but before
        it is returned to user code. This `post_create_external_api` interceptor runs
        before the `post_create_external_api_with_metadata` interceptor.
        """
        return response

    def post_create_external_api_with_metadata(
        self,
        response: common_fields.ExternalApi,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[common_fields.ExternalApi, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_external_api

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHub server but before it is returned to user code.

        We recommend only using this `post_create_external_api_with_metadata`
        interceptor in new development instead of the `post_create_external_api` interceptor.
        When both interceptors are used, this `post_create_external_api_with_metadata` interceptor runs after the
        `post_create_external_api` interceptor. The (possibly modified) response returned by
        `post_create_external_api` will be passed to
        `post_create_external_api_with_metadata`.
        """
        return response, metadata

    def pre_create_spec(
        self,
        request: apihub_service.CreateSpecRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.CreateSpecRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_spec

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def post_create_spec(self, response: common_fields.Spec) -> common_fields.Spec:
        """Post-rpc interceptor for create_spec

        DEPRECATED. Please use the `post_create_spec_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHub server but before
        it is returned to user code. This `post_create_spec` interceptor runs
        before the `post_create_spec_with_metadata` interceptor.
        """
        return response

    def post_create_spec_with_metadata(
        self,
        response: common_fields.Spec,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[common_fields.Spec, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_spec

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHub server but before it is returned to user code.

        We recommend only using this `post_create_spec_with_metadata`
        interceptor in new development instead of the `post_create_spec` interceptor.
        When both interceptors are used, this `post_create_spec_with_metadata` interceptor runs after the
        `post_create_spec` interceptor. The (possibly modified) response returned by
        `post_create_spec` will be passed to
        `post_create_spec_with_metadata`.
        """
        return response, metadata

    def pre_create_version(
        self,
        request: apihub_service.CreateVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.CreateVersionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def post_create_version(
        self, response: common_fields.Version
    ) -> common_fields.Version:
        """Post-rpc interceptor for create_version

        DEPRECATED. Please use the `post_create_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHub server but before
        it is returned to user code. This `post_create_version` interceptor runs
        before the `post_create_version_with_metadata` interceptor.
        """
        return response

    def post_create_version_with_metadata(
        self,
        response: common_fields.Version,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[common_fields.Version, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHub server but before it is returned to user code.

        We recommend only using this `post_create_version_with_metadata`
        interceptor in new development instead of the `post_create_version` interceptor.
        When both interceptors are used, this `post_create_version_with_metadata` interceptor runs after the
        `post_create_version` interceptor. The (possibly modified) response returned by
        `post_create_version` will be passed to
        `post_create_version_with_metadata`.
        """
        return response, metadata

    def pre_delete_api(
        self,
        request: apihub_service.DeleteApiRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.DeleteApiRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_api

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def pre_delete_api_operation(
        self,
        request: apihub_service.DeleteApiOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.DeleteApiOperationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_api_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def pre_delete_attribute(
        self,
        request: apihub_service.DeleteAttributeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.DeleteAttributeRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_attribute

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def pre_delete_deployment(
        self,
        request: apihub_service.DeleteDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.DeleteDeploymentRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def pre_delete_external_api(
        self,
        request: apihub_service.DeleteExternalApiRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.DeleteExternalApiRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_external_api

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def pre_delete_spec(
        self,
        request: apihub_service.DeleteSpecRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.DeleteSpecRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_spec

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def pre_delete_version(
        self,
        request: apihub_service.DeleteVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.DeleteVersionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def pre_get_api(
        self,
        request: apihub_service.GetApiRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[apihub_service.GetApiRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_api

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def post_get_api(self, response: common_fields.Api) -> common_fields.Api:
        """Post-rpc interceptor for get_api

        DEPRECATED. Please use the `post_get_api_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHub server but before
        it is returned to user code. This `post_get_api` interceptor runs
        before the `post_get_api_with_metadata` interceptor.
        """
        return response

    def post_get_api_with_metadata(
        self,
        response: common_fields.Api,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[common_fields.Api, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_api

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHub server but before it is returned to user code.

        We recommend only using this `post_get_api_with_metadata`
        interceptor in new development instead of the `post_get_api` interceptor.
        When both interceptors are used, this `post_get_api_with_metadata` interceptor runs after the
        `post_get_api` interceptor. The (possibly modified) response returned by
        `post_get_api` will be passed to
        `post_get_api_with_metadata`.
        """
        return response, metadata

    def pre_get_api_operation(
        self,
        request: apihub_service.GetApiOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.GetApiOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_api_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def post_get_api_operation(
        self, response: common_fields.ApiOperation
    ) -> common_fields.ApiOperation:
        """Post-rpc interceptor for get_api_operation

        DEPRECATED. Please use the `post_get_api_operation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHub server but before
        it is returned to user code. This `post_get_api_operation` interceptor runs
        before the `post_get_api_operation_with_metadata` interceptor.
        """
        return response

    def post_get_api_operation_with_metadata(
        self,
        response: common_fields.ApiOperation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[common_fields.ApiOperation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_api_operation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHub server but before it is returned to user code.

        We recommend only using this `post_get_api_operation_with_metadata`
        interceptor in new development instead of the `post_get_api_operation` interceptor.
        When both interceptors are used, this `post_get_api_operation_with_metadata` interceptor runs after the
        `post_get_api_operation` interceptor. The (possibly modified) response returned by
        `post_get_api_operation` will be passed to
        `post_get_api_operation_with_metadata`.
        """
        return response, metadata

    def pre_get_attribute(
        self,
        request: apihub_service.GetAttributeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.GetAttributeRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_attribute

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def post_get_attribute(
        self, response: common_fields.Attribute
    ) -> common_fields.Attribute:
        """Post-rpc interceptor for get_attribute

        DEPRECATED. Please use the `post_get_attribute_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHub server but before
        it is returned to user code. This `post_get_attribute` interceptor runs
        before the `post_get_attribute_with_metadata` interceptor.
        """
        return response

    def post_get_attribute_with_metadata(
        self,
        response: common_fields.Attribute,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[common_fields.Attribute, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_attribute

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHub server but before it is returned to user code.

        We recommend only using this `post_get_attribute_with_metadata`
        interceptor in new development instead of the `post_get_attribute` interceptor.
        When both interceptors are used, this `post_get_attribute_with_metadata` interceptor runs after the
        `post_get_attribute` interceptor. The (possibly modified) response returned by
        `post_get_attribute` will be passed to
        `post_get_attribute_with_metadata`.
        """
        return response, metadata

    def pre_get_definition(
        self,
        request: apihub_service.GetDefinitionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.GetDefinitionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_definition

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def post_get_definition(
        self, response: common_fields.Definition
    ) -> common_fields.Definition:
        """Post-rpc interceptor for get_definition

        DEPRECATED. Please use the `post_get_definition_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHub server but before
        it is returned to user code. This `post_get_definition` interceptor runs
        before the `post_get_definition_with_metadata` interceptor.
        """
        return response

    def post_get_definition_with_metadata(
        self,
        response: common_fields.Definition,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[common_fields.Definition, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_definition

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHub server but before it is returned to user code.

        We recommend only using this `post_get_definition_with_metadata`
        interceptor in new development instead of the `post_get_definition` interceptor.
        When both interceptors are used, this `post_get_definition_with_metadata` interceptor runs after the
        `post_get_definition` interceptor. The (possibly modified) response returned by
        `post_get_definition` will be passed to
        `post_get_definition_with_metadata`.
        """
        return response, metadata

    def pre_get_deployment(
        self,
        request: apihub_service.GetDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.GetDeploymentRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def post_get_deployment(
        self, response: common_fields.Deployment
    ) -> common_fields.Deployment:
        """Post-rpc interceptor for get_deployment

        DEPRECATED. Please use the `post_get_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHub server but before
        it is returned to user code. This `post_get_deployment` interceptor runs
        before the `post_get_deployment_with_metadata` interceptor.
        """
        return response

    def post_get_deployment_with_metadata(
        self,
        response: common_fields.Deployment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[common_fields.Deployment, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHub server but before it is returned to user code.

        We recommend only using this `post_get_deployment_with_metadata`
        interceptor in new development instead of the `post_get_deployment` interceptor.
        When both interceptors are used, this `post_get_deployment_with_metadata` interceptor runs after the
        `post_get_deployment` interceptor. The (possibly modified) response returned by
        `post_get_deployment` will be passed to
        `post_get_deployment_with_metadata`.
        """
        return response, metadata

    def pre_get_external_api(
        self,
        request: apihub_service.GetExternalApiRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.GetExternalApiRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_external_api

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def post_get_external_api(
        self, response: common_fields.ExternalApi
    ) -> common_fields.ExternalApi:
        """Post-rpc interceptor for get_external_api

        DEPRECATED. Please use the `post_get_external_api_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHub server but before
        it is returned to user code. This `post_get_external_api` interceptor runs
        before the `post_get_external_api_with_metadata` interceptor.
        """
        return response

    def post_get_external_api_with_metadata(
        self,
        response: common_fields.ExternalApi,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[common_fields.ExternalApi, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_external_api

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHub server but before it is returned to user code.

        We recommend only using this `post_get_external_api_with_metadata`
        interceptor in new development instead of the `post_get_external_api` interceptor.
        When both interceptors are used, this `post_get_external_api_with_metadata` interceptor runs after the
        `post_get_external_api` interceptor. The (possibly modified) response returned by
        `post_get_external_api` will be passed to
        `post_get_external_api_with_metadata`.
        """
        return response, metadata

    def pre_get_spec(
        self,
        request: apihub_service.GetSpecRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[apihub_service.GetSpecRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_spec

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def post_get_spec(self, response: common_fields.Spec) -> common_fields.Spec:
        """Post-rpc interceptor for get_spec

        DEPRECATED. Please use the `post_get_spec_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHub server but before
        it is returned to user code. This `post_get_spec` interceptor runs
        before the `post_get_spec_with_metadata` interceptor.
        """
        return response

    def post_get_spec_with_metadata(
        self,
        response: common_fields.Spec,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[common_fields.Spec, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_spec

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHub server but before it is returned to user code.

        We recommend only using this `post_get_spec_with_metadata`
        interceptor in new development instead of the `post_get_spec` interceptor.
        When both interceptors are used, this `post_get_spec_with_metadata` interceptor runs after the
        `post_get_spec` interceptor. The (possibly modified) response returned by
        `post_get_spec` will be passed to
        `post_get_spec_with_metadata`.
        """
        return response, metadata

    def pre_get_spec_contents(
        self,
        request: apihub_service.GetSpecContentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.GetSpecContentsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_spec_contents

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def post_get_spec_contents(
        self, response: common_fields.SpecContents
    ) -> common_fields.SpecContents:
        """Post-rpc interceptor for get_spec_contents

        DEPRECATED. Please use the `post_get_spec_contents_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHub server but before
        it is returned to user code. This `post_get_spec_contents` interceptor runs
        before the `post_get_spec_contents_with_metadata` interceptor.
        """
        return response

    def post_get_spec_contents_with_metadata(
        self,
        response: common_fields.SpecContents,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[common_fields.SpecContents, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_spec_contents

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHub server but before it is returned to user code.

        We recommend only using this `post_get_spec_contents_with_metadata`
        interceptor in new development instead of the `post_get_spec_contents` interceptor.
        When both interceptors are used, this `post_get_spec_contents_with_metadata` interceptor runs after the
        `post_get_spec_contents` interceptor. The (possibly modified) response returned by
        `post_get_spec_contents` will be passed to
        `post_get_spec_contents_with_metadata`.
        """
        return response, metadata

    def pre_get_version(
        self,
        request: apihub_service.GetVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.GetVersionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def post_get_version(
        self, response: common_fields.Version
    ) -> common_fields.Version:
        """Post-rpc interceptor for get_version

        DEPRECATED. Please use the `post_get_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHub server but before
        it is returned to user code. This `post_get_version` interceptor runs
        before the `post_get_version_with_metadata` interceptor.
        """
        return response

    def post_get_version_with_metadata(
        self,
        response: common_fields.Version,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[common_fields.Version, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHub server but before it is returned to user code.

        We recommend only using this `post_get_version_with_metadata`
        interceptor in new development instead of the `post_get_version` interceptor.
        When both interceptors are used, this `post_get_version_with_metadata` interceptor runs after the
        `post_get_version` interceptor. The (possibly modified) response returned by
        `post_get_version` will be passed to
        `post_get_version_with_metadata`.
        """
        return response, metadata

    def pre_list_api_operations(
        self,
        request: apihub_service.ListApiOperationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.ListApiOperationsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_api_operations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def post_list_api_operations(
        self, response: apihub_service.ListApiOperationsResponse
    ) -> apihub_service.ListApiOperationsResponse:
        """Post-rpc interceptor for list_api_operations

        DEPRECATED. Please use the `post_list_api_operations_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHub server but before
        it is returned to user code. This `post_list_api_operations` interceptor runs
        before the `post_list_api_operations_with_metadata` interceptor.
        """
        return response

    def post_list_api_operations_with_metadata(
        self,
        response: apihub_service.ListApiOperationsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.ListApiOperationsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_api_operations

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHub server but before it is returned to user code.

        We recommend only using this `post_list_api_operations_with_metadata`
        interceptor in new development instead of the `post_list_api_operations` interceptor.
        When both interceptors are used, this `post_list_api_operations_with_metadata` interceptor runs after the
        `post_list_api_operations` interceptor. The (possibly modified) response returned by
        `post_list_api_operations` will be passed to
        `post_list_api_operations_with_metadata`.
        """
        return response, metadata

    def pre_list_apis(
        self,
        request: apihub_service.ListApisRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[apihub_service.ListApisRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_apis

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def post_list_apis(
        self, response: apihub_service.ListApisResponse
    ) -> apihub_service.ListApisResponse:
        """Post-rpc interceptor for list_apis

        DEPRECATED. Please use the `post_list_apis_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHub server but before
        it is returned to user code. This `post_list_apis` interceptor runs
        before the `post_list_apis_with_metadata` interceptor.
        """
        return response

    def post_list_apis_with_metadata(
        self,
        response: apihub_service.ListApisResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.ListApisResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_apis

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHub server but before it is returned to user code.

        We recommend only using this `post_list_apis_with_metadata`
        interceptor in new development instead of the `post_list_apis` interceptor.
        When both interceptors are used, this `post_list_apis_with_metadata` interceptor runs after the
        `post_list_apis` interceptor. The (possibly modified) response returned by
        `post_list_apis` will be passed to
        `post_list_apis_with_metadata`.
        """
        return response, metadata

    def pre_list_attributes(
        self,
        request: apihub_service.ListAttributesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.ListAttributesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_attributes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def post_list_attributes(
        self, response: apihub_service.ListAttributesResponse
    ) -> apihub_service.ListAttributesResponse:
        """Post-rpc interceptor for list_attributes

        DEPRECATED. Please use the `post_list_attributes_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHub server but before
        it is returned to user code. This `post_list_attributes` interceptor runs
        before the `post_list_attributes_with_metadata` interceptor.
        """
        return response

    def post_list_attributes_with_metadata(
        self,
        response: apihub_service.ListAttributesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.ListAttributesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_attributes

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHub server but before it is returned to user code.

        We recommend only using this `post_list_attributes_with_metadata`
        interceptor in new development instead of the `post_list_attributes` interceptor.
        When both interceptors are used, this `post_list_attributes_with_metadata` interceptor runs after the
        `post_list_attributes` interceptor. The (possibly modified) response returned by
        `post_list_attributes` will be passed to
        `post_list_attributes_with_metadata`.
        """
        return response, metadata

    def pre_list_deployments(
        self,
        request: apihub_service.ListDeploymentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.ListDeploymentsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_deployments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def post_list_deployments(
        self, response: apihub_service.ListDeploymentsResponse
    ) -> apihub_service.ListDeploymentsResponse:
        """Post-rpc interceptor for list_deployments

        DEPRECATED. Please use the `post_list_deployments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHub server but before
        it is returned to user code. This `post_list_deployments` interceptor runs
        before the `post_list_deployments_with_metadata` interceptor.
        """
        return response

    def post_list_deployments_with_metadata(
        self,
        response: apihub_service.ListDeploymentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.ListDeploymentsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_deployments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHub server but before it is returned to user code.

        We recommend only using this `post_list_deployments_with_metadata`
        interceptor in new development instead of the `post_list_deployments` interceptor.
        When both interceptors are used, this `post_list_deployments_with_metadata` interceptor runs after the
        `post_list_deployments` interceptor. The (possibly modified) response returned by
        `post_list_deployments` will be passed to
        `post_list_deployments_with_metadata`.
        """
        return response, metadata

    def pre_list_external_apis(
        self,
        request: apihub_service.ListExternalApisRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.ListExternalApisRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_external_apis

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def post_list_external_apis(
        self, response: apihub_service.ListExternalApisResponse
    ) -> apihub_service.ListExternalApisResponse:
        """Post-rpc interceptor for list_external_apis

        DEPRECATED. Please use the `post_list_external_apis_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHub server but before
        it is returned to user code. This `post_list_external_apis` interceptor runs
        before the `post_list_external_apis_with_metadata` interceptor.
        """
        return response

    def post_list_external_apis_with_metadata(
        self,
        response: apihub_service.ListExternalApisResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.ListExternalApisResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_external_apis

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHub server but before it is returned to user code.

        We recommend only using this `post_list_external_apis_with_metadata`
        interceptor in new development instead of the `post_list_external_apis` interceptor.
        When both interceptors are used, this `post_list_external_apis_with_metadata` interceptor runs after the
        `post_list_external_apis` interceptor. The (possibly modified) response returned by
        `post_list_external_apis` will be passed to
        `post_list_external_apis_with_metadata`.
        """
        return response, metadata

    def pre_list_specs(
        self,
        request: apihub_service.ListSpecsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.ListSpecsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_specs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def post_list_specs(
        self, response: apihub_service.ListSpecsResponse
    ) -> apihub_service.ListSpecsResponse:
        """Post-rpc interceptor for list_specs

        DEPRECATED. Please use the `post_list_specs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHub server but before
        it is returned to user code. This `post_list_specs` interceptor runs
        before the `post_list_specs_with_metadata` interceptor.
        """
        return response

    def post_list_specs_with_metadata(
        self,
        response: apihub_service.ListSpecsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.ListSpecsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_specs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHub server but before it is returned to user code.

        We recommend only using this `post_list_specs_with_metadata`
        interceptor in new development instead of the `post_list_specs` interceptor.
        When both interceptors are used, this `post_list_specs_with_metadata` interceptor runs after the
        `post_list_specs` interceptor. The (possibly modified) response returned by
        `post_list_specs` will be passed to
        `post_list_specs_with_metadata`.
        """
        return response, metadata

    def pre_list_versions(
        self,
        request: apihub_service.ListVersionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.ListVersionsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_versions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def post_list_versions(
        self, response: apihub_service.ListVersionsResponse
    ) -> apihub_service.ListVersionsResponse:
        """Post-rpc interceptor for list_versions

        DEPRECATED. Please use the `post_list_versions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHub server but before
        it is returned to user code. This `post_list_versions` interceptor runs
        before the `post_list_versions_with_metadata` interceptor.
        """
        return response

    def post_list_versions_with_metadata(
        self,
        response: apihub_service.ListVersionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.ListVersionsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_versions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHub server but before it is returned to user code.

        We recommend only using this `post_list_versions_with_metadata`
        interceptor in new development instead of the `post_list_versions` interceptor.
        When both interceptors are used, this `post_list_versions_with_metadata` interceptor runs after the
        `post_list_versions` interceptor. The (possibly modified) response returned by
        `post_list_versions` will be passed to
        `post_list_versions_with_metadata`.
        """
        return response, metadata

    def pre_search_resources(
        self,
        request: apihub_service.SearchResourcesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.SearchResourcesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for search_resources

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def post_search_resources(
        self, response: apihub_service.SearchResourcesResponse
    ) -> apihub_service.SearchResourcesResponse:
        """Post-rpc interceptor for search_resources

        DEPRECATED. Please use the `post_search_resources_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHub server but before
        it is returned to user code. This `post_search_resources` interceptor runs
        before the `post_search_resources_with_metadata` interceptor.
        """
        return response

    def post_search_resources_with_metadata(
        self,
        response: apihub_service.SearchResourcesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.SearchResourcesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for search_resources

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHub server but before it is returned to user code.

        We recommend only using this `post_search_resources_with_metadata`
        interceptor in new development instead of the `post_search_resources` interceptor.
        When both interceptors are used, this `post_search_resources_with_metadata` interceptor runs after the
        `post_search_resources` interceptor. The (possibly modified) response returned by
        `post_search_resources` will be passed to
        `post_search_resources_with_metadata`.
        """
        return response, metadata

    def pre_update_api(
        self,
        request: apihub_service.UpdateApiRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.UpdateApiRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_api

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def post_update_api(self, response: common_fields.Api) -> common_fields.Api:
        """Post-rpc interceptor for update_api

        DEPRECATED. Please use the `post_update_api_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHub server but before
        it is returned to user code. This `post_update_api` interceptor runs
        before the `post_update_api_with_metadata` interceptor.
        """
        return response

    def post_update_api_with_metadata(
        self,
        response: common_fields.Api,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[common_fields.Api, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_api

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHub server but before it is returned to user code.

        We recommend only using this `post_update_api_with_metadata`
        interceptor in new development instead of the `post_update_api` interceptor.
        When both interceptors are used, this `post_update_api_with_metadata` interceptor runs after the
        `post_update_api` interceptor. The (possibly modified) response returned by
        `post_update_api` will be passed to
        `post_update_api_with_metadata`.
        """
        return response, metadata

    def pre_update_api_operation(
        self,
        request: apihub_service.UpdateApiOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.UpdateApiOperationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_api_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def post_update_api_operation(
        self, response: common_fields.ApiOperation
    ) -> common_fields.ApiOperation:
        """Post-rpc interceptor for update_api_operation

        DEPRECATED. Please use the `post_update_api_operation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHub server but before
        it is returned to user code. This `post_update_api_operation` interceptor runs
        before the `post_update_api_operation_with_metadata` interceptor.
        """
        return response

    def post_update_api_operation_with_metadata(
        self,
        response: common_fields.ApiOperation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[common_fields.ApiOperation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_api_operation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHub server but before it is returned to user code.

        We recommend only using this `post_update_api_operation_with_metadata`
        interceptor in new development instead of the `post_update_api_operation` interceptor.
        When both interceptors are used, this `post_update_api_operation_with_metadata` interceptor runs after the
        `post_update_api_operation` interceptor. The (possibly modified) response returned by
        `post_update_api_operation` will be passed to
        `post_update_api_operation_with_metadata`.
        """
        return response, metadata

    def pre_update_attribute(
        self,
        request: apihub_service.UpdateAttributeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.UpdateAttributeRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_attribute

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def post_update_attribute(
        self, response: common_fields.Attribute
    ) -> common_fields.Attribute:
        """Post-rpc interceptor for update_attribute

        DEPRECATED. Please use the `post_update_attribute_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHub server but before
        it is returned to user code. This `post_update_attribute` interceptor runs
        before the `post_update_attribute_with_metadata` interceptor.
        """
        return response

    def post_update_attribute_with_metadata(
        self,
        response: common_fields.Attribute,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[common_fields.Attribute, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_attribute

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHub server but before it is returned to user code.

        We recommend only using this `post_update_attribute_with_metadata`
        interceptor in new development instead of the `post_update_attribute` interceptor.
        When both interceptors are used, this `post_update_attribute_with_metadata` interceptor runs after the
        `post_update_attribute` interceptor. The (possibly modified) response returned by
        `post_update_attribute` will be passed to
        `post_update_attribute_with_metadata`.
        """
        return response, metadata

    def pre_update_deployment(
        self,
        request: apihub_service.UpdateDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.UpdateDeploymentRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def post_update_deployment(
        self, response: common_fields.Deployment
    ) -> common_fields.Deployment:
        """Post-rpc interceptor for update_deployment

        DEPRECATED. Please use the `post_update_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHub server but before
        it is returned to user code. This `post_update_deployment` interceptor runs
        before the `post_update_deployment_with_metadata` interceptor.
        """
        return response

    def post_update_deployment_with_metadata(
        self,
        response: common_fields.Deployment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[common_fields.Deployment, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHub server but before it is returned to user code.

        We recommend only using this `post_update_deployment_with_metadata`
        interceptor in new development instead of the `post_update_deployment` interceptor.
        When both interceptors are used, this `post_update_deployment_with_metadata` interceptor runs after the
        `post_update_deployment` interceptor. The (possibly modified) response returned by
        `post_update_deployment` will be passed to
        `post_update_deployment_with_metadata`.
        """
        return response, metadata

    def pre_update_external_api(
        self,
        request: apihub_service.UpdateExternalApiRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.UpdateExternalApiRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_external_api

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def post_update_external_api(
        self, response: common_fields.ExternalApi
    ) -> common_fields.ExternalApi:
        """Post-rpc interceptor for update_external_api

        DEPRECATED. Please use the `post_update_external_api_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHub server but before
        it is returned to user code. This `post_update_external_api` interceptor runs
        before the `post_update_external_api_with_metadata` interceptor.
        """
        return response

    def post_update_external_api_with_metadata(
        self,
        response: common_fields.ExternalApi,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[common_fields.ExternalApi, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_external_api

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHub server but before it is returned to user code.

        We recommend only using this `post_update_external_api_with_metadata`
        interceptor in new development instead of the `post_update_external_api` interceptor.
        When both interceptors are used, this `post_update_external_api_with_metadata` interceptor runs after the
        `post_update_external_api` interceptor. The (possibly modified) response returned by
        `post_update_external_api` will be passed to
        `post_update_external_api_with_metadata`.
        """
        return response, metadata

    def pre_update_spec(
        self,
        request: apihub_service.UpdateSpecRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.UpdateSpecRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_spec

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def post_update_spec(self, response: common_fields.Spec) -> common_fields.Spec:
        """Post-rpc interceptor for update_spec

        DEPRECATED. Please use the `post_update_spec_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHub server but before
        it is returned to user code. This `post_update_spec` interceptor runs
        before the `post_update_spec_with_metadata` interceptor.
        """
        return response

    def post_update_spec_with_metadata(
        self,
        response: common_fields.Spec,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[common_fields.Spec, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_spec

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHub server but before it is returned to user code.

        We recommend only using this `post_update_spec_with_metadata`
        interceptor in new development instead of the `post_update_spec` interceptor.
        When both interceptors are used, this `post_update_spec_with_metadata` interceptor runs after the
        `post_update_spec` interceptor. The (possibly modified) response returned by
        `post_update_spec` will be passed to
        `post_update_spec_with_metadata`.
        """
        return response, metadata

    def pre_update_version(
        self,
        request: apihub_service.UpdateVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apihub_service.UpdateVersionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def post_update_version(
        self, response: common_fields.Version
    ) -> common_fields.Version:
        """Post-rpc interceptor for update_version

        DEPRECATED. Please use the `post_update_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiHub server but before
        it is returned to user code. This `post_update_version` interceptor runs
        before the `post_update_version_with_metadata` interceptor.
        """
        return response

    def post_update_version_with_metadata(
        self,
        response: common_fields.Version,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[common_fields.Version, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiHub server but before it is returned to user code.

        We recommend only using this `post_update_version_with_metadata`
        interceptor in new development instead of the `post_update_version` interceptor.
        When both interceptors are used, this `post_update_version_with_metadata` interceptor runs after the
        `post_update_version` interceptor. The (possibly modified) response returned by
        `post_update_version` will be passed to
        `post_update_version_with_metadata`.
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
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the ApiHub server but before
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
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the ApiHub server but before
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
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the ApiHub server but before
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
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the ApiHub server but before
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
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the ApiHub server but before
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
        before they are sent to the ApiHub server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the ApiHub server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class ApiHubRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: ApiHubRestInterceptor


class ApiHubRestTransport(_BaseApiHubRestTransport):
    """REST backend synchronous transport for ApiHub.

    This service provides all methods related to the API hub.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "apihub.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[ApiHubRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'apihub.googleapis.com').
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
            interceptor (Optional[ApiHubRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or ApiHubRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CreateApi(_BaseApiHubRestTransport._BaseCreateApi, ApiHubRestStub):
        def __hash__(self):
            return hash("ApiHubRestTransport.CreateApi")

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
            request: apihub_service.CreateApiRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> common_fields.Api:
            r"""Call the create api method over HTTP.

            Args:
                request (~.apihub_service.CreateApiRequest):
                    The request object. The [CreateApi][google.cloud.apihub.v1.ApiHub.CreateApi]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.common_fields.Api:
                    An API resource in the API Hub.
            """

            http_options = _BaseApiHubRestTransport._BaseCreateApi._get_http_options()
            request, metadata = self._interceptor.pre_create_api(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseCreateApi,
                    "_BaseCreateApi__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.CreateApi",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "CreateApi",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._CreateApi._get_response(
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
            resp = common_fields.Api()
            pb_resp = common_fields.Api.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_api(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_api_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = common_fields.Api.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apihub_v1.ApiHubClient.create_api",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "CreateApi",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateApiOperation(
        _BaseApiHubRestTransport._BaseCreateApiOperation, ApiHubRestStub
    ):
        def __hash__(self):
            return hash("ApiHubRestTransport.CreateApiOperation")

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
            request: apihub_service.CreateApiOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> common_fields.ApiOperation:
            r"""Call the create api operation method over HTTP.

            Args:
                request (~.apihub_service.CreateApiOperationRequest):
                    The request object. The
                [CreateApiOperation][google.cloud.apihub.v1.ApiHub.CreateApiOperation]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.common_fields.ApiOperation:
                    Represents an operation contained in
                an API version in the API Hub. An
                operation is added/updated/deleted in an
                API version when a new spec is added or
                an existing spec is updated/deleted in a
                version. Currently, an operation will be
                created only corresponding to OpenAPI
                spec as parsing is supported for OpenAPI
                spec.
                Alternatively operations can be managed
                via create,update and delete APIs,
                creation of apiOperation can be possible
                only for version with no parsed
                operations and update/delete can be
                possible only for operations created via
                create API.

            """

            http_options = (
                _BaseApiHubRestTransport._BaseCreateApiOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_api_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseCreateApiOperation,
                    "_BaseCreateApiOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.CreateApiOperation",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "CreateApiOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._CreateApiOperation._get_response(
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
            resp = common_fields.ApiOperation()
            pb_resp = common_fields.ApiOperation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_api_operation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_api_operation_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = common_fields.ApiOperation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apihub_v1.ApiHubClient.create_api_operation",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "CreateApiOperation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateAttribute(
        _BaseApiHubRestTransport._BaseCreateAttribute, ApiHubRestStub
    ):
        def __hash__(self):
            return hash("ApiHubRestTransport.CreateAttribute")

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
            request: apihub_service.CreateAttributeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> common_fields.Attribute:
            r"""Call the create attribute method over HTTP.

            Args:
                request (~.apihub_service.CreateAttributeRequest):
                    The request object. The
                [CreateAttribute][google.cloud.apihub.v1.ApiHub.CreateAttribute]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.common_fields.Attribute:
                    An attribute in the API Hub.
                An attribute is a name value pair which
                can be attached to different resources
                in the API hub based on the scope of the
                attribute. Attributes can either be
                pre-defined by the API Hub or created by
                users.

            """

            http_options = (
                _BaseApiHubRestTransport._BaseCreateAttribute._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_attribute(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseCreateAttribute,
                    "_BaseCreateAttribute__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.CreateAttribute",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "CreateAttribute",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._CreateAttribute._get_response(
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
            resp = common_fields.Attribute()
            pb_resp = common_fields.Attribute.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_attribute(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_attribute_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = common_fields.Attribute.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apihub_v1.ApiHubClient.create_attribute",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "CreateAttribute",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateDeployment(
        _BaseApiHubRestTransport._BaseCreateDeployment, ApiHubRestStub
    ):
        def __hash__(self):
            return hash("ApiHubRestTransport.CreateDeployment")

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
            request: apihub_service.CreateDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> common_fields.Deployment:
            r"""Call the create deployment method over HTTP.

            Args:
                request (~.apihub_service.CreateDeploymentRequest):
                    The request object. The
                [CreateDeployment][google.cloud.apihub.v1.ApiHub.CreateDeployment]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.common_fields.Deployment:
                    Details of the deployment where APIs
                are hosted. A deployment could represent
                an Apigee proxy, API gateway, other
                Google Cloud services or non-Google
                Cloud services as well. A deployment
                entity is a root level entity in the API
                hub and exists independent of any API.

            """

            http_options = (
                _BaseApiHubRestTransport._BaseCreateDeployment._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseCreateDeployment,
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.CreateDeployment",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "CreateDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._CreateDeployment._get_response(
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
            resp = common_fields.Deployment()
            pb_resp = common_fields.Deployment.pb(resp)

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
                    response_payload = common_fields.Deployment.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apihub_v1.ApiHubClient.create_deployment",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "CreateDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateExternalApi(
        _BaseApiHubRestTransport._BaseCreateExternalApi, ApiHubRestStub
    ):
        def __hash__(self):
            return hash("ApiHubRestTransport.CreateExternalApi")

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
            request: apihub_service.CreateExternalApiRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> common_fields.ExternalApi:
            r"""Call the create external api method over HTTP.

            Args:
                request (~.apihub_service.CreateExternalApiRequest):
                    The request object. The
                [CreateExternalApi][google.cloud.apihub.v1.ApiHub.CreateExternalApi]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.common_fields.ExternalApi:
                    An external API represents an API
                being provided by external sources. This
                can be used to model third-party APIs
                and can be used to define dependencies.

            """

            http_options = (
                _BaseApiHubRestTransport._BaseCreateExternalApi._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_external_api(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseCreateExternalApi,
                    "_BaseCreateExternalApi__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.CreateExternalApi",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "CreateExternalApi",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._CreateExternalApi._get_response(
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
            resp = common_fields.ExternalApi()
            pb_resp = common_fields.ExternalApi.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_external_api(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_external_api_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = common_fields.ExternalApi.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apihub_v1.ApiHubClient.create_external_api",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "CreateExternalApi",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateSpec(_BaseApiHubRestTransport._BaseCreateSpec, ApiHubRestStub):
        def __hash__(self):
            return hash("ApiHubRestTransport.CreateSpec")

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
            request: apihub_service.CreateSpecRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> common_fields.Spec:
            r"""Call the create spec method over HTTP.

            Args:
                request (~.apihub_service.CreateSpecRequest):
                    The request object. The
                [CreateSpec][google.cloud.apihub.v1.ApiHub.CreateSpec]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.common_fields.Spec:
                    Represents a spec associated with an
                API version in the API Hub. Note that
                specs of various types can be uploaded,
                however parsing of details is supported
                for OpenAPI spec currently.

            """

            http_options = _BaseApiHubRestTransport._BaseCreateSpec._get_http_options()
            request, metadata = self._interceptor.pre_create_spec(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseCreateSpec,
                    "_BaseCreateSpec__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.CreateSpec",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "CreateSpec",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._CreateSpec._get_response(
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
            resp = common_fields.Spec()
            pb_resp = common_fields.Spec.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_spec(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_spec_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = common_fields.Spec.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apihub_v1.ApiHubClient.create_spec",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "CreateSpec",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateVersion(_BaseApiHubRestTransport._BaseCreateVersion, ApiHubRestStub):
        def __hash__(self):
            return hash("ApiHubRestTransport.CreateVersion")

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
            request: apihub_service.CreateVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> common_fields.Version:
            r"""Call the create version method over HTTP.

            Args:
                request (~.apihub_service.CreateVersionRequest):
                    The request object. The
                [CreateVersion][google.cloud.apihub.v1.ApiHub.CreateVersion]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.common_fields.Version:
                    Represents a version of the API
                resource in API hub. This is also
                referred to as the API version.

            """

            http_options = (
                _BaseApiHubRestTransport._BaseCreateVersion._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_version(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseCreateVersion,
                    "_BaseCreateVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.CreateVersion",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "CreateVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._CreateVersion._get_response(
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
            resp = common_fields.Version()
            pb_resp = common_fields.Version.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_version_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = common_fields.Version.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apihub_v1.ApiHubClient.create_version",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "CreateVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteApi(_BaseApiHubRestTransport._BaseDeleteApi, ApiHubRestStub):
        def __hash__(self):
            return hash("ApiHubRestTransport.DeleteApi")

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
            request: apihub_service.DeleteApiRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete api method over HTTP.

            Args:
                request (~.apihub_service.DeleteApiRequest):
                    The request object. The [DeleteApi][google.cloud.apihub.v1.ApiHub.DeleteApi]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseApiHubRestTransport._BaseDeleteApi._get_http_options()
            request, metadata = self._interceptor.pre_delete_api(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseDeleteApi,
                    "_BaseDeleteApi__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.DeleteApi",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "DeleteApi",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._DeleteApi._get_response(
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

    class _DeleteApiOperation(
        _BaseApiHubRestTransport._BaseDeleteApiOperation, ApiHubRestStub
    ):
        def __hash__(self):
            return hash("ApiHubRestTransport.DeleteApiOperation")

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
            request: apihub_service.DeleteApiOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete api operation method over HTTP.

            Args:
                request (~.apihub_service.DeleteApiOperationRequest):
                    The request object. The
                [DeleteApiOperation][google.cloud.apihub.v1.ApiHub.DeleteApiOperation]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseApiHubRestTransport._BaseDeleteApiOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_api_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseDeleteApiOperation,
                    "_BaseDeleteApiOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.DeleteApiOperation",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "DeleteApiOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._DeleteApiOperation._get_response(
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

    class _DeleteAttribute(
        _BaseApiHubRestTransport._BaseDeleteAttribute, ApiHubRestStub
    ):
        def __hash__(self):
            return hash("ApiHubRestTransport.DeleteAttribute")

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
            request: apihub_service.DeleteAttributeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete attribute method over HTTP.

            Args:
                request (~.apihub_service.DeleteAttributeRequest):
                    The request object. The
                [DeleteAttribute][google.cloud.apihub.v1.ApiHub.DeleteAttribute]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseApiHubRestTransport._BaseDeleteAttribute._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_attribute(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseDeleteAttribute,
                    "_BaseDeleteAttribute__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.DeleteAttribute",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "DeleteAttribute",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._DeleteAttribute._get_response(
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

    class _DeleteDeployment(
        _BaseApiHubRestTransport._BaseDeleteDeployment, ApiHubRestStub
    ):
        def __hash__(self):
            return hash("ApiHubRestTransport.DeleteDeployment")

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
            request: apihub_service.DeleteDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete deployment method over HTTP.

            Args:
                request (~.apihub_service.DeleteDeploymentRequest):
                    The request object. The
                [DeleteDeployment][google.cloud.apihub.v1.ApiHub.DeleteDeployment]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseApiHubRestTransport._BaseDeleteDeployment._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseDeleteDeployment,
                    "_BaseDeleteDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.DeleteDeployment",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "DeleteDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._DeleteDeployment._get_response(
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

    class _DeleteExternalApi(
        _BaseApiHubRestTransport._BaseDeleteExternalApi, ApiHubRestStub
    ):
        def __hash__(self):
            return hash("ApiHubRestTransport.DeleteExternalApi")

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
            request: apihub_service.DeleteExternalApiRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete external api method over HTTP.

            Args:
                request (~.apihub_service.DeleteExternalApiRequest):
                    The request object. The
                [DeleteExternalApi][google.cloud.apihub.v1.ApiHub.DeleteExternalApi]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseApiHubRestTransport._BaseDeleteExternalApi._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_external_api(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseDeleteExternalApi,
                    "_BaseDeleteExternalApi__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.DeleteExternalApi",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "DeleteExternalApi",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._DeleteExternalApi._get_response(
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

    class _DeleteSpec(_BaseApiHubRestTransport._BaseDeleteSpec, ApiHubRestStub):
        def __hash__(self):
            return hash("ApiHubRestTransport.DeleteSpec")

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
            request: apihub_service.DeleteSpecRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete spec method over HTTP.

            Args:
                request (~.apihub_service.DeleteSpecRequest):
                    The request object. The
                [DeleteSpec][google.cloud.apihub.v1.ApiHub.DeleteSpec]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseApiHubRestTransport._BaseDeleteSpec._get_http_options()
            request, metadata = self._interceptor.pre_delete_spec(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseDeleteSpec,
                    "_BaseDeleteSpec__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.DeleteSpec",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "DeleteSpec",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._DeleteSpec._get_response(
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

    class _DeleteVersion(_BaseApiHubRestTransport._BaseDeleteVersion, ApiHubRestStub):
        def __hash__(self):
            return hash("ApiHubRestTransport.DeleteVersion")

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
            request: apihub_service.DeleteVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete version method over HTTP.

            Args:
                request (~.apihub_service.DeleteVersionRequest):
                    The request object. The
                [DeleteVersion][google.cloud.apihub.v1.ApiHub.DeleteVersion]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseApiHubRestTransport._BaseDeleteVersion._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_version(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseDeleteVersion,
                    "_BaseDeleteVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.DeleteVersion",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "DeleteVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._DeleteVersion._get_response(
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

    class _GetApi(_BaseApiHubRestTransport._BaseGetApi, ApiHubRestStub):
        def __hash__(self):
            return hash("ApiHubRestTransport.GetApi")

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
            request: apihub_service.GetApiRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> common_fields.Api:
            r"""Call the get api method over HTTP.

            Args:
                request (~.apihub_service.GetApiRequest):
                    The request object. The [GetApi][google.cloud.apihub.v1.ApiHub.GetApi]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.common_fields.Api:
                    An API resource in the API Hub.
            """

            http_options = _BaseApiHubRestTransport._BaseGetApi._get_http_options()
            request, metadata = self._interceptor.pre_get_api(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseGetApi,
                    "_BaseGetApi__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.GetApi",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "GetApi",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._GetApi._get_response(
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
            resp = common_fields.Api()
            pb_resp = common_fields.Api.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_api(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_api_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = common_fields.Api.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apihub_v1.ApiHubClient.get_api",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "GetApi",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetApiOperation(
        _BaseApiHubRestTransport._BaseGetApiOperation, ApiHubRestStub
    ):
        def __hash__(self):
            return hash("ApiHubRestTransport.GetApiOperation")

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
            request: apihub_service.GetApiOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> common_fields.ApiOperation:
            r"""Call the get api operation method over HTTP.

            Args:
                request (~.apihub_service.GetApiOperationRequest):
                    The request object. The
                [GetApiOperation][google.cloud.apihub.v1.ApiHub.GetApiOperation]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.common_fields.ApiOperation:
                    Represents an operation contained in
                an API version in the API Hub. An
                operation is added/updated/deleted in an
                API version when a new spec is added or
                an existing spec is updated/deleted in a
                version. Currently, an operation will be
                created only corresponding to OpenAPI
                spec as parsing is supported for OpenAPI
                spec.
                Alternatively operations can be managed
                via create,update and delete APIs,
                creation of apiOperation can be possible
                only for version with no parsed
                operations and update/delete can be
                possible only for operations created via
                create API.

            """

            http_options = (
                _BaseApiHubRestTransport._BaseGetApiOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_api_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseGetApiOperation,
                    "_BaseGetApiOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.GetApiOperation",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "GetApiOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._GetApiOperation._get_response(
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
            resp = common_fields.ApiOperation()
            pb_resp = common_fields.ApiOperation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_api_operation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_api_operation_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = common_fields.ApiOperation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apihub_v1.ApiHubClient.get_api_operation",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "GetApiOperation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAttribute(_BaseApiHubRestTransport._BaseGetAttribute, ApiHubRestStub):
        def __hash__(self):
            return hash("ApiHubRestTransport.GetAttribute")

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
            request: apihub_service.GetAttributeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> common_fields.Attribute:
            r"""Call the get attribute method over HTTP.

            Args:
                request (~.apihub_service.GetAttributeRequest):
                    The request object. The
                [GetAttribute][google.cloud.apihub.v1.ApiHub.GetAttribute]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.common_fields.Attribute:
                    An attribute in the API Hub.
                An attribute is a name value pair which
                can be attached to different resources
                in the API hub based on the scope of the
                attribute. Attributes can either be
                pre-defined by the API Hub or created by
                users.

            """

            http_options = (
                _BaseApiHubRestTransport._BaseGetAttribute._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_attribute(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseGetAttribute,
                    "_BaseGetAttribute__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.GetAttribute",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "GetAttribute",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._GetAttribute._get_response(
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
            resp = common_fields.Attribute()
            pb_resp = common_fields.Attribute.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_attribute(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_attribute_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = common_fields.Attribute.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apihub_v1.ApiHubClient.get_attribute",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "GetAttribute",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDefinition(_BaseApiHubRestTransport._BaseGetDefinition, ApiHubRestStub):
        def __hash__(self):
            return hash("ApiHubRestTransport.GetDefinition")

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
            request: apihub_service.GetDefinitionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> common_fields.Definition:
            r"""Call the get definition method over HTTP.

            Args:
                request (~.apihub_service.GetDefinitionRequest):
                    The request object. The
                [GetDefinition][google.cloud.apihub.v1.ApiHub.GetDefinition]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.common_fields.Definition:
                    Represents a definition for example schema, request,
                response definitions contained in an API version. A
                definition is added/updated/deleted in an API version
                when a new spec is added or an existing spec is
                updated/deleted in a version. Currently, definition will
                be created only corresponding to OpenAPI spec as parsing
                is supported for OpenAPI spec. Also, within OpenAPI
                spec, only ``schema`` object is supported.

            """

            http_options = (
                _BaseApiHubRestTransport._BaseGetDefinition._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_definition(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseGetDefinition,
                    "_BaseGetDefinition__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.GetDefinition",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "GetDefinition",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._GetDefinition._get_response(
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
            resp = common_fields.Definition()
            pb_resp = common_fields.Definition.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_definition(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_definition_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = common_fields.Definition.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apihub_v1.ApiHubClient.get_definition",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "GetDefinition",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDeployment(_BaseApiHubRestTransport._BaseGetDeployment, ApiHubRestStub):
        def __hash__(self):
            return hash("ApiHubRestTransport.GetDeployment")

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
            request: apihub_service.GetDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> common_fields.Deployment:
            r"""Call the get deployment method over HTTP.

            Args:
                request (~.apihub_service.GetDeploymentRequest):
                    The request object. The
                [GetDeployment][google.cloud.apihub.v1.ApiHub.GetDeployment]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.common_fields.Deployment:
                    Details of the deployment where APIs
                are hosted. A deployment could represent
                an Apigee proxy, API gateway, other
                Google Cloud services or non-Google
                Cloud services as well. A deployment
                entity is a root level entity in the API
                hub and exists independent of any API.

            """

            http_options = (
                _BaseApiHubRestTransport._BaseGetDeployment._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_deployment(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseGetDeployment,
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.GetDeployment",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "GetDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._GetDeployment._get_response(
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
            resp = common_fields.Deployment()
            pb_resp = common_fields.Deployment.pb(resp)

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
                    response_payload = common_fields.Deployment.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apihub_v1.ApiHubClient.get_deployment",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "GetDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetExternalApi(_BaseApiHubRestTransport._BaseGetExternalApi, ApiHubRestStub):
        def __hash__(self):
            return hash("ApiHubRestTransport.GetExternalApi")

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
            request: apihub_service.GetExternalApiRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> common_fields.ExternalApi:
            r"""Call the get external api method over HTTP.

            Args:
                request (~.apihub_service.GetExternalApiRequest):
                    The request object. The
                [GetExternalApi][google.cloud.apihub.v1.ApiHub.GetExternalApi]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.common_fields.ExternalApi:
                    An external API represents an API
                being provided by external sources. This
                can be used to model third-party APIs
                and can be used to define dependencies.

            """

            http_options = (
                _BaseApiHubRestTransport._BaseGetExternalApi._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_external_api(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseGetExternalApi,
                    "_BaseGetExternalApi__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.GetExternalApi",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "GetExternalApi",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._GetExternalApi._get_response(
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
            resp = common_fields.ExternalApi()
            pb_resp = common_fields.ExternalApi.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_external_api(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_external_api_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = common_fields.ExternalApi.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apihub_v1.ApiHubClient.get_external_api",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "GetExternalApi",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetSpec(_BaseApiHubRestTransport._BaseGetSpec, ApiHubRestStub):
        def __hash__(self):
            return hash("ApiHubRestTransport.GetSpec")

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
            request: apihub_service.GetSpecRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> common_fields.Spec:
            r"""Call the get spec method over HTTP.

            Args:
                request (~.apihub_service.GetSpecRequest):
                    The request object. The [GetSpec][google.cloud.apihub.v1.ApiHub.GetSpec]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.common_fields.Spec:
                    Represents a spec associated with an
                API version in the API Hub. Note that
                specs of various types can be uploaded,
                however parsing of details is supported
                for OpenAPI spec currently.

            """

            http_options = _BaseApiHubRestTransport._BaseGetSpec._get_http_options()
            request, metadata = self._interceptor.pre_get_spec(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseGetSpec,
                    "_BaseGetSpec__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.GetSpec",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "GetSpec",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._GetSpec._get_response(
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
            resp = common_fields.Spec()
            pb_resp = common_fields.Spec.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_spec(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_spec_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = common_fields.Spec.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apihub_v1.ApiHubClient.get_spec",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "GetSpec",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetSpecContents(
        _BaseApiHubRestTransport._BaseGetSpecContents, ApiHubRestStub
    ):
        def __hash__(self):
            return hash("ApiHubRestTransport.GetSpecContents")

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
            request: apihub_service.GetSpecContentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> common_fields.SpecContents:
            r"""Call the get spec contents method over HTTP.

            Args:
                request (~.apihub_service.GetSpecContentsRequest):
                    The request object. The
                [GetSpecContents][google.cloud.apihub.v1.ApiHub.GetSpecContents]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.common_fields.SpecContents:
                    The spec contents.
            """

            http_options = (
                _BaseApiHubRestTransport._BaseGetSpecContents._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_spec_contents(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseGetSpecContents,
                    "_BaseGetSpecContents__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.GetSpecContents",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "GetSpecContents",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._GetSpecContents._get_response(
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
            resp = common_fields.SpecContents()
            pb_resp = common_fields.SpecContents.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_spec_contents(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_spec_contents_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = common_fields.SpecContents.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apihub_v1.ApiHubClient.get_spec_contents",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "GetSpecContents",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetVersion(_BaseApiHubRestTransport._BaseGetVersion, ApiHubRestStub):
        def __hash__(self):
            return hash("ApiHubRestTransport.GetVersion")

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
            request: apihub_service.GetVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> common_fields.Version:
            r"""Call the get version method over HTTP.

            Args:
                request (~.apihub_service.GetVersionRequest):
                    The request object. The
                [GetVersion][google.cloud.apihub.v1.ApiHub.GetVersion]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.common_fields.Version:
                    Represents a version of the API
                resource in API hub. This is also
                referred to as the API version.

            """

            http_options = _BaseApiHubRestTransport._BaseGetVersion._get_http_options()
            request, metadata = self._interceptor.pre_get_version(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseGetVersion,
                    "_BaseGetVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.GetVersion",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "GetVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._GetVersion._get_response(
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
            resp = common_fields.Version()
            pb_resp = common_fields.Version.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_version_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = common_fields.Version.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apihub_v1.ApiHubClient.get_version",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "GetVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListApiOperations(
        _BaseApiHubRestTransport._BaseListApiOperations, ApiHubRestStub
    ):
        def __hash__(self):
            return hash("ApiHubRestTransport.ListApiOperations")

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
            request: apihub_service.ListApiOperationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> apihub_service.ListApiOperationsResponse:
            r"""Call the list api operations method over HTTP.

            Args:
                request (~.apihub_service.ListApiOperationsRequest):
                    The request object. The
                [ListApiOperations][google.cloud.apihub.v1.ApiHub.ListApiOperations]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.apihub_service.ListApiOperationsResponse:
                    The
                [ListApiOperations][google.cloud.apihub.v1.ApiHub.ListApiOperations]
                method's response.

            """

            http_options = (
                _BaseApiHubRestTransport._BaseListApiOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_api_operations(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseListApiOperations,
                    "_BaseListApiOperations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.ListApiOperations",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "ListApiOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._ListApiOperations._get_response(
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
            resp = apihub_service.ListApiOperationsResponse()
            pb_resp = apihub_service.ListApiOperationsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_api_operations(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_api_operations_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = apihub_service.ListApiOperationsResponse.to_json(
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
                    "Received response for google.cloud.apihub_v1.ApiHubClient.list_api_operations",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "ListApiOperations",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListApis(_BaseApiHubRestTransport._BaseListApis, ApiHubRestStub):
        def __hash__(self):
            return hash("ApiHubRestTransport.ListApis")

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
            request: apihub_service.ListApisRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> apihub_service.ListApisResponse:
            r"""Call the list apis method over HTTP.

            Args:
                request (~.apihub_service.ListApisRequest):
                    The request object. The [ListApis][google.cloud.apihub.v1.ApiHub.ListApis]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.apihub_service.ListApisResponse:
                    The [ListApis][google.cloud.apihub.v1.ApiHub.ListApis]
                method's response.

            """

            http_options = _BaseApiHubRestTransport._BaseListApis._get_http_options()
            request, metadata = self._interceptor.pre_list_apis(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseListApis,
                    "_BaseListApis__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.ListApis",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "ListApis",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._ListApis._get_response(
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
            resp = apihub_service.ListApisResponse()
            pb_resp = apihub_service.ListApisResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_apis(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_apis_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = apihub_service.ListApisResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apihub_v1.ApiHubClient.list_apis",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "ListApis",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAttributes(_BaseApiHubRestTransport._BaseListAttributes, ApiHubRestStub):
        def __hash__(self):
            return hash("ApiHubRestTransport.ListAttributes")

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
            request: apihub_service.ListAttributesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> apihub_service.ListAttributesResponse:
            r"""Call the list attributes method over HTTP.

            Args:
                request (~.apihub_service.ListAttributesRequest):
                    The request object. The
                [ListAttributes][google.cloud.apihub.v1.ApiHub.ListAttributes]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.apihub_service.ListAttributesResponse:
                    The
                [ListAttributes][google.cloud.apihub.v1.ApiHub.ListAttributes]
                method's response.

            """

            http_options = (
                _BaseApiHubRestTransport._BaseListAttributes._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_attributes(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseListAttributes,
                    "_BaseListAttributes__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.ListAttributes",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "ListAttributes",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._ListAttributes._get_response(
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
            resp = apihub_service.ListAttributesResponse()
            pb_resp = apihub_service.ListAttributesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_attributes(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_attributes_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = apihub_service.ListAttributesResponse.to_json(
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
                    "Received response for google.cloud.apihub_v1.ApiHubClient.list_attributes",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "ListAttributes",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDeployments(
        _BaseApiHubRestTransport._BaseListDeployments, ApiHubRestStub
    ):
        def __hash__(self):
            return hash("ApiHubRestTransport.ListDeployments")

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
            request: apihub_service.ListDeploymentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> apihub_service.ListDeploymentsResponse:
            r"""Call the list deployments method over HTTP.

            Args:
                request (~.apihub_service.ListDeploymentsRequest):
                    The request object. The
                [ListDeployments][google.cloud.apihub.v1.ApiHub.ListDeployments]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.apihub_service.ListDeploymentsResponse:
                    The
                [ListDeployments][google.cloud.apihub.v1.ApiHub.ListDeployments]
                method's response.

            """

            http_options = (
                _BaseApiHubRestTransport._BaseListDeployments._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_deployments(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseListDeployments,
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.ListDeployments",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "ListDeployments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._ListDeployments._get_response(
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
            resp = apihub_service.ListDeploymentsResponse()
            pb_resp = apihub_service.ListDeploymentsResponse.pb(resp)

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
                    response_payload = apihub_service.ListDeploymentsResponse.to_json(
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
                    "Received response for google.cloud.apihub_v1.ApiHubClient.list_deployments",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "ListDeployments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListExternalApis(
        _BaseApiHubRestTransport._BaseListExternalApis, ApiHubRestStub
    ):
        def __hash__(self):
            return hash("ApiHubRestTransport.ListExternalApis")

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
            request: apihub_service.ListExternalApisRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> apihub_service.ListExternalApisResponse:
            r"""Call the list external apis method over HTTP.

            Args:
                request (~.apihub_service.ListExternalApisRequest):
                    The request object. The
                [ListExternalApis][google.cloud.apihub.v1.ApiHub.ListExternalApis]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.apihub_service.ListExternalApisResponse:
                    The
                [ListExternalApis][google.cloud.apihub.v1.ApiHub.ListExternalApis]
                method's response.

            """

            http_options = (
                _BaseApiHubRestTransport._BaseListExternalApis._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_external_apis(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseListExternalApis,
                    "_BaseListExternalApis__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.ListExternalApis",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "ListExternalApis",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._ListExternalApis._get_response(
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
            resp = apihub_service.ListExternalApisResponse()
            pb_resp = apihub_service.ListExternalApisResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_external_apis(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_external_apis_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = apihub_service.ListExternalApisResponse.to_json(
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
                    "Received response for google.cloud.apihub_v1.ApiHubClient.list_external_apis",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "ListExternalApis",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListSpecs(_BaseApiHubRestTransport._BaseListSpecs, ApiHubRestStub):
        def __hash__(self):
            return hash("ApiHubRestTransport.ListSpecs")

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
            request: apihub_service.ListSpecsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> apihub_service.ListSpecsResponse:
            r"""Call the list specs method over HTTP.

            Args:
                request (~.apihub_service.ListSpecsRequest):
                    The request object. The [ListSpecs][ListSpecs] method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.apihub_service.ListSpecsResponse:
                    The [ListSpecs][google.cloud.apihub.v1.ApiHub.ListSpecs]
                method's response.

            """

            http_options = _BaseApiHubRestTransport._BaseListSpecs._get_http_options()
            request, metadata = self._interceptor.pre_list_specs(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseListSpecs,
                    "_BaseListSpecs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.ListSpecs",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "ListSpecs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._ListSpecs._get_response(
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
            resp = apihub_service.ListSpecsResponse()
            pb_resp = apihub_service.ListSpecsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_specs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_specs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = apihub_service.ListSpecsResponse.to_json(
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
                    "Received response for google.cloud.apihub_v1.ApiHubClient.list_specs",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "ListSpecs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListVersions(_BaseApiHubRestTransport._BaseListVersions, ApiHubRestStub):
        def __hash__(self):
            return hash("ApiHubRestTransport.ListVersions")

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
            request: apihub_service.ListVersionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> apihub_service.ListVersionsResponse:
            r"""Call the list versions method over HTTP.

            Args:
                request (~.apihub_service.ListVersionsRequest):
                    The request object. The
                [ListVersions][google.cloud.apihub.v1.ApiHub.ListVersions]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.apihub_service.ListVersionsResponse:
                    The
                [ListVersions][google.cloud.apihub.v1.ApiHub.ListVersions]
                method's response.

            """

            http_options = (
                _BaseApiHubRestTransport._BaseListVersions._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_versions(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseListVersions,
                    "_BaseListVersions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.ListVersions",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "ListVersions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._ListVersions._get_response(
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
            resp = apihub_service.ListVersionsResponse()
            pb_resp = apihub_service.ListVersionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_versions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_versions_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = apihub_service.ListVersionsResponse.to_json(
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
                    "Received response for google.cloud.apihub_v1.ApiHubClient.list_versions",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "ListVersions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SearchResources(
        _BaseApiHubRestTransport._BaseSearchResources, ApiHubRestStub
    ):
        def __hash__(self):
            return hash("ApiHubRestTransport.SearchResources")

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
            request: apihub_service.SearchResourcesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> apihub_service.SearchResourcesResponse:
            r"""Call the search resources method over HTTP.

            Args:
                request (~.apihub_service.SearchResourcesRequest):
                    The request object. The
                [SearchResources][google.cloud.apihub.v1.ApiHub.SearchResources]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.apihub_service.SearchResourcesResponse:
                    Response for the
                [SearchResources][google.cloud.apihub.v1.ApiHub.SearchResources]
                method.

            """

            http_options = (
                _BaseApiHubRestTransport._BaseSearchResources._get_http_options()
            )
            request, metadata = self._interceptor.pre_search_resources(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseSearchResources,
                    "_BaseSearchResources__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.SearchResources",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "SearchResources",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._SearchResources._get_response(
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
            resp = apihub_service.SearchResourcesResponse()
            pb_resp = apihub_service.SearchResourcesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_search_resources(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_search_resources_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = apihub_service.SearchResourcesResponse.to_json(
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
                    "Received response for google.cloud.apihub_v1.ApiHubClient.search_resources",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "SearchResources",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateApi(_BaseApiHubRestTransport._BaseUpdateApi, ApiHubRestStub):
        def __hash__(self):
            return hash("ApiHubRestTransport.UpdateApi")

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
            request: apihub_service.UpdateApiRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> common_fields.Api:
            r"""Call the update api method over HTTP.

            Args:
                request (~.apihub_service.UpdateApiRequest):
                    The request object. The [UpdateApi][google.cloud.apihub.v1.ApiHub.UpdateApi]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.common_fields.Api:
                    An API resource in the API Hub.
            """

            http_options = _BaseApiHubRestTransport._BaseUpdateApi._get_http_options()
            request, metadata = self._interceptor.pre_update_api(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseUpdateApi,
                    "_BaseUpdateApi__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.UpdateApi",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "UpdateApi",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._UpdateApi._get_response(
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
            resp = common_fields.Api()
            pb_resp = common_fields.Api.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_api(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_api_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = common_fields.Api.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apihub_v1.ApiHubClient.update_api",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "UpdateApi",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateApiOperation(
        _BaseApiHubRestTransport._BaseUpdateApiOperation, ApiHubRestStub
    ):
        def __hash__(self):
            return hash("ApiHubRestTransport.UpdateApiOperation")

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
            request: apihub_service.UpdateApiOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> common_fields.ApiOperation:
            r"""Call the update api operation method over HTTP.

            Args:
                request (~.apihub_service.UpdateApiOperationRequest):
                    The request object. The
                [UpdateApiOperation][google.cloud.apihub.v1.ApiHub.UpdateApiOperation]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.common_fields.ApiOperation:
                    Represents an operation contained in
                an API version in the API Hub. An
                operation is added/updated/deleted in an
                API version when a new spec is added or
                an existing spec is updated/deleted in a
                version. Currently, an operation will be
                created only corresponding to OpenAPI
                spec as parsing is supported for OpenAPI
                spec.
                Alternatively operations can be managed
                via create,update and delete APIs,
                creation of apiOperation can be possible
                only for version with no parsed
                operations and update/delete can be
                possible only for operations created via
                create API.

            """

            http_options = (
                _BaseApiHubRestTransport._BaseUpdateApiOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_api_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseUpdateApiOperation,
                    "_BaseUpdateApiOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.UpdateApiOperation",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "UpdateApiOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._UpdateApiOperation._get_response(
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
            resp = common_fields.ApiOperation()
            pb_resp = common_fields.ApiOperation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_api_operation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_api_operation_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = common_fields.ApiOperation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apihub_v1.ApiHubClient.update_api_operation",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "UpdateApiOperation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateAttribute(
        _BaseApiHubRestTransport._BaseUpdateAttribute, ApiHubRestStub
    ):
        def __hash__(self):
            return hash("ApiHubRestTransport.UpdateAttribute")

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
            request: apihub_service.UpdateAttributeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> common_fields.Attribute:
            r"""Call the update attribute method over HTTP.

            Args:
                request (~.apihub_service.UpdateAttributeRequest):
                    The request object. The
                [UpdateAttribute][google.cloud.apihub.v1.ApiHub.UpdateAttribute]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.common_fields.Attribute:
                    An attribute in the API Hub.
                An attribute is a name value pair which
                can be attached to different resources
                in the API hub based on the scope of the
                attribute. Attributes can either be
                pre-defined by the API Hub or created by
                users.

            """

            http_options = (
                _BaseApiHubRestTransport._BaseUpdateAttribute._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_attribute(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseUpdateAttribute,
                    "_BaseUpdateAttribute__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.UpdateAttribute",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "UpdateAttribute",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._UpdateAttribute._get_response(
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
            resp = common_fields.Attribute()
            pb_resp = common_fields.Attribute.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_attribute(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_attribute_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = common_fields.Attribute.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apihub_v1.ApiHubClient.update_attribute",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "UpdateAttribute",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateDeployment(
        _BaseApiHubRestTransport._BaseUpdateDeployment, ApiHubRestStub
    ):
        def __hash__(self):
            return hash("ApiHubRestTransport.UpdateDeployment")

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
            request: apihub_service.UpdateDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> common_fields.Deployment:
            r"""Call the update deployment method over HTTP.

            Args:
                request (~.apihub_service.UpdateDeploymentRequest):
                    The request object. The
                [UpdateDeployment][google.cloud.apihub.v1.ApiHub.UpdateDeployment]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.common_fields.Deployment:
                    Details of the deployment where APIs
                are hosted. A deployment could represent
                an Apigee proxy, API gateway, other
                Google Cloud services or non-Google
                Cloud services as well. A deployment
                entity is a root level entity in the API
                hub and exists independent of any API.

            """

            http_options = (
                _BaseApiHubRestTransport._BaseUpdateDeployment._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseUpdateDeployment,
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.UpdateDeployment",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "UpdateDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._UpdateDeployment._get_response(
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
            resp = common_fields.Deployment()
            pb_resp = common_fields.Deployment.pb(resp)

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
                    response_payload = common_fields.Deployment.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apihub_v1.ApiHubClient.update_deployment",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "UpdateDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateExternalApi(
        _BaseApiHubRestTransport._BaseUpdateExternalApi, ApiHubRestStub
    ):
        def __hash__(self):
            return hash("ApiHubRestTransport.UpdateExternalApi")

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
            request: apihub_service.UpdateExternalApiRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> common_fields.ExternalApi:
            r"""Call the update external api method over HTTP.

            Args:
                request (~.apihub_service.UpdateExternalApiRequest):
                    The request object. The
                [UpdateExternalApi][google.cloud.apihub.v1.ApiHub.UpdateExternalApi]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.common_fields.ExternalApi:
                    An external API represents an API
                being provided by external sources. This
                can be used to model third-party APIs
                and can be used to define dependencies.

            """

            http_options = (
                _BaseApiHubRestTransport._BaseUpdateExternalApi._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_external_api(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseUpdateExternalApi,
                    "_BaseUpdateExternalApi__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.UpdateExternalApi",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "UpdateExternalApi",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._UpdateExternalApi._get_response(
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
            resp = common_fields.ExternalApi()
            pb_resp = common_fields.ExternalApi.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_external_api(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_external_api_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = common_fields.ExternalApi.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apihub_v1.ApiHubClient.update_external_api",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "UpdateExternalApi",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateSpec(_BaseApiHubRestTransport._BaseUpdateSpec, ApiHubRestStub):
        def __hash__(self):
            return hash("ApiHubRestTransport.UpdateSpec")

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
            request: apihub_service.UpdateSpecRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> common_fields.Spec:
            r"""Call the update spec method over HTTP.

            Args:
                request (~.apihub_service.UpdateSpecRequest):
                    The request object. The
                [UpdateSpec][google.cloud.apihub.v1.ApiHub.UpdateSpec]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.common_fields.Spec:
                    Represents a spec associated with an
                API version in the API Hub. Note that
                specs of various types can be uploaded,
                however parsing of details is supported
                for OpenAPI spec currently.

            """

            http_options = _BaseApiHubRestTransport._BaseUpdateSpec._get_http_options()
            request, metadata = self._interceptor.pre_update_spec(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseUpdateSpec,
                    "_BaseUpdateSpec__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.UpdateSpec",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "UpdateSpec",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._UpdateSpec._get_response(
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
            resp = common_fields.Spec()
            pb_resp = common_fields.Spec.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_spec(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_spec_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = common_fields.Spec.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apihub_v1.ApiHubClient.update_spec",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "UpdateSpec",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateVersion(_BaseApiHubRestTransport._BaseUpdateVersion, ApiHubRestStub):
        def __hash__(self):
            return hash("ApiHubRestTransport.UpdateVersion")

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
            request: apihub_service.UpdateVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> common_fields.Version:
            r"""Call the update version method over HTTP.

            Args:
                request (~.apihub_service.UpdateVersionRequest):
                    The request object. The
                [UpdateVersion][google.cloud.apihub.v1.ApiHub.UpdateVersion]
                method's request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.common_fields.Version:
                    Represents a version of the API
                resource in API hub. This is also
                referred to as the API version.

            """

            http_options = (
                _BaseApiHubRestTransport._BaseUpdateVersion._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_version(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseUpdateVersion,
                    "_BaseUpdateVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.UpdateVersion",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "UpdateVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._UpdateVersion._get_response(
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
            resp = common_fields.Version()
            pb_resp = common_fields.Version.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_version_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = common_fields.Version.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apihub_v1.ApiHubClient.update_version",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "UpdateVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_api(
        self,
    ) -> Callable[[apihub_service.CreateApiRequest], common_fields.Api]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateApi(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_api_operation(
        self,
    ) -> Callable[
        [apihub_service.CreateApiOperationRequest], common_fields.ApiOperation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateApiOperation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_attribute(
        self,
    ) -> Callable[[apihub_service.CreateAttributeRequest], common_fields.Attribute]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateAttribute(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_deployment(
        self,
    ) -> Callable[[apihub_service.CreateDeploymentRequest], common_fields.Deployment]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateDeployment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_external_api(
        self,
    ) -> Callable[[apihub_service.CreateExternalApiRequest], common_fields.ExternalApi]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateExternalApi(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_spec(
        self,
    ) -> Callable[[apihub_service.CreateSpecRequest], common_fields.Spec]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateSpec(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_version(
        self,
    ) -> Callable[[apihub_service.CreateVersionRequest], common_fields.Version]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateVersion(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_api(
        self,
    ) -> Callable[[apihub_service.DeleteApiRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteApi(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_api_operation(
        self,
    ) -> Callable[[apihub_service.DeleteApiOperationRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteApiOperation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_attribute(
        self,
    ) -> Callable[[apihub_service.DeleteAttributeRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteAttribute(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_deployment(
        self,
    ) -> Callable[[apihub_service.DeleteDeploymentRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteDeployment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_external_api(
        self,
    ) -> Callable[[apihub_service.DeleteExternalApiRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteExternalApi(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_spec(
        self,
    ) -> Callable[[apihub_service.DeleteSpecRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteSpec(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_version(
        self,
    ) -> Callable[[apihub_service.DeleteVersionRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteVersion(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_api(self) -> Callable[[apihub_service.GetApiRequest], common_fields.Api]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetApi(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_api_operation(
        self,
    ) -> Callable[[apihub_service.GetApiOperationRequest], common_fields.ApiOperation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetApiOperation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_attribute(
        self,
    ) -> Callable[[apihub_service.GetAttributeRequest], common_fields.Attribute]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAttribute(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_definition(
        self,
    ) -> Callable[[apihub_service.GetDefinitionRequest], common_fields.Definition]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDefinition(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_deployment(
        self,
    ) -> Callable[[apihub_service.GetDeploymentRequest], common_fields.Deployment]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDeployment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_external_api(
        self,
    ) -> Callable[[apihub_service.GetExternalApiRequest], common_fields.ExternalApi]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetExternalApi(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_spec(self) -> Callable[[apihub_service.GetSpecRequest], common_fields.Spec]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSpec(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_spec_contents(
        self,
    ) -> Callable[[apihub_service.GetSpecContentsRequest], common_fields.SpecContents]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSpecContents(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_version(
        self,
    ) -> Callable[[apihub_service.GetVersionRequest], common_fields.Version]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetVersion(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_api_operations(
        self,
    ) -> Callable[
        [apihub_service.ListApiOperationsRequest],
        apihub_service.ListApiOperationsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListApiOperations(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_apis(
        self,
    ) -> Callable[[apihub_service.ListApisRequest], apihub_service.ListApisResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListApis(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_attributes(
        self,
    ) -> Callable[
        [apihub_service.ListAttributesRequest], apihub_service.ListAttributesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAttributes(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_deployments(
        self,
    ) -> Callable[
        [apihub_service.ListDeploymentsRequest], apihub_service.ListDeploymentsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDeployments(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_external_apis(
        self,
    ) -> Callable[
        [apihub_service.ListExternalApisRequest],
        apihub_service.ListExternalApisResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListExternalApis(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_specs(
        self,
    ) -> Callable[[apihub_service.ListSpecsRequest], apihub_service.ListSpecsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListSpecs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_versions(
        self,
    ) -> Callable[
        [apihub_service.ListVersionsRequest], apihub_service.ListVersionsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListVersions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def search_resources(
        self,
    ) -> Callable[
        [apihub_service.SearchResourcesRequest], apihub_service.SearchResourcesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SearchResources(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_api(
        self,
    ) -> Callable[[apihub_service.UpdateApiRequest], common_fields.Api]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateApi(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_api_operation(
        self,
    ) -> Callable[
        [apihub_service.UpdateApiOperationRequest], common_fields.ApiOperation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateApiOperation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_attribute(
        self,
    ) -> Callable[[apihub_service.UpdateAttributeRequest], common_fields.Attribute]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateAttribute(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_deployment(
        self,
    ) -> Callable[[apihub_service.UpdateDeploymentRequest], common_fields.Deployment]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateDeployment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_external_api(
        self,
    ) -> Callable[[apihub_service.UpdateExternalApiRequest], common_fields.ExternalApi]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateExternalApi(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_spec(
        self,
    ) -> Callable[[apihub_service.UpdateSpecRequest], common_fields.Spec]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateSpec(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_version(
        self,
    ) -> Callable[[apihub_service.UpdateVersionRequest], common_fields.Version]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateVersion(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(_BaseApiHubRestTransport._BaseGetLocation, ApiHubRestStub):
        def __hash__(self):
            return hash("ApiHubRestTransport.GetLocation")

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

            http_options = _BaseApiHubRestTransport._BaseGetLocation._get_http_options()
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.apihub_v1.ApiHubAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "GetLocation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_locations(self):
        return self._ListLocations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListLocations(_BaseApiHubRestTransport._BaseListLocations, ApiHubRestStub):
        def __hash__(self):
            return hash("ApiHubRestTransport.ListLocations")

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
                _BaseApiHubRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.apihub_v1.ApiHubAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
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
        _BaseApiHubRestTransport._BaseCancelOperation, ApiHubRestStub
    ):
        def __hash__(self):
            return hash("ApiHubRestTransport.CancelOperation")

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
                _BaseApiHubRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._CancelOperation._get_response(
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
        _BaseApiHubRestTransport._BaseDeleteOperation, ApiHubRestStub
    ):
        def __hash__(self):
            return hash("ApiHubRestTransport.DeleteOperation")

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
                _BaseApiHubRestTransport._BaseDeleteOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._DeleteOperation._get_response(
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

    class _GetOperation(_BaseApiHubRestTransport._BaseGetOperation, ApiHubRestStub):
        def __hash__(self):
            return hash("ApiHubRestTransport.GetOperation")

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
                _BaseApiHubRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.apihub_v1.ApiHubAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "GetOperation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_operations(self):
        return self._ListOperations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListOperations(_BaseApiHubRestTransport._BaseListOperations, ApiHubRestStub):
        def __hash__(self):
            return hash("ApiHubRestTransport.ListOperations")

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
                _BaseApiHubRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiHubRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.apihub_v1.ApiHubClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiHubRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.apihub_v1.ApiHubAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.ApiHub",
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


__all__ = ("ApiHubRestTransport",)
