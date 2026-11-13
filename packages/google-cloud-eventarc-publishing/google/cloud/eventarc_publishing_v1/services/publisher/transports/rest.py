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

from google.cloud.eventarc_publishing_v1._compat import transcode_request
from google.cloud.eventarc_publishing_v1.types import publisher

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BasePublisherRestTransport

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


class PublisherRestInterceptor:
    """Interceptor for Publisher.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the PublisherRestTransport.

    .. code-block:: python
        class MyCustomPublisherInterceptor(PublisherRestInterceptor):
            def pre_publish(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_publish(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_publish_channel_connection_events(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_publish_channel_connection_events(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_publish_events(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_publish_events(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = PublisherRestTransport(interceptor=MyCustomPublisherInterceptor())
        client = PublisherClient(transport=transport)


    """

    def pre_publish(
        self,
        request: publisher.PublishRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[publisher.PublishRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for publish

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Publisher server.
        """
        return request, metadata

    def post_publish(
        self, response: publisher.PublishResponse
    ) -> publisher.PublishResponse:
        """Post-rpc interceptor for publish

        DEPRECATED. Please use the `post_publish_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Publisher server but before
        it is returned to user code. This `post_publish` interceptor runs
        before the `post_publish_with_metadata` interceptor.
        """
        return response

    def post_publish_with_metadata(
        self,
        response: publisher.PublishResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[publisher.PublishResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for publish

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Publisher server but before it is returned to user code.

        We recommend only using this `post_publish_with_metadata`
        interceptor in new development instead of the `post_publish` interceptor.
        When both interceptors are used, this `post_publish_with_metadata` interceptor runs after the
        `post_publish` interceptor. The (possibly modified) response returned by
        `post_publish` will be passed to
        `post_publish_with_metadata`.
        """
        return response, metadata

    def pre_publish_channel_connection_events(
        self,
        request: publisher.PublishChannelConnectionEventsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        publisher.PublishChannelConnectionEventsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for publish_channel_connection_events

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Publisher server.
        """
        return request, metadata

    def post_publish_channel_connection_events(
        self, response: publisher.PublishChannelConnectionEventsResponse
    ) -> publisher.PublishChannelConnectionEventsResponse:
        """Post-rpc interceptor for publish_channel_connection_events

        DEPRECATED. Please use the `post_publish_channel_connection_events_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Publisher server but before
        it is returned to user code. This `post_publish_channel_connection_events` interceptor runs
        before the `post_publish_channel_connection_events_with_metadata` interceptor.
        """
        return response

    def post_publish_channel_connection_events_with_metadata(
        self,
        response: publisher.PublishChannelConnectionEventsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        publisher.PublishChannelConnectionEventsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for publish_channel_connection_events

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Publisher server but before it is returned to user code.

        We recommend only using this `post_publish_channel_connection_events_with_metadata`
        interceptor in new development instead of the `post_publish_channel_connection_events` interceptor.
        When both interceptors are used, this `post_publish_channel_connection_events_with_metadata` interceptor runs after the
        `post_publish_channel_connection_events` interceptor. The (possibly modified) response returned by
        `post_publish_channel_connection_events` will be passed to
        `post_publish_channel_connection_events_with_metadata`.
        """
        return response, metadata

    def pre_publish_events(
        self,
        request: publisher.PublishEventsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[publisher.PublishEventsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for publish_events

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Publisher server.
        """
        return request, metadata

    def post_publish_events(
        self, response: publisher.PublishEventsResponse
    ) -> publisher.PublishEventsResponse:
        """Post-rpc interceptor for publish_events

        DEPRECATED. Please use the `post_publish_events_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Publisher server but before
        it is returned to user code. This `post_publish_events` interceptor runs
        before the `post_publish_events_with_metadata` interceptor.
        """
        return response

    def post_publish_events_with_metadata(
        self,
        response: publisher.PublishEventsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        publisher.PublishEventsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for publish_events

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Publisher server but before it is returned to user code.

        We recommend only using this `post_publish_events_with_metadata`
        interceptor in new development instead of the `post_publish_events` interceptor.
        When both interceptors are used, this `post_publish_events_with_metadata` interceptor runs after the
        `post_publish_events` interceptor. The (possibly modified) response returned by
        `post_publish_events` will be passed to
        `post_publish_events_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class PublisherRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: PublisherRestInterceptor


class PublisherRestTransport(_BasePublisherRestTransport):
    """REST backend synchronous transport for Publisher.

    Eventarc processes events generated by an event provider and
    delivers them to a subscriber.

    An event provider is a software-as-a-service (SaaS) system or
    product that can generate and deliver events through Eventarc.

    A third-party event provider is an event provider from outside
    of Google.

    A partner is a third-party event provider that is integrated
    with Eventarc.

    A subscriber is a Google Cloud customer interested in receiving
    events.

    Channel is a first-class Eventarc resource that is created and
    managed by the subscriber in their Google Cloud project. A
    Channel represents a subscriber's intent to receive events from
    an event provider. A Channel is associated with exactly one
    event provider.

    ChannelConnection is a first-class Eventarc resource that is
    created and managed by the partner in their Google Cloud
    project. A ChannelConnection represents a connection between a
    partner and a subscriber's Channel. A ChannelConnection has a
    one-to-one mapping with a Channel.

    Bus is a first-class Eventarc resource that is created and
    managed in a Google Cloud project. A Bus provides a discoverable
    endpoint for events and is a router that receives all events
    published by event providers and delivers them to zero or more
    subscribers.

    Publisher allows an event provider to publish events to
    Eventarc.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "eventarcpublishing.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[PublisherRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'eventarcpublishing.googleapis.com').
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
            interceptor (Optional[PublisherRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or PublisherRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _Publish(_BasePublisherRestTransport._BasePublish, PublisherRestStub):
        def __hash__(self):
            return hash("PublisherRestTransport.Publish")

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
            request: publisher.PublishRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> publisher.PublishResponse:
            r"""Call the publish method over HTTP.

            Args:
                request (~.publisher.PublishRequest):
                    The request object. The request message for the Publish
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.publisher.PublishResponse:
                    The response message for the Publish
                method.

            """

            http_options = _BasePublisherRestTransport._BasePublish._get_http_options()
            request, metadata = self._interceptor.pre_publish(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePublisherRestTransport._BasePublish,
                    "_BasePublish__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.eventarc.publishing_v1.PublisherClient.Publish",
                    extra={
                        "serviceName": "google.cloud.eventarc.publishing.v1.Publisher",
                        "rpcName": "Publish",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PublisherRestTransport._Publish._get_response(
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
            resp = publisher.PublishResponse()
            pb_resp = publisher.PublishResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_publish(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_publish_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = publisher.PublishResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.eventarc.publishing_v1.PublisherClient.publish",
                    extra={
                        "serviceName": "google.cloud.eventarc.publishing.v1.Publisher",
                        "rpcName": "Publish",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _PublishChannelConnectionEvents(
        _BasePublisherRestTransport._BasePublishChannelConnectionEvents,
        PublisherRestStub,
    ):
        def __hash__(self):
            return hash("PublisherRestTransport.PublishChannelConnectionEvents")

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
            request: publisher.PublishChannelConnectionEventsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> publisher.PublishChannelConnectionEventsResponse:
            r"""Call the publish channel
            connection events method over HTTP.

                Args:
                    request (~.publisher.PublishChannelConnectionEventsRequest):
                        The request object. The request message for the
                    PublishChannelConnectionEvents method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.publisher.PublishChannelConnectionEventsResponse:
                        The response message for the
                    PublishChannelConnectionEvents method.

            """

            http_options = _BasePublisherRestTransport._BasePublishChannelConnectionEvents._get_http_options()
            request, metadata = self._interceptor.pre_publish_channel_connection_events(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePublisherRestTransport._BasePublishChannelConnectionEvents,
                    "_BasePublishChannelConnectionEvents__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.eventarc.publishing_v1.PublisherClient.PublishChannelConnectionEvents",
                    extra={
                        "serviceName": "google.cloud.eventarc.publishing.v1.Publisher",
                        "rpcName": "PublishChannelConnectionEvents",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                PublisherRestTransport._PublishChannelConnectionEvents._get_response(
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
            resp = publisher.PublishChannelConnectionEventsResponse()
            pb_resp = publisher.PublishChannelConnectionEventsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_publish_channel_connection_events(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_publish_channel_connection_events_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        publisher.PublishChannelConnectionEventsResponse.to_json(
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
                    "Received response for google.cloud.eventarc.publishing_v1.PublisherClient.publish_channel_connection_events",
                    extra={
                        "serviceName": "google.cloud.eventarc.publishing.v1.Publisher",
                        "rpcName": "PublishChannelConnectionEvents",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _PublishEvents(
        _BasePublisherRestTransport._BasePublishEvents, PublisherRestStub
    ):
        def __hash__(self):
            return hash("PublisherRestTransport.PublishEvents")

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
            request: publisher.PublishEventsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> publisher.PublishEventsResponse:
            r"""Call the publish events method over HTTP.

            Args:
                request (~.publisher.PublishEventsRequest):
                    The request object. The request message for the
                PublishEvents method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.publisher.PublishEventsResponse:
                    The response message for the
                PublishEvents method.

            """

            http_options = (
                _BasePublisherRestTransport._BasePublishEvents._get_http_options()
            )
            request, metadata = self._interceptor.pre_publish_events(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePublisherRestTransport._BasePublishEvents,
                    "_BasePublishEvents__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.eventarc.publishing_v1.PublisherClient.PublishEvents",
                    extra={
                        "serviceName": "google.cloud.eventarc.publishing.v1.Publisher",
                        "rpcName": "PublishEvents",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PublisherRestTransport._PublishEvents._get_response(
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
            resp = publisher.PublishEventsResponse()
            pb_resp = publisher.PublishEventsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_publish_events(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_publish_events_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = publisher.PublishEventsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.eventarc.publishing_v1.PublisherClient.publish_events",
                    extra={
                        "serviceName": "google.cloud.eventarc.publishing.v1.Publisher",
                        "rpcName": "PublishEvents",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def publish(
        self,
    ) -> Callable[[publisher.PublishRequest], publisher.PublishResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Publish(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def publish_channel_connection_events(
        self,
    ) -> Callable[
        [publisher.PublishChannelConnectionEventsRequest],
        publisher.PublishChannelConnectionEventsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._PublishChannelConnectionEvents(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def publish_events(
        self,
    ) -> Callable[[publisher.PublishEventsRequest], publisher.PublishEventsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._PublishEvents(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("PublisherRestTransport",)
