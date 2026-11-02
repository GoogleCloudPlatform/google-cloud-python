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

from google.ads.admanager_v1._compat import transcode_request
from google.ads.admanager_v1.types import (
    custom_targeting_value_messages,
    custom_targeting_value_service,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseCustomTargetingValueServiceRestTransport

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


class CustomTargetingValueServiceRestInterceptor:
    """Interceptor for CustomTargetingValueService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the CustomTargetingValueServiceRestTransport.

    .. code-block:: python
        class MyCustomCustomTargetingValueServiceInterceptor(CustomTargetingValueServiceRestInterceptor):
            def pre_batch_activate_custom_targeting_values(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_activate_custom_targeting_values(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_create_custom_targeting_values(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_create_custom_targeting_values(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_deactivate_custom_targeting_values(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_deactivate_custom_targeting_values(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_update_custom_targeting_values(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_update_custom_targeting_values(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_custom_targeting_value(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_custom_targeting_value(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_custom_targeting_value(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_custom_targeting_value(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_custom_targeting_values(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_custom_targeting_values(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_custom_targeting_value(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_custom_targeting_value(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = CustomTargetingValueServiceRestTransport(interceptor=MyCustomCustomTargetingValueServiceInterceptor())
        client = CustomTargetingValueServiceClient(transport=transport)


    """

    def pre_batch_activate_custom_targeting_values(
        self,
        request: custom_targeting_value_service.BatchActivateCustomTargetingValuesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_targeting_value_service.BatchActivateCustomTargetingValuesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_activate_custom_targeting_values

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CustomTargetingValueService server.
        """
        return request, metadata

    def post_batch_activate_custom_targeting_values(
        self,
        response: custom_targeting_value_service.BatchActivateCustomTargetingValuesResponse,
    ) -> custom_targeting_value_service.BatchActivateCustomTargetingValuesResponse:
        """Post-rpc interceptor for batch_activate_custom_targeting_values

        DEPRECATED. Please use the `post_batch_activate_custom_targeting_values_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CustomTargetingValueService server but before
        it is returned to user code. This `post_batch_activate_custom_targeting_values` interceptor runs
        before the `post_batch_activate_custom_targeting_values_with_metadata` interceptor.
        """
        return response

    def post_batch_activate_custom_targeting_values_with_metadata(
        self,
        response: custom_targeting_value_service.BatchActivateCustomTargetingValuesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_targeting_value_service.BatchActivateCustomTargetingValuesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_activate_custom_targeting_values

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CustomTargetingValueService server but before it is returned to user code.

        We recommend only using this `post_batch_activate_custom_targeting_values_with_metadata`
        interceptor in new development instead of the `post_batch_activate_custom_targeting_values` interceptor.
        When both interceptors are used, this `post_batch_activate_custom_targeting_values_with_metadata` interceptor runs after the
        `post_batch_activate_custom_targeting_values` interceptor. The (possibly modified) response returned by
        `post_batch_activate_custom_targeting_values` will be passed to
        `post_batch_activate_custom_targeting_values_with_metadata`.
        """
        return response, metadata

    def pre_batch_create_custom_targeting_values(
        self,
        request: custom_targeting_value_service.BatchCreateCustomTargetingValuesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_targeting_value_service.BatchCreateCustomTargetingValuesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_create_custom_targeting_values

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CustomTargetingValueService server.
        """
        return request, metadata

    def post_batch_create_custom_targeting_values(
        self,
        response: custom_targeting_value_service.BatchCreateCustomTargetingValuesResponse,
    ) -> custom_targeting_value_service.BatchCreateCustomTargetingValuesResponse:
        """Post-rpc interceptor for batch_create_custom_targeting_values

        DEPRECATED. Please use the `post_batch_create_custom_targeting_values_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CustomTargetingValueService server but before
        it is returned to user code. This `post_batch_create_custom_targeting_values` interceptor runs
        before the `post_batch_create_custom_targeting_values_with_metadata` interceptor.
        """
        return response

    def post_batch_create_custom_targeting_values_with_metadata(
        self,
        response: custom_targeting_value_service.BatchCreateCustomTargetingValuesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_targeting_value_service.BatchCreateCustomTargetingValuesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_create_custom_targeting_values

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CustomTargetingValueService server but before it is returned to user code.

        We recommend only using this `post_batch_create_custom_targeting_values_with_metadata`
        interceptor in new development instead of the `post_batch_create_custom_targeting_values` interceptor.
        When both interceptors are used, this `post_batch_create_custom_targeting_values_with_metadata` interceptor runs after the
        `post_batch_create_custom_targeting_values` interceptor. The (possibly modified) response returned by
        `post_batch_create_custom_targeting_values` will be passed to
        `post_batch_create_custom_targeting_values_with_metadata`.
        """
        return response, metadata

    def pre_batch_deactivate_custom_targeting_values(
        self,
        request: custom_targeting_value_service.BatchDeactivateCustomTargetingValuesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_targeting_value_service.BatchDeactivateCustomTargetingValuesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_deactivate_custom_targeting_values

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CustomTargetingValueService server.
        """
        return request, metadata

    def post_batch_deactivate_custom_targeting_values(
        self,
        response: custom_targeting_value_service.BatchDeactivateCustomTargetingValuesResponse,
    ) -> custom_targeting_value_service.BatchDeactivateCustomTargetingValuesResponse:
        """Post-rpc interceptor for batch_deactivate_custom_targeting_values

        DEPRECATED. Please use the `post_batch_deactivate_custom_targeting_values_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CustomTargetingValueService server but before
        it is returned to user code. This `post_batch_deactivate_custom_targeting_values` interceptor runs
        before the `post_batch_deactivate_custom_targeting_values_with_metadata` interceptor.
        """
        return response

    def post_batch_deactivate_custom_targeting_values_with_metadata(
        self,
        response: custom_targeting_value_service.BatchDeactivateCustomTargetingValuesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_targeting_value_service.BatchDeactivateCustomTargetingValuesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_deactivate_custom_targeting_values

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CustomTargetingValueService server but before it is returned to user code.

        We recommend only using this `post_batch_deactivate_custom_targeting_values_with_metadata`
        interceptor in new development instead of the `post_batch_deactivate_custom_targeting_values` interceptor.
        When both interceptors are used, this `post_batch_deactivate_custom_targeting_values_with_metadata` interceptor runs after the
        `post_batch_deactivate_custom_targeting_values` interceptor. The (possibly modified) response returned by
        `post_batch_deactivate_custom_targeting_values` will be passed to
        `post_batch_deactivate_custom_targeting_values_with_metadata`.
        """
        return response, metadata

    def pre_batch_update_custom_targeting_values(
        self,
        request: custom_targeting_value_service.BatchUpdateCustomTargetingValuesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_targeting_value_service.BatchUpdateCustomTargetingValuesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_update_custom_targeting_values

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CustomTargetingValueService server.
        """
        return request, metadata

    def post_batch_update_custom_targeting_values(
        self,
        response: custom_targeting_value_service.BatchUpdateCustomTargetingValuesResponse,
    ) -> custom_targeting_value_service.BatchUpdateCustomTargetingValuesResponse:
        """Post-rpc interceptor for batch_update_custom_targeting_values

        DEPRECATED. Please use the `post_batch_update_custom_targeting_values_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CustomTargetingValueService server but before
        it is returned to user code. This `post_batch_update_custom_targeting_values` interceptor runs
        before the `post_batch_update_custom_targeting_values_with_metadata` interceptor.
        """
        return response

    def post_batch_update_custom_targeting_values_with_metadata(
        self,
        response: custom_targeting_value_service.BatchUpdateCustomTargetingValuesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_targeting_value_service.BatchUpdateCustomTargetingValuesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_update_custom_targeting_values

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CustomTargetingValueService server but before it is returned to user code.

        We recommend only using this `post_batch_update_custom_targeting_values_with_metadata`
        interceptor in new development instead of the `post_batch_update_custom_targeting_values` interceptor.
        When both interceptors are used, this `post_batch_update_custom_targeting_values_with_metadata` interceptor runs after the
        `post_batch_update_custom_targeting_values` interceptor. The (possibly modified) response returned by
        `post_batch_update_custom_targeting_values` will be passed to
        `post_batch_update_custom_targeting_values_with_metadata`.
        """
        return response, metadata

    def pre_create_custom_targeting_value(
        self,
        request: custom_targeting_value_service.CreateCustomTargetingValueRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_targeting_value_service.CreateCustomTargetingValueRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_custom_targeting_value

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CustomTargetingValueService server.
        """
        return request, metadata

    def post_create_custom_targeting_value(
        self, response: custom_targeting_value_messages.CustomTargetingValue
    ) -> custom_targeting_value_messages.CustomTargetingValue:
        """Post-rpc interceptor for create_custom_targeting_value

        DEPRECATED. Please use the `post_create_custom_targeting_value_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CustomTargetingValueService server but before
        it is returned to user code. This `post_create_custom_targeting_value` interceptor runs
        before the `post_create_custom_targeting_value_with_metadata` interceptor.
        """
        return response

    def post_create_custom_targeting_value_with_metadata(
        self,
        response: custom_targeting_value_messages.CustomTargetingValue,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_targeting_value_messages.CustomTargetingValue,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for create_custom_targeting_value

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CustomTargetingValueService server but before it is returned to user code.

        We recommend only using this `post_create_custom_targeting_value_with_metadata`
        interceptor in new development instead of the `post_create_custom_targeting_value` interceptor.
        When both interceptors are used, this `post_create_custom_targeting_value_with_metadata` interceptor runs after the
        `post_create_custom_targeting_value` interceptor. The (possibly modified) response returned by
        `post_create_custom_targeting_value` will be passed to
        `post_create_custom_targeting_value_with_metadata`.
        """
        return response, metadata

    def pre_get_custom_targeting_value(
        self,
        request: custom_targeting_value_service.GetCustomTargetingValueRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_targeting_value_service.GetCustomTargetingValueRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_custom_targeting_value

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CustomTargetingValueService server.
        """
        return request, metadata

    def post_get_custom_targeting_value(
        self, response: custom_targeting_value_messages.CustomTargetingValue
    ) -> custom_targeting_value_messages.CustomTargetingValue:
        """Post-rpc interceptor for get_custom_targeting_value

        DEPRECATED. Please use the `post_get_custom_targeting_value_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CustomTargetingValueService server but before
        it is returned to user code. This `post_get_custom_targeting_value` interceptor runs
        before the `post_get_custom_targeting_value_with_metadata` interceptor.
        """
        return response

    def post_get_custom_targeting_value_with_metadata(
        self,
        response: custom_targeting_value_messages.CustomTargetingValue,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_targeting_value_messages.CustomTargetingValue,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_custom_targeting_value

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CustomTargetingValueService server but before it is returned to user code.

        We recommend only using this `post_get_custom_targeting_value_with_metadata`
        interceptor in new development instead of the `post_get_custom_targeting_value` interceptor.
        When both interceptors are used, this `post_get_custom_targeting_value_with_metadata` interceptor runs after the
        `post_get_custom_targeting_value` interceptor. The (possibly modified) response returned by
        `post_get_custom_targeting_value` will be passed to
        `post_get_custom_targeting_value_with_metadata`.
        """
        return response, metadata

    def pre_list_custom_targeting_values(
        self,
        request: custom_targeting_value_service.ListCustomTargetingValuesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_targeting_value_service.ListCustomTargetingValuesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_custom_targeting_values

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CustomTargetingValueService server.
        """
        return request, metadata

    def post_list_custom_targeting_values(
        self, response: custom_targeting_value_service.ListCustomTargetingValuesResponse
    ) -> custom_targeting_value_service.ListCustomTargetingValuesResponse:
        """Post-rpc interceptor for list_custom_targeting_values

        DEPRECATED. Please use the `post_list_custom_targeting_values_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CustomTargetingValueService server but before
        it is returned to user code. This `post_list_custom_targeting_values` interceptor runs
        before the `post_list_custom_targeting_values_with_metadata` interceptor.
        """
        return response

    def post_list_custom_targeting_values_with_metadata(
        self,
        response: custom_targeting_value_service.ListCustomTargetingValuesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_targeting_value_service.ListCustomTargetingValuesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_custom_targeting_values

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CustomTargetingValueService server but before it is returned to user code.

        We recommend only using this `post_list_custom_targeting_values_with_metadata`
        interceptor in new development instead of the `post_list_custom_targeting_values` interceptor.
        When both interceptors are used, this `post_list_custom_targeting_values_with_metadata` interceptor runs after the
        `post_list_custom_targeting_values` interceptor. The (possibly modified) response returned by
        `post_list_custom_targeting_values` will be passed to
        `post_list_custom_targeting_values_with_metadata`.
        """
        return response, metadata

    def pre_update_custom_targeting_value(
        self,
        request: custom_targeting_value_service.UpdateCustomTargetingValueRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_targeting_value_service.UpdateCustomTargetingValueRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_custom_targeting_value

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CustomTargetingValueService server.
        """
        return request, metadata

    def post_update_custom_targeting_value(
        self, response: custom_targeting_value_messages.CustomTargetingValue
    ) -> custom_targeting_value_messages.CustomTargetingValue:
        """Post-rpc interceptor for update_custom_targeting_value

        DEPRECATED. Please use the `post_update_custom_targeting_value_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CustomTargetingValueService server but before
        it is returned to user code. This `post_update_custom_targeting_value` interceptor runs
        before the `post_update_custom_targeting_value_with_metadata` interceptor.
        """
        return response

    def post_update_custom_targeting_value_with_metadata(
        self,
        response: custom_targeting_value_messages.CustomTargetingValue,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_targeting_value_messages.CustomTargetingValue,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for update_custom_targeting_value

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CustomTargetingValueService server but before it is returned to user code.

        We recommend only using this `post_update_custom_targeting_value_with_metadata`
        interceptor in new development instead of the `post_update_custom_targeting_value` interceptor.
        When both interceptors are used, this `post_update_custom_targeting_value_with_metadata` interceptor runs after the
        `post_update_custom_targeting_value` interceptor. The (possibly modified) response returned by
        `post_update_custom_targeting_value` will be passed to
        `post_update_custom_targeting_value_with_metadata`.
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
        before they are sent to the CustomTargetingValueService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the CustomTargetingValueService server but before
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
        before they are sent to the CustomTargetingValueService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the CustomTargetingValueService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class CustomTargetingValueServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: CustomTargetingValueServiceRestInterceptor


class CustomTargetingValueServiceRestTransport(
    _BaseCustomTargetingValueServiceRestTransport
):
    """REST backend synchronous transport for CustomTargetingValueService.

    Provides methods for handling ``CustomTargetingValue`` objects.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "admanager.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[CustomTargetingValueServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'admanager.googleapis.com').
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
            interceptor (Optional[CustomTargetingValueServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or CustomTargetingValueServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _BatchActivateCustomTargetingValues(
        _BaseCustomTargetingValueServiceRestTransport._BaseBatchActivateCustomTargetingValues,
        CustomTargetingValueServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "CustomTargetingValueServiceRestTransport.BatchActivateCustomTargetingValues"
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
            request: custom_targeting_value_service.BatchActivateCustomTargetingValuesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> custom_targeting_value_service.BatchActivateCustomTargetingValuesResponse:
            r"""Call the batch activate custom
            targeting values method over HTTP.

                Args:
                    request (~.custom_targeting_value_service.BatchActivateCustomTargetingValuesRequest):
                        The request object. Request object for
                    ``BatchActivateCustomTargetingValues`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.custom_targeting_value_service.BatchActivateCustomTargetingValuesResponse:
                        Response object for
                    ``BatchActivateCustomTargetingValues`` method.

            """

            http_options = _BaseCustomTargetingValueServiceRestTransport._BaseBatchActivateCustomTargetingValues._get_http_options()
            request, metadata = (
                self._interceptor.pre_batch_activate_custom_targeting_values(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCustomTargetingValueServiceRestTransport._BaseBatchActivateCustomTargetingValues,
                    "_BaseBatchActivateCustomTargetingValues__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CustomTargetingValueServiceClient.BatchActivateCustomTargetingValues",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomTargetingValueService",
                        "rpcName": "BatchActivateCustomTargetingValues",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CustomTargetingValueServiceRestTransport._BatchActivateCustomTargetingValues._get_response(
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
            resp = custom_targeting_value_service.BatchActivateCustomTargetingValuesResponse()
            pb_resp = custom_targeting_value_service.BatchActivateCustomTargetingValuesResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_activate_custom_targeting_values(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_activate_custom_targeting_values_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = custom_targeting_value_service.BatchActivateCustomTargetingValuesResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.CustomTargetingValueServiceClient.batch_activate_custom_targeting_values",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomTargetingValueService",
                        "rpcName": "BatchActivateCustomTargetingValues",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchCreateCustomTargetingValues(
        _BaseCustomTargetingValueServiceRestTransport._BaseBatchCreateCustomTargetingValues,
        CustomTargetingValueServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "CustomTargetingValueServiceRestTransport.BatchCreateCustomTargetingValues"
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
            request: custom_targeting_value_service.BatchCreateCustomTargetingValuesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> custom_targeting_value_service.BatchCreateCustomTargetingValuesResponse:
            r"""Call the batch create custom
            targeting values method over HTTP.

                Args:
                    request (~.custom_targeting_value_service.BatchCreateCustomTargetingValuesRequest):
                        The request object. Request object for ``BatchCreateCustomTargetingValues``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.custom_targeting_value_service.BatchCreateCustomTargetingValuesResponse:
                        Response object for ``BatchCreateCustomTargetingValues``
                    method.

            """

            http_options = _BaseCustomTargetingValueServiceRestTransport._BaseBatchCreateCustomTargetingValues._get_http_options()
            request, metadata = (
                self._interceptor.pre_batch_create_custom_targeting_values(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCustomTargetingValueServiceRestTransport._BaseBatchCreateCustomTargetingValues,
                    "_BaseBatchCreateCustomTargetingValues__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CustomTargetingValueServiceClient.BatchCreateCustomTargetingValues",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomTargetingValueService",
                        "rpcName": "BatchCreateCustomTargetingValues",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CustomTargetingValueServiceRestTransport._BatchCreateCustomTargetingValues._get_response(
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
            resp = custom_targeting_value_service.BatchCreateCustomTargetingValuesResponse()
            pb_resp = custom_targeting_value_service.BatchCreateCustomTargetingValuesResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_create_custom_targeting_values(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_create_custom_targeting_values_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = custom_targeting_value_service.BatchCreateCustomTargetingValuesResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.CustomTargetingValueServiceClient.batch_create_custom_targeting_values",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomTargetingValueService",
                        "rpcName": "BatchCreateCustomTargetingValues",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchDeactivateCustomTargetingValues(
        _BaseCustomTargetingValueServiceRestTransport._BaseBatchDeactivateCustomTargetingValues,
        CustomTargetingValueServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "CustomTargetingValueServiceRestTransport.BatchDeactivateCustomTargetingValues"
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
            request: custom_targeting_value_service.BatchDeactivateCustomTargetingValuesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> (
            custom_targeting_value_service.BatchDeactivateCustomTargetingValuesResponse
        ):
            r"""Call the batch deactivate custom
            targeting values method over HTTP.

                Args:
                    request (~.custom_targeting_value_service.BatchDeactivateCustomTargetingValuesRequest):
                        The request object. Request message for
                    ``BatchDeactivateCustomTargetingValues`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.custom_targeting_value_service.BatchDeactivateCustomTargetingValuesResponse:
                        Response object for
                    ``BatchDeactivateCustomTargetingValues`` method.

            """

            http_options = _BaseCustomTargetingValueServiceRestTransport._BaseBatchDeactivateCustomTargetingValues._get_http_options()
            request, metadata = (
                self._interceptor.pre_batch_deactivate_custom_targeting_values(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCustomTargetingValueServiceRestTransport._BaseBatchDeactivateCustomTargetingValues,
                    "_BaseBatchDeactivateCustomTargetingValues__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CustomTargetingValueServiceClient.BatchDeactivateCustomTargetingValues",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomTargetingValueService",
                        "rpcName": "BatchDeactivateCustomTargetingValues",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CustomTargetingValueServiceRestTransport._BatchDeactivateCustomTargetingValues._get_response(
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
            resp = custom_targeting_value_service.BatchDeactivateCustomTargetingValuesResponse()
            pb_resp = custom_targeting_value_service.BatchDeactivateCustomTargetingValuesResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_deactivate_custom_targeting_values(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_deactivate_custom_targeting_values_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = custom_targeting_value_service.BatchDeactivateCustomTargetingValuesResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.CustomTargetingValueServiceClient.batch_deactivate_custom_targeting_values",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomTargetingValueService",
                        "rpcName": "BatchDeactivateCustomTargetingValues",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchUpdateCustomTargetingValues(
        _BaseCustomTargetingValueServiceRestTransport._BaseBatchUpdateCustomTargetingValues,
        CustomTargetingValueServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "CustomTargetingValueServiceRestTransport.BatchUpdateCustomTargetingValues"
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
            request: custom_targeting_value_service.BatchUpdateCustomTargetingValuesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> custom_targeting_value_service.BatchUpdateCustomTargetingValuesResponse:
            r"""Call the batch update custom
            targeting values method over HTTP.

                Args:
                    request (~.custom_targeting_value_service.BatchUpdateCustomTargetingValuesRequest):
                        The request object. Request object for ``BatchUpdateCustomTargetingValues``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.custom_targeting_value_service.BatchUpdateCustomTargetingValuesResponse:
                        Response object for ``BatchUpdateCustomTargetingValues``
                    method.

            """

            http_options = _BaseCustomTargetingValueServiceRestTransport._BaseBatchUpdateCustomTargetingValues._get_http_options()
            request, metadata = (
                self._interceptor.pre_batch_update_custom_targeting_values(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCustomTargetingValueServiceRestTransport._BaseBatchUpdateCustomTargetingValues,
                    "_BaseBatchUpdateCustomTargetingValues__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CustomTargetingValueServiceClient.BatchUpdateCustomTargetingValues",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomTargetingValueService",
                        "rpcName": "BatchUpdateCustomTargetingValues",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CustomTargetingValueServiceRestTransport._BatchUpdateCustomTargetingValues._get_response(
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
            resp = custom_targeting_value_service.BatchUpdateCustomTargetingValuesResponse()
            pb_resp = custom_targeting_value_service.BatchUpdateCustomTargetingValuesResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_update_custom_targeting_values(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_update_custom_targeting_values_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = custom_targeting_value_service.BatchUpdateCustomTargetingValuesResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.CustomTargetingValueServiceClient.batch_update_custom_targeting_values",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomTargetingValueService",
                        "rpcName": "BatchUpdateCustomTargetingValues",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateCustomTargetingValue(
        _BaseCustomTargetingValueServiceRestTransport._BaseCreateCustomTargetingValue,
        CustomTargetingValueServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "CustomTargetingValueServiceRestTransport.CreateCustomTargetingValue"
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
            request: custom_targeting_value_service.CreateCustomTargetingValueRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> custom_targeting_value_messages.CustomTargetingValue:
            r"""Call the create custom targeting
            value method over HTTP.

                Args:
                    request (~.custom_targeting_value_service.CreateCustomTargetingValueRequest):
                        The request object. Request object for ``CreateCustomTargetingValue``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.custom_targeting_value_messages.CustomTargetingValue:
                        The ``CustomTargetingValue`` resource.
            """

            http_options = _BaseCustomTargetingValueServiceRestTransport._BaseCreateCustomTargetingValue._get_http_options()
            request, metadata = self._interceptor.pre_create_custom_targeting_value(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCustomTargetingValueServiceRestTransport._BaseCreateCustomTargetingValue,
                    "_BaseCreateCustomTargetingValue__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CustomTargetingValueServiceClient.CreateCustomTargetingValue",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomTargetingValueService",
                        "rpcName": "CreateCustomTargetingValue",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CustomTargetingValueServiceRestTransport._CreateCustomTargetingValue._get_response(
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
            resp = custom_targeting_value_messages.CustomTargetingValue()
            pb_resp = custom_targeting_value_messages.CustomTargetingValue.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_custom_targeting_value(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_create_custom_targeting_value_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        custom_targeting_value_messages.CustomTargetingValue.to_json(
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
                    "Received response for google.ads.admanager_v1.CustomTargetingValueServiceClient.create_custom_targeting_value",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomTargetingValueService",
                        "rpcName": "CreateCustomTargetingValue",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetCustomTargetingValue(
        _BaseCustomTargetingValueServiceRestTransport._BaseGetCustomTargetingValue,
        CustomTargetingValueServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "CustomTargetingValueServiceRestTransport.GetCustomTargetingValue"
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
            request: custom_targeting_value_service.GetCustomTargetingValueRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> custom_targeting_value_messages.CustomTargetingValue:
            r"""Call the get custom targeting
            value method over HTTP.

                Args:
                    request (~.custom_targeting_value_service.GetCustomTargetingValueRequest):
                        The request object. Request object for ``GetCustomTargetingValue`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.custom_targeting_value_messages.CustomTargetingValue:
                        The ``CustomTargetingValue`` resource.
            """

            http_options = _BaseCustomTargetingValueServiceRestTransport._BaseGetCustomTargetingValue._get_http_options()
            request, metadata = self._interceptor.pre_get_custom_targeting_value(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCustomTargetingValueServiceRestTransport._BaseGetCustomTargetingValue,
                    "_BaseGetCustomTargetingValue__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CustomTargetingValueServiceClient.GetCustomTargetingValue",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomTargetingValueService",
                        "rpcName": "GetCustomTargetingValue",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CustomTargetingValueServiceRestTransport._GetCustomTargetingValue._get_response(
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
            resp = custom_targeting_value_messages.CustomTargetingValue()
            pb_resp = custom_targeting_value_messages.CustomTargetingValue.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_custom_targeting_value(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_custom_targeting_value_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        custom_targeting_value_messages.CustomTargetingValue.to_json(
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
                    "Received response for google.ads.admanager_v1.CustomTargetingValueServiceClient.get_custom_targeting_value",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomTargetingValueService",
                        "rpcName": "GetCustomTargetingValue",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListCustomTargetingValues(
        _BaseCustomTargetingValueServiceRestTransport._BaseListCustomTargetingValues,
        CustomTargetingValueServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "CustomTargetingValueServiceRestTransport.ListCustomTargetingValues"
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
            request: custom_targeting_value_service.ListCustomTargetingValuesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> custom_targeting_value_service.ListCustomTargetingValuesResponse:
            r"""Call the list custom targeting
            values method over HTTP.

                Args:
                    request (~.custom_targeting_value_service.ListCustomTargetingValuesRequest):
                        The request object. Request object for ``ListCustomTargetingValues`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.custom_targeting_value_service.ListCustomTargetingValuesResponse:
                        Response object for ``ListCustomTargetingValuesRequest``
                    containing matching ``CustomTargetingValue`` objects.

            """

            http_options = _BaseCustomTargetingValueServiceRestTransport._BaseListCustomTargetingValues._get_http_options()
            request, metadata = self._interceptor.pre_list_custom_targeting_values(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCustomTargetingValueServiceRestTransport._BaseListCustomTargetingValues,
                    "_BaseListCustomTargetingValues__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CustomTargetingValueServiceClient.ListCustomTargetingValues",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomTargetingValueService",
                        "rpcName": "ListCustomTargetingValues",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CustomTargetingValueServiceRestTransport._ListCustomTargetingValues._get_response(
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
            resp = custom_targeting_value_service.ListCustomTargetingValuesResponse()
            pb_resp = (
                custom_targeting_value_service.ListCustomTargetingValuesResponse.pb(
                    resp
                )
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_custom_targeting_values(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_custom_targeting_values_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = custom_targeting_value_service.ListCustomTargetingValuesResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.CustomTargetingValueServiceClient.list_custom_targeting_values",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomTargetingValueService",
                        "rpcName": "ListCustomTargetingValues",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateCustomTargetingValue(
        _BaseCustomTargetingValueServiceRestTransport._BaseUpdateCustomTargetingValue,
        CustomTargetingValueServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "CustomTargetingValueServiceRestTransport.UpdateCustomTargetingValue"
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
            request: custom_targeting_value_service.UpdateCustomTargetingValueRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> custom_targeting_value_messages.CustomTargetingValue:
            r"""Call the update custom targeting
            value method over HTTP.

                Args:
                    request (~.custom_targeting_value_service.UpdateCustomTargetingValueRequest):
                        The request object. Request object for ``UpdateCustomTargetingValue``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.custom_targeting_value_messages.CustomTargetingValue:
                        The ``CustomTargetingValue`` resource.
            """

            http_options = _BaseCustomTargetingValueServiceRestTransport._BaseUpdateCustomTargetingValue._get_http_options()
            request, metadata = self._interceptor.pre_update_custom_targeting_value(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCustomTargetingValueServiceRestTransport._BaseUpdateCustomTargetingValue,
                    "_BaseUpdateCustomTargetingValue__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CustomTargetingValueServiceClient.UpdateCustomTargetingValue",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomTargetingValueService",
                        "rpcName": "UpdateCustomTargetingValue",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CustomTargetingValueServiceRestTransport._UpdateCustomTargetingValue._get_response(
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
            resp = custom_targeting_value_messages.CustomTargetingValue()
            pb_resp = custom_targeting_value_messages.CustomTargetingValue.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_custom_targeting_value(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_update_custom_targeting_value_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        custom_targeting_value_messages.CustomTargetingValue.to_json(
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
                    "Received response for google.ads.admanager_v1.CustomTargetingValueServiceClient.update_custom_targeting_value",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomTargetingValueService",
                        "rpcName": "UpdateCustomTargetingValue",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_activate_custom_targeting_values(
        self,
    ) -> Callable[
        [custom_targeting_value_service.BatchActivateCustomTargetingValuesRequest],
        custom_targeting_value_service.BatchActivateCustomTargetingValuesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchActivateCustomTargetingValues(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_create_custom_targeting_values(
        self,
    ) -> Callable[
        [custom_targeting_value_service.BatchCreateCustomTargetingValuesRequest],
        custom_targeting_value_service.BatchCreateCustomTargetingValuesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchCreateCustomTargetingValues(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_deactivate_custom_targeting_values(
        self,
    ) -> Callable[
        [custom_targeting_value_service.BatchDeactivateCustomTargetingValuesRequest],
        custom_targeting_value_service.BatchDeactivateCustomTargetingValuesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchDeactivateCustomTargetingValues(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_update_custom_targeting_values(
        self,
    ) -> Callable[
        [custom_targeting_value_service.BatchUpdateCustomTargetingValuesRequest],
        custom_targeting_value_service.BatchUpdateCustomTargetingValuesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchUpdateCustomTargetingValues(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_custom_targeting_value(
        self,
    ) -> Callable[
        [custom_targeting_value_service.CreateCustomTargetingValueRequest],
        custom_targeting_value_messages.CustomTargetingValue,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateCustomTargetingValue(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_custom_targeting_value(
        self,
    ) -> Callable[
        [custom_targeting_value_service.GetCustomTargetingValueRequest],
        custom_targeting_value_messages.CustomTargetingValue,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetCustomTargetingValue(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_custom_targeting_values(
        self,
    ) -> Callable[
        [custom_targeting_value_service.ListCustomTargetingValuesRequest],
        custom_targeting_value_service.ListCustomTargetingValuesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListCustomTargetingValues(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_custom_targeting_value(
        self,
    ) -> Callable[
        [custom_targeting_value_service.UpdateCustomTargetingValueRequest],
        custom_targeting_value_messages.CustomTargetingValue,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateCustomTargetingValue(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseCustomTargetingValueServiceRestTransport._BaseCancelOperation,
        CustomTargetingValueServiceRestStub,
    ):
        def __hash__(self):
            return hash("CustomTargetingValueServiceRestTransport.CancelOperation")

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

            http_options = _BaseCustomTargetingValueServiceRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCustomTargetingValueServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.ads.admanager_v1.CustomTargetingValueServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomTargetingValueService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CustomTargetingValueServiceRestTransport._CancelOperation._get_response(
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

            return self._interceptor.post_cancel_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseCustomTargetingValueServiceRestTransport._BaseGetOperation,
        CustomTargetingValueServiceRestStub,
    ):
        def __hash__(self):
            return hash("CustomTargetingValueServiceRestTransport.GetOperation")

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

            http_options = _BaseCustomTargetingValueServiceRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCustomTargetingValueServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.ads.admanager_v1.CustomTargetingValueServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomTargetingValueService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CustomTargetingValueServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.ads.admanager_v1.CustomTargetingValueServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomTargetingValueService",
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


__all__ = ("CustomTargetingValueServiceRestTransport",)
