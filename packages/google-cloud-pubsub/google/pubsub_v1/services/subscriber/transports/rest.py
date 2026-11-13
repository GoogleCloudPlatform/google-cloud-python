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
from .rest_base import _BaseSubscriberRestTransport

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


class SubscriberRestInterceptor:
    """Interceptor for Subscriber.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the SubscriberRestTransport.

    .. code-block:: python
        class MyCustomSubscriberInterceptor(SubscriberRestInterceptor):
            def pre_acknowledge(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_create_snapshot(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_snapshot(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_subscription(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_subscription(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_snapshot(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_subscription(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_snapshot(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_snapshot(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_subscription(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_subscription(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_snapshots(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_snapshots(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_subscriptions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_subscriptions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_modify_ack_deadline(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_modify_push_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_pull(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_pull(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_seek(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_seek(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_snapshot(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_snapshot(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_subscription(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_subscription(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = SubscriberRestTransport(interceptor=MyCustomSubscriberInterceptor())
        client = SubscriberClient(transport=transport)


    """

    def pre_acknowledge(
        self,
        request: pubsub.AcknowledgeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[pubsub.AcknowledgeRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for acknowledge

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Subscriber server.
        """
        return request, metadata

    def pre_create_snapshot(
        self,
        request: pubsub.CreateSnapshotRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[pubsub.CreateSnapshotRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_snapshot

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Subscriber server.
        """
        return request, metadata

    def post_create_snapshot(self, response: pubsub.Snapshot) -> pubsub.Snapshot:
        """Post-rpc interceptor for create_snapshot

        DEPRECATED. Please use the `post_create_snapshot_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Subscriber server but before
        it is returned to user code. This `post_create_snapshot` interceptor runs
        before the `post_create_snapshot_with_metadata` interceptor.
        """
        return response

    def post_create_snapshot_with_metadata(
        self,
        response: pubsub.Snapshot,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[pubsub.Snapshot, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_snapshot

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Subscriber server but before it is returned to user code.

        We recommend only using this `post_create_snapshot_with_metadata`
        interceptor in new development instead of the `post_create_snapshot` interceptor.
        When both interceptors are used, this `post_create_snapshot_with_metadata` interceptor runs after the
        `post_create_snapshot` interceptor. The (possibly modified) response returned by
        `post_create_snapshot` will be passed to
        `post_create_snapshot_with_metadata`.
        """
        return response, metadata

    def pre_create_subscription(
        self,
        request: pubsub.Subscription,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[pubsub.Subscription, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_subscription

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Subscriber server.
        """
        return request, metadata

    def post_create_subscription(
        self, response: pubsub.Subscription
    ) -> pubsub.Subscription:
        """Post-rpc interceptor for create_subscription

        DEPRECATED. Please use the `post_create_subscription_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Subscriber server but before
        it is returned to user code. This `post_create_subscription` interceptor runs
        before the `post_create_subscription_with_metadata` interceptor.
        """
        return response

    def post_create_subscription_with_metadata(
        self,
        response: pubsub.Subscription,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[pubsub.Subscription, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_subscription

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Subscriber server but before it is returned to user code.

        We recommend only using this `post_create_subscription_with_metadata`
        interceptor in new development instead of the `post_create_subscription` interceptor.
        When both interceptors are used, this `post_create_subscription_with_metadata` interceptor runs after the
        `post_create_subscription` interceptor. The (possibly modified) response returned by
        `post_create_subscription` will be passed to
        `post_create_subscription_with_metadata`.
        """
        return response, metadata

    def pre_delete_snapshot(
        self,
        request: pubsub.DeleteSnapshotRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[pubsub.DeleteSnapshotRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_snapshot

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Subscriber server.
        """
        return request, metadata

    def pre_delete_subscription(
        self,
        request: pubsub.DeleteSubscriptionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        pubsub.DeleteSubscriptionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_subscription

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Subscriber server.
        """
        return request, metadata

    def pre_get_snapshot(
        self,
        request: pubsub.GetSnapshotRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[pubsub.GetSnapshotRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_snapshot

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Subscriber server.
        """
        return request, metadata

    def post_get_snapshot(self, response: pubsub.Snapshot) -> pubsub.Snapshot:
        """Post-rpc interceptor for get_snapshot

        DEPRECATED. Please use the `post_get_snapshot_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Subscriber server but before
        it is returned to user code. This `post_get_snapshot` interceptor runs
        before the `post_get_snapshot_with_metadata` interceptor.
        """
        return response

    def post_get_snapshot_with_metadata(
        self,
        response: pubsub.Snapshot,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[pubsub.Snapshot, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_snapshot

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Subscriber server but before it is returned to user code.

        We recommend only using this `post_get_snapshot_with_metadata`
        interceptor in new development instead of the `post_get_snapshot` interceptor.
        When both interceptors are used, this `post_get_snapshot_with_metadata` interceptor runs after the
        `post_get_snapshot` interceptor. The (possibly modified) response returned by
        `post_get_snapshot` will be passed to
        `post_get_snapshot_with_metadata`.
        """
        return response, metadata

    def pre_get_subscription(
        self,
        request: pubsub.GetSubscriptionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[pubsub.GetSubscriptionRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_subscription

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Subscriber server.
        """
        return request, metadata

    def post_get_subscription(
        self, response: pubsub.Subscription
    ) -> pubsub.Subscription:
        """Post-rpc interceptor for get_subscription

        DEPRECATED. Please use the `post_get_subscription_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Subscriber server but before
        it is returned to user code. This `post_get_subscription` interceptor runs
        before the `post_get_subscription_with_metadata` interceptor.
        """
        return response

    def post_get_subscription_with_metadata(
        self,
        response: pubsub.Subscription,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[pubsub.Subscription, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_subscription

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Subscriber server but before it is returned to user code.

        We recommend only using this `post_get_subscription_with_metadata`
        interceptor in new development instead of the `post_get_subscription` interceptor.
        When both interceptors are used, this `post_get_subscription_with_metadata` interceptor runs after the
        `post_get_subscription` interceptor. The (possibly modified) response returned by
        `post_get_subscription` will be passed to
        `post_get_subscription_with_metadata`.
        """
        return response, metadata

    def pre_list_snapshots(
        self,
        request: pubsub.ListSnapshotsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[pubsub.ListSnapshotsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_snapshots

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Subscriber server.
        """
        return request, metadata

    def post_list_snapshots(
        self, response: pubsub.ListSnapshotsResponse
    ) -> pubsub.ListSnapshotsResponse:
        """Post-rpc interceptor for list_snapshots

        DEPRECATED. Please use the `post_list_snapshots_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Subscriber server but before
        it is returned to user code. This `post_list_snapshots` interceptor runs
        before the `post_list_snapshots_with_metadata` interceptor.
        """
        return response

    def post_list_snapshots_with_metadata(
        self,
        response: pubsub.ListSnapshotsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[pubsub.ListSnapshotsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_snapshots

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Subscriber server but before it is returned to user code.

        We recommend only using this `post_list_snapshots_with_metadata`
        interceptor in new development instead of the `post_list_snapshots` interceptor.
        When both interceptors are used, this `post_list_snapshots_with_metadata` interceptor runs after the
        `post_list_snapshots` interceptor. The (possibly modified) response returned by
        `post_list_snapshots` will be passed to
        `post_list_snapshots_with_metadata`.
        """
        return response, metadata

    def pre_list_subscriptions(
        self,
        request: pubsub.ListSubscriptionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        pubsub.ListSubscriptionsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_subscriptions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Subscriber server.
        """
        return request, metadata

    def post_list_subscriptions(
        self, response: pubsub.ListSubscriptionsResponse
    ) -> pubsub.ListSubscriptionsResponse:
        """Post-rpc interceptor for list_subscriptions

        DEPRECATED. Please use the `post_list_subscriptions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Subscriber server but before
        it is returned to user code. This `post_list_subscriptions` interceptor runs
        before the `post_list_subscriptions_with_metadata` interceptor.
        """
        return response

    def post_list_subscriptions_with_metadata(
        self,
        response: pubsub.ListSubscriptionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        pubsub.ListSubscriptionsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_subscriptions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Subscriber server but before it is returned to user code.

        We recommend only using this `post_list_subscriptions_with_metadata`
        interceptor in new development instead of the `post_list_subscriptions` interceptor.
        When both interceptors are used, this `post_list_subscriptions_with_metadata` interceptor runs after the
        `post_list_subscriptions` interceptor. The (possibly modified) response returned by
        `post_list_subscriptions` will be passed to
        `post_list_subscriptions_with_metadata`.
        """
        return response, metadata

    def pre_modify_ack_deadline(
        self,
        request: pubsub.ModifyAckDeadlineRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        pubsub.ModifyAckDeadlineRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for modify_ack_deadline

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Subscriber server.
        """
        return request, metadata

    def pre_modify_push_config(
        self,
        request: pubsub.ModifyPushConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[pubsub.ModifyPushConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for modify_push_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Subscriber server.
        """
        return request, metadata

    def pre_pull(
        self,
        request: pubsub.PullRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[pubsub.PullRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for pull

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Subscriber server.
        """
        return request, metadata

    def post_pull(self, response: pubsub.PullResponse) -> pubsub.PullResponse:
        """Post-rpc interceptor for pull

        DEPRECATED. Please use the `post_pull_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Subscriber server but before
        it is returned to user code. This `post_pull` interceptor runs
        before the `post_pull_with_metadata` interceptor.
        """
        return response

    def post_pull_with_metadata(
        self,
        response: pubsub.PullResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[pubsub.PullResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for pull

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Subscriber server but before it is returned to user code.

        We recommend only using this `post_pull_with_metadata`
        interceptor in new development instead of the `post_pull` interceptor.
        When both interceptors are used, this `post_pull_with_metadata` interceptor runs after the
        `post_pull` interceptor. The (possibly modified) response returned by
        `post_pull` will be passed to
        `post_pull_with_metadata`.
        """
        return response, metadata

    def pre_seek(
        self,
        request: pubsub.SeekRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[pubsub.SeekRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for seek

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Subscriber server.
        """
        return request, metadata

    def post_seek(self, response: pubsub.SeekResponse) -> pubsub.SeekResponse:
        """Post-rpc interceptor for seek

        DEPRECATED. Please use the `post_seek_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Subscriber server but before
        it is returned to user code. This `post_seek` interceptor runs
        before the `post_seek_with_metadata` interceptor.
        """
        return response

    def post_seek_with_metadata(
        self,
        response: pubsub.SeekResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[pubsub.SeekResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for seek

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Subscriber server but before it is returned to user code.

        We recommend only using this `post_seek_with_metadata`
        interceptor in new development instead of the `post_seek` interceptor.
        When both interceptors are used, this `post_seek_with_metadata` interceptor runs after the
        `post_seek` interceptor. The (possibly modified) response returned by
        `post_seek` will be passed to
        `post_seek_with_metadata`.
        """
        return response, metadata

    def pre_update_snapshot(
        self,
        request: pubsub.UpdateSnapshotRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[pubsub.UpdateSnapshotRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_snapshot

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Subscriber server.
        """
        return request, metadata

    def post_update_snapshot(self, response: pubsub.Snapshot) -> pubsub.Snapshot:
        """Post-rpc interceptor for update_snapshot

        DEPRECATED. Please use the `post_update_snapshot_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Subscriber server but before
        it is returned to user code. This `post_update_snapshot` interceptor runs
        before the `post_update_snapshot_with_metadata` interceptor.
        """
        return response

    def post_update_snapshot_with_metadata(
        self,
        response: pubsub.Snapshot,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[pubsub.Snapshot, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_snapshot

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Subscriber server but before it is returned to user code.

        We recommend only using this `post_update_snapshot_with_metadata`
        interceptor in new development instead of the `post_update_snapshot` interceptor.
        When both interceptors are used, this `post_update_snapshot_with_metadata` interceptor runs after the
        `post_update_snapshot` interceptor. The (possibly modified) response returned by
        `post_update_snapshot` will be passed to
        `post_update_snapshot_with_metadata`.
        """
        return response, metadata

    def pre_update_subscription(
        self,
        request: pubsub.UpdateSubscriptionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        pubsub.UpdateSubscriptionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_subscription

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Subscriber server.
        """
        return request, metadata

    def post_update_subscription(
        self, response: pubsub.Subscription
    ) -> pubsub.Subscription:
        """Post-rpc interceptor for update_subscription

        DEPRECATED. Please use the `post_update_subscription_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Subscriber server but before
        it is returned to user code. This `post_update_subscription` interceptor runs
        before the `post_update_subscription_with_metadata` interceptor.
        """
        return response

    def post_update_subscription_with_metadata(
        self,
        response: pubsub.Subscription,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[pubsub.Subscription, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_subscription

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Subscriber server but before it is returned to user code.

        We recommend only using this `post_update_subscription_with_metadata`
        interceptor in new development instead of the `post_update_subscription` interceptor.
        When both interceptors are used, this `post_update_subscription_with_metadata` interceptor runs after the
        `post_update_subscription` interceptor. The (possibly modified) response returned by
        `post_update_subscription` will be passed to
        `post_update_subscription_with_metadata`.
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
        before they are sent to the Subscriber server.
        """
        return request, metadata

    def post_get_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the Subscriber server but before
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
        before they are sent to the Subscriber server.
        """
        return request, metadata

    def post_set_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the Subscriber server but before
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
        before they are sent to the Subscriber server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the response
        after it is returned by the Subscriber server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class SubscriberRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: SubscriberRestInterceptor


class SubscriberRestTransport(_BaseSubscriberRestTransport):
    """REST backend synchronous transport for Subscriber.

    The service that an application uses to manipulate subscriptions and
    to consume messages from a subscription via the ``Pull`` method or
    by establishing a bi-directional stream using the ``StreamingPull``
    method.

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
        interceptor: Optional[SubscriberRestInterceptor] = None,
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
            interceptor (Optional[SubscriberRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or SubscriberRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _Acknowledge(
        _BaseSubscriberRestTransport._BaseAcknowledge, SubscriberRestStub
    ):
        def __hash__(self):
            return hash("SubscriberRestTransport.Acknowledge")

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
            request: pubsub.AcknowledgeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the acknowledge method over HTTP.

            Args:
                request (~.pubsub.AcknowledgeRequest):
                    The request object. Request for the Acknowledge method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseSubscriberRestTransport._BaseAcknowledge._get_http_options()
            )
            request, metadata = self._interceptor.pre_acknowledge(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSubscriberRestTransport._BaseAcknowledge,
                    "_BaseAcknowledge__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.pubsub_v1.SubscriberClient.Acknowledge",
                    extra={
                        "serviceName": "google.pubsub.v1.Subscriber",
                        "rpcName": "Acknowledge",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SubscriberRestTransport._Acknowledge._get_response(
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

    class _CreateSnapshot(
        _BaseSubscriberRestTransport._BaseCreateSnapshot, SubscriberRestStub
    ):
        def __hash__(self):
            return hash("SubscriberRestTransport.CreateSnapshot")

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
            request: pubsub.CreateSnapshotRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> pubsub.Snapshot:
            r"""Call the create snapshot method over HTTP.

            Args:
                request (~.pubsub.CreateSnapshotRequest):
                    The request object. Request for the ``CreateSnapshot`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.pubsub.Snapshot:
                    A snapshot resource. Snapshots are used in
                `Seek <https://cloud.google.com/pubsub/docs/replay-overview>`__
                operations, which allow you to manage message
                acknowledgments in bulk. That is, you can set the
                acknowledgment state of messages in an existing
                subscription to the state captured by a snapshot.

            """

            http_options = (
                _BaseSubscriberRestTransport._BaseCreateSnapshot._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_snapshot(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSubscriberRestTransport._BaseCreateSnapshot,
                    "_BaseCreateSnapshot__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.pubsub_v1.SubscriberClient.CreateSnapshot",
                    extra={
                        "serviceName": "google.pubsub.v1.Subscriber",
                        "rpcName": "CreateSnapshot",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SubscriberRestTransport._CreateSnapshot._get_response(
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
            resp = pubsub.Snapshot()
            pb_resp = pubsub.Snapshot.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_snapshot(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_snapshot_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = pubsub.Snapshot.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.pubsub_v1.SubscriberClient.create_snapshot",
                    extra={
                        "serviceName": "google.pubsub.v1.Subscriber",
                        "rpcName": "CreateSnapshot",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateSubscription(
        _BaseSubscriberRestTransport._BaseCreateSubscription, SubscriberRestStub
    ):
        def __hash__(self):
            return hash("SubscriberRestTransport.CreateSubscription")

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
            request: pubsub.Subscription,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> pubsub.Subscription:
            r"""Call the create subscription method over HTTP.

            Args:
                request (~.pubsub.Subscription):
                    The request object. A subscription resource. If none of ``push_config``,
                ``bigquery_config``, ``cloud_storage_config``, or
                ``bigtable_config`` is set, then the subscriber will
                pull and ack messages using API methods. At most one of
                these fields may be set.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.pubsub.Subscription:
                    A subscription resource. If none of ``push_config``,
                ``bigquery_config``, ``cloud_storage_config``, or
                ``bigtable_config`` is set, then the subscriber will
                pull and ack messages using API methods. At most one of
                these fields may be set.

            """

            http_options = (
                _BaseSubscriberRestTransport._BaseCreateSubscription._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_subscription(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSubscriberRestTransport._BaseCreateSubscription,
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
                    f"Sending request for google.pubsub_v1.SubscriberClient.CreateSubscription",
                    extra={
                        "serviceName": "google.pubsub.v1.Subscriber",
                        "rpcName": "CreateSubscription",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SubscriberRestTransport._CreateSubscription._get_response(
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
            resp = pubsub.Subscription()
            pb_resp = pubsub.Subscription.pb(resp)

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
                    response_payload = pubsub.Subscription.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.pubsub_v1.SubscriberClient.create_subscription",
                    extra={
                        "serviceName": "google.pubsub.v1.Subscriber",
                        "rpcName": "CreateSubscription",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteSnapshot(
        _BaseSubscriberRestTransport._BaseDeleteSnapshot, SubscriberRestStub
    ):
        def __hash__(self):
            return hash("SubscriberRestTransport.DeleteSnapshot")

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
            request: pubsub.DeleteSnapshotRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete snapshot method over HTTP.

            Args:
                request (~.pubsub.DeleteSnapshotRequest):
                    The request object. Request for the ``DeleteSnapshot`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseSubscriberRestTransport._BaseDeleteSnapshot._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_snapshot(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSubscriberRestTransport._BaseDeleteSnapshot,
                    "_BaseDeleteSnapshot__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.pubsub_v1.SubscriberClient.DeleteSnapshot",
                    extra={
                        "serviceName": "google.pubsub.v1.Subscriber",
                        "rpcName": "DeleteSnapshot",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SubscriberRestTransport._DeleteSnapshot._get_response(
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

    class _DeleteSubscription(
        _BaseSubscriberRestTransport._BaseDeleteSubscription, SubscriberRestStub
    ):
        def __hash__(self):
            return hash("SubscriberRestTransport.DeleteSubscription")

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
            request: pubsub.DeleteSubscriptionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete subscription method over HTTP.

            Args:
                request (~.pubsub.DeleteSubscriptionRequest):
                    The request object. Request for the DeleteSubscription
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseSubscriberRestTransport._BaseDeleteSubscription._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_subscription(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSubscriberRestTransport._BaseDeleteSubscription,
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
                    f"Sending request for google.pubsub_v1.SubscriberClient.DeleteSubscription",
                    extra={
                        "serviceName": "google.pubsub.v1.Subscriber",
                        "rpcName": "DeleteSubscription",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SubscriberRestTransport._DeleteSubscription._get_response(
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

    class _GetSnapshot(
        _BaseSubscriberRestTransport._BaseGetSnapshot, SubscriberRestStub
    ):
        def __hash__(self):
            return hash("SubscriberRestTransport.GetSnapshot")

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
            request: pubsub.GetSnapshotRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> pubsub.Snapshot:
            r"""Call the get snapshot method over HTTP.

            Args:
                request (~.pubsub.GetSnapshotRequest):
                    The request object. Request for the GetSnapshot method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.pubsub.Snapshot:
                    A snapshot resource. Snapshots are used in
                `Seek <https://cloud.google.com/pubsub/docs/replay-overview>`__
                operations, which allow you to manage message
                acknowledgments in bulk. That is, you can set the
                acknowledgment state of messages in an existing
                subscription to the state captured by a snapshot.

            """

            http_options = (
                _BaseSubscriberRestTransport._BaseGetSnapshot._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_snapshot(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSubscriberRestTransport._BaseGetSnapshot,
                    "_BaseGetSnapshot__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.pubsub_v1.SubscriberClient.GetSnapshot",
                    extra={
                        "serviceName": "google.pubsub.v1.Subscriber",
                        "rpcName": "GetSnapshot",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SubscriberRestTransport._GetSnapshot._get_response(
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
            resp = pubsub.Snapshot()
            pb_resp = pubsub.Snapshot.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_snapshot(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_snapshot_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = pubsub.Snapshot.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.pubsub_v1.SubscriberClient.get_snapshot",
                    extra={
                        "serviceName": "google.pubsub.v1.Subscriber",
                        "rpcName": "GetSnapshot",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetSubscription(
        _BaseSubscriberRestTransport._BaseGetSubscription, SubscriberRestStub
    ):
        def __hash__(self):
            return hash("SubscriberRestTransport.GetSubscription")

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
            request: pubsub.GetSubscriptionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> pubsub.Subscription:
            r"""Call the get subscription method over HTTP.

            Args:
                request (~.pubsub.GetSubscriptionRequest):
                    The request object. Request for the GetSubscription
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.pubsub.Subscription:
                    A subscription resource. If none of ``push_config``,
                ``bigquery_config``, ``cloud_storage_config``, or
                ``bigtable_config`` is set, then the subscriber will
                pull and ack messages using API methods. At most one of
                these fields may be set.

            """

            http_options = (
                _BaseSubscriberRestTransport._BaseGetSubscription._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_subscription(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSubscriberRestTransport._BaseGetSubscription,
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
                    f"Sending request for google.pubsub_v1.SubscriberClient.GetSubscription",
                    extra={
                        "serviceName": "google.pubsub.v1.Subscriber",
                        "rpcName": "GetSubscription",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SubscriberRestTransport._GetSubscription._get_response(
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
            resp = pubsub.Subscription()
            pb_resp = pubsub.Subscription.pb(resp)

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
                    response_payload = pubsub.Subscription.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.pubsub_v1.SubscriberClient.get_subscription",
                    extra={
                        "serviceName": "google.pubsub.v1.Subscriber",
                        "rpcName": "GetSubscription",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListSnapshots(
        _BaseSubscriberRestTransport._BaseListSnapshots, SubscriberRestStub
    ):
        def __hash__(self):
            return hash("SubscriberRestTransport.ListSnapshots")

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
            request: pubsub.ListSnapshotsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> pubsub.ListSnapshotsResponse:
            r"""Call the list snapshots method over HTTP.

            Args:
                request (~.pubsub.ListSnapshotsRequest):
                    The request object. Request for the ``ListSnapshots`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.pubsub.ListSnapshotsResponse:
                    Response for the ``ListSnapshots`` method.
            """

            http_options = (
                _BaseSubscriberRestTransport._BaseListSnapshots._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_snapshots(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSubscriberRestTransport._BaseListSnapshots,
                    "_BaseListSnapshots__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.pubsub_v1.SubscriberClient.ListSnapshots",
                    extra={
                        "serviceName": "google.pubsub.v1.Subscriber",
                        "rpcName": "ListSnapshots",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SubscriberRestTransport._ListSnapshots._get_response(
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
            resp = pubsub.ListSnapshotsResponse()
            pb_resp = pubsub.ListSnapshotsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_snapshots(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_snapshots_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = pubsub.ListSnapshotsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.pubsub_v1.SubscriberClient.list_snapshots",
                    extra={
                        "serviceName": "google.pubsub.v1.Subscriber",
                        "rpcName": "ListSnapshots",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListSubscriptions(
        _BaseSubscriberRestTransport._BaseListSubscriptions, SubscriberRestStub
    ):
        def __hash__(self):
            return hash("SubscriberRestTransport.ListSubscriptions")

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
            request: pubsub.ListSubscriptionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> pubsub.ListSubscriptionsResponse:
            r"""Call the list subscriptions method over HTTP.

            Args:
                request (~.pubsub.ListSubscriptionsRequest):
                    The request object. Request for the ``ListSubscriptions`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.pubsub.ListSubscriptionsResponse:
                    Response for the ``ListSubscriptions`` method.
            """

            http_options = (
                _BaseSubscriberRestTransport._BaseListSubscriptions._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_subscriptions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSubscriberRestTransport._BaseListSubscriptions,
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
                    f"Sending request for google.pubsub_v1.SubscriberClient.ListSubscriptions",
                    extra={
                        "serviceName": "google.pubsub.v1.Subscriber",
                        "rpcName": "ListSubscriptions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SubscriberRestTransport._ListSubscriptions._get_response(
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
            resp = pubsub.ListSubscriptionsResponse()
            pb_resp = pubsub.ListSubscriptionsResponse.pb(resp)

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
                    response_payload = pubsub.ListSubscriptionsResponse.to_json(
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
                    "Received response for google.pubsub_v1.SubscriberClient.list_subscriptions",
                    extra={
                        "serviceName": "google.pubsub.v1.Subscriber",
                        "rpcName": "ListSubscriptions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ModifyAckDeadline(
        _BaseSubscriberRestTransport._BaseModifyAckDeadline, SubscriberRestStub
    ):
        def __hash__(self):
            return hash("SubscriberRestTransport.ModifyAckDeadline")

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
            request: pubsub.ModifyAckDeadlineRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the modify ack deadline method over HTTP.

            Args:
                request (~.pubsub.ModifyAckDeadlineRequest):
                    The request object. Request for the ModifyAckDeadline
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseSubscriberRestTransport._BaseModifyAckDeadline._get_http_options()
            )
            request, metadata = self._interceptor.pre_modify_ack_deadline(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSubscriberRestTransport._BaseModifyAckDeadline,
                    "_BaseModifyAckDeadline__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.pubsub_v1.SubscriberClient.ModifyAckDeadline",
                    extra={
                        "serviceName": "google.pubsub.v1.Subscriber",
                        "rpcName": "ModifyAckDeadline",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SubscriberRestTransport._ModifyAckDeadline._get_response(
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

    class _ModifyPushConfig(
        _BaseSubscriberRestTransport._BaseModifyPushConfig, SubscriberRestStub
    ):
        def __hash__(self):
            return hash("SubscriberRestTransport.ModifyPushConfig")

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
            request: pubsub.ModifyPushConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the modify push config method over HTTP.

            Args:
                request (~.pubsub.ModifyPushConfigRequest):
                    The request object. Request for the ModifyPushConfig
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseSubscriberRestTransport._BaseModifyPushConfig._get_http_options()
            )
            request, metadata = self._interceptor.pre_modify_push_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSubscriberRestTransport._BaseModifyPushConfig,
                    "_BaseModifyPushConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.pubsub_v1.SubscriberClient.ModifyPushConfig",
                    extra={
                        "serviceName": "google.pubsub.v1.Subscriber",
                        "rpcName": "ModifyPushConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SubscriberRestTransport._ModifyPushConfig._get_response(
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

    class _Pull(_BaseSubscriberRestTransport._BasePull, SubscriberRestStub):
        def __hash__(self):
            return hash("SubscriberRestTransport.Pull")

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
            request: pubsub.PullRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> pubsub.PullResponse:
            r"""Call the pull method over HTTP.

            Args:
                request (~.pubsub.PullRequest):
                    The request object. Request for the ``Pull`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.pubsub.PullResponse:
                    Response for the ``Pull`` method.
            """

            http_options = _BaseSubscriberRestTransport._BasePull._get_http_options()
            request, metadata = self._interceptor.pre_pull(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSubscriberRestTransport._BasePull,
                    "_BasePull__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.pubsub_v1.SubscriberClient.Pull",
                    extra={
                        "serviceName": "google.pubsub.v1.Subscriber",
                        "rpcName": "Pull",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SubscriberRestTransport._Pull._get_response(
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
            resp = pubsub.PullResponse()
            pb_resp = pubsub.PullResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_pull(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_pull_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = pubsub.PullResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.pubsub_v1.SubscriberClient.pull",
                    extra={
                        "serviceName": "google.pubsub.v1.Subscriber",
                        "rpcName": "Pull",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Seek(_BaseSubscriberRestTransport._BaseSeek, SubscriberRestStub):
        def __hash__(self):
            return hash("SubscriberRestTransport.Seek")

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
            request: pubsub.SeekRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> pubsub.SeekResponse:
            r"""Call the seek method over HTTP.

            Args:
                request (~.pubsub.SeekRequest):
                    The request object. Request for the ``Seek`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.pubsub.SeekResponse:
                    Response for the ``Seek`` method (this response is
                empty).

            """

            http_options = _BaseSubscriberRestTransport._BaseSeek._get_http_options()
            request, metadata = self._interceptor.pre_seek(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSubscriberRestTransport._BaseSeek,
                    "_BaseSeek__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.pubsub_v1.SubscriberClient.Seek",
                    extra={
                        "serviceName": "google.pubsub.v1.Subscriber",
                        "rpcName": "Seek",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SubscriberRestTransport._Seek._get_response(
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
            resp = pubsub.SeekResponse()
            pb_resp = pubsub.SeekResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_seek(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_seek_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = pubsub.SeekResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.pubsub_v1.SubscriberClient.seek",
                    extra={
                        "serviceName": "google.pubsub.v1.Subscriber",
                        "rpcName": "Seek",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _StreamingPull(
        _BaseSubscriberRestTransport._BaseStreamingPull, SubscriberRestStub
    ):
        def __hash__(self):
            return hash("SubscriberRestTransport.StreamingPull")

        def __call__(
            self,
            request: pubsub.StreamingPullRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> rest_streaming.ResponseIterator:
            raise NotImplementedError(
                "Method StreamingPull is not available over REST transport"
            )

    class _UpdateSnapshot(
        _BaseSubscriberRestTransport._BaseUpdateSnapshot, SubscriberRestStub
    ):
        def __hash__(self):
            return hash("SubscriberRestTransport.UpdateSnapshot")

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
            request: pubsub.UpdateSnapshotRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> pubsub.Snapshot:
            r"""Call the update snapshot method over HTTP.

            Args:
                request (~.pubsub.UpdateSnapshotRequest):
                    The request object. Request for the UpdateSnapshot
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.pubsub.Snapshot:
                    A snapshot resource. Snapshots are used in
                `Seek <https://cloud.google.com/pubsub/docs/replay-overview>`__
                operations, which allow you to manage message
                acknowledgments in bulk. That is, you can set the
                acknowledgment state of messages in an existing
                subscription to the state captured by a snapshot.

            """

            http_options = (
                _BaseSubscriberRestTransport._BaseUpdateSnapshot._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_snapshot(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSubscriberRestTransport._BaseUpdateSnapshot,
                    "_BaseUpdateSnapshot__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.pubsub_v1.SubscriberClient.UpdateSnapshot",
                    extra={
                        "serviceName": "google.pubsub.v1.Subscriber",
                        "rpcName": "UpdateSnapshot",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SubscriberRestTransport._UpdateSnapshot._get_response(
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
            resp = pubsub.Snapshot()
            pb_resp = pubsub.Snapshot.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_snapshot(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_snapshot_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = pubsub.Snapshot.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.pubsub_v1.SubscriberClient.update_snapshot",
                    extra={
                        "serviceName": "google.pubsub.v1.Subscriber",
                        "rpcName": "UpdateSnapshot",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateSubscription(
        _BaseSubscriberRestTransport._BaseUpdateSubscription, SubscriberRestStub
    ):
        def __hash__(self):
            return hash("SubscriberRestTransport.UpdateSubscription")

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
            request: pubsub.UpdateSubscriptionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> pubsub.Subscription:
            r"""Call the update subscription method over HTTP.

            Args:
                request (~.pubsub.UpdateSubscriptionRequest):
                    The request object. Request for the UpdateSubscription
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.pubsub.Subscription:
                    A subscription resource. If none of ``push_config``,
                ``bigquery_config``, ``cloud_storage_config``, or
                ``bigtable_config`` is set, then the subscriber will
                pull and ack messages using API methods. At most one of
                these fields may be set.

            """

            http_options = (
                _BaseSubscriberRestTransport._BaseUpdateSubscription._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_subscription(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSubscriberRestTransport._BaseUpdateSubscription,
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
                    f"Sending request for google.pubsub_v1.SubscriberClient.UpdateSubscription",
                    extra={
                        "serviceName": "google.pubsub.v1.Subscriber",
                        "rpcName": "UpdateSubscription",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SubscriberRestTransport._UpdateSubscription._get_response(
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
            resp = pubsub.Subscription()
            pb_resp = pubsub.Subscription.pb(resp)

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
                    response_payload = pubsub.Subscription.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.pubsub_v1.SubscriberClient.update_subscription",
                    extra={
                        "serviceName": "google.pubsub.v1.Subscriber",
                        "rpcName": "UpdateSubscription",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def acknowledge(self) -> Callable[[pubsub.AcknowledgeRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Acknowledge(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_snapshot(
        self,
    ) -> Callable[[pubsub.CreateSnapshotRequest], pubsub.Snapshot]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateSnapshot(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_subscription(
        self,
    ) -> Callable[[pubsub.Subscription], pubsub.Subscription]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateSubscription(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_snapshot(
        self,
    ) -> Callable[[pubsub.DeleteSnapshotRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteSnapshot(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_subscription(
        self,
    ) -> Callable[[pubsub.DeleteSubscriptionRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteSubscription(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_snapshot(self) -> Callable[[pubsub.GetSnapshotRequest], pubsub.Snapshot]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSnapshot(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_subscription(
        self,
    ) -> Callable[[pubsub.GetSubscriptionRequest], pubsub.Subscription]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSubscription(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_snapshots(
        self,
    ) -> Callable[[pubsub.ListSnapshotsRequest], pubsub.ListSnapshotsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListSnapshots(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_subscriptions(
        self,
    ) -> Callable[[pubsub.ListSubscriptionsRequest], pubsub.ListSubscriptionsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListSubscriptions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def modify_ack_deadline(
        self,
    ) -> Callable[[pubsub.ModifyAckDeadlineRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ModifyAckDeadline(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def modify_push_config(
        self,
    ) -> Callable[[pubsub.ModifyPushConfigRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ModifyPushConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def pull(self) -> Callable[[pubsub.PullRequest], pubsub.PullResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Pull(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def seek(self) -> Callable[[pubsub.SeekRequest], pubsub.SeekResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Seek(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def streaming_pull(
        self,
    ) -> Callable[[pubsub.StreamingPullRequest], pubsub.StreamingPullResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._StreamingPull(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_snapshot(
        self,
    ) -> Callable[[pubsub.UpdateSnapshotRequest], pubsub.Snapshot]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateSnapshot(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_subscription(
        self,
    ) -> Callable[[pubsub.UpdateSubscriptionRequest], pubsub.Subscription]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateSubscription(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_iam_policy(self):
        return self._GetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    class _GetIamPolicy(
        _BaseSubscriberRestTransport._BaseGetIamPolicy, SubscriberRestStub
    ):
        def __hash__(self):
            return hash("SubscriberRestTransport.GetIamPolicy")

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
                _BaseSubscriberRestTransport._BaseGetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSubscriberRestTransport._BaseGetIamPolicy,
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
                    f"Sending request for google.pubsub_v1.SubscriberClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.pubsub.v1.Subscriber",
                        "rpcName": "GetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SubscriberRestTransport._GetIamPolicy._get_response(
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
                    "Received response for google.pubsub_v1.SubscriberAsyncClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.pubsub.v1.Subscriber",
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
        _BaseSubscriberRestTransport._BaseSetIamPolicy, SubscriberRestStub
    ):
        def __hash__(self):
            return hash("SubscriberRestTransport.SetIamPolicy")

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
                _BaseSubscriberRestTransport._BaseSetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSubscriberRestTransport._BaseSetIamPolicy,
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
                    f"Sending request for google.pubsub_v1.SubscriberClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.pubsub.v1.Subscriber",
                        "rpcName": "SetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SubscriberRestTransport._SetIamPolicy._get_response(
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
                    "Received response for google.pubsub_v1.SubscriberAsyncClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.pubsub.v1.Subscriber",
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
        _BaseSubscriberRestTransport._BaseTestIamPermissions, SubscriberRestStub
    ):
        def __hash__(self):
            return hash("SubscriberRestTransport.TestIamPermissions")

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
                _BaseSubscriberRestTransport._BaseTestIamPermissions._get_http_options()
            )
            request, metadata = self._interceptor.pre_test_iam_permissions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSubscriberRestTransport._BaseTestIamPermissions,
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
                    f"Sending request for google.pubsub_v1.SubscriberClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.pubsub.v1.Subscriber",
                        "rpcName": "TestIamPermissions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SubscriberRestTransport._TestIamPermissions._get_response(
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
                    "Received response for google.pubsub_v1.SubscriberAsyncClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.pubsub.v1.Subscriber",
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


__all__ = ("SubscriberRestTransport",)
