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
    dai_authentication_key_messages,
    dai_authentication_key_service,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseDaiAuthenticationKeyServiceRestTransport

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


class DaiAuthenticationKeyServiceRestInterceptor:
    """Interceptor for DaiAuthenticationKeyService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the DaiAuthenticationKeyServiceRestTransport.

    .. code-block:: python
        class MyCustomDaiAuthenticationKeyServiceInterceptor(DaiAuthenticationKeyServiceRestInterceptor):
            def pre_batch_activate_dai_authentication_keys(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_activate_dai_authentication_keys(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_create_dai_authentication_keys(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_create_dai_authentication_keys(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_deactivate_dai_authentication_keys(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_deactivate_dai_authentication_keys(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_update_dai_authentication_keys(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_update_dai_authentication_keys(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_dai_authentication_key(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_dai_authentication_key(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_dai_authentication_key(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_dai_authentication_key(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_dai_authentication_keys(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_dai_authentication_keys(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_dai_authentication_key(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_dai_authentication_key(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = DaiAuthenticationKeyServiceRestTransport(interceptor=MyCustomDaiAuthenticationKeyServiceInterceptor())
        client = DaiAuthenticationKeyServiceClient(transport=transport)


    """

    def pre_batch_activate_dai_authentication_keys(
        self,
        request: dai_authentication_key_service.BatchActivateDaiAuthenticationKeysRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dai_authentication_key_service.BatchActivateDaiAuthenticationKeysRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_activate_dai_authentication_keys

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DaiAuthenticationKeyService server.
        """
        return request, metadata

    def post_batch_activate_dai_authentication_keys(
        self,
        response: dai_authentication_key_service.BatchActivateDaiAuthenticationKeysResponse,
    ) -> dai_authentication_key_service.BatchActivateDaiAuthenticationKeysResponse:
        """Post-rpc interceptor for batch_activate_dai_authentication_keys

        DEPRECATED. Please use the `post_batch_activate_dai_authentication_keys_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DaiAuthenticationKeyService server but before
        it is returned to user code. This `post_batch_activate_dai_authentication_keys` interceptor runs
        before the `post_batch_activate_dai_authentication_keys_with_metadata` interceptor.
        """
        return response

    def post_batch_activate_dai_authentication_keys_with_metadata(
        self,
        response: dai_authentication_key_service.BatchActivateDaiAuthenticationKeysResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dai_authentication_key_service.BatchActivateDaiAuthenticationKeysResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_activate_dai_authentication_keys

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DaiAuthenticationKeyService server but before it is returned to user code.

        We recommend only using this `post_batch_activate_dai_authentication_keys_with_metadata`
        interceptor in new development instead of the `post_batch_activate_dai_authentication_keys` interceptor.
        When both interceptors are used, this `post_batch_activate_dai_authentication_keys_with_metadata` interceptor runs after the
        `post_batch_activate_dai_authentication_keys` interceptor. The (possibly modified) response returned by
        `post_batch_activate_dai_authentication_keys` will be passed to
        `post_batch_activate_dai_authentication_keys_with_metadata`.
        """
        return response, metadata

    def pre_batch_create_dai_authentication_keys(
        self,
        request: dai_authentication_key_service.BatchCreateDaiAuthenticationKeysRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dai_authentication_key_service.BatchCreateDaiAuthenticationKeysRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_create_dai_authentication_keys

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DaiAuthenticationKeyService server.
        """
        return request, metadata

    def post_batch_create_dai_authentication_keys(
        self,
        response: dai_authentication_key_service.BatchCreateDaiAuthenticationKeysResponse,
    ) -> dai_authentication_key_service.BatchCreateDaiAuthenticationKeysResponse:
        """Post-rpc interceptor for batch_create_dai_authentication_keys

        DEPRECATED. Please use the `post_batch_create_dai_authentication_keys_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DaiAuthenticationKeyService server but before
        it is returned to user code. This `post_batch_create_dai_authentication_keys` interceptor runs
        before the `post_batch_create_dai_authentication_keys_with_metadata` interceptor.
        """
        return response

    def post_batch_create_dai_authentication_keys_with_metadata(
        self,
        response: dai_authentication_key_service.BatchCreateDaiAuthenticationKeysResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dai_authentication_key_service.BatchCreateDaiAuthenticationKeysResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_create_dai_authentication_keys

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DaiAuthenticationKeyService server but before it is returned to user code.

        We recommend only using this `post_batch_create_dai_authentication_keys_with_metadata`
        interceptor in new development instead of the `post_batch_create_dai_authentication_keys` interceptor.
        When both interceptors are used, this `post_batch_create_dai_authentication_keys_with_metadata` interceptor runs after the
        `post_batch_create_dai_authentication_keys` interceptor. The (possibly modified) response returned by
        `post_batch_create_dai_authentication_keys` will be passed to
        `post_batch_create_dai_authentication_keys_with_metadata`.
        """
        return response, metadata

    def pre_batch_deactivate_dai_authentication_keys(
        self,
        request: dai_authentication_key_service.BatchDeactivateDaiAuthenticationKeysRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dai_authentication_key_service.BatchDeactivateDaiAuthenticationKeysRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_deactivate_dai_authentication_keys

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DaiAuthenticationKeyService server.
        """
        return request, metadata

    def post_batch_deactivate_dai_authentication_keys(
        self,
        response: dai_authentication_key_service.BatchDeactivateDaiAuthenticationKeysResponse,
    ) -> dai_authentication_key_service.BatchDeactivateDaiAuthenticationKeysResponse:
        """Post-rpc interceptor for batch_deactivate_dai_authentication_keys

        DEPRECATED. Please use the `post_batch_deactivate_dai_authentication_keys_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DaiAuthenticationKeyService server but before
        it is returned to user code. This `post_batch_deactivate_dai_authentication_keys` interceptor runs
        before the `post_batch_deactivate_dai_authentication_keys_with_metadata` interceptor.
        """
        return response

    def post_batch_deactivate_dai_authentication_keys_with_metadata(
        self,
        response: dai_authentication_key_service.BatchDeactivateDaiAuthenticationKeysResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dai_authentication_key_service.BatchDeactivateDaiAuthenticationKeysResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_deactivate_dai_authentication_keys

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DaiAuthenticationKeyService server but before it is returned to user code.

        We recommend only using this `post_batch_deactivate_dai_authentication_keys_with_metadata`
        interceptor in new development instead of the `post_batch_deactivate_dai_authentication_keys` interceptor.
        When both interceptors are used, this `post_batch_deactivate_dai_authentication_keys_with_metadata` interceptor runs after the
        `post_batch_deactivate_dai_authentication_keys` interceptor. The (possibly modified) response returned by
        `post_batch_deactivate_dai_authentication_keys` will be passed to
        `post_batch_deactivate_dai_authentication_keys_with_metadata`.
        """
        return response, metadata

    def pre_batch_update_dai_authentication_keys(
        self,
        request: dai_authentication_key_service.BatchUpdateDaiAuthenticationKeysRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dai_authentication_key_service.BatchUpdateDaiAuthenticationKeysRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_update_dai_authentication_keys

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DaiAuthenticationKeyService server.
        """
        return request, metadata

    def post_batch_update_dai_authentication_keys(
        self,
        response: dai_authentication_key_service.BatchUpdateDaiAuthenticationKeysResponse,
    ) -> dai_authentication_key_service.BatchUpdateDaiAuthenticationKeysResponse:
        """Post-rpc interceptor for batch_update_dai_authentication_keys

        DEPRECATED. Please use the `post_batch_update_dai_authentication_keys_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DaiAuthenticationKeyService server but before
        it is returned to user code. This `post_batch_update_dai_authentication_keys` interceptor runs
        before the `post_batch_update_dai_authentication_keys_with_metadata` interceptor.
        """
        return response

    def post_batch_update_dai_authentication_keys_with_metadata(
        self,
        response: dai_authentication_key_service.BatchUpdateDaiAuthenticationKeysResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dai_authentication_key_service.BatchUpdateDaiAuthenticationKeysResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_update_dai_authentication_keys

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DaiAuthenticationKeyService server but before it is returned to user code.

        We recommend only using this `post_batch_update_dai_authentication_keys_with_metadata`
        interceptor in new development instead of the `post_batch_update_dai_authentication_keys` interceptor.
        When both interceptors are used, this `post_batch_update_dai_authentication_keys_with_metadata` interceptor runs after the
        `post_batch_update_dai_authentication_keys` interceptor. The (possibly modified) response returned by
        `post_batch_update_dai_authentication_keys` will be passed to
        `post_batch_update_dai_authentication_keys_with_metadata`.
        """
        return response, metadata

    def pre_create_dai_authentication_key(
        self,
        request: dai_authentication_key_service.CreateDaiAuthenticationKeyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dai_authentication_key_service.CreateDaiAuthenticationKeyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_dai_authentication_key

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DaiAuthenticationKeyService server.
        """
        return request, metadata

    def post_create_dai_authentication_key(
        self, response: dai_authentication_key_messages.DaiAuthenticationKey
    ) -> dai_authentication_key_messages.DaiAuthenticationKey:
        """Post-rpc interceptor for create_dai_authentication_key

        DEPRECATED. Please use the `post_create_dai_authentication_key_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DaiAuthenticationKeyService server but before
        it is returned to user code. This `post_create_dai_authentication_key` interceptor runs
        before the `post_create_dai_authentication_key_with_metadata` interceptor.
        """
        return response

    def post_create_dai_authentication_key_with_metadata(
        self,
        response: dai_authentication_key_messages.DaiAuthenticationKey,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dai_authentication_key_messages.DaiAuthenticationKey,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for create_dai_authentication_key

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DaiAuthenticationKeyService server but before it is returned to user code.

        We recommend only using this `post_create_dai_authentication_key_with_metadata`
        interceptor in new development instead of the `post_create_dai_authentication_key` interceptor.
        When both interceptors are used, this `post_create_dai_authentication_key_with_metadata` interceptor runs after the
        `post_create_dai_authentication_key` interceptor. The (possibly modified) response returned by
        `post_create_dai_authentication_key` will be passed to
        `post_create_dai_authentication_key_with_metadata`.
        """
        return response, metadata

    def pre_get_dai_authentication_key(
        self,
        request: dai_authentication_key_service.GetDaiAuthenticationKeyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dai_authentication_key_service.GetDaiAuthenticationKeyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_dai_authentication_key

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DaiAuthenticationKeyService server.
        """
        return request, metadata

    def post_get_dai_authentication_key(
        self, response: dai_authentication_key_messages.DaiAuthenticationKey
    ) -> dai_authentication_key_messages.DaiAuthenticationKey:
        """Post-rpc interceptor for get_dai_authentication_key

        DEPRECATED. Please use the `post_get_dai_authentication_key_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DaiAuthenticationKeyService server but before
        it is returned to user code. This `post_get_dai_authentication_key` interceptor runs
        before the `post_get_dai_authentication_key_with_metadata` interceptor.
        """
        return response

    def post_get_dai_authentication_key_with_metadata(
        self,
        response: dai_authentication_key_messages.DaiAuthenticationKey,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dai_authentication_key_messages.DaiAuthenticationKey,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_dai_authentication_key

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DaiAuthenticationKeyService server but before it is returned to user code.

        We recommend only using this `post_get_dai_authentication_key_with_metadata`
        interceptor in new development instead of the `post_get_dai_authentication_key` interceptor.
        When both interceptors are used, this `post_get_dai_authentication_key_with_metadata` interceptor runs after the
        `post_get_dai_authentication_key` interceptor. The (possibly modified) response returned by
        `post_get_dai_authentication_key` will be passed to
        `post_get_dai_authentication_key_with_metadata`.
        """
        return response, metadata

    def pre_list_dai_authentication_keys(
        self,
        request: dai_authentication_key_service.ListDaiAuthenticationKeysRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dai_authentication_key_service.ListDaiAuthenticationKeysRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_dai_authentication_keys

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DaiAuthenticationKeyService server.
        """
        return request, metadata

    def post_list_dai_authentication_keys(
        self, response: dai_authentication_key_service.ListDaiAuthenticationKeysResponse
    ) -> dai_authentication_key_service.ListDaiAuthenticationKeysResponse:
        """Post-rpc interceptor for list_dai_authentication_keys

        DEPRECATED. Please use the `post_list_dai_authentication_keys_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DaiAuthenticationKeyService server but before
        it is returned to user code. This `post_list_dai_authentication_keys` interceptor runs
        before the `post_list_dai_authentication_keys_with_metadata` interceptor.
        """
        return response

    def post_list_dai_authentication_keys_with_metadata(
        self,
        response: dai_authentication_key_service.ListDaiAuthenticationKeysResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dai_authentication_key_service.ListDaiAuthenticationKeysResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_dai_authentication_keys

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DaiAuthenticationKeyService server but before it is returned to user code.

        We recommend only using this `post_list_dai_authentication_keys_with_metadata`
        interceptor in new development instead of the `post_list_dai_authentication_keys` interceptor.
        When both interceptors are used, this `post_list_dai_authentication_keys_with_metadata` interceptor runs after the
        `post_list_dai_authentication_keys` interceptor. The (possibly modified) response returned by
        `post_list_dai_authentication_keys` will be passed to
        `post_list_dai_authentication_keys_with_metadata`.
        """
        return response, metadata

    def pre_update_dai_authentication_key(
        self,
        request: dai_authentication_key_service.UpdateDaiAuthenticationKeyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dai_authentication_key_service.UpdateDaiAuthenticationKeyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_dai_authentication_key

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DaiAuthenticationKeyService server.
        """
        return request, metadata

    def post_update_dai_authentication_key(
        self, response: dai_authentication_key_messages.DaiAuthenticationKey
    ) -> dai_authentication_key_messages.DaiAuthenticationKey:
        """Post-rpc interceptor for update_dai_authentication_key

        DEPRECATED. Please use the `post_update_dai_authentication_key_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DaiAuthenticationKeyService server but before
        it is returned to user code. This `post_update_dai_authentication_key` interceptor runs
        before the `post_update_dai_authentication_key_with_metadata` interceptor.
        """
        return response

    def post_update_dai_authentication_key_with_metadata(
        self,
        response: dai_authentication_key_messages.DaiAuthenticationKey,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dai_authentication_key_messages.DaiAuthenticationKey,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for update_dai_authentication_key

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DaiAuthenticationKeyService server but before it is returned to user code.

        We recommend only using this `post_update_dai_authentication_key_with_metadata`
        interceptor in new development instead of the `post_update_dai_authentication_key` interceptor.
        When both interceptors are used, this `post_update_dai_authentication_key_with_metadata` interceptor runs after the
        `post_update_dai_authentication_key` interceptor. The (possibly modified) response returned by
        `post_update_dai_authentication_key` will be passed to
        `post_update_dai_authentication_key_with_metadata`.
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
        before they are sent to the DaiAuthenticationKeyService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the DaiAuthenticationKeyService server but before
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
        before they are sent to the DaiAuthenticationKeyService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the DaiAuthenticationKeyService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class DaiAuthenticationKeyServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: DaiAuthenticationKeyServiceRestInterceptor


class DaiAuthenticationKeyServiceRestTransport(
    _BaseDaiAuthenticationKeyServiceRestTransport
):
    """REST backend synchronous transport for DaiAuthenticationKeyService.

    Provides methods for handling ``DaiAuthenticationKey`` objects.

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
        interceptor: Optional[DaiAuthenticationKeyServiceRestInterceptor] = None,
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
            interceptor (Optional[DaiAuthenticationKeyServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or DaiAuthenticationKeyServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _BatchActivateDaiAuthenticationKeys(
        _BaseDaiAuthenticationKeyServiceRestTransport._BaseBatchActivateDaiAuthenticationKeys,
        DaiAuthenticationKeyServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "DaiAuthenticationKeyServiceRestTransport.BatchActivateDaiAuthenticationKeys"
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
            request: dai_authentication_key_service.BatchActivateDaiAuthenticationKeysRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dai_authentication_key_service.BatchActivateDaiAuthenticationKeysResponse:
            r"""Call the batch activate dai
            authentication keys method over HTTP.

                Args:
                    request (~.dai_authentication_key_service.BatchActivateDaiAuthenticationKeysRequest):
                        The request object. Request object for
                    ``BatchPerformDaiAuthenticationKeyAction`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.dai_authentication_key_service.BatchActivateDaiAuthenticationKeysResponse:
                        Response object for
                    ``BatchActivateDaiAuthenticationKeys`` method.

            """

            http_options = _BaseDaiAuthenticationKeyServiceRestTransport._BaseBatchActivateDaiAuthenticationKeys._get_http_options()
            request, metadata = (
                self._interceptor.pre_batch_activate_dai_authentication_keys(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDaiAuthenticationKeyServiceRestTransport._BaseBatchActivateDaiAuthenticationKeys,
                    "_BaseBatchActivateDaiAuthenticationKeys__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.DaiAuthenticationKeyServiceClient.BatchActivateDaiAuthenticationKeys",
                    extra={
                        "serviceName": "google.ads.admanager.v1.DaiAuthenticationKeyService",
                        "rpcName": "BatchActivateDaiAuthenticationKeys",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DaiAuthenticationKeyServiceRestTransport._BatchActivateDaiAuthenticationKeys._get_response(
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
            resp = dai_authentication_key_service.BatchActivateDaiAuthenticationKeysResponse()
            pb_resp = dai_authentication_key_service.BatchActivateDaiAuthenticationKeysResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_activate_dai_authentication_keys(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_activate_dai_authentication_keys_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dai_authentication_key_service.BatchActivateDaiAuthenticationKeysResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.DaiAuthenticationKeyServiceClient.batch_activate_dai_authentication_keys",
                    extra={
                        "serviceName": "google.ads.admanager.v1.DaiAuthenticationKeyService",
                        "rpcName": "BatchActivateDaiAuthenticationKeys",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchCreateDaiAuthenticationKeys(
        _BaseDaiAuthenticationKeyServiceRestTransport._BaseBatchCreateDaiAuthenticationKeys,
        DaiAuthenticationKeyServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "DaiAuthenticationKeyServiceRestTransport.BatchCreateDaiAuthenticationKeys"
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
            request: dai_authentication_key_service.BatchCreateDaiAuthenticationKeysRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dai_authentication_key_service.BatchCreateDaiAuthenticationKeysResponse:
            r"""Call the batch create dai
            authentication keys method over HTTP.

                Args:
                    request (~.dai_authentication_key_service.BatchCreateDaiAuthenticationKeysRequest):
                        The request object. Request object for ``BatchCreateDaiAuthenticationKeys``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.dai_authentication_key_service.BatchCreateDaiAuthenticationKeysResponse:
                        Response object for ``BatchCreateDaiAuthenticationKeys``
                    method.

            """

            http_options = _BaseDaiAuthenticationKeyServiceRestTransport._BaseBatchCreateDaiAuthenticationKeys._get_http_options()
            request, metadata = (
                self._interceptor.pre_batch_create_dai_authentication_keys(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDaiAuthenticationKeyServiceRestTransport._BaseBatchCreateDaiAuthenticationKeys,
                    "_BaseBatchCreateDaiAuthenticationKeys__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.DaiAuthenticationKeyServiceClient.BatchCreateDaiAuthenticationKeys",
                    extra={
                        "serviceName": "google.ads.admanager.v1.DaiAuthenticationKeyService",
                        "rpcName": "BatchCreateDaiAuthenticationKeys",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DaiAuthenticationKeyServiceRestTransport._BatchCreateDaiAuthenticationKeys._get_response(
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
            resp = dai_authentication_key_service.BatchCreateDaiAuthenticationKeysResponse()
            pb_resp = dai_authentication_key_service.BatchCreateDaiAuthenticationKeysResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_create_dai_authentication_keys(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_create_dai_authentication_keys_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dai_authentication_key_service.BatchCreateDaiAuthenticationKeysResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.DaiAuthenticationKeyServiceClient.batch_create_dai_authentication_keys",
                    extra={
                        "serviceName": "google.ads.admanager.v1.DaiAuthenticationKeyService",
                        "rpcName": "BatchCreateDaiAuthenticationKeys",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchDeactivateDaiAuthenticationKeys(
        _BaseDaiAuthenticationKeyServiceRestTransport._BaseBatchDeactivateDaiAuthenticationKeys,
        DaiAuthenticationKeyServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "DaiAuthenticationKeyServiceRestTransport.BatchDeactivateDaiAuthenticationKeys"
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
            request: dai_authentication_key_service.BatchDeactivateDaiAuthenticationKeysRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> (
            dai_authentication_key_service.BatchDeactivateDaiAuthenticationKeysResponse
        ):
            r"""Call the batch deactivate dai
            authentication keys method over HTTP.

                Args:
                    request (~.dai_authentication_key_service.BatchDeactivateDaiAuthenticationKeysRequest):
                        The request object. Request object for
                    ``BatchPerformDaiAuthenticationKeyAction`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.dai_authentication_key_service.BatchDeactivateDaiAuthenticationKeysResponse:
                        Response object for
                    ``BatchDeactivateDaiAuthenticationKeys`` method.

            """

            http_options = _BaseDaiAuthenticationKeyServiceRestTransport._BaseBatchDeactivateDaiAuthenticationKeys._get_http_options()
            request, metadata = (
                self._interceptor.pre_batch_deactivate_dai_authentication_keys(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDaiAuthenticationKeyServiceRestTransport._BaseBatchDeactivateDaiAuthenticationKeys,
                    "_BaseBatchDeactivateDaiAuthenticationKeys__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.DaiAuthenticationKeyServiceClient.BatchDeactivateDaiAuthenticationKeys",
                    extra={
                        "serviceName": "google.ads.admanager.v1.DaiAuthenticationKeyService",
                        "rpcName": "BatchDeactivateDaiAuthenticationKeys",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DaiAuthenticationKeyServiceRestTransport._BatchDeactivateDaiAuthenticationKeys._get_response(
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
            resp = dai_authentication_key_service.BatchDeactivateDaiAuthenticationKeysResponse()
            pb_resp = dai_authentication_key_service.BatchDeactivateDaiAuthenticationKeysResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_deactivate_dai_authentication_keys(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_deactivate_dai_authentication_keys_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dai_authentication_key_service.BatchDeactivateDaiAuthenticationKeysResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.DaiAuthenticationKeyServiceClient.batch_deactivate_dai_authentication_keys",
                    extra={
                        "serviceName": "google.ads.admanager.v1.DaiAuthenticationKeyService",
                        "rpcName": "BatchDeactivateDaiAuthenticationKeys",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchUpdateDaiAuthenticationKeys(
        _BaseDaiAuthenticationKeyServiceRestTransport._BaseBatchUpdateDaiAuthenticationKeys,
        DaiAuthenticationKeyServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "DaiAuthenticationKeyServiceRestTransport.BatchUpdateDaiAuthenticationKeys"
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
            request: dai_authentication_key_service.BatchUpdateDaiAuthenticationKeysRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dai_authentication_key_service.BatchUpdateDaiAuthenticationKeysResponse:
            r"""Call the batch update dai
            authentication keys method over HTTP.

                Args:
                    request (~.dai_authentication_key_service.BatchUpdateDaiAuthenticationKeysRequest):
                        The request object. Request object for ``BatchUpdateDaiAuthenticationKeys``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.dai_authentication_key_service.BatchUpdateDaiAuthenticationKeysResponse:
                        Response object for ``BatchUpdateDaiAuthenticationKeys``
                    method.

            """

            http_options = _BaseDaiAuthenticationKeyServiceRestTransport._BaseBatchUpdateDaiAuthenticationKeys._get_http_options()
            request, metadata = (
                self._interceptor.pre_batch_update_dai_authentication_keys(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDaiAuthenticationKeyServiceRestTransport._BaseBatchUpdateDaiAuthenticationKeys,
                    "_BaseBatchUpdateDaiAuthenticationKeys__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.DaiAuthenticationKeyServiceClient.BatchUpdateDaiAuthenticationKeys",
                    extra={
                        "serviceName": "google.ads.admanager.v1.DaiAuthenticationKeyService",
                        "rpcName": "BatchUpdateDaiAuthenticationKeys",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DaiAuthenticationKeyServiceRestTransport._BatchUpdateDaiAuthenticationKeys._get_response(
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
            resp = dai_authentication_key_service.BatchUpdateDaiAuthenticationKeysResponse()
            pb_resp = dai_authentication_key_service.BatchUpdateDaiAuthenticationKeysResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_update_dai_authentication_keys(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_update_dai_authentication_keys_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dai_authentication_key_service.BatchUpdateDaiAuthenticationKeysResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.DaiAuthenticationKeyServiceClient.batch_update_dai_authentication_keys",
                    extra={
                        "serviceName": "google.ads.admanager.v1.DaiAuthenticationKeyService",
                        "rpcName": "BatchUpdateDaiAuthenticationKeys",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateDaiAuthenticationKey(
        _BaseDaiAuthenticationKeyServiceRestTransport._BaseCreateDaiAuthenticationKey,
        DaiAuthenticationKeyServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "DaiAuthenticationKeyServiceRestTransport.CreateDaiAuthenticationKey"
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
            request: dai_authentication_key_service.CreateDaiAuthenticationKeyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dai_authentication_key_messages.DaiAuthenticationKey:
            r"""Call the create dai authentication
            key method over HTTP.

                Args:
                    request (~.dai_authentication_key_service.CreateDaiAuthenticationKeyRequest):
                        The request object. Request object for ``CreateDaiAuthenticationKey``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.dai_authentication_key_messages.DaiAuthenticationKey:
                        A DaiAuthenticationKey is used to
                    authenticate stream requests to the IMA
                    SDK API.

            """

            http_options = _BaseDaiAuthenticationKeyServiceRestTransport._BaseCreateDaiAuthenticationKey._get_http_options()
            request, metadata = self._interceptor.pre_create_dai_authentication_key(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDaiAuthenticationKeyServiceRestTransport._BaseCreateDaiAuthenticationKey,
                    "_BaseCreateDaiAuthenticationKey__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.DaiAuthenticationKeyServiceClient.CreateDaiAuthenticationKey",
                    extra={
                        "serviceName": "google.ads.admanager.v1.DaiAuthenticationKeyService",
                        "rpcName": "CreateDaiAuthenticationKey",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DaiAuthenticationKeyServiceRestTransport._CreateDaiAuthenticationKey._get_response(
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
            resp = dai_authentication_key_messages.DaiAuthenticationKey()
            pb_resp = dai_authentication_key_messages.DaiAuthenticationKey.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_dai_authentication_key(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_create_dai_authentication_key_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        dai_authentication_key_messages.DaiAuthenticationKey.to_json(
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
                    "Received response for google.ads.admanager_v1.DaiAuthenticationKeyServiceClient.create_dai_authentication_key",
                    extra={
                        "serviceName": "google.ads.admanager.v1.DaiAuthenticationKeyService",
                        "rpcName": "CreateDaiAuthenticationKey",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDaiAuthenticationKey(
        _BaseDaiAuthenticationKeyServiceRestTransport._BaseGetDaiAuthenticationKey,
        DaiAuthenticationKeyServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "DaiAuthenticationKeyServiceRestTransport.GetDaiAuthenticationKey"
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
            request: dai_authentication_key_service.GetDaiAuthenticationKeyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dai_authentication_key_messages.DaiAuthenticationKey:
            r"""Call the get dai authentication
            key method over HTTP.

                Args:
                    request (~.dai_authentication_key_service.GetDaiAuthenticationKeyRequest):
                        The request object. Request object for ``GetDaiAuthenticationKey`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.dai_authentication_key_messages.DaiAuthenticationKey:
                        A DaiAuthenticationKey is used to
                    authenticate stream requests to the IMA
                    SDK API.

            """

            http_options = _BaseDaiAuthenticationKeyServiceRestTransport._BaseGetDaiAuthenticationKey._get_http_options()
            request, metadata = self._interceptor.pre_get_dai_authentication_key(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDaiAuthenticationKeyServiceRestTransport._BaseGetDaiAuthenticationKey,
                    "_BaseGetDaiAuthenticationKey__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.DaiAuthenticationKeyServiceClient.GetDaiAuthenticationKey",
                    extra={
                        "serviceName": "google.ads.admanager.v1.DaiAuthenticationKeyService",
                        "rpcName": "GetDaiAuthenticationKey",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DaiAuthenticationKeyServiceRestTransport._GetDaiAuthenticationKey._get_response(
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
            resp = dai_authentication_key_messages.DaiAuthenticationKey()
            pb_resp = dai_authentication_key_messages.DaiAuthenticationKey.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_dai_authentication_key(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_dai_authentication_key_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        dai_authentication_key_messages.DaiAuthenticationKey.to_json(
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
                    "Received response for google.ads.admanager_v1.DaiAuthenticationKeyServiceClient.get_dai_authentication_key",
                    extra={
                        "serviceName": "google.ads.admanager.v1.DaiAuthenticationKeyService",
                        "rpcName": "GetDaiAuthenticationKey",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDaiAuthenticationKeys(
        _BaseDaiAuthenticationKeyServiceRestTransport._BaseListDaiAuthenticationKeys,
        DaiAuthenticationKeyServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "DaiAuthenticationKeyServiceRestTransport.ListDaiAuthenticationKeys"
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
            request: dai_authentication_key_service.ListDaiAuthenticationKeysRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dai_authentication_key_service.ListDaiAuthenticationKeysResponse:
            r"""Call the list dai authentication
            keys method over HTTP.

                Args:
                    request (~.dai_authentication_key_service.ListDaiAuthenticationKeysRequest):
                        The request object. Request object for ``ListDaiAuthenticationKeys`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.dai_authentication_key_service.ListDaiAuthenticationKeysResponse:
                        Response object for ``ListDaiAuthenticationKeysRequest``
                    containing matching ``DaiAuthenticationKey`` objects.

            """

            http_options = _BaseDaiAuthenticationKeyServiceRestTransport._BaseListDaiAuthenticationKeys._get_http_options()
            request, metadata = self._interceptor.pre_list_dai_authentication_keys(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDaiAuthenticationKeyServiceRestTransport._BaseListDaiAuthenticationKeys,
                    "_BaseListDaiAuthenticationKeys__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.DaiAuthenticationKeyServiceClient.ListDaiAuthenticationKeys",
                    extra={
                        "serviceName": "google.ads.admanager.v1.DaiAuthenticationKeyService",
                        "rpcName": "ListDaiAuthenticationKeys",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DaiAuthenticationKeyServiceRestTransport._ListDaiAuthenticationKeys._get_response(
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
            resp = dai_authentication_key_service.ListDaiAuthenticationKeysResponse()
            pb_resp = (
                dai_authentication_key_service.ListDaiAuthenticationKeysResponse.pb(
                    resp
                )
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_dai_authentication_keys(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_dai_authentication_keys_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dai_authentication_key_service.ListDaiAuthenticationKeysResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.DaiAuthenticationKeyServiceClient.list_dai_authentication_keys",
                    extra={
                        "serviceName": "google.ads.admanager.v1.DaiAuthenticationKeyService",
                        "rpcName": "ListDaiAuthenticationKeys",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateDaiAuthenticationKey(
        _BaseDaiAuthenticationKeyServiceRestTransport._BaseUpdateDaiAuthenticationKey,
        DaiAuthenticationKeyServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "DaiAuthenticationKeyServiceRestTransport.UpdateDaiAuthenticationKey"
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
            request: dai_authentication_key_service.UpdateDaiAuthenticationKeyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dai_authentication_key_messages.DaiAuthenticationKey:
            r"""Call the update dai authentication
            key method over HTTP.

                Args:
                    request (~.dai_authentication_key_service.UpdateDaiAuthenticationKeyRequest):
                        The request object. Request object for ``UpdateDaiAuthenticationKey``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.dai_authentication_key_messages.DaiAuthenticationKey:
                        A DaiAuthenticationKey is used to
                    authenticate stream requests to the IMA
                    SDK API.

            """

            http_options = _BaseDaiAuthenticationKeyServiceRestTransport._BaseUpdateDaiAuthenticationKey._get_http_options()
            request, metadata = self._interceptor.pre_update_dai_authentication_key(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDaiAuthenticationKeyServiceRestTransport._BaseUpdateDaiAuthenticationKey,
                    "_BaseUpdateDaiAuthenticationKey__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.DaiAuthenticationKeyServiceClient.UpdateDaiAuthenticationKey",
                    extra={
                        "serviceName": "google.ads.admanager.v1.DaiAuthenticationKeyService",
                        "rpcName": "UpdateDaiAuthenticationKey",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DaiAuthenticationKeyServiceRestTransport._UpdateDaiAuthenticationKey._get_response(
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
            resp = dai_authentication_key_messages.DaiAuthenticationKey()
            pb_resp = dai_authentication_key_messages.DaiAuthenticationKey.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_dai_authentication_key(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_update_dai_authentication_key_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        dai_authentication_key_messages.DaiAuthenticationKey.to_json(
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
                    "Received response for google.ads.admanager_v1.DaiAuthenticationKeyServiceClient.update_dai_authentication_key",
                    extra={
                        "serviceName": "google.ads.admanager.v1.DaiAuthenticationKeyService",
                        "rpcName": "UpdateDaiAuthenticationKey",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_activate_dai_authentication_keys(
        self,
    ) -> Callable[
        [dai_authentication_key_service.BatchActivateDaiAuthenticationKeysRequest],
        dai_authentication_key_service.BatchActivateDaiAuthenticationKeysResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchActivateDaiAuthenticationKeys(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_create_dai_authentication_keys(
        self,
    ) -> Callable[
        [dai_authentication_key_service.BatchCreateDaiAuthenticationKeysRequest],
        dai_authentication_key_service.BatchCreateDaiAuthenticationKeysResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchCreateDaiAuthenticationKeys(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_deactivate_dai_authentication_keys(
        self,
    ) -> Callable[
        [dai_authentication_key_service.BatchDeactivateDaiAuthenticationKeysRequest],
        dai_authentication_key_service.BatchDeactivateDaiAuthenticationKeysResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchDeactivateDaiAuthenticationKeys(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_update_dai_authentication_keys(
        self,
    ) -> Callable[
        [dai_authentication_key_service.BatchUpdateDaiAuthenticationKeysRequest],
        dai_authentication_key_service.BatchUpdateDaiAuthenticationKeysResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchUpdateDaiAuthenticationKeys(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_dai_authentication_key(
        self,
    ) -> Callable[
        [dai_authentication_key_service.CreateDaiAuthenticationKeyRequest],
        dai_authentication_key_messages.DaiAuthenticationKey,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateDaiAuthenticationKey(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_dai_authentication_key(
        self,
    ) -> Callable[
        [dai_authentication_key_service.GetDaiAuthenticationKeyRequest],
        dai_authentication_key_messages.DaiAuthenticationKey,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDaiAuthenticationKey(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_dai_authentication_keys(
        self,
    ) -> Callable[
        [dai_authentication_key_service.ListDaiAuthenticationKeysRequest],
        dai_authentication_key_service.ListDaiAuthenticationKeysResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDaiAuthenticationKeys(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_dai_authentication_key(
        self,
    ) -> Callable[
        [dai_authentication_key_service.UpdateDaiAuthenticationKeyRequest],
        dai_authentication_key_messages.DaiAuthenticationKey,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateDaiAuthenticationKey(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseDaiAuthenticationKeyServiceRestTransport._BaseCancelOperation,
        DaiAuthenticationKeyServiceRestStub,
    ):
        def __hash__(self):
            return hash("DaiAuthenticationKeyServiceRestTransport.CancelOperation")

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

            http_options = _BaseDaiAuthenticationKeyServiceRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDaiAuthenticationKeyServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.ads.admanager_v1.DaiAuthenticationKeyServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.DaiAuthenticationKeyService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DaiAuthenticationKeyServiceRestTransport._CancelOperation._get_response(
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
        _BaseDaiAuthenticationKeyServiceRestTransport._BaseGetOperation,
        DaiAuthenticationKeyServiceRestStub,
    ):
        def __hash__(self):
            return hash("DaiAuthenticationKeyServiceRestTransport.GetOperation")

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

            http_options = _BaseDaiAuthenticationKeyServiceRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDaiAuthenticationKeyServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.ads.admanager_v1.DaiAuthenticationKeyServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.DaiAuthenticationKeyService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DaiAuthenticationKeyServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.ads.admanager_v1.DaiAuthenticationKeyServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.DaiAuthenticationKeyService",
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


__all__ = ("DaiAuthenticationKeyServiceRestTransport",)
