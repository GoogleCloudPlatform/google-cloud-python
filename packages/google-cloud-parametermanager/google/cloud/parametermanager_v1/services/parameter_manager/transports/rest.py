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
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.parametermanager_v1._compat import transcode_request
from google.cloud.parametermanager_v1.types import service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseParameterManagerRestTransport

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


class ParameterManagerRestInterceptor:
    """Interceptor for ParameterManager.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the ParameterManagerRestTransport.

    .. code-block:: python
        class MyCustomParameterManagerInterceptor(ParameterManagerRestInterceptor):
            def pre_create_parameter(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_parameter(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_parameter_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_parameter_version(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_template(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_template_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_template_version(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_parameter(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_parameter_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_template_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_parameter(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_parameter(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_parameter_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_parameter_version(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_template(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_template_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_template_version(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_parameters(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_parameters(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_parameter_versions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_parameter_versions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_templates(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_templates(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_template_versions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_template_versions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_render_parameter_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_render_parameter_version(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_render_template_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_render_template_version(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_parameter(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_parameter(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_parameter_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_parameter_version(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_template(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_template_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_template_version(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = ParameterManagerRestTransport(interceptor=MyCustomParameterManagerInterceptor())
        client = ParameterManagerClient(transport=transport)


    """

    def pre_create_parameter(
        self,
        request: service.CreateParameterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.CreateParameterRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_parameter

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ParameterManager server.
        """
        return request, metadata

    def post_create_parameter(self, response: service.Parameter) -> service.Parameter:
        """Post-rpc interceptor for create_parameter

        DEPRECATED. Please use the `post_create_parameter_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ParameterManager server but before
        it is returned to user code. This `post_create_parameter` interceptor runs
        before the `post_create_parameter_with_metadata` interceptor.
        """
        return response

    def post_create_parameter_with_metadata(
        self,
        response: service.Parameter,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.Parameter, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_parameter

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ParameterManager server but before it is returned to user code.

        We recommend only using this `post_create_parameter_with_metadata`
        interceptor in new development instead of the `post_create_parameter` interceptor.
        When both interceptors are used, this `post_create_parameter_with_metadata` interceptor runs after the
        `post_create_parameter` interceptor. The (possibly modified) response returned by
        `post_create_parameter` will be passed to
        `post_create_parameter_with_metadata`.
        """
        return response, metadata

    def pre_create_parameter_version(
        self,
        request: service.CreateParameterVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.CreateParameterVersionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_parameter_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ParameterManager server.
        """
        return request, metadata

    def post_create_parameter_version(
        self, response: service.ParameterVersion
    ) -> service.ParameterVersion:
        """Post-rpc interceptor for create_parameter_version

        DEPRECATED. Please use the `post_create_parameter_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ParameterManager server but before
        it is returned to user code. This `post_create_parameter_version` interceptor runs
        before the `post_create_parameter_version_with_metadata` interceptor.
        """
        return response

    def post_create_parameter_version_with_metadata(
        self,
        response: service.ParameterVersion,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ParameterVersion, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_parameter_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ParameterManager server but before it is returned to user code.

        We recommend only using this `post_create_parameter_version_with_metadata`
        interceptor in new development instead of the `post_create_parameter_version` interceptor.
        When both interceptors are used, this `post_create_parameter_version_with_metadata` interceptor runs after the
        `post_create_parameter_version` interceptor. The (possibly modified) response returned by
        `post_create_parameter_version` will be passed to
        `post_create_parameter_version_with_metadata`.
        """
        return response, metadata

    def pre_create_template(
        self,
        request: service.CreateTemplateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.CreateTemplateRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ParameterManager server.
        """
        return request, metadata

    def post_create_template(self, response: service.Template) -> service.Template:
        """Post-rpc interceptor for create_template

        DEPRECATED. Please use the `post_create_template_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ParameterManager server but before
        it is returned to user code. This `post_create_template` interceptor runs
        before the `post_create_template_with_metadata` interceptor.
        """
        return response

    def post_create_template_with_metadata(
        self,
        response: service.Template,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.Template, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_template

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ParameterManager server but before it is returned to user code.

        We recommend only using this `post_create_template_with_metadata`
        interceptor in new development instead of the `post_create_template` interceptor.
        When both interceptors are used, this `post_create_template_with_metadata` interceptor runs after the
        `post_create_template` interceptor. The (possibly modified) response returned by
        `post_create_template` will be passed to
        `post_create_template_with_metadata`.
        """
        return response, metadata

    def pre_create_template_version(
        self,
        request: service.CreateTemplateVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.CreateTemplateVersionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_template_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ParameterManager server.
        """
        return request, metadata

    def post_create_template_version(
        self, response: service.TemplateVersion
    ) -> service.TemplateVersion:
        """Post-rpc interceptor for create_template_version

        DEPRECATED. Please use the `post_create_template_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ParameterManager server but before
        it is returned to user code. This `post_create_template_version` interceptor runs
        before the `post_create_template_version_with_metadata` interceptor.
        """
        return response

    def post_create_template_version_with_metadata(
        self,
        response: service.TemplateVersion,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.TemplateVersion, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_template_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ParameterManager server but before it is returned to user code.

        We recommend only using this `post_create_template_version_with_metadata`
        interceptor in new development instead of the `post_create_template_version` interceptor.
        When both interceptors are used, this `post_create_template_version_with_metadata` interceptor runs after the
        `post_create_template_version` interceptor. The (possibly modified) response returned by
        `post_create_template_version` will be passed to
        `post_create_template_version_with_metadata`.
        """
        return response, metadata

    def pre_delete_parameter(
        self,
        request: service.DeleteParameterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.DeleteParameterRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_parameter

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ParameterManager server.
        """
        return request, metadata

    def pre_delete_parameter_version(
        self,
        request: service.DeleteParameterVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.DeleteParameterVersionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_parameter_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ParameterManager server.
        """
        return request, metadata

    def pre_delete_template(
        self,
        request: service.DeleteTemplateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.DeleteTemplateRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ParameterManager server.
        """
        return request, metadata

    def pre_delete_template_version(
        self,
        request: service.DeleteTemplateVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.DeleteTemplateVersionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_template_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ParameterManager server.
        """
        return request, metadata

    def pre_get_parameter(
        self,
        request: service.GetParameterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.GetParameterRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_parameter

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ParameterManager server.
        """
        return request, metadata

    def post_get_parameter(self, response: service.Parameter) -> service.Parameter:
        """Post-rpc interceptor for get_parameter

        DEPRECATED. Please use the `post_get_parameter_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ParameterManager server but before
        it is returned to user code. This `post_get_parameter` interceptor runs
        before the `post_get_parameter_with_metadata` interceptor.
        """
        return response

    def post_get_parameter_with_metadata(
        self,
        response: service.Parameter,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.Parameter, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_parameter

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ParameterManager server but before it is returned to user code.

        We recommend only using this `post_get_parameter_with_metadata`
        interceptor in new development instead of the `post_get_parameter` interceptor.
        When both interceptors are used, this `post_get_parameter_with_metadata` interceptor runs after the
        `post_get_parameter` interceptor. The (possibly modified) response returned by
        `post_get_parameter` will be passed to
        `post_get_parameter_with_metadata`.
        """
        return response, metadata

    def pre_get_parameter_version(
        self,
        request: service.GetParameterVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.GetParameterVersionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_parameter_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ParameterManager server.
        """
        return request, metadata

    def post_get_parameter_version(
        self, response: service.ParameterVersion
    ) -> service.ParameterVersion:
        """Post-rpc interceptor for get_parameter_version

        DEPRECATED. Please use the `post_get_parameter_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ParameterManager server but before
        it is returned to user code. This `post_get_parameter_version` interceptor runs
        before the `post_get_parameter_version_with_metadata` interceptor.
        """
        return response

    def post_get_parameter_version_with_metadata(
        self,
        response: service.ParameterVersion,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ParameterVersion, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_parameter_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ParameterManager server but before it is returned to user code.

        We recommend only using this `post_get_parameter_version_with_metadata`
        interceptor in new development instead of the `post_get_parameter_version` interceptor.
        When both interceptors are used, this `post_get_parameter_version_with_metadata` interceptor runs after the
        `post_get_parameter_version` interceptor. The (possibly modified) response returned by
        `post_get_parameter_version` will be passed to
        `post_get_parameter_version_with_metadata`.
        """
        return response, metadata

    def pre_get_template(
        self,
        request: service.GetTemplateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.GetTemplateRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ParameterManager server.
        """
        return request, metadata

    def post_get_template(self, response: service.Template) -> service.Template:
        """Post-rpc interceptor for get_template

        DEPRECATED. Please use the `post_get_template_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ParameterManager server but before
        it is returned to user code. This `post_get_template` interceptor runs
        before the `post_get_template_with_metadata` interceptor.
        """
        return response

    def post_get_template_with_metadata(
        self,
        response: service.Template,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.Template, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_template

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ParameterManager server but before it is returned to user code.

        We recommend only using this `post_get_template_with_metadata`
        interceptor in new development instead of the `post_get_template` interceptor.
        When both interceptors are used, this `post_get_template_with_metadata` interceptor runs after the
        `post_get_template` interceptor. The (possibly modified) response returned by
        `post_get_template` will be passed to
        `post_get_template_with_metadata`.
        """
        return response, metadata

    def pre_get_template_version(
        self,
        request: service.GetTemplateVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.GetTemplateVersionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_template_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ParameterManager server.
        """
        return request, metadata

    def post_get_template_version(
        self, response: service.TemplateVersion
    ) -> service.TemplateVersion:
        """Post-rpc interceptor for get_template_version

        DEPRECATED. Please use the `post_get_template_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ParameterManager server but before
        it is returned to user code. This `post_get_template_version` interceptor runs
        before the `post_get_template_version_with_metadata` interceptor.
        """
        return response

    def post_get_template_version_with_metadata(
        self,
        response: service.TemplateVersion,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.TemplateVersion, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_template_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ParameterManager server but before it is returned to user code.

        We recommend only using this `post_get_template_version_with_metadata`
        interceptor in new development instead of the `post_get_template_version` interceptor.
        When both interceptors are used, this `post_get_template_version_with_metadata` interceptor runs after the
        `post_get_template_version` interceptor. The (possibly modified) response returned by
        `post_get_template_version` will be passed to
        `post_get_template_version_with_metadata`.
        """
        return response, metadata

    def pre_list_parameters(
        self,
        request: service.ListParametersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListParametersRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_parameters

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ParameterManager server.
        """
        return request, metadata

    def post_list_parameters(
        self, response: service.ListParametersResponse
    ) -> service.ListParametersResponse:
        """Post-rpc interceptor for list_parameters

        DEPRECATED. Please use the `post_list_parameters_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ParameterManager server but before
        it is returned to user code. This `post_list_parameters` interceptor runs
        before the `post_list_parameters_with_metadata` interceptor.
        """
        return response

    def post_list_parameters_with_metadata(
        self,
        response: service.ListParametersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListParametersResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_parameters

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ParameterManager server but before it is returned to user code.

        We recommend only using this `post_list_parameters_with_metadata`
        interceptor in new development instead of the `post_list_parameters` interceptor.
        When both interceptors are used, this `post_list_parameters_with_metadata` interceptor runs after the
        `post_list_parameters` interceptor. The (possibly modified) response returned by
        `post_list_parameters` will be passed to
        `post_list_parameters_with_metadata`.
        """
        return response, metadata

    def pre_list_parameter_versions(
        self,
        request: service.ListParameterVersionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ListParameterVersionsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_parameter_versions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ParameterManager server.
        """
        return request, metadata

    def post_list_parameter_versions(
        self, response: service.ListParameterVersionsResponse
    ) -> service.ListParameterVersionsResponse:
        """Post-rpc interceptor for list_parameter_versions

        DEPRECATED. Please use the `post_list_parameter_versions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ParameterManager server but before
        it is returned to user code. This `post_list_parameter_versions` interceptor runs
        before the `post_list_parameter_versions_with_metadata` interceptor.
        """
        return response

    def post_list_parameter_versions_with_metadata(
        self,
        response: service.ListParameterVersionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ListParameterVersionsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_parameter_versions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ParameterManager server but before it is returned to user code.

        We recommend only using this `post_list_parameter_versions_with_metadata`
        interceptor in new development instead of the `post_list_parameter_versions` interceptor.
        When both interceptors are used, this `post_list_parameter_versions_with_metadata` interceptor runs after the
        `post_list_parameter_versions` interceptor. The (possibly modified) response returned by
        `post_list_parameter_versions` will be passed to
        `post_list_parameter_versions_with_metadata`.
        """
        return response, metadata

    def pre_list_templates(
        self,
        request: service.ListTemplatesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListTemplatesRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_templates

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ParameterManager server.
        """
        return request, metadata

    def post_list_templates(
        self, response: service.ListTemplatesResponse
    ) -> service.ListTemplatesResponse:
        """Post-rpc interceptor for list_templates

        DEPRECATED. Please use the `post_list_templates_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ParameterManager server but before
        it is returned to user code. This `post_list_templates` interceptor runs
        before the `post_list_templates_with_metadata` interceptor.
        """
        return response

    def post_list_templates_with_metadata(
        self,
        response: service.ListTemplatesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListTemplatesResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_templates

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ParameterManager server but before it is returned to user code.

        We recommend only using this `post_list_templates_with_metadata`
        interceptor in new development instead of the `post_list_templates` interceptor.
        When both interceptors are used, this `post_list_templates_with_metadata` interceptor runs after the
        `post_list_templates` interceptor. The (possibly modified) response returned by
        `post_list_templates` will be passed to
        `post_list_templates_with_metadata`.
        """
        return response, metadata

    def pre_list_template_versions(
        self,
        request: service.ListTemplateVersionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ListTemplateVersionsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_template_versions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ParameterManager server.
        """
        return request, metadata

    def post_list_template_versions(
        self, response: service.ListTemplateVersionsResponse
    ) -> service.ListTemplateVersionsResponse:
        """Post-rpc interceptor for list_template_versions

        DEPRECATED. Please use the `post_list_template_versions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ParameterManager server but before
        it is returned to user code. This `post_list_template_versions` interceptor runs
        before the `post_list_template_versions_with_metadata` interceptor.
        """
        return response

    def post_list_template_versions_with_metadata(
        self,
        response: service.ListTemplateVersionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ListTemplateVersionsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_template_versions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ParameterManager server but before it is returned to user code.

        We recommend only using this `post_list_template_versions_with_metadata`
        interceptor in new development instead of the `post_list_template_versions` interceptor.
        When both interceptors are used, this `post_list_template_versions_with_metadata` interceptor runs after the
        `post_list_template_versions` interceptor. The (possibly modified) response returned by
        `post_list_template_versions` will be passed to
        `post_list_template_versions_with_metadata`.
        """
        return response, metadata

    def pre_render_parameter_version(
        self,
        request: service.RenderParameterVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.RenderParameterVersionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for render_parameter_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ParameterManager server.
        """
        return request, metadata

    def post_render_parameter_version(
        self, response: service.RenderParameterVersionResponse
    ) -> service.RenderParameterVersionResponse:
        """Post-rpc interceptor for render_parameter_version

        DEPRECATED. Please use the `post_render_parameter_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ParameterManager server but before
        it is returned to user code. This `post_render_parameter_version` interceptor runs
        before the `post_render_parameter_version_with_metadata` interceptor.
        """
        return response

    def post_render_parameter_version_with_metadata(
        self,
        response: service.RenderParameterVersionResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.RenderParameterVersionResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for render_parameter_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ParameterManager server but before it is returned to user code.

        We recommend only using this `post_render_parameter_version_with_metadata`
        interceptor in new development instead of the `post_render_parameter_version` interceptor.
        When both interceptors are used, this `post_render_parameter_version_with_metadata` interceptor runs after the
        `post_render_parameter_version` interceptor. The (possibly modified) response returned by
        `post_render_parameter_version` will be passed to
        `post_render_parameter_version_with_metadata`.
        """
        return response, metadata

    def pre_render_template_version(
        self,
        request: service.RenderTemplateVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.RenderTemplateVersionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for render_template_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ParameterManager server.
        """
        return request, metadata

    def post_render_template_version(
        self, response: service.RenderTemplateVersionResponse
    ) -> service.RenderTemplateVersionResponse:
        """Post-rpc interceptor for render_template_version

        DEPRECATED. Please use the `post_render_template_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ParameterManager server but before
        it is returned to user code. This `post_render_template_version` interceptor runs
        before the `post_render_template_version_with_metadata` interceptor.
        """
        return response

    def post_render_template_version_with_metadata(
        self,
        response: service.RenderTemplateVersionResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.RenderTemplateVersionResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for render_template_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ParameterManager server but before it is returned to user code.

        We recommend only using this `post_render_template_version_with_metadata`
        interceptor in new development instead of the `post_render_template_version` interceptor.
        When both interceptors are used, this `post_render_template_version_with_metadata` interceptor runs after the
        `post_render_template_version` interceptor. The (possibly modified) response returned by
        `post_render_template_version` will be passed to
        `post_render_template_version_with_metadata`.
        """
        return response, metadata

    def pre_update_parameter(
        self,
        request: service.UpdateParameterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.UpdateParameterRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_parameter

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ParameterManager server.
        """
        return request, metadata

    def post_update_parameter(self, response: service.Parameter) -> service.Parameter:
        """Post-rpc interceptor for update_parameter

        DEPRECATED. Please use the `post_update_parameter_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ParameterManager server but before
        it is returned to user code. This `post_update_parameter` interceptor runs
        before the `post_update_parameter_with_metadata` interceptor.
        """
        return response

    def post_update_parameter_with_metadata(
        self,
        response: service.Parameter,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.Parameter, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_parameter

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ParameterManager server but before it is returned to user code.

        We recommend only using this `post_update_parameter_with_metadata`
        interceptor in new development instead of the `post_update_parameter` interceptor.
        When both interceptors are used, this `post_update_parameter_with_metadata` interceptor runs after the
        `post_update_parameter` interceptor. The (possibly modified) response returned by
        `post_update_parameter` will be passed to
        `post_update_parameter_with_metadata`.
        """
        return response, metadata

    def pre_update_parameter_version(
        self,
        request: service.UpdateParameterVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.UpdateParameterVersionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_parameter_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ParameterManager server.
        """
        return request, metadata

    def post_update_parameter_version(
        self, response: service.ParameterVersion
    ) -> service.ParameterVersion:
        """Post-rpc interceptor for update_parameter_version

        DEPRECATED. Please use the `post_update_parameter_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ParameterManager server but before
        it is returned to user code. This `post_update_parameter_version` interceptor runs
        before the `post_update_parameter_version_with_metadata` interceptor.
        """
        return response

    def post_update_parameter_version_with_metadata(
        self,
        response: service.ParameterVersion,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ParameterVersion, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_parameter_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ParameterManager server but before it is returned to user code.

        We recommend only using this `post_update_parameter_version_with_metadata`
        interceptor in new development instead of the `post_update_parameter_version` interceptor.
        When both interceptors are used, this `post_update_parameter_version_with_metadata` interceptor runs after the
        `post_update_parameter_version` interceptor. The (possibly modified) response returned by
        `post_update_parameter_version` will be passed to
        `post_update_parameter_version_with_metadata`.
        """
        return response, metadata

    def pre_update_template(
        self,
        request: service.UpdateTemplateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.UpdateTemplateRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ParameterManager server.
        """
        return request, metadata

    def post_update_template(self, response: service.Template) -> service.Template:
        """Post-rpc interceptor for update_template

        DEPRECATED. Please use the `post_update_template_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ParameterManager server but before
        it is returned to user code. This `post_update_template` interceptor runs
        before the `post_update_template_with_metadata` interceptor.
        """
        return response

    def post_update_template_with_metadata(
        self,
        response: service.Template,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.Template, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_template

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ParameterManager server but before it is returned to user code.

        We recommend only using this `post_update_template_with_metadata`
        interceptor in new development instead of the `post_update_template` interceptor.
        When both interceptors are used, this `post_update_template_with_metadata` interceptor runs after the
        `post_update_template` interceptor. The (possibly modified) response returned by
        `post_update_template` will be passed to
        `post_update_template_with_metadata`.
        """
        return response, metadata

    def pre_update_template_version(
        self,
        request: service.UpdateTemplateVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.UpdateTemplateVersionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_template_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ParameterManager server.
        """
        return request, metadata

    def post_update_template_version(
        self, response: service.TemplateVersion
    ) -> service.TemplateVersion:
        """Post-rpc interceptor for update_template_version

        DEPRECATED. Please use the `post_update_template_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ParameterManager server but before
        it is returned to user code. This `post_update_template_version` interceptor runs
        before the `post_update_template_version_with_metadata` interceptor.
        """
        return response

    def post_update_template_version_with_metadata(
        self,
        response: service.TemplateVersion,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.TemplateVersion, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_template_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ParameterManager server but before it is returned to user code.

        We recommend only using this `post_update_template_version_with_metadata`
        interceptor in new development instead of the `post_update_template_version` interceptor.
        When both interceptors are used, this `post_update_template_version_with_metadata` interceptor runs after the
        `post_update_template_version` interceptor. The (possibly modified) response returned by
        `post_update_template_version` will be passed to
        `post_update_template_version_with_metadata`.
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
        before they are sent to the ParameterManager server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the ParameterManager server but before
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
        before they are sent to the ParameterManager server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the ParameterManager server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class ParameterManagerRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: ParameterManagerRestInterceptor


class ParameterManagerRestTransport(_BaseParameterManagerRestTransport):
    """REST backend synchronous transport for ParameterManager.

    Service describing handlers for resources

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "parametermanager.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[ParameterManagerRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'parametermanager.googleapis.com').
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
            interceptor (Optional[ParameterManagerRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or ParameterManagerRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CreateParameter(
        _BaseParameterManagerRestTransport._BaseCreateParameter,
        ParameterManagerRestStub,
    ):
        def __hash__(self):
            return hash("ParameterManagerRestTransport.CreateParameter")

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
            request: service.CreateParameterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.Parameter:
            r"""Call the create parameter method over HTTP.

            Args:
                request (~.service.CreateParameterRequest):
                    The request object. Message for creating a Parameter
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.Parameter:
                    Message describing Parameter resource
            """

            http_options = _BaseParameterManagerRestTransport._BaseCreateParameter._get_http_options()
            request, metadata = self._interceptor.pre_create_parameter(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseParameterManagerRestTransport._BaseCreateParameter,
                    "_BaseCreateParameter__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.parametermanager_v1.ParameterManagerClient.CreateParameter",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "CreateParameter",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ParameterManagerRestTransport._CreateParameter._get_response(
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
            resp = service.Parameter()
            pb_resp = service.Parameter.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_parameter(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_parameter_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.Parameter.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.parametermanager_v1.ParameterManagerClient.create_parameter",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "CreateParameter",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateParameterVersion(
        _BaseParameterManagerRestTransport._BaseCreateParameterVersion,
        ParameterManagerRestStub,
    ):
        def __hash__(self):
            return hash("ParameterManagerRestTransport.CreateParameterVersion")

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
            request: service.CreateParameterVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ParameterVersion:
            r"""Call the create parameter version method over HTTP.

            Args:
                request (~.service.CreateParameterVersionRequest):
                    The request object. Message for creating a
                ParameterVersion
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ParameterVersion:
                    Message describing ParameterVersion
                resource

            """

            http_options = _BaseParameterManagerRestTransport._BaseCreateParameterVersion._get_http_options()
            request, metadata = self._interceptor.pre_create_parameter_version(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseParameterManagerRestTransport._BaseCreateParameterVersion,
                    "_BaseCreateParameterVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.parametermanager_v1.ParameterManagerClient.CreateParameterVersion",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "CreateParameterVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ParameterManagerRestTransport._CreateParameterVersion._get_response(
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
            resp = service.ParameterVersion()
            pb_resp = service.ParameterVersion.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_parameter_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_parameter_version_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ParameterVersion.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.parametermanager_v1.ParameterManagerClient.create_parameter_version",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "CreateParameterVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateTemplate(
        _BaseParameterManagerRestTransport._BaseCreateTemplate, ParameterManagerRestStub
    ):
        def __hash__(self):
            return hash("ParameterManagerRestTransport.CreateTemplate")

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
            request: service.CreateTemplateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.Template:
            r"""Call the create template method over HTTP.

            Args:
                request (~.service.CreateTemplateRequest):
                    The request object. Message for creating a Template
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.Template:
                    Message describing Template resource
            """

            http_options = _BaseParameterManagerRestTransport._BaseCreateTemplate._get_http_options()
            request, metadata = self._interceptor.pre_create_template(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseParameterManagerRestTransport._BaseCreateTemplate,
                    "_BaseCreateTemplate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.parametermanager_v1.ParameterManagerClient.CreateTemplate",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "CreateTemplate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ParameterManagerRestTransport._CreateTemplate._get_response(
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
            resp = service.Template()
            pb_resp = service.Template.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_template(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_template_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.Template.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.parametermanager_v1.ParameterManagerClient.create_template",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "CreateTemplate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateTemplateVersion(
        _BaseParameterManagerRestTransport._BaseCreateTemplateVersion,
        ParameterManagerRestStub,
    ):
        def __hash__(self):
            return hash("ParameterManagerRestTransport.CreateTemplateVersion")

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
            request: service.CreateTemplateVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.TemplateVersion:
            r"""Call the create template version method over HTTP.

            Args:
                request (~.service.CreateTemplateVersionRequest):
                    The request object. Message for creating a
                TemplateVersion
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.TemplateVersion:
                    Message describing TemplateVersion
                resource

            """

            http_options = _BaseParameterManagerRestTransport._BaseCreateTemplateVersion._get_http_options()
            request, metadata = self._interceptor.pre_create_template_version(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseParameterManagerRestTransport._BaseCreateTemplateVersion,
                    "_BaseCreateTemplateVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.parametermanager_v1.ParameterManagerClient.CreateTemplateVersion",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "CreateTemplateVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ParameterManagerRestTransport._CreateTemplateVersion._get_response(
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
            resp = service.TemplateVersion()
            pb_resp = service.TemplateVersion.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_template_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_template_version_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.TemplateVersion.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.parametermanager_v1.ParameterManagerClient.create_template_version",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "CreateTemplateVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteParameter(
        _BaseParameterManagerRestTransport._BaseDeleteParameter,
        ParameterManagerRestStub,
    ):
        def __hash__(self):
            return hash("ParameterManagerRestTransport.DeleteParameter")

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
            request: service.DeleteParameterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete parameter method over HTTP.

            Args:
                request (~.service.DeleteParameterRequest):
                    The request object. Message for deleting a Parameter
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseParameterManagerRestTransport._BaseDeleteParameter._get_http_options()
            request, metadata = self._interceptor.pre_delete_parameter(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseParameterManagerRestTransport._BaseDeleteParameter,
                    "_BaseDeleteParameter__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.parametermanager_v1.ParameterManagerClient.DeleteParameter",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "DeleteParameter",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ParameterManagerRestTransport._DeleteParameter._get_response(
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

    class _DeleteParameterVersion(
        _BaseParameterManagerRestTransport._BaseDeleteParameterVersion,
        ParameterManagerRestStub,
    ):
        def __hash__(self):
            return hash("ParameterManagerRestTransport.DeleteParameterVersion")

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
            request: service.DeleteParameterVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete parameter version method over HTTP.

            Args:
                request (~.service.DeleteParameterVersionRequest):
                    The request object. Message for deleting a
                ParameterVersion
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseParameterManagerRestTransport._BaseDeleteParameterVersion._get_http_options()
            request, metadata = self._interceptor.pre_delete_parameter_version(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseParameterManagerRestTransport._BaseDeleteParameterVersion,
                    "_BaseDeleteParameterVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.parametermanager_v1.ParameterManagerClient.DeleteParameterVersion",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "DeleteParameterVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ParameterManagerRestTransport._DeleteParameterVersion._get_response(
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

    class _DeleteTemplate(
        _BaseParameterManagerRestTransport._BaseDeleteTemplate, ParameterManagerRestStub
    ):
        def __hash__(self):
            return hash("ParameterManagerRestTransport.DeleteTemplate")

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
            request: service.DeleteTemplateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete template method over HTTP.

            Args:
                request (~.service.DeleteTemplateRequest):
                    The request object. Message for deleting a Template
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseParameterManagerRestTransport._BaseDeleteTemplate._get_http_options()
            request, metadata = self._interceptor.pre_delete_template(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseParameterManagerRestTransport._BaseDeleteTemplate,
                    "_BaseDeleteTemplate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.parametermanager_v1.ParameterManagerClient.DeleteTemplate",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "DeleteTemplate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ParameterManagerRestTransport._DeleteTemplate._get_response(
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

    class _DeleteTemplateVersion(
        _BaseParameterManagerRestTransport._BaseDeleteTemplateVersion,
        ParameterManagerRestStub,
    ):
        def __hash__(self):
            return hash("ParameterManagerRestTransport.DeleteTemplateVersion")

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
            request: service.DeleteTemplateVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete template version method over HTTP.

            Args:
                request (~.service.DeleteTemplateVersionRequest):
                    The request object. Message for deleting a
                TemplateVersion
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseParameterManagerRestTransport._BaseDeleteTemplateVersion._get_http_options()
            request, metadata = self._interceptor.pre_delete_template_version(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseParameterManagerRestTransport._BaseDeleteTemplateVersion,
                    "_BaseDeleteTemplateVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.parametermanager_v1.ParameterManagerClient.DeleteTemplateVersion",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "DeleteTemplateVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ParameterManagerRestTransport._DeleteTemplateVersion._get_response(
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

    class _GetParameter(
        _BaseParameterManagerRestTransport._BaseGetParameter, ParameterManagerRestStub
    ):
        def __hash__(self):
            return hash("ParameterManagerRestTransport.GetParameter")

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
            request: service.GetParameterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.Parameter:
            r"""Call the get parameter method over HTTP.

            Args:
                request (~.service.GetParameterRequest):
                    The request object. Message for getting a Parameter
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.Parameter:
                    Message describing Parameter resource
            """

            http_options = (
                _BaseParameterManagerRestTransport._BaseGetParameter._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_parameter(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseParameterManagerRestTransport._BaseGetParameter,
                    "_BaseGetParameter__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.parametermanager_v1.ParameterManagerClient.GetParameter",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "GetParameter",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ParameterManagerRestTransport._GetParameter._get_response(
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
            resp = service.Parameter()
            pb_resp = service.Parameter.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_parameter(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_parameter_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.Parameter.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.parametermanager_v1.ParameterManagerClient.get_parameter",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "GetParameter",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetParameterVersion(
        _BaseParameterManagerRestTransport._BaseGetParameterVersion,
        ParameterManagerRestStub,
    ):
        def __hash__(self):
            return hash("ParameterManagerRestTransport.GetParameterVersion")

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
            request: service.GetParameterVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ParameterVersion:
            r"""Call the get parameter version method over HTTP.

            Args:
                request (~.service.GetParameterVersionRequest):
                    The request object. Message for getting a
                ParameterVersion
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ParameterVersion:
                    Message describing ParameterVersion
                resource

            """

            http_options = _BaseParameterManagerRestTransport._BaseGetParameterVersion._get_http_options()
            request, metadata = self._interceptor.pre_get_parameter_version(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseParameterManagerRestTransport._BaseGetParameterVersion,
                    "_BaseGetParameterVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.parametermanager_v1.ParameterManagerClient.GetParameterVersion",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "GetParameterVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ParameterManagerRestTransport._GetParameterVersion._get_response(
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
            resp = service.ParameterVersion()
            pb_resp = service.ParameterVersion.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_parameter_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_parameter_version_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ParameterVersion.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.parametermanager_v1.ParameterManagerClient.get_parameter_version",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "GetParameterVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetTemplate(
        _BaseParameterManagerRestTransport._BaseGetTemplate, ParameterManagerRestStub
    ):
        def __hash__(self):
            return hash("ParameterManagerRestTransport.GetTemplate")

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
            request: service.GetTemplateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.Template:
            r"""Call the get template method over HTTP.

            Args:
                request (~.service.GetTemplateRequest):
                    The request object. Message for getting a Template
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.Template:
                    Message describing Template resource
            """

            http_options = (
                _BaseParameterManagerRestTransport._BaseGetTemplate._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_template(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseParameterManagerRestTransport._BaseGetTemplate,
                    "_BaseGetTemplate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.parametermanager_v1.ParameterManagerClient.GetTemplate",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "GetTemplate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ParameterManagerRestTransport._GetTemplate._get_response(
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
            resp = service.Template()
            pb_resp = service.Template.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_template(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_template_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.Template.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.parametermanager_v1.ParameterManagerClient.get_template",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "GetTemplate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetTemplateVersion(
        _BaseParameterManagerRestTransport._BaseGetTemplateVersion,
        ParameterManagerRestStub,
    ):
        def __hash__(self):
            return hash("ParameterManagerRestTransport.GetTemplateVersion")

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
            request: service.GetTemplateVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.TemplateVersion:
            r"""Call the get template version method over HTTP.

            Args:
                request (~.service.GetTemplateVersionRequest):
                    The request object. Message for getting a TemplateVersion
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.TemplateVersion:
                    Message describing TemplateVersion
                resource

            """

            http_options = _BaseParameterManagerRestTransport._BaseGetTemplateVersion._get_http_options()
            request, metadata = self._interceptor.pre_get_template_version(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseParameterManagerRestTransport._BaseGetTemplateVersion,
                    "_BaseGetTemplateVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.parametermanager_v1.ParameterManagerClient.GetTemplateVersion",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "GetTemplateVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ParameterManagerRestTransport._GetTemplateVersion._get_response(
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
            resp = service.TemplateVersion()
            pb_resp = service.TemplateVersion.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_template_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_template_version_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.TemplateVersion.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.parametermanager_v1.ParameterManagerClient.get_template_version",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "GetTemplateVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListParameters(
        _BaseParameterManagerRestTransport._BaseListParameters, ParameterManagerRestStub
    ):
        def __hash__(self):
            return hash("ParameterManagerRestTransport.ListParameters")

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
            request: service.ListParametersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListParametersResponse:
            r"""Call the list parameters method over HTTP.

            Args:
                request (~.service.ListParametersRequest):
                    The request object. Message for requesting list of
                Parameters
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListParametersResponse:
                    Message for response to listing
                Parameters

            """

            http_options = _BaseParameterManagerRestTransport._BaseListParameters._get_http_options()
            request, metadata = self._interceptor.pre_list_parameters(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseParameterManagerRestTransport._BaseListParameters,
                    "_BaseListParameters__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.parametermanager_v1.ParameterManagerClient.ListParameters",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "ListParameters",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ParameterManagerRestTransport._ListParameters._get_response(
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
            resp = service.ListParametersResponse()
            pb_resp = service.ListParametersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_parameters(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_parameters_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListParametersResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.parametermanager_v1.ParameterManagerClient.list_parameters",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "ListParameters",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListParameterVersions(
        _BaseParameterManagerRestTransport._BaseListParameterVersions,
        ParameterManagerRestStub,
    ):
        def __hash__(self):
            return hash("ParameterManagerRestTransport.ListParameterVersions")

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
            request: service.ListParameterVersionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListParameterVersionsResponse:
            r"""Call the list parameter versions method over HTTP.

            Args:
                request (~.service.ListParameterVersionsRequest):
                    The request object. Message for requesting list of
                ParameterVersions
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListParameterVersionsResponse:
                    Message for response to listing
                ParameterVersions

            """

            http_options = _BaseParameterManagerRestTransport._BaseListParameterVersions._get_http_options()
            request, metadata = self._interceptor.pre_list_parameter_versions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseParameterManagerRestTransport._BaseListParameterVersions,
                    "_BaseListParameterVersions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.parametermanager_v1.ParameterManagerClient.ListParameterVersions",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "ListParameterVersions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ParameterManagerRestTransport._ListParameterVersions._get_response(
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
            resp = service.ListParameterVersionsResponse()
            pb_resp = service.ListParameterVersionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_parameter_versions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_parameter_versions_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListParameterVersionsResponse.to_json(
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
                    "Received response for google.cloud.parametermanager_v1.ParameterManagerClient.list_parameter_versions",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "ListParameterVersions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListTemplates(
        _BaseParameterManagerRestTransport._BaseListTemplates, ParameterManagerRestStub
    ):
        def __hash__(self):
            return hash("ParameterManagerRestTransport.ListTemplates")

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
            request: service.ListTemplatesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListTemplatesResponse:
            r"""Call the list templates method over HTTP.

            Args:
                request (~.service.ListTemplatesRequest):
                    The request object. Message for requesting list of
                Templates
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListTemplatesResponse:
                    Message for response to listing
                Templates

            """

            http_options = _BaseParameterManagerRestTransport._BaseListTemplates._get_http_options()
            request, metadata = self._interceptor.pre_list_templates(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseParameterManagerRestTransport._BaseListTemplates,
                    "_BaseListTemplates__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.parametermanager_v1.ParameterManagerClient.ListTemplates",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "ListTemplates",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ParameterManagerRestTransport._ListTemplates._get_response(
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
            resp = service.ListTemplatesResponse()
            pb_resp = service.ListTemplatesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_templates(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_templates_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListTemplatesResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.parametermanager_v1.ParameterManagerClient.list_templates",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "ListTemplates",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListTemplateVersions(
        _BaseParameterManagerRestTransport._BaseListTemplateVersions,
        ParameterManagerRestStub,
    ):
        def __hash__(self):
            return hash("ParameterManagerRestTransport.ListTemplateVersions")

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
            request: service.ListTemplateVersionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListTemplateVersionsResponse:
            r"""Call the list template versions method over HTTP.

            Args:
                request (~.service.ListTemplateVersionsRequest):
                    The request object. Message for requesting list of
                TemplateVersions
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListTemplateVersionsResponse:
                    Message for response to listing
                TemplateVersions

            """

            http_options = _BaseParameterManagerRestTransport._BaseListTemplateVersions._get_http_options()
            request, metadata = self._interceptor.pre_list_template_versions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseParameterManagerRestTransport._BaseListTemplateVersions,
                    "_BaseListTemplateVersions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.parametermanager_v1.ParameterManagerClient.ListTemplateVersions",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "ListTemplateVersions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ParameterManagerRestTransport._ListTemplateVersions._get_response(
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
            resp = service.ListTemplateVersionsResponse()
            pb_resp = service.ListTemplateVersionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_template_versions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_template_versions_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListTemplateVersionsResponse.to_json(
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
                    "Received response for google.cloud.parametermanager_v1.ParameterManagerClient.list_template_versions",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "ListTemplateVersions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RenderParameterVersion(
        _BaseParameterManagerRestTransport._BaseRenderParameterVersion,
        ParameterManagerRestStub,
    ):
        def __hash__(self):
            return hash("ParameterManagerRestTransport.RenderParameterVersion")

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
            request: service.RenderParameterVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.RenderParameterVersionResponse:
            r"""Call the render parameter version method over HTTP.

            Args:
                request (~.service.RenderParameterVersionRequest):
                    The request object. Message for getting a
                ParameterVersionRender
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.RenderParameterVersionResponse:
                    Message describing
                RenderParameterVersionResponse resource

            """

            http_options = _BaseParameterManagerRestTransport._BaseRenderParameterVersion._get_http_options()
            request, metadata = self._interceptor.pre_render_parameter_version(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseParameterManagerRestTransport._BaseRenderParameterVersion,
                    "_BaseRenderParameterVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.parametermanager_v1.ParameterManagerClient.RenderParameterVersion",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "RenderParameterVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ParameterManagerRestTransport._RenderParameterVersion._get_response(
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
            resp = service.RenderParameterVersionResponse()
            pb_resp = service.RenderParameterVersionResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_render_parameter_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_render_parameter_version_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.RenderParameterVersionResponse.to_json(
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
                    "Received response for google.cloud.parametermanager_v1.ParameterManagerClient.render_parameter_version",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "RenderParameterVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RenderTemplateVersion(
        _BaseParameterManagerRestTransport._BaseRenderTemplateVersion,
        ParameterManagerRestStub,
    ):
        def __hash__(self):
            return hash("ParameterManagerRestTransport.RenderTemplateVersion")

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
            request: service.RenderTemplateVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.RenderTemplateVersionResponse:
            r"""Call the render template version method over HTTP.

            Args:
                request (~.service.RenderTemplateVersionRequest):
                    The request object. Message describing
                RenderTemplateVersionRequest resource
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.RenderTemplateVersionResponse:
                    Message describing
                RenderTemplateVersionResponse resource

            """

            http_options = _BaseParameterManagerRestTransport._BaseRenderTemplateVersion._get_http_options()
            request, metadata = self._interceptor.pre_render_template_version(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseParameterManagerRestTransport._BaseRenderTemplateVersion,
                    "_BaseRenderTemplateVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.parametermanager_v1.ParameterManagerClient.RenderTemplateVersion",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "RenderTemplateVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ParameterManagerRestTransport._RenderTemplateVersion._get_response(
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
            resp = service.RenderTemplateVersionResponse()
            pb_resp = service.RenderTemplateVersionResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_render_template_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_render_template_version_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.RenderTemplateVersionResponse.to_json(
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
                    "Received response for google.cloud.parametermanager_v1.ParameterManagerClient.render_template_version",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "RenderTemplateVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateParameter(
        _BaseParameterManagerRestTransport._BaseUpdateParameter,
        ParameterManagerRestStub,
    ):
        def __hash__(self):
            return hash("ParameterManagerRestTransport.UpdateParameter")

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
            request: service.UpdateParameterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.Parameter:
            r"""Call the update parameter method over HTTP.

            Args:
                request (~.service.UpdateParameterRequest):
                    The request object. Message for updating a Parameter
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.Parameter:
                    Message describing Parameter resource
            """

            http_options = _BaseParameterManagerRestTransport._BaseUpdateParameter._get_http_options()
            request, metadata = self._interceptor.pre_update_parameter(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseParameterManagerRestTransport._BaseUpdateParameter,
                    "_BaseUpdateParameter__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.parametermanager_v1.ParameterManagerClient.UpdateParameter",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "UpdateParameter",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ParameterManagerRestTransport._UpdateParameter._get_response(
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
            resp = service.Parameter()
            pb_resp = service.Parameter.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_parameter(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_parameter_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.Parameter.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.parametermanager_v1.ParameterManagerClient.update_parameter",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "UpdateParameter",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateParameterVersion(
        _BaseParameterManagerRestTransport._BaseUpdateParameterVersion,
        ParameterManagerRestStub,
    ):
        def __hash__(self):
            return hash("ParameterManagerRestTransport.UpdateParameterVersion")

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
            request: service.UpdateParameterVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ParameterVersion:
            r"""Call the update parameter version method over HTTP.

            Args:
                request (~.service.UpdateParameterVersionRequest):
                    The request object. Message for updating a
                ParameterVersion
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ParameterVersion:
                    Message describing ParameterVersion
                resource

            """

            http_options = _BaseParameterManagerRestTransport._BaseUpdateParameterVersion._get_http_options()
            request, metadata = self._interceptor.pre_update_parameter_version(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseParameterManagerRestTransport._BaseUpdateParameterVersion,
                    "_BaseUpdateParameterVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.parametermanager_v1.ParameterManagerClient.UpdateParameterVersion",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "UpdateParameterVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ParameterManagerRestTransport._UpdateParameterVersion._get_response(
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
            resp = service.ParameterVersion()
            pb_resp = service.ParameterVersion.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_parameter_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_parameter_version_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ParameterVersion.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.parametermanager_v1.ParameterManagerClient.update_parameter_version",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "UpdateParameterVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateTemplate(
        _BaseParameterManagerRestTransport._BaseUpdateTemplate, ParameterManagerRestStub
    ):
        def __hash__(self):
            return hash("ParameterManagerRestTransport.UpdateTemplate")

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
            request: service.UpdateTemplateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.Template:
            r"""Call the update template method over HTTP.

            Args:
                request (~.service.UpdateTemplateRequest):
                    The request object. Message for updating a Template
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.Template:
                    Message describing Template resource
            """

            http_options = _BaseParameterManagerRestTransport._BaseUpdateTemplate._get_http_options()
            request, metadata = self._interceptor.pre_update_template(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseParameterManagerRestTransport._BaseUpdateTemplate,
                    "_BaseUpdateTemplate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.parametermanager_v1.ParameterManagerClient.UpdateTemplate",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "UpdateTemplate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ParameterManagerRestTransport._UpdateTemplate._get_response(
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
            resp = service.Template()
            pb_resp = service.Template.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_template(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_template_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.Template.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.parametermanager_v1.ParameterManagerClient.update_template",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "UpdateTemplate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateTemplateVersion(
        _BaseParameterManagerRestTransport._BaseUpdateTemplateVersion,
        ParameterManagerRestStub,
    ):
        def __hash__(self):
            return hash("ParameterManagerRestTransport.UpdateTemplateVersion")

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
            request: service.UpdateTemplateVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.TemplateVersion:
            r"""Call the update template version method over HTTP.

            Args:
                request (~.service.UpdateTemplateVersionRequest):
                    The request object. Message for updating a
                TemplateVersion
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.TemplateVersion:
                    Message describing TemplateVersion
                resource

            """

            http_options = _BaseParameterManagerRestTransport._BaseUpdateTemplateVersion._get_http_options()
            request, metadata = self._interceptor.pre_update_template_version(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseParameterManagerRestTransport._BaseUpdateTemplateVersion,
                    "_BaseUpdateTemplateVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.parametermanager_v1.ParameterManagerClient.UpdateTemplateVersion",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "UpdateTemplateVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ParameterManagerRestTransport._UpdateTemplateVersion._get_response(
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
            resp = service.TemplateVersion()
            pb_resp = service.TemplateVersion.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_template_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_template_version_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.TemplateVersion.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.parametermanager_v1.ParameterManagerClient.update_template_version",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "UpdateTemplateVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_parameter(
        self,
    ) -> Callable[[service.CreateParameterRequest], service.Parameter]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateParameter(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_parameter_version(
        self,
    ) -> Callable[[service.CreateParameterVersionRequest], service.ParameterVersion]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateParameterVersion(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_template(
        self,
    ) -> Callable[[service.CreateTemplateRequest], service.Template]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateTemplate(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_template_version(
        self,
    ) -> Callable[[service.CreateTemplateVersionRequest], service.TemplateVersion]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateTemplateVersion(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_parameter(
        self,
    ) -> Callable[[service.DeleteParameterRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteParameter(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_parameter_version(
        self,
    ) -> Callable[[service.DeleteParameterVersionRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteParameterVersion(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_template(
        self,
    ) -> Callable[[service.DeleteTemplateRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteTemplate(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_template_version(
        self,
    ) -> Callable[[service.DeleteTemplateVersionRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteTemplateVersion(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_parameter(
        self,
    ) -> Callable[[service.GetParameterRequest], service.Parameter]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetParameter(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_parameter_version(
        self,
    ) -> Callable[[service.GetParameterVersionRequest], service.ParameterVersion]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetParameterVersion(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_template(self) -> Callable[[service.GetTemplateRequest], service.Template]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetTemplate(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_template_version(
        self,
    ) -> Callable[[service.GetTemplateVersionRequest], service.TemplateVersion]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetTemplateVersion(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_parameters(
        self,
    ) -> Callable[[service.ListParametersRequest], service.ListParametersResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListParameters(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_parameter_versions(
        self,
    ) -> Callable[
        [service.ListParameterVersionsRequest], service.ListParameterVersionsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListParameterVersions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_templates(
        self,
    ) -> Callable[[service.ListTemplatesRequest], service.ListTemplatesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListTemplates(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_template_versions(
        self,
    ) -> Callable[
        [service.ListTemplateVersionsRequest], service.ListTemplateVersionsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListTemplateVersions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def render_parameter_version(
        self,
    ) -> Callable[
        [service.RenderParameterVersionRequest], service.RenderParameterVersionResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RenderParameterVersion(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def render_template_version(
        self,
    ) -> Callable[
        [service.RenderTemplateVersionRequest], service.RenderTemplateVersionResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RenderTemplateVersion(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_parameter(
        self,
    ) -> Callable[[service.UpdateParameterRequest], service.Parameter]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateParameter(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_parameter_version(
        self,
    ) -> Callable[[service.UpdateParameterVersionRequest], service.ParameterVersion]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateParameterVersion(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_template(
        self,
    ) -> Callable[[service.UpdateTemplateRequest], service.Template]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateTemplate(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_template_version(
        self,
    ) -> Callable[[service.UpdateTemplateVersionRequest], service.TemplateVersion]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateTemplateVersion(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseParameterManagerRestTransport._BaseGetLocation, ParameterManagerRestStub
    ):
        def __hash__(self):
            return hash("ParameterManagerRestTransport.GetLocation")

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
                _BaseParameterManagerRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseParameterManagerRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.parametermanager_v1.ParameterManagerClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ParameterManagerRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.parametermanager_v1.ParameterManagerAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
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
        _BaseParameterManagerRestTransport._BaseListLocations, ParameterManagerRestStub
    ):
        def __hash__(self):
            return hash("ParameterManagerRestTransport.ListLocations")

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

            http_options = _BaseParameterManagerRestTransport._BaseListLocations._get_http_options()
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseParameterManagerRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.parametermanager_v1.ParameterManagerClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ParameterManagerRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.parametermanager_v1.ParameterManagerAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.parametermanager.v1.ParameterManager",
                        "rpcName": "ListLocations",
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


__all__ = ("ParameterManagerRestTransport",)
