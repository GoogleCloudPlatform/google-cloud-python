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

from google.apps.events_subscriptions_v1beta._compat import transcode_request
from google.apps.events_subscriptions_v1beta.types import (
    subscription_resource,
    subscriptions_service,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseSubscriptionsServiceRestTransport

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


class SubscriptionsServiceRestInterceptor:
    """Interceptor for SubscriptionsService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the SubscriptionsServiceRestTransport.

    .. code-block:: python
        class MyCustomSubscriptionsServiceInterceptor(SubscriptionsServiceRestInterceptor):
            def pre_create_subscription(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_subscription(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_subscription(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_subscription(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_subscription(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_subscription(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_subscriptions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_subscriptions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_reactivate_subscription(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_reactivate_subscription(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_subscription(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_subscription(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = SubscriptionsServiceRestTransport(interceptor=MyCustomSubscriptionsServiceInterceptor())
        client = SubscriptionsServiceClient(transport=transport)


    """

    def pre_create_subscription(
        self,
        request: subscriptions_service.CreateSubscriptionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        subscriptions_service.CreateSubscriptionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_subscription

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SubscriptionsService server.
        """
        return request, metadata

    def post_create_subscription(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_subscription

        DEPRECATED. Please use the `post_create_subscription_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SubscriptionsService server but before
        it is returned to user code. This `post_create_subscription` interceptor runs
        before the `post_create_subscription_with_metadata` interceptor.
        """
        return response

    def post_create_subscription_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_subscription

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SubscriptionsService server but before it is returned to user code.

        We recommend only using this `post_create_subscription_with_metadata`
        interceptor in new development instead of the `post_create_subscription` interceptor.
        When both interceptors are used, this `post_create_subscription_with_metadata` interceptor runs after the
        `post_create_subscription` interceptor. The (possibly modified) response returned by
        `post_create_subscription` will be passed to
        `post_create_subscription_with_metadata`.
        """
        return response, metadata

    def pre_delete_subscription(
        self,
        request: subscriptions_service.DeleteSubscriptionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        subscriptions_service.DeleteSubscriptionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_subscription

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SubscriptionsService server.
        """
        return request, metadata

    def post_delete_subscription(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_subscription

        DEPRECATED. Please use the `post_delete_subscription_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SubscriptionsService server but before
        it is returned to user code. This `post_delete_subscription` interceptor runs
        before the `post_delete_subscription_with_metadata` interceptor.
        """
        return response

    def post_delete_subscription_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_subscription

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SubscriptionsService server but before it is returned to user code.

        We recommend only using this `post_delete_subscription_with_metadata`
        interceptor in new development instead of the `post_delete_subscription` interceptor.
        When both interceptors are used, this `post_delete_subscription_with_metadata` interceptor runs after the
        `post_delete_subscription` interceptor. The (possibly modified) response returned by
        `post_delete_subscription` will be passed to
        `post_delete_subscription_with_metadata`.
        """
        return response, metadata

    def pre_get_subscription(
        self,
        request: subscriptions_service.GetSubscriptionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        subscriptions_service.GetSubscriptionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_subscription

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SubscriptionsService server.
        """
        return request, metadata

    def post_get_subscription(
        self, response: subscription_resource.Subscription
    ) -> subscription_resource.Subscription:
        """Post-rpc interceptor for get_subscription

        DEPRECATED. Please use the `post_get_subscription_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SubscriptionsService server but before
        it is returned to user code. This `post_get_subscription` interceptor runs
        before the `post_get_subscription_with_metadata` interceptor.
        """
        return response

    def post_get_subscription_with_metadata(
        self,
        response: subscription_resource.Subscription,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        subscription_resource.Subscription, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_subscription

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SubscriptionsService server but before it is returned to user code.

        We recommend only using this `post_get_subscription_with_metadata`
        interceptor in new development instead of the `post_get_subscription` interceptor.
        When both interceptors are used, this `post_get_subscription_with_metadata` interceptor runs after the
        `post_get_subscription` interceptor. The (possibly modified) response returned by
        `post_get_subscription` will be passed to
        `post_get_subscription_with_metadata`.
        """
        return response, metadata

    def pre_list_subscriptions(
        self,
        request: subscriptions_service.ListSubscriptionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        subscriptions_service.ListSubscriptionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_subscriptions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SubscriptionsService server.
        """
        return request, metadata

    def post_list_subscriptions(
        self, response: subscriptions_service.ListSubscriptionsResponse
    ) -> subscriptions_service.ListSubscriptionsResponse:
        """Post-rpc interceptor for list_subscriptions

        DEPRECATED. Please use the `post_list_subscriptions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SubscriptionsService server but before
        it is returned to user code. This `post_list_subscriptions` interceptor runs
        before the `post_list_subscriptions_with_metadata` interceptor.
        """
        return response

    def post_list_subscriptions_with_metadata(
        self,
        response: subscriptions_service.ListSubscriptionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        subscriptions_service.ListSubscriptionsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_subscriptions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SubscriptionsService server but before it is returned to user code.

        We recommend only using this `post_list_subscriptions_with_metadata`
        interceptor in new development instead of the `post_list_subscriptions` interceptor.
        When both interceptors are used, this `post_list_subscriptions_with_metadata` interceptor runs after the
        `post_list_subscriptions` interceptor. The (possibly modified) response returned by
        `post_list_subscriptions` will be passed to
        `post_list_subscriptions_with_metadata`.
        """
        return response, metadata

    def pre_reactivate_subscription(
        self,
        request: subscriptions_service.ReactivateSubscriptionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        subscriptions_service.ReactivateSubscriptionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for reactivate_subscription

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SubscriptionsService server.
        """
        return request, metadata

    def post_reactivate_subscription(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for reactivate_subscription

        DEPRECATED. Please use the `post_reactivate_subscription_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SubscriptionsService server but before
        it is returned to user code. This `post_reactivate_subscription` interceptor runs
        before the `post_reactivate_subscription_with_metadata` interceptor.
        """
        return response

    def post_reactivate_subscription_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for reactivate_subscription

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SubscriptionsService server but before it is returned to user code.

        We recommend only using this `post_reactivate_subscription_with_metadata`
        interceptor in new development instead of the `post_reactivate_subscription` interceptor.
        When both interceptors are used, this `post_reactivate_subscription_with_metadata` interceptor runs after the
        `post_reactivate_subscription` interceptor. The (possibly modified) response returned by
        `post_reactivate_subscription` will be passed to
        `post_reactivate_subscription_with_metadata`.
        """
        return response, metadata

    def pre_update_subscription(
        self,
        request: subscriptions_service.UpdateSubscriptionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        subscriptions_service.UpdateSubscriptionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_subscription

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SubscriptionsService server.
        """
        return request, metadata

    def post_update_subscription(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_subscription

        DEPRECATED. Please use the `post_update_subscription_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SubscriptionsService server but before
        it is returned to user code. This `post_update_subscription` interceptor runs
        before the `post_update_subscription_with_metadata` interceptor.
        """
        return response

    def post_update_subscription_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_subscription

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SubscriptionsService server but before it is returned to user code.

        We recommend only using this `post_update_subscription_with_metadata`
        interceptor in new development instead of the `post_update_subscription` interceptor.
        When both interceptors are used, this `post_update_subscription_with_metadata` interceptor runs after the
        `post_update_subscription` interceptor. The (possibly modified) response returned by
        `post_update_subscription` will be passed to
        `post_update_subscription_with_metadata`.
        """
        return response, metadata

    def pre_get_operation(
        self,
        request: operations_pb2.GetOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.GetOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SubscriptionsService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the SubscriptionsService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class SubscriptionsServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: SubscriptionsServiceRestInterceptor


class SubscriptionsServiceRestTransport(_BaseSubscriptionsServiceRestTransport):
    """REST backend synchronous transport for SubscriptionsService.

    A service that manages subscriptions to Google Workspace
    events.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "workspaceevents.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[SubscriptionsServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'workspaceevents.googleapis.com').
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
            interceptor (Optional[SubscriptionsServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or SubscriptionsServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    @property
    def operations_client(self) -> operations_v1.AbstractOperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Only create a new client if we do not already have one.
        if self._operations_client is None:
            http_options: Dict[str, List[Dict[str, str]]] = {
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v1beta/{name=operations/**}",
                    },
                ],
            }

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

    class _CreateSubscription(
        _BaseSubscriptionsServiceRestTransport._BaseCreateSubscription,
        SubscriptionsServiceRestStub,
    ):
        def __hash__(self):
            return hash("SubscriptionsServiceRestTransport.CreateSubscription")

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
            request: subscriptions_service.CreateSubscriptionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create subscription method over HTTP.

            Args:
                request (~.subscriptions_service.CreateSubscriptionRequest):
                    The request object. The request message for
                [SubscriptionsService.CreateSubscription][google.apps.events.subscriptions.v1beta.SubscriptionsService.CreateSubscription].
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

            http_options = _BaseSubscriptionsServiceRestTransport._BaseCreateSubscription._get_http_options()
            request, metadata = self._interceptor.pre_create_subscription(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSubscriptionsServiceRestTransport._BaseCreateSubscription,
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
                    f"Sending request for google.apps.events.subscriptions_v1beta.SubscriptionsServiceClient.CreateSubscription",
                    extra={
                        "serviceName": "google.apps.events.subscriptions.v1beta.SubscriptionsService",
                        "rpcName": "CreateSubscription",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                SubscriptionsServiceRestTransport._CreateSubscription._get_response(
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

            resp = self._interceptor.post_create_subscription(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_subscription_with_metadata(
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
                    "Received response for google.apps.events.subscriptions_v1beta.SubscriptionsServiceClient.create_subscription",
                    extra={
                        "serviceName": "google.apps.events.subscriptions.v1beta.SubscriptionsService",
                        "rpcName": "CreateSubscription",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteSubscription(
        _BaseSubscriptionsServiceRestTransport._BaseDeleteSubscription,
        SubscriptionsServiceRestStub,
    ):
        def __hash__(self):
            return hash("SubscriptionsServiceRestTransport.DeleteSubscription")

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
            request: subscriptions_service.DeleteSubscriptionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete subscription method over HTTP.

            Args:
                request (~.subscriptions_service.DeleteSubscriptionRequest):
                    The request object. The request message for
                [SubscriptionsService.DeleteSubscription][google.apps.events.subscriptions.v1beta.SubscriptionsService.DeleteSubscription].
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

            http_options = _BaseSubscriptionsServiceRestTransport._BaseDeleteSubscription._get_http_options()
            request, metadata = self._interceptor.pre_delete_subscription(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSubscriptionsServiceRestTransport._BaseDeleteSubscription,
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
                    f"Sending request for google.apps.events.subscriptions_v1beta.SubscriptionsServiceClient.DeleteSubscription",
                    extra={
                        "serviceName": "google.apps.events.subscriptions.v1beta.SubscriptionsService",
                        "rpcName": "DeleteSubscription",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                SubscriptionsServiceRestTransport._DeleteSubscription._get_response(
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

            resp = self._interceptor.post_delete_subscription(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_subscription_with_metadata(
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
                    "Received response for google.apps.events.subscriptions_v1beta.SubscriptionsServiceClient.delete_subscription",
                    extra={
                        "serviceName": "google.apps.events.subscriptions.v1beta.SubscriptionsService",
                        "rpcName": "DeleteSubscription",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetSubscription(
        _BaseSubscriptionsServiceRestTransport._BaseGetSubscription,
        SubscriptionsServiceRestStub,
    ):
        def __hash__(self):
            return hash("SubscriptionsServiceRestTransport.GetSubscription")

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
            request: subscriptions_service.GetSubscriptionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> subscription_resource.Subscription:
            r"""Call the get subscription method over HTTP.

            Args:
                request (~.subscriptions_service.GetSubscriptionRequest):
                    The request object. The request message for
                [SubscriptionsService.GetSubscription][google.apps.events.subscriptions.v1beta.SubscriptionsService.GetSubscription].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.subscription_resource.Subscription:
                    A subscription to receive events about a Google
                Workspace resource. To learn more about subscriptions,
                see the `Google Workspace Events API
                overview <https://developers.google.com/workspace/events>`__.

            """

            http_options = _BaseSubscriptionsServiceRestTransport._BaseGetSubscription._get_http_options()
            request, metadata = self._interceptor.pre_get_subscription(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSubscriptionsServiceRestTransport._BaseGetSubscription,
                    "_BaseGetSubscription__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.apps.events.subscriptions_v1beta.SubscriptionsServiceClient.GetSubscription",
                    extra={
                        "serviceName": "google.apps.events.subscriptions.v1beta.SubscriptionsService",
                        "rpcName": "GetSubscription",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SubscriptionsServiceRestTransport._GetSubscription._get_response(
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
            resp = subscription_resource.Subscription()
            pb_resp = subscription_resource.Subscription.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_subscription(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_subscription_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = subscription_resource.Subscription.to_json(
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
                    "Received response for google.apps.events.subscriptions_v1beta.SubscriptionsServiceClient.get_subscription",
                    extra={
                        "serviceName": "google.apps.events.subscriptions.v1beta.SubscriptionsService",
                        "rpcName": "GetSubscription",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListSubscriptions(
        _BaseSubscriptionsServiceRestTransport._BaseListSubscriptions,
        SubscriptionsServiceRestStub,
    ):
        def __hash__(self):
            return hash("SubscriptionsServiceRestTransport.ListSubscriptions")

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
            request: subscriptions_service.ListSubscriptionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> subscriptions_service.ListSubscriptionsResponse:
            r"""Call the list subscriptions method over HTTP.

            Args:
                request (~.subscriptions_service.ListSubscriptionsRequest):
                    The request object. The request message for
                [SubscriptionsService.ListSubscriptions][google.apps.events.subscriptions.v1beta.SubscriptionsService.ListSubscriptions].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.subscriptions_service.ListSubscriptionsResponse:
                    The response message for
                [SubscriptionsService.ListSubscriptions][google.apps.events.subscriptions.v1beta.SubscriptionsService.ListSubscriptions].

            """

            http_options = _BaseSubscriptionsServiceRestTransport._BaseListSubscriptions._get_http_options()
            request, metadata = self._interceptor.pre_list_subscriptions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSubscriptionsServiceRestTransport._BaseListSubscriptions,
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
                    f"Sending request for google.apps.events.subscriptions_v1beta.SubscriptionsServiceClient.ListSubscriptions",
                    extra={
                        "serviceName": "google.apps.events.subscriptions.v1beta.SubscriptionsService",
                        "rpcName": "ListSubscriptions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                SubscriptionsServiceRestTransport._ListSubscriptions._get_response(
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
            resp = subscriptions_service.ListSubscriptionsResponse()
            pb_resp = subscriptions_service.ListSubscriptionsResponse.pb(resp)

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
                        subscriptions_service.ListSubscriptionsResponse.to_json(
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
                    "Received response for google.apps.events.subscriptions_v1beta.SubscriptionsServiceClient.list_subscriptions",
                    extra={
                        "serviceName": "google.apps.events.subscriptions.v1beta.SubscriptionsService",
                        "rpcName": "ListSubscriptions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ReactivateSubscription(
        _BaseSubscriptionsServiceRestTransport._BaseReactivateSubscription,
        SubscriptionsServiceRestStub,
    ):
        def __hash__(self):
            return hash("SubscriptionsServiceRestTransport.ReactivateSubscription")

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
            request: subscriptions_service.ReactivateSubscriptionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the reactivate subscription method over HTTP.

            Args:
                request (~.subscriptions_service.ReactivateSubscriptionRequest):
                    The request object. The request message for
                [SubscriptionsService.ReactivateSubscription][google.apps.events.subscriptions.v1beta.SubscriptionsService.ReactivateSubscription].
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

            http_options = _BaseSubscriptionsServiceRestTransport._BaseReactivateSubscription._get_http_options()
            request, metadata = self._interceptor.pre_reactivate_subscription(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSubscriptionsServiceRestTransport._BaseReactivateSubscription,
                    "_BaseReactivateSubscription__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.apps.events.subscriptions_v1beta.SubscriptionsServiceClient.ReactivateSubscription",
                    extra={
                        "serviceName": "google.apps.events.subscriptions.v1beta.SubscriptionsService",
                        "rpcName": "ReactivateSubscription",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                SubscriptionsServiceRestTransport._ReactivateSubscription._get_response(
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

            resp = self._interceptor.post_reactivate_subscription(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_reactivate_subscription_with_metadata(
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
                    "Received response for google.apps.events.subscriptions_v1beta.SubscriptionsServiceClient.reactivate_subscription",
                    extra={
                        "serviceName": "google.apps.events.subscriptions.v1beta.SubscriptionsService",
                        "rpcName": "ReactivateSubscription",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateSubscription(
        _BaseSubscriptionsServiceRestTransport._BaseUpdateSubscription,
        SubscriptionsServiceRestStub,
    ):
        def __hash__(self):
            return hash("SubscriptionsServiceRestTransport.UpdateSubscription")

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
            request: subscriptions_service.UpdateSubscriptionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update subscription method over HTTP.

            Args:
                request (~.subscriptions_service.UpdateSubscriptionRequest):
                    The request object. The request message for
                [SubscriptionsService.UpdateSubscription][google.apps.events.subscriptions.v1beta.SubscriptionsService.UpdateSubscription].
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

            http_options = _BaseSubscriptionsServiceRestTransport._BaseUpdateSubscription._get_http_options()
            request, metadata = self._interceptor.pre_update_subscription(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSubscriptionsServiceRestTransport._BaseUpdateSubscription,
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
                    f"Sending request for google.apps.events.subscriptions_v1beta.SubscriptionsServiceClient.UpdateSubscription",
                    extra={
                        "serviceName": "google.apps.events.subscriptions.v1beta.SubscriptionsService",
                        "rpcName": "UpdateSubscription",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                SubscriptionsServiceRestTransport._UpdateSubscription._get_response(
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

            resp = self._interceptor.post_update_subscription(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_subscription_with_metadata(
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
                    "Received response for google.apps.events.subscriptions_v1beta.SubscriptionsServiceClient.update_subscription",
                    extra={
                        "serviceName": "google.apps.events.subscriptions.v1beta.SubscriptionsService",
                        "rpcName": "UpdateSubscription",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_subscription(
        self,
    ) -> Callable[
        [subscriptions_service.CreateSubscriptionRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateSubscription(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_subscription(
        self,
    ) -> Callable[
        [subscriptions_service.DeleteSubscriptionRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteSubscription(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_subscription(
        self,
    ) -> Callable[
        [subscriptions_service.GetSubscriptionRequest],
        subscription_resource.Subscription,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSubscription(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_subscriptions(
        self,
    ) -> Callable[
        [subscriptions_service.ListSubscriptionsRequest],
        subscriptions_service.ListSubscriptionsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListSubscriptions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def reactivate_subscription(
        self,
    ) -> Callable[
        [subscriptions_service.ReactivateSubscriptionRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ReactivateSubscription(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_subscription(
        self,
    ) -> Callable[
        [subscriptions_service.UpdateSubscriptionRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateSubscription(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseSubscriptionsServiceRestTransport._BaseGetOperation,
        SubscriptionsServiceRestStub,
    ):
        def __hash__(self):
            return hash("SubscriptionsServiceRestTransport.GetOperation")

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

            http_options = _BaseSubscriptionsServiceRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSubscriptionsServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.apps.events.subscriptions_v1beta.SubscriptionsServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.apps.events.subscriptions.v1beta.SubscriptionsService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SubscriptionsServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.apps.events.subscriptions_v1beta.SubscriptionsServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.apps.events.subscriptions.v1beta.SubscriptionsService",
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


__all__ = ("SubscriptionsServiceRestTransport",)
