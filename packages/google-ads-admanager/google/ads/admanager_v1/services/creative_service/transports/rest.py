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
from google.ads.admanager_v1.types import creative_messages, creative_service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseCreativeServiceRestTransport

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


class CreativeServiceRestInterceptor:
    """Interceptor for CreativeService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the CreativeServiceRestTransport.

    .. code-block:: python
        class MyCustomCreativeServiceInterceptor(CreativeServiceRestInterceptor):
            def pre_batch_activate_creatives(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_activate_creatives(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_deactivate_creatives(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_deactivate_creatives(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_creative(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_creative(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_creatives(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_creatives(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = CreativeServiceRestTransport(interceptor=MyCustomCreativeServiceInterceptor())
        client = CreativeServiceClient(transport=transport)


    """

    def pre_batch_activate_creatives(
        self,
        request: creative_service.BatchActivateCreativesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        creative_service.BatchActivateCreativesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_activate_creatives

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CreativeService server.
        """
        return request, metadata

    def post_batch_activate_creatives(
        self, response: creative_service.BatchActivateCreativesResponse
    ) -> creative_service.BatchActivateCreativesResponse:
        """Post-rpc interceptor for batch_activate_creatives

        DEPRECATED. Please use the `post_batch_activate_creatives_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CreativeService server but before
        it is returned to user code. This `post_batch_activate_creatives` interceptor runs
        before the `post_batch_activate_creatives_with_metadata` interceptor.
        """
        return response

    def post_batch_activate_creatives_with_metadata(
        self,
        response: creative_service.BatchActivateCreativesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        creative_service.BatchActivateCreativesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_activate_creatives

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CreativeService server but before it is returned to user code.

        We recommend only using this `post_batch_activate_creatives_with_metadata`
        interceptor in new development instead of the `post_batch_activate_creatives` interceptor.
        When both interceptors are used, this `post_batch_activate_creatives_with_metadata` interceptor runs after the
        `post_batch_activate_creatives` interceptor. The (possibly modified) response returned by
        `post_batch_activate_creatives` will be passed to
        `post_batch_activate_creatives_with_metadata`.
        """
        return response, metadata

    def pre_batch_deactivate_creatives(
        self,
        request: creative_service.BatchDeactivateCreativesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        creative_service.BatchDeactivateCreativesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_deactivate_creatives

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CreativeService server.
        """
        return request, metadata

    def post_batch_deactivate_creatives(
        self, response: creative_service.BatchDeactivateCreativesResponse
    ) -> creative_service.BatchDeactivateCreativesResponse:
        """Post-rpc interceptor for batch_deactivate_creatives

        DEPRECATED. Please use the `post_batch_deactivate_creatives_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CreativeService server but before
        it is returned to user code. This `post_batch_deactivate_creatives` interceptor runs
        before the `post_batch_deactivate_creatives_with_metadata` interceptor.
        """
        return response

    def post_batch_deactivate_creatives_with_metadata(
        self,
        response: creative_service.BatchDeactivateCreativesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        creative_service.BatchDeactivateCreativesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_deactivate_creatives

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CreativeService server but before it is returned to user code.

        We recommend only using this `post_batch_deactivate_creatives_with_metadata`
        interceptor in new development instead of the `post_batch_deactivate_creatives` interceptor.
        When both interceptors are used, this `post_batch_deactivate_creatives_with_metadata` interceptor runs after the
        `post_batch_deactivate_creatives` interceptor. The (possibly modified) response returned by
        `post_batch_deactivate_creatives` will be passed to
        `post_batch_deactivate_creatives_with_metadata`.
        """
        return response, metadata

    def pre_get_creative(
        self,
        request: creative_service.GetCreativeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        creative_service.GetCreativeRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_creative

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CreativeService server.
        """
        return request, metadata

    def post_get_creative(
        self, response: creative_messages.Creative
    ) -> creative_messages.Creative:
        """Post-rpc interceptor for get_creative

        DEPRECATED. Please use the `post_get_creative_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CreativeService server but before
        it is returned to user code. This `post_get_creative` interceptor runs
        before the `post_get_creative_with_metadata` interceptor.
        """
        return response

    def post_get_creative_with_metadata(
        self,
        response: creative_messages.Creative,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[creative_messages.Creative, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_creative

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CreativeService server but before it is returned to user code.

        We recommend only using this `post_get_creative_with_metadata`
        interceptor in new development instead of the `post_get_creative` interceptor.
        When both interceptors are used, this `post_get_creative_with_metadata` interceptor runs after the
        `post_get_creative` interceptor. The (possibly modified) response returned by
        `post_get_creative` will be passed to
        `post_get_creative_with_metadata`.
        """
        return response, metadata

    def pre_list_creatives(
        self,
        request: creative_service.ListCreativesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        creative_service.ListCreativesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_creatives

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CreativeService server.
        """
        return request, metadata

    def post_list_creatives(
        self, response: creative_service.ListCreativesResponse
    ) -> creative_service.ListCreativesResponse:
        """Post-rpc interceptor for list_creatives

        DEPRECATED. Please use the `post_list_creatives_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CreativeService server but before
        it is returned to user code. This `post_list_creatives` interceptor runs
        before the `post_list_creatives_with_metadata` interceptor.
        """
        return response

    def post_list_creatives_with_metadata(
        self,
        response: creative_service.ListCreativesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        creative_service.ListCreativesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_creatives

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CreativeService server but before it is returned to user code.

        We recommend only using this `post_list_creatives_with_metadata`
        interceptor in new development instead of the `post_list_creatives` interceptor.
        When both interceptors are used, this `post_list_creatives_with_metadata` interceptor runs after the
        `post_list_creatives` interceptor. The (possibly modified) response returned by
        `post_list_creatives` will be passed to
        `post_list_creatives_with_metadata`.
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
        before they are sent to the CreativeService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the CreativeService server but before
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
        before they are sent to the CreativeService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the CreativeService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class CreativeServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: CreativeServiceRestInterceptor


class CreativeServiceRestTransport(_BaseCreativeServiceRestTransport):
    """REST backend synchronous transport for CreativeService.

    Provides methods for handling ``Creative`` objects.

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
        interceptor: Optional[CreativeServiceRestInterceptor] = None,
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
            interceptor (Optional[CreativeServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or CreativeServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _BatchActivateCreatives(
        _BaseCreativeServiceRestTransport._BaseBatchActivateCreatives,
        CreativeServiceRestStub,
    ):
        def __hash__(self):
            return hash("CreativeServiceRestTransport.BatchActivateCreatives")

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
            request: creative_service.BatchActivateCreativesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> creative_service.BatchActivateCreativesResponse:
            r"""Call the batch activate creatives method over HTTP.

            Args:
                request (~.creative_service.BatchActivateCreativesRequest):
                    The request object. Request object for ``BatchActivateCreatives`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.creative_service.BatchActivateCreativesResponse:
                    Response object for ``BatchActivateCreatives`` method.
            """

            http_options = _BaseCreativeServiceRestTransport._BaseBatchActivateCreatives._get_http_options()
            request, metadata = self._interceptor.pre_batch_activate_creatives(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCreativeServiceRestTransport._BaseBatchActivateCreatives,
                    "_BaseBatchActivateCreatives__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CreativeServiceClient.BatchActivateCreatives",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CreativeService",
                        "rpcName": "BatchActivateCreatives",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CreativeServiceRestTransport._BatchActivateCreatives._get_response(
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
            resp = creative_service.BatchActivateCreativesResponse()
            pb_resp = creative_service.BatchActivateCreativesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_activate_creatives(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_activate_creatives_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        creative_service.BatchActivateCreativesResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.CreativeServiceClient.batch_activate_creatives",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CreativeService",
                        "rpcName": "BatchActivateCreatives",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchDeactivateCreatives(
        _BaseCreativeServiceRestTransport._BaseBatchDeactivateCreatives,
        CreativeServiceRestStub,
    ):
        def __hash__(self):
            return hash("CreativeServiceRestTransport.BatchDeactivateCreatives")

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
            request: creative_service.BatchDeactivateCreativesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> creative_service.BatchDeactivateCreativesResponse:
            r"""Call the batch deactivate
            creatives method over HTTP.

                Args:
                    request (~.creative_service.BatchDeactivateCreativesRequest):
                        The request object. Request object for ``BatchDeactivateCreatives`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.creative_service.BatchDeactivateCreativesResponse:
                        Response object for ``BatchDeactivateCreatives`` method.
            """

            http_options = _BaseCreativeServiceRestTransport._BaseBatchDeactivateCreatives._get_http_options()
            request, metadata = self._interceptor.pre_batch_deactivate_creatives(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCreativeServiceRestTransport._BaseBatchDeactivateCreatives,
                    "_BaseBatchDeactivateCreatives__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CreativeServiceClient.BatchDeactivateCreatives",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CreativeService",
                        "rpcName": "BatchDeactivateCreatives",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CreativeServiceRestTransport._BatchDeactivateCreatives._get_response(
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
            resp = creative_service.BatchDeactivateCreativesResponse()
            pb_resp = creative_service.BatchDeactivateCreativesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_deactivate_creatives(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_deactivate_creatives_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        creative_service.BatchDeactivateCreativesResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.CreativeServiceClient.batch_deactivate_creatives",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CreativeService",
                        "rpcName": "BatchDeactivateCreatives",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetCreative(
        _BaseCreativeServiceRestTransport._BaseGetCreative, CreativeServiceRestStub
    ):
        def __hash__(self):
            return hash("CreativeServiceRestTransport.GetCreative")

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
            request: creative_service.GetCreativeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> creative_messages.Creative:
            r"""Call the get creative method over HTTP.

            Args:
                request (~.creative_service.GetCreativeRequest):
                    The request object. Request object for ``GetCreative`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.creative_messages.Creative:
                    The Creative resource.
            """

            http_options = (
                _BaseCreativeServiceRestTransport._BaseGetCreative._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_creative(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCreativeServiceRestTransport._BaseGetCreative,
                    "_BaseGetCreative__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CreativeServiceClient.GetCreative",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CreativeService",
                        "rpcName": "GetCreative",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CreativeServiceRestTransport._GetCreative._get_response(
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
            resp = creative_messages.Creative()
            pb_resp = creative_messages.Creative.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_creative(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_creative_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = creative_messages.Creative.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.CreativeServiceClient.get_creative",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CreativeService",
                        "rpcName": "GetCreative",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListCreatives(
        _BaseCreativeServiceRestTransport._BaseListCreatives, CreativeServiceRestStub
    ):
        def __hash__(self):
            return hash("CreativeServiceRestTransport.ListCreatives")

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
            request: creative_service.ListCreativesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> creative_service.ListCreativesResponse:
            r"""Call the list creatives method over HTTP.

            Args:
                request (~.creative_service.ListCreativesRequest):
                    The request object. Request object for ``ListCreatives`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.creative_service.ListCreativesResponse:
                    Response object for ``ListCreativesRequest`` containing
                matching ``Creative`` objects.

            """

            http_options = (
                _BaseCreativeServiceRestTransport._BaseListCreatives._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_creatives(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCreativeServiceRestTransport._BaseListCreatives,
                    "_BaseListCreatives__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CreativeServiceClient.ListCreatives",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CreativeService",
                        "rpcName": "ListCreatives",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CreativeServiceRestTransport._ListCreatives._get_response(
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
            resp = creative_service.ListCreativesResponse()
            pb_resp = creative_service.ListCreativesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_creatives(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_creatives_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = creative_service.ListCreativesResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.CreativeServiceClient.list_creatives",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CreativeService",
                        "rpcName": "ListCreatives",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_activate_creatives(
        self,
    ) -> Callable[
        [creative_service.BatchActivateCreativesRequest],
        creative_service.BatchActivateCreativesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchActivateCreatives(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_deactivate_creatives(
        self,
    ) -> Callable[
        [creative_service.BatchDeactivateCreativesRequest],
        creative_service.BatchDeactivateCreativesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchDeactivateCreatives(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_creative(
        self,
    ) -> Callable[[creative_service.GetCreativeRequest], creative_messages.Creative]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetCreative(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_creatives(
        self,
    ) -> Callable[
        [creative_service.ListCreativesRequest], creative_service.ListCreativesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListCreatives(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseCreativeServiceRestTransport._BaseCancelOperation, CreativeServiceRestStub
    ):
        def __hash__(self):
            return hash("CreativeServiceRestTransport.CancelOperation")

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

            http_options = _BaseCreativeServiceRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCreativeServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.ads.admanager_v1.CreativeServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CreativeService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CreativeServiceRestTransport._CancelOperation._get_response(
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
        _BaseCreativeServiceRestTransport._BaseGetOperation, CreativeServiceRestStub
    ):
        def __hash__(self):
            return hash("CreativeServiceRestTransport.GetOperation")

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
                _BaseCreativeServiceRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCreativeServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.ads.admanager_v1.CreativeServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CreativeService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CreativeServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.ads.admanager_v1.CreativeServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CreativeService",
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


__all__ = ("CreativeServiceRestTransport",)
