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
from google.ads.admanager_v1.types import cdn_config_messages, cdn_config_service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseCdnConfigServiceRestTransport

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


class CdnConfigServiceRestInterceptor:
    """Interceptor for CdnConfigService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the CdnConfigServiceRestTransport.

    .. code-block:: python
        class MyCustomCdnConfigServiceInterceptor(CdnConfigServiceRestInterceptor):
            def pre_batch_activate_cdn_configs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_activate_cdn_configs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_archive_cdn_configs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_archive_cdn_configs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_create_cdn_configs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_create_cdn_configs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_update_cdn_configs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_update_cdn_configs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_cdn_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_cdn_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_cdn_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_cdn_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_cdn_configs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_cdn_configs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_cdn_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_cdn_config(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = CdnConfigServiceRestTransport(interceptor=MyCustomCdnConfigServiceInterceptor())
        client = CdnConfigServiceClient(transport=transport)


    """

    def pre_batch_activate_cdn_configs(
        self,
        request: cdn_config_service.BatchActivateCdnConfigsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cdn_config_service.BatchActivateCdnConfigsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_activate_cdn_configs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CdnConfigService server.
        """
        return request, metadata

    def post_batch_activate_cdn_configs(
        self, response: cdn_config_service.BatchActivateCdnConfigsResponse
    ) -> cdn_config_service.BatchActivateCdnConfigsResponse:
        """Post-rpc interceptor for batch_activate_cdn_configs

        DEPRECATED. Please use the `post_batch_activate_cdn_configs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CdnConfigService server but before
        it is returned to user code. This `post_batch_activate_cdn_configs` interceptor runs
        before the `post_batch_activate_cdn_configs_with_metadata` interceptor.
        """
        return response

    def post_batch_activate_cdn_configs_with_metadata(
        self,
        response: cdn_config_service.BatchActivateCdnConfigsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cdn_config_service.BatchActivateCdnConfigsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_activate_cdn_configs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CdnConfigService server but before it is returned to user code.

        We recommend only using this `post_batch_activate_cdn_configs_with_metadata`
        interceptor in new development instead of the `post_batch_activate_cdn_configs` interceptor.
        When both interceptors are used, this `post_batch_activate_cdn_configs_with_metadata` interceptor runs after the
        `post_batch_activate_cdn_configs` interceptor. The (possibly modified) response returned by
        `post_batch_activate_cdn_configs` will be passed to
        `post_batch_activate_cdn_configs_with_metadata`.
        """
        return response, metadata

    def pre_batch_archive_cdn_configs(
        self,
        request: cdn_config_service.BatchArchiveCdnConfigsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cdn_config_service.BatchArchiveCdnConfigsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_archive_cdn_configs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CdnConfigService server.
        """
        return request, metadata

    def post_batch_archive_cdn_configs(
        self, response: cdn_config_service.BatchArchiveCdnConfigsResponse
    ) -> cdn_config_service.BatchArchiveCdnConfigsResponse:
        """Post-rpc interceptor for batch_archive_cdn_configs

        DEPRECATED. Please use the `post_batch_archive_cdn_configs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CdnConfigService server but before
        it is returned to user code. This `post_batch_archive_cdn_configs` interceptor runs
        before the `post_batch_archive_cdn_configs_with_metadata` interceptor.
        """
        return response

    def post_batch_archive_cdn_configs_with_metadata(
        self,
        response: cdn_config_service.BatchArchiveCdnConfigsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cdn_config_service.BatchArchiveCdnConfigsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_archive_cdn_configs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CdnConfigService server but before it is returned to user code.

        We recommend only using this `post_batch_archive_cdn_configs_with_metadata`
        interceptor in new development instead of the `post_batch_archive_cdn_configs` interceptor.
        When both interceptors are used, this `post_batch_archive_cdn_configs_with_metadata` interceptor runs after the
        `post_batch_archive_cdn_configs` interceptor. The (possibly modified) response returned by
        `post_batch_archive_cdn_configs` will be passed to
        `post_batch_archive_cdn_configs_with_metadata`.
        """
        return response, metadata

    def pre_batch_create_cdn_configs(
        self,
        request: cdn_config_service.BatchCreateCdnConfigsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cdn_config_service.BatchCreateCdnConfigsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_create_cdn_configs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CdnConfigService server.
        """
        return request, metadata

    def post_batch_create_cdn_configs(
        self, response: cdn_config_service.BatchCreateCdnConfigsResponse
    ) -> cdn_config_service.BatchCreateCdnConfigsResponse:
        """Post-rpc interceptor for batch_create_cdn_configs

        DEPRECATED. Please use the `post_batch_create_cdn_configs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CdnConfigService server but before
        it is returned to user code. This `post_batch_create_cdn_configs` interceptor runs
        before the `post_batch_create_cdn_configs_with_metadata` interceptor.
        """
        return response

    def post_batch_create_cdn_configs_with_metadata(
        self,
        response: cdn_config_service.BatchCreateCdnConfigsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cdn_config_service.BatchCreateCdnConfigsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_create_cdn_configs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CdnConfigService server but before it is returned to user code.

        We recommend only using this `post_batch_create_cdn_configs_with_metadata`
        interceptor in new development instead of the `post_batch_create_cdn_configs` interceptor.
        When both interceptors are used, this `post_batch_create_cdn_configs_with_metadata` interceptor runs after the
        `post_batch_create_cdn_configs` interceptor. The (possibly modified) response returned by
        `post_batch_create_cdn_configs` will be passed to
        `post_batch_create_cdn_configs_with_metadata`.
        """
        return response, metadata

    def pre_batch_update_cdn_configs(
        self,
        request: cdn_config_service.BatchUpdateCdnConfigsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cdn_config_service.BatchUpdateCdnConfigsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_update_cdn_configs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CdnConfigService server.
        """
        return request, metadata

    def post_batch_update_cdn_configs(
        self, response: cdn_config_service.BatchUpdateCdnConfigsResponse
    ) -> cdn_config_service.BatchUpdateCdnConfigsResponse:
        """Post-rpc interceptor for batch_update_cdn_configs

        DEPRECATED. Please use the `post_batch_update_cdn_configs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CdnConfigService server but before
        it is returned to user code. This `post_batch_update_cdn_configs` interceptor runs
        before the `post_batch_update_cdn_configs_with_metadata` interceptor.
        """
        return response

    def post_batch_update_cdn_configs_with_metadata(
        self,
        response: cdn_config_service.BatchUpdateCdnConfigsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cdn_config_service.BatchUpdateCdnConfigsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_update_cdn_configs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CdnConfigService server but before it is returned to user code.

        We recommend only using this `post_batch_update_cdn_configs_with_metadata`
        interceptor in new development instead of the `post_batch_update_cdn_configs` interceptor.
        When both interceptors are used, this `post_batch_update_cdn_configs_with_metadata` interceptor runs after the
        `post_batch_update_cdn_configs` interceptor. The (possibly modified) response returned by
        `post_batch_update_cdn_configs` will be passed to
        `post_batch_update_cdn_configs_with_metadata`.
        """
        return response, metadata

    def pre_create_cdn_config(
        self,
        request: cdn_config_service.CreateCdnConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cdn_config_service.CreateCdnConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_cdn_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CdnConfigService server.
        """
        return request, metadata

    def post_create_cdn_config(
        self, response: cdn_config_messages.CdnConfig
    ) -> cdn_config_messages.CdnConfig:
        """Post-rpc interceptor for create_cdn_config

        DEPRECATED. Please use the `post_create_cdn_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CdnConfigService server but before
        it is returned to user code. This `post_create_cdn_config` interceptor runs
        before the `post_create_cdn_config_with_metadata` interceptor.
        """
        return response

    def post_create_cdn_config_with_metadata(
        self,
        response: cdn_config_messages.CdnConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cdn_config_messages.CdnConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_cdn_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CdnConfigService server but before it is returned to user code.

        We recommend only using this `post_create_cdn_config_with_metadata`
        interceptor in new development instead of the `post_create_cdn_config` interceptor.
        When both interceptors are used, this `post_create_cdn_config_with_metadata` interceptor runs after the
        `post_create_cdn_config` interceptor. The (possibly modified) response returned by
        `post_create_cdn_config` will be passed to
        `post_create_cdn_config_with_metadata`.
        """
        return response, metadata

    def pre_get_cdn_config(
        self,
        request: cdn_config_service.GetCdnConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cdn_config_service.GetCdnConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_cdn_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CdnConfigService server.
        """
        return request, metadata

    def post_get_cdn_config(
        self, response: cdn_config_messages.CdnConfig
    ) -> cdn_config_messages.CdnConfig:
        """Post-rpc interceptor for get_cdn_config

        DEPRECATED. Please use the `post_get_cdn_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CdnConfigService server but before
        it is returned to user code. This `post_get_cdn_config` interceptor runs
        before the `post_get_cdn_config_with_metadata` interceptor.
        """
        return response

    def post_get_cdn_config_with_metadata(
        self,
        response: cdn_config_messages.CdnConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cdn_config_messages.CdnConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_cdn_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CdnConfigService server but before it is returned to user code.

        We recommend only using this `post_get_cdn_config_with_metadata`
        interceptor in new development instead of the `post_get_cdn_config` interceptor.
        When both interceptors are used, this `post_get_cdn_config_with_metadata` interceptor runs after the
        `post_get_cdn_config` interceptor. The (possibly modified) response returned by
        `post_get_cdn_config` will be passed to
        `post_get_cdn_config_with_metadata`.
        """
        return response, metadata

    def pre_list_cdn_configs(
        self,
        request: cdn_config_service.ListCdnConfigsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cdn_config_service.ListCdnConfigsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_cdn_configs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CdnConfigService server.
        """
        return request, metadata

    def post_list_cdn_configs(
        self, response: cdn_config_service.ListCdnConfigsResponse
    ) -> cdn_config_service.ListCdnConfigsResponse:
        """Post-rpc interceptor for list_cdn_configs

        DEPRECATED. Please use the `post_list_cdn_configs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CdnConfigService server but before
        it is returned to user code. This `post_list_cdn_configs` interceptor runs
        before the `post_list_cdn_configs_with_metadata` interceptor.
        """
        return response

    def post_list_cdn_configs_with_metadata(
        self,
        response: cdn_config_service.ListCdnConfigsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cdn_config_service.ListCdnConfigsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_cdn_configs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CdnConfigService server but before it is returned to user code.

        We recommend only using this `post_list_cdn_configs_with_metadata`
        interceptor in new development instead of the `post_list_cdn_configs` interceptor.
        When both interceptors are used, this `post_list_cdn_configs_with_metadata` interceptor runs after the
        `post_list_cdn_configs` interceptor. The (possibly modified) response returned by
        `post_list_cdn_configs` will be passed to
        `post_list_cdn_configs_with_metadata`.
        """
        return response, metadata

    def pre_update_cdn_config(
        self,
        request: cdn_config_service.UpdateCdnConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cdn_config_service.UpdateCdnConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_cdn_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CdnConfigService server.
        """
        return request, metadata

    def post_update_cdn_config(
        self, response: cdn_config_messages.CdnConfig
    ) -> cdn_config_messages.CdnConfig:
        """Post-rpc interceptor for update_cdn_config

        DEPRECATED. Please use the `post_update_cdn_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CdnConfigService server but before
        it is returned to user code. This `post_update_cdn_config` interceptor runs
        before the `post_update_cdn_config_with_metadata` interceptor.
        """
        return response

    def post_update_cdn_config_with_metadata(
        self,
        response: cdn_config_messages.CdnConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cdn_config_messages.CdnConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_cdn_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CdnConfigService server but before it is returned to user code.

        We recommend only using this `post_update_cdn_config_with_metadata`
        interceptor in new development instead of the `post_update_cdn_config` interceptor.
        When both interceptors are used, this `post_update_cdn_config_with_metadata` interceptor runs after the
        `post_update_cdn_config` interceptor. The (possibly modified) response returned by
        `post_update_cdn_config` will be passed to
        `post_update_cdn_config_with_metadata`.
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
        before they are sent to the CdnConfigService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the CdnConfigService server but before
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
        before they are sent to the CdnConfigService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the CdnConfigService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class CdnConfigServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: CdnConfigServiceRestInterceptor


class CdnConfigServiceRestTransport(_BaseCdnConfigServiceRestTransport):
    """REST backend synchronous transport for CdnConfigService.

    Provides methods for handling ``CdnConfig`` objects.

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
        interceptor: Optional[CdnConfigServiceRestInterceptor] = None,
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
            interceptor (Optional[CdnConfigServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or CdnConfigServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _BatchActivateCdnConfigs(
        _BaseCdnConfigServiceRestTransport._BaseBatchActivateCdnConfigs,
        CdnConfigServiceRestStub,
    ):
        def __hash__(self):
            return hash("CdnConfigServiceRestTransport.BatchActivateCdnConfigs")

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
            request: cdn_config_service.BatchActivateCdnConfigsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cdn_config_service.BatchActivateCdnConfigsResponse:
            r"""Call the batch activate cdn
            configs method over HTTP.

                Args:
                    request (~.cdn_config_service.BatchActivateCdnConfigsRequest):
                        The request object. Request message to activate ``CdnConfig`` objects.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.cdn_config_service.BatchActivateCdnConfigsResponse:
                        Response message for ``BatchActivateCdnConfigs`` method.
            """

            http_options = _BaseCdnConfigServiceRestTransport._BaseBatchActivateCdnConfigs._get_http_options()
            request, metadata = self._interceptor.pre_batch_activate_cdn_configs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCdnConfigServiceRestTransport._BaseBatchActivateCdnConfigs,
                    "_BaseBatchActivateCdnConfigs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CdnConfigServiceClient.BatchActivateCdnConfigs",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CdnConfigService",
                        "rpcName": "BatchActivateCdnConfigs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CdnConfigServiceRestTransport._BatchActivateCdnConfigs._get_response(
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
            resp = cdn_config_service.BatchActivateCdnConfigsResponse()
            pb_resp = cdn_config_service.BatchActivateCdnConfigsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_activate_cdn_configs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_activate_cdn_configs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        cdn_config_service.BatchActivateCdnConfigsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.CdnConfigServiceClient.batch_activate_cdn_configs",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CdnConfigService",
                        "rpcName": "BatchActivateCdnConfigs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchArchiveCdnConfigs(
        _BaseCdnConfigServiceRestTransport._BaseBatchArchiveCdnConfigs,
        CdnConfigServiceRestStub,
    ):
        def __hash__(self):
            return hash("CdnConfigServiceRestTransport.BatchArchiveCdnConfigs")

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
            request: cdn_config_service.BatchArchiveCdnConfigsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cdn_config_service.BatchArchiveCdnConfigsResponse:
            r"""Call the batch archive cdn configs method over HTTP.

            Args:
                request (~.cdn_config_service.BatchArchiveCdnConfigsRequest):
                    The request object. Request message to archive ``CdnConfig`` objects.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cdn_config_service.BatchArchiveCdnConfigsResponse:
                    Response object for ``BatchArchiveCdnConfigs`` method.
            """

            http_options = _BaseCdnConfigServiceRestTransport._BaseBatchArchiveCdnConfigs._get_http_options()
            request, metadata = self._interceptor.pre_batch_archive_cdn_configs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCdnConfigServiceRestTransport._BaseBatchArchiveCdnConfigs,
                    "_BaseBatchArchiveCdnConfigs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CdnConfigServiceClient.BatchArchiveCdnConfigs",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CdnConfigService",
                        "rpcName": "BatchArchiveCdnConfigs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CdnConfigServiceRestTransport._BatchArchiveCdnConfigs._get_response(
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
            resp = cdn_config_service.BatchArchiveCdnConfigsResponse()
            pb_resp = cdn_config_service.BatchArchiveCdnConfigsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_archive_cdn_configs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_archive_cdn_configs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        cdn_config_service.BatchArchiveCdnConfigsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.CdnConfigServiceClient.batch_archive_cdn_configs",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CdnConfigService",
                        "rpcName": "BatchArchiveCdnConfigs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchCreateCdnConfigs(
        _BaseCdnConfigServiceRestTransport._BaseBatchCreateCdnConfigs,
        CdnConfigServiceRestStub,
    ):
        def __hash__(self):
            return hash("CdnConfigServiceRestTransport.BatchCreateCdnConfigs")

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
            request: cdn_config_service.BatchCreateCdnConfigsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cdn_config_service.BatchCreateCdnConfigsResponse:
            r"""Call the batch create cdn configs method over HTTP.

            Args:
                request (~.cdn_config_service.BatchCreateCdnConfigsRequest):
                    The request object. Request object for ``BatchCreateCdnConfigs`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cdn_config_service.BatchCreateCdnConfigsResponse:
                    Response object for ``BatchCreateCdnConfigs`` method.
            """

            http_options = _BaseCdnConfigServiceRestTransport._BaseBatchCreateCdnConfigs._get_http_options()
            request, metadata = self._interceptor.pre_batch_create_cdn_configs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCdnConfigServiceRestTransport._BaseBatchCreateCdnConfigs,
                    "_BaseBatchCreateCdnConfigs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CdnConfigServiceClient.BatchCreateCdnConfigs",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CdnConfigService",
                        "rpcName": "BatchCreateCdnConfigs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CdnConfigServiceRestTransport._BatchCreateCdnConfigs._get_response(
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
            resp = cdn_config_service.BatchCreateCdnConfigsResponse()
            pb_resp = cdn_config_service.BatchCreateCdnConfigsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_create_cdn_configs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_create_cdn_configs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        cdn_config_service.BatchCreateCdnConfigsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.CdnConfigServiceClient.batch_create_cdn_configs",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CdnConfigService",
                        "rpcName": "BatchCreateCdnConfigs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchUpdateCdnConfigs(
        _BaseCdnConfigServiceRestTransport._BaseBatchUpdateCdnConfigs,
        CdnConfigServiceRestStub,
    ):
        def __hash__(self):
            return hash("CdnConfigServiceRestTransport.BatchUpdateCdnConfigs")

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
            request: cdn_config_service.BatchUpdateCdnConfigsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cdn_config_service.BatchUpdateCdnConfigsResponse:
            r"""Call the batch update cdn configs method over HTTP.

            Args:
                request (~.cdn_config_service.BatchUpdateCdnConfigsRequest):
                    The request object. Request object for ``BatchUpdateCdnConfigs`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cdn_config_service.BatchUpdateCdnConfigsResponse:
                    Response object for ``BatchUpdateCdnConfigs`` method.
            """

            http_options = _BaseCdnConfigServiceRestTransport._BaseBatchUpdateCdnConfigs._get_http_options()
            request, metadata = self._interceptor.pre_batch_update_cdn_configs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCdnConfigServiceRestTransport._BaseBatchUpdateCdnConfigs,
                    "_BaseBatchUpdateCdnConfigs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CdnConfigServiceClient.BatchUpdateCdnConfigs",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CdnConfigService",
                        "rpcName": "BatchUpdateCdnConfigs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CdnConfigServiceRestTransport._BatchUpdateCdnConfigs._get_response(
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
            resp = cdn_config_service.BatchUpdateCdnConfigsResponse()
            pb_resp = cdn_config_service.BatchUpdateCdnConfigsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_update_cdn_configs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_update_cdn_configs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        cdn_config_service.BatchUpdateCdnConfigsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.CdnConfigServiceClient.batch_update_cdn_configs",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CdnConfigService",
                        "rpcName": "BatchUpdateCdnConfigs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateCdnConfig(
        _BaseCdnConfigServiceRestTransport._BaseCreateCdnConfig,
        CdnConfigServiceRestStub,
    ):
        def __hash__(self):
            return hash("CdnConfigServiceRestTransport.CreateCdnConfig")

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
            request: cdn_config_service.CreateCdnConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cdn_config_messages.CdnConfig:
            r"""Call the create cdn config method over HTTP.

            Args:
                request (~.cdn_config_service.CreateCdnConfigRequest):
                    The request object. Request object for ``CreateCdnConfig`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cdn_config_messages.CdnConfig:
                    A CdnConfig encapsulates information
                about where and how to ingest and
                deliver content enabled for DAI (Dynamic
                Ad Insertion).

            """

            http_options = _BaseCdnConfigServiceRestTransport._BaseCreateCdnConfig._get_http_options()
            request, metadata = self._interceptor.pre_create_cdn_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCdnConfigServiceRestTransport._BaseCreateCdnConfig,
                    "_BaseCreateCdnConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CdnConfigServiceClient.CreateCdnConfig",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CdnConfigService",
                        "rpcName": "CreateCdnConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CdnConfigServiceRestTransport._CreateCdnConfig._get_response(
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
            resp = cdn_config_messages.CdnConfig()
            pb_resp = cdn_config_messages.CdnConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_cdn_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_cdn_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cdn_config_messages.CdnConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.CdnConfigServiceClient.create_cdn_config",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CdnConfigService",
                        "rpcName": "CreateCdnConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetCdnConfig(
        _BaseCdnConfigServiceRestTransport._BaseGetCdnConfig, CdnConfigServiceRestStub
    ):
        def __hash__(self):
            return hash("CdnConfigServiceRestTransport.GetCdnConfig")

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
            request: cdn_config_service.GetCdnConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cdn_config_messages.CdnConfig:
            r"""Call the get cdn config method over HTTP.

            Args:
                request (~.cdn_config_service.GetCdnConfigRequest):
                    The request object. Request object for ``GetCdnConfig`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cdn_config_messages.CdnConfig:
                    A CdnConfig encapsulates information
                about where and how to ingest and
                deliver content enabled for DAI (Dynamic
                Ad Insertion).

            """

            http_options = (
                _BaseCdnConfigServiceRestTransport._BaseGetCdnConfig._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_cdn_config(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCdnConfigServiceRestTransport._BaseGetCdnConfig,
                    "_BaseGetCdnConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CdnConfigServiceClient.GetCdnConfig",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CdnConfigService",
                        "rpcName": "GetCdnConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CdnConfigServiceRestTransport._GetCdnConfig._get_response(
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
            resp = cdn_config_messages.CdnConfig()
            pb_resp = cdn_config_messages.CdnConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_cdn_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_cdn_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cdn_config_messages.CdnConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.CdnConfigServiceClient.get_cdn_config",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CdnConfigService",
                        "rpcName": "GetCdnConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListCdnConfigs(
        _BaseCdnConfigServiceRestTransport._BaseListCdnConfigs, CdnConfigServiceRestStub
    ):
        def __hash__(self):
            return hash("CdnConfigServiceRestTransport.ListCdnConfigs")

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
            request: cdn_config_service.ListCdnConfigsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cdn_config_service.ListCdnConfigsResponse:
            r"""Call the list cdn configs method over HTTP.

            Args:
                request (~.cdn_config_service.ListCdnConfigsRequest):
                    The request object. Request object for ``ListCdnConfigs`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cdn_config_service.ListCdnConfigsResponse:
                    Response object for ``ListCdnConfigsRequest`` containing
                matching ``CdnConfig`` objects.

            """

            http_options = _BaseCdnConfigServiceRestTransport._BaseListCdnConfigs._get_http_options()
            request, metadata = self._interceptor.pre_list_cdn_configs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCdnConfigServiceRestTransport._BaseListCdnConfigs,
                    "_BaseListCdnConfigs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CdnConfigServiceClient.ListCdnConfigs",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CdnConfigService",
                        "rpcName": "ListCdnConfigs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CdnConfigServiceRestTransport._ListCdnConfigs._get_response(
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
            resp = cdn_config_service.ListCdnConfigsResponse()
            pb_resp = cdn_config_service.ListCdnConfigsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_cdn_configs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_cdn_configs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        cdn_config_service.ListCdnConfigsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.CdnConfigServiceClient.list_cdn_configs",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CdnConfigService",
                        "rpcName": "ListCdnConfigs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateCdnConfig(
        _BaseCdnConfigServiceRestTransport._BaseUpdateCdnConfig,
        CdnConfigServiceRestStub,
    ):
        def __hash__(self):
            return hash("CdnConfigServiceRestTransport.UpdateCdnConfig")

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
            request: cdn_config_service.UpdateCdnConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cdn_config_messages.CdnConfig:
            r"""Call the update cdn config method over HTTP.

            Args:
                request (~.cdn_config_service.UpdateCdnConfigRequest):
                    The request object. Request object for ``UpdateCdnConfig`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cdn_config_messages.CdnConfig:
                    A CdnConfig encapsulates information
                about where and how to ingest and
                deliver content enabled for DAI (Dynamic
                Ad Insertion).

            """

            http_options = _BaseCdnConfigServiceRestTransport._BaseUpdateCdnConfig._get_http_options()
            request, metadata = self._interceptor.pre_update_cdn_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCdnConfigServiceRestTransport._BaseUpdateCdnConfig,
                    "_BaseUpdateCdnConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CdnConfigServiceClient.UpdateCdnConfig",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CdnConfigService",
                        "rpcName": "UpdateCdnConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CdnConfigServiceRestTransport._UpdateCdnConfig._get_response(
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
            resp = cdn_config_messages.CdnConfig()
            pb_resp = cdn_config_messages.CdnConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_cdn_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_cdn_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cdn_config_messages.CdnConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.CdnConfigServiceClient.update_cdn_config",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CdnConfigService",
                        "rpcName": "UpdateCdnConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_activate_cdn_configs(
        self,
    ) -> Callable[
        [cdn_config_service.BatchActivateCdnConfigsRequest],
        cdn_config_service.BatchActivateCdnConfigsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchActivateCdnConfigs(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_archive_cdn_configs(
        self,
    ) -> Callable[
        [cdn_config_service.BatchArchiveCdnConfigsRequest],
        cdn_config_service.BatchArchiveCdnConfigsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchArchiveCdnConfigs(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_create_cdn_configs(
        self,
    ) -> Callable[
        [cdn_config_service.BatchCreateCdnConfigsRequest],
        cdn_config_service.BatchCreateCdnConfigsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchCreateCdnConfigs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_update_cdn_configs(
        self,
    ) -> Callable[
        [cdn_config_service.BatchUpdateCdnConfigsRequest],
        cdn_config_service.BatchUpdateCdnConfigsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchUpdateCdnConfigs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_cdn_config(
        self,
    ) -> Callable[
        [cdn_config_service.CreateCdnConfigRequest], cdn_config_messages.CdnConfig
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateCdnConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_cdn_config(
        self,
    ) -> Callable[
        [cdn_config_service.GetCdnConfigRequest], cdn_config_messages.CdnConfig
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetCdnConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_cdn_configs(
        self,
    ) -> Callable[
        [cdn_config_service.ListCdnConfigsRequest],
        cdn_config_service.ListCdnConfigsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListCdnConfigs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_cdn_config(
        self,
    ) -> Callable[
        [cdn_config_service.UpdateCdnConfigRequest], cdn_config_messages.CdnConfig
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateCdnConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseCdnConfigServiceRestTransport._BaseCancelOperation,
        CdnConfigServiceRestStub,
    ):
        def __hash__(self):
            return hash("CdnConfigServiceRestTransport.CancelOperation")

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

            http_options = _BaseCdnConfigServiceRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCdnConfigServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.ads.admanager_v1.CdnConfigServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CdnConfigService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CdnConfigServiceRestTransport._CancelOperation._get_response(
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

            return self._interceptor.post_cancel_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseCdnConfigServiceRestTransport._BaseGetOperation, CdnConfigServiceRestStub
    ):
        def __hash__(self):
            return hash("CdnConfigServiceRestTransport.GetOperation")

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
                _BaseCdnConfigServiceRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCdnConfigServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.ads.admanager_v1.CdnConfigServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CdnConfigService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CdnConfigServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.ads.admanager_v1.CdnConfigServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CdnConfigService",
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


__all__ = ("CdnConfigServiceRestTransport",)
