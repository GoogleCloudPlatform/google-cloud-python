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
from google.api_core import gapic_v1, operations_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.capacityplanner_v1beta._compat import transcode_request
from google.cloud.capacityplanner_v1beta.types import usage_service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseUsageServiceRestTransport

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


class UsageServiceRestInterceptor:
    """Interceptor for UsageService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the UsageServiceRestTransport.

    .. code-block:: python
        class MyCustomUsageServiceInterceptor(UsageServiceRestInterceptor):
            def pre_export_forecasts(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_export_forecasts(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_export_reservations_usage(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_export_reservations_usage(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_export_usage_histories(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_export_usage_histories(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_query_forecasts(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_query_forecasts(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_query_reservations(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_query_reservations(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_query_usage_histories(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_query_usage_histories(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = UsageServiceRestTransport(interceptor=MyCustomUsageServiceInterceptor())
        client = UsageServiceClient(transport=transport)


    """

    def pre_export_forecasts(
        self,
        request: usage_service.ExportForecastsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        usage_service.ExportForecastsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for export_forecasts

        Override in a subclass to manipulate the request or metadata
        before they are sent to the UsageService server.
        """
        return request, metadata

    def post_export_forecasts(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for export_forecasts

        DEPRECATED. Please use the `post_export_forecasts_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the UsageService server but before
        it is returned to user code. This `post_export_forecasts` interceptor runs
        before the `post_export_forecasts_with_metadata` interceptor.
        """
        return response

    def post_export_forecasts_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for export_forecasts

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the UsageService server but before it is returned to user code.

        We recommend only using this `post_export_forecasts_with_metadata`
        interceptor in new development instead of the `post_export_forecasts` interceptor.
        When both interceptors are used, this `post_export_forecasts_with_metadata` interceptor runs after the
        `post_export_forecasts` interceptor. The (possibly modified) response returned by
        `post_export_forecasts` will be passed to
        `post_export_forecasts_with_metadata`.
        """
        return response, metadata

    def pre_export_reservations_usage(
        self,
        request: usage_service.ExportReservationsUsageRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        usage_service.ExportReservationsUsageRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for export_reservations_usage

        Override in a subclass to manipulate the request or metadata
        before they are sent to the UsageService server.
        """
        return request, metadata

    def post_export_reservations_usage(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for export_reservations_usage

        DEPRECATED. Please use the `post_export_reservations_usage_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the UsageService server but before
        it is returned to user code. This `post_export_reservations_usage` interceptor runs
        before the `post_export_reservations_usage_with_metadata` interceptor.
        """
        return response

    def post_export_reservations_usage_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for export_reservations_usage

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the UsageService server but before it is returned to user code.

        We recommend only using this `post_export_reservations_usage_with_metadata`
        interceptor in new development instead of the `post_export_reservations_usage` interceptor.
        When both interceptors are used, this `post_export_reservations_usage_with_metadata` interceptor runs after the
        `post_export_reservations_usage` interceptor. The (possibly modified) response returned by
        `post_export_reservations_usage` will be passed to
        `post_export_reservations_usage_with_metadata`.
        """
        return response, metadata

    def pre_export_usage_histories(
        self,
        request: usage_service.ExportUsageHistoriesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        usage_service.ExportUsageHistoriesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for export_usage_histories

        Override in a subclass to manipulate the request or metadata
        before they are sent to the UsageService server.
        """
        return request, metadata

    def post_export_usage_histories(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for export_usage_histories

        DEPRECATED. Please use the `post_export_usage_histories_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the UsageService server but before
        it is returned to user code. This `post_export_usage_histories` interceptor runs
        before the `post_export_usage_histories_with_metadata` interceptor.
        """
        return response

    def post_export_usage_histories_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for export_usage_histories

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the UsageService server but before it is returned to user code.

        We recommend only using this `post_export_usage_histories_with_metadata`
        interceptor in new development instead of the `post_export_usage_histories` interceptor.
        When both interceptors are used, this `post_export_usage_histories_with_metadata` interceptor runs after the
        `post_export_usage_histories` interceptor. The (possibly modified) response returned by
        `post_export_usage_histories` will be passed to
        `post_export_usage_histories_with_metadata`.
        """
        return response, metadata

    def pre_query_forecasts(
        self,
        request: usage_service.QueryForecastsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        usage_service.QueryForecastsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for query_forecasts

        Override in a subclass to manipulate the request or metadata
        before they are sent to the UsageService server.
        """
        return request, metadata

    def post_query_forecasts(
        self, response: usage_service.QueryForecastsResponse
    ) -> usage_service.QueryForecastsResponse:
        """Post-rpc interceptor for query_forecasts

        DEPRECATED. Please use the `post_query_forecasts_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the UsageService server but before
        it is returned to user code. This `post_query_forecasts` interceptor runs
        before the `post_query_forecasts_with_metadata` interceptor.
        """
        return response

    def post_query_forecasts_with_metadata(
        self,
        response: usage_service.QueryForecastsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        usage_service.QueryForecastsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for query_forecasts

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the UsageService server but before it is returned to user code.

        We recommend only using this `post_query_forecasts_with_metadata`
        interceptor in new development instead of the `post_query_forecasts` interceptor.
        When both interceptors are used, this `post_query_forecasts_with_metadata` interceptor runs after the
        `post_query_forecasts` interceptor. The (possibly modified) response returned by
        `post_query_forecasts` will be passed to
        `post_query_forecasts_with_metadata`.
        """
        return response, metadata

    def pre_query_reservations(
        self,
        request: usage_service.QueryReservationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        usage_service.QueryReservationsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for query_reservations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the UsageService server.
        """
        return request, metadata

    def post_query_reservations(
        self, response: usage_service.QueryReservationsResponse
    ) -> usage_service.QueryReservationsResponse:
        """Post-rpc interceptor for query_reservations

        DEPRECATED. Please use the `post_query_reservations_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the UsageService server but before
        it is returned to user code. This `post_query_reservations` interceptor runs
        before the `post_query_reservations_with_metadata` interceptor.
        """
        return response

    def post_query_reservations_with_metadata(
        self,
        response: usage_service.QueryReservationsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        usage_service.QueryReservationsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for query_reservations

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the UsageService server but before it is returned to user code.

        We recommend only using this `post_query_reservations_with_metadata`
        interceptor in new development instead of the `post_query_reservations` interceptor.
        When both interceptors are used, this `post_query_reservations_with_metadata` interceptor runs after the
        `post_query_reservations` interceptor. The (possibly modified) response returned by
        `post_query_reservations` will be passed to
        `post_query_reservations_with_metadata`.
        """
        return response, metadata

    def pre_query_usage_histories(
        self,
        request: usage_service.QueryUsageHistoriesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        usage_service.QueryUsageHistoriesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for query_usage_histories

        Override in a subclass to manipulate the request or metadata
        before they are sent to the UsageService server.
        """
        return request, metadata

    def post_query_usage_histories(
        self, response: usage_service.QueryUsageHistoriesResponse
    ) -> usage_service.QueryUsageHistoriesResponse:
        """Post-rpc interceptor for query_usage_histories

        DEPRECATED. Please use the `post_query_usage_histories_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the UsageService server but before
        it is returned to user code. This `post_query_usage_histories` interceptor runs
        before the `post_query_usage_histories_with_metadata` interceptor.
        """
        return response

    def post_query_usage_histories_with_metadata(
        self,
        response: usage_service.QueryUsageHistoriesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        usage_service.QueryUsageHistoriesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for query_usage_histories

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the UsageService server but before it is returned to user code.

        We recommend only using this `post_query_usage_histories_with_metadata`
        interceptor in new development instead of the `post_query_usage_histories` interceptor.
        When both interceptors are used, this `post_query_usage_histories_with_metadata` interceptor runs after the
        `post_query_usage_histories` interceptor. The (possibly modified) response returned by
        `post_query_usage_histories` will be passed to
        `post_query_usage_histories_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class UsageServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: UsageServiceRestInterceptor


class UsageServiceRestTransport(_BaseUsageServiceRestTransport):
    """REST backend synchronous transport for UsageService.

    Provides access to historical and forecasted usage data.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "capacityplanner.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[UsageServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'capacityplanner.googleapis.com').
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
            interceptor (Optional[UsageServiceRestInterceptor]): Interceptor used
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
        self._operations_client: Optional[operations_v1.AbstractOperationsClient] = None
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or UsageServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    @property
    def operations_client(self) -> operations_v1.AbstractOperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Only create a new client if we do not already have one.
        if self._operations_client is None:
            http_options: Dict[str, List[Dict[str, str]]] = {}

            rest_transport = operations_v1.OperationsRestTransport(
                host=self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                scopes=self._scopes,
                http_options=http_options,
                path_prefix="v1beta",
            )

            self._operations_client = operations_v1.AbstractOperationsClient(
                transport=rest_transport
            )

        # Return the client from cache.
        return self._operations_client

    class _ExportForecasts(
        _BaseUsageServiceRestTransport._BaseExportForecasts, UsageServiceRestStub
    ):
        def __hash__(self):
            return hash("UsageServiceRestTransport.ExportForecasts")

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
            request: usage_service.ExportForecastsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the export forecasts method over HTTP.

            Args:
                request (~.usage_service.ExportForecastsRequest):
                    The request object. The ``ExportForecasts`` request Next : 13
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = (
                _BaseUsageServiceRestTransport._BaseExportForecasts._get_http_options()
            )
            request, metadata = self._interceptor.pre_export_forecasts(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseUsageServiceRestTransport._BaseExportForecasts,
                    "_BaseExportForecasts__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.capacityplanner_v1beta.UsageServiceClient.ExportForecasts",
                    extra={
                        "serviceName": "google.cloud.capacityplanner.v1beta.UsageService",
                        "rpcName": "ExportForecasts",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = UsageServiceRestTransport._ExportForecasts._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_export_forecasts(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_export_forecasts_with_metadata(
                resp, response_metadata
            )
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
                    "Received response for google.cloud.capacityplanner_v1beta.UsageServiceClient.export_forecasts",
                    extra={
                        "serviceName": "google.cloud.capacityplanner.v1beta.UsageService",
                        "rpcName": "ExportForecasts",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ExportReservationsUsage(
        _BaseUsageServiceRestTransport._BaseExportReservationsUsage,
        UsageServiceRestStub,
    ):
        def __hash__(self):
            return hash("UsageServiceRestTransport.ExportReservationsUsage")

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
            request: usage_service.ExportReservationsUsageRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the export reservations usage method over HTTP.

            Args:
                request (~.usage_service.ExportReservationsUsageRequest):
                    The request object. The ``ExportReservationsUsage`` request
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = _BaseUsageServiceRestTransport._BaseExportReservationsUsage._get_http_options()
            request, metadata = self._interceptor.pre_export_reservations_usage(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseUsageServiceRestTransport._BaseExportReservationsUsage,
                    "_BaseExportReservationsUsage__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.capacityplanner_v1beta.UsageServiceClient.ExportReservationsUsage",
                    extra={
                        "serviceName": "google.cloud.capacityplanner.v1beta.UsageService",
                        "rpcName": "ExportReservationsUsage",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = UsageServiceRestTransport._ExportReservationsUsage._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_export_reservations_usage(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_export_reservations_usage_with_metadata(
                resp, response_metadata
            )
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
                    "Received response for google.cloud.capacityplanner_v1beta.UsageServiceClient.export_reservations_usage",
                    extra={
                        "serviceName": "google.cloud.capacityplanner.v1beta.UsageService",
                        "rpcName": "ExportReservationsUsage",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ExportUsageHistories(
        _BaseUsageServiceRestTransport._BaseExportUsageHistories, UsageServiceRestStub
    ):
        def __hash__(self):
            return hash("UsageServiceRestTransport.ExportUsageHistories")

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
            request: usage_service.ExportUsageHistoriesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the export usage histories method over HTTP.

            Args:
                request (~.usage_service.ExportUsageHistoriesRequest):
                    The request object. The ``ExportUsageHistories`` request Next : 12
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = _BaseUsageServiceRestTransport._BaseExportUsageHistories._get_http_options()
            request, metadata = self._interceptor.pre_export_usage_histories(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseUsageServiceRestTransport._BaseExportUsageHistories,
                    "_BaseExportUsageHistories__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.capacityplanner_v1beta.UsageServiceClient.ExportUsageHistories",
                    extra={
                        "serviceName": "google.cloud.capacityplanner.v1beta.UsageService",
                        "rpcName": "ExportUsageHistories",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = UsageServiceRestTransport._ExportUsageHistories._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_export_usage_histories(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_export_usage_histories_with_metadata(
                resp, response_metadata
            )
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
                    "Received response for google.cloud.capacityplanner_v1beta.UsageServiceClient.export_usage_histories",
                    extra={
                        "serviceName": "google.cloud.capacityplanner.v1beta.UsageService",
                        "rpcName": "ExportUsageHistories",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _QueryForecasts(
        _BaseUsageServiceRestTransport._BaseQueryForecasts, UsageServiceRestStub
    ):
        def __hash__(self):
            return hash("UsageServiceRestTransport.QueryForecasts")

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
            request: usage_service.QueryForecastsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> usage_service.QueryForecastsResponse:
            r"""Call the query forecasts method over HTTP.

            Args:
                request (~.usage_service.QueryForecastsRequest):
                    The request object. The ``QueryForecasts`` request. Next : 14
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.usage_service.QueryForecastsResponse:
                    The ``QueryForecasts`` response.
            """

            http_options = (
                _BaseUsageServiceRestTransport._BaseQueryForecasts._get_http_options()
            )
            request, metadata = self._interceptor.pre_query_forecasts(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseUsageServiceRestTransport._BaseQueryForecasts,
                    "_BaseQueryForecasts__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.capacityplanner_v1beta.UsageServiceClient.QueryForecasts",
                    extra={
                        "serviceName": "google.cloud.capacityplanner.v1beta.UsageService",
                        "rpcName": "QueryForecasts",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = UsageServiceRestTransport._QueryForecasts._get_response(
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
            resp = usage_service.QueryForecastsResponse()
            pb_resp = usage_service.QueryForecastsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_query_forecasts(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_query_forecasts_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = usage_service.QueryForecastsResponse.to_json(
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
                    "Received response for google.cloud.capacityplanner_v1beta.UsageServiceClient.query_forecasts",
                    extra={
                        "serviceName": "google.cloud.capacityplanner.v1beta.UsageService",
                        "rpcName": "QueryForecasts",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _QueryReservations(
        _BaseUsageServiceRestTransport._BaseQueryReservations, UsageServiceRestStub
    ):
        def __hash__(self):
            return hash("UsageServiceRestTransport.QueryReservations")

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
            request: usage_service.QueryReservationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> usage_service.QueryReservationsResponse:
            r"""Call the query reservations method over HTTP.

            Args:
                request (~.usage_service.QueryReservationsRequest):
                    The request object. The ``QueryReservations`` request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.usage_service.QueryReservationsResponse:
                    The ``QueryReservations`` response.
            """

            http_options = _BaseUsageServiceRestTransport._BaseQueryReservations._get_http_options()
            request, metadata = self._interceptor.pre_query_reservations(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseUsageServiceRestTransport._BaseQueryReservations,
                    "_BaseQueryReservations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.capacityplanner_v1beta.UsageServiceClient.QueryReservations",
                    extra={
                        "serviceName": "google.cloud.capacityplanner.v1beta.UsageService",
                        "rpcName": "QueryReservations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = UsageServiceRestTransport._QueryReservations._get_response(
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
            resp = usage_service.QueryReservationsResponse()
            pb_resp = usage_service.QueryReservationsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_query_reservations(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_query_reservations_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = usage_service.QueryReservationsResponse.to_json(
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
                    "Received response for google.cloud.capacityplanner_v1beta.UsageServiceClient.query_reservations",
                    extra={
                        "serviceName": "google.cloud.capacityplanner.v1beta.UsageService",
                        "rpcName": "QueryReservations",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _QueryUsageHistories(
        _BaseUsageServiceRestTransport._BaseQueryUsageHistories, UsageServiceRestStub
    ):
        def __hash__(self):
            return hash("UsageServiceRestTransport.QueryUsageHistories")

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
            request: usage_service.QueryUsageHistoriesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> usage_service.QueryUsageHistoriesResponse:
            r"""Call the query usage histories method over HTTP.

            Args:
                request (~.usage_service.QueryUsageHistoriesRequest):
                    The request object. The ``QueryUsageHistories`` request. Next : 16
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.usage_service.QueryUsageHistoriesResponse:
                    The ``QueryUsageHistories`` response.
            """

            http_options = _BaseUsageServiceRestTransport._BaseQueryUsageHistories._get_http_options()
            request, metadata = self._interceptor.pre_query_usage_histories(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseUsageServiceRestTransport._BaseQueryUsageHistories,
                    "_BaseQueryUsageHistories__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.capacityplanner_v1beta.UsageServiceClient.QueryUsageHistories",
                    extra={
                        "serviceName": "google.cloud.capacityplanner.v1beta.UsageService",
                        "rpcName": "QueryUsageHistories",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = UsageServiceRestTransport._QueryUsageHistories._get_response(
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
            resp = usage_service.QueryUsageHistoriesResponse()
            pb_resp = usage_service.QueryUsageHistoriesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_query_usage_histories(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_query_usage_histories_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        usage_service.QueryUsageHistoriesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.capacityplanner_v1beta.UsageServiceClient.query_usage_histories",
                    extra={
                        "serviceName": "google.cloud.capacityplanner.v1beta.UsageService",
                        "rpcName": "QueryUsageHistories",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def export_forecasts(
        self,
    ) -> Callable[[usage_service.ExportForecastsRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExportForecasts(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def export_reservations_usage(
        self,
    ) -> Callable[
        [usage_service.ExportReservationsUsageRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExportReservationsUsage(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def export_usage_histories(
        self,
    ) -> Callable[
        [usage_service.ExportUsageHistoriesRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExportUsageHistories(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def query_forecasts(
        self,
    ) -> Callable[
        [usage_service.QueryForecastsRequest], usage_service.QueryForecastsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._QueryForecasts(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def query_reservations(
        self,
    ) -> Callable[
        [usage_service.QueryReservationsRequest],
        usage_service.QueryReservationsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._QueryReservations(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def query_usage_histories(
        self,
    ) -> Callable[
        [usage_service.QueryUsageHistoriesRequest],
        usage_service.QueryUsageHistoriesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._QueryUsageHistories(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("UsageServiceRestTransport",)
