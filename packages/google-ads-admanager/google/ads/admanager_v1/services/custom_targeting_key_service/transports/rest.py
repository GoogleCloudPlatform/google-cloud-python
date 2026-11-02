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
    custom_targeting_key_messages,
    custom_targeting_key_service,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseCustomTargetingKeyServiceRestTransport

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


class CustomTargetingKeyServiceRestInterceptor:
    """Interceptor for CustomTargetingKeyService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the CustomTargetingKeyServiceRestTransport.

    .. code-block:: python
        class MyCustomCustomTargetingKeyServiceInterceptor(CustomTargetingKeyServiceRestInterceptor):
            def pre_batch_activate_custom_targeting_keys(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_activate_custom_targeting_keys(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_create_custom_targeting_keys(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_create_custom_targeting_keys(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_deactivate_custom_targeting_keys(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_deactivate_custom_targeting_keys(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_update_custom_targeting_keys(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_update_custom_targeting_keys(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_custom_targeting_key(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_custom_targeting_key(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_custom_targeting_key(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_custom_targeting_key(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_custom_targeting_keys(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_custom_targeting_keys(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_custom_targeting_key(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_custom_targeting_key(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = CustomTargetingKeyServiceRestTransport(interceptor=MyCustomCustomTargetingKeyServiceInterceptor())
        client = CustomTargetingKeyServiceClient(transport=transport)


    """

    def pre_batch_activate_custom_targeting_keys(
        self,
        request: custom_targeting_key_service.BatchActivateCustomTargetingKeysRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_targeting_key_service.BatchActivateCustomTargetingKeysRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_activate_custom_targeting_keys

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CustomTargetingKeyService server.
        """
        return request, metadata

    def post_batch_activate_custom_targeting_keys(
        self,
        response: custom_targeting_key_service.BatchActivateCustomTargetingKeysResponse,
    ) -> custom_targeting_key_service.BatchActivateCustomTargetingKeysResponse:
        """Post-rpc interceptor for batch_activate_custom_targeting_keys

        DEPRECATED. Please use the `post_batch_activate_custom_targeting_keys_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CustomTargetingKeyService server but before
        it is returned to user code. This `post_batch_activate_custom_targeting_keys` interceptor runs
        before the `post_batch_activate_custom_targeting_keys_with_metadata` interceptor.
        """
        return response

    def post_batch_activate_custom_targeting_keys_with_metadata(
        self,
        response: custom_targeting_key_service.BatchActivateCustomTargetingKeysResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_targeting_key_service.BatchActivateCustomTargetingKeysResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_activate_custom_targeting_keys

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CustomTargetingKeyService server but before it is returned to user code.

        We recommend only using this `post_batch_activate_custom_targeting_keys_with_metadata`
        interceptor in new development instead of the `post_batch_activate_custom_targeting_keys` interceptor.
        When both interceptors are used, this `post_batch_activate_custom_targeting_keys_with_metadata` interceptor runs after the
        `post_batch_activate_custom_targeting_keys` interceptor. The (possibly modified) response returned by
        `post_batch_activate_custom_targeting_keys` will be passed to
        `post_batch_activate_custom_targeting_keys_with_metadata`.
        """
        return response, metadata

    def pre_batch_create_custom_targeting_keys(
        self,
        request: custom_targeting_key_service.BatchCreateCustomTargetingKeysRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_targeting_key_service.BatchCreateCustomTargetingKeysRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_create_custom_targeting_keys

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CustomTargetingKeyService server.
        """
        return request, metadata

    def post_batch_create_custom_targeting_keys(
        self,
        response: custom_targeting_key_service.BatchCreateCustomTargetingKeysResponse,
    ) -> custom_targeting_key_service.BatchCreateCustomTargetingKeysResponse:
        """Post-rpc interceptor for batch_create_custom_targeting_keys

        DEPRECATED. Please use the `post_batch_create_custom_targeting_keys_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CustomTargetingKeyService server but before
        it is returned to user code. This `post_batch_create_custom_targeting_keys` interceptor runs
        before the `post_batch_create_custom_targeting_keys_with_metadata` interceptor.
        """
        return response

    def post_batch_create_custom_targeting_keys_with_metadata(
        self,
        response: custom_targeting_key_service.BatchCreateCustomTargetingKeysResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_targeting_key_service.BatchCreateCustomTargetingKeysResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_create_custom_targeting_keys

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CustomTargetingKeyService server but before it is returned to user code.

        We recommend only using this `post_batch_create_custom_targeting_keys_with_metadata`
        interceptor in new development instead of the `post_batch_create_custom_targeting_keys` interceptor.
        When both interceptors are used, this `post_batch_create_custom_targeting_keys_with_metadata` interceptor runs after the
        `post_batch_create_custom_targeting_keys` interceptor. The (possibly modified) response returned by
        `post_batch_create_custom_targeting_keys` will be passed to
        `post_batch_create_custom_targeting_keys_with_metadata`.
        """
        return response, metadata

    def pre_batch_deactivate_custom_targeting_keys(
        self,
        request: custom_targeting_key_service.BatchDeactivateCustomTargetingKeysRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_targeting_key_service.BatchDeactivateCustomTargetingKeysRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_deactivate_custom_targeting_keys

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CustomTargetingKeyService server.
        """
        return request, metadata

    def post_batch_deactivate_custom_targeting_keys(
        self,
        response: custom_targeting_key_service.BatchDeactivateCustomTargetingKeysResponse,
    ) -> custom_targeting_key_service.BatchDeactivateCustomTargetingKeysResponse:
        """Post-rpc interceptor for batch_deactivate_custom_targeting_keys

        DEPRECATED. Please use the `post_batch_deactivate_custom_targeting_keys_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CustomTargetingKeyService server but before
        it is returned to user code. This `post_batch_deactivate_custom_targeting_keys` interceptor runs
        before the `post_batch_deactivate_custom_targeting_keys_with_metadata` interceptor.
        """
        return response

    def post_batch_deactivate_custom_targeting_keys_with_metadata(
        self,
        response: custom_targeting_key_service.BatchDeactivateCustomTargetingKeysResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_targeting_key_service.BatchDeactivateCustomTargetingKeysResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_deactivate_custom_targeting_keys

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CustomTargetingKeyService server but before it is returned to user code.

        We recommend only using this `post_batch_deactivate_custom_targeting_keys_with_metadata`
        interceptor in new development instead of the `post_batch_deactivate_custom_targeting_keys` interceptor.
        When both interceptors are used, this `post_batch_deactivate_custom_targeting_keys_with_metadata` interceptor runs after the
        `post_batch_deactivate_custom_targeting_keys` interceptor. The (possibly modified) response returned by
        `post_batch_deactivate_custom_targeting_keys` will be passed to
        `post_batch_deactivate_custom_targeting_keys_with_metadata`.
        """
        return response, metadata

    def pre_batch_update_custom_targeting_keys(
        self,
        request: custom_targeting_key_service.BatchUpdateCustomTargetingKeysRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_targeting_key_service.BatchUpdateCustomTargetingKeysRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_update_custom_targeting_keys

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CustomTargetingKeyService server.
        """
        return request, metadata

    def post_batch_update_custom_targeting_keys(
        self,
        response: custom_targeting_key_service.BatchUpdateCustomTargetingKeysResponse,
    ) -> custom_targeting_key_service.BatchUpdateCustomTargetingKeysResponse:
        """Post-rpc interceptor for batch_update_custom_targeting_keys

        DEPRECATED. Please use the `post_batch_update_custom_targeting_keys_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CustomTargetingKeyService server but before
        it is returned to user code. This `post_batch_update_custom_targeting_keys` interceptor runs
        before the `post_batch_update_custom_targeting_keys_with_metadata` interceptor.
        """
        return response

    def post_batch_update_custom_targeting_keys_with_metadata(
        self,
        response: custom_targeting_key_service.BatchUpdateCustomTargetingKeysResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_targeting_key_service.BatchUpdateCustomTargetingKeysResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_update_custom_targeting_keys

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CustomTargetingKeyService server but before it is returned to user code.

        We recommend only using this `post_batch_update_custom_targeting_keys_with_metadata`
        interceptor in new development instead of the `post_batch_update_custom_targeting_keys` interceptor.
        When both interceptors are used, this `post_batch_update_custom_targeting_keys_with_metadata` interceptor runs after the
        `post_batch_update_custom_targeting_keys` interceptor. The (possibly modified) response returned by
        `post_batch_update_custom_targeting_keys` will be passed to
        `post_batch_update_custom_targeting_keys_with_metadata`.
        """
        return response, metadata

    def pre_create_custom_targeting_key(
        self,
        request: custom_targeting_key_service.CreateCustomTargetingKeyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_targeting_key_service.CreateCustomTargetingKeyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_custom_targeting_key

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CustomTargetingKeyService server.
        """
        return request, metadata

    def post_create_custom_targeting_key(
        self, response: custom_targeting_key_messages.CustomTargetingKey
    ) -> custom_targeting_key_messages.CustomTargetingKey:
        """Post-rpc interceptor for create_custom_targeting_key

        DEPRECATED. Please use the `post_create_custom_targeting_key_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CustomTargetingKeyService server but before
        it is returned to user code. This `post_create_custom_targeting_key` interceptor runs
        before the `post_create_custom_targeting_key_with_metadata` interceptor.
        """
        return response

    def post_create_custom_targeting_key_with_metadata(
        self,
        response: custom_targeting_key_messages.CustomTargetingKey,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_targeting_key_messages.CustomTargetingKey,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for create_custom_targeting_key

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CustomTargetingKeyService server but before it is returned to user code.

        We recommend only using this `post_create_custom_targeting_key_with_metadata`
        interceptor in new development instead of the `post_create_custom_targeting_key` interceptor.
        When both interceptors are used, this `post_create_custom_targeting_key_with_metadata` interceptor runs after the
        `post_create_custom_targeting_key` interceptor. The (possibly modified) response returned by
        `post_create_custom_targeting_key` will be passed to
        `post_create_custom_targeting_key_with_metadata`.
        """
        return response, metadata

    def pre_get_custom_targeting_key(
        self,
        request: custom_targeting_key_service.GetCustomTargetingKeyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_targeting_key_service.GetCustomTargetingKeyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_custom_targeting_key

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CustomTargetingKeyService server.
        """
        return request, metadata

    def post_get_custom_targeting_key(
        self, response: custom_targeting_key_messages.CustomTargetingKey
    ) -> custom_targeting_key_messages.CustomTargetingKey:
        """Post-rpc interceptor for get_custom_targeting_key

        DEPRECATED. Please use the `post_get_custom_targeting_key_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CustomTargetingKeyService server but before
        it is returned to user code. This `post_get_custom_targeting_key` interceptor runs
        before the `post_get_custom_targeting_key_with_metadata` interceptor.
        """
        return response

    def post_get_custom_targeting_key_with_metadata(
        self,
        response: custom_targeting_key_messages.CustomTargetingKey,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_targeting_key_messages.CustomTargetingKey,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_custom_targeting_key

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CustomTargetingKeyService server but before it is returned to user code.

        We recommend only using this `post_get_custom_targeting_key_with_metadata`
        interceptor in new development instead of the `post_get_custom_targeting_key` interceptor.
        When both interceptors are used, this `post_get_custom_targeting_key_with_metadata` interceptor runs after the
        `post_get_custom_targeting_key` interceptor. The (possibly modified) response returned by
        `post_get_custom_targeting_key` will be passed to
        `post_get_custom_targeting_key_with_metadata`.
        """
        return response, metadata

    def pre_list_custom_targeting_keys(
        self,
        request: custom_targeting_key_service.ListCustomTargetingKeysRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_targeting_key_service.ListCustomTargetingKeysRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_custom_targeting_keys

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CustomTargetingKeyService server.
        """
        return request, metadata

    def post_list_custom_targeting_keys(
        self, response: custom_targeting_key_service.ListCustomTargetingKeysResponse
    ) -> custom_targeting_key_service.ListCustomTargetingKeysResponse:
        """Post-rpc interceptor for list_custom_targeting_keys

        DEPRECATED. Please use the `post_list_custom_targeting_keys_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CustomTargetingKeyService server but before
        it is returned to user code. This `post_list_custom_targeting_keys` interceptor runs
        before the `post_list_custom_targeting_keys_with_metadata` interceptor.
        """
        return response

    def post_list_custom_targeting_keys_with_metadata(
        self,
        response: custom_targeting_key_service.ListCustomTargetingKeysResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_targeting_key_service.ListCustomTargetingKeysResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_custom_targeting_keys

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CustomTargetingKeyService server but before it is returned to user code.

        We recommend only using this `post_list_custom_targeting_keys_with_metadata`
        interceptor in new development instead of the `post_list_custom_targeting_keys` interceptor.
        When both interceptors are used, this `post_list_custom_targeting_keys_with_metadata` interceptor runs after the
        `post_list_custom_targeting_keys` interceptor. The (possibly modified) response returned by
        `post_list_custom_targeting_keys` will be passed to
        `post_list_custom_targeting_keys_with_metadata`.
        """
        return response, metadata

    def pre_update_custom_targeting_key(
        self,
        request: custom_targeting_key_service.UpdateCustomTargetingKeyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_targeting_key_service.UpdateCustomTargetingKeyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_custom_targeting_key

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CustomTargetingKeyService server.
        """
        return request, metadata

    def post_update_custom_targeting_key(
        self, response: custom_targeting_key_messages.CustomTargetingKey
    ) -> custom_targeting_key_messages.CustomTargetingKey:
        """Post-rpc interceptor for update_custom_targeting_key

        DEPRECATED. Please use the `post_update_custom_targeting_key_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CustomTargetingKeyService server but before
        it is returned to user code. This `post_update_custom_targeting_key` interceptor runs
        before the `post_update_custom_targeting_key_with_metadata` interceptor.
        """
        return response

    def post_update_custom_targeting_key_with_metadata(
        self,
        response: custom_targeting_key_messages.CustomTargetingKey,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        custom_targeting_key_messages.CustomTargetingKey,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for update_custom_targeting_key

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CustomTargetingKeyService server but before it is returned to user code.

        We recommend only using this `post_update_custom_targeting_key_with_metadata`
        interceptor in new development instead of the `post_update_custom_targeting_key` interceptor.
        When both interceptors are used, this `post_update_custom_targeting_key_with_metadata` interceptor runs after the
        `post_update_custom_targeting_key` interceptor. The (possibly modified) response returned by
        `post_update_custom_targeting_key` will be passed to
        `post_update_custom_targeting_key_with_metadata`.
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
        before they are sent to the CustomTargetingKeyService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the CustomTargetingKeyService server but before
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
        before they are sent to the CustomTargetingKeyService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the CustomTargetingKeyService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class CustomTargetingKeyServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: CustomTargetingKeyServiceRestInterceptor


class CustomTargetingKeyServiceRestTransport(
    _BaseCustomTargetingKeyServiceRestTransport
):
    """REST backend synchronous transport for CustomTargetingKeyService.

    Provides methods for handling ``CustomTargetingKey`` objects.

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
        interceptor: Optional[CustomTargetingKeyServiceRestInterceptor] = None,
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
            interceptor (Optional[CustomTargetingKeyServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or CustomTargetingKeyServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _BatchActivateCustomTargetingKeys(
        _BaseCustomTargetingKeyServiceRestTransport._BaseBatchActivateCustomTargetingKeys,
        CustomTargetingKeyServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "CustomTargetingKeyServiceRestTransport.BatchActivateCustomTargetingKeys"
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
            request: custom_targeting_key_service.BatchActivateCustomTargetingKeysRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> custom_targeting_key_service.BatchActivateCustomTargetingKeysResponse:
            r"""Call the batch activate custom
            targeting keys method over HTTP.

                Args:
                    request (~.custom_targeting_key_service.BatchActivateCustomTargetingKeysRequest):
                        The request object. Request object for ``BatchActivateCustomTargetingKeys``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.custom_targeting_key_service.BatchActivateCustomTargetingKeysResponse:
                        Response object for ``BatchActivateCustomTargetingKeys``
                    method.

            """

            http_options = _BaseCustomTargetingKeyServiceRestTransport._BaseBatchActivateCustomTargetingKeys._get_http_options()
            request, metadata = (
                self._interceptor.pre_batch_activate_custom_targeting_keys(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCustomTargetingKeyServiceRestTransport._BaseBatchActivateCustomTargetingKeys,
                    "_BaseBatchActivateCustomTargetingKeys__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CustomTargetingKeyServiceClient.BatchActivateCustomTargetingKeys",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomTargetingKeyService",
                        "rpcName": "BatchActivateCustomTargetingKeys",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CustomTargetingKeyServiceRestTransport._BatchActivateCustomTargetingKeys._get_response(
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
            resp = (
                custom_targeting_key_service.BatchActivateCustomTargetingKeysResponse()
            )
            pb_resp = custom_targeting_key_service.BatchActivateCustomTargetingKeysResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_activate_custom_targeting_keys(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_activate_custom_targeting_keys_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = custom_targeting_key_service.BatchActivateCustomTargetingKeysResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.CustomTargetingKeyServiceClient.batch_activate_custom_targeting_keys",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomTargetingKeyService",
                        "rpcName": "BatchActivateCustomTargetingKeys",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchCreateCustomTargetingKeys(
        _BaseCustomTargetingKeyServiceRestTransport._BaseBatchCreateCustomTargetingKeys,
        CustomTargetingKeyServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "CustomTargetingKeyServiceRestTransport.BatchCreateCustomTargetingKeys"
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
            request: custom_targeting_key_service.BatchCreateCustomTargetingKeysRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> custom_targeting_key_service.BatchCreateCustomTargetingKeysResponse:
            r"""Call the batch create custom
            targeting keys method over HTTP.

                Args:
                    request (~.custom_targeting_key_service.BatchCreateCustomTargetingKeysRequest):
                        The request object. Request object for ``BatchCreateCustomTargetingKeys``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.custom_targeting_key_service.BatchCreateCustomTargetingKeysResponse:
                        Response object for ``BatchCreateCustomTargetingKeys``
                    method.

            """

            http_options = _BaseCustomTargetingKeyServiceRestTransport._BaseBatchCreateCustomTargetingKeys._get_http_options()
            request, metadata = (
                self._interceptor.pre_batch_create_custom_targeting_keys(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCustomTargetingKeyServiceRestTransport._BaseBatchCreateCustomTargetingKeys,
                    "_BaseBatchCreateCustomTargetingKeys__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CustomTargetingKeyServiceClient.BatchCreateCustomTargetingKeys",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomTargetingKeyService",
                        "rpcName": "BatchCreateCustomTargetingKeys",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CustomTargetingKeyServiceRestTransport._BatchCreateCustomTargetingKeys._get_response(
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
            resp = custom_targeting_key_service.BatchCreateCustomTargetingKeysResponse()
            pb_resp = (
                custom_targeting_key_service.BatchCreateCustomTargetingKeysResponse.pb(
                    resp
                )
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_create_custom_targeting_keys(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_create_custom_targeting_keys_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = custom_targeting_key_service.BatchCreateCustomTargetingKeysResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.CustomTargetingKeyServiceClient.batch_create_custom_targeting_keys",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomTargetingKeyService",
                        "rpcName": "BatchCreateCustomTargetingKeys",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchDeactivateCustomTargetingKeys(
        _BaseCustomTargetingKeyServiceRestTransport._BaseBatchDeactivateCustomTargetingKeys,
        CustomTargetingKeyServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "CustomTargetingKeyServiceRestTransport.BatchDeactivateCustomTargetingKeys"
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
            request: custom_targeting_key_service.BatchDeactivateCustomTargetingKeysRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> custom_targeting_key_service.BatchDeactivateCustomTargetingKeysResponse:
            r"""Call the batch deactivate custom
            targeting keys method over HTTP.

                Args:
                    request (~.custom_targeting_key_service.BatchDeactivateCustomTargetingKeysRequest):
                        The request object. Request message for
                    ``BatchDeactivateCustomTargetingKeys`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.custom_targeting_key_service.BatchDeactivateCustomTargetingKeysResponse:
                        Response object for
                    ``BatchDeactivateCustomTargetingKeys`` method.

            """

            http_options = _BaseCustomTargetingKeyServiceRestTransport._BaseBatchDeactivateCustomTargetingKeys._get_http_options()
            request, metadata = (
                self._interceptor.pre_batch_deactivate_custom_targeting_keys(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCustomTargetingKeyServiceRestTransport._BaseBatchDeactivateCustomTargetingKeys,
                    "_BaseBatchDeactivateCustomTargetingKeys__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CustomTargetingKeyServiceClient.BatchDeactivateCustomTargetingKeys",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomTargetingKeyService",
                        "rpcName": "BatchDeactivateCustomTargetingKeys",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CustomTargetingKeyServiceRestTransport._BatchDeactivateCustomTargetingKeys._get_response(
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
            resp = custom_targeting_key_service.BatchDeactivateCustomTargetingKeysResponse()
            pb_resp = custom_targeting_key_service.BatchDeactivateCustomTargetingKeysResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_deactivate_custom_targeting_keys(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_deactivate_custom_targeting_keys_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = custom_targeting_key_service.BatchDeactivateCustomTargetingKeysResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.CustomTargetingKeyServiceClient.batch_deactivate_custom_targeting_keys",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomTargetingKeyService",
                        "rpcName": "BatchDeactivateCustomTargetingKeys",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchUpdateCustomTargetingKeys(
        _BaseCustomTargetingKeyServiceRestTransport._BaseBatchUpdateCustomTargetingKeys,
        CustomTargetingKeyServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "CustomTargetingKeyServiceRestTransport.BatchUpdateCustomTargetingKeys"
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
            request: custom_targeting_key_service.BatchUpdateCustomTargetingKeysRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> custom_targeting_key_service.BatchUpdateCustomTargetingKeysResponse:
            r"""Call the batch update custom
            targeting keys method over HTTP.

                Args:
                    request (~.custom_targeting_key_service.BatchUpdateCustomTargetingKeysRequest):
                        The request object. Request object for ``BatchUpdateCustomTargetingKeys``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.custom_targeting_key_service.BatchUpdateCustomTargetingKeysResponse:
                        Response object for ``BatchUpdateCustomTargetingKeys``
                    method.

            """

            http_options = _BaseCustomTargetingKeyServiceRestTransport._BaseBatchUpdateCustomTargetingKeys._get_http_options()
            request, metadata = (
                self._interceptor.pre_batch_update_custom_targeting_keys(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCustomTargetingKeyServiceRestTransport._BaseBatchUpdateCustomTargetingKeys,
                    "_BaseBatchUpdateCustomTargetingKeys__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CustomTargetingKeyServiceClient.BatchUpdateCustomTargetingKeys",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomTargetingKeyService",
                        "rpcName": "BatchUpdateCustomTargetingKeys",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CustomTargetingKeyServiceRestTransport._BatchUpdateCustomTargetingKeys._get_response(
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
            resp = custom_targeting_key_service.BatchUpdateCustomTargetingKeysResponse()
            pb_resp = (
                custom_targeting_key_service.BatchUpdateCustomTargetingKeysResponse.pb(
                    resp
                )
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_update_custom_targeting_keys(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_update_custom_targeting_keys_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = custom_targeting_key_service.BatchUpdateCustomTargetingKeysResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.CustomTargetingKeyServiceClient.batch_update_custom_targeting_keys",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomTargetingKeyService",
                        "rpcName": "BatchUpdateCustomTargetingKeys",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateCustomTargetingKey(
        _BaseCustomTargetingKeyServiceRestTransport._BaseCreateCustomTargetingKey,
        CustomTargetingKeyServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "CustomTargetingKeyServiceRestTransport.CreateCustomTargetingKey"
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
            request: custom_targeting_key_service.CreateCustomTargetingKeyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> custom_targeting_key_messages.CustomTargetingKey:
            r"""Call the create custom targeting
            key method over HTTP.

                Args:
                    request (~.custom_targeting_key_service.CreateCustomTargetingKeyRequest):
                        The request object. Request object for ``CreateCustomTargetingKey`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.custom_targeting_key_messages.CustomTargetingKey:
                        The ``CustomTargetingKey`` resource.
            """

            http_options = _BaseCustomTargetingKeyServiceRestTransport._BaseCreateCustomTargetingKey._get_http_options()
            request, metadata = self._interceptor.pre_create_custom_targeting_key(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCustomTargetingKeyServiceRestTransport._BaseCreateCustomTargetingKey,
                    "_BaseCreateCustomTargetingKey__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CustomTargetingKeyServiceClient.CreateCustomTargetingKey",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomTargetingKeyService",
                        "rpcName": "CreateCustomTargetingKey",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CustomTargetingKeyServiceRestTransport._CreateCustomTargetingKey._get_response(
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
            resp = custom_targeting_key_messages.CustomTargetingKey()
            pb_resp = custom_targeting_key_messages.CustomTargetingKey.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_custom_targeting_key(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_custom_targeting_key_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        custom_targeting_key_messages.CustomTargetingKey.to_json(
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
                    "Received response for google.ads.admanager_v1.CustomTargetingKeyServiceClient.create_custom_targeting_key",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomTargetingKeyService",
                        "rpcName": "CreateCustomTargetingKey",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetCustomTargetingKey(
        _BaseCustomTargetingKeyServiceRestTransport._BaseGetCustomTargetingKey,
        CustomTargetingKeyServiceRestStub,
    ):
        def __hash__(self):
            return hash("CustomTargetingKeyServiceRestTransport.GetCustomTargetingKey")

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
            request: custom_targeting_key_service.GetCustomTargetingKeyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> custom_targeting_key_messages.CustomTargetingKey:
            r"""Call the get custom targeting key method over HTTP.

            Args:
                request (~.custom_targeting_key_service.GetCustomTargetingKeyRequest):
                    The request object. Request object for ``GetCustomTargetingKey`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.custom_targeting_key_messages.CustomTargetingKey:
                    The ``CustomTargetingKey`` resource.
            """

            http_options = _BaseCustomTargetingKeyServiceRestTransport._BaseGetCustomTargetingKey._get_http_options()
            request, metadata = self._interceptor.pre_get_custom_targeting_key(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCustomTargetingKeyServiceRestTransport._BaseGetCustomTargetingKey,
                    "_BaseGetCustomTargetingKey__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CustomTargetingKeyServiceClient.GetCustomTargetingKey",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomTargetingKeyService",
                        "rpcName": "GetCustomTargetingKey",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CustomTargetingKeyServiceRestTransport._GetCustomTargetingKey._get_response(
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
            resp = custom_targeting_key_messages.CustomTargetingKey()
            pb_resp = custom_targeting_key_messages.CustomTargetingKey.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_custom_targeting_key(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_custom_targeting_key_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        custom_targeting_key_messages.CustomTargetingKey.to_json(
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
                    "Received response for google.ads.admanager_v1.CustomTargetingKeyServiceClient.get_custom_targeting_key",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomTargetingKeyService",
                        "rpcName": "GetCustomTargetingKey",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListCustomTargetingKeys(
        _BaseCustomTargetingKeyServiceRestTransport._BaseListCustomTargetingKeys,
        CustomTargetingKeyServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "CustomTargetingKeyServiceRestTransport.ListCustomTargetingKeys"
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
            request: custom_targeting_key_service.ListCustomTargetingKeysRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> custom_targeting_key_service.ListCustomTargetingKeysResponse:
            r"""Call the list custom targeting
            keys method over HTTP.

                Args:
                    request (~.custom_targeting_key_service.ListCustomTargetingKeysRequest):
                        The request object. Request object for ``ListCustomTargetingKeys`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.custom_targeting_key_service.ListCustomTargetingKeysResponse:
                        Response object for ``ListCustomTargetingKeysRequest``
                    containing matching ``CustomTargetingKey`` objects.

            """

            http_options = _BaseCustomTargetingKeyServiceRestTransport._BaseListCustomTargetingKeys._get_http_options()
            request, metadata = self._interceptor.pre_list_custom_targeting_keys(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCustomTargetingKeyServiceRestTransport._BaseListCustomTargetingKeys,
                    "_BaseListCustomTargetingKeys__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CustomTargetingKeyServiceClient.ListCustomTargetingKeys",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomTargetingKeyService",
                        "rpcName": "ListCustomTargetingKeys",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CustomTargetingKeyServiceRestTransport._ListCustomTargetingKeys._get_response(
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
            resp = custom_targeting_key_service.ListCustomTargetingKeysResponse()
            pb_resp = custom_targeting_key_service.ListCustomTargetingKeysResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_custom_targeting_keys(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_custom_targeting_keys_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = custom_targeting_key_service.ListCustomTargetingKeysResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.CustomTargetingKeyServiceClient.list_custom_targeting_keys",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomTargetingKeyService",
                        "rpcName": "ListCustomTargetingKeys",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateCustomTargetingKey(
        _BaseCustomTargetingKeyServiceRestTransport._BaseUpdateCustomTargetingKey,
        CustomTargetingKeyServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "CustomTargetingKeyServiceRestTransport.UpdateCustomTargetingKey"
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
            request: custom_targeting_key_service.UpdateCustomTargetingKeyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> custom_targeting_key_messages.CustomTargetingKey:
            r"""Call the update custom targeting
            key method over HTTP.

                Args:
                    request (~.custom_targeting_key_service.UpdateCustomTargetingKeyRequest):
                        The request object. Request object for ``UpdateCustomTargetingKey`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.custom_targeting_key_messages.CustomTargetingKey:
                        The ``CustomTargetingKey`` resource.
            """

            http_options = _BaseCustomTargetingKeyServiceRestTransport._BaseUpdateCustomTargetingKey._get_http_options()
            request, metadata = self._interceptor.pre_update_custom_targeting_key(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCustomTargetingKeyServiceRestTransport._BaseUpdateCustomTargetingKey,
                    "_BaseUpdateCustomTargetingKey__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CustomTargetingKeyServiceClient.UpdateCustomTargetingKey",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomTargetingKeyService",
                        "rpcName": "UpdateCustomTargetingKey",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CustomTargetingKeyServiceRestTransport._UpdateCustomTargetingKey._get_response(
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
            resp = custom_targeting_key_messages.CustomTargetingKey()
            pb_resp = custom_targeting_key_messages.CustomTargetingKey.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_custom_targeting_key(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_custom_targeting_key_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        custom_targeting_key_messages.CustomTargetingKey.to_json(
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
                    "Received response for google.ads.admanager_v1.CustomTargetingKeyServiceClient.update_custom_targeting_key",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomTargetingKeyService",
                        "rpcName": "UpdateCustomTargetingKey",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_activate_custom_targeting_keys(
        self,
    ) -> Callable[
        [custom_targeting_key_service.BatchActivateCustomTargetingKeysRequest],
        custom_targeting_key_service.BatchActivateCustomTargetingKeysResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchActivateCustomTargetingKeys(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_create_custom_targeting_keys(
        self,
    ) -> Callable[
        [custom_targeting_key_service.BatchCreateCustomTargetingKeysRequest],
        custom_targeting_key_service.BatchCreateCustomTargetingKeysResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchCreateCustomTargetingKeys(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_deactivate_custom_targeting_keys(
        self,
    ) -> Callable[
        [custom_targeting_key_service.BatchDeactivateCustomTargetingKeysRequest],
        custom_targeting_key_service.BatchDeactivateCustomTargetingKeysResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchDeactivateCustomTargetingKeys(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_update_custom_targeting_keys(
        self,
    ) -> Callable[
        [custom_targeting_key_service.BatchUpdateCustomTargetingKeysRequest],
        custom_targeting_key_service.BatchUpdateCustomTargetingKeysResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchUpdateCustomTargetingKeys(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_custom_targeting_key(
        self,
    ) -> Callable[
        [custom_targeting_key_service.CreateCustomTargetingKeyRequest],
        custom_targeting_key_messages.CustomTargetingKey,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateCustomTargetingKey(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_custom_targeting_key(
        self,
    ) -> Callable[
        [custom_targeting_key_service.GetCustomTargetingKeyRequest],
        custom_targeting_key_messages.CustomTargetingKey,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetCustomTargetingKey(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_custom_targeting_keys(
        self,
    ) -> Callable[
        [custom_targeting_key_service.ListCustomTargetingKeysRequest],
        custom_targeting_key_service.ListCustomTargetingKeysResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListCustomTargetingKeys(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_custom_targeting_key(
        self,
    ) -> Callable[
        [custom_targeting_key_service.UpdateCustomTargetingKeyRequest],
        custom_targeting_key_messages.CustomTargetingKey,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateCustomTargetingKey(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseCustomTargetingKeyServiceRestTransport._BaseCancelOperation,
        CustomTargetingKeyServiceRestStub,
    ):
        def __hash__(self):
            return hash("CustomTargetingKeyServiceRestTransport.CancelOperation")

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

            http_options = _BaseCustomTargetingKeyServiceRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCustomTargetingKeyServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.ads.admanager_v1.CustomTargetingKeyServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomTargetingKeyService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CustomTargetingKeyServiceRestTransport._CancelOperation._get_response(
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
        _BaseCustomTargetingKeyServiceRestTransport._BaseGetOperation,
        CustomTargetingKeyServiceRestStub,
    ):
        def __hash__(self):
            return hash("CustomTargetingKeyServiceRestTransport.GetOperation")

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

            http_options = _BaseCustomTargetingKeyServiceRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCustomTargetingKeyServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.ads.admanager_v1.CustomTargetingKeyServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomTargetingKeyService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CustomTargetingKeyServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.ads.admanager_v1.CustomTargetingKeyServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CustomTargetingKeyService",
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


__all__ = ("CustomTargetingKeyServiceRestTransport",)
