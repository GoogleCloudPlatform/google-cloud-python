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

from google.ads.datamanager_v1._compat import transcode_request
from google.ads.datamanager_v1.types import ingestion_service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseIngestionServiceRestTransport

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


class IngestionServiceRestInterceptor:
    """Interceptor for IngestionService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the IngestionServiceRestTransport.

    .. code-block:: python
        class MyCustomIngestionServiceInterceptor(IngestionServiceRestInterceptor):
            def pre_ingest_ad_events(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_ingest_ad_events(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_ingest_audience_members(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_ingest_audience_members(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_ingest_events(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_ingest_events(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_ingest_users(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_ingest_users(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_remove_all_audience_members(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_remove_all_audience_members(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_remove_audience_members(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_remove_audience_members(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_remove_users(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_remove_users(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_retrieve_request_status(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_retrieve_request_status(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = IngestionServiceRestTransport(interceptor=MyCustomIngestionServiceInterceptor())
        client = IngestionServiceClient(transport=transport)


    """

    def pre_ingest_ad_events(
        self,
        request: ingestion_service.IngestAdEventsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ingestion_service.IngestAdEventsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for ingest_ad_events

        Override in a subclass to manipulate the request or metadata
        before they are sent to the IngestionService server.
        """
        return request, metadata

    def post_ingest_ad_events(
        self, response: ingestion_service.IngestAdEventsResponse
    ) -> ingestion_service.IngestAdEventsResponse:
        """Post-rpc interceptor for ingest_ad_events

        DEPRECATED. Please use the `post_ingest_ad_events_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the IngestionService server but before
        it is returned to user code. This `post_ingest_ad_events` interceptor runs
        before the `post_ingest_ad_events_with_metadata` interceptor.
        """
        return response

    def post_ingest_ad_events_with_metadata(
        self,
        response: ingestion_service.IngestAdEventsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ingestion_service.IngestAdEventsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for ingest_ad_events

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the IngestionService server but before it is returned to user code.

        We recommend only using this `post_ingest_ad_events_with_metadata`
        interceptor in new development instead of the `post_ingest_ad_events` interceptor.
        When both interceptors are used, this `post_ingest_ad_events_with_metadata` interceptor runs after the
        `post_ingest_ad_events` interceptor. The (possibly modified) response returned by
        `post_ingest_ad_events` will be passed to
        `post_ingest_ad_events_with_metadata`.
        """
        return response, metadata

    def pre_ingest_audience_members(
        self,
        request: ingestion_service.IngestAudienceMembersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ingestion_service.IngestAudienceMembersRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for ingest_audience_members

        Override in a subclass to manipulate the request or metadata
        before they are sent to the IngestionService server.
        """
        return request, metadata

    def post_ingest_audience_members(
        self, response: ingestion_service.IngestAudienceMembersResponse
    ) -> ingestion_service.IngestAudienceMembersResponse:
        """Post-rpc interceptor for ingest_audience_members

        DEPRECATED. Please use the `post_ingest_audience_members_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the IngestionService server but before
        it is returned to user code. This `post_ingest_audience_members` interceptor runs
        before the `post_ingest_audience_members_with_metadata` interceptor.
        """
        return response

    def post_ingest_audience_members_with_metadata(
        self,
        response: ingestion_service.IngestAudienceMembersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ingestion_service.IngestAudienceMembersResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for ingest_audience_members

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the IngestionService server but before it is returned to user code.

        We recommend only using this `post_ingest_audience_members_with_metadata`
        interceptor in new development instead of the `post_ingest_audience_members` interceptor.
        When both interceptors are used, this `post_ingest_audience_members_with_metadata` interceptor runs after the
        `post_ingest_audience_members` interceptor. The (possibly modified) response returned by
        `post_ingest_audience_members` will be passed to
        `post_ingest_audience_members_with_metadata`.
        """
        return response, metadata

    def pre_ingest_events(
        self,
        request: ingestion_service.IngestEventsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ingestion_service.IngestEventsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for ingest_events

        Override in a subclass to manipulate the request or metadata
        before they are sent to the IngestionService server.
        """
        return request, metadata

    def post_ingest_events(
        self, response: ingestion_service.IngestEventsResponse
    ) -> ingestion_service.IngestEventsResponse:
        """Post-rpc interceptor for ingest_events

        DEPRECATED. Please use the `post_ingest_events_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the IngestionService server but before
        it is returned to user code. This `post_ingest_events` interceptor runs
        before the `post_ingest_events_with_metadata` interceptor.
        """
        return response

    def post_ingest_events_with_metadata(
        self,
        response: ingestion_service.IngestEventsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ingestion_service.IngestEventsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for ingest_events

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the IngestionService server but before it is returned to user code.

        We recommend only using this `post_ingest_events_with_metadata`
        interceptor in new development instead of the `post_ingest_events` interceptor.
        When both interceptors are used, this `post_ingest_events_with_metadata` interceptor runs after the
        `post_ingest_events` interceptor. The (possibly modified) response returned by
        `post_ingest_events` will be passed to
        `post_ingest_events_with_metadata`.
        """
        return response, metadata

    def pre_ingest_users(
        self,
        request: ingestion_service.IngestUsersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ingestion_service.IngestUsersRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for ingest_users

        Override in a subclass to manipulate the request or metadata
        before they are sent to the IngestionService server.
        """
        return request, metadata

    def post_ingest_users(
        self, response: ingestion_service.IngestUsersResponse
    ) -> ingestion_service.IngestUsersResponse:
        """Post-rpc interceptor for ingest_users

        DEPRECATED. Please use the `post_ingest_users_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the IngestionService server but before
        it is returned to user code. This `post_ingest_users` interceptor runs
        before the `post_ingest_users_with_metadata` interceptor.
        """
        return response

    def post_ingest_users_with_metadata(
        self,
        response: ingestion_service.IngestUsersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ingestion_service.IngestUsersResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for ingest_users

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the IngestionService server but before it is returned to user code.

        We recommend only using this `post_ingest_users_with_metadata`
        interceptor in new development instead of the `post_ingest_users` interceptor.
        When both interceptors are used, this `post_ingest_users_with_metadata` interceptor runs after the
        `post_ingest_users` interceptor. The (possibly modified) response returned by
        `post_ingest_users` will be passed to
        `post_ingest_users_with_metadata`.
        """
        return response, metadata

    def pre_remove_all_audience_members(
        self,
        request: ingestion_service.RemoveAllAudienceMembersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ingestion_service.RemoveAllAudienceMembersRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for remove_all_audience_members

        Override in a subclass to manipulate the request or metadata
        before they are sent to the IngestionService server.
        """
        return request, metadata

    def post_remove_all_audience_members(
        self, response: ingestion_service.RemoveAllAudienceMembersResponse
    ) -> ingestion_service.RemoveAllAudienceMembersResponse:
        """Post-rpc interceptor for remove_all_audience_members

        DEPRECATED. Please use the `post_remove_all_audience_members_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the IngestionService server but before
        it is returned to user code. This `post_remove_all_audience_members` interceptor runs
        before the `post_remove_all_audience_members_with_metadata` interceptor.
        """
        return response

    def post_remove_all_audience_members_with_metadata(
        self,
        response: ingestion_service.RemoveAllAudienceMembersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ingestion_service.RemoveAllAudienceMembersResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for remove_all_audience_members

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the IngestionService server but before it is returned to user code.

        We recommend only using this `post_remove_all_audience_members_with_metadata`
        interceptor in new development instead of the `post_remove_all_audience_members` interceptor.
        When both interceptors are used, this `post_remove_all_audience_members_with_metadata` interceptor runs after the
        `post_remove_all_audience_members` interceptor. The (possibly modified) response returned by
        `post_remove_all_audience_members` will be passed to
        `post_remove_all_audience_members_with_metadata`.
        """
        return response, metadata

    def pre_remove_audience_members(
        self,
        request: ingestion_service.RemoveAudienceMembersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ingestion_service.RemoveAudienceMembersRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for remove_audience_members

        Override in a subclass to manipulate the request or metadata
        before they are sent to the IngestionService server.
        """
        return request, metadata

    def post_remove_audience_members(
        self, response: ingestion_service.RemoveAudienceMembersResponse
    ) -> ingestion_service.RemoveAudienceMembersResponse:
        """Post-rpc interceptor for remove_audience_members

        DEPRECATED. Please use the `post_remove_audience_members_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the IngestionService server but before
        it is returned to user code. This `post_remove_audience_members` interceptor runs
        before the `post_remove_audience_members_with_metadata` interceptor.
        """
        return response

    def post_remove_audience_members_with_metadata(
        self,
        response: ingestion_service.RemoveAudienceMembersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ingestion_service.RemoveAudienceMembersResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for remove_audience_members

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the IngestionService server but before it is returned to user code.

        We recommend only using this `post_remove_audience_members_with_metadata`
        interceptor in new development instead of the `post_remove_audience_members` interceptor.
        When both interceptors are used, this `post_remove_audience_members_with_metadata` interceptor runs after the
        `post_remove_audience_members` interceptor. The (possibly modified) response returned by
        `post_remove_audience_members` will be passed to
        `post_remove_audience_members_with_metadata`.
        """
        return response, metadata

    def pre_remove_users(
        self,
        request: ingestion_service.RemoveUsersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ingestion_service.RemoveUsersRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for remove_users

        Override in a subclass to manipulate the request or metadata
        before they are sent to the IngestionService server.
        """
        return request, metadata

    def post_remove_users(
        self, response: ingestion_service.RemoveUsersResponse
    ) -> ingestion_service.RemoveUsersResponse:
        """Post-rpc interceptor for remove_users

        DEPRECATED. Please use the `post_remove_users_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the IngestionService server but before
        it is returned to user code. This `post_remove_users` interceptor runs
        before the `post_remove_users_with_metadata` interceptor.
        """
        return response

    def post_remove_users_with_metadata(
        self,
        response: ingestion_service.RemoveUsersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ingestion_service.RemoveUsersResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for remove_users

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the IngestionService server but before it is returned to user code.

        We recommend only using this `post_remove_users_with_metadata`
        interceptor in new development instead of the `post_remove_users` interceptor.
        When both interceptors are used, this `post_remove_users_with_metadata` interceptor runs after the
        `post_remove_users` interceptor. The (possibly modified) response returned by
        `post_remove_users` will be passed to
        `post_remove_users_with_metadata`.
        """
        return response, metadata

    def pre_retrieve_request_status(
        self,
        request: ingestion_service.RetrieveRequestStatusRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ingestion_service.RetrieveRequestStatusRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for retrieve_request_status

        Override in a subclass to manipulate the request or metadata
        before they are sent to the IngestionService server.
        """
        return request, metadata

    def post_retrieve_request_status(
        self, response: ingestion_service.RetrieveRequestStatusResponse
    ) -> ingestion_service.RetrieveRequestStatusResponse:
        """Post-rpc interceptor for retrieve_request_status

        DEPRECATED. Please use the `post_retrieve_request_status_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the IngestionService server but before
        it is returned to user code. This `post_retrieve_request_status` interceptor runs
        before the `post_retrieve_request_status_with_metadata` interceptor.
        """
        return response

    def post_retrieve_request_status_with_metadata(
        self,
        response: ingestion_service.RetrieveRequestStatusResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ingestion_service.RetrieveRequestStatusResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for retrieve_request_status

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the IngestionService server but before it is returned to user code.

        We recommend only using this `post_retrieve_request_status_with_metadata`
        interceptor in new development instead of the `post_retrieve_request_status` interceptor.
        When both interceptors are used, this `post_retrieve_request_status_with_metadata` interceptor runs after the
        `post_retrieve_request_status` interceptor. The (possibly modified) response returned by
        `post_retrieve_request_status` will be passed to
        `post_retrieve_request_status_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class IngestionServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: IngestionServiceRestInterceptor


class IngestionServiceRestTransport(_BaseIngestionServiceRestTransport):
    """REST backend synchronous transport for IngestionService.

    Service for sending audience data to supported destinations.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "datamanager.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[IngestionServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'datamanager.googleapis.com').
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
            interceptor (Optional[IngestionServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or IngestionServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _IngestAdEvents(
        _BaseIngestionServiceRestTransport._BaseIngestAdEvents, IngestionServiceRestStub
    ):
        def __hash__(self):
            return hash("IngestionServiceRestTransport.IngestAdEvents")

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
            request: ingestion_service.IngestAdEventsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ingestion_service.IngestAdEventsResponse:
            r"""Call the ingest ad events method over HTTP.

            Args:
                request (~.ingestion_service.IngestAdEventsRequest):
                    The request object. Request to upload ad events.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ingestion_service.IngestAdEventsResponse:
                    Response from an ad event ingestion
                operation.

            """

            http_options = _BaseIngestionServiceRestTransport._BaseIngestAdEvents._get_http_options()
            request, metadata = self._interceptor.pre_ingest_ad_events(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseIngestionServiceRestTransport._BaseIngestAdEvents,
                    "_BaseIngestAdEvents__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.datamanager_v1.IngestionServiceClient.IngestAdEvents",
                    extra={
                        "serviceName": "google.ads.datamanager.v1.IngestionService",
                        "rpcName": "IngestAdEvents",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = IngestionServiceRestTransport._IngestAdEvents._get_response(
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
            resp = ingestion_service.IngestAdEventsResponse()
            pb_resp = ingestion_service.IngestAdEventsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_ingest_ad_events(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_ingest_ad_events_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = ingestion_service.IngestAdEventsResponse.to_json(
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
                    "Received response for google.ads.datamanager_v1.IngestionServiceClient.ingest_ad_events",
                    extra={
                        "serviceName": "google.ads.datamanager.v1.IngestionService",
                        "rpcName": "IngestAdEvents",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _IngestAudienceMembers(
        _BaseIngestionServiceRestTransport._BaseIngestAudienceMembers,
        IngestionServiceRestStub,
    ):
        def __hash__(self):
            return hash("IngestionServiceRestTransport.IngestAudienceMembers")

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
            request: ingestion_service.IngestAudienceMembersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ingestion_service.IngestAudienceMembersResponse:
            r"""Call the ingest audience members method over HTTP.

            Args:
                request (~.ingestion_service.IngestAudienceMembersRequest):
                    The request object. Request to upload audience members to the provided
                destinations. Returns an
                [IngestAudienceMembersResponse][google.ads.datamanager.v1.IngestAudienceMembersResponse].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ingestion_service.IngestAudienceMembersResponse:
                    Response from the
                [IngestAudienceMembersRequest][google.ads.datamanager.v1.IngestAudienceMembersRequest].

            """

            http_options = _BaseIngestionServiceRestTransport._BaseIngestAudienceMembers._get_http_options()
            request, metadata = self._interceptor.pre_ingest_audience_members(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseIngestionServiceRestTransport._BaseIngestAudienceMembers,
                    "_BaseIngestAudienceMembers__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.datamanager_v1.IngestionServiceClient.IngestAudienceMembers",
                    extra={
                        "serviceName": "google.ads.datamanager.v1.IngestionService",
                        "rpcName": "IngestAudienceMembers",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                IngestionServiceRestTransport._IngestAudienceMembers._get_response(
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
            resp = ingestion_service.IngestAudienceMembersResponse()
            pb_resp = ingestion_service.IngestAudienceMembersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_ingest_audience_members(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_ingest_audience_members_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        ingestion_service.IngestAudienceMembersResponse.to_json(
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
                    "Received response for google.ads.datamanager_v1.IngestionServiceClient.ingest_audience_members",
                    extra={
                        "serviceName": "google.ads.datamanager.v1.IngestionService",
                        "rpcName": "IngestAudienceMembers",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _IngestEvents(
        _BaseIngestionServiceRestTransport._BaseIngestEvents, IngestionServiceRestStub
    ):
        def __hash__(self):
            return hash("IngestionServiceRestTransport.IngestEvents")

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
            request: ingestion_service.IngestEventsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ingestion_service.IngestEventsResponse:
            r"""Call the ingest events method over HTTP.

            Args:
                request (~.ingestion_service.IngestEventsRequest):
                    The request object. Request to upload audience members to the provided
                destinations. Returns an
                [IngestEventsResponse][google.ads.datamanager.v1.IngestEventsResponse].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ingestion_service.IngestEventsResponse:
                    Response from the
                [IngestEventsRequest][google.ads.datamanager.v1.IngestEventsRequest].

            """

            http_options = (
                _BaseIngestionServiceRestTransport._BaseIngestEvents._get_http_options()
            )
            request, metadata = self._interceptor.pre_ingest_events(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseIngestionServiceRestTransport._BaseIngestEvents,
                    "_BaseIngestEvents__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.datamanager_v1.IngestionServiceClient.IngestEvents",
                    extra={
                        "serviceName": "google.ads.datamanager.v1.IngestionService",
                        "rpcName": "IngestEvents",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = IngestionServiceRestTransport._IngestEvents._get_response(
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
            resp = ingestion_service.IngestEventsResponse()
            pb_resp = ingestion_service.IngestEventsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_ingest_events(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_ingest_events_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = ingestion_service.IngestEventsResponse.to_json(
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
                    "Received response for google.ads.datamanager_v1.IngestionServiceClient.ingest_events",
                    extra={
                        "serviceName": "google.ads.datamanager.v1.IngestionService",
                        "rpcName": "IngestEvents",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _IngestUsers(
        _BaseIngestionServiceRestTransport._BaseIngestUsers, IngestionServiceRestStub
    ):
        def __hash__(self):
            return hash("IngestionServiceRestTransport.IngestUsers")

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
            request: ingestion_service.IngestUsersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ingestion_service.IngestUsersResponse:
            r"""Call the ingest users method over HTTP.

            Args:
                request (~.ingestion_service.IngestUsersRequest):
                    The request object. Request to upload users to the
                provided destinations.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ingestion_service.IngestUsersResponse:
                    Response from the IngestUsersRequest.
            """

            http_options = (
                _BaseIngestionServiceRestTransport._BaseIngestUsers._get_http_options()
            )
            request, metadata = self._interceptor.pre_ingest_users(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseIngestionServiceRestTransport._BaseIngestUsers,
                    "_BaseIngestUsers__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.datamanager_v1.IngestionServiceClient.IngestUsers",
                    extra={
                        "serviceName": "google.ads.datamanager.v1.IngestionService",
                        "rpcName": "IngestUsers",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = IngestionServiceRestTransport._IngestUsers._get_response(
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
            resp = ingestion_service.IngestUsersResponse()
            pb_resp = ingestion_service.IngestUsersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_ingest_users(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_ingest_users_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = ingestion_service.IngestUsersResponse.to_json(
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
                    "Received response for google.ads.datamanager_v1.IngestionServiceClient.ingest_users",
                    extra={
                        "serviceName": "google.ads.datamanager.v1.IngestionService",
                        "rpcName": "IngestUsers",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RemoveAllAudienceMembers(
        _BaseIngestionServiceRestTransport._BaseRemoveAllAudienceMembers,
        IngestionServiceRestStub,
    ):
        def __hash__(self):
            return hash("IngestionServiceRestTransport.RemoveAllAudienceMembers")

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
            request: ingestion_service.RemoveAllAudienceMembersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ingestion_service.RemoveAllAudienceMembersResponse:
            r"""Call the remove all audience
            members method over HTTP.

                Args:
                    request (~.ingestion_service.RemoveAllAudienceMembersRequest):
                        The request object. Request to remove all users from an audience in the
                    provided destinations. Returns a
                    [RemoveAllAudienceMembersResponse][google.ads.datamanager.v1.RemoveAllAudienceMembersResponse].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.ingestion_service.RemoveAllAudienceMembersResponse:
                        Response from the
                    [RemoveAllAudienceMembersRequest][google.ads.datamanager.v1.RemoveAllAudienceMembersRequest].

            """

            http_options = _BaseIngestionServiceRestTransport._BaseRemoveAllAudienceMembers._get_http_options()
            request, metadata = self._interceptor.pre_remove_all_audience_members(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseIngestionServiceRestTransport._BaseRemoveAllAudienceMembers,
                    "_BaseRemoveAllAudienceMembers__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.datamanager_v1.IngestionServiceClient.RemoveAllAudienceMembers",
                    extra={
                        "serviceName": "google.ads.datamanager.v1.IngestionService",
                        "rpcName": "RemoveAllAudienceMembers",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                IngestionServiceRestTransport._RemoveAllAudienceMembers._get_response(
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
            resp = ingestion_service.RemoveAllAudienceMembersResponse()
            pb_resp = ingestion_service.RemoveAllAudienceMembersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_remove_all_audience_members(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_remove_all_audience_members_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        ingestion_service.RemoveAllAudienceMembersResponse.to_json(
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
                    "Received response for google.ads.datamanager_v1.IngestionServiceClient.remove_all_audience_members",
                    extra={
                        "serviceName": "google.ads.datamanager.v1.IngestionService",
                        "rpcName": "RemoveAllAudienceMembers",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RemoveAudienceMembers(
        _BaseIngestionServiceRestTransport._BaseRemoveAudienceMembers,
        IngestionServiceRestStub,
    ):
        def __hash__(self):
            return hash("IngestionServiceRestTransport.RemoveAudienceMembers")

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
            request: ingestion_service.RemoveAudienceMembersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ingestion_service.RemoveAudienceMembersResponse:
            r"""Call the remove audience members method over HTTP.

            Args:
                request (~.ingestion_service.RemoveAudienceMembersRequest):
                    The request object. Request to remove users from an audience in the provided
                destinations. Returns a
                [RemoveAudienceMembersResponse][google.ads.datamanager.v1.RemoveAudienceMembersResponse].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ingestion_service.RemoveAudienceMembersResponse:
                    Response from the
                [RemoveAudienceMembersRequest][google.ads.datamanager.v1.RemoveAudienceMembersRequest].

            """

            http_options = _BaseIngestionServiceRestTransport._BaseRemoveAudienceMembers._get_http_options()
            request, metadata = self._interceptor.pre_remove_audience_members(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseIngestionServiceRestTransport._BaseRemoveAudienceMembers,
                    "_BaseRemoveAudienceMembers__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.datamanager_v1.IngestionServiceClient.RemoveAudienceMembers",
                    extra={
                        "serviceName": "google.ads.datamanager.v1.IngestionService",
                        "rpcName": "RemoveAudienceMembers",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                IngestionServiceRestTransport._RemoveAudienceMembers._get_response(
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
            resp = ingestion_service.RemoveAudienceMembersResponse()
            pb_resp = ingestion_service.RemoveAudienceMembersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_remove_audience_members(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_remove_audience_members_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        ingestion_service.RemoveAudienceMembersResponse.to_json(
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
                    "Received response for google.ads.datamanager_v1.IngestionServiceClient.remove_audience_members",
                    extra={
                        "serviceName": "google.ads.datamanager.v1.IngestionService",
                        "rpcName": "RemoveAudienceMembers",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RemoveUsers(
        _BaseIngestionServiceRestTransport._BaseRemoveUsers, IngestionServiceRestStub
    ):
        def __hash__(self):
            return hash("IngestionServiceRestTransport.RemoveUsers")

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
            request: ingestion_service.RemoveUsersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ingestion_service.RemoveUsersResponse:
            r"""Call the remove users method over HTTP.

            Args:
                request (~.ingestion_service.RemoveUsersRequest):
                    The request object. Request to remove users from the
                provided destinations.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ingestion_service.RemoveUsersResponse:
                    Response from the RemoveUsersRequest.
            """

            http_options = (
                _BaseIngestionServiceRestTransport._BaseRemoveUsers._get_http_options()
            )
            request, metadata = self._interceptor.pre_remove_users(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseIngestionServiceRestTransport._BaseRemoveUsers,
                    "_BaseRemoveUsers__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.datamanager_v1.IngestionServiceClient.RemoveUsers",
                    extra={
                        "serviceName": "google.ads.datamanager.v1.IngestionService",
                        "rpcName": "RemoveUsers",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = IngestionServiceRestTransport._RemoveUsers._get_response(
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
            resp = ingestion_service.RemoveUsersResponse()
            pb_resp = ingestion_service.RemoveUsersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_remove_users(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_remove_users_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = ingestion_service.RemoveUsersResponse.to_json(
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
                    "Received response for google.ads.datamanager_v1.IngestionServiceClient.remove_users",
                    extra={
                        "serviceName": "google.ads.datamanager.v1.IngestionService",
                        "rpcName": "RemoveUsers",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RetrieveRequestStatus(
        _BaseIngestionServiceRestTransport._BaseRetrieveRequestStatus,
        IngestionServiceRestStub,
    ):
        def __hash__(self):
            return hash("IngestionServiceRestTransport.RetrieveRequestStatus")

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
            request: ingestion_service.RetrieveRequestStatusRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ingestion_service.RetrieveRequestStatusResponse:
            r"""Call the retrieve request status method over HTTP.

            Args:
                request (~.ingestion_service.RetrieveRequestStatusRequest):
                    The request object. Request to get the status of request made to the DM API
                for a given request ID. Returns a
                [RetrieveRequestStatusResponse][google.ads.datamanager.v1.RetrieveRequestStatusResponse].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ingestion_service.RetrieveRequestStatusResponse:
                    Response from the
                [RetrieveRequestStatusRequest][google.ads.datamanager.v1.RetrieveRequestStatusRequest].

            """

            http_options = _BaseIngestionServiceRestTransport._BaseRetrieveRequestStatus._get_http_options()
            request, metadata = self._interceptor.pre_retrieve_request_status(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseIngestionServiceRestTransport._BaseRetrieveRequestStatus,
                    "_BaseRetrieveRequestStatus__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.datamanager_v1.IngestionServiceClient.RetrieveRequestStatus",
                    extra={
                        "serviceName": "google.ads.datamanager.v1.IngestionService",
                        "rpcName": "RetrieveRequestStatus",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                IngestionServiceRestTransport._RetrieveRequestStatus._get_response(
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
            resp = ingestion_service.RetrieveRequestStatusResponse()
            pb_resp = ingestion_service.RetrieveRequestStatusResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_retrieve_request_status(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_retrieve_request_status_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        ingestion_service.RetrieveRequestStatusResponse.to_json(
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
                    "Received response for google.ads.datamanager_v1.IngestionServiceClient.retrieve_request_status",
                    extra={
                        "serviceName": "google.ads.datamanager.v1.IngestionService",
                        "rpcName": "RetrieveRequestStatus",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def ingest_ad_events(
        self,
    ) -> Callable[
        [ingestion_service.IngestAdEventsRequest],
        ingestion_service.IngestAdEventsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._IngestAdEvents(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def ingest_audience_members(
        self,
    ) -> Callable[
        [ingestion_service.IngestAudienceMembersRequest],
        ingestion_service.IngestAudienceMembersResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._IngestAudienceMembers(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def ingest_events(
        self,
    ) -> Callable[
        [ingestion_service.IngestEventsRequest], ingestion_service.IngestEventsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._IngestEvents(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def ingest_users(
        self,
    ) -> Callable[
        [ingestion_service.IngestUsersRequest], ingestion_service.IngestUsersResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._IngestUsers(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def remove_all_audience_members(
        self,
    ) -> Callable[
        [ingestion_service.RemoveAllAudienceMembersRequest],
        ingestion_service.RemoveAllAudienceMembersResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RemoveAllAudienceMembers(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def remove_audience_members(
        self,
    ) -> Callable[
        [ingestion_service.RemoveAudienceMembersRequest],
        ingestion_service.RemoveAudienceMembersResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RemoveAudienceMembers(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def remove_users(
        self,
    ) -> Callable[
        [ingestion_service.RemoveUsersRequest], ingestion_service.RemoveUsersResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RemoveUsers(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def retrieve_request_status(
        self,
    ) -> Callable[
        [ingestion_service.RetrieveRequestStatusRequest],
        ingestion_service.RetrieveRequestStatusResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RetrieveRequestStatus(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("IngestionServiceRestTransport",)
