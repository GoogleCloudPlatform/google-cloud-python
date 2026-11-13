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
from google.ads.admanager_v1.types import ad_spot_messages, ad_spot_service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseAdSpotServiceRestTransport

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


class AdSpotServiceRestInterceptor:
    """Interceptor for AdSpotService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the AdSpotServiceRestTransport.

    .. code-block:: python
        class MyCustomAdSpotServiceInterceptor(AdSpotServiceRestInterceptor):
            def pre_batch_create_ad_spots(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_create_ad_spots(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_update_ad_spots(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_update_ad_spots(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_ad_spot(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_ad_spot(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_ad_spot(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_ad_spot(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_ad_spots(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_ad_spots(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_ad_spot(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_ad_spot(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = AdSpotServiceRestTransport(interceptor=MyCustomAdSpotServiceInterceptor())
        client = AdSpotServiceClient(transport=transport)


    """

    def pre_batch_create_ad_spots(
        self,
        request: ad_spot_service.BatchCreateAdSpotsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_spot_service.BatchCreateAdSpotsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_create_ad_spots

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AdSpotService server.
        """
        return request, metadata

    def post_batch_create_ad_spots(
        self, response: ad_spot_service.BatchCreateAdSpotsResponse
    ) -> ad_spot_service.BatchCreateAdSpotsResponse:
        """Post-rpc interceptor for batch_create_ad_spots

        DEPRECATED. Please use the `post_batch_create_ad_spots_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AdSpotService server but before
        it is returned to user code. This `post_batch_create_ad_spots` interceptor runs
        before the `post_batch_create_ad_spots_with_metadata` interceptor.
        """
        return response

    def post_batch_create_ad_spots_with_metadata(
        self,
        response: ad_spot_service.BatchCreateAdSpotsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_spot_service.BatchCreateAdSpotsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_create_ad_spots

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AdSpotService server but before it is returned to user code.

        We recommend only using this `post_batch_create_ad_spots_with_metadata`
        interceptor in new development instead of the `post_batch_create_ad_spots` interceptor.
        When both interceptors are used, this `post_batch_create_ad_spots_with_metadata` interceptor runs after the
        `post_batch_create_ad_spots` interceptor. The (possibly modified) response returned by
        `post_batch_create_ad_spots` will be passed to
        `post_batch_create_ad_spots_with_metadata`.
        """
        return response, metadata

    def pre_batch_update_ad_spots(
        self,
        request: ad_spot_service.BatchUpdateAdSpotsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_spot_service.BatchUpdateAdSpotsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_update_ad_spots

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AdSpotService server.
        """
        return request, metadata

    def post_batch_update_ad_spots(
        self, response: ad_spot_service.BatchUpdateAdSpotsResponse
    ) -> ad_spot_service.BatchUpdateAdSpotsResponse:
        """Post-rpc interceptor for batch_update_ad_spots

        DEPRECATED. Please use the `post_batch_update_ad_spots_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AdSpotService server but before
        it is returned to user code. This `post_batch_update_ad_spots` interceptor runs
        before the `post_batch_update_ad_spots_with_metadata` interceptor.
        """
        return response

    def post_batch_update_ad_spots_with_metadata(
        self,
        response: ad_spot_service.BatchUpdateAdSpotsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_spot_service.BatchUpdateAdSpotsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_update_ad_spots

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AdSpotService server but before it is returned to user code.

        We recommend only using this `post_batch_update_ad_spots_with_metadata`
        interceptor in new development instead of the `post_batch_update_ad_spots` interceptor.
        When both interceptors are used, this `post_batch_update_ad_spots_with_metadata` interceptor runs after the
        `post_batch_update_ad_spots` interceptor. The (possibly modified) response returned by
        `post_batch_update_ad_spots` will be passed to
        `post_batch_update_ad_spots_with_metadata`.
        """
        return response, metadata

    def pre_create_ad_spot(
        self,
        request: ad_spot_service.CreateAdSpotRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_spot_service.CreateAdSpotRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_ad_spot

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AdSpotService server.
        """
        return request, metadata

    def post_create_ad_spot(
        self, response: ad_spot_messages.AdSpot
    ) -> ad_spot_messages.AdSpot:
        """Post-rpc interceptor for create_ad_spot

        DEPRECATED. Please use the `post_create_ad_spot_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AdSpotService server but before
        it is returned to user code. This `post_create_ad_spot` interceptor runs
        before the `post_create_ad_spot_with_metadata` interceptor.
        """
        return response

    def post_create_ad_spot_with_metadata(
        self,
        response: ad_spot_messages.AdSpot,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[ad_spot_messages.AdSpot, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_ad_spot

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AdSpotService server but before it is returned to user code.

        We recommend only using this `post_create_ad_spot_with_metadata`
        interceptor in new development instead of the `post_create_ad_spot` interceptor.
        When both interceptors are used, this `post_create_ad_spot_with_metadata` interceptor runs after the
        `post_create_ad_spot` interceptor. The (possibly modified) response returned by
        `post_create_ad_spot` will be passed to
        `post_create_ad_spot_with_metadata`.
        """
        return response, metadata

    def pre_get_ad_spot(
        self,
        request: ad_spot_service.GetAdSpotRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_spot_service.GetAdSpotRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_ad_spot

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AdSpotService server.
        """
        return request, metadata

    def post_get_ad_spot(
        self, response: ad_spot_messages.AdSpot
    ) -> ad_spot_messages.AdSpot:
        """Post-rpc interceptor for get_ad_spot

        DEPRECATED. Please use the `post_get_ad_spot_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AdSpotService server but before
        it is returned to user code. This `post_get_ad_spot` interceptor runs
        before the `post_get_ad_spot_with_metadata` interceptor.
        """
        return response

    def post_get_ad_spot_with_metadata(
        self,
        response: ad_spot_messages.AdSpot,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[ad_spot_messages.AdSpot, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_ad_spot

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AdSpotService server but before it is returned to user code.

        We recommend only using this `post_get_ad_spot_with_metadata`
        interceptor in new development instead of the `post_get_ad_spot` interceptor.
        When both interceptors are used, this `post_get_ad_spot_with_metadata` interceptor runs after the
        `post_get_ad_spot` interceptor. The (possibly modified) response returned by
        `post_get_ad_spot` will be passed to
        `post_get_ad_spot_with_metadata`.
        """
        return response, metadata

    def pre_list_ad_spots(
        self,
        request: ad_spot_service.ListAdSpotsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_spot_service.ListAdSpotsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_ad_spots

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AdSpotService server.
        """
        return request, metadata

    def post_list_ad_spots(
        self, response: ad_spot_service.ListAdSpotsResponse
    ) -> ad_spot_service.ListAdSpotsResponse:
        """Post-rpc interceptor for list_ad_spots

        DEPRECATED. Please use the `post_list_ad_spots_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AdSpotService server but before
        it is returned to user code. This `post_list_ad_spots` interceptor runs
        before the `post_list_ad_spots_with_metadata` interceptor.
        """
        return response

    def post_list_ad_spots_with_metadata(
        self,
        response: ad_spot_service.ListAdSpotsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_spot_service.ListAdSpotsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_ad_spots

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AdSpotService server but before it is returned to user code.

        We recommend only using this `post_list_ad_spots_with_metadata`
        interceptor in new development instead of the `post_list_ad_spots` interceptor.
        When both interceptors are used, this `post_list_ad_spots_with_metadata` interceptor runs after the
        `post_list_ad_spots` interceptor. The (possibly modified) response returned by
        `post_list_ad_spots` will be passed to
        `post_list_ad_spots_with_metadata`.
        """
        return response, metadata

    def pre_update_ad_spot(
        self,
        request: ad_spot_service.UpdateAdSpotRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_spot_service.UpdateAdSpotRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_ad_spot

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AdSpotService server.
        """
        return request, metadata

    def post_update_ad_spot(
        self, response: ad_spot_messages.AdSpot
    ) -> ad_spot_messages.AdSpot:
        """Post-rpc interceptor for update_ad_spot

        DEPRECATED. Please use the `post_update_ad_spot_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AdSpotService server but before
        it is returned to user code. This `post_update_ad_spot` interceptor runs
        before the `post_update_ad_spot_with_metadata` interceptor.
        """
        return response

    def post_update_ad_spot_with_metadata(
        self,
        response: ad_spot_messages.AdSpot,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[ad_spot_messages.AdSpot, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_ad_spot

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AdSpotService server but before it is returned to user code.

        We recommend only using this `post_update_ad_spot_with_metadata`
        interceptor in new development instead of the `post_update_ad_spot` interceptor.
        When both interceptors are used, this `post_update_ad_spot_with_metadata` interceptor runs after the
        `post_update_ad_spot` interceptor. The (possibly modified) response returned by
        `post_update_ad_spot` will be passed to
        `post_update_ad_spot_with_metadata`.
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
        before they are sent to the AdSpotService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the AdSpotService server but before
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
        before they are sent to the AdSpotService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the AdSpotService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class AdSpotServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: AdSpotServiceRestInterceptor


class AdSpotServiceRestTransport(_BaseAdSpotServiceRestTransport):
    """REST backend synchronous transport for AdSpotService.

    Provides methods for handling ``AdSpot`` objects.

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
        interceptor: Optional[AdSpotServiceRestInterceptor] = None,
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
            interceptor (Optional[AdSpotServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or AdSpotServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _BatchCreateAdSpots(
        _BaseAdSpotServiceRestTransport._BaseBatchCreateAdSpots, AdSpotServiceRestStub
    ):
        def __hash__(self):
            return hash("AdSpotServiceRestTransport.BatchCreateAdSpots")

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
            request: ad_spot_service.BatchCreateAdSpotsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ad_spot_service.BatchCreateAdSpotsResponse:
            r"""Call the batch create ad spots method over HTTP.

            Args:
                request (~.ad_spot_service.BatchCreateAdSpotsRequest):
                    The request object. Request object for ``BatchCreateAdSpots`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ad_spot_service.BatchCreateAdSpotsResponse:
                    Response object for ``BatchCreateAdSpots`` method.
            """

            http_options = _BaseAdSpotServiceRestTransport._BaseBatchCreateAdSpots._get_http_options()
            request, metadata = self._interceptor.pre_batch_create_ad_spots(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAdSpotServiceRestTransport._BaseBatchCreateAdSpots,
                    "_BaseBatchCreateAdSpots__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.AdSpotServiceClient.BatchCreateAdSpots",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdSpotService",
                        "rpcName": "BatchCreateAdSpots",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AdSpotServiceRestTransport._BatchCreateAdSpots._get_response(
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
            resp = ad_spot_service.BatchCreateAdSpotsResponse()
            pb_resp = ad_spot_service.BatchCreateAdSpotsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_create_ad_spots(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_create_ad_spots_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        ad_spot_service.BatchCreateAdSpotsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.AdSpotServiceClient.batch_create_ad_spots",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdSpotService",
                        "rpcName": "BatchCreateAdSpots",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchUpdateAdSpots(
        _BaseAdSpotServiceRestTransport._BaseBatchUpdateAdSpots, AdSpotServiceRestStub
    ):
        def __hash__(self):
            return hash("AdSpotServiceRestTransport.BatchUpdateAdSpots")

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
            request: ad_spot_service.BatchUpdateAdSpotsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ad_spot_service.BatchUpdateAdSpotsResponse:
            r"""Call the batch update ad spots method over HTTP.

            Args:
                request (~.ad_spot_service.BatchUpdateAdSpotsRequest):
                    The request object. Request object for ``BatchUpdateAdSpots`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ad_spot_service.BatchUpdateAdSpotsResponse:
                    Response object for ``BatchUpdateAdSpots`` method.
            """

            http_options = _BaseAdSpotServiceRestTransport._BaseBatchUpdateAdSpots._get_http_options()
            request, metadata = self._interceptor.pre_batch_update_ad_spots(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAdSpotServiceRestTransport._BaseBatchUpdateAdSpots,
                    "_BaseBatchUpdateAdSpots__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.AdSpotServiceClient.BatchUpdateAdSpots",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdSpotService",
                        "rpcName": "BatchUpdateAdSpots",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AdSpotServiceRestTransport._BatchUpdateAdSpots._get_response(
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
            resp = ad_spot_service.BatchUpdateAdSpotsResponse()
            pb_resp = ad_spot_service.BatchUpdateAdSpotsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_update_ad_spots(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_update_ad_spots_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        ad_spot_service.BatchUpdateAdSpotsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.AdSpotServiceClient.batch_update_ad_spots",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdSpotService",
                        "rpcName": "BatchUpdateAdSpots",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateAdSpot(
        _BaseAdSpotServiceRestTransport._BaseCreateAdSpot, AdSpotServiceRestStub
    ):
        def __hash__(self):
            return hash("AdSpotServiceRestTransport.CreateAdSpot")

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
            request: ad_spot_service.CreateAdSpotRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ad_spot_messages.AdSpot:
            r"""Call the create ad spot method over HTTP.

            Args:
                request (~.ad_spot_service.CreateAdSpotRequest):
                    The request object. Request object for ``CreateAdSpot`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ad_spot_messages.AdSpot:
                    An AdSpot is a targetable entity used
                in the creation of AdRule objects. A ad
                spot contains a variable number of ads
                and has constraints (ad duration,
                reservation type, etc) on the ads that
                can appear in it.

            """

            http_options = (
                _BaseAdSpotServiceRestTransport._BaseCreateAdSpot._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_ad_spot(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAdSpotServiceRestTransport._BaseCreateAdSpot,
                    "_BaseCreateAdSpot__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.AdSpotServiceClient.CreateAdSpot",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdSpotService",
                        "rpcName": "CreateAdSpot",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AdSpotServiceRestTransport._CreateAdSpot._get_response(
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
            resp = ad_spot_messages.AdSpot()
            pb_resp = ad_spot_messages.AdSpot.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_ad_spot(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_ad_spot_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = ad_spot_messages.AdSpot.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.AdSpotServiceClient.create_ad_spot",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdSpotService",
                        "rpcName": "CreateAdSpot",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAdSpot(
        _BaseAdSpotServiceRestTransport._BaseGetAdSpot, AdSpotServiceRestStub
    ):
        def __hash__(self):
            return hash("AdSpotServiceRestTransport.GetAdSpot")

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
            request: ad_spot_service.GetAdSpotRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ad_spot_messages.AdSpot:
            r"""Call the get ad spot method over HTTP.

            Args:
                request (~.ad_spot_service.GetAdSpotRequest):
                    The request object. Request object for ``GetAdSpot`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ad_spot_messages.AdSpot:
                    An AdSpot is a targetable entity used
                in the creation of AdRule objects. A ad
                spot contains a variable number of ads
                and has constraints (ad duration,
                reservation type, etc) on the ads that
                can appear in it.

            """

            http_options = (
                _BaseAdSpotServiceRestTransport._BaseGetAdSpot._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_ad_spot(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAdSpotServiceRestTransport._BaseGetAdSpot,
                    "_BaseGetAdSpot__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.AdSpotServiceClient.GetAdSpot",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdSpotService",
                        "rpcName": "GetAdSpot",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AdSpotServiceRestTransport._GetAdSpot._get_response(
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
            resp = ad_spot_messages.AdSpot()
            pb_resp = ad_spot_messages.AdSpot.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_ad_spot(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_ad_spot_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = ad_spot_messages.AdSpot.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.AdSpotServiceClient.get_ad_spot",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdSpotService",
                        "rpcName": "GetAdSpot",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAdSpots(
        _BaseAdSpotServiceRestTransport._BaseListAdSpots, AdSpotServiceRestStub
    ):
        def __hash__(self):
            return hash("AdSpotServiceRestTransport.ListAdSpots")

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
            request: ad_spot_service.ListAdSpotsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ad_spot_service.ListAdSpotsResponse:
            r"""Call the list ad spots method over HTTP.

            Args:
                request (~.ad_spot_service.ListAdSpotsRequest):
                    The request object. Request object for ``ListAdSpots`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ad_spot_service.ListAdSpotsResponse:
                    Response object for ``ListAdSpotsRequest`` containing
                matching ``AdSpot`` objects.

            """

            http_options = (
                _BaseAdSpotServiceRestTransport._BaseListAdSpots._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_ad_spots(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAdSpotServiceRestTransport._BaseListAdSpots,
                    "_BaseListAdSpots__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.AdSpotServiceClient.ListAdSpots",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdSpotService",
                        "rpcName": "ListAdSpots",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AdSpotServiceRestTransport._ListAdSpots._get_response(
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
            resp = ad_spot_service.ListAdSpotsResponse()
            pb_resp = ad_spot_service.ListAdSpotsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_ad_spots(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_ad_spots_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = ad_spot_service.ListAdSpotsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.AdSpotServiceClient.list_ad_spots",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdSpotService",
                        "rpcName": "ListAdSpots",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateAdSpot(
        _BaseAdSpotServiceRestTransport._BaseUpdateAdSpot, AdSpotServiceRestStub
    ):
        def __hash__(self):
            return hash("AdSpotServiceRestTransport.UpdateAdSpot")

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
            request: ad_spot_service.UpdateAdSpotRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ad_spot_messages.AdSpot:
            r"""Call the update ad spot method over HTTP.

            Args:
                request (~.ad_spot_service.UpdateAdSpotRequest):
                    The request object. Request object for ``UpdateAdSpot`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ad_spot_messages.AdSpot:
                    An AdSpot is a targetable entity used
                in the creation of AdRule objects. A ad
                spot contains a variable number of ads
                and has constraints (ad duration,
                reservation type, etc) on the ads that
                can appear in it.

            """

            http_options = (
                _BaseAdSpotServiceRestTransport._BaseUpdateAdSpot._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_ad_spot(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAdSpotServiceRestTransport._BaseUpdateAdSpot,
                    "_BaseUpdateAdSpot__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.AdSpotServiceClient.UpdateAdSpot",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdSpotService",
                        "rpcName": "UpdateAdSpot",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AdSpotServiceRestTransport._UpdateAdSpot._get_response(
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
            resp = ad_spot_messages.AdSpot()
            pb_resp = ad_spot_messages.AdSpot.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_ad_spot(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_ad_spot_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = ad_spot_messages.AdSpot.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.AdSpotServiceClient.update_ad_spot",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdSpotService",
                        "rpcName": "UpdateAdSpot",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_create_ad_spots(
        self,
    ) -> Callable[
        [ad_spot_service.BatchCreateAdSpotsRequest],
        ad_spot_service.BatchCreateAdSpotsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchCreateAdSpots(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_update_ad_spots(
        self,
    ) -> Callable[
        [ad_spot_service.BatchUpdateAdSpotsRequest],
        ad_spot_service.BatchUpdateAdSpotsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchUpdateAdSpots(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_ad_spot(
        self,
    ) -> Callable[[ad_spot_service.CreateAdSpotRequest], ad_spot_messages.AdSpot]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateAdSpot(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_ad_spot(
        self,
    ) -> Callable[[ad_spot_service.GetAdSpotRequest], ad_spot_messages.AdSpot]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAdSpot(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_ad_spots(
        self,
    ) -> Callable[
        [ad_spot_service.ListAdSpotsRequest], ad_spot_service.ListAdSpotsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAdSpots(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_ad_spot(
        self,
    ) -> Callable[[ad_spot_service.UpdateAdSpotRequest], ad_spot_messages.AdSpot]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateAdSpot(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseAdSpotServiceRestTransport._BaseCancelOperation, AdSpotServiceRestStub
    ):
        def __hash__(self):
            return hash("AdSpotServiceRestTransport.CancelOperation")

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

            http_options = (
                _BaseAdSpotServiceRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAdSpotServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.ads.admanager_v1.AdSpotServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdSpotService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AdSpotServiceRestTransport._CancelOperation._get_response(
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
        _BaseAdSpotServiceRestTransport._BaseGetOperation, AdSpotServiceRestStub
    ):
        def __hash__(self):
            return hash("AdSpotServiceRestTransport.GetOperation")

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
                _BaseAdSpotServiceRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAdSpotServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.ads.admanager_v1.AdSpotServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdSpotService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AdSpotServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.ads.admanager_v1.AdSpotServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdSpotService",
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


__all__ = ("AdSpotServiceRestTransport",)
