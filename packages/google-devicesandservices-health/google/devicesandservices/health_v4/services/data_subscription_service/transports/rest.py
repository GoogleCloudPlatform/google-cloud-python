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
from google.api_core import gapic_v1, operations_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.devicesandservices.health_v4._compat import transcode_request
from google.devicesandservices.health_v4.types import data_subscription_service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseDataSubscriptionServiceRestTransport

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


class DataSubscriptionServiceRestInterceptor:
    """Interceptor for DataSubscriptionService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the DataSubscriptionServiceRestTransport.

    .. code-block:: python
        class MyCustomDataSubscriptionServiceInterceptor(DataSubscriptionServiceRestInterceptor):
            def pre_create_subscriber(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_subscriber(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_subscription(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_subscription(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_subscriber(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_subscriber(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_subscription(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_list_subscribers(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_subscribers(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_subscriptions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_subscriptions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_subscriber(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_subscriber(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_subscription(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_subscription(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = DataSubscriptionServiceRestTransport(interceptor=MyCustomDataSubscriptionServiceInterceptor())
        client = DataSubscriptionServiceClient(transport=transport)


    """

    def pre_create_subscriber(
        self,
        request: data_subscription_service.CreateSubscriberRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_subscription_service.CreateSubscriberRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_subscriber

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataSubscriptionService server.
        """
        return request, metadata

    def post_create_subscriber(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_subscriber

        DEPRECATED. Please use the `post_create_subscriber_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataSubscriptionService server but before
        it is returned to user code. This `post_create_subscriber` interceptor runs
        before the `post_create_subscriber_with_metadata` interceptor.
        """
        return response

    def post_create_subscriber_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_subscriber

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataSubscriptionService server but before it is returned to user code.

        We recommend only using this `post_create_subscriber_with_metadata`
        interceptor in new development instead of the `post_create_subscriber` interceptor.
        When both interceptors are used, this `post_create_subscriber_with_metadata` interceptor runs after the
        `post_create_subscriber` interceptor. The (possibly modified) response returned by
        `post_create_subscriber` will be passed to
        `post_create_subscriber_with_metadata`.
        """
        return response, metadata

    def pre_create_subscription(
        self,
        request: data_subscription_service.CreateSubscriptionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_subscription_service.CreateSubscriptionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_subscription

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataSubscriptionService server.
        """
        return request, metadata

    def post_create_subscription(
        self, response: data_subscription_service.Subscription
    ) -> data_subscription_service.Subscription:
        """Post-rpc interceptor for create_subscription

        DEPRECATED. Please use the `post_create_subscription_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataSubscriptionService server but before
        it is returned to user code. This `post_create_subscription` interceptor runs
        before the `post_create_subscription_with_metadata` interceptor.
        """
        return response

    def post_create_subscription_with_metadata(
        self,
        response: data_subscription_service.Subscription,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_subscription_service.Subscription, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for create_subscription

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataSubscriptionService server but before it is returned to user code.

        We recommend only using this `post_create_subscription_with_metadata`
        interceptor in new development instead of the `post_create_subscription` interceptor.
        When both interceptors are used, this `post_create_subscription_with_metadata` interceptor runs after the
        `post_create_subscription` interceptor. The (possibly modified) response returned by
        `post_create_subscription` will be passed to
        `post_create_subscription_with_metadata`.
        """
        return response, metadata

    def pre_delete_subscriber(
        self,
        request: data_subscription_service.DeleteSubscriberRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_subscription_service.DeleteSubscriberRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_subscriber

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataSubscriptionService server.
        """
        return request, metadata

    def post_delete_subscriber(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_subscriber

        DEPRECATED. Please use the `post_delete_subscriber_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataSubscriptionService server but before
        it is returned to user code. This `post_delete_subscriber` interceptor runs
        before the `post_delete_subscriber_with_metadata` interceptor.
        """
        return response

    def post_delete_subscriber_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_subscriber

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataSubscriptionService server but before it is returned to user code.

        We recommend only using this `post_delete_subscriber_with_metadata`
        interceptor in new development instead of the `post_delete_subscriber` interceptor.
        When both interceptors are used, this `post_delete_subscriber_with_metadata` interceptor runs after the
        `post_delete_subscriber` interceptor. The (possibly modified) response returned by
        `post_delete_subscriber` will be passed to
        `post_delete_subscriber_with_metadata`.
        """
        return response, metadata

    def pre_delete_subscription(
        self,
        request: data_subscription_service.DeleteSubscriptionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_subscription_service.DeleteSubscriptionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_subscription

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataSubscriptionService server.
        """
        return request, metadata

    def pre_list_subscribers(
        self,
        request: data_subscription_service.ListSubscribersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_subscription_service.ListSubscribersRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_subscribers

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataSubscriptionService server.
        """
        return request, metadata

    def post_list_subscribers(
        self, response: data_subscription_service.ListSubscribersResponse
    ) -> data_subscription_service.ListSubscribersResponse:
        """Post-rpc interceptor for list_subscribers

        DEPRECATED. Please use the `post_list_subscribers_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataSubscriptionService server but before
        it is returned to user code. This `post_list_subscribers` interceptor runs
        before the `post_list_subscribers_with_metadata` interceptor.
        """
        return response

    def post_list_subscribers_with_metadata(
        self,
        response: data_subscription_service.ListSubscribersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_subscription_service.ListSubscribersResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_subscribers

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataSubscriptionService server but before it is returned to user code.

        We recommend only using this `post_list_subscribers_with_metadata`
        interceptor in new development instead of the `post_list_subscribers` interceptor.
        When both interceptors are used, this `post_list_subscribers_with_metadata` interceptor runs after the
        `post_list_subscribers` interceptor. The (possibly modified) response returned by
        `post_list_subscribers` will be passed to
        `post_list_subscribers_with_metadata`.
        """
        return response, metadata

    def pre_list_subscriptions(
        self,
        request: data_subscription_service.ListSubscriptionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_subscription_service.ListSubscriptionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_subscriptions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataSubscriptionService server.
        """
        return request, metadata

    def post_list_subscriptions(
        self, response: data_subscription_service.ListSubscriptionsResponse
    ) -> data_subscription_service.ListSubscriptionsResponse:
        """Post-rpc interceptor for list_subscriptions

        DEPRECATED. Please use the `post_list_subscriptions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataSubscriptionService server but before
        it is returned to user code. This `post_list_subscriptions` interceptor runs
        before the `post_list_subscriptions_with_metadata` interceptor.
        """
        return response

    def post_list_subscriptions_with_metadata(
        self,
        response: data_subscription_service.ListSubscriptionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_subscription_service.ListSubscriptionsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_subscriptions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataSubscriptionService server but before it is returned to user code.

        We recommend only using this `post_list_subscriptions_with_metadata`
        interceptor in new development instead of the `post_list_subscriptions` interceptor.
        When both interceptors are used, this `post_list_subscriptions_with_metadata` interceptor runs after the
        `post_list_subscriptions` interceptor. The (possibly modified) response returned by
        `post_list_subscriptions` will be passed to
        `post_list_subscriptions_with_metadata`.
        """
        return response, metadata

    def pre_update_subscriber(
        self,
        request: data_subscription_service.UpdateSubscriberRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_subscription_service.UpdateSubscriberRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_subscriber

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataSubscriptionService server.
        """
        return request, metadata

    def post_update_subscriber(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_subscriber

        DEPRECATED. Please use the `post_update_subscriber_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataSubscriptionService server but before
        it is returned to user code. This `post_update_subscriber` interceptor runs
        before the `post_update_subscriber_with_metadata` interceptor.
        """
        return response

    def post_update_subscriber_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_subscriber

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataSubscriptionService server but before it is returned to user code.

        We recommend only using this `post_update_subscriber_with_metadata`
        interceptor in new development instead of the `post_update_subscriber` interceptor.
        When both interceptors are used, this `post_update_subscriber_with_metadata` interceptor runs after the
        `post_update_subscriber` interceptor. The (possibly modified) response returned by
        `post_update_subscriber` will be passed to
        `post_update_subscriber_with_metadata`.
        """
        return response, metadata

    def pre_update_subscription(
        self,
        request: data_subscription_service.UpdateSubscriptionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_subscription_service.UpdateSubscriptionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_subscription

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataSubscriptionService server.
        """
        return request, metadata

    def post_update_subscription(
        self, response: data_subscription_service.Subscription
    ) -> data_subscription_service.Subscription:
        """Post-rpc interceptor for update_subscription

        DEPRECATED. Please use the `post_update_subscription_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataSubscriptionService server but before
        it is returned to user code. This `post_update_subscription` interceptor runs
        before the `post_update_subscription_with_metadata` interceptor.
        """
        return response

    def post_update_subscription_with_metadata(
        self,
        response: data_subscription_service.Subscription,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_subscription_service.Subscription, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for update_subscription

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataSubscriptionService server but before it is returned to user code.

        We recommend only using this `post_update_subscription_with_metadata`
        interceptor in new development instead of the `post_update_subscription` interceptor.
        When both interceptors are used, this `post_update_subscription_with_metadata` interceptor runs after the
        `post_update_subscription` interceptor. The (possibly modified) response returned by
        `post_update_subscription` will be passed to
        `post_update_subscription_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class DataSubscriptionServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: DataSubscriptionServiceRestInterceptor


class DataSubscriptionServiceRestTransport(_BaseDataSubscriptionServiceRestTransport):
    """REST backend synchronous transport for DataSubscriptionService.

    Data Subscription Service that allows clients (e.g., Fitbit
    3P applications, internal Fitbit Services) to manage their
    subscriber endpoints. This service provides CRUD APIs for
    subscribers,
    and also offers functionalities for subscriber verification and
    statistics.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "health.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[DataSubscriptionServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'health.googleapis.com').
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
            interceptor (Optional[DataSubscriptionServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or DataSubscriptionServiceRestInterceptor()
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
                path_prefix="v4",
            )

            self._operations_client = operations_v1.AbstractOperationsClient(
                transport=rest_transport
            )

        # Return the client from cache.
        return self._operations_client

    class _CreateSubscriber(
        _BaseDataSubscriptionServiceRestTransport._BaseCreateSubscriber,
        DataSubscriptionServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataSubscriptionServiceRestTransport.CreateSubscriber")

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
            request: data_subscription_service.CreateSubscriberRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create subscriber method over HTTP.

            Args:
                request (~.data_subscription_service.CreateSubscriberRequest):
                    The request object. -- Messages --
                Request message for CreateSubscriber.
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

            http_options = _BaseDataSubscriptionServiceRestTransport._BaseCreateSubscriber._get_http_options()
            request, metadata = self._interceptor.pre_create_subscriber(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataSubscriptionServiceRestTransport._BaseCreateSubscriber,
                    "_BaseCreateSubscriber__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devicesandservices.health_v4.DataSubscriptionServiceClient.CreateSubscriber",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.DataSubscriptionService",
                        "rpcName": "CreateSubscriber",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataSubscriptionServiceRestTransport._CreateSubscriber._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_subscriber(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_subscriber_with_metadata(
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
                    "Received response for google.devicesandservices.health_v4.DataSubscriptionServiceClient.create_subscriber",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.DataSubscriptionService",
                        "rpcName": "CreateSubscriber",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateSubscription(
        _BaseDataSubscriptionServiceRestTransport._BaseCreateSubscription,
        DataSubscriptionServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataSubscriptionServiceRestTransport.CreateSubscription")

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
            request: data_subscription_service.CreateSubscriptionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> data_subscription_service.Subscription:
            r"""Call the create subscription method over HTTP.

            Args:
                request (~.data_subscription_service.CreateSubscriptionRequest):
                    The request object. Request message for
                CreateSubscription.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.data_subscription_service.Subscription:
                    A subscription to a data collection
                for a specific user, to be delivered to
                a subscriber.

            """

            http_options = _BaseDataSubscriptionServiceRestTransport._BaseCreateSubscription._get_http_options()
            request, metadata = self._interceptor.pre_create_subscription(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataSubscriptionServiceRestTransport._BaseCreateSubscription,
                    "_BaseCreateSubscription__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devicesandservices.health_v4.DataSubscriptionServiceClient.CreateSubscription",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.DataSubscriptionService",
                        "rpcName": "CreateSubscription",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataSubscriptionServiceRestTransport._CreateSubscription._get_response(
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
            resp = data_subscription_service.Subscription()
            pb_resp = data_subscription_service.Subscription.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_subscription(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_subscription_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = data_subscription_service.Subscription.to_json(
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
                    "Received response for google.devicesandservices.health_v4.DataSubscriptionServiceClient.create_subscription",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.DataSubscriptionService",
                        "rpcName": "CreateSubscription",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteSubscriber(
        _BaseDataSubscriptionServiceRestTransport._BaseDeleteSubscriber,
        DataSubscriptionServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataSubscriptionServiceRestTransport.DeleteSubscriber")

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
            request: data_subscription_service.DeleteSubscriberRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete subscriber method over HTTP.

            Args:
                request (~.data_subscription_service.DeleteSubscriberRequest):
                    The request object. Request message for DeleteSubscriber.
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

            http_options = _BaseDataSubscriptionServiceRestTransport._BaseDeleteSubscriber._get_http_options()
            request, metadata = self._interceptor.pre_delete_subscriber(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataSubscriptionServiceRestTransport._BaseDeleteSubscriber,
                    "_BaseDeleteSubscriber__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devicesandservices.health_v4.DataSubscriptionServiceClient.DeleteSubscriber",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.DataSubscriptionService",
                        "rpcName": "DeleteSubscriber",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataSubscriptionServiceRestTransport._DeleteSubscriber._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_subscriber(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_subscriber_with_metadata(
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
                    "Received response for google.devicesandservices.health_v4.DataSubscriptionServiceClient.delete_subscriber",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.DataSubscriptionService",
                        "rpcName": "DeleteSubscriber",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteSubscription(
        _BaseDataSubscriptionServiceRestTransport._BaseDeleteSubscription,
        DataSubscriptionServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataSubscriptionServiceRestTransport.DeleteSubscription")

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
            request: data_subscription_service.DeleteSubscriptionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete subscription method over HTTP.

            Args:
                request (~.data_subscription_service.DeleteSubscriptionRequest):
                    The request object. Request message for
                DeleteSubscription.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseDataSubscriptionServiceRestTransport._BaseDeleteSubscription._get_http_options()
            request, metadata = self._interceptor.pre_delete_subscription(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataSubscriptionServiceRestTransport._BaseDeleteSubscription,
                    "_BaseDeleteSubscription__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devicesandservices.health_v4.DataSubscriptionServiceClient.DeleteSubscription",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.DataSubscriptionService",
                        "rpcName": "DeleteSubscription",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataSubscriptionServiceRestTransport._DeleteSubscription._get_response(
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

    class _ListSubscribers(
        _BaseDataSubscriptionServiceRestTransport._BaseListSubscribers,
        DataSubscriptionServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataSubscriptionServiceRestTransport.ListSubscribers")

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
            request: data_subscription_service.ListSubscribersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> data_subscription_service.ListSubscribersResponse:
            r"""Call the list subscribers method over HTTP.

            Args:
                request (~.data_subscription_service.ListSubscribersRequest):
                    The request object. Request message for ListSubscribers.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.data_subscription_service.ListSubscribersResponse:
                    Response message for ListSubscribers.
            """

            http_options = _BaseDataSubscriptionServiceRestTransport._BaseListSubscribers._get_http_options()
            request, metadata = self._interceptor.pre_list_subscribers(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataSubscriptionServiceRestTransport._BaseListSubscribers,
                    "_BaseListSubscribers__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devicesandservices.health_v4.DataSubscriptionServiceClient.ListSubscribers",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.DataSubscriptionService",
                        "rpcName": "ListSubscribers",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataSubscriptionServiceRestTransport._ListSubscribers._get_response(
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
            resp = data_subscription_service.ListSubscribersResponse()
            pb_resp = data_subscription_service.ListSubscribersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_subscribers(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_subscribers_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        data_subscription_service.ListSubscribersResponse.to_json(
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
                    "Received response for google.devicesandservices.health_v4.DataSubscriptionServiceClient.list_subscribers",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.DataSubscriptionService",
                        "rpcName": "ListSubscribers",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListSubscriptions(
        _BaseDataSubscriptionServiceRestTransport._BaseListSubscriptions,
        DataSubscriptionServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataSubscriptionServiceRestTransport.ListSubscriptions")

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
            request: data_subscription_service.ListSubscriptionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> data_subscription_service.ListSubscriptionsResponse:
            r"""Call the list subscriptions method over HTTP.

            Args:
                request (~.data_subscription_service.ListSubscriptionsRequest):
                    The request object. Request message for
                ListSubscriptions.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.data_subscription_service.ListSubscriptionsResponse:
                    Response message for
                ListSubscriptions.

            """

            http_options = _BaseDataSubscriptionServiceRestTransport._BaseListSubscriptions._get_http_options()
            request, metadata = self._interceptor.pre_list_subscriptions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataSubscriptionServiceRestTransport._BaseListSubscriptions,
                    "_BaseListSubscriptions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devicesandservices.health_v4.DataSubscriptionServiceClient.ListSubscriptions",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.DataSubscriptionService",
                        "rpcName": "ListSubscriptions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataSubscriptionServiceRestTransport._ListSubscriptions._get_response(
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
            resp = data_subscription_service.ListSubscriptionsResponse()
            pb_resp = data_subscription_service.ListSubscriptionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_subscriptions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_subscriptions_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        data_subscription_service.ListSubscriptionsResponse.to_json(
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
                    "Received response for google.devicesandservices.health_v4.DataSubscriptionServiceClient.list_subscriptions",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.DataSubscriptionService",
                        "rpcName": "ListSubscriptions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateSubscriber(
        _BaseDataSubscriptionServiceRestTransport._BaseUpdateSubscriber,
        DataSubscriptionServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataSubscriptionServiceRestTransport.UpdateSubscriber")

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
            request: data_subscription_service.UpdateSubscriberRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update subscriber method over HTTP.

            Args:
                request (~.data_subscription_service.UpdateSubscriberRequest):
                    The request object. Request message for UpdateSubscriber.
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

            http_options = _BaseDataSubscriptionServiceRestTransport._BaseUpdateSubscriber._get_http_options()
            request, metadata = self._interceptor.pre_update_subscriber(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataSubscriptionServiceRestTransport._BaseUpdateSubscriber,
                    "_BaseUpdateSubscriber__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devicesandservices.health_v4.DataSubscriptionServiceClient.UpdateSubscriber",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.DataSubscriptionService",
                        "rpcName": "UpdateSubscriber",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataSubscriptionServiceRestTransport._UpdateSubscriber._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_subscriber(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_subscriber_with_metadata(
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
                    "Received response for google.devicesandservices.health_v4.DataSubscriptionServiceClient.update_subscriber",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.DataSubscriptionService",
                        "rpcName": "UpdateSubscriber",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateSubscription(
        _BaseDataSubscriptionServiceRestTransport._BaseUpdateSubscription,
        DataSubscriptionServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataSubscriptionServiceRestTransport.UpdateSubscription")

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
            request: data_subscription_service.UpdateSubscriptionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> data_subscription_service.Subscription:
            r"""Call the update subscription method over HTTP.

            Args:
                request (~.data_subscription_service.UpdateSubscriptionRequest):
                    The request object. Request message for
                UpdateSubscription.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.data_subscription_service.Subscription:
                    A subscription to a data collection
                for a specific user, to be delivered to
                a subscriber.

            """

            http_options = _BaseDataSubscriptionServiceRestTransport._BaseUpdateSubscription._get_http_options()
            request, metadata = self._interceptor.pre_update_subscription(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataSubscriptionServiceRestTransport._BaseUpdateSubscription,
                    "_BaseUpdateSubscription__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devicesandservices.health_v4.DataSubscriptionServiceClient.UpdateSubscription",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.DataSubscriptionService",
                        "rpcName": "UpdateSubscription",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataSubscriptionServiceRestTransport._UpdateSubscription._get_response(
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
            resp = data_subscription_service.Subscription()
            pb_resp = data_subscription_service.Subscription.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_subscription(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_subscription_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = data_subscription_service.Subscription.to_json(
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
                    "Received response for google.devicesandservices.health_v4.DataSubscriptionServiceClient.update_subscription",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.DataSubscriptionService",
                        "rpcName": "UpdateSubscription",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_subscriber(
        self,
    ) -> Callable[
        [data_subscription_service.CreateSubscriberRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateSubscriber(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_subscription(
        self,
    ) -> Callable[
        [data_subscription_service.CreateSubscriptionRequest],
        data_subscription_service.Subscription,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateSubscription(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_subscriber(
        self,
    ) -> Callable[
        [data_subscription_service.DeleteSubscriberRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteSubscriber(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_subscription(
        self,
    ) -> Callable[
        [data_subscription_service.DeleteSubscriptionRequest], empty_pb2.Empty
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteSubscription(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_subscribers(
        self,
    ) -> Callable[
        [data_subscription_service.ListSubscribersRequest],
        data_subscription_service.ListSubscribersResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListSubscribers(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_subscriptions(
        self,
    ) -> Callable[
        [data_subscription_service.ListSubscriptionsRequest],
        data_subscription_service.ListSubscriptionsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListSubscriptions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_subscriber(
        self,
    ) -> Callable[
        [data_subscription_service.UpdateSubscriberRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateSubscriber(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_subscription(
        self,
    ) -> Callable[
        [data_subscription_service.UpdateSubscriptionRequest],
        data_subscription_service.Subscription,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateSubscription(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("DataSubscriptionServiceRestTransport",)
