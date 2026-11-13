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
from google.api_core import gapic_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.support_v2._compat import transcode_request
from google.cloud.support_v2.types import (
    support_event_subscription,
    support_event_subscription_service,
)
from google.cloud.support_v2.types import (
    support_event_subscription as gcs_support_event_subscription,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseSupportEventSubscriptionServiceRestTransport

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


class SupportEventSubscriptionServiceRestInterceptor:
    """Interceptor for SupportEventSubscriptionService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the SupportEventSubscriptionServiceRestTransport.

    .. code-block:: python
        class MyCustomSupportEventSubscriptionServiceInterceptor(SupportEventSubscriptionServiceRestInterceptor):
            def pre_create_support_event_subscription(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_support_event_subscription(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_support_event_subscription(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_support_event_subscription(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_expunge_support_event_subscription(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_support_event_subscription(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_support_event_subscription(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_support_event_subscriptions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_support_event_subscriptions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_undelete_support_event_subscription(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_undelete_support_event_subscription(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_support_event_subscription(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_support_event_subscription(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = SupportEventSubscriptionServiceRestTransport(interceptor=MyCustomSupportEventSubscriptionServiceInterceptor())
        client = SupportEventSubscriptionServiceClient(transport=transport)


    """

    def pre_create_support_event_subscription(
        self,
        request: support_event_subscription_service.CreateSupportEventSubscriptionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        support_event_subscription_service.CreateSupportEventSubscriptionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_support_event_subscription

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SupportEventSubscriptionService server.
        """
        return request, metadata

    def post_create_support_event_subscription(
        self, response: gcs_support_event_subscription.SupportEventSubscription
    ) -> gcs_support_event_subscription.SupportEventSubscription:
        """Post-rpc interceptor for create_support_event_subscription

        DEPRECATED. Please use the `post_create_support_event_subscription_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SupportEventSubscriptionService server but before
        it is returned to user code. This `post_create_support_event_subscription` interceptor runs
        before the `post_create_support_event_subscription_with_metadata` interceptor.
        """
        return response

    def post_create_support_event_subscription_with_metadata(
        self,
        response: gcs_support_event_subscription.SupportEventSubscription,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcs_support_event_subscription.SupportEventSubscription,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for create_support_event_subscription

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SupportEventSubscriptionService server but before it is returned to user code.

        We recommend only using this `post_create_support_event_subscription_with_metadata`
        interceptor in new development instead of the `post_create_support_event_subscription` interceptor.
        When both interceptors are used, this `post_create_support_event_subscription_with_metadata` interceptor runs after the
        `post_create_support_event_subscription` interceptor. The (possibly modified) response returned by
        `post_create_support_event_subscription` will be passed to
        `post_create_support_event_subscription_with_metadata`.
        """
        return response, metadata

    def pre_delete_support_event_subscription(
        self,
        request: support_event_subscription_service.DeleteSupportEventSubscriptionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        support_event_subscription_service.DeleteSupportEventSubscriptionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_support_event_subscription

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SupportEventSubscriptionService server.
        """
        return request, metadata

    def post_delete_support_event_subscription(
        self, response: support_event_subscription.SupportEventSubscription
    ) -> support_event_subscription.SupportEventSubscription:
        """Post-rpc interceptor for delete_support_event_subscription

        DEPRECATED. Please use the `post_delete_support_event_subscription_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SupportEventSubscriptionService server but before
        it is returned to user code. This `post_delete_support_event_subscription` interceptor runs
        before the `post_delete_support_event_subscription_with_metadata` interceptor.
        """
        return response

    def post_delete_support_event_subscription_with_metadata(
        self,
        response: support_event_subscription.SupportEventSubscription,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        support_event_subscription.SupportEventSubscription,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for delete_support_event_subscription

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SupportEventSubscriptionService server but before it is returned to user code.

        We recommend only using this `post_delete_support_event_subscription_with_metadata`
        interceptor in new development instead of the `post_delete_support_event_subscription` interceptor.
        When both interceptors are used, this `post_delete_support_event_subscription_with_metadata` interceptor runs after the
        `post_delete_support_event_subscription` interceptor. The (possibly modified) response returned by
        `post_delete_support_event_subscription` will be passed to
        `post_delete_support_event_subscription_with_metadata`.
        """
        return response, metadata

    def pre_expunge_support_event_subscription(
        self,
        request: support_event_subscription_service.ExpungeSupportEventSubscriptionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        support_event_subscription_service.ExpungeSupportEventSubscriptionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for expunge_support_event_subscription

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SupportEventSubscriptionService server.
        """
        return request, metadata

    def pre_get_support_event_subscription(
        self,
        request: support_event_subscription_service.GetSupportEventSubscriptionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        support_event_subscription_service.GetSupportEventSubscriptionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_support_event_subscription

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SupportEventSubscriptionService server.
        """
        return request, metadata

    def post_get_support_event_subscription(
        self, response: support_event_subscription.SupportEventSubscription
    ) -> support_event_subscription.SupportEventSubscription:
        """Post-rpc interceptor for get_support_event_subscription

        DEPRECATED. Please use the `post_get_support_event_subscription_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SupportEventSubscriptionService server but before
        it is returned to user code. This `post_get_support_event_subscription` interceptor runs
        before the `post_get_support_event_subscription_with_metadata` interceptor.
        """
        return response

    def post_get_support_event_subscription_with_metadata(
        self,
        response: support_event_subscription.SupportEventSubscription,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        support_event_subscription.SupportEventSubscription,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_support_event_subscription

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SupportEventSubscriptionService server but before it is returned to user code.

        We recommend only using this `post_get_support_event_subscription_with_metadata`
        interceptor in new development instead of the `post_get_support_event_subscription` interceptor.
        When both interceptors are used, this `post_get_support_event_subscription_with_metadata` interceptor runs after the
        `post_get_support_event_subscription` interceptor. The (possibly modified) response returned by
        `post_get_support_event_subscription` will be passed to
        `post_get_support_event_subscription_with_metadata`.
        """
        return response, metadata

    def pre_list_support_event_subscriptions(
        self,
        request: support_event_subscription_service.ListSupportEventSubscriptionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        support_event_subscription_service.ListSupportEventSubscriptionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_support_event_subscriptions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SupportEventSubscriptionService server.
        """
        return request, metadata

    def post_list_support_event_subscriptions(
        self,
        response: support_event_subscription_service.ListSupportEventSubscriptionsResponse,
    ) -> support_event_subscription_service.ListSupportEventSubscriptionsResponse:
        """Post-rpc interceptor for list_support_event_subscriptions

        DEPRECATED. Please use the `post_list_support_event_subscriptions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SupportEventSubscriptionService server but before
        it is returned to user code. This `post_list_support_event_subscriptions` interceptor runs
        before the `post_list_support_event_subscriptions_with_metadata` interceptor.
        """
        return response

    def post_list_support_event_subscriptions_with_metadata(
        self,
        response: support_event_subscription_service.ListSupportEventSubscriptionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        support_event_subscription_service.ListSupportEventSubscriptionsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_support_event_subscriptions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SupportEventSubscriptionService server but before it is returned to user code.

        We recommend only using this `post_list_support_event_subscriptions_with_metadata`
        interceptor in new development instead of the `post_list_support_event_subscriptions` interceptor.
        When both interceptors are used, this `post_list_support_event_subscriptions_with_metadata` interceptor runs after the
        `post_list_support_event_subscriptions` interceptor. The (possibly modified) response returned by
        `post_list_support_event_subscriptions` will be passed to
        `post_list_support_event_subscriptions_with_metadata`.
        """
        return response, metadata

    def pre_undelete_support_event_subscription(
        self,
        request: support_event_subscription_service.UndeleteSupportEventSubscriptionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        support_event_subscription_service.UndeleteSupportEventSubscriptionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for undelete_support_event_subscription

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SupportEventSubscriptionService server.
        """
        return request, metadata

    def post_undelete_support_event_subscription(
        self, response: support_event_subscription.SupportEventSubscription
    ) -> support_event_subscription.SupportEventSubscription:
        """Post-rpc interceptor for undelete_support_event_subscription

        DEPRECATED. Please use the `post_undelete_support_event_subscription_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SupportEventSubscriptionService server but before
        it is returned to user code. This `post_undelete_support_event_subscription` interceptor runs
        before the `post_undelete_support_event_subscription_with_metadata` interceptor.
        """
        return response

    def post_undelete_support_event_subscription_with_metadata(
        self,
        response: support_event_subscription.SupportEventSubscription,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        support_event_subscription.SupportEventSubscription,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for undelete_support_event_subscription

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SupportEventSubscriptionService server but before it is returned to user code.

        We recommend only using this `post_undelete_support_event_subscription_with_metadata`
        interceptor in new development instead of the `post_undelete_support_event_subscription` interceptor.
        When both interceptors are used, this `post_undelete_support_event_subscription_with_metadata` interceptor runs after the
        `post_undelete_support_event_subscription` interceptor. The (possibly modified) response returned by
        `post_undelete_support_event_subscription` will be passed to
        `post_undelete_support_event_subscription_with_metadata`.
        """
        return response, metadata

    def pre_update_support_event_subscription(
        self,
        request: support_event_subscription_service.UpdateSupportEventSubscriptionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        support_event_subscription_service.UpdateSupportEventSubscriptionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_support_event_subscription

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SupportEventSubscriptionService server.
        """
        return request, metadata

    def post_update_support_event_subscription(
        self, response: gcs_support_event_subscription.SupportEventSubscription
    ) -> gcs_support_event_subscription.SupportEventSubscription:
        """Post-rpc interceptor for update_support_event_subscription

        DEPRECATED. Please use the `post_update_support_event_subscription_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SupportEventSubscriptionService server but before
        it is returned to user code. This `post_update_support_event_subscription` interceptor runs
        before the `post_update_support_event_subscription_with_metadata` interceptor.
        """
        return response

    def post_update_support_event_subscription_with_metadata(
        self,
        response: gcs_support_event_subscription.SupportEventSubscription,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcs_support_event_subscription.SupportEventSubscription,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for update_support_event_subscription

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SupportEventSubscriptionService server but before it is returned to user code.

        We recommend only using this `post_update_support_event_subscription_with_metadata`
        interceptor in new development instead of the `post_update_support_event_subscription` interceptor.
        When both interceptors are used, this `post_update_support_event_subscription_with_metadata` interceptor runs after the
        `post_update_support_event_subscription` interceptor. The (possibly modified) response returned by
        `post_update_support_event_subscription` will be passed to
        `post_update_support_event_subscription_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class SupportEventSubscriptionServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: SupportEventSubscriptionServiceRestInterceptor


class SupportEventSubscriptionServiceRestTransport(
    _BaseSupportEventSubscriptionServiceRestTransport
):
    """REST backend synchronous transport for SupportEventSubscriptionService.

    Service for managing customer support event subscriptions.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "cloudsupport.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[SupportEventSubscriptionServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'cloudsupport.googleapis.com').
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
            interceptor (Optional[SupportEventSubscriptionServiceRestInterceptor]): Interceptor used
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
            interceptor or SupportEventSubscriptionServiceRestInterceptor()
        )
        self._prep_wrapped_messages(client_info)

    class _CreateSupportEventSubscription(
        _BaseSupportEventSubscriptionServiceRestTransport._BaseCreateSupportEventSubscription,
        SupportEventSubscriptionServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "SupportEventSubscriptionServiceRestTransport.CreateSupportEventSubscription"
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
            request: support_event_subscription_service.CreateSupportEventSubscriptionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcs_support_event_subscription.SupportEventSubscription:
            r"""Call the create support event
            subscription method over HTTP.

                Args:
                    request (~.support_event_subscription_service.CreateSupportEventSubscriptionRequest):
                        The request object. Request message for
                    CreateSupportEventSubscription.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.gcs_support_event_subscription.SupportEventSubscription:
                        A support event subscription.

                    You can also manage support event subscriptions using
                    other tools:

                    - ```gcloud support support-event-subscriptions`` </sdk/gcloud/reference/support/support-event-subscriptions>`__
                      (or
                      ```gcloud beta`` </sdk/gcloud/reference/beta/support/support-event-subscriptions>`__
                      for beta)
                    - `Terraform
                      ``google_cloud_support_support_event_subscription`` <https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_support_support_event_subscription>`__
                      (or `google-beta
                      provider <https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/cloud_support_support_event_subscription>`__
                      for beta)

            """

            http_options = _BaseSupportEventSubscriptionServiceRestTransport._BaseCreateSupportEventSubscription._get_http_options()
            request, metadata = self._interceptor.pre_create_support_event_subscription(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSupportEventSubscriptionServiceRestTransport._BaseCreateSupportEventSubscription,
                    "_BaseCreateSupportEventSubscription__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.support_v2.SupportEventSubscriptionServiceClient.CreateSupportEventSubscription",
                    extra={
                        "serviceName": "google.cloud.support.v2.SupportEventSubscriptionService",
                        "rpcName": "CreateSupportEventSubscription",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SupportEventSubscriptionServiceRestTransport._CreateSupportEventSubscription._get_response(
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
            resp = gcs_support_event_subscription.SupportEventSubscription()
            pb_resp = gcs_support_event_subscription.SupportEventSubscription.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_support_event_subscription(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_create_support_event_subscription_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        gcs_support_event_subscription.SupportEventSubscription.to_json(
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
                    "Received response for google.cloud.support_v2.SupportEventSubscriptionServiceClient.create_support_event_subscription",
                    extra={
                        "serviceName": "google.cloud.support.v2.SupportEventSubscriptionService",
                        "rpcName": "CreateSupportEventSubscription",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteSupportEventSubscription(
        _BaseSupportEventSubscriptionServiceRestTransport._BaseDeleteSupportEventSubscription,
        SupportEventSubscriptionServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "SupportEventSubscriptionServiceRestTransport.DeleteSupportEventSubscription"
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
            request: support_event_subscription_service.DeleteSupportEventSubscriptionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> support_event_subscription.SupportEventSubscription:
            r"""Call the delete support event
            subscription method over HTTP.

                Args:
                    request (~.support_event_subscription_service.DeleteSupportEventSubscriptionRequest):
                        The request object. Request message for
                    DeleteSupportEventSubscription.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.support_event_subscription.SupportEventSubscription:
                        A support event subscription.

                    You can also manage support event subscriptions using
                    other tools:

                    - ```gcloud support support-event-subscriptions`` </sdk/gcloud/reference/support/support-event-subscriptions>`__
                      (or
                      ```gcloud beta`` </sdk/gcloud/reference/beta/support/support-event-subscriptions>`__
                      for beta)
                    - `Terraform
                      ``google_cloud_support_support_event_subscription`` <https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_support_support_event_subscription>`__
                      (or `google-beta
                      provider <https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/cloud_support_support_event_subscription>`__
                      for beta)

            """

            http_options = _BaseSupportEventSubscriptionServiceRestTransport._BaseDeleteSupportEventSubscription._get_http_options()
            request, metadata = self._interceptor.pre_delete_support_event_subscription(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSupportEventSubscriptionServiceRestTransport._BaseDeleteSupportEventSubscription,
                    "_BaseDeleteSupportEventSubscription__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.support_v2.SupportEventSubscriptionServiceClient.DeleteSupportEventSubscription",
                    extra={
                        "serviceName": "google.cloud.support.v2.SupportEventSubscriptionService",
                        "rpcName": "DeleteSupportEventSubscription",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SupportEventSubscriptionServiceRestTransport._DeleteSupportEventSubscription._get_response(
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
            resp = support_event_subscription.SupportEventSubscription()
            pb_resp = support_event_subscription.SupportEventSubscription.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_support_event_subscription(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_delete_support_event_subscription_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        support_event_subscription.SupportEventSubscription.to_json(
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
                    "Received response for google.cloud.support_v2.SupportEventSubscriptionServiceClient.delete_support_event_subscription",
                    extra={
                        "serviceName": "google.cloud.support.v2.SupportEventSubscriptionService",
                        "rpcName": "DeleteSupportEventSubscription",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ExpungeSupportEventSubscription(
        _BaseSupportEventSubscriptionServiceRestTransport._BaseExpungeSupportEventSubscription,
        SupportEventSubscriptionServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "SupportEventSubscriptionServiceRestTransport.ExpungeSupportEventSubscription"
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
            request: support_event_subscription_service.ExpungeSupportEventSubscriptionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the expunge support event
            subscription method over HTTP.

                Args:
                    request (~.support_event_subscription_service.ExpungeSupportEventSubscriptionRequest):
                        The request object. Request message for
                    ExpungeSupportEventSubscription.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.
            """

            http_options = _BaseSupportEventSubscriptionServiceRestTransport._BaseExpungeSupportEventSubscription._get_http_options()
            request, metadata = (
                self._interceptor.pre_expunge_support_event_subscription(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSupportEventSubscriptionServiceRestTransport._BaseExpungeSupportEventSubscription,
                    "_BaseExpungeSupportEventSubscription__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.support_v2.SupportEventSubscriptionServiceClient.ExpungeSupportEventSubscription",
                    extra={
                        "serviceName": "google.cloud.support.v2.SupportEventSubscriptionService",
                        "rpcName": "ExpungeSupportEventSubscription",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SupportEventSubscriptionServiceRestTransport._ExpungeSupportEventSubscription._get_response(
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

    class _GetSupportEventSubscription(
        _BaseSupportEventSubscriptionServiceRestTransport._BaseGetSupportEventSubscription,
        SupportEventSubscriptionServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "SupportEventSubscriptionServiceRestTransport.GetSupportEventSubscription"
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
            request: support_event_subscription_service.GetSupportEventSubscriptionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> support_event_subscription.SupportEventSubscription:
            r"""Call the get support event
            subscription method over HTTP.

                Args:
                    request (~.support_event_subscription_service.GetSupportEventSubscriptionRequest):
                        The request object. Request message for
                    GetSupportEventSubscription.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.support_event_subscription.SupportEventSubscription:
                        A support event subscription.

                    You can also manage support event subscriptions using
                    other tools:

                    - ```gcloud support support-event-subscriptions`` </sdk/gcloud/reference/support/support-event-subscriptions>`__
                      (or
                      ```gcloud beta`` </sdk/gcloud/reference/beta/support/support-event-subscriptions>`__
                      for beta)
                    - `Terraform
                      ``google_cloud_support_support_event_subscription`` <https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_support_support_event_subscription>`__
                      (or `google-beta
                      provider <https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/cloud_support_support_event_subscription>`__
                      for beta)

            """

            http_options = _BaseSupportEventSubscriptionServiceRestTransport._BaseGetSupportEventSubscription._get_http_options()
            request, metadata = self._interceptor.pre_get_support_event_subscription(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSupportEventSubscriptionServiceRestTransport._BaseGetSupportEventSubscription,
                    "_BaseGetSupportEventSubscription__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.support_v2.SupportEventSubscriptionServiceClient.GetSupportEventSubscription",
                    extra={
                        "serviceName": "google.cloud.support.v2.SupportEventSubscriptionService",
                        "rpcName": "GetSupportEventSubscription",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SupportEventSubscriptionServiceRestTransport._GetSupportEventSubscription._get_response(
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
            resp = support_event_subscription.SupportEventSubscription()
            pb_resp = support_event_subscription.SupportEventSubscription.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_support_event_subscription(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_get_support_event_subscription_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        support_event_subscription.SupportEventSubscription.to_json(
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
                    "Received response for google.cloud.support_v2.SupportEventSubscriptionServiceClient.get_support_event_subscription",
                    extra={
                        "serviceName": "google.cloud.support.v2.SupportEventSubscriptionService",
                        "rpcName": "GetSupportEventSubscription",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListSupportEventSubscriptions(
        _BaseSupportEventSubscriptionServiceRestTransport._BaseListSupportEventSubscriptions,
        SupportEventSubscriptionServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "SupportEventSubscriptionServiceRestTransport.ListSupportEventSubscriptions"
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
            request: support_event_subscription_service.ListSupportEventSubscriptionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> support_event_subscription_service.ListSupportEventSubscriptionsResponse:
            r"""Call the list support event
            subscriptions method over HTTP.

                Args:
                    request (~.support_event_subscription_service.ListSupportEventSubscriptionsRequest):
                        The request object. Request message for
                    ListSupportEventSubscriptions.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.support_event_subscription_service.ListSupportEventSubscriptionsResponse:
                        Response message for
                    ListSupportEventSubscriptions.

            """

            http_options = _BaseSupportEventSubscriptionServiceRestTransport._BaseListSupportEventSubscriptions._get_http_options()
            request, metadata = self._interceptor.pre_list_support_event_subscriptions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSupportEventSubscriptionServiceRestTransport._BaseListSupportEventSubscriptions,
                    "_BaseListSupportEventSubscriptions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.support_v2.SupportEventSubscriptionServiceClient.ListSupportEventSubscriptions",
                    extra={
                        "serviceName": "google.cloud.support.v2.SupportEventSubscriptionService",
                        "rpcName": "ListSupportEventSubscriptions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SupportEventSubscriptionServiceRestTransport._ListSupportEventSubscriptions._get_response(
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
            resp = support_event_subscription_service.ListSupportEventSubscriptionsResponse()
            pb_resp = support_event_subscription_service.ListSupportEventSubscriptionsResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_support_event_subscriptions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_support_event_subscriptions_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = support_event_subscription_service.ListSupportEventSubscriptionsResponse.to_json(
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
                    "Received response for google.cloud.support_v2.SupportEventSubscriptionServiceClient.list_support_event_subscriptions",
                    extra={
                        "serviceName": "google.cloud.support.v2.SupportEventSubscriptionService",
                        "rpcName": "ListSupportEventSubscriptions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UndeleteSupportEventSubscription(
        _BaseSupportEventSubscriptionServiceRestTransport._BaseUndeleteSupportEventSubscription,
        SupportEventSubscriptionServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "SupportEventSubscriptionServiceRestTransport.UndeleteSupportEventSubscription"
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
            request: support_event_subscription_service.UndeleteSupportEventSubscriptionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> support_event_subscription.SupportEventSubscription:
            r"""Call the undelete support event
            subscription method over HTTP.

                Args:
                    request (~.support_event_subscription_service.UndeleteSupportEventSubscriptionRequest):
                        The request object. Request message for
                    UndeleteSupportEventSubscription.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.support_event_subscription.SupportEventSubscription:
                        A support event subscription.

                    You can also manage support event subscriptions using
                    other tools:

                    - ```gcloud support support-event-subscriptions`` </sdk/gcloud/reference/support/support-event-subscriptions>`__
                      (or
                      ```gcloud beta`` </sdk/gcloud/reference/beta/support/support-event-subscriptions>`__
                      for beta)
                    - `Terraform
                      ``google_cloud_support_support_event_subscription`` <https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_support_support_event_subscription>`__
                      (or `google-beta
                      provider <https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/cloud_support_support_event_subscription>`__
                      for beta)

            """

            http_options = _BaseSupportEventSubscriptionServiceRestTransport._BaseUndeleteSupportEventSubscription._get_http_options()
            request, metadata = (
                self._interceptor.pre_undelete_support_event_subscription(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSupportEventSubscriptionServiceRestTransport._BaseUndeleteSupportEventSubscription,
                    "_BaseUndeleteSupportEventSubscription__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.support_v2.SupportEventSubscriptionServiceClient.UndeleteSupportEventSubscription",
                    extra={
                        "serviceName": "google.cloud.support.v2.SupportEventSubscriptionService",
                        "rpcName": "UndeleteSupportEventSubscription",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SupportEventSubscriptionServiceRestTransport._UndeleteSupportEventSubscription._get_response(
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
            resp = support_event_subscription.SupportEventSubscription()
            pb_resp = support_event_subscription.SupportEventSubscription.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_undelete_support_event_subscription(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_undelete_support_event_subscription_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        support_event_subscription.SupportEventSubscription.to_json(
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
                    "Received response for google.cloud.support_v2.SupportEventSubscriptionServiceClient.undelete_support_event_subscription",
                    extra={
                        "serviceName": "google.cloud.support.v2.SupportEventSubscriptionService",
                        "rpcName": "UndeleteSupportEventSubscription",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateSupportEventSubscription(
        _BaseSupportEventSubscriptionServiceRestTransport._BaseUpdateSupportEventSubscription,
        SupportEventSubscriptionServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "SupportEventSubscriptionServiceRestTransport.UpdateSupportEventSubscription"
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
            request: support_event_subscription_service.UpdateSupportEventSubscriptionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcs_support_event_subscription.SupportEventSubscription:
            r"""Call the update support event
            subscription method over HTTP.

                Args:
                    request (~.support_event_subscription_service.UpdateSupportEventSubscriptionRequest):
                        The request object. Request message for
                    UpdateSupportEventSubscription.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.gcs_support_event_subscription.SupportEventSubscription:
                        A support event subscription.

                    You can also manage support event subscriptions using
                    other tools:

                    - ```gcloud support support-event-subscriptions`` </sdk/gcloud/reference/support/support-event-subscriptions>`__
                      (or
                      ```gcloud beta`` </sdk/gcloud/reference/beta/support/support-event-subscriptions>`__
                      for beta)
                    - `Terraform
                      ``google_cloud_support_support_event_subscription`` <https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_support_support_event_subscription>`__
                      (or `google-beta
                      provider <https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/cloud_support_support_event_subscription>`__
                      for beta)

            """

            http_options = _BaseSupportEventSubscriptionServiceRestTransport._BaseUpdateSupportEventSubscription._get_http_options()
            request, metadata = self._interceptor.pre_update_support_event_subscription(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSupportEventSubscriptionServiceRestTransport._BaseUpdateSupportEventSubscription,
                    "_BaseUpdateSupportEventSubscription__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.support_v2.SupportEventSubscriptionServiceClient.UpdateSupportEventSubscription",
                    extra={
                        "serviceName": "google.cloud.support.v2.SupportEventSubscriptionService",
                        "rpcName": "UpdateSupportEventSubscription",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SupportEventSubscriptionServiceRestTransport._UpdateSupportEventSubscription._get_response(
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
            resp = gcs_support_event_subscription.SupportEventSubscription()
            pb_resp = gcs_support_event_subscription.SupportEventSubscription.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_support_event_subscription(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_update_support_event_subscription_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        gcs_support_event_subscription.SupportEventSubscription.to_json(
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
                    "Received response for google.cloud.support_v2.SupportEventSubscriptionServiceClient.update_support_event_subscription",
                    extra={
                        "serviceName": "google.cloud.support.v2.SupportEventSubscriptionService",
                        "rpcName": "UpdateSupportEventSubscription",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_support_event_subscription(
        self,
    ) -> Callable[
        [support_event_subscription_service.CreateSupportEventSubscriptionRequest],
        gcs_support_event_subscription.SupportEventSubscription,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateSupportEventSubscription(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_support_event_subscription(
        self,
    ) -> Callable[
        [support_event_subscription_service.DeleteSupportEventSubscriptionRequest],
        support_event_subscription.SupportEventSubscription,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteSupportEventSubscription(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def expunge_support_event_subscription(
        self,
    ) -> Callable[
        [support_event_subscription_service.ExpungeSupportEventSubscriptionRequest],
        empty_pb2.Empty,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExpungeSupportEventSubscription(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_support_event_subscription(
        self,
    ) -> Callable[
        [support_event_subscription_service.GetSupportEventSubscriptionRequest],
        support_event_subscription.SupportEventSubscription,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSupportEventSubscription(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_support_event_subscriptions(
        self,
    ) -> Callable[
        [support_event_subscription_service.ListSupportEventSubscriptionsRequest],
        support_event_subscription_service.ListSupportEventSubscriptionsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListSupportEventSubscriptions(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def undelete_support_event_subscription(
        self,
    ) -> Callable[
        [support_event_subscription_service.UndeleteSupportEventSubscriptionRequest],
        support_event_subscription.SupportEventSubscription,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UndeleteSupportEventSubscription(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_support_event_subscription(
        self,
    ) -> Callable[
        [support_event_subscription_service.UpdateSupportEventSubscriptionRequest],
        gcs_support_event_subscription.SupportEventSubscription,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateSupportEventSubscription(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("SupportEventSubscriptionServiceRestTransport",)
