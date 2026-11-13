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

import google.api.httpbody_pb2 as httpbody_pb2  # type: ignore
import google.protobuf
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.chronicle_v1._compat import transcode_request
from google.cloud.chronicle_v1.types import feed
from google.cloud.chronicle_v1.types import feed as gcc_feed

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseFeedsServiceRestTransport

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


class FeedsServiceRestInterceptor:
    """Interceptor for FeedsService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the FeedsServiceRestTransport.

    .. code-block:: python
        class MyCustomFeedsServiceInterceptor(FeedsServiceRestInterceptor):
            def pre_create_feed(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_feed(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_feed(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_disable_feed(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_disable_feed(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_enable_feed(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_enable_feed(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_fetch_service_account_for_customer(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_service_account_for_customer(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_generate_secret(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_generate_secret(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_feed(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_feed(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_feed_pack(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_feed_pack(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_import_push_logs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_import_push_logs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_feed_packs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_feed_packs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_feeds(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_feeds(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_feed_source_type_schemas(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_feed_source_type_schemas(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_log_type_schemas(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_log_type_schemas(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_feed(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_feed(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = FeedsServiceRestTransport(interceptor=MyCustomFeedsServiceInterceptor())
        client = FeedsServiceClient(transport=transport)


    """

    def pre_create_feed(
        self,
        request: gcc_feed.CreateFeedRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcc_feed.CreateFeedRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_feed

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FeedsService server.
        """
        return request, metadata

    def post_create_feed(self, response: gcc_feed.Feed) -> gcc_feed.Feed:
        """Post-rpc interceptor for create_feed

        DEPRECATED. Please use the `post_create_feed_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the FeedsService server but before
        it is returned to user code. This `post_create_feed` interceptor runs
        before the `post_create_feed_with_metadata` interceptor.
        """
        return response

    def post_create_feed_with_metadata(
        self, response: gcc_feed.Feed, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[gcc_feed.Feed, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_feed

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the FeedsService server but before it is returned to user code.

        We recommend only using this `post_create_feed_with_metadata`
        interceptor in new development instead of the `post_create_feed` interceptor.
        When both interceptors are used, this `post_create_feed_with_metadata` interceptor runs after the
        `post_create_feed` interceptor. The (possibly modified) response returned by
        `post_create_feed` will be passed to
        `post_create_feed_with_metadata`.
        """
        return response, metadata

    def pre_delete_feed(
        self,
        request: feed.DeleteFeedRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[feed.DeleteFeedRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_feed

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FeedsService server.
        """
        return request, metadata

    def pre_disable_feed(
        self,
        request: feed.DisableFeedRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[feed.DisableFeedRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for disable_feed

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FeedsService server.
        """
        return request, metadata

    def post_disable_feed(self, response: feed.Feed) -> feed.Feed:
        """Post-rpc interceptor for disable_feed

        DEPRECATED. Please use the `post_disable_feed_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the FeedsService server but before
        it is returned to user code. This `post_disable_feed` interceptor runs
        before the `post_disable_feed_with_metadata` interceptor.
        """
        return response

    def post_disable_feed_with_metadata(
        self, response: feed.Feed, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[feed.Feed, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for disable_feed

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the FeedsService server but before it is returned to user code.

        We recommend only using this `post_disable_feed_with_metadata`
        interceptor in new development instead of the `post_disable_feed` interceptor.
        When both interceptors are used, this `post_disable_feed_with_metadata` interceptor runs after the
        `post_disable_feed` interceptor. The (possibly modified) response returned by
        `post_disable_feed` will be passed to
        `post_disable_feed_with_metadata`.
        """
        return response, metadata

    def pre_enable_feed(
        self,
        request: feed.EnableFeedRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[feed.EnableFeedRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for enable_feed

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FeedsService server.
        """
        return request, metadata

    def post_enable_feed(self, response: feed.Feed) -> feed.Feed:
        """Post-rpc interceptor for enable_feed

        DEPRECATED. Please use the `post_enable_feed_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the FeedsService server but before
        it is returned to user code. This `post_enable_feed` interceptor runs
        before the `post_enable_feed_with_metadata` interceptor.
        """
        return response

    def post_enable_feed_with_metadata(
        self, response: feed.Feed, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[feed.Feed, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for enable_feed

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the FeedsService server but before it is returned to user code.

        We recommend only using this `post_enable_feed_with_metadata`
        interceptor in new development instead of the `post_enable_feed` interceptor.
        When both interceptors are used, this `post_enable_feed_with_metadata` interceptor runs after the
        `post_enable_feed` interceptor. The (possibly modified) response returned by
        `post_enable_feed` will be passed to
        `post_enable_feed_with_metadata`.
        """
        return response, metadata

    def pre_fetch_service_account_for_customer(
        self,
        request: feed.FetchServiceAccountForCustomerRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        feed.FetchServiceAccountForCustomerRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for fetch_service_account_for_customer

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FeedsService server.
        """
        return request, metadata

    def post_fetch_service_account_for_customer(
        self, response: feed.FeedServiceAccount
    ) -> feed.FeedServiceAccount:
        """Post-rpc interceptor for fetch_service_account_for_customer

        DEPRECATED. Please use the `post_fetch_service_account_for_customer_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the FeedsService server but before
        it is returned to user code. This `post_fetch_service_account_for_customer` interceptor runs
        before the `post_fetch_service_account_for_customer_with_metadata` interceptor.
        """
        return response

    def post_fetch_service_account_for_customer_with_metadata(
        self,
        response: feed.FeedServiceAccount,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[feed.FeedServiceAccount, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for fetch_service_account_for_customer

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the FeedsService server but before it is returned to user code.

        We recommend only using this `post_fetch_service_account_for_customer_with_metadata`
        interceptor in new development instead of the `post_fetch_service_account_for_customer` interceptor.
        When both interceptors are used, this `post_fetch_service_account_for_customer_with_metadata` interceptor runs after the
        `post_fetch_service_account_for_customer` interceptor. The (possibly modified) response returned by
        `post_fetch_service_account_for_customer` will be passed to
        `post_fetch_service_account_for_customer_with_metadata`.
        """
        return response, metadata

    def pre_generate_secret(
        self,
        request: feed.GenerateSecretRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[feed.GenerateSecretRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for generate_secret

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FeedsService server.
        """
        return request, metadata

    def post_generate_secret(
        self, response: feed.GenerateSecretResponse
    ) -> feed.GenerateSecretResponse:
        """Post-rpc interceptor for generate_secret

        DEPRECATED. Please use the `post_generate_secret_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the FeedsService server but before
        it is returned to user code. This `post_generate_secret` interceptor runs
        before the `post_generate_secret_with_metadata` interceptor.
        """
        return response

    def post_generate_secret_with_metadata(
        self,
        response: feed.GenerateSecretResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[feed.GenerateSecretResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for generate_secret

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the FeedsService server but before it is returned to user code.

        We recommend only using this `post_generate_secret_with_metadata`
        interceptor in new development instead of the `post_generate_secret` interceptor.
        When both interceptors are used, this `post_generate_secret_with_metadata` interceptor runs after the
        `post_generate_secret` interceptor. The (possibly modified) response returned by
        `post_generate_secret` will be passed to
        `post_generate_secret_with_metadata`.
        """
        return response, metadata

    def pre_get_feed(
        self,
        request: feed.GetFeedRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[feed.GetFeedRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_feed

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FeedsService server.
        """
        return request, metadata

    def post_get_feed(self, response: feed.Feed) -> feed.Feed:
        """Post-rpc interceptor for get_feed

        DEPRECATED. Please use the `post_get_feed_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the FeedsService server but before
        it is returned to user code. This `post_get_feed` interceptor runs
        before the `post_get_feed_with_metadata` interceptor.
        """
        return response

    def post_get_feed_with_metadata(
        self, response: feed.Feed, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[feed.Feed, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_feed

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the FeedsService server but before it is returned to user code.

        We recommend only using this `post_get_feed_with_metadata`
        interceptor in new development instead of the `post_get_feed` interceptor.
        When both interceptors are used, this `post_get_feed_with_metadata` interceptor runs after the
        `post_get_feed` interceptor. The (possibly modified) response returned by
        `post_get_feed` will be passed to
        `post_get_feed_with_metadata`.
        """
        return response, metadata

    def pre_get_feed_pack(
        self,
        request: feed.GetFeedPackRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[feed.GetFeedPackRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_feed_pack

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FeedsService server.
        """
        return request, metadata

    def post_get_feed_pack(self, response: feed.FeedPack) -> feed.FeedPack:
        """Post-rpc interceptor for get_feed_pack

        DEPRECATED. Please use the `post_get_feed_pack_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the FeedsService server but before
        it is returned to user code. This `post_get_feed_pack` interceptor runs
        before the `post_get_feed_pack_with_metadata` interceptor.
        """
        return response

    def post_get_feed_pack_with_metadata(
        self, response: feed.FeedPack, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[feed.FeedPack, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_feed_pack

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the FeedsService server but before it is returned to user code.

        We recommend only using this `post_get_feed_pack_with_metadata`
        interceptor in new development instead of the `post_get_feed_pack` interceptor.
        When both interceptors are used, this `post_get_feed_pack_with_metadata` interceptor runs after the
        `post_get_feed_pack` interceptor. The (possibly modified) response returned by
        `post_get_feed_pack` will be passed to
        `post_get_feed_pack_with_metadata`.
        """
        return response, metadata

    def pre_import_push_logs(
        self,
        request: feed.ImportPushLogsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[feed.ImportPushLogsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for import_push_logs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FeedsService server.
        """
        return request, metadata

    def post_import_push_logs(
        self, response: httpbody_pb2.HttpBody
    ) -> httpbody_pb2.HttpBody:
        """Post-rpc interceptor for import_push_logs

        DEPRECATED. Please use the `post_import_push_logs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the FeedsService server but before
        it is returned to user code. This `post_import_push_logs` interceptor runs
        before the `post_import_push_logs_with_metadata` interceptor.
        """
        return response

    def post_import_push_logs_with_metadata(
        self,
        response: httpbody_pb2.HttpBody,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[httpbody_pb2.HttpBody, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for import_push_logs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the FeedsService server but before it is returned to user code.

        We recommend only using this `post_import_push_logs_with_metadata`
        interceptor in new development instead of the `post_import_push_logs` interceptor.
        When both interceptors are used, this `post_import_push_logs_with_metadata` interceptor runs after the
        `post_import_push_logs` interceptor. The (possibly modified) response returned by
        `post_import_push_logs` will be passed to
        `post_import_push_logs_with_metadata`.
        """
        return response, metadata

    def pre_list_feed_packs(
        self,
        request: feed.ListFeedPacksRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[feed.ListFeedPacksRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_feed_packs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FeedsService server.
        """
        return request, metadata

    def post_list_feed_packs(
        self, response: feed.ListFeedPacksResponse
    ) -> feed.ListFeedPacksResponse:
        """Post-rpc interceptor for list_feed_packs

        DEPRECATED. Please use the `post_list_feed_packs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the FeedsService server but before
        it is returned to user code. This `post_list_feed_packs` interceptor runs
        before the `post_list_feed_packs_with_metadata` interceptor.
        """
        return response

    def post_list_feed_packs_with_metadata(
        self,
        response: feed.ListFeedPacksResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[feed.ListFeedPacksResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_feed_packs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the FeedsService server but before it is returned to user code.

        We recommend only using this `post_list_feed_packs_with_metadata`
        interceptor in new development instead of the `post_list_feed_packs` interceptor.
        When both interceptors are used, this `post_list_feed_packs_with_metadata` interceptor runs after the
        `post_list_feed_packs` interceptor. The (possibly modified) response returned by
        `post_list_feed_packs` will be passed to
        `post_list_feed_packs_with_metadata`.
        """
        return response, metadata

    def pre_list_feeds(
        self,
        request: feed.ListFeedsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[feed.ListFeedsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_feeds

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FeedsService server.
        """
        return request, metadata

    def post_list_feeds(
        self, response: feed.ListFeedsResponse
    ) -> feed.ListFeedsResponse:
        """Post-rpc interceptor for list_feeds

        DEPRECATED. Please use the `post_list_feeds_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the FeedsService server but before
        it is returned to user code. This `post_list_feeds` interceptor runs
        before the `post_list_feeds_with_metadata` interceptor.
        """
        return response

    def post_list_feeds_with_metadata(
        self,
        response: feed.ListFeedsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[feed.ListFeedsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_feeds

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the FeedsService server but before it is returned to user code.

        We recommend only using this `post_list_feeds_with_metadata`
        interceptor in new development instead of the `post_list_feeds` interceptor.
        When both interceptors are used, this `post_list_feeds_with_metadata` interceptor runs after the
        `post_list_feeds` interceptor. The (possibly modified) response returned by
        `post_list_feeds` will be passed to
        `post_list_feeds_with_metadata`.
        """
        return response, metadata

    def pre_list_feed_source_type_schemas(
        self,
        request: feed.ListFeedSourceTypeSchemasRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        feed.ListFeedSourceTypeSchemasRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_feed_source_type_schemas

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FeedsService server.
        """
        return request, metadata

    def post_list_feed_source_type_schemas(
        self, response: feed.ListFeedSourceTypeSchemasResponse
    ) -> feed.ListFeedSourceTypeSchemasResponse:
        """Post-rpc interceptor for list_feed_source_type_schemas

        DEPRECATED. Please use the `post_list_feed_source_type_schemas_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the FeedsService server but before
        it is returned to user code. This `post_list_feed_source_type_schemas` interceptor runs
        before the `post_list_feed_source_type_schemas_with_metadata` interceptor.
        """
        return response

    def post_list_feed_source_type_schemas_with_metadata(
        self,
        response: feed.ListFeedSourceTypeSchemasResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        feed.ListFeedSourceTypeSchemasResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_feed_source_type_schemas

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the FeedsService server but before it is returned to user code.

        We recommend only using this `post_list_feed_source_type_schemas_with_metadata`
        interceptor in new development instead of the `post_list_feed_source_type_schemas` interceptor.
        When both interceptors are used, this `post_list_feed_source_type_schemas_with_metadata` interceptor runs after the
        `post_list_feed_source_type_schemas` interceptor. The (possibly modified) response returned by
        `post_list_feed_source_type_schemas` will be passed to
        `post_list_feed_source_type_schemas_with_metadata`.
        """
        return response, metadata

    def pre_list_log_type_schemas(
        self,
        request: feed.ListLogTypeSchemasRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[feed.ListLogTypeSchemasRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_log_type_schemas

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FeedsService server.
        """
        return request, metadata

    def post_list_log_type_schemas(
        self, response: feed.ListLogTypeSchemasResponse
    ) -> feed.ListLogTypeSchemasResponse:
        """Post-rpc interceptor for list_log_type_schemas

        DEPRECATED. Please use the `post_list_log_type_schemas_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the FeedsService server but before
        it is returned to user code. This `post_list_log_type_schemas` interceptor runs
        before the `post_list_log_type_schemas_with_metadata` interceptor.
        """
        return response

    def post_list_log_type_schemas_with_metadata(
        self,
        response: feed.ListLogTypeSchemasResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        feed.ListLogTypeSchemasResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_log_type_schemas

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the FeedsService server but before it is returned to user code.

        We recommend only using this `post_list_log_type_schemas_with_metadata`
        interceptor in new development instead of the `post_list_log_type_schemas` interceptor.
        When both interceptors are used, this `post_list_log_type_schemas_with_metadata` interceptor runs after the
        `post_list_log_type_schemas` interceptor. The (possibly modified) response returned by
        `post_list_log_type_schemas` will be passed to
        `post_list_log_type_schemas_with_metadata`.
        """
        return response, metadata

    def pre_update_feed(
        self,
        request: gcc_feed.UpdateFeedRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcc_feed.UpdateFeedRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_feed

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FeedsService server.
        """
        return request, metadata

    def post_update_feed(self, response: gcc_feed.Feed) -> gcc_feed.Feed:
        """Post-rpc interceptor for update_feed

        DEPRECATED. Please use the `post_update_feed_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the FeedsService server but before
        it is returned to user code. This `post_update_feed` interceptor runs
        before the `post_update_feed_with_metadata` interceptor.
        """
        return response

    def post_update_feed_with_metadata(
        self, response: gcc_feed.Feed, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[gcc_feed.Feed, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_feed

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the FeedsService server but before it is returned to user code.

        We recommend only using this `post_update_feed_with_metadata`
        interceptor in new development instead of the `post_update_feed` interceptor.
        When both interceptors are used, this `post_update_feed_with_metadata` interceptor runs after the
        `post_update_feed` interceptor. The (possibly modified) response returned by
        `post_update_feed` will be passed to
        `post_update_feed_with_metadata`.
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
        before they are sent to the FeedsService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the FeedsService server but before
        it is returned to user code.
        """
        return response

    def pre_delete_operation(
        self,
        request: operations_pb2.DeleteOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.DeleteOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FeedsService server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the FeedsService server but before
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
        before they are sent to the FeedsService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the FeedsService server but before
        it is returned to user code.
        """
        return response

    def pre_list_operations(
        self,
        request: operations_pb2.ListOperationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.ListOperationsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_operations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the FeedsService server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the FeedsService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class FeedsServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: FeedsServiceRestInterceptor


class FeedsServiceRestTransport(_BaseFeedsServiceRestTransport):
    """REST backend synchronous transport for FeedsService.

    FeedsService contains procedures for managing Chronicle
    third-party feeds.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "chronicle.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[FeedsServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'chronicle.googleapis.com').
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
            interceptor (Optional[FeedsServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or FeedsServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CreateFeed(
        _BaseFeedsServiceRestTransport._BaseCreateFeed, FeedsServiceRestStub
    ):
        def __hash__(self):
            return hash("FeedsServiceRestTransport.CreateFeed")

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
            request: gcc_feed.CreateFeedRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcc_feed.Feed:
            r"""Call the create feed method over HTTP.

            Args:
                request (~.gcc_feed.CreateFeedRequest):
                    The request object. Request message for CreateFeed.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcc_feed.Feed:
                    Feed is a resource that contains feed
                information needed to create a feed.

            """

            http_options = (
                _BaseFeedsServiceRestTransport._BaseCreateFeed._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_feed(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFeedsServiceRestTransport._BaseCreateFeed,
                    "_BaseCreateFeed__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.FeedsServiceClient.CreateFeed",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FeedsService",
                        "rpcName": "CreateFeed",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FeedsServiceRestTransport._CreateFeed._get_response(
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
            resp = gcc_feed.Feed()
            pb_resp = gcc_feed.Feed.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_feed(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_feed_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcc_feed.Feed.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.chronicle_v1.FeedsServiceClient.create_feed",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FeedsService",
                        "rpcName": "CreateFeed",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteFeed(
        _BaseFeedsServiceRestTransport._BaseDeleteFeed, FeedsServiceRestStub
    ):
        def __hash__(self):
            return hash("FeedsServiceRestTransport.DeleteFeed")

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
            request: feed.DeleteFeedRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete feed method over HTTP.

            Args:
                request (~.feed.DeleteFeedRequest):
                    The request object. Request message to delete a feed.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseFeedsServiceRestTransport._BaseDeleteFeed._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_feed(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFeedsServiceRestTransport._BaseDeleteFeed,
                    "_BaseDeleteFeed__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.FeedsServiceClient.DeleteFeed",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FeedsService",
                        "rpcName": "DeleteFeed",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FeedsServiceRestTransport._DeleteFeed._get_response(
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

    class _DisableFeed(
        _BaseFeedsServiceRestTransport._BaseDisableFeed, FeedsServiceRestStub
    ):
        def __hash__(self):
            return hash("FeedsServiceRestTransport.DisableFeed")

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
            request: feed.DisableFeedRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> feed.Feed:
            r"""Call the disable feed method over HTTP.

            Args:
                request (~.feed.DisableFeedRequest):
                    The request object. DisableFeed request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.feed.Feed:
                    Feed is a resource that contains feed
                information needed to create a feed.

            """

            http_options = (
                _BaseFeedsServiceRestTransport._BaseDisableFeed._get_http_options()
            )
            request, metadata = self._interceptor.pre_disable_feed(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFeedsServiceRestTransport._BaseDisableFeed,
                    "_BaseDisableFeed__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.FeedsServiceClient.DisableFeed",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FeedsService",
                        "rpcName": "DisableFeed",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FeedsServiceRestTransport._DisableFeed._get_response(
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
            resp = feed.Feed()
            pb_resp = feed.Feed.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_disable_feed(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_disable_feed_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = feed.Feed.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.chronicle_v1.FeedsServiceClient.disable_feed",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FeedsService",
                        "rpcName": "DisableFeed",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _EnableFeed(
        _BaseFeedsServiceRestTransport._BaseEnableFeed, FeedsServiceRestStub
    ):
        def __hash__(self):
            return hash("FeedsServiceRestTransport.EnableFeed")

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
            request: feed.EnableFeedRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> feed.Feed:
            r"""Call the enable feed method over HTTP.

            Args:
                request (~.feed.EnableFeedRequest):
                    The request object. EnableFeed request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.feed.Feed:
                    Feed is a resource that contains feed
                information needed to create a feed.

            """

            http_options = (
                _BaseFeedsServiceRestTransport._BaseEnableFeed._get_http_options()
            )
            request, metadata = self._interceptor.pre_enable_feed(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFeedsServiceRestTransport._BaseEnableFeed,
                    "_BaseEnableFeed__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.FeedsServiceClient.EnableFeed",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FeedsService",
                        "rpcName": "EnableFeed",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FeedsServiceRestTransport._EnableFeed._get_response(
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
            resp = feed.Feed()
            pb_resp = feed.Feed.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_enable_feed(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_enable_feed_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = feed.Feed.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.chronicle_v1.FeedsServiceClient.enable_feed",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FeedsService",
                        "rpcName": "EnableFeed",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FetchServiceAccountForCustomer(
        _BaseFeedsServiceRestTransport._BaseFetchServiceAccountForCustomer,
        FeedsServiceRestStub,
    ):
        def __hash__(self):
            return hash("FeedsServiceRestTransport.FetchServiceAccountForCustomer")

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
            request: feed.FetchServiceAccountForCustomerRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> feed.FeedServiceAccount:
            r"""Call the fetch service account for
            customer method over HTTP.

                Args:
                    request (~.feed.FetchServiceAccountForCustomerRequest):
                        The request object. Request message for
                    FetchServiceAccountForCustomer.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.feed.FeedServiceAccount:
                        FeedServiceAccount is a resource that
                    wraps the feed service account's name.

            """

            http_options = _BaseFeedsServiceRestTransport._BaseFetchServiceAccountForCustomer._get_http_options()
            request, metadata = (
                self._interceptor.pre_fetch_service_account_for_customer(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFeedsServiceRestTransport._BaseFetchServiceAccountForCustomer,
                    "_BaseFetchServiceAccountForCustomer__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.FeedsServiceClient.FetchServiceAccountForCustomer",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FeedsService",
                        "rpcName": "FetchServiceAccountForCustomer",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                FeedsServiceRestTransport._FetchServiceAccountForCustomer._get_response(
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
            resp = feed.FeedServiceAccount()
            pb_resp = feed.FeedServiceAccount.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_fetch_service_account_for_customer(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_fetch_service_account_for_customer_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = feed.FeedServiceAccount.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.chronicle_v1.FeedsServiceClient.fetch_service_account_for_customer",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FeedsService",
                        "rpcName": "FetchServiceAccountForCustomer",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GenerateSecret(
        _BaseFeedsServiceRestTransport._BaseGenerateSecret, FeedsServiceRestStub
    ):
        def __hash__(self):
            return hash("FeedsServiceRestTransport.GenerateSecret")

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
            request: feed.GenerateSecretRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> feed.GenerateSecretResponse:
            r"""Call the generate secret method over HTTP.

            Args:
                request (~.feed.GenerateSecretRequest):
                    The request object. GenerateSecret request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.feed.GenerateSecretResponse:
                    GenerateSecret response message.
            """

            http_options = (
                _BaseFeedsServiceRestTransport._BaseGenerateSecret._get_http_options()
            )
            request, metadata = self._interceptor.pre_generate_secret(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFeedsServiceRestTransport._BaseGenerateSecret,
                    "_BaseGenerateSecret__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.FeedsServiceClient.GenerateSecret",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FeedsService",
                        "rpcName": "GenerateSecret",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FeedsServiceRestTransport._GenerateSecret._get_response(
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
            resp = feed.GenerateSecretResponse()
            pb_resp = feed.GenerateSecretResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_generate_secret(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_generate_secret_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = feed.GenerateSecretResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.chronicle_v1.FeedsServiceClient.generate_secret",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FeedsService",
                        "rpcName": "GenerateSecret",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetFeed(_BaseFeedsServiceRestTransport._BaseGetFeed, FeedsServiceRestStub):
        def __hash__(self):
            return hash("FeedsServiceRestTransport.GetFeed")

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
            request: feed.GetFeedRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> feed.Feed:
            r"""Call the get feed method over HTTP.

            Args:
                request (~.feed.GetFeedRequest):
                    The request object. Request message to retrieve a feed.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.feed.Feed:
                    Feed is a resource that contains feed
                information needed to create a feed.

            """

            http_options = (
                _BaseFeedsServiceRestTransport._BaseGetFeed._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_feed(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFeedsServiceRestTransport._BaseGetFeed,
                    "_BaseGetFeed__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.FeedsServiceClient.GetFeed",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FeedsService",
                        "rpcName": "GetFeed",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FeedsServiceRestTransport._GetFeed._get_response(
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
            resp = feed.Feed()
            pb_resp = feed.Feed.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_feed(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_feed_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = feed.Feed.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.chronicle_v1.FeedsServiceClient.get_feed",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FeedsService",
                        "rpcName": "GetFeed",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetFeedPack(
        _BaseFeedsServiceRestTransport._BaseGetFeedPack, FeedsServiceRestStub
    ):
        def __hash__(self):
            return hash("FeedsServiceRestTransport.GetFeedPack")

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
            request: feed.GetFeedPackRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> feed.FeedPack:
            r"""Call the get feed pack method over HTTP.

            Args:
                request (~.feed.GetFeedPackRequest):
                    The request object. Request message for GetFeedPack.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.feed.FeedPack:
                    FeedPack is a logical container for
                related LogTypes for which feeds can be
                configured.

            """

            http_options = (
                _BaseFeedsServiceRestTransport._BaseGetFeedPack._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_feed_pack(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFeedsServiceRestTransport._BaseGetFeedPack,
                    "_BaseGetFeedPack__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.FeedsServiceClient.GetFeedPack",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FeedsService",
                        "rpcName": "GetFeedPack",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FeedsServiceRestTransport._GetFeedPack._get_response(
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
            resp = feed.FeedPack()
            pb_resp = feed.FeedPack.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_feed_pack(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_feed_pack_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = feed.FeedPack.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.chronicle_v1.FeedsServiceClient.get_feed_pack",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FeedsService",
                        "rpcName": "GetFeedPack",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ImportPushLogs(
        _BaseFeedsServiceRestTransport._BaseImportPushLogs, FeedsServiceRestStub
    ):
        def __hash__(self):
            return hash("FeedsServiceRestTransport.ImportPushLogs")

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
            request: feed.ImportPushLogsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> httpbody_pb2.HttpBody:
            r"""Call the import push logs method over HTTP.

            Args:
                request (~.feed.ImportPushLogsRequest):
                    The request object. ImportPushLogsRequest request
                message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.httpbody_pb2.HttpBody:
                    Message that represents an arbitrary HTTP body. It
                should only be used for payload formats that can't be
                represented as JSON, such as raw binary or an HTML page.

                This message can be used both in streaming and
                non-streaming API methods in the request as well as the
                response.

                It can be used as a top-level request field, which is
                convenient if one wants to extract parameters from
                either the URL or HTTP template into the request fields
                and also want access to the raw HTTP body.

                Example:

                ::

                    message GetResourceRequest {
                      // A unique request id.
                      string request_id = 1;

                      // The raw HTTP body is bound to this field.
                      google.api.HttpBody http_body = 2;

                    }

                    service ResourceService {
                      rpc GetResource(GetResourceRequest)
                        returns (google.api.HttpBody);
                      rpc UpdateResource(google.api.HttpBody)
                        returns (google.protobuf.Empty);

                    }

                Example with streaming methods:

                ::

                    service CaldavService {
                      rpc GetCalendar(stream google.api.HttpBody)
                        returns (stream google.api.HttpBody);
                      rpc UpdateCalendar(stream google.api.HttpBody)
                        returns (stream google.api.HttpBody);

                    }

                Use of this type only changes how the request and
                response bodies are handled, all other features will
                continue to work unchanged.

            """

            http_options = (
                _BaseFeedsServiceRestTransport._BaseImportPushLogs._get_http_options()
            )
            request, metadata = self._interceptor.pre_import_push_logs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFeedsServiceRestTransport._BaseImportPushLogs,
                    "_BaseImportPushLogs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.FeedsServiceClient.ImportPushLogs",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FeedsService",
                        "rpcName": "ImportPushLogs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FeedsServiceRestTransport._ImportPushLogs._get_response(
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
            resp = httpbody_pb2.HttpBody()
            pb_resp = resp

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_import_push_logs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_import_push_logs_with_metadata(
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
                    "Received response for google.cloud.chronicle_v1.FeedsServiceClient.import_push_logs",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FeedsService",
                        "rpcName": "ImportPushLogs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListFeedPacks(
        _BaseFeedsServiceRestTransport._BaseListFeedPacks, FeedsServiceRestStub
    ):
        def __hash__(self):
            return hash("FeedsServiceRestTransport.ListFeedPacks")

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
            request: feed.ListFeedPacksRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> feed.ListFeedPacksResponse:
            r"""Call the list feed packs method over HTTP.

            Args:
                request (~.feed.ListFeedPacksRequest):
                    The request object. Request message for ListFeedPacks.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.feed.ListFeedPacksResponse:
                    Response message for ListFeedPacks.
            """

            http_options = (
                _BaseFeedsServiceRestTransport._BaseListFeedPacks._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_feed_packs(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFeedsServiceRestTransport._BaseListFeedPacks,
                    "_BaseListFeedPacks__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.FeedsServiceClient.ListFeedPacks",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FeedsService",
                        "rpcName": "ListFeedPacks",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FeedsServiceRestTransport._ListFeedPacks._get_response(
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
            resp = feed.ListFeedPacksResponse()
            pb_resp = feed.ListFeedPacksResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_feed_packs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_feed_packs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = feed.ListFeedPacksResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.chronicle_v1.FeedsServiceClient.list_feed_packs",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FeedsService",
                        "rpcName": "ListFeedPacks",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListFeeds(
        _BaseFeedsServiceRestTransport._BaseListFeeds, FeedsServiceRestStub
    ):
        def __hash__(self):
            return hash("FeedsServiceRestTransport.ListFeeds")

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
            request: feed.ListFeedsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> feed.ListFeedsResponse:
            r"""Call the list feeds method over HTTP.

            Args:
                request (~.feed.ListFeedsRequest):
                    The request object. Request message for ListFeed.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.feed.ListFeedsResponse:
                    Response message for ListFeed.
            """

            http_options = (
                _BaseFeedsServiceRestTransport._BaseListFeeds._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_feeds(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFeedsServiceRestTransport._BaseListFeeds,
                    "_BaseListFeeds__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.FeedsServiceClient.ListFeeds",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FeedsService",
                        "rpcName": "ListFeeds",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FeedsServiceRestTransport._ListFeeds._get_response(
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
            resp = feed.ListFeedsResponse()
            pb_resp = feed.ListFeedsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_feeds(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_feeds_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = feed.ListFeedsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.chronicle_v1.FeedsServiceClient.list_feeds",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FeedsService",
                        "rpcName": "ListFeeds",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListFeedSourceTypeSchemas(
        _BaseFeedsServiceRestTransport._BaseListFeedSourceTypeSchemas,
        FeedsServiceRestStub,
    ):
        def __hash__(self):
            return hash("FeedsServiceRestTransport.ListFeedSourceTypeSchemas")

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
            request: feed.ListFeedSourceTypeSchemasRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> feed.ListFeedSourceTypeSchemasResponse:
            r"""Call the list feed source type
            schemas method over HTTP.

                Args:
                    request (~.feed.ListFeedSourceTypeSchemasRequest):
                        The request object. ListFeedSourceTypeSchemas request
                    message. Note that Feed schemas do not
                    contain customer data, so are not scoped
                    to a particular customer.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.feed.ListFeedSourceTypeSchemasResponse:
                        ListFeedSourceTypeSchemas response
                    message.

            """

            http_options = _BaseFeedsServiceRestTransport._BaseListFeedSourceTypeSchemas._get_http_options()
            request, metadata = self._interceptor.pre_list_feed_source_type_schemas(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFeedsServiceRestTransport._BaseListFeedSourceTypeSchemas,
                    "_BaseListFeedSourceTypeSchemas__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.FeedsServiceClient.ListFeedSourceTypeSchemas",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FeedsService",
                        "rpcName": "ListFeedSourceTypeSchemas",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                FeedsServiceRestTransport._ListFeedSourceTypeSchemas._get_response(
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
            resp = feed.ListFeedSourceTypeSchemasResponse()
            pb_resp = feed.ListFeedSourceTypeSchemasResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_feed_source_type_schemas(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_feed_source_type_schemas_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = feed.ListFeedSourceTypeSchemasResponse.to_json(
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
                    "Received response for google.cloud.chronicle_v1.FeedsServiceClient.list_feed_source_type_schemas",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FeedsService",
                        "rpcName": "ListFeedSourceTypeSchemas",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListLogTypeSchemas(
        _BaseFeedsServiceRestTransport._BaseListLogTypeSchemas, FeedsServiceRestStub
    ):
        def __hash__(self):
            return hash("FeedsServiceRestTransport.ListLogTypeSchemas")

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
            request: feed.ListLogTypeSchemasRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> feed.ListLogTypeSchemasResponse:
            r"""Call the list log type schemas method over HTTP.

            Args:
                request (~.feed.ListLogTypeSchemasRequest):
                    The request object. ListLogTypeSchemas request message.
                Note that feed schemas do not contain
                customer data, so are not scoped to a
                particular customer.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.feed.ListLogTypeSchemasResponse:
                    ListLogTypeSchemas response message.
            """

            http_options = _BaseFeedsServiceRestTransport._BaseListLogTypeSchemas._get_http_options()
            request, metadata = self._interceptor.pre_list_log_type_schemas(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFeedsServiceRestTransport._BaseListLogTypeSchemas,
                    "_BaseListLogTypeSchemas__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.FeedsServiceClient.ListLogTypeSchemas",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FeedsService",
                        "rpcName": "ListLogTypeSchemas",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FeedsServiceRestTransport._ListLogTypeSchemas._get_response(
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
            resp = feed.ListLogTypeSchemasResponse()
            pb_resp = feed.ListLogTypeSchemasResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_log_type_schemas(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_log_type_schemas_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = feed.ListLogTypeSchemasResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.chronicle_v1.FeedsServiceClient.list_log_type_schemas",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FeedsService",
                        "rpcName": "ListLogTypeSchemas",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateFeed(
        _BaseFeedsServiceRestTransport._BaseUpdateFeed, FeedsServiceRestStub
    ):
        def __hash__(self):
            return hash("FeedsServiceRestTransport.UpdateFeed")

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
            request: gcc_feed.UpdateFeedRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcc_feed.Feed:
            r"""Call the update feed method over HTTP.

            Args:
                request (~.gcc_feed.UpdateFeedRequest):
                    The request object. Request message for UpdateFeed.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcc_feed.Feed:
                    Feed is a resource that contains feed
                information needed to create a feed.

            """

            http_options = (
                _BaseFeedsServiceRestTransport._BaseUpdateFeed._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_feed(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFeedsServiceRestTransport._BaseUpdateFeed,
                    "_BaseUpdateFeed__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.FeedsServiceClient.UpdateFeed",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FeedsService",
                        "rpcName": "UpdateFeed",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FeedsServiceRestTransport._UpdateFeed._get_response(
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
            resp = gcc_feed.Feed()
            pb_resp = gcc_feed.Feed.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_feed(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_feed_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcc_feed.Feed.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.chronicle_v1.FeedsServiceClient.update_feed",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FeedsService",
                        "rpcName": "UpdateFeed",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_feed(self) -> Callable[[gcc_feed.CreateFeedRequest], gcc_feed.Feed]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateFeed(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_feed(self) -> Callable[[feed.DeleteFeedRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteFeed(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def disable_feed(self) -> Callable[[feed.DisableFeedRequest], feed.Feed]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DisableFeed(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def enable_feed(self) -> Callable[[feed.EnableFeedRequest], feed.Feed]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._EnableFeed(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def fetch_service_account_for_customer(
        self,
    ) -> Callable[
        [feed.FetchServiceAccountForCustomerRequest], feed.FeedServiceAccount
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchServiceAccountForCustomer(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def generate_secret(
        self,
    ) -> Callable[[feed.GenerateSecretRequest], feed.GenerateSecretResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GenerateSecret(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_feed(self) -> Callable[[feed.GetFeedRequest], feed.Feed]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetFeed(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_feed_pack(self) -> Callable[[feed.GetFeedPackRequest], feed.FeedPack]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetFeedPack(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def import_push_logs(
        self,
    ) -> Callable[[feed.ImportPushLogsRequest], httpbody_pb2.HttpBody]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ImportPushLogs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_feed_packs(
        self,
    ) -> Callable[[feed.ListFeedPacksRequest], feed.ListFeedPacksResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListFeedPacks(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_feeds(self) -> Callable[[feed.ListFeedsRequest], feed.ListFeedsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListFeeds(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_feed_source_type_schemas(
        self,
    ) -> Callable[
        [feed.ListFeedSourceTypeSchemasRequest], feed.ListFeedSourceTypeSchemasResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListFeedSourceTypeSchemas(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_log_type_schemas(
        self,
    ) -> Callable[[feed.ListLogTypeSchemasRequest], feed.ListLogTypeSchemasResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListLogTypeSchemas(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_feed(self) -> Callable[[gcc_feed.UpdateFeedRequest], gcc_feed.Feed]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateFeed(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseFeedsServiceRestTransport._BaseCancelOperation, FeedsServiceRestStub
    ):
        def __hash__(self):
            return hash("FeedsServiceRestTransport.CancelOperation")

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

            http_options = (
                _BaseFeedsServiceRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFeedsServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.chronicle_v1.FeedsServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FeedsService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FeedsServiceRestTransport._CancelOperation._get_response(
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

            return self._interceptor.post_cancel_operation(None)

    @property
    def delete_operation(self):
        return self._DeleteOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _DeleteOperation(
        _BaseFeedsServiceRestTransport._BaseDeleteOperation, FeedsServiceRestStub
    ):
        def __hash__(self):
            return hash("FeedsServiceRestTransport.DeleteOperation")

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
            request: operations_pb2.DeleteOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> None:
            r"""Call the delete operation method over HTTP.

            Args:
                request (operations_pb2.DeleteOperationRequest):
                    The request object for DeleteOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseFeedsServiceRestTransport._BaseDeleteOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFeedsServiceRestTransport._BaseDeleteOperation,
                    "_BaseDeleteOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.FeedsServiceClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FeedsService",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FeedsServiceRestTransport._DeleteOperation._get_response(
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

            return self._interceptor.post_delete_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseFeedsServiceRestTransport._BaseGetOperation, FeedsServiceRestStub
    ):
        def __hash__(self):
            return hash("FeedsServiceRestTransport.GetOperation")

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

            http_options = (
                _BaseFeedsServiceRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFeedsServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.chronicle_v1.FeedsServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FeedsService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FeedsServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.chronicle_v1.FeedsServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FeedsService",
                        "rpcName": "GetOperation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_operations(self):
        return self._ListOperations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListOperations(
        _BaseFeedsServiceRestTransport._BaseListOperations, FeedsServiceRestStub
    ):
        def __hash__(self):
            return hash("FeedsServiceRestTransport.ListOperations")

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
            request: operations_pb2.ListOperationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.ListOperationsResponse:
            r"""Call the list operations method over HTTP.

            Args:
                request (operations_pb2.ListOperationsRequest):
                    The request object for ListOperations method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                operations_pb2.ListOperationsResponse: Response from ListOperations method.
            """

            http_options = (
                _BaseFeedsServiceRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseFeedsServiceRestTransport._BaseListOperations,
                    "_BaseListOperations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.FeedsServiceClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FeedsService",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = FeedsServiceRestTransport._ListOperations._get_response(
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
            resp = operations_pb2.ListOperationsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_list_operations(resp)
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
                    "Received response for google.cloud.chronicle_v1.FeedsServiceAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.FeedsService",
                        "rpcName": "ListOperations",
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


__all__ = ("FeedsServiceRestTransport",)
