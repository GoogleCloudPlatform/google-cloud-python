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
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.iap_v1._compat import transcode_request
from google.cloud.iap_v1.types import service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseIdentityAwareProxyOAuthServiceRestTransport

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


class IdentityAwareProxyOAuthServiceRestInterceptor:
    """Interceptor for IdentityAwareProxyOAuthService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the IdentityAwareProxyOAuthServiceRestTransport.

    .. code-block:: python
        class MyCustomIdentityAwareProxyOAuthServiceInterceptor(IdentityAwareProxyOAuthServiceRestInterceptor):
            def pre_create_brand(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_brand(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_identity_aware_proxy_client(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_identity_aware_proxy_client(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_identity_aware_proxy_client(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_brand(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_brand(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_identity_aware_proxy_client(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_identity_aware_proxy_client(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_brands(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_brands(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_identity_aware_proxy_clients(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_identity_aware_proxy_clients(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_reset_identity_aware_proxy_client_secret(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_reset_identity_aware_proxy_client_secret(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = IdentityAwareProxyOAuthServiceRestTransport(interceptor=MyCustomIdentityAwareProxyOAuthServiceInterceptor())
        client = IdentityAwareProxyOAuthServiceClient(transport=transport)


    """

    def pre_create_brand(
        self,
        request: service.CreateBrandRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.CreateBrandRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_brand

        Override in a subclass to manipulate the request or metadata
        before they are sent to the IdentityAwareProxyOAuthService server.
        """
        return request, metadata

    def post_create_brand(self, response: service.Brand) -> service.Brand:
        """Post-rpc interceptor for create_brand

        DEPRECATED. Please use the `post_create_brand_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the IdentityAwareProxyOAuthService server but before
        it is returned to user code. This `post_create_brand` interceptor runs
        before the `post_create_brand_with_metadata` interceptor.
        """
        return response

    def post_create_brand_with_metadata(
        self, response: service.Brand, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[service.Brand, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_brand

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the IdentityAwareProxyOAuthService server but before it is returned to user code.

        We recommend only using this `post_create_brand_with_metadata`
        interceptor in new development instead of the `post_create_brand` interceptor.
        When both interceptors are used, this `post_create_brand_with_metadata` interceptor runs after the
        `post_create_brand` interceptor. The (possibly modified) response returned by
        `post_create_brand` will be passed to
        `post_create_brand_with_metadata`.
        """
        return response, metadata

    def pre_create_identity_aware_proxy_client(
        self,
        request: service.CreateIdentityAwareProxyClientRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.CreateIdentityAwareProxyClientRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_identity_aware_proxy_client

        Override in a subclass to manipulate the request or metadata
        before they are sent to the IdentityAwareProxyOAuthService server.
        """
        return request, metadata

    def post_create_identity_aware_proxy_client(
        self, response: service.IdentityAwareProxyClient
    ) -> service.IdentityAwareProxyClient:
        """Post-rpc interceptor for create_identity_aware_proxy_client

        DEPRECATED. Please use the `post_create_identity_aware_proxy_client_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the IdentityAwareProxyOAuthService server but before
        it is returned to user code. This `post_create_identity_aware_proxy_client` interceptor runs
        before the `post_create_identity_aware_proxy_client_with_metadata` interceptor.
        """
        return response

    def post_create_identity_aware_proxy_client_with_metadata(
        self,
        response: service.IdentityAwareProxyClient,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.IdentityAwareProxyClient, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for create_identity_aware_proxy_client

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the IdentityAwareProxyOAuthService server but before it is returned to user code.

        We recommend only using this `post_create_identity_aware_proxy_client_with_metadata`
        interceptor in new development instead of the `post_create_identity_aware_proxy_client` interceptor.
        When both interceptors are used, this `post_create_identity_aware_proxy_client_with_metadata` interceptor runs after the
        `post_create_identity_aware_proxy_client` interceptor. The (possibly modified) response returned by
        `post_create_identity_aware_proxy_client` will be passed to
        `post_create_identity_aware_proxy_client_with_metadata`.
        """
        return response, metadata

    def pre_delete_identity_aware_proxy_client(
        self,
        request: service.DeleteIdentityAwareProxyClientRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.DeleteIdentityAwareProxyClientRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_identity_aware_proxy_client

        Override in a subclass to manipulate the request or metadata
        before they are sent to the IdentityAwareProxyOAuthService server.
        """
        return request, metadata

    def pre_get_brand(
        self,
        request: service.GetBrandRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.GetBrandRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_brand

        Override in a subclass to manipulate the request or metadata
        before they are sent to the IdentityAwareProxyOAuthService server.
        """
        return request, metadata

    def post_get_brand(self, response: service.Brand) -> service.Brand:
        """Post-rpc interceptor for get_brand

        DEPRECATED. Please use the `post_get_brand_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the IdentityAwareProxyOAuthService server but before
        it is returned to user code. This `post_get_brand` interceptor runs
        before the `post_get_brand_with_metadata` interceptor.
        """
        return response

    def post_get_brand_with_metadata(
        self, response: service.Brand, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[service.Brand, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_brand

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the IdentityAwareProxyOAuthService server but before it is returned to user code.

        We recommend only using this `post_get_brand_with_metadata`
        interceptor in new development instead of the `post_get_brand` interceptor.
        When both interceptors are used, this `post_get_brand_with_metadata` interceptor runs after the
        `post_get_brand` interceptor. The (possibly modified) response returned by
        `post_get_brand` will be passed to
        `post_get_brand_with_metadata`.
        """
        return response, metadata

    def pre_get_identity_aware_proxy_client(
        self,
        request: service.GetIdentityAwareProxyClientRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.GetIdentityAwareProxyClientRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_identity_aware_proxy_client

        Override in a subclass to manipulate the request or metadata
        before they are sent to the IdentityAwareProxyOAuthService server.
        """
        return request, metadata

    def post_get_identity_aware_proxy_client(
        self, response: service.IdentityAwareProxyClient
    ) -> service.IdentityAwareProxyClient:
        """Post-rpc interceptor for get_identity_aware_proxy_client

        DEPRECATED. Please use the `post_get_identity_aware_proxy_client_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the IdentityAwareProxyOAuthService server but before
        it is returned to user code. This `post_get_identity_aware_proxy_client` interceptor runs
        before the `post_get_identity_aware_proxy_client_with_metadata` interceptor.
        """
        return response

    def post_get_identity_aware_proxy_client_with_metadata(
        self,
        response: service.IdentityAwareProxyClient,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.IdentityAwareProxyClient, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_identity_aware_proxy_client

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the IdentityAwareProxyOAuthService server but before it is returned to user code.

        We recommend only using this `post_get_identity_aware_proxy_client_with_metadata`
        interceptor in new development instead of the `post_get_identity_aware_proxy_client` interceptor.
        When both interceptors are used, this `post_get_identity_aware_proxy_client_with_metadata` interceptor runs after the
        `post_get_identity_aware_proxy_client` interceptor. The (possibly modified) response returned by
        `post_get_identity_aware_proxy_client` will be passed to
        `post_get_identity_aware_proxy_client_with_metadata`.
        """
        return response, metadata

    def pre_list_brands(
        self,
        request: service.ListBrandsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListBrandsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_brands

        Override in a subclass to manipulate the request or metadata
        before they are sent to the IdentityAwareProxyOAuthService server.
        """
        return request, metadata

    def post_list_brands(
        self, response: service.ListBrandsResponse
    ) -> service.ListBrandsResponse:
        """Post-rpc interceptor for list_brands

        DEPRECATED. Please use the `post_list_brands_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the IdentityAwareProxyOAuthService server but before
        it is returned to user code. This `post_list_brands` interceptor runs
        before the `post_list_brands_with_metadata` interceptor.
        """
        return response

    def post_list_brands_with_metadata(
        self,
        response: service.ListBrandsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListBrandsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_brands

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the IdentityAwareProxyOAuthService server but before it is returned to user code.

        We recommend only using this `post_list_brands_with_metadata`
        interceptor in new development instead of the `post_list_brands` interceptor.
        When both interceptors are used, this `post_list_brands_with_metadata` interceptor runs after the
        `post_list_brands` interceptor. The (possibly modified) response returned by
        `post_list_brands` will be passed to
        `post_list_brands_with_metadata`.
        """
        return response, metadata

    def pre_list_identity_aware_proxy_clients(
        self,
        request: service.ListIdentityAwareProxyClientsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ListIdentityAwareProxyClientsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_identity_aware_proxy_clients

        Override in a subclass to manipulate the request or metadata
        before they are sent to the IdentityAwareProxyOAuthService server.
        """
        return request, metadata

    def post_list_identity_aware_proxy_clients(
        self, response: service.ListIdentityAwareProxyClientsResponse
    ) -> service.ListIdentityAwareProxyClientsResponse:
        """Post-rpc interceptor for list_identity_aware_proxy_clients

        DEPRECATED. Please use the `post_list_identity_aware_proxy_clients_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the IdentityAwareProxyOAuthService server but before
        it is returned to user code. This `post_list_identity_aware_proxy_clients` interceptor runs
        before the `post_list_identity_aware_proxy_clients_with_metadata` interceptor.
        """
        return response

    def post_list_identity_aware_proxy_clients_with_metadata(
        self,
        response: service.ListIdentityAwareProxyClientsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ListIdentityAwareProxyClientsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_identity_aware_proxy_clients

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the IdentityAwareProxyOAuthService server but before it is returned to user code.

        We recommend only using this `post_list_identity_aware_proxy_clients_with_metadata`
        interceptor in new development instead of the `post_list_identity_aware_proxy_clients` interceptor.
        When both interceptors are used, this `post_list_identity_aware_proxy_clients_with_metadata` interceptor runs after the
        `post_list_identity_aware_proxy_clients` interceptor. The (possibly modified) response returned by
        `post_list_identity_aware_proxy_clients` will be passed to
        `post_list_identity_aware_proxy_clients_with_metadata`.
        """
        return response, metadata

    def pre_reset_identity_aware_proxy_client_secret(
        self,
        request: service.ResetIdentityAwareProxyClientSecretRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ResetIdentityAwareProxyClientSecretRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for reset_identity_aware_proxy_client_secret

        Override in a subclass to manipulate the request or metadata
        before they are sent to the IdentityAwareProxyOAuthService server.
        """
        return request, metadata

    def post_reset_identity_aware_proxy_client_secret(
        self, response: service.IdentityAwareProxyClient
    ) -> service.IdentityAwareProxyClient:
        """Post-rpc interceptor for reset_identity_aware_proxy_client_secret

        DEPRECATED. Please use the `post_reset_identity_aware_proxy_client_secret_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the IdentityAwareProxyOAuthService server but before
        it is returned to user code. This `post_reset_identity_aware_proxy_client_secret` interceptor runs
        before the `post_reset_identity_aware_proxy_client_secret_with_metadata` interceptor.
        """
        return response

    def post_reset_identity_aware_proxy_client_secret_with_metadata(
        self,
        response: service.IdentityAwareProxyClient,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.IdentityAwareProxyClient, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for reset_identity_aware_proxy_client_secret

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the IdentityAwareProxyOAuthService server but before it is returned to user code.

        We recommend only using this `post_reset_identity_aware_proxy_client_secret_with_metadata`
        interceptor in new development instead of the `post_reset_identity_aware_proxy_client_secret` interceptor.
        When both interceptors are used, this `post_reset_identity_aware_proxy_client_secret_with_metadata` interceptor runs after the
        `post_reset_identity_aware_proxy_client_secret` interceptor. The (possibly modified) response returned by
        `post_reset_identity_aware_proxy_client_secret` will be passed to
        `post_reset_identity_aware_proxy_client_secret_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class IdentityAwareProxyOAuthServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: IdentityAwareProxyOAuthServiceRestInterceptor


class IdentityAwareProxyOAuthServiceRestTransport(
    _BaseIdentityAwareProxyOAuthServiceRestTransport
):
    """REST backend synchronous transport for IdentityAwareProxyOAuthService.

    API to programmatically create, list and retrieve Identity
    Aware Proxy (IAP) OAuth brands; and create, retrieve, delete and
    reset-secret of IAP OAuth clients.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "iap.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[IdentityAwareProxyOAuthServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'iap.googleapis.com').
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
            interceptor (Optional[IdentityAwareProxyOAuthServiceRestInterceptor]): Interceptor used
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
        self._interceptor = (
            interceptor or IdentityAwareProxyOAuthServiceRestInterceptor()
        )
        self._prep_wrapped_messages(client_info)

    class _CreateBrand(
        _BaseIdentityAwareProxyOAuthServiceRestTransport._BaseCreateBrand,
        IdentityAwareProxyOAuthServiceRestStub,
    ):
        def __hash__(self):
            return hash("IdentityAwareProxyOAuthServiceRestTransport.CreateBrand")

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
            request: service.CreateBrandRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.Brand:
            r"""Call the create brand method over HTTP.

            Args:
                request (~.service.CreateBrandRequest):
                    The request object. The request sent to CreateBrand.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.Brand:
                    OAuth brand data.
                NOTE: Only contains a portion of the
                data that describes a brand.

            """

            http_options = _BaseIdentityAwareProxyOAuthServiceRestTransport._BaseCreateBrand._get_http_options()
            request, metadata = self._interceptor.pre_create_brand(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseIdentityAwareProxyOAuthServiceRestTransport._BaseCreateBrand,
                    "_BaseCreateBrand__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.iap_v1.IdentityAwareProxyOAuthServiceClient.CreateBrand",
                    extra={
                        "serviceName": "google.cloud.iap.v1.IdentityAwareProxyOAuthService",
                        "rpcName": "CreateBrand",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                IdentityAwareProxyOAuthServiceRestTransport._CreateBrand._get_response(
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
            resp = service.Brand()
            pb_resp = service.Brand.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_brand(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_brand_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.Brand.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.iap_v1.IdentityAwareProxyOAuthServiceClient.create_brand",
                    extra={
                        "serviceName": "google.cloud.iap.v1.IdentityAwareProxyOAuthService",
                        "rpcName": "CreateBrand",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateIdentityAwareProxyClient(
        _BaseIdentityAwareProxyOAuthServiceRestTransport._BaseCreateIdentityAwareProxyClient,
        IdentityAwareProxyOAuthServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "IdentityAwareProxyOAuthServiceRestTransport.CreateIdentityAwareProxyClient"
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
            request: service.CreateIdentityAwareProxyClientRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.IdentityAwareProxyClient:
            r"""Call the create identity aware
            proxy client method over HTTP.

                Args:
                    request (~.service.CreateIdentityAwareProxyClientRequest):
                        The request object. The request sent to
                    CreateIdentityAwareProxyClient.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.service.IdentityAwareProxyClient:
                        Contains the data that describes an
                    Identity Aware Proxy owned client.

            """

            http_options = _BaseIdentityAwareProxyOAuthServiceRestTransport._BaseCreateIdentityAwareProxyClient._get_http_options()
            request, metadata = (
                self._interceptor.pre_create_identity_aware_proxy_client(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseIdentityAwareProxyOAuthServiceRestTransport._BaseCreateIdentityAwareProxyClient,
                    "_BaseCreateIdentityAwareProxyClient__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.iap_v1.IdentityAwareProxyOAuthServiceClient.CreateIdentityAwareProxyClient",
                    extra={
                        "serviceName": "google.cloud.iap.v1.IdentityAwareProxyOAuthService",
                        "rpcName": "CreateIdentityAwareProxyClient",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = IdentityAwareProxyOAuthServiceRestTransport._CreateIdentityAwareProxyClient._get_response(
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
            resp = service.IdentityAwareProxyClient()
            pb_resp = service.IdentityAwareProxyClient.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_identity_aware_proxy_client(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_create_identity_aware_proxy_client_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.IdentityAwareProxyClient.to_json(
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
                    "Received response for google.cloud.iap_v1.IdentityAwareProxyOAuthServiceClient.create_identity_aware_proxy_client",
                    extra={
                        "serviceName": "google.cloud.iap.v1.IdentityAwareProxyOAuthService",
                        "rpcName": "CreateIdentityAwareProxyClient",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteIdentityAwareProxyClient(
        _BaseIdentityAwareProxyOAuthServiceRestTransport._BaseDeleteIdentityAwareProxyClient,
        IdentityAwareProxyOAuthServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "IdentityAwareProxyOAuthServiceRestTransport.DeleteIdentityAwareProxyClient"
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
            request: service.DeleteIdentityAwareProxyClientRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete identity aware
            proxy client method over HTTP.

                Args:
                    request (~.service.DeleteIdentityAwareProxyClientRequest):
                        The request object. The request sent to
                    DeleteIdentityAwareProxyClient.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.
            """

            http_options = _BaseIdentityAwareProxyOAuthServiceRestTransport._BaseDeleteIdentityAwareProxyClient._get_http_options()
            request, metadata = (
                self._interceptor.pre_delete_identity_aware_proxy_client(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseIdentityAwareProxyOAuthServiceRestTransport._BaseDeleteIdentityAwareProxyClient,
                    "_BaseDeleteIdentityAwareProxyClient__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.iap_v1.IdentityAwareProxyOAuthServiceClient.DeleteIdentityAwareProxyClient",
                    extra={
                        "serviceName": "google.cloud.iap.v1.IdentityAwareProxyOAuthService",
                        "rpcName": "DeleteIdentityAwareProxyClient",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = IdentityAwareProxyOAuthServiceRestTransport._DeleteIdentityAwareProxyClient._get_response(
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

    class _GetBrand(
        _BaseIdentityAwareProxyOAuthServiceRestTransport._BaseGetBrand,
        IdentityAwareProxyOAuthServiceRestStub,
    ):
        def __hash__(self):
            return hash("IdentityAwareProxyOAuthServiceRestTransport.GetBrand")

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
            request: service.GetBrandRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.Brand:
            r"""Call the get brand method over HTTP.

            Args:
                request (~.service.GetBrandRequest):
                    The request object. The request sent to GetBrand.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.Brand:
                    OAuth brand data.
                NOTE: Only contains a portion of the
                data that describes a brand.

            """

            http_options = _BaseIdentityAwareProxyOAuthServiceRestTransport._BaseGetBrand._get_http_options()
            request, metadata = self._interceptor.pre_get_brand(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseIdentityAwareProxyOAuthServiceRestTransport._BaseGetBrand,
                    "_BaseGetBrand__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.iap_v1.IdentityAwareProxyOAuthServiceClient.GetBrand",
                    extra={
                        "serviceName": "google.cloud.iap.v1.IdentityAwareProxyOAuthService",
                        "rpcName": "GetBrand",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                IdentityAwareProxyOAuthServiceRestTransport._GetBrand._get_response(
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
            resp = service.Brand()
            pb_resp = service.Brand.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_brand(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_brand_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.Brand.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.iap_v1.IdentityAwareProxyOAuthServiceClient.get_brand",
                    extra={
                        "serviceName": "google.cloud.iap.v1.IdentityAwareProxyOAuthService",
                        "rpcName": "GetBrand",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetIdentityAwareProxyClient(
        _BaseIdentityAwareProxyOAuthServiceRestTransport._BaseGetIdentityAwareProxyClient,
        IdentityAwareProxyOAuthServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "IdentityAwareProxyOAuthServiceRestTransport.GetIdentityAwareProxyClient"
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
            request: service.GetIdentityAwareProxyClientRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.IdentityAwareProxyClient:
            r"""Call the get identity aware proxy
            client method over HTTP.

                Args:
                    request (~.service.GetIdentityAwareProxyClientRequest):
                        The request object. The request sent to
                    GetIdentityAwareProxyClient.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.service.IdentityAwareProxyClient:
                        Contains the data that describes an
                    Identity Aware Proxy owned client.

            """

            http_options = _BaseIdentityAwareProxyOAuthServiceRestTransport._BaseGetIdentityAwareProxyClient._get_http_options()
            request, metadata = self._interceptor.pre_get_identity_aware_proxy_client(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseIdentityAwareProxyOAuthServiceRestTransport._BaseGetIdentityAwareProxyClient,
                    "_BaseGetIdentityAwareProxyClient__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.iap_v1.IdentityAwareProxyOAuthServiceClient.GetIdentityAwareProxyClient",
                    extra={
                        "serviceName": "google.cloud.iap.v1.IdentityAwareProxyOAuthService",
                        "rpcName": "GetIdentityAwareProxyClient",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = IdentityAwareProxyOAuthServiceRestTransport._GetIdentityAwareProxyClient._get_response(
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
            resp = service.IdentityAwareProxyClient()
            pb_resp = service.IdentityAwareProxyClient.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_identity_aware_proxy_client(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_get_identity_aware_proxy_client_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.IdentityAwareProxyClient.to_json(
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
                    "Received response for google.cloud.iap_v1.IdentityAwareProxyOAuthServiceClient.get_identity_aware_proxy_client",
                    extra={
                        "serviceName": "google.cloud.iap.v1.IdentityAwareProxyOAuthService",
                        "rpcName": "GetIdentityAwareProxyClient",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListBrands(
        _BaseIdentityAwareProxyOAuthServiceRestTransport._BaseListBrands,
        IdentityAwareProxyOAuthServiceRestStub,
    ):
        def __hash__(self):
            return hash("IdentityAwareProxyOAuthServiceRestTransport.ListBrands")

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
            request: service.ListBrandsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListBrandsResponse:
            r"""Call the list brands method over HTTP.

            Args:
                request (~.service.ListBrandsRequest):
                    The request object. The request sent to ListBrands.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListBrandsResponse:
                    Response message for ListBrands.
            """

            http_options = _BaseIdentityAwareProxyOAuthServiceRestTransport._BaseListBrands._get_http_options()
            request, metadata = self._interceptor.pre_list_brands(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseIdentityAwareProxyOAuthServiceRestTransport._BaseListBrands,
                    "_BaseListBrands__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.iap_v1.IdentityAwareProxyOAuthServiceClient.ListBrands",
                    extra={
                        "serviceName": "google.cloud.iap.v1.IdentityAwareProxyOAuthService",
                        "rpcName": "ListBrands",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                IdentityAwareProxyOAuthServiceRestTransport._ListBrands._get_response(
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
            resp = service.ListBrandsResponse()
            pb_resp = service.ListBrandsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_brands(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_brands_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListBrandsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.iap_v1.IdentityAwareProxyOAuthServiceClient.list_brands",
                    extra={
                        "serviceName": "google.cloud.iap.v1.IdentityAwareProxyOAuthService",
                        "rpcName": "ListBrands",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListIdentityAwareProxyClients(
        _BaseIdentityAwareProxyOAuthServiceRestTransport._BaseListIdentityAwareProxyClients,
        IdentityAwareProxyOAuthServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "IdentityAwareProxyOAuthServiceRestTransport.ListIdentityAwareProxyClients"
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
            request: service.ListIdentityAwareProxyClientsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListIdentityAwareProxyClientsResponse:
            r"""Call the list identity aware proxy
            clients method over HTTP.

                Args:
                    request (~.service.ListIdentityAwareProxyClientsRequest):
                        The request object. The request sent to
                    ListIdentityAwareProxyClients.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.service.ListIdentityAwareProxyClientsResponse:
                        Response message for
                    ListIdentityAwareProxyClients.

            """

            http_options = _BaseIdentityAwareProxyOAuthServiceRestTransport._BaseListIdentityAwareProxyClients._get_http_options()
            request, metadata = self._interceptor.pre_list_identity_aware_proxy_clients(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseIdentityAwareProxyOAuthServiceRestTransport._BaseListIdentityAwareProxyClients,
                    "_BaseListIdentityAwareProxyClients__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.iap_v1.IdentityAwareProxyOAuthServiceClient.ListIdentityAwareProxyClients",
                    extra={
                        "serviceName": "google.cloud.iap.v1.IdentityAwareProxyOAuthService",
                        "rpcName": "ListIdentityAwareProxyClients",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = IdentityAwareProxyOAuthServiceRestTransport._ListIdentityAwareProxyClients._get_response(
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
            resp = service.ListIdentityAwareProxyClientsResponse()
            pb_resp = service.ListIdentityAwareProxyClientsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_identity_aware_proxy_clients(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_identity_aware_proxy_clients_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        service.ListIdentityAwareProxyClientsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.iap_v1.IdentityAwareProxyOAuthServiceClient.list_identity_aware_proxy_clients",
                    extra={
                        "serviceName": "google.cloud.iap.v1.IdentityAwareProxyOAuthService",
                        "rpcName": "ListIdentityAwareProxyClients",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ResetIdentityAwareProxyClientSecret(
        _BaseIdentityAwareProxyOAuthServiceRestTransport._BaseResetIdentityAwareProxyClientSecret,
        IdentityAwareProxyOAuthServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "IdentityAwareProxyOAuthServiceRestTransport.ResetIdentityAwareProxyClientSecret"
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
            request: service.ResetIdentityAwareProxyClientSecretRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.IdentityAwareProxyClient:
            r"""Call the reset identity aware
            proxy client secret method over HTTP.

                Args:
                    request (~.service.ResetIdentityAwareProxyClientSecretRequest):
                        The request object. The request sent to
                    ResetIdentityAwareProxyClientSecret.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.service.IdentityAwareProxyClient:
                        Contains the data that describes an
                    Identity Aware Proxy owned client.

            """

            http_options = _BaseIdentityAwareProxyOAuthServiceRestTransport._BaseResetIdentityAwareProxyClientSecret._get_http_options()
            request, metadata = (
                self._interceptor.pre_reset_identity_aware_proxy_client_secret(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseIdentityAwareProxyOAuthServiceRestTransport._BaseResetIdentityAwareProxyClientSecret,
                    "_BaseResetIdentityAwareProxyClientSecret__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.iap_v1.IdentityAwareProxyOAuthServiceClient.ResetIdentityAwareProxyClientSecret",
                    extra={
                        "serviceName": "google.cloud.iap.v1.IdentityAwareProxyOAuthService",
                        "rpcName": "ResetIdentityAwareProxyClientSecret",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = IdentityAwareProxyOAuthServiceRestTransport._ResetIdentityAwareProxyClientSecret._get_response(
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
            resp = service.IdentityAwareProxyClient()
            pb_resp = service.IdentityAwareProxyClient.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_reset_identity_aware_proxy_client_secret(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_reset_identity_aware_proxy_client_secret_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.IdentityAwareProxyClient.to_json(
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
                    "Received response for google.cloud.iap_v1.IdentityAwareProxyOAuthServiceClient.reset_identity_aware_proxy_client_secret",
                    extra={
                        "serviceName": "google.cloud.iap.v1.IdentityAwareProxyOAuthService",
                        "rpcName": "ResetIdentityAwareProxyClientSecret",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_brand(self) -> Callable[[service.CreateBrandRequest], service.Brand]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateBrand(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_identity_aware_proxy_client(
        self,
    ) -> Callable[
        [service.CreateIdentityAwareProxyClientRequest],
        service.IdentityAwareProxyClient,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateIdentityAwareProxyClient(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_identity_aware_proxy_client(
        self,
    ) -> Callable[[service.DeleteIdentityAwareProxyClientRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteIdentityAwareProxyClient(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_brand(self) -> Callable[[service.GetBrandRequest], service.Brand]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetBrand(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_identity_aware_proxy_client(
        self,
    ) -> Callable[
        [service.GetIdentityAwareProxyClientRequest], service.IdentityAwareProxyClient
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetIdentityAwareProxyClient(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_brands(
        self,
    ) -> Callable[[service.ListBrandsRequest], service.ListBrandsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListBrands(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_identity_aware_proxy_clients(
        self,
    ) -> Callable[
        [service.ListIdentityAwareProxyClientsRequest],
        service.ListIdentityAwareProxyClientsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListIdentityAwareProxyClients(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def reset_identity_aware_proxy_client_secret(
        self,
    ) -> Callable[
        [service.ResetIdentityAwareProxyClientSecretRequest],
        service.IdentityAwareProxyClient,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ResetIdentityAwareProxyClientSecret(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("IdentityAwareProxyOAuthServiceRestTransport",)
