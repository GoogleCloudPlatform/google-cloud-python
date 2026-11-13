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
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.errorreporting_v1beta1._compat import transcode_request
from google.cloud.errorreporting_v1beta1.types import error_stats_service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseErrorStatsServiceRestTransport

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


class ErrorStatsServiceRestInterceptor:
    """Interceptor for ErrorStatsService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the ErrorStatsServiceRestTransport.

    .. code-block:: python
        class MyCustomErrorStatsServiceInterceptor(ErrorStatsServiceRestInterceptor):
            def pre_delete_events(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_events(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_events(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_events(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_group_stats(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_group_stats(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = ErrorStatsServiceRestTransport(interceptor=MyCustomErrorStatsServiceInterceptor())
        client = ErrorStatsServiceClient(transport=transport)


    """

    def pre_delete_events(
        self,
        request: error_stats_service.DeleteEventsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        error_stats_service.DeleteEventsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_events

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ErrorStatsService server.
        """
        return request, metadata

    def post_delete_events(
        self, response: error_stats_service.DeleteEventsResponse
    ) -> error_stats_service.DeleteEventsResponse:
        """Post-rpc interceptor for delete_events

        DEPRECATED. Please use the `post_delete_events_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ErrorStatsService server but before
        it is returned to user code. This `post_delete_events` interceptor runs
        before the `post_delete_events_with_metadata` interceptor.
        """
        return response

    def post_delete_events_with_metadata(
        self,
        response: error_stats_service.DeleteEventsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        error_stats_service.DeleteEventsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for delete_events

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ErrorStatsService server but before it is returned to user code.

        We recommend only using this `post_delete_events_with_metadata`
        interceptor in new development instead of the `post_delete_events` interceptor.
        When both interceptors are used, this `post_delete_events_with_metadata` interceptor runs after the
        `post_delete_events` interceptor. The (possibly modified) response returned by
        `post_delete_events` will be passed to
        `post_delete_events_with_metadata`.
        """
        return response, metadata

    def pre_list_events(
        self,
        request: error_stats_service.ListEventsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        error_stats_service.ListEventsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_events

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ErrorStatsService server.
        """
        return request, metadata

    def post_list_events(
        self, response: error_stats_service.ListEventsResponse
    ) -> error_stats_service.ListEventsResponse:
        """Post-rpc interceptor for list_events

        DEPRECATED. Please use the `post_list_events_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ErrorStatsService server but before
        it is returned to user code. This `post_list_events` interceptor runs
        before the `post_list_events_with_metadata` interceptor.
        """
        return response

    def post_list_events_with_metadata(
        self,
        response: error_stats_service.ListEventsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        error_stats_service.ListEventsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_events

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ErrorStatsService server but before it is returned to user code.

        We recommend only using this `post_list_events_with_metadata`
        interceptor in new development instead of the `post_list_events` interceptor.
        When both interceptors are used, this `post_list_events_with_metadata` interceptor runs after the
        `post_list_events` interceptor. The (possibly modified) response returned by
        `post_list_events` will be passed to
        `post_list_events_with_metadata`.
        """
        return response, metadata

    def pre_list_group_stats(
        self,
        request: error_stats_service.ListGroupStatsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        error_stats_service.ListGroupStatsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_group_stats

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ErrorStatsService server.
        """
        return request, metadata

    def post_list_group_stats(
        self, response: error_stats_service.ListGroupStatsResponse
    ) -> error_stats_service.ListGroupStatsResponse:
        """Post-rpc interceptor for list_group_stats

        DEPRECATED. Please use the `post_list_group_stats_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ErrorStatsService server but before
        it is returned to user code. This `post_list_group_stats` interceptor runs
        before the `post_list_group_stats_with_metadata` interceptor.
        """
        return response

    def post_list_group_stats_with_metadata(
        self,
        response: error_stats_service.ListGroupStatsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        error_stats_service.ListGroupStatsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_group_stats

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ErrorStatsService server but before it is returned to user code.

        We recommend only using this `post_list_group_stats_with_metadata`
        interceptor in new development instead of the `post_list_group_stats` interceptor.
        When both interceptors are used, this `post_list_group_stats_with_metadata` interceptor runs after the
        `post_list_group_stats` interceptor. The (possibly modified) response returned by
        `post_list_group_stats` will be passed to
        `post_list_group_stats_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class ErrorStatsServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: ErrorStatsServiceRestInterceptor


class ErrorStatsServiceRestTransport(_BaseErrorStatsServiceRestTransport):
    """REST backend synchronous transport for ErrorStatsService.

    An API for retrieving and managing error statistics as well
    as data for individual events.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "clouderrorreporting.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[ErrorStatsServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'clouderrorreporting.googleapis.com').
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
            interceptor (Optional[ErrorStatsServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or ErrorStatsServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _DeleteEvents(
        _BaseErrorStatsServiceRestTransport._BaseDeleteEvents, ErrorStatsServiceRestStub
    ):
        def __hash__(self):
            return hash("ErrorStatsServiceRestTransport.DeleteEvents")

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
            request: error_stats_service.DeleteEventsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> error_stats_service.DeleteEventsResponse:
            r"""Call the delete events method over HTTP.

            Args:
                request (~.error_stats_service.DeleteEventsRequest):
                    The request object. Deletes all events in the project.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.error_stats_service.DeleteEventsResponse:
                    Response message for deleting error
                events.

            """

            http_options = _BaseErrorStatsServiceRestTransport._BaseDeleteEvents._get_http_options()
            request, metadata = self._interceptor.pre_delete_events(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseErrorStatsServiceRestTransport._BaseDeleteEvents,
                    "_BaseDeleteEvents__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.clouderrorreporting_v1beta1.ErrorStatsServiceClient.DeleteEvents",
                    extra={
                        "serviceName": "google.devtools.clouderrorreporting.v1beta1.ErrorStatsService",
                        "rpcName": "DeleteEvents",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ErrorStatsServiceRestTransport._DeleteEvents._get_response(
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
            resp = error_stats_service.DeleteEventsResponse()
            pb_resp = error_stats_service.DeleteEventsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_events(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_events_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = error_stats_service.DeleteEventsResponse.to_json(
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
                    "Received response for google.devtools.clouderrorreporting_v1beta1.ErrorStatsServiceClient.delete_events",
                    extra={
                        "serviceName": "google.devtools.clouderrorreporting.v1beta1.ErrorStatsService",
                        "rpcName": "DeleteEvents",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListEvents(
        _BaseErrorStatsServiceRestTransport._BaseListEvents, ErrorStatsServiceRestStub
    ):
        def __hash__(self):
            return hash("ErrorStatsServiceRestTransport.ListEvents")

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
            request: error_stats_service.ListEventsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> error_stats_service.ListEventsResponse:
            r"""Call the list events method over HTTP.

            Args:
                request (~.error_stats_service.ListEventsRequest):
                    The request object. Specifies a set of error events to
                return.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.error_stats_service.ListEventsResponse:
                    Contains a set of requested error
                events.

            """

            http_options = (
                _BaseErrorStatsServiceRestTransport._BaseListEvents._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_events(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseErrorStatsServiceRestTransport._BaseListEvents,
                    "_BaseListEvents__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.clouderrorreporting_v1beta1.ErrorStatsServiceClient.ListEvents",
                    extra={
                        "serviceName": "google.devtools.clouderrorreporting.v1beta1.ErrorStatsService",
                        "rpcName": "ListEvents",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ErrorStatsServiceRestTransport._ListEvents._get_response(
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
            resp = error_stats_service.ListEventsResponse()
            pb_resp = error_stats_service.ListEventsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_events(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_events_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = error_stats_service.ListEventsResponse.to_json(
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
                    "Received response for google.devtools.clouderrorreporting_v1beta1.ErrorStatsServiceClient.list_events",
                    extra={
                        "serviceName": "google.devtools.clouderrorreporting.v1beta1.ErrorStatsService",
                        "rpcName": "ListEvents",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListGroupStats(
        _BaseErrorStatsServiceRestTransport._BaseListGroupStats,
        ErrorStatsServiceRestStub,
    ):
        def __hash__(self):
            return hash("ErrorStatsServiceRestTransport.ListGroupStats")

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
            request: error_stats_service.ListGroupStatsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> error_stats_service.ListGroupStatsResponse:
            r"""Call the list group stats method over HTTP.

            Args:
                request (~.error_stats_service.ListGroupStatsRequest):
                    The request object. Specifies a set of ``ErrorGroupStats`` to return.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.error_stats_service.ListGroupStatsResponse:
                    Contains a set of requested error
                group stats.

            """

            http_options = _BaseErrorStatsServiceRestTransport._BaseListGroupStats._get_http_options()
            request, metadata = self._interceptor.pre_list_group_stats(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseErrorStatsServiceRestTransport._BaseListGroupStats,
                    "_BaseListGroupStats__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.clouderrorreporting_v1beta1.ErrorStatsServiceClient.ListGroupStats",
                    extra={
                        "serviceName": "google.devtools.clouderrorreporting.v1beta1.ErrorStatsService",
                        "rpcName": "ListGroupStats",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ErrorStatsServiceRestTransport._ListGroupStats._get_response(
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
            resp = error_stats_service.ListGroupStatsResponse()
            pb_resp = error_stats_service.ListGroupStatsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_group_stats(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_group_stats_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        error_stats_service.ListGroupStatsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.devtools.clouderrorreporting_v1beta1.ErrorStatsServiceClient.list_group_stats",
                    extra={
                        "serviceName": "google.devtools.clouderrorreporting.v1beta1.ErrorStatsService",
                        "rpcName": "ListGroupStats",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def delete_events(
        self,
    ) -> Callable[
        [error_stats_service.DeleteEventsRequest],
        error_stats_service.DeleteEventsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteEvents(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_events(
        self,
    ) -> Callable[
        [error_stats_service.ListEventsRequest], error_stats_service.ListEventsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListEvents(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_group_stats(
        self,
    ) -> Callable[
        [error_stats_service.ListGroupStatsRequest],
        error_stats_service.ListGroupStatsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListGroupStats(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("ErrorStatsServiceRestTransport",)
