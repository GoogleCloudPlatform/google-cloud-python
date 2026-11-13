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
from google.ads.admanager_v1.types import network_messages, network_service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseNetworkServiceRestTransport

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


class NetworkServiceRestInterceptor:
    """Interceptor for NetworkService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the NetworkServiceRestTransport.

    .. code-block:: python
        class MyCustomNetworkServiceInterceptor(NetworkServiceRestInterceptor):
            def pre_get_default_third_party_data_declaration(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_default_third_party_data_declaration(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_network(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_network(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_networks(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_networks(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_provision_test_network(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_provision_test_network(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_network(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_network(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = NetworkServiceRestTransport(interceptor=MyCustomNetworkServiceInterceptor())
        client = NetworkServiceClient(transport=transport)


    """

    def pre_get_default_third_party_data_declaration(
        self,
        request: network_service.GetDefaultThirdPartyDataDeclarationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        network_service.GetDefaultThirdPartyDataDeclarationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_default_third_party_data_declaration

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkService server.
        """
        return request, metadata

    def post_get_default_third_party_data_declaration(
        self, response: network_messages.DefaultThirdPartyDataDeclaration
    ) -> network_messages.DefaultThirdPartyDataDeclaration:
        """Post-rpc interceptor for get_default_third_party_data_declaration

        DEPRECATED. Please use the `post_get_default_third_party_data_declaration_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkService server but before
        it is returned to user code. This `post_get_default_third_party_data_declaration` interceptor runs
        before the `post_get_default_third_party_data_declaration_with_metadata` interceptor.
        """
        return response

    def post_get_default_third_party_data_declaration_with_metadata(
        self,
        response: network_messages.DefaultThirdPartyDataDeclaration,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        network_messages.DefaultThirdPartyDataDeclaration,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_default_third_party_data_declaration

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkService server but before it is returned to user code.

        We recommend only using this `post_get_default_third_party_data_declaration_with_metadata`
        interceptor in new development instead of the `post_get_default_third_party_data_declaration` interceptor.
        When both interceptors are used, this `post_get_default_third_party_data_declaration_with_metadata` interceptor runs after the
        `post_get_default_third_party_data_declaration` interceptor. The (possibly modified) response returned by
        `post_get_default_third_party_data_declaration` will be passed to
        `post_get_default_third_party_data_declaration_with_metadata`.
        """
        return response, metadata

    def pre_get_network(
        self,
        request: network_service.GetNetworkRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        network_service.GetNetworkRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_network

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkService server.
        """
        return request, metadata

    def post_get_network(
        self, response: network_messages.Network
    ) -> network_messages.Network:
        """Post-rpc interceptor for get_network

        DEPRECATED. Please use the `post_get_network_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkService server but before
        it is returned to user code. This `post_get_network` interceptor runs
        before the `post_get_network_with_metadata` interceptor.
        """
        return response

    def post_get_network_with_metadata(
        self,
        response: network_messages.Network,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[network_messages.Network, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_network

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkService server but before it is returned to user code.

        We recommend only using this `post_get_network_with_metadata`
        interceptor in new development instead of the `post_get_network` interceptor.
        When both interceptors are used, this `post_get_network_with_metadata` interceptor runs after the
        `post_get_network` interceptor. The (possibly modified) response returned by
        `post_get_network` will be passed to
        `post_get_network_with_metadata`.
        """
        return response, metadata

    def pre_list_networks(
        self,
        request: network_service.ListNetworksRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        network_service.ListNetworksRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_networks

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkService server.
        """
        return request, metadata

    def post_list_networks(
        self, response: network_service.ListNetworksResponse
    ) -> network_service.ListNetworksResponse:
        """Post-rpc interceptor for list_networks

        DEPRECATED. Please use the `post_list_networks_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkService server but before
        it is returned to user code. This `post_list_networks` interceptor runs
        before the `post_list_networks_with_metadata` interceptor.
        """
        return response

    def post_list_networks_with_metadata(
        self,
        response: network_service.ListNetworksResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        network_service.ListNetworksResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_networks

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkService server but before it is returned to user code.

        We recommend only using this `post_list_networks_with_metadata`
        interceptor in new development instead of the `post_list_networks` interceptor.
        When both interceptors are used, this `post_list_networks_with_metadata` interceptor runs after the
        `post_list_networks` interceptor. The (possibly modified) response returned by
        `post_list_networks` will be passed to
        `post_list_networks_with_metadata`.
        """
        return response, metadata

    def pre_provision_test_network(
        self,
        request: network_service.ProvisionTestNetworkRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        network_service.ProvisionTestNetworkRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for provision_test_network

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkService server.
        """
        return request, metadata

    def post_provision_test_network(
        self, response: network_messages.Network
    ) -> network_messages.Network:
        """Post-rpc interceptor for provision_test_network

        DEPRECATED. Please use the `post_provision_test_network_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkService server but before
        it is returned to user code. This `post_provision_test_network` interceptor runs
        before the `post_provision_test_network_with_metadata` interceptor.
        """
        return response

    def post_provision_test_network_with_metadata(
        self,
        response: network_messages.Network,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[network_messages.Network, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for provision_test_network

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkService server but before it is returned to user code.

        We recommend only using this `post_provision_test_network_with_metadata`
        interceptor in new development instead of the `post_provision_test_network` interceptor.
        When both interceptors are used, this `post_provision_test_network_with_metadata` interceptor runs after the
        `post_provision_test_network` interceptor. The (possibly modified) response returned by
        `post_provision_test_network` will be passed to
        `post_provision_test_network_with_metadata`.
        """
        return response, metadata

    def pre_update_network(
        self,
        request: network_service.UpdateNetworkRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        network_service.UpdateNetworkRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_network

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetworkService server.
        """
        return request, metadata

    def post_update_network(
        self, response: network_messages.Network
    ) -> network_messages.Network:
        """Post-rpc interceptor for update_network

        DEPRECATED. Please use the `post_update_network_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetworkService server but before
        it is returned to user code. This `post_update_network` interceptor runs
        before the `post_update_network_with_metadata` interceptor.
        """
        return response

    def post_update_network_with_metadata(
        self,
        response: network_messages.Network,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[network_messages.Network, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_network

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetworkService server but before it is returned to user code.

        We recommend only using this `post_update_network_with_metadata`
        interceptor in new development instead of the `post_update_network` interceptor.
        When both interceptors are used, this `post_update_network_with_metadata` interceptor runs after the
        `post_update_network` interceptor. The (possibly modified) response returned by
        `post_update_network` will be passed to
        `post_update_network_with_metadata`.
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
        before they are sent to the NetworkService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the NetworkService server but before
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
        before they are sent to the NetworkService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the NetworkService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class NetworkServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: NetworkServiceRestInterceptor


class NetworkServiceRestTransport(_BaseNetworkServiceRestTransport):
    """REST backend synchronous transport for NetworkService.

    Provides methods for handling ``Network`` objects.

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
        interceptor: Optional[NetworkServiceRestInterceptor] = None,
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
            interceptor (Optional[NetworkServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or NetworkServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _GetDefaultThirdPartyDataDeclaration(
        _BaseNetworkServiceRestTransport._BaseGetDefaultThirdPartyDataDeclaration,
        NetworkServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "NetworkServiceRestTransport.GetDefaultThirdPartyDataDeclaration"
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
            request: network_service.GetDefaultThirdPartyDataDeclarationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> network_messages.DefaultThirdPartyDataDeclaration:
            r"""Call the get default third party
            data declaration method over HTTP.

                Args:
                    request (~.network_service.GetDefaultThirdPartyDataDeclarationRequest):
                        The request object. Request for the ``GetDefaultThirdPartyDataDeclaration``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.network_messages.DefaultThirdPartyDataDeclaration:
                        The ``DefaultThirdPartyDataDeclaration`` singleton
                    resource.

            """

            http_options = _BaseNetworkServiceRestTransport._BaseGetDefaultThirdPartyDataDeclaration._get_http_options()
            request, metadata = (
                self._interceptor.pre_get_default_third_party_data_declaration(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServiceRestTransport._BaseGetDefaultThirdPartyDataDeclaration,
                    "_BaseGetDefaultThirdPartyDataDeclaration__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.NetworkServiceClient.GetDefaultThirdPartyDataDeclaration",
                    extra={
                        "serviceName": "google.ads.admanager.v1.NetworkService",
                        "rpcName": "GetDefaultThirdPartyDataDeclaration",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServiceRestTransport._GetDefaultThirdPartyDataDeclaration._get_response(
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
            resp = network_messages.DefaultThirdPartyDataDeclaration()
            pb_resp = network_messages.DefaultThirdPartyDataDeclaration.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_default_third_party_data_declaration(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_get_default_third_party_data_declaration_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        network_messages.DefaultThirdPartyDataDeclaration.to_json(
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
                    "Received response for google.ads.admanager_v1.NetworkServiceClient.get_default_third_party_data_declaration",
                    extra={
                        "serviceName": "google.ads.admanager.v1.NetworkService",
                        "rpcName": "GetDefaultThirdPartyDataDeclaration",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetNetwork(
        _BaseNetworkServiceRestTransport._BaseGetNetwork, NetworkServiceRestStub
    ):
        def __hash__(self):
            return hash("NetworkServiceRestTransport.GetNetwork")

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
            request: network_service.GetNetworkRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> network_messages.Network:
            r"""Call the get network method over HTTP.

            Args:
                request (~.network_service.GetNetworkRequest):
                    The request object. Request to get Network
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.network_messages.Network:
                    The Network resource.
            """

            http_options = (
                _BaseNetworkServiceRestTransport._BaseGetNetwork._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_network(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServiceRestTransport._BaseGetNetwork,
                    "_BaseGetNetwork__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.NetworkServiceClient.GetNetwork",
                    extra={
                        "serviceName": "google.ads.admanager.v1.NetworkService",
                        "rpcName": "GetNetwork",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServiceRestTransport._GetNetwork._get_response(
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
            resp = network_messages.Network()
            pb_resp = network_messages.Network.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_network(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_network_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = network_messages.Network.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.NetworkServiceClient.get_network",
                    extra={
                        "serviceName": "google.ads.admanager.v1.NetworkService",
                        "rpcName": "GetNetwork",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListNetworks(
        _BaseNetworkServiceRestTransport._BaseListNetworks, NetworkServiceRestStub
    ):
        def __hash__(self):
            return hash("NetworkServiceRestTransport.ListNetworks")

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
            request: network_service.ListNetworksRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> network_service.ListNetworksResponse:
            r"""Call the list networks method over HTTP.

            Args:
                request (~.network_service.ListNetworksRequest):
                    The request object. Request object for ``ListNetworks`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.network_service.ListNetworksResponse:
                    Response object for ``ListNetworks`` method.
            """

            http_options = (
                _BaseNetworkServiceRestTransport._BaseListNetworks._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_networks(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServiceRestTransport._BaseListNetworks,
                    "_BaseListNetworks__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.NetworkServiceClient.ListNetworks",
                    extra={
                        "serviceName": "google.ads.admanager.v1.NetworkService",
                        "rpcName": "ListNetworks",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServiceRestTransport._ListNetworks._get_response(
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
            resp = network_service.ListNetworksResponse()
            pb_resp = network_service.ListNetworksResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_networks(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_networks_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = network_service.ListNetworksResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.NetworkServiceClient.list_networks",
                    extra={
                        "serviceName": "google.ads.admanager.v1.NetworkService",
                        "rpcName": "ListNetworks",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ProvisionTestNetwork(
        _BaseNetworkServiceRestTransport._BaseProvisionTestNetwork,
        NetworkServiceRestStub,
    ):
        def __hash__(self):
            return hash("NetworkServiceRestTransport.ProvisionTestNetwork")

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
            request: network_service.ProvisionTestNetworkRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> network_messages.Network:
            r"""Call the provision test network method over HTTP.

            Args:
                request (~.network_service.ProvisionTestNetworkRequest):
                    The request object. Request for the ``ProvisionTestNetwork`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.network_messages.Network:
                    The Network resource.
            """

            http_options = _BaseNetworkServiceRestTransport._BaseProvisionTestNetwork._get_http_options()
            request, metadata = self._interceptor.pre_provision_test_network(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServiceRestTransport._BaseProvisionTestNetwork,
                    "_BaseProvisionTestNetwork__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.NetworkServiceClient.ProvisionTestNetwork",
                    extra={
                        "serviceName": "google.ads.admanager.v1.NetworkService",
                        "rpcName": "ProvisionTestNetwork",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServiceRestTransport._ProvisionTestNetwork._get_response(
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
            resp = network_messages.Network()
            pb_resp = network_messages.Network.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_provision_test_network(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_provision_test_network_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = network_messages.Network.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.NetworkServiceClient.provision_test_network",
                    extra={
                        "serviceName": "google.ads.admanager.v1.NetworkService",
                        "rpcName": "ProvisionTestNetwork",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateNetwork(
        _BaseNetworkServiceRestTransport._BaseUpdateNetwork, NetworkServiceRestStub
    ):
        def __hash__(self):
            return hash("NetworkServiceRestTransport.UpdateNetwork")

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
            request: network_service.UpdateNetworkRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> network_messages.Network:
            r"""Call the update network method over HTTP.

            Args:
                request (~.network_service.UpdateNetworkRequest):
                    The request object. Request for the ``UpdateNetwork`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.network_messages.Network:
                    The Network resource.
            """

            http_options = (
                _BaseNetworkServiceRestTransport._BaseUpdateNetwork._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_network(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServiceRestTransport._BaseUpdateNetwork,
                    "_BaseUpdateNetwork__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.NetworkServiceClient.UpdateNetwork",
                    extra={
                        "serviceName": "google.ads.admanager.v1.NetworkService",
                        "rpcName": "UpdateNetwork",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServiceRestTransport._UpdateNetwork._get_response(
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
            resp = network_messages.Network()
            pb_resp = network_messages.Network.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_network(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_network_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = network_messages.Network.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.NetworkServiceClient.update_network",
                    extra={
                        "serviceName": "google.ads.admanager.v1.NetworkService",
                        "rpcName": "UpdateNetwork",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def get_default_third_party_data_declaration(
        self,
    ) -> Callable[
        [network_service.GetDefaultThirdPartyDataDeclarationRequest],
        network_messages.DefaultThirdPartyDataDeclaration,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDefaultThirdPartyDataDeclaration(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_network(
        self,
    ) -> Callable[[network_service.GetNetworkRequest], network_messages.Network]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetNetwork(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_networks(
        self,
    ) -> Callable[
        [network_service.ListNetworksRequest], network_service.ListNetworksResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListNetworks(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def provision_test_network(
        self,
    ) -> Callable[
        [network_service.ProvisionTestNetworkRequest], network_messages.Network
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ProvisionTestNetwork(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_network(
        self,
    ) -> Callable[[network_service.UpdateNetworkRequest], network_messages.Network]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateNetwork(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseNetworkServiceRestTransport._BaseCancelOperation, NetworkServiceRestStub
    ):
        def __hash__(self):
            return hash("NetworkServiceRestTransport.CancelOperation")

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

            http_options = _BaseNetworkServiceRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.ads.admanager_v1.NetworkServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.NetworkService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServiceRestTransport._CancelOperation._get_response(
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
        _BaseNetworkServiceRestTransport._BaseGetOperation, NetworkServiceRestStub
    ):
        def __hash__(self):
            return hash("NetworkServiceRestTransport.GetOperation")

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
                _BaseNetworkServiceRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetworkServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.ads.admanager_v1.NetworkServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.NetworkService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetworkServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.ads.admanager_v1.NetworkServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.NetworkService",
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


__all__ = ("NetworkServiceRestTransport",)
