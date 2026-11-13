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
    traffic_forecast_segment_messages,
    traffic_forecast_segment_service,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseTrafficForecastSegmentServiceRestTransport

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


class TrafficForecastSegmentServiceRestInterceptor:
    """Interceptor for TrafficForecastSegmentService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the TrafficForecastSegmentServiceRestTransport.

    .. code-block:: python
        class MyCustomTrafficForecastSegmentServiceInterceptor(TrafficForecastSegmentServiceRestInterceptor):
            def pre_batch_create_traffic_forecast_segments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_create_traffic_forecast_segments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_update_traffic_forecast_segments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_update_traffic_forecast_segments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_traffic_forecast_segment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_traffic_forecast_segment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_traffic_forecast_segment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_traffic_forecast_segment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_traffic_forecast_segments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_traffic_forecast_segments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_traffic_forecast_segment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_traffic_forecast_segment(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = TrafficForecastSegmentServiceRestTransport(interceptor=MyCustomTrafficForecastSegmentServiceInterceptor())
        client = TrafficForecastSegmentServiceClient(transport=transport)


    """

    def pre_batch_create_traffic_forecast_segments(
        self,
        request: traffic_forecast_segment_service.BatchCreateTrafficForecastSegmentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        traffic_forecast_segment_service.BatchCreateTrafficForecastSegmentsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_create_traffic_forecast_segments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TrafficForecastSegmentService server.
        """
        return request, metadata

    def post_batch_create_traffic_forecast_segments(
        self,
        response: traffic_forecast_segment_service.BatchCreateTrafficForecastSegmentsResponse,
    ) -> traffic_forecast_segment_service.BatchCreateTrafficForecastSegmentsResponse:
        """Post-rpc interceptor for batch_create_traffic_forecast_segments

        DEPRECATED. Please use the `post_batch_create_traffic_forecast_segments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TrafficForecastSegmentService server but before
        it is returned to user code. This `post_batch_create_traffic_forecast_segments` interceptor runs
        before the `post_batch_create_traffic_forecast_segments_with_metadata` interceptor.
        """
        return response

    def post_batch_create_traffic_forecast_segments_with_metadata(
        self,
        response: traffic_forecast_segment_service.BatchCreateTrafficForecastSegmentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        traffic_forecast_segment_service.BatchCreateTrafficForecastSegmentsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_create_traffic_forecast_segments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TrafficForecastSegmentService server but before it is returned to user code.

        We recommend only using this `post_batch_create_traffic_forecast_segments_with_metadata`
        interceptor in new development instead of the `post_batch_create_traffic_forecast_segments` interceptor.
        When both interceptors are used, this `post_batch_create_traffic_forecast_segments_with_metadata` interceptor runs after the
        `post_batch_create_traffic_forecast_segments` interceptor. The (possibly modified) response returned by
        `post_batch_create_traffic_forecast_segments` will be passed to
        `post_batch_create_traffic_forecast_segments_with_metadata`.
        """
        return response, metadata

    def pre_batch_update_traffic_forecast_segments(
        self,
        request: traffic_forecast_segment_service.BatchUpdateTrafficForecastSegmentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        traffic_forecast_segment_service.BatchUpdateTrafficForecastSegmentsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_update_traffic_forecast_segments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TrafficForecastSegmentService server.
        """
        return request, metadata

    def post_batch_update_traffic_forecast_segments(
        self,
        response: traffic_forecast_segment_service.BatchUpdateTrafficForecastSegmentsResponse,
    ) -> traffic_forecast_segment_service.BatchUpdateTrafficForecastSegmentsResponse:
        """Post-rpc interceptor for batch_update_traffic_forecast_segments

        DEPRECATED. Please use the `post_batch_update_traffic_forecast_segments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TrafficForecastSegmentService server but before
        it is returned to user code. This `post_batch_update_traffic_forecast_segments` interceptor runs
        before the `post_batch_update_traffic_forecast_segments_with_metadata` interceptor.
        """
        return response

    def post_batch_update_traffic_forecast_segments_with_metadata(
        self,
        response: traffic_forecast_segment_service.BatchUpdateTrafficForecastSegmentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        traffic_forecast_segment_service.BatchUpdateTrafficForecastSegmentsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_update_traffic_forecast_segments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TrafficForecastSegmentService server but before it is returned to user code.

        We recommend only using this `post_batch_update_traffic_forecast_segments_with_metadata`
        interceptor in new development instead of the `post_batch_update_traffic_forecast_segments` interceptor.
        When both interceptors are used, this `post_batch_update_traffic_forecast_segments_with_metadata` interceptor runs after the
        `post_batch_update_traffic_forecast_segments` interceptor. The (possibly modified) response returned by
        `post_batch_update_traffic_forecast_segments` will be passed to
        `post_batch_update_traffic_forecast_segments_with_metadata`.
        """
        return response, metadata

    def pre_create_traffic_forecast_segment(
        self,
        request: traffic_forecast_segment_service.CreateTrafficForecastSegmentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        traffic_forecast_segment_service.CreateTrafficForecastSegmentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_traffic_forecast_segment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TrafficForecastSegmentService server.
        """
        return request, metadata

    def post_create_traffic_forecast_segment(
        self, response: traffic_forecast_segment_messages.TrafficForecastSegment
    ) -> traffic_forecast_segment_messages.TrafficForecastSegment:
        """Post-rpc interceptor for create_traffic_forecast_segment

        DEPRECATED. Please use the `post_create_traffic_forecast_segment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TrafficForecastSegmentService server but before
        it is returned to user code. This `post_create_traffic_forecast_segment` interceptor runs
        before the `post_create_traffic_forecast_segment_with_metadata` interceptor.
        """
        return response

    def post_create_traffic_forecast_segment_with_metadata(
        self,
        response: traffic_forecast_segment_messages.TrafficForecastSegment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        traffic_forecast_segment_messages.TrafficForecastSegment,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for create_traffic_forecast_segment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TrafficForecastSegmentService server but before it is returned to user code.

        We recommend only using this `post_create_traffic_forecast_segment_with_metadata`
        interceptor in new development instead of the `post_create_traffic_forecast_segment` interceptor.
        When both interceptors are used, this `post_create_traffic_forecast_segment_with_metadata` interceptor runs after the
        `post_create_traffic_forecast_segment` interceptor. The (possibly modified) response returned by
        `post_create_traffic_forecast_segment` will be passed to
        `post_create_traffic_forecast_segment_with_metadata`.
        """
        return response, metadata

    def pre_get_traffic_forecast_segment(
        self,
        request: traffic_forecast_segment_service.GetTrafficForecastSegmentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        traffic_forecast_segment_service.GetTrafficForecastSegmentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_traffic_forecast_segment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TrafficForecastSegmentService server.
        """
        return request, metadata

    def post_get_traffic_forecast_segment(
        self, response: traffic_forecast_segment_messages.TrafficForecastSegment
    ) -> traffic_forecast_segment_messages.TrafficForecastSegment:
        """Post-rpc interceptor for get_traffic_forecast_segment

        DEPRECATED. Please use the `post_get_traffic_forecast_segment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TrafficForecastSegmentService server but before
        it is returned to user code. This `post_get_traffic_forecast_segment` interceptor runs
        before the `post_get_traffic_forecast_segment_with_metadata` interceptor.
        """
        return response

    def post_get_traffic_forecast_segment_with_metadata(
        self,
        response: traffic_forecast_segment_messages.TrafficForecastSegment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        traffic_forecast_segment_messages.TrafficForecastSegment,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_traffic_forecast_segment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TrafficForecastSegmentService server but before it is returned to user code.

        We recommend only using this `post_get_traffic_forecast_segment_with_metadata`
        interceptor in new development instead of the `post_get_traffic_forecast_segment` interceptor.
        When both interceptors are used, this `post_get_traffic_forecast_segment_with_metadata` interceptor runs after the
        `post_get_traffic_forecast_segment` interceptor. The (possibly modified) response returned by
        `post_get_traffic_forecast_segment` will be passed to
        `post_get_traffic_forecast_segment_with_metadata`.
        """
        return response, metadata

    def pre_list_traffic_forecast_segments(
        self,
        request: traffic_forecast_segment_service.ListTrafficForecastSegmentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        traffic_forecast_segment_service.ListTrafficForecastSegmentsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_traffic_forecast_segments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TrafficForecastSegmentService server.
        """
        return request, metadata

    def post_list_traffic_forecast_segments(
        self,
        response: traffic_forecast_segment_service.ListTrafficForecastSegmentsResponse,
    ) -> traffic_forecast_segment_service.ListTrafficForecastSegmentsResponse:
        """Post-rpc interceptor for list_traffic_forecast_segments

        DEPRECATED. Please use the `post_list_traffic_forecast_segments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TrafficForecastSegmentService server but before
        it is returned to user code. This `post_list_traffic_forecast_segments` interceptor runs
        before the `post_list_traffic_forecast_segments_with_metadata` interceptor.
        """
        return response

    def post_list_traffic_forecast_segments_with_metadata(
        self,
        response: traffic_forecast_segment_service.ListTrafficForecastSegmentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        traffic_forecast_segment_service.ListTrafficForecastSegmentsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_traffic_forecast_segments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TrafficForecastSegmentService server but before it is returned to user code.

        We recommend only using this `post_list_traffic_forecast_segments_with_metadata`
        interceptor in new development instead of the `post_list_traffic_forecast_segments` interceptor.
        When both interceptors are used, this `post_list_traffic_forecast_segments_with_metadata` interceptor runs after the
        `post_list_traffic_forecast_segments` interceptor. The (possibly modified) response returned by
        `post_list_traffic_forecast_segments` will be passed to
        `post_list_traffic_forecast_segments_with_metadata`.
        """
        return response, metadata

    def pre_update_traffic_forecast_segment(
        self,
        request: traffic_forecast_segment_service.UpdateTrafficForecastSegmentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        traffic_forecast_segment_service.UpdateTrafficForecastSegmentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_traffic_forecast_segment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TrafficForecastSegmentService server.
        """
        return request, metadata

    def post_update_traffic_forecast_segment(
        self, response: traffic_forecast_segment_messages.TrafficForecastSegment
    ) -> traffic_forecast_segment_messages.TrafficForecastSegment:
        """Post-rpc interceptor for update_traffic_forecast_segment

        DEPRECATED. Please use the `post_update_traffic_forecast_segment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TrafficForecastSegmentService server but before
        it is returned to user code. This `post_update_traffic_forecast_segment` interceptor runs
        before the `post_update_traffic_forecast_segment_with_metadata` interceptor.
        """
        return response

    def post_update_traffic_forecast_segment_with_metadata(
        self,
        response: traffic_forecast_segment_messages.TrafficForecastSegment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        traffic_forecast_segment_messages.TrafficForecastSegment,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for update_traffic_forecast_segment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TrafficForecastSegmentService server but before it is returned to user code.

        We recommend only using this `post_update_traffic_forecast_segment_with_metadata`
        interceptor in new development instead of the `post_update_traffic_forecast_segment` interceptor.
        When both interceptors are used, this `post_update_traffic_forecast_segment_with_metadata` interceptor runs after the
        `post_update_traffic_forecast_segment` interceptor. The (possibly modified) response returned by
        `post_update_traffic_forecast_segment` will be passed to
        `post_update_traffic_forecast_segment_with_metadata`.
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
        before they are sent to the TrafficForecastSegmentService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the TrafficForecastSegmentService server but before
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
        before they are sent to the TrafficForecastSegmentService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the TrafficForecastSegmentService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class TrafficForecastSegmentServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: TrafficForecastSegmentServiceRestInterceptor


class TrafficForecastSegmentServiceRestTransport(
    _BaseTrafficForecastSegmentServiceRestTransport
):
    """REST backend synchronous transport for TrafficForecastSegmentService.

    Provides methods for handling ``TrafficForecastSegment`` objects.

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
        interceptor: Optional[TrafficForecastSegmentServiceRestInterceptor] = None,
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
            interceptor (Optional[TrafficForecastSegmentServiceRestInterceptor]): Interceptor used
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
            interceptor or TrafficForecastSegmentServiceRestInterceptor()
        )
        self._prep_wrapped_messages(client_info)

    class _BatchCreateTrafficForecastSegments(
        _BaseTrafficForecastSegmentServiceRestTransport._BaseBatchCreateTrafficForecastSegments,
        TrafficForecastSegmentServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "TrafficForecastSegmentServiceRestTransport.BatchCreateTrafficForecastSegments"
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
            request: traffic_forecast_segment_service.BatchCreateTrafficForecastSegmentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> (
            traffic_forecast_segment_service.BatchCreateTrafficForecastSegmentsResponse
        ):
            r"""Call the batch create traffic
            forecast segments method over HTTP.

                Args:
                    request (~.traffic_forecast_segment_service.BatchCreateTrafficForecastSegmentsRequest):
                        The request object. Request object for
                    ``BatchCreateTrafficForecastSegments`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.traffic_forecast_segment_service.BatchCreateTrafficForecastSegmentsResponse:
                        Response object for
                    ``BatchCreateTrafficForecastSegments`` method.

            """

            http_options = _BaseTrafficForecastSegmentServiceRestTransport._BaseBatchCreateTrafficForecastSegments._get_http_options()
            request, metadata = (
                self._interceptor.pre_batch_create_traffic_forecast_segments(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTrafficForecastSegmentServiceRestTransport._BaseBatchCreateTrafficForecastSegments,
                    "_BaseBatchCreateTrafficForecastSegments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.TrafficForecastSegmentServiceClient.BatchCreateTrafficForecastSegments",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TrafficForecastSegmentService",
                        "rpcName": "BatchCreateTrafficForecastSegments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TrafficForecastSegmentServiceRestTransport._BatchCreateTrafficForecastSegments._get_response(
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
            resp = traffic_forecast_segment_service.BatchCreateTrafficForecastSegmentsResponse()
            pb_resp = traffic_forecast_segment_service.BatchCreateTrafficForecastSegmentsResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_create_traffic_forecast_segments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_create_traffic_forecast_segments_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = traffic_forecast_segment_service.BatchCreateTrafficForecastSegmentsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.TrafficForecastSegmentServiceClient.batch_create_traffic_forecast_segments",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TrafficForecastSegmentService",
                        "rpcName": "BatchCreateTrafficForecastSegments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchUpdateTrafficForecastSegments(
        _BaseTrafficForecastSegmentServiceRestTransport._BaseBatchUpdateTrafficForecastSegments,
        TrafficForecastSegmentServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "TrafficForecastSegmentServiceRestTransport.BatchUpdateTrafficForecastSegments"
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
            request: traffic_forecast_segment_service.BatchUpdateTrafficForecastSegmentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> (
            traffic_forecast_segment_service.BatchUpdateTrafficForecastSegmentsResponse
        ):
            r"""Call the batch update traffic
            forecast segments method over HTTP.

                Args:
                    request (~.traffic_forecast_segment_service.BatchUpdateTrafficForecastSegmentsRequest):
                        The request object. Request object for
                    ``BatchUpdateTrafficForecastSegments`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.traffic_forecast_segment_service.BatchUpdateTrafficForecastSegmentsResponse:
                        Response object for
                    ``BatchUpdateTrafficForecastSegments`` method.

            """

            http_options = _BaseTrafficForecastSegmentServiceRestTransport._BaseBatchUpdateTrafficForecastSegments._get_http_options()
            request, metadata = (
                self._interceptor.pre_batch_update_traffic_forecast_segments(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTrafficForecastSegmentServiceRestTransport._BaseBatchUpdateTrafficForecastSegments,
                    "_BaseBatchUpdateTrafficForecastSegments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.TrafficForecastSegmentServiceClient.BatchUpdateTrafficForecastSegments",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TrafficForecastSegmentService",
                        "rpcName": "BatchUpdateTrafficForecastSegments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TrafficForecastSegmentServiceRestTransport._BatchUpdateTrafficForecastSegments._get_response(
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
            resp = traffic_forecast_segment_service.BatchUpdateTrafficForecastSegmentsResponse()
            pb_resp = traffic_forecast_segment_service.BatchUpdateTrafficForecastSegmentsResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_update_traffic_forecast_segments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_update_traffic_forecast_segments_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = traffic_forecast_segment_service.BatchUpdateTrafficForecastSegmentsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.TrafficForecastSegmentServiceClient.batch_update_traffic_forecast_segments",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TrafficForecastSegmentService",
                        "rpcName": "BatchUpdateTrafficForecastSegments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateTrafficForecastSegment(
        _BaseTrafficForecastSegmentServiceRestTransport._BaseCreateTrafficForecastSegment,
        TrafficForecastSegmentServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "TrafficForecastSegmentServiceRestTransport.CreateTrafficForecastSegment"
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
            request: traffic_forecast_segment_service.CreateTrafficForecastSegmentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> traffic_forecast_segment_messages.TrafficForecastSegment:
            r"""Call the create traffic forecast
            segment method over HTTP.

                Args:
                    request (~.traffic_forecast_segment_service.CreateTrafficForecastSegmentRequest):
                        The request object. Request object for ``CreateTrafficForecastSegment``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.traffic_forecast_segment_messages.TrafficForecastSegment:
                        An entity that defines a segment of
                    traffic that will be adjusted or
                    explored.

            """

            http_options = _BaseTrafficForecastSegmentServiceRestTransport._BaseCreateTrafficForecastSegment._get_http_options()
            request, metadata = self._interceptor.pre_create_traffic_forecast_segment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTrafficForecastSegmentServiceRestTransport._BaseCreateTrafficForecastSegment,
                    "_BaseCreateTrafficForecastSegment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.TrafficForecastSegmentServiceClient.CreateTrafficForecastSegment",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TrafficForecastSegmentService",
                        "rpcName": "CreateTrafficForecastSegment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TrafficForecastSegmentServiceRestTransport._CreateTrafficForecastSegment._get_response(
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
            resp = traffic_forecast_segment_messages.TrafficForecastSegment()
            pb_resp = traffic_forecast_segment_messages.TrafficForecastSegment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_traffic_forecast_segment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_create_traffic_forecast_segment_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = traffic_forecast_segment_messages.TrafficForecastSegment.to_json(
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
                    "Received response for google.ads.admanager_v1.TrafficForecastSegmentServiceClient.create_traffic_forecast_segment",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TrafficForecastSegmentService",
                        "rpcName": "CreateTrafficForecastSegment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetTrafficForecastSegment(
        _BaseTrafficForecastSegmentServiceRestTransport._BaseGetTrafficForecastSegment,
        TrafficForecastSegmentServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "TrafficForecastSegmentServiceRestTransport.GetTrafficForecastSegment"
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
            request: traffic_forecast_segment_service.GetTrafficForecastSegmentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> traffic_forecast_segment_messages.TrafficForecastSegment:
            r"""Call the get traffic forecast
            segment method over HTTP.

                Args:
                    request (~.traffic_forecast_segment_service.GetTrafficForecastSegmentRequest):
                        The request object. Request object for ``GetTrafficForecastSegment`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.traffic_forecast_segment_messages.TrafficForecastSegment:
                        An entity that defines a segment of
                    traffic that will be adjusted or
                    explored.

            """

            http_options = _BaseTrafficForecastSegmentServiceRestTransport._BaseGetTrafficForecastSegment._get_http_options()
            request, metadata = self._interceptor.pre_get_traffic_forecast_segment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTrafficForecastSegmentServiceRestTransport._BaseGetTrafficForecastSegment,
                    "_BaseGetTrafficForecastSegment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.TrafficForecastSegmentServiceClient.GetTrafficForecastSegment",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TrafficForecastSegmentService",
                        "rpcName": "GetTrafficForecastSegment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TrafficForecastSegmentServiceRestTransport._GetTrafficForecastSegment._get_response(
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
            resp = traffic_forecast_segment_messages.TrafficForecastSegment()
            pb_resp = traffic_forecast_segment_messages.TrafficForecastSegment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_traffic_forecast_segment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_traffic_forecast_segment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = traffic_forecast_segment_messages.TrafficForecastSegment.to_json(
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
                    "Received response for google.ads.admanager_v1.TrafficForecastSegmentServiceClient.get_traffic_forecast_segment",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TrafficForecastSegmentService",
                        "rpcName": "GetTrafficForecastSegment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListTrafficForecastSegments(
        _BaseTrafficForecastSegmentServiceRestTransport._BaseListTrafficForecastSegments,
        TrafficForecastSegmentServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "TrafficForecastSegmentServiceRestTransport.ListTrafficForecastSegments"
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
            request: traffic_forecast_segment_service.ListTrafficForecastSegmentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> traffic_forecast_segment_service.ListTrafficForecastSegmentsResponse:
            r"""Call the list traffic forecast
            segments method over HTTP.

                Args:
                    request (~.traffic_forecast_segment_service.ListTrafficForecastSegmentsRequest):
                        The request object. Request object for ``ListTrafficForecastSegments``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.traffic_forecast_segment_service.ListTrafficForecastSegmentsResponse:
                        Response object for
                    ``ListTrafficForecastSegmentsRequest`` containing
                    matching ``TrafficForecastSegment`` objects.

            """

            http_options = _BaseTrafficForecastSegmentServiceRestTransport._BaseListTrafficForecastSegments._get_http_options()
            request, metadata = self._interceptor.pre_list_traffic_forecast_segments(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTrafficForecastSegmentServiceRestTransport._BaseListTrafficForecastSegments,
                    "_BaseListTrafficForecastSegments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.TrafficForecastSegmentServiceClient.ListTrafficForecastSegments",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TrafficForecastSegmentService",
                        "rpcName": "ListTrafficForecastSegments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TrafficForecastSegmentServiceRestTransport._ListTrafficForecastSegments._get_response(
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
            resp = (
                traffic_forecast_segment_service.ListTrafficForecastSegmentsResponse()
            )
            pb_resp = (
                traffic_forecast_segment_service.ListTrafficForecastSegmentsResponse.pb(
                    resp
                )
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_traffic_forecast_segments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_traffic_forecast_segments_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = traffic_forecast_segment_service.ListTrafficForecastSegmentsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.TrafficForecastSegmentServiceClient.list_traffic_forecast_segments",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TrafficForecastSegmentService",
                        "rpcName": "ListTrafficForecastSegments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateTrafficForecastSegment(
        _BaseTrafficForecastSegmentServiceRestTransport._BaseUpdateTrafficForecastSegment,
        TrafficForecastSegmentServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "TrafficForecastSegmentServiceRestTransport.UpdateTrafficForecastSegment"
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
            request: traffic_forecast_segment_service.UpdateTrafficForecastSegmentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> traffic_forecast_segment_messages.TrafficForecastSegment:
            r"""Call the update traffic forecast
            segment method over HTTP.

                Args:
                    request (~.traffic_forecast_segment_service.UpdateTrafficForecastSegmentRequest):
                        The request object. Request object for ``UpdateTrafficForecastSegment``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.traffic_forecast_segment_messages.TrafficForecastSegment:
                        An entity that defines a segment of
                    traffic that will be adjusted or
                    explored.

            """

            http_options = _BaseTrafficForecastSegmentServiceRestTransport._BaseUpdateTrafficForecastSegment._get_http_options()
            request, metadata = self._interceptor.pre_update_traffic_forecast_segment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTrafficForecastSegmentServiceRestTransport._BaseUpdateTrafficForecastSegment,
                    "_BaseUpdateTrafficForecastSegment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.TrafficForecastSegmentServiceClient.UpdateTrafficForecastSegment",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TrafficForecastSegmentService",
                        "rpcName": "UpdateTrafficForecastSegment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TrafficForecastSegmentServiceRestTransport._UpdateTrafficForecastSegment._get_response(
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
            resp = traffic_forecast_segment_messages.TrafficForecastSegment()
            pb_resp = traffic_forecast_segment_messages.TrafficForecastSegment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_traffic_forecast_segment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_update_traffic_forecast_segment_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = traffic_forecast_segment_messages.TrafficForecastSegment.to_json(
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
                    "Received response for google.ads.admanager_v1.TrafficForecastSegmentServiceClient.update_traffic_forecast_segment",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TrafficForecastSegmentService",
                        "rpcName": "UpdateTrafficForecastSegment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_create_traffic_forecast_segments(
        self,
    ) -> Callable[
        [traffic_forecast_segment_service.BatchCreateTrafficForecastSegmentsRequest],
        traffic_forecast_segment_service.BatchCreateTrafficForecastSegmentsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchCreateTrafficForecastSegments(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_update_traffic_forecast_segments(
        self,
    ) -> Callable[
        [traffic_forecast_segment_service.BatchUpdateTrafficForecastSegmentsRequest],
        traffic_forecast_segment_service.BatchUpdateTrafficForecastSegmentsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchUpdateTrafficForecastSegments(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_traffic_forecast_segment(
        self,
    ) -> Callable[
        [traffic_forecast_segment_service.CreateTrafficForecastSegmentRequest],
        traffic_forecast_segment_messages.TrafficForecastSegment,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateTrafficForecastSegment(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_traffic_forecast_segment(
        self,
    ) -> Callable[
        [traffic_forecast_segment_service.GetTrafficForecastSegmentRequest],
        traffic_forecast_segment_messages.TrafficForecastSegment,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetTrafficForecastSegment(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_traffic_forecast_segments(
        self,
    ) -> Callable[
        [traffic_forecast_segment_service.ListTrafficForecastSegmentsRequest],
        traffic_forecast_segment_service.ListTrafficForecastSegmentsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListTrafficForecastSegments(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_traffic_forecast_segment(
        self,
    ) -> Callable[
        [traffic_forecast_segment_service.UpdateTrafficForecastSegmentRequest],
        traffic_forecast_segment_messages.TrafficForecastSegment,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateTrafficForecastSegment(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseTrafficForecastSegmentServiceRestTransport._BaseCancelOperation,
        TrafficForecastSegmentServiceRestStub,
    ):
        def __hash__(self):
            return hash("TrafficForecastSegmentServiceRestTransport.CancelOperation")

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

            http_options = _BaseTrafficForecastSegmentServiceRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTrafficForecastSegmentServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.ads.admanager_v1.TrafficForecastSegmentServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TrafficForecastSegmentService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TrafficForecastSegmentServiceRestTransport._CancelOperation._get_response(
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
        _BaseTrafficForecastSegmentServiceRestTransport._BaseGetOperation,
        TrafficForecastSegmentServiceRestStub,
    ):
        def __hash__(self):
            return hash("TrafficForecastSegmentServiceRestTransport.GetOperation")

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

            http_options = _BaseTrafficForecastSegmentServiceRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTrafficForecastSegmentServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.ads.admanager_v1.TrafficForecastSegmentServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TrafficForecastSegmentService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                TrafficForecastSegmentServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.ads.admanager_v1.TrafficForecastSegmentServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TrafficForecastSegmentService",
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


__all__ = ("TrafficForecastSegmentServiceRestTransport",)
