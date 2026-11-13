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
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.pubsub_v1._compat import transcode_request
from google.pubsub_v1.types import pubsub

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
            def pre_create_topic(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_topic(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_topic(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_detach_subscription(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_detach_subscription(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_topic(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_topic(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_topics(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_topics(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_topic_snapshots(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_topic_snapshots(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_topic_subscriptions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_topic_subscriptions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_publish(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_publish(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_topic(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_topic(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = PublisherRestTransport(interceptor=MyCustomPublisherInterceptor())
        client = PublisherClient(transport=transport)


    """

    def pre_create_topic(
        self, request: pubsub.Topic, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[pubsub.Topic, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_topic

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Publisher server.
        """
        return request, metadata

    def post_create_topic(self, response: pubsub.Topic) -> pubsub.Topic:
        """Post-rpc interceptor for create_topic

        DEPRECATED. Please use the `post_create_topic_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Publisher server but before
        it is returned to user code. This `post_create_topic` interceptor runs
        before the `post_create_topic_with_metadata` interceptor.
        """
        return response

    def post_create_topic_with_metadata(
        self, response: pubsub.Topic, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[pubsub.Topic, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_topic

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Publisher server but before it is returned to user code.

        We recommend only using this `post_create_topic_with_metadata`
        interceptor in new development instead of the `post_create_topic` interceptor.
        When both interceptors are used, this `post_create_topic_with_metadata` interceptor runs after the
        `post_create_topic` interceptor. The (possibly modified) response returned by
        `post_create_topic` will be passed to
        `post_create_topic_with_metadata`.
        """
        return response, metadata

    def pre_delete_topic(
        self,
        request: pubsub.DeleteTopicRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[pubsub.DeleteTopicRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_topic

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Publisher server.
        """
        return request, metadata

    def pre_detach_subscription(
        self,
        request: pubsub.DetachSubscriptionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        pubsub.DetachSubscriptionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for detach_subscription

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Publisher server.
        """
        return request, metadata

    def post_detach_subscription(
        self, response: pubsub.DetachSubscriptionResponse
    ) -> pubsub.DetachSubscriptionResponse:
        """Post-rpc interceptor for detach_subscription

        DEPRECATED. Please use the `post_detach_subscription_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Publisher server but before
        it is returned to user code. This `post_detach_subscription` interceptor runs
        before the `post_detach_subscription_with_metadata` interceptor.
        """
        return response

    def post_detach_subscription_with_metadata(
        self,
        response: pubsub.DetachSubscriptionResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        pubsub.DetachSubscriptionResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for detach_subscription

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Publisher server but before it is returned to user code.

        We recommend only using this `post_detach_subscription_with_metadata`
        interceptor in new development instead of the `post_detach_subscription` interceptor.
        When both interceptors are used, this `post_detach_subscription_with_metadata` interceptor runs after the
        `post_detach_subscription` interceptor. The (possibly modified) response returned by
        `post_detach_subscription` will be passed to
        `post_detach_subscription_with_metadata`.
        """
        return response, metadata

    def pre_get_topic(
        self,
        request: pubsub.GetTopicRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[pubsub.GetTopicRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_topic

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Publisher server.
        """
        return request, metadata

    def post_get_topic(self, response: pubsub.Topic) -> pubsub.Topic:
        """Post-rpc interceptor for get_topic

        DEPRECATED. Please use the `post_get_topic_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Publisher server but before
        it is returned to user code. This `post_get_topic` interceptor runs
        before the `post_get_topic_with_metadata` interceptor.
        """
        return response

    def post_get_topic_with_metadata(
        self, response: pubsub.Topic, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[pubsub.Topic, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_topic

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Publisher server but before it is returned to user code.

        We recommend only using this `post_get_topic_with_metadata`
        interceptor in new development instead of the `post_get_topic` interceptor.
        When both interceptors are used, this `post_get_topic_with_metadata` interceptor runs after the
        `post_get_topic` interceptor. The (possibly modified) response returned by
        `post_get_topic` will be passed to
        `post_get_topic_with_metadata`.
        """
        return response, metadata

    def pre_list_topics(
        self,
        request: pubsub.ListTopicsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[pubsub.ListTopicsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_topics

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Publisher server.
        """
        return request, metadata

    def post_list_topics(
        self, response: pubsub.ListTopicsResponse
    ) -> pubsub.ListTopicsResponse:
        """Post-rpc interceptor for list_topics

        DEPRECATED. Please use the `post_list_topics_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Publisher server but before
        it is returned to user code. This `post_list_topics` interceptor runs
        before the `post_list_topics_with_metadata` interceptor.
        """
        return response

    def post_list_topics_with_metadata(
        self,
        response: pubsub.ListTopicsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[pubsub.ListTopicsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_topics

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Publisher server but before it is returned to user code.

        We recommend only using this `post_list_topics_with_metadata`
        interceptor in new development instead of the `post_list_topics` interceptor.
        When both interceptors are used, this `post_list_topics_with_metadata` interceptor runs after the
        `post_list_topics` interceptor. The (possibly modified) response returned by
        `post_list_topics` will be passed to
        `post_list_topics_with_metadata`.
        """
        return response, metadata

    def pre_list_topic_snapshots(
        self,
        request: pubsub.ListTopicSnapshotsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        pubsub.ListTopicSnapshotsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_topic_snapshots

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Publisher server.
        """
        return request, metadata

    def post_list_topic_snapshots(
        self, response: pubsub.ListTopicSnapshotsResponse
    ) -> pubsub.ListTopicSnapshotsResponse:
        """Post-rpc interceptor for list_topic_snapshots

        DEPRECATED. Please use the `post_list_topic_snapshots_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Publisher server but before
        it is returned to user code. This `post_list_topic_snapshots` interceptor runs
        before the `post_list_topic_snapshots_with_metadata` interceptor.
        """
        return response

    def post_list_topic_snapshots_with_metadata(
        self,
        response: pubsub.ListTopicSnapshotsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        pubsub.ListTopicSnapshotsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_topic_snapshots

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Publisher server but before it is returned to user code.

        We recommend only using this `post_list_topic_snapshots_with_metadata`
        interceptor in new development instead of the `post_list_topic_snapshots` interceptor.
        When both interceptors are used, this `post_list_topic_snapshots_with_metadata` interceptor runs after the
        `post_list_topic_snapshots` interceptor. The (possibly modified) response returned by
        `post_list_topic_snapshots` will be passed to
        `post_list_topic_snapshots_with_metadata`.
        """
        return response, metadata

    def pre_list_topic_subscriptions(
        self,
        request: pubsub.ListTopicSubscriptionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        pubsub.ListTopicSubscriptionsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_topic_subscriptions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Publisher server.
        """
        return request, metadata

    def post_list_topic_subscriptions(
        self, response: pubsub.ListTopicSubscriptionsResponse
    ) -> pubsub.ListTopicSubscriptionsResponse:
        """Post-rpc interceptor for list_topic_subscriptions

        DEPRECATED. Please use the `post_list_topic_subscriptions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Publisher server but before
        it is returned to user code. This `post_list_topic_subscriptions` interceptor runs
        before the `post_list_topic_subscriptions_with_metadata` interceptor.
        """
        return response

    def post_list_topic_subscriptions_with_metadata(
        self,
        response: pubsub.ListTopicSubscriptionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        pubsub.ListTopicSubscriptionsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_topic_subscriptions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Publisher server but before it is returned to user code.

        We recommend only using this `post_list_topic_subscriptions_with_metadata`
        interceptor in new development instead of the `post_list_topic_subscriptions` interceptor.
        When both interceptors are used, this `post_list_topic_subscriptions_with_metadata` interceptor runs after the
        `post_list_topic_subscriptions` interceptor. The (possibly modified) response returned by
        `post_list_topic_subscriptions` will be passed to
        `post_list_topic_subscriptions_with_metadata`.
        """
        return response, metadata

    def pre_publish(
        self,
        request: pubsub.PublishRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[pubsub.PublishRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for publish

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Publisher server.
        """
        return request, metadata

    def post_publish(self, response: pubsub.PublishResponse) -> pubsub.PublishResponse:
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
        response: pubsub.PublishResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[pubsub.PublishResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
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

    def pre_update_topic(
        self,
        request: pubsub.UpdateTopicRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[pubsub.UpdateTopicRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_topic

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Publisher server.
        """
        return request, metadata

    def post_update_topic(self, response: pubsub.Topic) -> pubsub.Topic:
        """Post-rpc interceptor for update_topic

        DEPRECATED. Please use the `post_update_topic_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Publisher server but before
        it is returned to user code. This `post_update_topic` interceptor runs
        before the `post_update_topic_with_metadata` interceptor.
        """
        return response

    def post_update_topic_with_metadata(
        self, response: pubsub.Topic, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[pubsub.Topic, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_topic

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Publisher server but before it is returned to user code.

        We recommend only using this `post_update_topic_with_metadata`
        interceptor in new development instead of the `post_update_topic` interceptor.
        When both interceptors are used, this `post_update_topic_with_metadata` interceptor runs after the
        `post_update_topic` interceptor. The (possibly modified) response returned by
        `post_update_topic` will be passed to
        `post_update_topic_with_metadata`.
        """
        return response, metadata

    def pre_get_iam_policy(
        self,
        request: iam_policy_pb2.GetIamPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.GetIamPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Publisher server.
        """
        return request, metadata

    def post_get_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the Publisher server but before
        it is returned to user code.
        """
        return response

    def pre_set_iam_policy(
        self,
        request: iam_policy_pb2.SetIamPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.SetIamPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Publisher server.
        """
        return request, metadata

    def post_set_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the Publisher server but before
        it is returned to user code.
        """
        return response

    def pre_test_iam_permissions(
        self,
        request: iam_policy_pb2.TestIamPermissionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.TestIamPermissionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Publisher server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the response
        after it is returned by the Publisher server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class PublisherRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: PublisherRestInterceptor


class PublisherRestTransport(_BasePublisherRestTransport):
    """REST backend synchronous transport for Publisher.

    The service that an application uses to manipulate topics,
    and to send messages to a topic.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "pubsub.googleapis.com",
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
                 The hostname to connect to (default: 'pubsub.googleapis.com').
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

    class _CreateTopic(_BasePublisherRestTransport._BaseCreateTopic, PublisherRestStub):
        def __hash__(self):
            return hash("PublisherRestTransport.CreateTopic")

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
            request: pubsub.Topic,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> pubsub.Topic:
            r"""Call the create topic method over HTTP.

            Args:
                request (~.pubsub.Topic):
                    The request object. A topic resource.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.pubsub.Topic:
                    A topic resource.
            """

            http_options = (
                _BasePublisherRestTransport._BaseCreateTopic._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_topic(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePublisherRestTransport._BaseCreateTopic,
                    "_BaseCreateTopic__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.pubsub_v1.PublisherClient.CreateTopic",
                    extra={
                        "serviceName": "google.pubsub.v1.Publisher",
                        "rpcName": "CreateTopic",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PublisherRestTransport._CreateTopic._get_response(
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
            resp = pubsub.Topic()
            pb_resp = pubsub.Topic.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_topic(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_topic_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = pubsub.Topic.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.pubsub_v1.PublisherClient.create_topic",
                    extra={
                        "serviceName": "google.pubsub.v1.Publisher",
                        "rpcName": "CreateTopic",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteTopic(_BasePublisherRestTransport._BaseDeleteTopic, PublisherRestStub):
        def __hash__(self):
            return hash("PublisherRestTransport.DeleteTopic")

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
            request: pubsub.DeleteTopicRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete topic method over HTTP.

            Args:
                request (~.pubsub.DeleteTopicRequest):
                    The request object. Request for the ``DeleteTopic`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BasePublisherRestTransport._BaseDeleteTopic._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_topic(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePublisherRestTransport._BaseDeleteTopic,
                    "_BaseDeleteTopic__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.pubsub_v1.PublisherClient.DeleteTopic",
                    extra={
                        "serviceName": "google.pubsub.v1.Publisher",
                        "rpcName": "DeleteTopic",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PublisherRestTransport._DeleteTopic._get_response(
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

    class _DetachSubscription(
        _BasePublisherRestTransport._BaseDetachSubscription, PublisherRestStub
    ):
        def __hash__(self):
            return hash("PublisherRestTransport.DetachSubscription")

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
            request: pubsub.DetachSubscriptionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> pubsub.DetachSubscriptionResponse:
            r"""Call the detach subscription method over HTTP.

            Args:
                request (~.pubsub.DetachSubscriptionRequest):
                    The request object. Request for the DetachSubscription
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.pubsub.DetachSubscriptionResponse:
                    Response for the DetachSubscription
                method. Reserved for future use.

            """

            http_options = (
                _BasePublisherRestTransport._BaseDetachSubscription._get_http_options()
            )
            request, metadata = self._interceptor.pre_detach_subscription(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePublisherRestTransport._BaseDetachSubscription,
                    "_BaseDetachSubscription__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.pubsub_v1.PublisherClient.DetachSubscription",
                    extra={
                        "serviceName": "google.pubsub.v1.Publisher",
                        "rpcName": "DetachSubscription",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PublisherRestTransport._DetachSubscription._get_response(
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
            resp = pubsub.DetachSubscriptionResponse()
            pb_resp = pubsub.DetachSubscriptionResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_detach_subscription(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_detach_subscription_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = pubsub.DetachSubscriptionResponse.to_json(
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
                    "Received response for google.pubsub_v1.PublisherClient.detach_subscription",
                    extra={
                        "serviceName": "google.pubsub.v1.Publisher",
                        "rpcName": "DetachSubscription",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetTopic(_BasePublisherRestTransport._BaseGetTopic, PublisherRestStub):
        def __hash__(self):
            return hash("PublisherRestTransport.GetTopic")

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
            request: pubsub.GetTopicRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> pubsub.Topic:
            r"""Call the get topic method over HTTP.

            Args:
                request (~.pubsub.GetTopicRequest):
                    The request object. Request for the GetTopic method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.pubsub.Topic:
                    A topic resource.
            """

            http_options = _BasePublisherRestTransport._BaseGetTopic._get_http_options()
            request, metadata = self._interceptor.pre_get_topic(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePublisherRestTransport._BaseGetTopic,
                    "_BaseGetTopic__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.pubsub_v1.PublisherClient.GetTopic",
                    extra={
                        "serviceName": "google.pubsub.v1.Publisher",
                        "rpcName": "GetTopic",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PublisherRestTransport._GetTopic._get_response(
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
            resp = pubsub.Topic()
            pb_resp = pubsub.Topic.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_topic(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_topic_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = pubsub.Topic.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.pubsub_v1.PublisherClient.get_topic",
                    extra={
                        "serviceName": "google.pubsub.v1.Publisher",
                        "rpcName": "GetTopic",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListTopics(_BasePublisherRestTransport._BaseListTopics, PublisherRestStub):
        def __hash__(self):
            return hash("PublisherRestTransport.ListTopics")

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
            request: pubsub.ListTopicsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> pubsub.ListTopicsResponse:
            r"""Call the list topics method over HTTP.

            Args:
                request (~.pubsub.ListTopicsRequest):
                    The request object. Request for the ``ListTopics`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.pubsub.ListTopicsResponse:
                    Response for the ``ListTopics`` method.
            """

            http_options = (
                _BasePublisherRestTransport._BaseListTopics._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_topics(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePublisherRestTransport._BaseListTopics,
                    "_BaseListTopics__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.pubsub_v1.PublisherClient.ListTopics",
                    extra={
                        "serviceName": "google.pubsub.v1.Publisher",
                        "rpcName": "ListTopics",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PublisherRestTransport._ListTopics._get_response(
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
            resp = pubsub.ListTopicsResponse()
            pb_resp = pubsub.ListTopicsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_topics(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_topics_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = pubsub.ListTopicsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.pubsub_v1.PublisherClient.list_topics",
                    extra={
                        "serviceName": "google.pubsub.v1.Publisher",
                        "rpcName": "ListTopics",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListTopicSnapshots(
        _BasePublisherRestTransport._BaseListTopicSnapshots, PublisherRestStub
    ):
        def __hash__(self):
            return hash("PublisherRestTransport.ListTopicSnapshots")

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
            request: pubsub.ListTopicSnapshotsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> pubsub.ListTopicSnapshotsResponse:
            r"""Call the list topic snapshots method over HTTP.

            Args:
                request (~.pubsub.ListTopicSnapshotsRequest):
                    The request object. Request for the ``ListTopicSnapshots`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.pubsub.ListTopicSnapshotsResponse:
                    Response for the ``ListTopicSnapshots`` method.
            """

            http_options = (
                _BasePublisherRestTransport._BaseListTopicSnapshots._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_topic_snapshots(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePublisherRestTransport._BaseListTopicSnapshots,
                    "_BaseListTopicSnapshots__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.pubsub_v1.PublisherClient.ListTopicSnapshots",
                    extra={
                        "serviceName": "google.pubsub.v1.Publisher",
                        "rpcName": "ListTopicSnapshots",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PublisherRestTransport._ListTopicSnapshots._get_response(
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
            resp = pubsub.ListTopicSnapshotsResponse()
            pb_resp = pubsub.ListTopicSnapshotsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_topic_snapshots(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_topic_snapshots_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = pubsub.ListTopicSnapshotsResponse.to_json(
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
                    "Received response for google.pubsub_v1.PublisherClient.list_topic_snapshots",
                    extra={
                        "serviceName": "google.pubsub.v1.Publisher",
                        "rpcName": "ListTopicSnapshots",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListTopicSubscriptions(
        _BasePublisherRestTransport._BaseListTopicSubscriptions, PublisherRestStub
    ):
        def __hash__(self):
            return hash("PublisherRestTransport.ListTopicSubscriptions")

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
            request: pubsub.ListTopicSubscriptionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> pubsub.ListTopicSubscriptionsResponse:
            r"""Call the list topic subscriptions method over HTTP.

            Args:
                request (~.pubsub.ListTopicSubscriptionsRequest):
                    The request object. Request for the ``ListTopicSubscriptions`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.pubsub.ListTopicSubscriptionsResponse:
                    Response for the ``ListTopicSubscriptions`` method.
            """

            http_options = _BasePublisherRestTransport._BaseListTopicSubscriptions._get_http_options()
            request, metadata = self._interceptor.pre_list_topic_subscriptions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePublisherRestTransport._BaseListTopicSubscriptions,
                    "_BaseListTopicSubscriptions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.pubsub_v1.PublisherClient.ListTopicSubscriptions",
                    extra={
                        "serviceName": "google.pubsub.v1.Publisher",
                        "rpcName": "ListTopicSubscriptions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PublisherRestTransport._ListTopicSubscriptions._get_response(
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
            resp = pubsub.ListTopicSubscriptionsResponse()
            pb_resp = pubsub.ListTopicSubscriptionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_topic_subscriptions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_topic_subscriptions_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = pubsub.ListTopicSubscriptionsResponse.to_json(
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
                    "Received response for google.pubsub_v1.PublisherClient.list_topic_subscriptions",
                    extra={
                        "serviceName": "google.pubsub.v1.Publisher",
                        "rpcName": "ListTopicSubscriptions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

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
            request: pubsub.PublishRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> pubsub.PublishResponse:
            r"""Call the publish method over HTTP.

            Args:
                request (~.pubsub.PublishRequest):
                    The request object. Request for the Publish method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.pubsub.PublishResponse:
                    Response for the ``Publish`` method.
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
                    f"Sending request for google.pubsub_v1.PublisherClient.Publish",
                    extra={
                        "serviceName": "google.pubsub.v1.Publisher",
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
            resp = pubsub.PublishResponse()
            pb_resp = pubsub.PublishResponse.pb(resp)

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
                    response_payload = pubsub.PublishResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.pubsub_v1.PublisherClient.publish",
                    extra={
                        "serviceName": "google.pubsub.v1.Publisher",
                        "rpcName": "Publish",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateTopic(_BasePublisherRestTransport._BaseUpdateTopic, PublisherRestStub):
        def __hash__(self):
            return hash("PublisherRestTransport.UpdateTopic")

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
            request: pubsub.UpdateTopicRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> pubsub.Topic:
            r"""Call the update topic method over HTTP.

            Args:
                request (~.pubsub.UpdateTopicRequest):
                    The request object. Request for the UpdateTopic method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.pubsub.Topic:
                    A topic resource.
            """

            http_options = (
                _BasePublisherRestTransport._BaseUpdateTopic._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_topic(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePublisherRestTransport._BaseUpdateTopic,
                    "_BaseUpdateTopic__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.pubsub_v1.PublisherClient.UpdateTopic",
                    extra={
                        "serviceName": "google.pubsub.v1.Publisher",
                        "rpcName": "UpdateTopic",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PublisherRestTransport._UpdateTopic._get_response(
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
            resp = pubsub.Topic()
            pb_resp = pubsub.Topic.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_topic(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_topic_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = pubsub.Topic.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.pubsub_v1.PublisherClient.update_topic",
                    extra={
                        "serviceName": "google.pubsub.v1.Publisher",
                        "rpcName": "UpdateTopic",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_topic(self) -> Callable[[pubsub.Topic], pubsub.Topic]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateTopic(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_topic(self) -> Callable[[pubsub.DeleteTopicRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteTopic(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def detach_subscription(
        self,
    ) -> Callable[
        [pubsub.DetachSubscriptionRequest], pubsub.DetachSubscriptionResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DetachSubscription(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_topic(self) -> Callable[[pubsub.GetTopicRequest], pubsub.Topic]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetTopic(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_topics(
        self,
    ) -> Callable[[pubsub.ListTopicsRequest], pubsub.ListTopicsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListTopics(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_topic_snapshots(
        self,
    ) -> Callable[
        [pubsub.ListTopicSnapshotsRequest], pubsub.ListTopicSnapshotsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListTopicSnapshots(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_topic_subscriptions(
        self,
    ) -> Callable[
        [pubsub.ListTopicSubscriptionsRequest], pubsub.ListTopicSubscriptionsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListTopicSubscriptions(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def publish(self) -> Callable[[pubsub.PublishRequest], pubsub.PublishResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Publish(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_topic(self) -> Callable[[pubsub.UpdateTopicRequest], pubsub.Topic]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateTopic(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_iam_policy(self):
        return self._GetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    class _GetIamPolicy(
        _BasePublisherRestTransport._BaseGetIamPolicy, PublisherRestStub
    ):
        def __hash__(self):
            return hash("PublisherRestTransport.GetIamPolicy")

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
            request: iam_policy_pb2.GetIamPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> policy_pb2.Policy:
            r"""Call the get iam policy method over HTTP.

            Args:
                request (iam_policy_pb2.GetIamPolicyRequest):
                    The request object for GetIamPolicy method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                policy_pb2.Policy: Response from GetIamPolicy method.
            """

            http_options = (
                _BasePublisherRestTransport._BaseGetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePublisherRestTransport._BaseGetIamPolicy,
                    "_BaseGetIamPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.pubsub_v1.PublisherClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.pubsub.v1.Publisher",
                        "rpcName": "GetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PublisherRestTransport._GetIamPolicy._get_response(
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
            resp = policy_pb2.Policy()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_iam_policy(resp)
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
                    "Received response for google.pubsub_v1.PublisherAsyncClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.pubsub.v1.Publisher",
                        "rpcName": "GetIamPolicy",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def set_iam_policy(self):
        return self._SetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    class _SetIamPolicy(
        _BasePublisherRestTransport._BaseSetIamPolicy, PublisherRestStub
    ):
        def __hash__(self):
            return hash("PublisherRestTransport.SetIamPolicy")

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
            request: iam_policy_pb2.SetIamPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> policy_pb2.Policy:
            r"""Call the set iam policy method over HTTP.

            Args:
                request (iam_policy_pb2.SetIamPolicyRequest):
                    The request object for SetIamPolicy method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                policy_pb2.Policy: Response from SetIamPolicy method.
            """

            http_options = (
                _BasePublisherRestTransport._BaseSetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePublisherRestTransport._BaseSetIamPolicy,
                    "_BaseSetIamPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.pubsub_v1.PublisherClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.pubsub.v1.Publisher",
                        "rpcName": "SetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PublisherRestTransport._SetIamPolicy._get_response(
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

            content = response.content.decode("utf-8")
            resp = policy_pb2.Policy()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_set_iam_policy(resp)
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
                    "Received response for google.pubsub_v1.PublisherAsyncClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.pubsub.v1.Publisher",
                        "rpcName": "SetIamPolicy",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def test_iam_permissions(self):
        return self._TestIamPermissions(self._session, self._host, self._interceptor)  # type: ignore

    class _TestIamPermissions(
        _BasePublisherRestTransport._BaseTestIamPermissions, PublisherRestStub
    ):
        def __hash__(self):
            return hash("PublisherRestTransport.TestIamPermissions")

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
            request: iam_policy_pb2.TestIamPermissionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> iam_policy_pb2.TestIamPermissionsResponse:
            r"""Call the test iam permissions method over HTTP.

            Args:
                request (iam_policy_pb2.TestIamPermissionsRequest):
                    The request object for TestIamPermissions method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                iam_policy_pb2.TestIamPermissionsResponse: Response from TestIamPermissions method.
            """

            http_options = (
                _BasePublisherRestTransport._BaseTestIamPermissions._get_http_options()
            )
            request, metadata = self._interceptor.pre_test_iam_permissions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePublisherRestTransport._BaseTestIamPermissions,
                    "_BaseTestIamPermissions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.pubsub_v1.PublisherClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.pubsub.v1.Publisher",
                        "rpcName": "TestIamPermissions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PublisherRestTransport._TestIamPermissions._get_response(
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

            content = response.content.decode("utf-8")
            resp = iam_policy_pb2.TestIamPermissionsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_test_iam_permissions(resp)
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
                    "Received response for google.pubsub_v1.PublisherAsyncClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.pubsub.v1.Publisher",
                        "rpcName": "TestIamPermissions",
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


__all__ = ("PublisherRestTransport",)
