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

from google.shopping.merchant_conversions_v1._compat import transcode_request
from google.shopping.merchant_conversions_v1.types import conversionsources

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseConversionSourcesServiceRestTransport

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


class ConversionSourcesServiceRestInterceptor:
    """Interceptor for ConversionSourcesService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the ConversionSourcesServiceRestTransport.

    .. code-block:: python
        class MyCustomConversionSourcesServiceInterceptor(ConversionSourcesServiceRestInterceptor):
            def pre_create_conversion_source(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_conversion_source(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_conversion_source(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_conversion_source(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_conversion_source(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_conversion_sources(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_conversion_sources(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_undelete_conversion_source(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_undelete_conversion_source(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_conversion_source(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_conversion_source(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = ConversionSourcesServiceRestTransport(interceptor=MyCustomConversionSourcesServiceInterceptor())
        client = ConversionSourcesServiceClient(transport=transport)


    """

    def pre_create_conversion_source(
        self,
        request: conversionsources.CreateConversionSourceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        conversionsources.CreateConversionSourceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_conversion_source

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConversionSourcesService server.
        """
        return request, metadata

    def post_create_conversion_source(
        self, response: conversionsources.ConversionSource
    ) -> conversionsources.ConversionSource:
        """Post-rpc interceptor for create_conversion_source

        DEPRECATED. Please use the `post_create_conversion_source_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConversionSourcesService server but before
        it is returned to user code. This `post_create_conversion_source` interceptor runs
        before the `post_create_conversion_source_with_metadata` interceptor.
        """
        return response

    def post_create_conversion_source_with_metadata(
        self,
        response: conversionsources.ConversionSource,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        conversionsources.ConversionSource, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for create_conversion_source

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConversionSourcesService server but before it is returned to user code.

        We recommend only using this `post_create_conversion_source_with_metadata`
        interceptor in new development instead of the `post_create_conversion_source` interceptor.
        When both interceptors are used, this `post_create_conversion_source_with_metadata` interceptor runs after the
        `post_create_conversion_source` interceptor. The (possibly modified) response returned by
        `post_create_conversion_source` will be passed to
        `post_create_conversion_source_with_metadata`.
        """
        return response, metadata

    def pre_delete_conversion_source(
        self,
        request: conversionsources.DeleteConversionSourceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        conversionsources.DeleteConversionSourceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_conversion_source

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConversionSourcesService server.
        """
        return request, metadata

    def pre_get_conversion_source(
        self,
        request: conversionsources.GetConversionSourceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        conversionsources.GetConversionSourceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_conversion_source

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConversionSourcesService server.
        """
        return request, metadata

    def post_get_conversion_source(
        self, response: conversionsources.ConversionSource
    ) -> conversionsources.ConversionSource:
        """Post-rpc interceptor for get_conversion_source

        DEPRECATED. Please use the `post_get_conversion_source_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConversionSourcesService server but before
        it is returned to user code. This `post_get_conversion_source` interceptor runs
        before the `post_get_conversion_source_with_metadata` interceptor.
        """
        return response

    def post_get_conversion_source_with_metadata(
        self,
        response: conversionsources.ConversionSource,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        conversionsources.ConversionSource, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_conversion_source

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConversionSourcesService server but before it is returned to user code.

        We recommend only using this `post_get_conversion_source_with_metadata`
        interceptor in new development instead of the `post_get_conversion_source` interceptor.
        When both interceptors are used, this `post_get_conversion_source_with_metadata` interceptor runs after the
        `post_get_conversion_source` interceptor. The (possibly modified) response returned by
        `post_get_conversion_source` will be passed to
        `post_get_conversion_source_with_metadata`.
        """
        return response, metadata

    def pre_list_conversion_sources(
        self,
        request: conversionsources.ListConversionSourcesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        conversionsources.ListConversionSourcesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_conversion_sources

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConversionSourcesService server.
        """
        return request, metadata

    def post_list_conversion_sources(
        self, response: conversionsources.ListConversionSourcesResponse
    ) -> conversionsources.ListConversionSourcesResponse:
        """Post-rpc interceptor for list_conversion_sources

        DEPRECATED. Please use the `post_list_conversion_sources_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConversionSourcesService server but before
        it is returned to user code. This `post_list_conversion_sources` interceptor runs
        before the `post_list_conversion_sources_with_metadata` interceptor.
        """
        return response

    def post_list_conversion_sources_with_metadata(
        self,
        response: conversionsources.ListConversionSourcesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        conversionsources.ListConversionSourcesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_conversion_sources

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConversionSourcesService server but before it is returned to user code.

        We recommend only using this `post_list_conversion_sources_with_metadata`
        interceptor in new development instead of the `post_list_conversion_sources` interceptor.
        When both interceptors are used, this `post_list_conversion_sources_with_metadata` interceptor runs after the
        `post_list_conversion_sources` interceptor. The (possibly modified) response returned by
        `post_list_conversion_sources` will be passed to
        `post_list_conversion_sources_with_metadata`.
        """
        return response, metadata

    def pre_undelete_conversion_source(
        self,
        request: conversionsources.UndeleteConversionSourceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        conversionsources.UndeleteConversionSourceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for undelete_conversion_source

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConversionSourcesService server.
        """
        return request, metadata

    def post_undelete_conversion_source(
        self, response: conversionsources.ConversionSource
    ) -> conversionsources.ConversionSource:
        """Post-rpc interceptor for undelete_conversion_source

        DEPRECATED. Please use the `post_undelete_conversion_source_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConversionSourcesService server but before
        it is returned to user code. This `post_undelete_conversion_source` interceptor runs
        before the `post_undelete_conversion_source_with_metadata` interceptor.
        """
        return response

    def post_undelete_conversion_source_with_metadata(
        self,
        response: conversionsources.ConversionSource,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        conversionsources.ConversionSource, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for undelete_conversion_source

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConversionSourcesService server but before it is returned to user code.

        We recommend only using this `post_undelete_conversion_source_with_metadata`
        interceptor in new development instead of the `post_undelete_conversion_source` interceptor.
        When both interceptors are used, this `post_undelete_conversion_source_with_metadata` interceptor runs after the
        `post_undelete_conversion_source` interceptor. The (possibly modified) response returned by
        `post_undelete_conversion_source` will be passed to
        `post_undelete_conversion_source_with_metadata`.
        """
        return response, metadata

    def pre_update_conversion_source(
        self,
        request: conversionsources.UpdateConversionSourceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        conversionsources.UpdateConversionSourceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_conversion_source

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ConversionSourcesService server.
        """
        return request, metadata

    def post_update_conversion_source(
        self, response: conversionsources.ConversionSource
    ) -> conversionsources.ConversionSource:
        """Post-rpc interceptor for update_conversion_source

        DEPRECATED. Please use the `post_update_conversion_source_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ConversionSourcesService server but before
        it is returned to user code. This `post_update_conversion_source` interceptor runs
        before the `post_update_conversion_source_with_metadata` interceptor.
        """
        return response

    def post_update_conversion_source_with_metadata(
        self,
        response: conversionsources.ConversionSource,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        conversionsources.ConversionSource, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for update_conversion_source

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ConversionSourcesService server but before it is returned to user code.

        We recommend only using this `post_update_conversion_source_with_metadata`
        interceptor in new development instead of the `post_update_conversion_source` interceptor.
        When both interceptors are used, this `post_update_conversion_source_with_metadata` interceptor runs after the
        `post_update_conversion_source` interceptor. The (possibly modified) response returned by
        `post_update_conversion_source` will be passed to
        `post_update_conversion_source_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class ConversionSourcesServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: ConversionSourcesServiceRestInterceptor


class ConversionSourcesServiceRestTransport(_BaseConversionSourcesServiceRestTransport):
    """REST backend synchronous transport for ConversionSourcesService.

    Service for managing conversion sources for a merchant
    account.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "merchantapi.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[ConversionSourcesServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'merchantapi.googleapis.com').
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
            interceptor (Optional[ConversionSourcesServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or ConversionSourcesServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CreateConversionSource(
        _BaseConversionSourcesServiceRestTransport._BaseCreateConversionSource,
        ConversionSourcesServiceRestStub,
    ):
        def __hash__(self):
            return hash("ConversionSourcesServiceRestTransport.CreateConversionSource")

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
            request: conversionsources.CreateConversionSourceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> conversionsources.ConversionSource:
            r"""Call the create conversion source method over HTTP.

            Args:
                request (~.conversionsources.CreateConversionSourceRequest):
                    The request object. Request message for the
                CreateConversionSource method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.conversionsources.ConversionSource:
                    Represents a conversion source owned
                by a Merchant account. A merchant
                account can have up to 200 conversion
                sources.

            """

            http_options = _BaseConversionSourcesServiceRestTransport._BaseCreateConversionSource._get_http_options()
            request, metadata = self._interceptor.pre_create_conversion_source(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConversionSourcesServiceRestTransport._BaseCreateConversionSource,
                    "_BaseCreateConversionSource__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.conversions_v1.ConversionSourcesServiceClient.CreateConversionSource",
                    extra={
                        "serviceName": "google.shopping.merchant.conversions.v1.ConversionSourcesService",
                        "rpcName": "CreateConversionSource",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConversionSourcesServiceRestTransport._CreateConversionSource._get_response(
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
            resp = conversionsources.ConversionSource()
            pb_resp = conversionsources.ConversionSource.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_conversion_source(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_conversion_source_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = conversionsources.ConversionSource.to_json(
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
                    "Received response for google.shopping.merchant.conversions_v1.ConversionSourcesServiceClient.create_conversion_source",
                    extra={
                        "serviceName": "google.shopping.merchant.conversions.v1.ConversionSourcesService",
                        "rpcName": "CreateConversionSource",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteConversionSource(
        _BaseConversionSourcesServiceRestTransport._BaseDeleteConversionSource,
        ConversionSourcesServiceRestStub,
    ):
        def __hash__(self):
            return hash("ConversionSourcesServiceRestTransport.DeleteConversionSource")

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
            request: conversionsources.DeleteConversionSourceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete conversion source method over HTTP.

            Args:
                request (~.conversionsources.DeleteConversionSourceRequest):
                    The request object. Request message for the
                DeleteConversionSource method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseConversionSourcesServiceRestTransport._BaseDeleteConversionSource._get_http_options()
            request, metadata = self._interceptor.pre_delete_conversion_source(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConversionSourcesServiceRestTransport._BaseDeleteConversionSource,
                    "_BaseDeleteConversionSource__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.conversions_v1.ConversionSourcesServiceClient.DeleteConversionSource",
                    extra={
                        "serviceName": "google.shopping.merchant.conversions.v1.ConversionSourcesService",
                        "rpcName": "DeleteConversionSource",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConversionSourcesServiceRestTransport._DeleteConversionSource._get_response(
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

    class _GetConversionSource(
        _BaseConversionSourcesServiceRestTransport._BaseGetConversionSource,
        ConversionSourcesServiceRestStub,
    ):
        def __hash__(self):
            return hash("ConversionSourcesServiceRestTransport.GetConversionSource")

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
            request: conversionsources.GetConversionSourceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> conversionsources.ConversionSource:
            r"""Call the get conversion source method over HTTP.

            Args:
                request (~.conversionsources.GetConversionSourceRequest):
                    The request object. Request message for the
                GetConversionSource method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.conversionsources.ConversionSource:
                    Represents a conversion source owned
                by a Merchant account. A merchant
                account can have up to 200 conversion
                sources.

            """

            http_options = _BaseConversionSourcesServiceRestTransport._BaseGetConversionSource._get_http_options()
            request, metadata = self._interceptor.pre_get_conversion_source(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConversionSourcesServiceRestTransport._BaseGetConversionSource,
                    "_BaseGetConversionSource__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.conversions_v1.ConversionSourcesServiceClient.GetConversionSource",
                    extra={
                        "serviceName": "google.shopping.merchant.conversions.v1.ConversionSourcesService",
                        "rpcName": "GetConversionSource",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConversionSourcesServiceRestTransport._GetConversionSource._get_response(
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
            resp = conversionsources.ConversionSource()
            pb_resp = conversionsources.ConversionSource.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_conversion_source(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_conversion_source_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = conversionsources.ConversionSource.to_json(
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
                    "Received response for google.shopping.merchant.conversions_v1.ConversionSourcesServiceClient.get_conversion_source",
                    extra={
                        "serviceName": "google.shopping.merchant.conversions.v1.ConversionSourcesService",
                        "rpcName": "GetConversionSource",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListConversionSources(
        _BaseConversionSourcesServiceRestTransport._BaseListConversionSources,
        ConversionSourcesServiceRestStub,
    ):
        def __hash__(self):
            return hash("ConversionSourcesServiceRestTransport.ListConversionSources")

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
            request: conversionsources.ListConversionSourcesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> conversionsources.ListConversionSourcesResponse:
            r"""Call the list conversion sources method over HTTP.

            Args:
                request (~.conversionsources.ListConversionSourcesRequest):
                    The request object. Request message for the
                ListConversionSources method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.conversionsources.ListConversionSourcesResponse:
                    Response message for the
                ListConversionSources method.

            """

            http_options = _BaseConversionSourcesServiceRestTransport._BaseListConversionSources._get_http_options()
            request, metadata = self._interceptor.pre_list_conversion_sources(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConversionSourcesServiceRestTransport._BaseListConversionSources,
                    "_BaseListConversionSources__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.conversions_v1.ConversionSourcesServiceClient.ListConversionSources",
                    extra={
                        "serviceName": "google.shopping.merchant.conversions.v1.ConversionSourcesService",
                        "rpcName": "ListConversionSources",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConversionSourcesServiceRestTransport._ListConversionSources._get_response(
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
            resp = conversionsources.ListConversionSourcesResponse()
            pb_resp = conversionsources.ListConversionSourcesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_conversion_sources(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_conversion_sources_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        conversionsources.ListConversionSourcesResponse.to_json(
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
                    "Received response for google.shopping.merchant.conversions_v1.ConversionSourcesServiceClient.list_conversion_sources",
                    extra={
                        "serviceName": "google.shopping.merchant.conversions.v1.ConversionSourcesService",
                        "rpcName": "ListConversionSources",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UndeleteConversionSource(
        _BaseConversionSourcesServiceRestTransport._BaseUndeleteConversionSource,
        ConversionSourcesServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "ConversionSourcesServiceRestTransport.UndeleteConversionSource"
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
            request: conversionsources.UndeleteConversionSourceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> conversionsources.ConversionSource:
            r"""Call the undelete conversion
            source method over HTTP.

                Args:
                    request (~.conversionsources.UndeleteConversionSourceRequest):
                        The request object. Request message for the
                    UndeleteConversionSource method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.conversionsources.ConversionSource:
                        Represents a conversion source owned
                    by a Merchant account. A merchant
                    account can have up to 200 conversion
                    sources.

            """

            http_options = _BaseConversionSourcesServiceRestTransport._BaseUndeleteConversionSource._get_http_options()
            request, metadata = self._interceptor.pre_undelete_conversion_source(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConversionSourcesServiceRestTransport._BaseUndeleteConversionSource,
                    "_BaseUndeleteConversionSource__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.conversions_v1.ConversionSourcesServiceClient.UndeleteConversionSource",
                    extra={
                        "serviceName": "google.shopping.merchant.conversions.v1.ConversionSourcesService",
                        "rpcName": "UndeleteConversionSource",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConversionSourcesServiceRestTransport._UndeleteConversionSource._get_response(
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
            resp = conversionsources.ConversionSource()
            pb_resp = conversionsources.ConversionSource.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_undelete_conversion_source(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_undelete_conversion_source_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = conversionsources.ConversionSource.to_json(
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
                    "Received response for google.shopping.merchant.conversions_v1.ConversionSourcesServiceClient.undelete_conversion_source",
                    extra={
                        "serviceName": "google.shopping.merchant.conversions.v1.ConversionSourcesService",
                        "rpcName": "UndeleteConversionSource",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateConversionSource(
        _BaseConversionSourcesServiceRestTransport._BaseUpdateConversionSource,
        ConversionSourcesServiceRestStub,
    ):
        def __hash__(self):
            return hash("ConversionSourcesServiceRestTransport.UpdateConversionSource")

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
            request: conversionsources.UpdateConversionSourceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> conversionsources.ConversionSource:
            r"""Call the update conversion source method over HTTP.

            Args:
                request (~.conversionsources.UpdateConversionSourceRequest):
                    The request object. Request message for the
                UpdateConversionSource method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.conversionsources.ConversionSource:
                    Represents a conversion source owned
                by a Merchant account. A merchant
                account can have up to 200 conversion
                sources.

            """

            http_options = _BaseConversionSourcesServiceRestTransport._BaseUpdateConversionSource._get_http_options()
            request, metadata = self._interceptor.pre_update_conversion_source(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConversionSourcesServiceRestTransport._BaseUpdateConversionSource,
                    "_BaseUpdateConversionSource__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.conversions_v1.ConversionSourcesServiceClient.UpdateConversionSource",
                    extra={
                        "serviceName": "google.shopping.merchant.conversions.v1.ConversionSourcesService",
                        "rpcName": "UpdateConversionSource",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConversionSourcesServiceRestTransport._UpdateConversionSource._get_response(
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
            resp = conversionsources.ConversionSource()
            pb_resp = conversionsources.ConversionSource.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_conversion_source(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_conversion_source_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = conversionsources.ConversionSource.to_json(
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
                    "Received response for google.shopping.merchant.conversions_v1.ConversionSourcesServiceClient.update_conversion_source",
                    extra={
                        "serviceName": "google.shopping.merchant.conversions.v1.ConversionSourcesService",
                        "rpcName": "UpdateConversionSource",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_conversion_source(
        self,
    ) -> Callable[
        [conversionsources.CreateConversionSourceRequest],
        conversionsources.ConversionSource,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateConversionSource(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_conversion_source(
        self,
    ) -> Callable[[conversionsources.DeleteConversionSourceRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteConversionSource(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_conversion_source(
        self,
    ) -> Callable[
        [conversionsources.GetConversionSourceRequest],
        conversionsources.ConversionSource,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetConversionSource(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_conversion_sources(
        self,
    ) -> Callable[
        [conversionsources.ListConversionSourcesRequest],
        conversionsources.ListConversionSourcesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListConversionSources(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def undelete_conversion_source(
        self,
    ) -> Callable[
        [conversionsources.UndeleteConversionSourceRequest],
        conversionsources.ConversionSource,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UndeleteConversionSource(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_conversion_source(
        self,
    ) -> Callable[
        [conversionsources.UpdateConversionSourceRequest],
        conversionsources.ConversionSource,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateConversionSource(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("ConversionSourcesServiceRestTransport",)
