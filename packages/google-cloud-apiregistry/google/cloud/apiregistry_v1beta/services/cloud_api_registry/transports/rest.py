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
from google.cloud.location import locations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.apiregistry_v1beta._compat import transcode_request
from google.cloud.apiregistry_v1beta.types import resources, service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseCloudApiRegistryRestTransport

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


class CloudApiRegistryRestInterceptor:
    """Interceptor for CloudApiRegistry.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the CloudApiRegistryRestTransport.

    .. code-block:: python
        class MyCustomCloudApiRegistryInterceptor(CloudApiRegistryRestInterceptor):
            def pre_get_mcp_server(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_mcp_server(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_mcp_tool(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_mcp_tool(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_mcp_servers(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_mcp_servers(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_mcp_tools(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_mcp_tools(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = CloudApiRegistryRestTransport(interceptor=MyCustomCloudApiRegistryInterceptor())
        client = CloudApiRegistryClient(transport=transport)


    """

    def pre_get_mcp_server(
        self,
        request: service.GetMcpServerRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.GetMcpServerRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_mcp_server

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudApiRegistry server.
        """
        return request, metadata

    def post_get_mcp_server(self, response: resources.McpServer) -> resources.McpServer:
        """Post-rpc interceptor for get_mcp_server

        DEPRECATED. Please use the `post_get_mcp_server_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudApiRegistry server but before
        it is returned to user code. This `post_get_mcp_server` interceptor runs
        before the `post_get_mcp_server_with_metadata` interceptor.
        """
        return response

    def post_get_mcp_server_with_metadata(
        self,
        response: resources.McpServer,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.McpServer, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_mcp_server

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudApiRegistry server but before it is returned to user code.

        We recommend only using this `post_get_mcp_server_with_metadata`
        interceptor in new development instead of the `post_get_mcp_server` interceptor.
        When both interceptors are used, this `post_get_mcp_server_with_metadata` interceptor runs after the
        `post_get_mcp_server` interceptor. The (possibly modified) response returned by
        `post_get_mcp_server` will be passed to
        `post_get_mcp_server_with_metadata`.
        """
        return response, metadata

    def pre_get_mcp_tool(
        self,
        request: service.GetMcpToolRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.GetMcpToolRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_mcp_tool

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudApiRegistry server.
        """
        return request, metadata

    def post_get_mcp_tool(self, response: resources.McpTool) -> resources.McpTool:
        """Post-rpc interceptor for get_mcp_tool

        DEPRECATED. Please use the `post_get_mcp_tool_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudApiRegistry server but before
        it is returned to user code. This `post_get_mcp_tool` interceptor runs
        before the `post_get_mcp_tool_with_metadata` interceptor.
        """
        return response

    def post_get_mcp_tool_with_metadata(
        self,
        response: resources.McpTool,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.McpTool, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_mcp_tool

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudApiRegistry server but before it is returned to user code.

        We recommend only using this `post_get_mcp_tool_with_metadata`
        interceptor in new development instead of the `post_get_mcp_tool` interceptor.
        When both interceptors are used, this `post_get_mcp_tool_with_metadata` interceptor runs after the
        `post_get_mcp_tool` interceptor. The (possibly modified) response returned by
        `post_get_mcp_tool` will be passed to
        `post_get_mcp_tool_with_metadata`.
        """
        return response, metadata

    def pre_list_mcp_servers(
        self,
        request: service.ListMcpServersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListMcpServersRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_mcp_servers

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudApiRegistry server.
        """
        return request, metadata

    def post_list_mcp_servers(
        self, response: service.ListMcpServersResponse
    ) -> service.ListMcpServersResponse:
        """Post-rpc interceptor for list_mcp_servers

        DEPRECATED. Please use the `post_list_mcp_servers_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudApiRegistry server but before
        it is returned to user code. This `post_list_mcp_servers` interceptor runs
        before the `post_list_mcp_servers_with_metadata` interceptor.
        """
        return response

    def post_list_mcp_servers_with_metadata(
        self,
        response: service.ListMcpServersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListMcpServersResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_mcp_servers

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudApiRegistry server but before it is returned to user code.

        We recommend only using this `post_list_mcp_servers_with_metadata`
        interceptor in new development instead of the `post_list_mcp_servers` interceptor.
        When both interceptors are used, this `post_list_mcp_servers_with_metadata` interceptor runs after the
        `post_list_mcp_servers` interceptor. The (possibly modified) response returned by
        `post_list_mcp_servers` will be passed to
        `post_list_mcp_servers_with_metadata`.
        """
        return response, metadata

    def pre_list_mcp_tools(
        self,
        request: service.ListMcpToolsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListMcpToolsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_mcp_tools

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudApiRegistry server.
        """
        return request, metadata

    def post_list_mcp_tools(
        self, response: service.ListMcpToolsResponse
    ) -> service.ListMcpToolsResponse:
        """Post-rpc interceptor for list_mcp_tools

        DEPRECATED. Please use the `post_list_mcp_tools_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudApiRegistry server but before
        it is returned to user code. This `post_list_mcp_tools` interceptor runs
        before the `post_list_mcp_tools_with_metadata` interceptor.
        """
        return response

    def post_list_mcp_tools_with_metadata(
        self,
        response: service.ListMcpToolsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListMcpToolsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_mcp_tools

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudApiRegistry server but before it is returned to user code.

        We recommend only using this `post_list_mcp_tools_with_metadata`
        interceptor in new development instead of the `post_list_mcp_tools` interceptor.
        When both interceptors are used, this `post_list_mcp_tools_with_metadata` interceptor runs after the
        `post_list_mcp_tools` interceptor. The (possibly modified) response returned by
        `post_list_mcp_tools` will be passed to
        `post_list_mcp_tools_with_metadata`.
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
        before they are sent to the CloudApiRegistry server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the CloudApiRegistry server but before
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
        before they are sent to the CloudApiRegistry server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the CloudApiRegistry server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class CloudApiRegistryRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: CloudApiRegistryRestInterceptor


class CloudApiRegistryRestTransport(_BaseCloudApiRegistryRestTransport):
    """REST backend synchronous transport for CloudApiRegistry.

    The Cloud API Registry service provides a central registry
    for managing API Data.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "cloudapiregistry.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[CloudApiRegistryRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'cloudapiregistry.googleapis.com').
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
            interceptor (Optional[CloudApiRegistryRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or CloudApiRegistryRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _GetMcpServer(
        _BaseCloudApiRegistryRestTransport._BaseGetMcpServer, CloudApiRegistryRestStub
    ):
        def __hash__(self):
            return hash("CloudApiRegistryRestTransport.GetMcpServer")

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
            request: service.GetMcpServerRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.McpServer:
            r"""Call the get mcp server method over HTTP.

            Args:
                request (~.service.GetMcpServerRequest):
                    The request object. Message for getting a McpServer
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.McpServer:
                    Represents an MCP Server. MCP Servers
                act as endpoints that expose a
                collection of tools that can be invoked
                by agents.

            """

            http_options = (
                _BaseCloudApiRegistryRestTransport._BaseGetMcpServer._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_mcp_server(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudApiRegistryRestTransport._BaseGetMcpServer,
                    "_BaseGetMcpServer__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apiregistry_v1beta.CloudApiRegistryClient.GetMcpServer",
                    extra={
                        "serviceName": "google.cloud.apiregistry.v1beta.CloudApiRegistry",
                        "rpcName": "GetMcpServer",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudApiRegistryRestTransport._GetMcpServer._get_response(
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
            resp = resources.McpServer()
            pb_resp = resources.McpServer.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_mcp_server(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_mcp_server_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.McpServer.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apiregistry_v1beta.CloudApiRegistryClient.get_mcp_server",
                    extra={
                        "serviceName": "google.cloud.apiregistry.v1beta.CloudApiRegistry",
                        "rpcName": "GetMcpServer",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetMcpTool(
        _BaseCloudApiRegistryRestTransport._BaseGetMcpTool, CloudApiRegistryRestStub
    ):
        def __hash__(self):
            return hash("CloudApiRegistryRestTransport.GetMcpTool")

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
            request: service.GetMcpToolRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.McpTool:
            r"""Call the get mcp tool method over HTTP.

            Args:
                request (~.service.GetMcpToolRequest):
                    The request object. Message for getting a McpTool
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.McpTool:
                    Message describing McpTool object
            """

            http_options = (
                _BaseCloudApiRegistryRestTransport._BaseGetMcpTool._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_mcp_tool(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudApiRegistryRestTransport._BaseGetMcpTool,
                    "_BaseGetMcpTool__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apiregistry_v1beta.CloudApiRegistryClient.GetMcpTool",
                    extra={
                        "serviceName": "google.cloud.apiregistry.v1beta.CloudApiRegistry",
                        "rpcName": "GetMcpTool",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudApiRegistryRestTransport._GetMcpTool._get_response(
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
            resp = resources.McpTool()
            pb_resp = resources.McpTool.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_mcp_tool(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_mcp_tool_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.McpTool.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apiregistry_v1beta.CloudApiRegistryClient.get_mcp_tool",
                    extra={
                        "serviceName": "google.cloud.apiregistry.v1beta.CloudApiRegistry",
                        "rpcName": "GetMcpTool",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListMcpServers(
        _BaseCloudApiRegistryRestTransport._BaseListMcpServers, CloudApiRegistryRestStub
    ):
        def __hash__(self):
            return hash("CloudApiRegistryRestTransport.ListMcpServers")

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
            request: service.ListMcpServersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListMcpServersResponse:
            r"""Call the list mcp servers method over HTTP.

            Args:
                request (~.service.ListMcpServersRequest):
                    The request object. Message for requesting list of
                McpServers
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListMcpServersResponse:
                    Message for response to listing
                McpServers

            """

            http_options = _BaseCloudApiRegistryRestTransport._BaseListMcpServers._get_http_options()
            request, metadata = self._interceptor.pre_list_mcp_servers(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudApiRegistryRestTransport._BaseListMcpServers,
                    "_BaseListMcpServers__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apiregistry_v1beta.CloudApiRegistryClient.ListMcpServers",
                    extra={
                        "serviceName": "google.cloud.apiregistry.v1beta.CloudApiRegistry",
                        "rpcName": "ListMcpServers",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudApiRegistryRestTransport._ListMcpServers._get_response(
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
            resp = service.ListMcpServersResponse()
            pb_resp = service.ListMcpServersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_mcp_servers(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_mcp_servers_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListMcpServersResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apiregistry_v1beta.CloudApiRegistryClient.list_mcp_servers",
                    extra={
                        "serviceName": "google.cloud.apiregistry.v1beta.CloudApiRegistry",
                        "rpcName": "ListMcpServers",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListMcpTools(
        _BaseCloudApiRegistryRestTransport._BaseListMcpTools, CloudApiRegistryRestStub
    ):
        def __hash__(self):
            return hash("CloudApiRegistryRestTransport.ListMcpTools")

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
            request: service.ListMcpToolsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListMcpToolsResponse:
            r"""Call the list mcp tools method over HTTP.

            Args:
                request (~.service.ListMcpToolsRequest):
                    The request object. Message for requesting list of
                McpTools
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListMcpToolsResponse:
                    Message for response to listing
                McpTools

            """

            http_options = (
                _BaseCloudApiRegistryRestTransport._BaseListMcpTools._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_mcp_tools(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudApiRegistryRestTransport._BaseListMcpTools,
                    "_BaseListMcpTools__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apiregistry_v1beta.CloudApiRegistryClient.ListMcpTools",
                    extra={
                        "serviceName": "google.cloud.apiregistry.v1beta.CloudApiRegistry",
                        "rpcName": "ListMcpTools",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudApiRegistryRestTransport._ListMcpTools._get_response(
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
            resp = service.ListMcpToolsResponse()
            pb_resp = service.ListMcpToolsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_mcp_tools(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_mcp_tools_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListMcpToolsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.apiregistry_v1beta.CloudApiRegistryClient.list_mcp_tools",
                    extra={
                        "serviceName": "google.cloud.apiregistry.v1beta.CloudApiRegistry",
                        "rpcName": "ListMcpTools",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def get_mcp_server(
        self,
    ) -> Callable[[service.GetMcpServerRequest], resources.McpServer]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetMcpServer(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_mcp_tool(self) -> Callable[[service.GetMcpToolRequest], resources.McpTool]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetMcpTool(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_mcp_servers(
        self,
    ) -> Callable[[service.ListMcpServersRequest], service.ListMcpServersResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListMcpServers(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_mcp_tools(
        self,
    ) -> Callable[[service.ListMcpToolsRequest], service.ListMcpToolsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListMcpTools(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseCloudApiRegistryRestTransport._BaseGetLocation, CloudApiRegistryRestStub
    ):
        def __hash__(self):
            return hash("CloudApiRegistryRestTransport.GetLocation")

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
                _BaseCloudApiRegistryRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudApiRegistryRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.apiregistry_v1beta.CloudApiRegistryClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.apiregistry.v1beta.CloudApiRegistry",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudApiRegistryRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.apiregistry_v1beta.CloudApiRegistryAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.apiregistry.v1beta.CloudApiRegistry",
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
        _BaseCloudApiRegistryRestTransport._BaseListLocations, CloudApiRegistryRestStub
    ):
        def __hash__(self):
            return hash("CloudApiRegistryRestTransport.ListLocations")

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

            http_options = _BaseCloudApiRegistryRestTransport._BaseListLocations._get_http_options()
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudApiRegistryRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.apiregistry_v1beta.CloudApiRegistryClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.apiregistry.v1beta.CloudApiRegistry",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudApiRegistryRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.apiregistry_v1beta.CloudApiRegistryAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.apiregistry.v1beta.CloudApiRegistry",
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


__all__ = ("CloudApiRegistryRestTransport",)
