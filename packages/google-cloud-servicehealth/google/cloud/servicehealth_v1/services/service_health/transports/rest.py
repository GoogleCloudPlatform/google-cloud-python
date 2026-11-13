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

from google.cloud.servicehealth_v1._compat import transcode_request
from google.cloud.servicehealth_v1.types import event_resources

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseServiceHealthRestTransport

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


class ServiceHealthRestInterceptor:
    """Interceptor for ServiceHealth.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the ServiceHealthRestTransport.

    .. code-block:: python
        class MyCustomServiceHealthInterceptor(ServiceHealthRestInterceptor):
            def pre_get_event(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_event(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_organization_event(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_organization_event(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_organization_impact(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_organization_impact(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_events(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_events(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_organization_events(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_organization_events(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_organization_impacts(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_organization_impacts(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = ServiceHealthRestTransport(interceptor=MyCustomServiceHealthInterceptor())
        client = ServiceHealthClient(transport=transport)


    """

    def pre_get_event(
        self,
        request: event_resources.GetEventRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        event_resources.GetEventRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_event

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ServiceHealth server.
        """
        return request, metadata

    def post_get_event(self, response: event_resources.Event) -> event_resources.Event:
        """Post-rpc interceptor for get_event

        DEPRECATED. Please use the `post_get_event_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ServiceHealth server but before
        it is returned to user code. This `post_get_event` interceptor runs
        before the `post_get_event_with_metadata` interceptor.
        """
        return response

    def post_get_event_with_metadata(
        self,
        response: event_resources.Event,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[event_resources.Event, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_event

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ServiceHealth server but before it is returned to user code.

        We recommend only using this `post_get_event_with_metadata`
        interceptor in new development instead of the `post_get_event` interceptor.
        When both interceptors are used, this `post_get_event_with_metadata` interceptor runs after the
        `post_get_event` interceptor. The (possibly modified) response returned by
        `post_get_event` will be passed to
        `post_get_event_with_metadata`.
        """
        return response, metadata

    def pre_get_organization_event(
        self,
        request: event_resources.GetOrganizationEventRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        event_resources.GetOrganizationEventRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_organization_event

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ServiceHealth server.
        """
        return request, metadata

    def post_get_organization_event(
        self, response: event_resources.OrganizationEvent
    ) -> event_resources.OrganizationEvent:
        """Post-rpc interceptor for get_organization_event

        DEPRECATED. Please use the `post_get_organization_event_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ServiceHealth server but before
        it is returned to user code. This `post_get_organization_event` interceptor runs
        before the `post_get_organization_event_with_metadata` interceptor.
        """
        return response

    def post_get_organization_event_with_metadata(
        self,
        response: event_resources.OrganizationEvent,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        event_resources.OrganizationEvent, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_organization_event

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ServiceHealth server but before it is returned to user code.

        We recommend only using this `post_get_organization_event_with_metadata`
        interceptor in new development instead of the `post_get_organization_event` interceptor.
        When both interceptors are used, this `post_get_organization_event_with_metadata` interceptor runs after the
        `post_get_organization_event` interceptor. The (possibly modified) response returned by
        `post_get_organization_event` will be passed to
        `post_get_organization_event_with_metadata`.
        """
        return response, metadata

    def pre_get_organization_impact(
        self,
        request: event_resources.GetOrganizationImpactRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        event_resources.GetOrganizationImpactRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_organization_impact

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ServiceHealth server.
        """
        return request, metadata

    def post_get_organization_impact(
        self, response: event_resources.OrganizationImpact
    ) -> event_resources.OrganizationImpact:
        """Post-rpc interceptor for get_organization_impact

        DEPRECATED. Please use the `post_get_organization_impact_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ServiceHealth server but before
        it is returned to user code. This `post_get_organization_impact` interceptor runs
        before the `post_get_organization_impact_with_metadata` interceptor.
        """
        return response

    def post_get_organization_impact_with_metadata(
        self,
        response: event_resources.OrganizationImpact,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        event_resources.OrganizationImpact, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_organization_impact

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ServiceHealth server but before it is returned to user code.

        We recommend only using this `post_get_organization_impact_with_metadata`
        interceptor in new development instead of the `post_get_organization_impact` interceptor.
        When both interceptors are used, this `post_get_organization_impact_with_metadata` interceptor runs after the
        `post_get_organization_impact` interceptor. The (possibly modified) response returned by
        `post_get_organization_impact` will be passed to
        `post_get_organization_impact_with_metadata`.
        """
        return response, metadata

    def pre_list_events(
        self,
        request: event_resources.ListEventsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        event_resources.ListEventsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_events

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ServiceHealth server.
        """
        return request, metadata

    def post_list_events(
        self, response: event_resources.ListEventsResponse
    ) -> event_resources.ListEventsResponse:
        """Post-rpc interceptor for list_events

        DEPRECATED. Please use the `post_list_events_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ServiceHealth server but before
        it is returned to user code. This `post_list_events` interceptor runs
        before the `post_list_events_with_metadata` interceptor.
        """
        return response

    def post_list_events_with_metadata(
        self,
        response: event_resources.ListEventsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        event_resources.ListEventsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_events

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ServiceHealth server but before it is returned to user code.

        We recommend only using this `post_list_events_with_metadata`
        interceptor in new development instead of the `post_list_events` interceptor.
        When both interceptors are used, this `post_list_events_with_metadata` interceptor runs after the
        `post_list_events` interceptor. The (possibly modified) response returned by
        `post_list_events` will be passed to
        `post_list_events_with_metadata`.
        """
        return response, metadata

    def pre_list_organization_events(
        self,
        request: event_resources.ListOrganizationEventsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        event_resources.ListOrganizationEventsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_organization_events

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ServiceHealth server.
        """
        return request, metadata

    def post_list_organization_events(
        self, response: event_resources.ListOrganizationEventsResponse
    ) -> event_resources.ListOrganizationEventsResponse:
        """Post-rpc interceptor for list_organization_events

        DEPRECATED. Please use the `post_list_organization_events_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ServiceHealth server but before
        it is returned to user code. This `post_list_organization_events` interceptor runs
        before the `post_list_organization_events_with_metadata` interceptor.
        """
        return response

    def post_list_organization_events_with_metadata(
        self,
        response: event_resources.ListOrganizationEventsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        event_resources.ListOrganizationEventsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_organization_events

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ServiceHealth server but before it is returned to user code.

        We recommend only using this `post_list_organization_events_with_metadata`
        interceptor in new development instead of the `post_list_organization_events` interceptor.
        When both interceptors are used, this `post_list_organization_events_with_metadata` interceptor runs after the
        `post_list_organization_events` interceptor. The (possibly modified) response returned by
        `post_list_organization_events` will be passed to
        `post_list_organization_events_with_metadata`.
        """
        return response, metadata

    def pre_list_organization_impacts(
        self,
        request: event_resources.ListOrganizationImpactsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        event_resources.ListOrganizationImpactsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_organization_impacts

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ServiceHealth server.
        """
        return request, metadata

    def post_list_organization_impacts(
        self, response: event_resources.ListOrganizationImpactsResponse
    ) -> event_resources.ListOrganizationImpactsResponse:
        """Post-rpc interceptor for list_organization_impacts

        DEPRECATED. Please use the `post_list_organization_impacts_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ServiceHealth server but before
        it is returned to user code. This `post_list_organization_impacts` interceptor runs
        before the `post_list_organization_impacts_with_metadata` interceptor.
        """
        return response

    def post_list_organization_impacts_with_metadata(
        self,
        response: event_resources.ListOrganizationImpactsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        event_resources.ListOrganizationImpactsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_organization_impacts

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ServiceHealth server but before it is returned to user code.

        We recommend only using this `post_list_organization_impacts_with_metadata`
        interceptor in new development instead of the `post_list_organization_impacts` interceptor.
        When both interceptors are used, this `post_list_organization_impacts_with_metadata` interceptor runs after the
        `post_list_organization_impacts` interceptor. The (possibly modified) response returned by
        `post_list_organization_impacts` will be passed to
        `post_list_organization_impacts_with_metadata`.
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
        before they are sent to the ServiceHealth server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the ServiceHealth server but before
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
        before they are sent to the ServiceHealth server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the ServiceHealth server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class ServiceHealthRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: ServiceHealthRestInterceptor


class ServiceHealthRestTransport(_BaseServiceHealthRestTransport):
    """REST backend synchronous transport for ServiceHealth.

    Request service health events relevant to your Google Cloud
    project.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "servicehealth.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[ServiceHealthRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'servicehealth.googleapis.com').
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
            interceptor (Optional[ServiceHealthRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or ServiceHealthRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _GetEvent(
        _BaseServiceHealthRestTransport._BaseGetEvent, ServiceHealthRestStub
    ):
        def __hash__(self):
            return hash("ServiceHealthRestTransport.GetEvent")

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
            request: event_resources.GetEventRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> event_resources.Event:
            r"""Call the get event method over HTTP.

            Args:
                request (~.event_resources.GetEventRequest):
                    The request object. Gets information about a specific
                event.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.event_resources.Event:
                    Represents service health events that
                may affect Google Cloud products. Event
                resource is a read-only view and does
                not allow any modifications. All fields
                are output only.

            """

            http_options = (
                _BaseServiceHealthRestTransport._BaseGetEvent._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_event(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseServiceHealthRestTransport._BaseGetEvent,
                    "_BaseGetEvent__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.servicehealth_v1.ServiceHealthClient.GetEvent",
                    extra={
                        "serviceName": "google.cloud.servicehealth.v1.ServiceHealth",
                        "rpcName": "GetEvent",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ServiceHealthRestTransport._GetEvent._get_response(
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
            resp = event_resources.Event()
            pb_resp = event_resources.Event.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_event(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_event_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = event_resources.Event.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.servicehealth_v1.ServiceHealthClient.get_event",
                    extra={
                        "serviceName": "google.cloud.servicehealth.v1.ServiceHealth",
                        "rpcName": "GetEvent",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetOrganizationEvent(
        _BaseServiceHealthRestTransport._BaseGetOrganizationEvent, ServiceHealthRestStub
    ):
        def __hash__(self):
            return hash("ServiceHealthRestTransport.GetOrganizationEvent")

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
            request: event_resources.GetOrganizationEventRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> event_resources.OrganizationEvent:
            r"""Call the get organization event method over HTTP.

            Args:
                request (~.event_resources.GetOrganizationEventRequest):
                    The request object. Gets information about a specific
                event affecting an organization.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.event_resources.OrganizationEvent:
                    Represents service health events that
                may affect Google Cloud products used
                across the organization. It is a
                read-only view and does not allow any
                modifications.

            """

            http_options = _BaseServiceHealthRestTransport._BaseGetOrganizationEvent._get_http_options()
            request, metadata = self._interceptor.pre_get_organization_event(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseServiceHealthRestTransport._BaseGetOrganizationEvent,
                    "_BaseGetOrganizationEvent__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.servicehealth_v1.ServiceHealthClient.GetOrganizationEvent",
                    extra={
                        "serviceName": "google.cloud.servicehealth.v1.ServiceHealth",
                        "rpcName": "GetOrganizationEvent",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ServiceHealthRestTransport._GetOrganizationEvent._get_response(
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
            resp = event_resources.OrganizationEvent()
            pb_resp = event_resources.OrganizationEvent.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_organization_event(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_organization_event_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = event_resources.OrganizationEvent.to_json(
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
                    "Received response for google.cloud.servicehealth_v1.ServiceHealthClient.get_organization_event",
                    extra={
                        "serviceName": "google.cloud.servicehealth.v1.ServiceHealth",
                        "rpcName": "GetOrganizationEvent",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetOrganizationImpact(
        _BaseServiceHealthRestTransport._BaseGetOrganizationImpact,
        ServiceHealthRestStub,
    ):
        def __hash__(self):
            return hash("ServiceHealthRestTransport.GetOrganizationImpact")

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
            request: event_resources.GetOrganizationImpactRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> event_resources.OrganizationImpact:
            r"""Call the get organization impact method over HTTP.

            Args:
                request (~.event_resources.GetOrganizationImpactRequest):
                    The request object. Gets information about an event that
                affects a project under an organization.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.event_resources.OrganizationImpact:
                    Represents impact to assets at
                organizational level. It is a read-only
                view and does not allow any
                modifications.

            """

            http_options = _BaseServiceHealthRestTransport._BaseGetOrganizationImpact._get_http_options()
            request, metadata = self._interceptor.pre_get_organization_impact(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseServiceHealthRestTransport._BaseGetOrganizationImpact,
                    "_BaseGetOrganizationImpact__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.servicehealth_v1.ServiceHealthClient.GetOrganizationImpact",
                    extra={
                        "serviceName": "google.cloud.servicehealth.v1.ServiceHealth",
                        "rpcName": "GetOrganizationImpact",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ServiceHealthRestTransport._GetOrganizationImpact._get_response(
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
            resp = event_resources.OrganizationImpact()
            pb_resp = event_resources.OrganizationImpact.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_organization_impact(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_organization_impact_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = event_resources.OrganizationImpact.to_json(
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
                    "Received response for google.cloud.servicehealth_v1.ServiceHealthClient.get_organization_impact",
                    extra={
                        "serviceName": "google.cloud.servicehealth.v1.ServiceHealth",
                        "rpcName": "GetOrganizationImpact",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListEvents(
        _BaseServiceHealthRestTransport._BaseListEvents, ServiceHealthRestStub
    ):
        def __hash__(self):
            return hash("ServiceHealthRestTransport.ListEvents")

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
            request: event_resources.ListEventsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> event_resources.ListEventsResponse:
            r"""Call the list events method over HTTP.

            Args:
                request (~.event_resources.ListEventsRequest):
                    The request object. Requests list of events.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.event_resources.ListEventsResponse:
                    Response to request for listing
                events.

            """

            http_options = (
                _BaseServiceHealthRestTransport._BaseListEvents._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_events(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseServiceHealthRestTransport._BaseListEvents,
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
                    f"Sending request for google.cloud.servicehealth_v1.ServiceHealthClient.ListEvents",
                    extra={
                        "serviceName": "google.cloud.servicehealth.v1.ServiceHealth",
                        "rpcName": "ListEvents",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ServiceHealthRestTransport._ListEvents._get_response(
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
            resp = event_resources.ListEventsResponse()
            pb_resp = event_resources.ListEventsResponse.pb(resp)

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
                    response_payload = event_resources.ListEventsResponse.to_json(
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
                    "Received response for google.cloud.servicehealth_v1.ServiceHealthClient.list_events",
                    extra={
                        "serviceName": "google.cloud.servicehealth.v1.ServiceHealth",
                        "rpcName": "ListEvents",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListOrganizationEvents(
        _BaseServiceHealthRestTransport._BaseListOrganizationEvents,
        ServiceHealthRestStub,
    ):
        def __hash__(self):
            return hash("ServiceHealthRestTransport.ListOrganizationEvents")

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
            request: event_resources.ListOrganizationEventsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> event_resources.ListOrganizationEventsResponse:
            r"""Call the list organization events method over HTTP.

            Args:
                request (~.event_resources.ListOrganizationEventsRequest):
                    The request object. Requests list of events that affect
                an organization.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.event_resources.ListOrganizationEventsResponse:
                    Response to request for listing
                organization events.

            """

            http_options = _BaseServiceHealthRestTransport._BaseListOrganizationEvents._get_http_options()
            request, metadata = self._interceptor.pre_list_organization_events(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseServiceHealthRestTransport._BaseListOrganizationEvents,
                    "_BaseListOrganizationEvents__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.servicehealth_v1.ServiceHealthClient.ListOrganizationEvents",
                    extra={
                        "serviceName": "google.cloud.servicehealth.v1.ServiceHealth",
                        "rpcName": "ListOrganizationEvents",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ServiceHealthRestTransport._ListOrganizationEvents._get_response(
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
            resp = event_resources.ListOrganizationEventsResponse()
            pb_resp = event_resources.ListOrganizationEventsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_organization_events(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_organization_events_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        event_resources.ListOrganizationEventsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.servicehealth_v1.ServiceHealthClient.list_organization_events",
                    extra={
                        "serviceName": "google.cloud.servicehealth.v1.ServiceHealth",
                        "rpcName": "ListOrganizationEvents",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListOrganizationImpacts(
        _BaseServiceHealthRestTransport._BaseListOrganizationImpacts,
        ServiceHealthRestStub,
    ):
        def __hash__(self):
            return hash("ServiceHealthRestTransport.ListOrganizationImpacts")

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
            request: event_resources.ListOrganizationImpactsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> event_resources.ListOrganizationImpactsResponse:
            r"""Call the list organization impacts method over HTTP.

            Args:
                request (~.event_resources.ListOrganizationImpactsRequest):
                    The request object. Requests list of projects under an
                organization affected by an event.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.event_resources.ListOrganizationImpactsResponse:
                    Response to request for listing
                projects under an organization affected
                by an event.

            """

            http_options = _BaseServiceHealthRestTransport._BaseListOrganizationImpacts._get_http_options()
            request, metadata = self._interceptor.pre_list_organization_impacts(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseServiceHealthRestTransport._BaseListOrganizationImpacts,
                    "_BaseListOrganizationImpacts__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.servicehealth_v1.ServiceHealthClient.ListOrganizationImpacts",
                    extra={
                        "serviceName": "google.cloud.servicehealth.v1.ServiceHealth",
                        "rpcName": "ListOrganizationImpacts",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ServiceHealthRestTransport._ListOrganizationImpacts._get_response(
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
            resp = event_resources.ListOrganizationImpactsResponse()
            pb_resp = event_resources.ListOrganizationImpactsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_organization_impacts(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_organization_impacts_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        event_resources.ListOrganizationImpactsResponse.to_json(
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
                    "Received response for google.cloud.servicehealth_v1.ServiceHealthClient.list_organization_impacts",
                    extra={
                        "serviceName": "google.cloud.servicehealth.v1.ServiceHealth",
                        "rpcName": "ListOrganizationImpacts",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def get_event(
        self,
    ) -> Callable[[event_resources.GetEventRequest], event_resources.Event]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetEvent(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_organization_event(
        self,
    ) -> Callable[
        [event_resources.GetOrganizationEventRequest], event_resources.OrganizationEvent
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetOrganizationEvent(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_organization_impact(
        self,
    ) -> Callable[
        [event_resources.GetOrganizationImpactRequest],
        event_resources.OrganizationImpact,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetOrganizationImpact(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_events(
        self,
    ) -> Callable[
        [event_resources.ListEventsRequest], event_resources.ListEventsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListEvents(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_organization_events(
        self,
    ) -> Callable[
        [event_resources.ListOrganizationEventsRequest],
        event_resources.ListOrganizationEventsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListOrganizationEvents(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_organization_impacts(
        self,
    ) -> Callable[
        [event_resources.ListOrganizationImpactsRequest],
        event_resources.ListOrganizationImpactsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListOrganizationImpacts(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseServiceHealthRestTransport._BaseGetLocation, ServiceHealthRestStub
    ):
        def __hash__(self):
            return hash("ServiceHealthRestTransport.GetLocation")

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
                _BaseServiceHealthRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseServiceHealthRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.servicehealth_v1.ServiceHealthClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.servicehealth.v1.ServiceHealth",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ServiceHealthRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.servicehealth_v1.ServiceHealthAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.servicehealth.v1.ServiceHealth",
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
        _BaseServiceHealthRestTransport._BaseListLocations, ServiceHealthRestStub
    ):
        def __hash__(self):
            return hash("ServiceHealthRestTransport.ListLocations")

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

            http_options = (
                _BaseServiceHealthRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseServiceHealthRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.servicehealth_v1.ServiceHealthClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.servicehealth.v1.ServiceHealth",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ServiceHealthRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.servicehealth_v1.ServiceHealthAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.servicehealth.v1.ServiceHealth",
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


__all__ = ("ServiceHealthRestTransport",)
