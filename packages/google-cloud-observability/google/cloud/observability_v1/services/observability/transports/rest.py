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
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.observability_v1._compat import transcode_request
from google.cloud.observability_v1.types import observability

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseObservabilityRestTransport

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


class ObservabilityRestInterceptor:
    """Interceptor for Observability.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the ObservabilityRestTransport.

    .. code-block:: python
        class MyCustomObservabilityInterceptor(ObservabilityRestInterceptor):
            def pre_create_bucket(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_bucket(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_link(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_link(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_trace_scope(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_trace_scope(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_link(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_link(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_trace_scope(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_bucket(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_bucket(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_dataset(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_dataset(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_link(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_link(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_scope(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_scope(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_settings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_settings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_trace_scope(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_trace_scope(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_view(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_view(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_buckets(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_buckets(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_datasets(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_datasets(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_links(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_links(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_trace_scopes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_trace_scopes(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_views(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_views(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_bucket(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_bucket(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_link(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_link(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_scope(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_scope(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_settings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_settings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_trace_scope(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_trace_scope(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = ObservabilityRestTransport(interceptor=MyCustomObservabilityInterceptor())
        client = ObservabilityClient(transport=transport)


    """

    def pre_create_bucket(
        self,
        request: observability.CreateBucketRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        observability.CreateBucketRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_bucket

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Observability server.
        """
        return request, metadata

    def post_create_bucket(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_bucket

        DEPRECATED. Please use the `post_create_bucket_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Observability server but before
        it is returned to user code. This `post_create_bucket` interceptor runs
        before the `post_create_bucket_with_metadata` interceptor.
        """
        return response

    def post_create_bucket_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_bucket

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Observability server but before it is returned to user code.

        We recommend only using this `post_create_bucket_with_metadata`
        interceptor in new development instead of the `post_create_bucket` interceptor.
        When both interceptors are used, this `post_create_bucket_with_metadata` interceptor runs after the
        `post_create_bucket` interceptor. The (possibly modified) response returned by
        `post_create_bucket` will be passed to
        `post_create_bucket_with_metadata`.
        """
        return response, metadata

    def pre_create_link(
        self,
        request: observability.CreateLinkRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        observability.CreateLinkRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_link

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Observability server.
        """
        return request, metadata

    def post_create_link(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_link

        DEPRECATED. Please use the `post_create_link_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Observability server but before
        it is returned to user code. This `post_create_link` interceptor runs
        before the `post_create_link_with_metadata` interceptor.
        """
        return response

    def post_create_link_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_link

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Observability server but before it is returned to user code.

        We recommend only using this `post_create_link_with_metadata`
        interceptor in new development instead of the `post_create_link` interceptor.
        When both interceptors are used, this `post_create_link_with_metadata` interceptor runs after the
        `post_create_link` interceptor. The (possibly modified) response returned by
        `post_create_link` will be passed to
        `post_create_link_with_metadata`.
        """
        return response, metadata

    def pre_create_trace_scope(
        self,
        request: observability.CreateTraceScopeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        observability.CreateTraceScopeRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_trace_scope

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Observability server.
        """
        return request, metadata

    def post_create_trace_scope(
        self, response: observability.TraceScope
    ) -> observability.TraceScope:
        """Post-rpc interceptor for create_trace_scope

        DEPRECATED. Please use the `post_create_trace_scope_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Observability server but before
        it is returned to user code. This `post_create_trace_scope` interceptor runs
        before the `post_create_trace_scope_with_metadata` interceptor.
        """
        return response

    def post_create_trace_scope_with_metadata(
        self,
        response: observability.TraceScope,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[observability.TraceScope, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_trace_scope

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Observability server but before it is returned to user code.

        We recommend only using this `post_create_trace_scope_with_metadata`
        interceptor in new development instead of the `post_create_trace_scope` interceptor.
        When both interceptors are used, this `post_create_trace_scope_with_metadata` interceptor runs after the
        `post_create_trace_scope` interceptor. The (possibly modified) response returned by
        `post_create_trace_scope` will be passed to
        `post_create_trace_scope_with_metadata`.
        """
        return response, metadata

    def pre_delete_link(
        self,
        request: observability.DeleteLinkRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        observability.DeleteLinkRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_link

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Observability server.
        """
        return request, metadata

    def post_delete_link(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_link

        DEPRECATED. Please use the `post_delete_link_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Observability server but before
        it is returned to user code. This `post_delete_link` interceptor runs
        before the `post_delete_link_with_metadata` interceptor.
        """
        return response

    def post_delete_link_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_link

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Observability server but before it is returned to user code.

        We recommend only using this `post_delete_link_with_metadata`
        interceptor in new development instead of the `post_delete_link` interceptor.
        When both interceptors are used, this `post_delete_link_with_metadata` interceptor runs after the
        `post_delete_link` interceptor. The (possibly modified) response returned by
        `post_delete_link` will be passed to
        `post_delete_link_with_metadata`.
        """
        return response, metadata

    def pre_delete_trace_scope(
        self,
        request: observability.DeleteTraceScopeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        observability.DeleteTraceScopeRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_trace_scope

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Observability server.
        """
        return request, metadata

    def pre_get_bucket(
        self,
        request: observability.GetBucketRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[observability.GetBucketRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_bucket

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Observability server.
        """
        return request, metadata

    def post_get_bucket(self, response: observability.Bucket) -> observability.Bucket:
        """Post-rpc interceptor for get_bucket

        DEPRECATED. Please use the `post_get_bucket_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Observability server but before
        it is returned to user code. This `post_get_bucket` interceptor runs
        before the `post_get_bucket_with_metadata` interceptor.
        """
        return response

    def post_get_bucket_with_metadata(
        self,
        response: observability.Bucket,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[observability.Bucket, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_bucket

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Observability server but before it is returned to user code.

        We recommend only using this `post_get_bucket_with_metadata`
        interceptor in new development instead of the `post_get_bucket` interceptor.
        When both interceptors are used, this `post_get_bucket_with_metadata` interceptor runs after the
        `post_get_bucket` interceptor. The (possibly modified) response returned by
        `post_get_bucket` will be passed to
        `post_get_bucket_with_metadata`.
        """
        return response, metadata

    def pre_get_dataset(
        self,
        request: observability.GetDatasetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        observability.GetDatasetRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_dataset

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Observability server.
        """
        return request, metadata

    def post_get_dataset(
        self, response: observability.Dataset
    ) -> observability.Dataset:
        """Post-rpc interceptor for get_dataset

        DEPRECATED. Please use the `post_get_dataset_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Observability server but before
        it is returned to user code. This `post_get_dataset` interceptor runs
        before the `post_get_dataset_with_metadata` interceptor.
        """
        return response

    def post_get_dataset_with_metadata(
        self,
        response: observability.Dataset,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[observability.Dataset, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_dataset

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Observability server but before it is returned to user code.

        We recommend only using this `post_get_dataset_with_metadata`
        interceptor in new development instead of the `post_get_dataset` interceptor.
        When both interceptors are used, this `post_get_dataset_with_metadata` interceptor runs after the
        `post_get_dataset` interceptor. The (possibly modified) response returned by
        `post_get_dataset` will be passed to
        `post_get_dataset_with_metadata`.
        """
        return response, metadata

    def pre_get_link(
        self,
        request: observability.GetLinkRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[observability.GetLinkRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_link

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Observability server.
        """
        return request, metadata

    def post_get_link(self, response: observability.Link) -> observability.Link:
        """Post-rpc interceptor for get_link

        DEPRECATED. Please use the `post_get_link_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Observability server but before
        it is returned to user code. This `post_get_link` interceptor runs
        before the `post_get_link_with_metadata` interceptor.
        """
        return response

    def post_get_link_with_metadata(
        self,
        response: observability.Link,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[observability.Link, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_link

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Observability server but before it is returned to user code.

        We recommend only using this `post_get_link_with_metadata`
        interceptor in new development instead of the `post_get_link` interceptor.
        When both interceptors are used, this `post_get_link_with_metadata` interceptor runs after the
        `post_get_link` interceptor. The (possibly modified) response returned by
        `post_get_link` will be passed to
        `post_get_link_with_metadata`.
        """
        return response, metadata

    def pre_get_scope(
        self,
        request: observability.GetScopeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[observability.GetScopeRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_scope

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Observability server.
        """
        return request, metadata

    def post_get_scope(self, response: observability.Scope) -> observability.Scope:
        """Post-rpc interceptor for get_scope

        DEPRECATED. Please use the `post_get_scope_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Observability server but before
        it is returned to user code. This `post_get_scope` interceptor runs
        before the `post_get_scope_with_metadata` interceptor.
        """
        return response

    def post_get_scope_with_metadata(
        self,
        response: observability.Scope,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[observability.Scope, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_scope

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Observability server but before it is returned to user code.

        We recommend only using this `post_get_scope_with_metadata`
        interceptor in new development instead of the `post_get_scope` interceptor.
        When both interceptors are used, this `post_get_scope_with_metadata` interceptor runs after the
        `post_get_scope` interceptor. The (possibly modified) response returned by
        `post_get_scope` will be passed to
        `post_get_scope_with_metadata`.
        """
        return response, metadata

    def pre_get_settings(
        self,
        request: observability.GetSettingsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        observability.GetSettingsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_settings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Observability server.
        """
        return request, metadata

    def post_get_settings(
        self, response: observability.Settings
    ) -> observability.Settings:
        """Post-rpc interceptor for get_settings

        DEPRECATED. Please use the `post_get_settings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Observability server but before
        it is returned to user code. This `post_get_settings` interceptor runs
        before the `post_get_settings_with_metadata` interceptor.
        """
        return response

    def post_get_settings_with_metadata(
        self,
        response: observability.Settings,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[observability.Settings, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_settings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Observability server but before it is returned to user code.

        We recommend only using this `post_get_settings_with_metadata`
        interceptor in new development instead of the `post_get_settings` interceptor.
        When both interceptors are used, this `post_get_settings_with_metadata` interceptor runs after the
        `post_get_settings` interceptor. The (possibly modified) response returned by
        `post_get_settings` will be passed to
        `post_get_settings_with_metadata`.
        """
        return response, metadata

    def pre_get_trace_scope(
        self,
        request: observability.GetTraceScopeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        observability.GetTraceScopeRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_trace_scope

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Observability server.
        """
        return request, metadata

    def post_get_trace_scope(
        self, response: observability.TraceScope
    ) -> observability.TraceScope:
        """Post-rpc interceptor for get_trace_scope

        DEPRECATED. Please use the `post_get_trace_scope_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Observability server but before
        it is returned to user code. This `post_get_trace_scope` interceptor runs
        before the `post_get_trace_scope_with_metadata` interceptor.
        """
        return response

    def post_get_trace_scope_with_metadata(
        self,
        response: observability.TraceScope,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[observability.TraceScope, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_trace_scope

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Observability server but before it is returned to user code.

        We recommend only using this `post_get_trace_scope_with_metadata`
        interceptor in new development instead of the `post_get_trace_scope` interceptor.
        When both interceptors are used, this `post_get_trace_scope_with_metadata` interceptor runs after the
        `post_get_trace_scope` interceptor. The (possibly modified) response returned by
        `post_get_trace_scope` will be passed to
        `post_get_trace_scope_with_metadata`.
        """
        return response, metadata

    def pre_get_view(
        self,
        request: observability.GetViewRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[observability.GetViewRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_view

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Observability server.
        """
        return request, metadata

    def post_get_view(self, response: observability.View) -> observability.View:
        """Post-rpc interceptor for get_view

        DEPRECATED. Please use the `post_get_view_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Observability server but before
        it is returned to user code. This `post_get_view` interceptor runs
        before the `post_get_view_with_metadata` interceptor.
        """
        return response

    def post_get_view_with_metadata(
        self,
        response: observability.View,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[observability.View, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_view

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Observability server but before it is returned to user code.

        We recommend only using this `post_get_view_with_metadata`
        interceptor in new development instead of the `post_get_view` interceptor.
        When both interceptors are used, this `post_get_view_with_metadata` interceptor runs after the
        `post_get_view` interceptor. The (possibly modified) response returned by
        `post_get_view` will be passed to
        `post_get_view_with_metadata`.
        """
        return response, metadata

    def pre_list_buckets(
        self,
        request: observability.ListBucketsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        observability.ListBucketsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_buckets

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Observability server.
        """
        return request, metadata

    def post_list_buckets(
        self, response: observability.ListBucketsResponse
    ) -> observability.ListBucketsResponse:
        """Post-rpc interceptor for list_buckets

        DEPRECATED. Please use the `post_list_buckets_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Observability server but before
        it is returned to user code. This `post_list_buckets` interceptor runs
        before the `post_list_buckets_with_metadata` interceptor.
        """
        return response

    def post_list_buckets_with_metadata(
        self,
        response: observability.ListBucketsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        observability.ListBucketsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_buckets

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Observability server but before it is returned to user code.

        We recommend only using this `post_list_buckets_with_metadata`
        interceptor in new development instead of the `post_list_buckets` interceptor.
        When both interceptors are used, this `post_list_buckets_with_metadata` interceptor runs after the
        `post_list_buckets` interceptor. The (possibly modified) response returned by
        `post_list_buckets` will be passed to
        `post_list_buckets_with_metadata`.
        """
        return response, metadata

    def pre_list_datasets(
        self,
        request: observability.ListDatasetsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        observability.ListDatasetsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_datasets

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Observability server.
        """
        return request, metadata

    def post_list_datasets(
        self, response: observability.ListDatasetsResponse
    ) -> observability.ListDatasetsResponse:
        """Post-rpc interceptor for list_datasets

        DEPRECATED. Please use the `post_list_datasets_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Observability server but before
        it is returned to user code. This `post_list_datasets` interceptor runs
        before the `post_list_datasets_with_metadata` interceptor.
        """
        return response

    def post_list_datasets_with_metadata(
        self,
        response: observability.ListDatasetsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        observability.ListDatasetsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_datasets

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Observability server but before it is returned to user code.

        We recommend only using this `post_list_datasets_with_metadata`
        interceptor in new development instead of the `post_list_datasets` interceptor.
        When both interceptors are used, this `post_list_datasets_with_metadata` interceptor runs after the
        `post_list_datasets` interceptor. The (possibly modified) response returned by
        `post_list_datasets` will be passed to
        `post_list_datasets_with_metadata`.
        """
        return response, metadata

    def pre_list_links(
        self,
        request: observability.ListLinksRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[observability.ListLinksRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_links

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Observability server.
        """
        return request, metadata

    def post_list_links(
        self, response: observability.ListLinksResponse
    ) -> observability.ListLinksResponse:
        """Post-rpc interceptor for list_links

        DEPRECATED. Please use the `post_list_links_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Observability server but before
        it is returned to user code. This `post_list_links` interceptor runs
        before the `post_list_links_with_metadata` interceptor.
        """
        return response

    def post_list_links_with_metadata(
        self,
        response: observability.ListLinksResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        observability.ListLinksResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_links

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Observability server but before it is returned to user code.

        We recommend only using this `post_list_links_with_metadata`
        interceptor in new development instead of the `post_list_links` interceptor.
        When both interceptors are used, this `post_list_links_with_metadata` interceptor runs after the
        `post_list_links` interceptor. The (possibly modified) response returned by
        `post_list_links` will be passed to
        `post_list_links_with_metadata`.
        """
        return response, metadata

    def pre_list_trace_scopes(
        self,
        request: observability.ListTraceScopesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        observability.ListTraceScopesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_trace_scopes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Observability server.
        """
        return request, metadata

    def post_list_trace_scopes(
        self, response: observability.ListTraceScopesResponse
    ) -> observability.ListTraceScopesResponse:
        """Post-rpc interceptor for list_trace_scopes

        DEPRECATED. Please use the `post_list_trace_scopes_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Observability server but before
        it is returned to user code. This `post_list_trace_scopes` interceptor runs
        before the `post_list_trace_scopes_with_metadata` interceptor.
        """
        return response

    def post_list_trace_scopes_with_metadata(
        self,
        response: observability.ListTraceScopesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        observability.ListTraceScopesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_trace_scopes

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Observability server but before it is returned to user code.

        We recommend only using this `post_list_trace_scopes_with_metadata`
        interceptor in new development instead of the `post_list_trace_scopes` interceptor.
        When both interceptors are used, this `post_list_trace_scopes_with_metadata` interceptor runs after the
        `post_list_trace_scopes` interceptor. The (possibly modified) response returned by
        `post_list_trace_scopes` will be passed to
        `post_list_trace_scopes_with_metadata`.
        """
        return response, metadata

    def pre_list_views(
        self,
        request: observability.ListViewsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[observability.ListViewsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_views

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Observability server.
        """
        return request, metadata

    def post_list_views(
        self, response: observability.ListViewsResponse
    ) -> observability.ListViewsResponse:
        """Post-rpc interceptor for list_views

        DEPRECATED. Please use the `post_list_views_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Observability server but before
        it is returned to user code. This `post_list_views` interceptor runs
        before the `post_list_views_with_metadata` interceptor.
        """
        return response

    def post_list_views_with_metadata(
        self,
        response: observability.ListViewsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        observability.ListViewsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_views

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Observability server but before it is returned to user code.

        We recommend only using this `post_list_views_with_metadata`
        interceptor in new development instead of the `post_list_views` interceptor.
        When both interceptors are used, this `post_list_views_with_metadata` interceptor runs after the
        `post_list_views` interceptor. The (possibly modified) response returned by
        `post_list_views` will be passed to
        `post_list_views_with_metadata`.
        """
        return response, metadata

    def pre_update_bucket(
        self,
        request: observability.UpdateBucketRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        observability.UpdateBucketRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_bucket

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Observability server.
        """
        return request, metadata

    def post_update_bucket(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_bucket

        DEPRECATED. Please use the `post_update_bucket_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Observability server but before
        it is returned to user code. This `post_update_bucket` interceptor runs
        before the `post_update_bucket_with_metadata` interceptor.
        """
        return response

    def post_update_bucket_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_bucket

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Observability server but before it is returned to user code.

        We recommend only using this `post_update_bucket_with_metadata`
        interceptor in new development instead of the `post_update_bucket` interceptor.
        When both interceptors are used, this `post_update_bucket_with_metadata` interceptor runs after the
        `post_update_bucket` interceptor. The (possibly modified) response returned by
        `post_update_bucket` will be passed to
        `post_update_bucket_with_metadata`.
        """
        return response, metadata

    def pre_update_link(
        self,
        request: observability.UpdateLinkRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        observability.UpdateLinkRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_link

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Observability server.
        """
        return request, metadata

    def post_update_link(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_link

        DEPRECATED. Please use the `post_update_link_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Observability server but before
        it is returned to user code. This `post_update_link` interceptor runs
        before the `post_update_link_with_metadata` interceptor.
        """
        return response

    def post_update_link_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_link

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Observability server but before it is returned to user code.

        We recommend only using this `post_update_link_with_metadata`
        interceptor in new development instead of the `post_update_link` interceptor.
        When both interceptors are used, this `post_update_link_with_metadata` interceptor runs after the
        `post_update_link` interceptor. The (possibly modified) response returned by
        `post_update_link` will be passed to
        `post_update_link_with_metadata`.
        """
        return response, metadata

    def pre_update_scope(
        self,
        request: observability.UpdateScopeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        observability.UpdateScopeRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_scope

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Observability server.
        """
        return request, metadata

    def post_update_scope(self, response: observability.Scope) -> observability.Scope:
        """Post-rpc interceptor for update_scope

        DEPRECATED. Please use the `post_update_scope_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Observability server but before
        it is returned to user code. This `post_update_scope` interceptor runs
        before the `post_update_scope_with_metadata` interceptor.
        """
        return response

    def post_update_scope_with_metadata(
        self,
        response: observability.Scope,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[observability.Scope, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_scope

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Observability server but before it is returned to user code.

        We recommend only using this `post_update_scope_with_metadata`
        interceptor in new development instead of the `post_update_scope` interceptor.
        When both interceptors are used, this `post_update_scope_with_metadata` interceptor runs after the
        `post_update_scope` interceptor. The (possibly modified) response returned by
        `post_update_scope` will be passed to
        `post_update_scope_with_metadata`.
        """
        return response, metadata

    def pre_update_settings(
        self,
        request: observability.UpdateSettingsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        observability.UpdateSettingsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_settings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Observability server.
        """
        return request, metadata

    def post_update_settings(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_settings

        DEPRECATED. Please use the `post_update_settings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Observability server but before
        it is returned to user code. This `post_update_settings` interceptor runs
        before the `post_update_settings_with_metadata` interceptor.
        """
        return response

    def post_update_settings_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_settings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Observability server but before it is returned to user code.

        We recommend only using this `post_update_settings_with_metadata`
        interceptor in new development instead of the `post_update_settings` interceptor.
        When both interceptors are used, this `post_update_settings_with_metadata` interceptor runs after the
        `post_update_settings` interceptor. The (possibly modified) response returned by
        `post_update_settings` will be passed to
        `post_update_settings_with_metadata`.
        """
        return response, metadata

    def pre_update_trace_scope(
        self,
        request: observability.UpdateTraceScopeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        observability.UpdateTraceScopeRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_trace_scope

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Observability server.
        """
        return request, metadata

    def post_update_trace_scope(
        self, response: observability.TraceScope
    ) -> observability.TraceScope:
        """Post-rpc interceptor for update_trace_scope

        DEPRECATED. Please use the `post_update_trace_scope_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Observability server but before
        it is returned to user code. This `post_update_trace_scope` interceptor runs
        before the `post_update_trace_scope_with_metadata` interceptor.
        """
        return response

    def post_update_trace_scope_with_metadata(
        self,
        response: observability.TraceScope,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[observability.TraceScope, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_trace_scope

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Observability server but before it is returned to user code.

        We recommend only using this `post_update_trace_scope_with_metadata`
        interceptor in new development instead of the `post_update_trace_scope` interceptor.
        When both interceptors are used, this `post_update_trace_scope_with_metadata` interceptor runs after the
        `post_update_trace_scope` interceptor. The (possibly modified) response returned by
        `post_update_trace_scope` will be passed to
        `post_update_trace_scope_with_metadata`.
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
        before they are sent to the Observability server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the Observability server but before
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
        before they are sent to the Observability server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the Observability server but before
        it is returned to user code.
        """
        return response

    def pre_cancel_operation(
        self,
        request: operations_pb2.CancelOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.CancelOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Observability server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the Observability server but before
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
        before they are sent to the Observability server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the Observability server but before
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
        before they are sent to the Observability server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the Observability server but before
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
        before they are sent to the Observability server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the Observability server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class ObservabilityRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: ObservabilityRestInterceptor


class ObservabilityRestTransport(_BaseObservabilityRestTransport):
    """REST backend synchronous transport for Observability.

    Service describing handlers for resources

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "observability.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[ObservabilityRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'observability.googleapis.com').
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
            interceptor (Optional[ObservabilityRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or ObservabilityRestInterceptor()
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
                "google.longrunning.Operations.CancelOperation": [
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}:cancel",
                        "body": "*",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=folders/*/locations/*/operations/*}:cancel",
                        "body": "*",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=organizations/*/locations/*/operations/*}:cancel",
                        "body": "*",
                    },
                ],
                "google.longrunning.Operations.DeleteOperation": [
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=folders/*/locations/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=organizations/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=folders/*/locations/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=organizations/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.ListOperations": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=folders/*/locations/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=organizations/*/locations/*}/operations",
                    },
                ],
            }

            rest_transport = operations_v1.OperationsRestTransport(
                host=self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                scopes=self._scopes,
                http_options=http_options,
                path_prefix="v1",
            )

            self._operations_client = operations_v1.AbstractOperationsClient(
                transport=rest_transport
            )

        # Return the client from cache.
        return self._operations_client

    class _CreateBucket(
        _BaseObservabilityRestTransport._BaseCreateBucket, ObservabilityRestStub
    ):
        def __hash__(self):
            return hash("ObservabilityRestTransport.CreateBucket")

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
            request: observability.CreateBucketRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create bucket method over HTTP.

            Args:
                request (~.observability.CreateBucketRequest):
                    The request object. Request for creating a bucket.
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

            http_options = (
                _BaseObservabilityRestTransport._BaseCreateBucket._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_bucket(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseObservabilityRestTransport._BaseCreateBucket,
                    "_BaseCreateBucket__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.observability_v1.ObservabilityClient.CreateBucket",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "CreateBucket",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ObservabilityRestTransport._CreateBucket._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_bucket(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_bucket_with_metadata(
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
                    "Received response for google.cloud.observability_v1.ObservabilityClient.create_bucket",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "CreateBucket",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateLink(
        _BaseObservabilityRestTransport._BaseCreateLink, ObservabilityRestStub
    ):
        def __hash__(self):
            return hash("ObservabilityRestTransport.CreateLink")

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
            request: observability.CreateLinkRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create link method over HTTP.

            Args:
                request (~.observability.CreateLinkRequest):
                    The request object. Request for creating a link.
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

            http_options = (
                _BaseObservabilityRestTransport._BaseCreateLink._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_link(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseObservabilityRestTransport._BaseCreateLink,
                    "_BaseCreateLink__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.observability_v1.ObservabilityClient.CreateLink",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "CreateLink",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ObservabilityRestTransport._CreateLink._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_link(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_link_with_metadata(
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
                    "Received response for google.cloud.observability_v1.ObservabilityClient.create_link",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "CreateLink",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateTraceScope(
        _BaseObservabilityRestTransport._BaseCreateTraceScope, ObservabilityRestStub
    ):
        def __hash__(self):
            return hash("ObservabilityRestTransport.CreateTraceScope")

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
            request: observability.CreateTraceScopeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> observability.TraceScope:
            r"""Call the create trace scope method over HTTP.

            Args:
                request (~.observability.CreateTraceScopeRequest):
                    The request object. Request for creating a TraceScope.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.observability.TraceScope:
                    A trace scope is a collection of
                resources whose traces are queried
                together.

            """

            http_options = _BaseObservabilityRestTransport._BaseCreateTraceScope._get_http_options()
            request, metadata = self._interceptor.pre_create_trace_scope(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseObservabilityRestTransport._BaseCreateTraceScope,
                    "_BaseCreateTraceScope__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.observability_v1.ObservabilityClient.CreateTraceScope",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "CreateTraceScope",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ObservabilityRestTransport._CreateTraceScope._get_response(
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
            resp = observability.TraceScope()
            pb_resp = observability.TraceScope.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_trace_scope(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_trace_scope_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = observability.TraceScope.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.observability_v1.ObservabilityClient.create_trace_scope",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "CreateTraceScope",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteLink(
        _BaseObservabilityRestTransport._BaseDeleteLink, ObservabilityRestStub
    ):
        def __hash__(self):
            return hash("ObservabilityRestTransport.DeleteLink")

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
            request: observability.DeleteLinkRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete link method over HTTP.

            Args:
                request (~.observability.DeleteLinkRequest):
                    The request object. Request for deleting a link.
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

            http_options = (
                _BaseObservabilityRestTransport._BaseDeleteLink._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_link(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseObservabilityRestTransport._BaseDeleteLink,
                    "_BaseDeleteLink__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.observability_v1.ObservabilityClient.DeleteLink",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "DeleteLink",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ObservabilityRestTransport._DeleteLink._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_link(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_link_with_metadata(
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
                    "Received response for google.cloud.observability_v1.ObservabilityClient.delete_link",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "DeleteLink",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteTraceScope(
        _BaseObservabilityRestTransport._BaseDeleteTraceScope, ObservabilityRestStub
    ):
        def __hash__(self):
            return hash("ObservabilityRestTransport.DeleteTraceScope")

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
            request: observability.DeleteTraceScopeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete trace scope method over HTTP.

            Args:
                request (~.observability.DeleteTraceScopeRequest):
                    The request object. Request for deleting a TraceScope.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseObservabilityRestTransport._BaseDeleteTraceScope._get_http_options()
            request, metadata = self._interceptor.pre_delete_trace_scope(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseObservabilityRestTransport._BaseDeleteTraceScope,
                    "_BaseDeleteTraceScope__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.observability_v1.ObservabilityClient.DeleteTraceScope",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "DeleteTraceScope",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ObservabilityRestTransport._DeleteTraceScope._get_response(
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

    class _GetBucket(
        _BaseObservabilityRestTransport._BaseGetBucket, ObservabilityRestStub
    ):
        def __hash__(self):
            return hash("ObservabilityRestTransport.GetBucket")

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
            request: observability.GetBucketRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> observability.Bucket:
            r"""Call the get bucket method over HTTP.

            Args:
                request (~.observability.GetBucketRequest):
                    The request object. Request for getting a bucket.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.observability.Bucket:
                    Bucket configuration for storing
                observability data.

            """

            http_options = (
                _BaseObservabilityRestTransport._BaseGetBucket._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_bucket(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseObservabilityRestTransport._BaseGetBucket,
                    "_BaseGetBucket__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.observability_v1.ObservabilityClient.GetBucket",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "GetBucket",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ObservabilityRestTransport._GetBucket._get_response(
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
            resp = observability.Bucket()
            pb_resp = observability.Bucket.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_bucket(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_bucket_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = observability.Bucket.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.observability_v1.ObservabilityClient.get_bucket",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "GetBucket",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDataset(
        _BaseObservabilityRestTransport._BaseGetDataset, ObservabilityRestStub
    ):
        def __hash__(self):
            return hash("ObservabilityRestTransport.GetDataset")

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
            request: observability.GetDatasetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> observability.Dataset:
            r"""Call the get dataset method over HTTP.

            Args:
                request (~.observability.GetDatasetRequest):
                    The request object. Request for getting a dataset.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.observability.Dataset:
                    A dataset is a collection of data
                that has a specific configuration. A
                dataset can be backed by multiple
                tables. One bucket can have multiple
                datasets.

            """

            http_options = (
                _BaseObservabilityRestTransport._BaseGetDataset._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_dataset(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseObservabilityRestTransport._BaseGetDataset,
                    "_BaseGetDataset__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.observability_v1.ObservabilityClient.GetDataset",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "GetDataset",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ObservabilityRestTransport._GetDataset._get_response(
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
            resp = observability.Dataset()
            pb_resp = observability.Dataset.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_dataset(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_dataset_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = observability.Dataset.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.observability_v1.ObservabilityClient.get_dataset",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "GetDataset",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetLink(_BaseObservabilityRestTransport._BaseGetLink, ObservabilityRestStub):
        def __hash__(self):
            return hash("ObservabilityRestTransport.GetLink")

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
            request: observability.GetLinkRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> observability.Link:
            r"""Call the get link method over HTTP.

            Args:
                request (~.observability.GetLinkRequest):
                    The request object. Request for getting a link.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.observability.Link:
                    A link lets a dataset be accessible
                to BigQuery via usage of linked
                datasets.

            """

            http_options = (
                _BaseObservabilityRestTransport._BaseGetLink._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_link(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseObservabilityRestTransport._BaseGetLink,
                    "_BaseGetLink__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.observability_v1.ObservabilityClient.GetLink",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "GetLink",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ObservabilityRestTransport._GetLink._get_response(
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
            resp = observability.Link()
            pb_resp = observability.Link.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_link(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_link_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = observability.Link.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.observability_v1.ObservabilityClient.get_link",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "GetLink",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetScope(
        _BaseObservabilityRestTransport._BaseGetScope, ObservabilityRestStub
    ):
        def __hash__(self):
            return hash("ObservabilityRestTransport.GetScope")

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
            request: observability.GetScopeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> observability.Scope:
            r"""Call the get scope method over HTTP.

            Args:
                request (~.observability.GetScopeRequest):
                    The request object. Message for getting a Scope.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.observability.Scope:
                    Message describing Scope object
            """

            http_options = (
                _BaseObservabilityRestTransport._BaseGetScope._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_scope(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseObservabilityRestTransport._BaseGetScope,
                    "_BaseGetScope__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.observability_v1.ObservabilityClient.GetScope",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "GetScope",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ObservabilityRestTransport._GetScope._get_response(
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
            resp = observability.Scope()
            pb_resp = observability.Scope.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_scope(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_scope_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = observability.Scope.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.observability_v1.ObservabilityClient.get_scope",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "GetScope",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetSettings(
        _BaseObservabilityRestTransport._BaseGetSettings, ObservabilityRestStub
    ):
        def __hash__(self):
            return hash("ObservabilityRestTransport.GetSettings")

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
            request: observability.GetSettingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> observability.Settings:
            r"""Call the get settings method over HTTP.

            Args:
                request (~.observability.GetSettingsRequest):
                    The request object. Request for getting Settings.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.observability.Settings:
                    Describes the settings associated
                with a project, organization, or folder.

            """

            http_options = (
                _BaseObservabilityRestTransport._BaseGetSettings._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_settings(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseObservabilityRestTransport._BaseGetSettings,
                    "_BaseGetSettings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.observability_v1.ObservabilityClient.GetSettings",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "GetSettings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ObservabilityRestTransport._GetSettings._get_response(
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
            resp = observability.Settings()
            pb_resp = observability.Settings.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_settings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_settings_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = observability.Settings.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.observability_v1.ObservabilityClient.get_settings",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "GetSettings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetTraceScope(
        _BaseObservabilityRestTransport._BaseGetTraceScope, ObservabilityRestStub
    ):
        def __hash__(self):
            return hash("ObservabilityRestTransport.GetTraceScope")

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
            request: observability.GetTraceScopeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> observability.TraceScope:
            r"""Call the get trace scope method over HTTP.

            Args:
                request (~.observability.GetTraceScopeRequest):
                    The request object. Request for getting a TraceScope.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.observability.TraceScope:
                    A trace scope is a collection of
                resources whose traces are queried
                together.

            """

            http_options = (
                _BaseObservabilityRestTransport._BaseGetTraceScope._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_trace_scope(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseObservabilityRestTransport._BaseGetTraceScope,
                    "_BaseGetTraceScope__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.observability_v1.ObservabilityClient.GetTraceScope",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "GetTraceScope",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ObservabilityRestTransport._GetTraceScope._get_response(
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
            resp = observability.TraceScope()
            pb_resp = observability.TraceScope.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_trace_scope(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_trace_scope_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = observability.TraceScope.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.observability_v1.ObservabilityClient.get_trace_scope",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "GetTraceScope",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetView(_BaseObservabilityRestTransport._BaseGetView, ObservabilityRestStub):
        def __hash__(self):
            return hash("ObservabilityRestTransport.GetView")

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
            request: observability.GetViewRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> observability.View:
            r"""Call the get view method over HTTP.

            Args:
                request (~.observability.GetViewRequest):
                    The request object. Request for getting a view.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.observability.View:
                    A view corresponds to a read-only
                representation of a subset of the data
                in a dataset.

            """

            http_options = (
                _BaseObservabilityRestTransport._BaseGetView._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_view(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseObservabilityRestTransport._BaseGetView,
                    "_BaseGetView__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.observability_v1.ObservabilityClient.GetView",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "GetView",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ObservabilityRestTransport._GetView._get_response(
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
            resp = observability.View()
            pb_resp = observability.View.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_view(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_view_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = observability.View.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.observability_v1.ObservabilityClient.get_view",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "GetView",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListBuckets(
        _BaseObservabilityRestTransport._BaseListBuckets, ObservabilityRestStub
    ):
        def __hash__(self):
            return hash("ObservabilityRestTransport.ListBuckets")

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
            request: observability.ListBucketsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> observability.ListBucketsResponse:
            r"""Call the list buckets method over HTTP.

            Args:
                request (~.observability.ListBucketsRequest):
                    The request object. Request for listing buckets.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.observability.ListBucketsResponse:
                    Response for listing buckets.
            """

            http_options = (
                _BaseObservabilityRestTransport._BaseListBuckets._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_buckets(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseObservabilityRestTransport._BaseListBuckets,
                    "_BaseListBuckets__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.observability_v1.ObservabilityClient.ListBuckets",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "ListBuckets",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ObservabilityRestTransport._ListBuckets._get_response(
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
            resp = observability.ListBucketsResponse()
            pb_resp = observability.ListBucketsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_buckets(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_buckets_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = observability.ListBucketsResponse.to_json(
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
                    "Received response for google.cloud.observability_v1.ObservabilityClient.list_buckets",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "ListBuckets",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDatasets(
        _BaseObservabilityRestTransport._BaseListDatasets, ObservabilityRestStub
    ):
        def __hash__(self):
            return hash("ObservabilityRestTransport.ListDatasets")

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
            request: observability.ListDatasetsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> observability.ListDatasetsResponse:
            r"""Call the list datasets method over HTTP.

            Args:
                request (~.observability.ListDatasetsRequest):
                    The request object. Request for listing datasets.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.observability.ListDatasetsResponse:
                    Response for listing datasets.
            """

            http_options = (
                _BaseObservabilityRestTransport._BaseListDatasets._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_datasets(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseObservabilityRestTransport._BaseListDatasets,
                    "_BaseListDatasets__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.observability_v1.ObservabilityClient.ListDatasets",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "ListDatasets",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ObservabilityRestTransport._ListDatasets._get_response(
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
            resp = observability.ListDatasetsResponse()
            pb_resp = observability.ListDatasetsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_datasets(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_datasets_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = observability.ListDatasetsResponse.to_json(
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
                    "Received response for google.cloud.observability_v1.ObservabilityClient.list_datasets",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "ListDatasets",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListLinks(
        _BaseObservabilityRestTransport._BaseListLinks, ObservabilityRestStub
    ):
        def __hash__(self):
            return hash("ObservabilityRestTransport.ListLinks")

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
            request: observability.ListLinksRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> observability.ListLinksResponse:
            r"""Call the list links method over HTTP.

            Args:
                request (~.observability.ListLinksRequest):
                    The request object. Request for listing links.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.observability.ListLinksResponse:
                    Response for listing links.
            """

            http_options = (
                _BaseObservabilityRestTransport._BaseListLinks._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_links(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseObservabilityRestTransport._BaseListLinks,
                    "_BaseListLinks__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.observability_v1.ObservabilityClient.ListLinks",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "ListLinks",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ObservabilityRestTransport._ListLinks._get_response(
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
            resp = observability.ListLinksResponse()
            pb_resp = observability.ListLinksResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_links(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_links_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = observability.ListLinksResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.observability_v1.ObservabilityClient.list_links",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "ListLinks",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListTraceScopes(
        _BaseObservabilityRestTransport._BaseListTraceScopes, ObservabilityRestStub
    ):
        def __hash__(self):
            return hash("ObservabilityRestTransport.ListTraceScopes")

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
            request: observability.ListTraceScopesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> observability.ListTraceScopesResponse:
            r"""Call the list trace scopes method over HTTP.

            Args:
                request (~.observability.ListTraceScopesRequest):
                    The request object. Request for listing TraceScopes.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.observability.ListTraceScopesResponse:
                    Response for listing TraceScopes.
            """

            http_options = (
                _BaseObservabilityRestTransport._BaseListTraceScopes._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_trace_scopes(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseObservabilityRestTransport._BaseListTraceScopes,
                    "_BaseListTraceScopes__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.observability_v1.ObservabilityClient.ListTraceScopes",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "ListTraceScopes",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ObservabilityRestTransport._ListTraceScopes._get_response(
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
            resp = observability.ListTraceScopesResponse()
            pb_resp = observability.ListTraceScopesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_trace_scopes(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_trace_scopes_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = observability.ListTraceScopesResponse.to_json(
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
                    "Received response for google.cloud.observability_v1.ObservabilityClient.list_trace_scopes",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "ListTraceScopes",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListViews(
        _BaseObservabilityRestTransport._BaseListViews, ObservabilityRestStub
    ):
        def __hash__(self):
            return hash("ObservabilityRestTransport.ListViews")

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
            request: observability.ListViewsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> observability.ListViewsResponse:
            r"""Call the list views method over HTTP.

            Args:
                request (~.observability.ListViewsRequest):
                    The request object. Request for listing views.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.observability.ListViewsResponse:
                    Response for listing views.
            """

            http_options = (
                _BaseObservabilityRestTransport._BaseListViews._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_views(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseObservabilityRestTransport._BaseListViews,
                    "_BaseListViews__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.observability_v1.ObservabilityClient.ListViews",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "ListViews",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ObservabilityRestTransport._ListViews._get_response(
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
            resp = observability.ListViewsResponse()
            pb_resp = observability.ListViewsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_views(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_views_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = observability.ListViewsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.observability_v1.ObservabilityClient.list_views",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "ListViews",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateBucket(
        _BaseObservabilityRestTransport._BaseUpdateBucket, ObservabilityRestStub
    ):
        def __hash__(self):
            return hash("ObservabilityRestTransport.UpdateBucket")

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
            request: observability.UpdateBucketRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update bucket method over HTTP.

            Args:
                request (~.observability.UpdateBucketRequest):
                    The request object. Request for updating a bucket.
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

            http_options = (
                _BaseObservabilityRestTransport._BaseUpdateBucket._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_bucket(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseObservabilityRestTransport._BaseUpdateBucket,
                    "_BaseUpdateBucket__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.observability_v1.ObservabilityClient.UpdateBucket",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "UpdateBucket",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ObservabilityRestTransport._UpdateBucket._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_bucket(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_bucket_with_metadata(
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
                    "Received response for google.cloud.observability_v1.ObservabilityClient.update_bucket",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "UpdateBucket",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateLink(
        _BaseObservabilityRestTransport._BaseUpdateLink, ObservabilityRestStub
    ):
        def __hash__(self):
            return hash("ObservabilityRestTransport.UpdateLink")

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
            request: observability.UpdateLinkRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update link method over HTTP.

            Args:
                request (~.observability.UpdateLinkRequest):
                    The request object. Request for updating a link.
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

            http_options = (
                _BaseObservabilityRestTransport._BaseUpdateLink._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_link(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseObservabilityRestTransport._BaseUpdateLink,
                    "_BaseUpdateLink__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.observability_v1.ObservabilityClient.UpdateLink",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "UpdateLink",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ObservabilityRestTransport._UpdateLink._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_link(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_link_with_metadata(
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
                    "Received response for google.cloud.observability_v1.ObservabilityClient.update_link",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "UpdateLink",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateScope(
        _BaseObservabilityRestTransport._BaseUpdateScope, ObservabilityRestStub
    ):
        def __hash__(self):
            return hash("ObservabilityRestTransport.UpdateScope")

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
            request: observability.UpdateScopeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> observability.Scope:
            r"""Call the update scope method over HTTP.

            Args:
                request (~.observability.UpdateScopeRequest):
                    The request object. Message for updating a Scope.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.observability.Scope:
                    Message describing Scope object
            """

            http_options = (
                _BaseObservabilityRestTransport._BaseUpdateScope._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_scope(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseObservabilityRestTransport._BaseUpdateScope,
                    "_BaseUpdateScope__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.observability_v1.ObservabilityClient.UpdateScope",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "UpdateScope",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ObservabilityRestTransport._UpdateScope._get_response(
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
            resp = observability.Scope()
            pb_resp = observability.Scope.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_scope(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_scope_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = observability.Scope.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.observability_v1.ObservabilityClient.update_scope",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "UpdateScope",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateSettings(
        _BaseObservabilityRestTransport._BaseUpdateSettings, ObservabilityRestStub
    ):
        def __hash__(self):
            return hash("ObservabilityRestTransport.UpdateSettings")

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
            request: observability.UpdateSettingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update settings method over HTTP.

            Args:
                request (~.observability.UpdateSettingsRequest):
                    The request object. Request for updating Settings.
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

            http_options = (
                _BaseObservabilityRestTransport._BaseUpdateSettings._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_settings(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseObservabilityRestTransport._BaseUpdateSettings,
                    "_BaseUpdateSettings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.observability_v1.ObservabilityClient.UpdateSettings",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "UpdateSettings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ObservabilityRestTransport._UpdateSettings._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_settings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_settings_with_metadata(
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
                    "Received response for google.cloud.observability_v1.ObservabilityClient.update_settings",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "UpdateSettings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateTraceScope(
        _BaseObservabilityRestTransport._BaseUpdateTraceScope, ObservabilityRestStub
    ):
        def __hash__(self):
            return hash("ObservabilityRestTransport.UpdateTraceScope")

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
            request: observability.UpdateTraceScopeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> observability.TraceScope:
            r"""Call the update trace scope method over HTTP.

            Args:
                request (~.observability.UpdateTraceScopeRequest):
                    The request object. Request for updating a TraceScope.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.observability.TraceScope:
                    A trace scope is a collection of
                resources whose traces are queried
                together.

            """

            http_options = _BaseObservabilityRestTransport._BaseUpdateTraceScope._get_http_options()
            request, metadata = self._interceptor.pre_update_trace_scope(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseObservabilityRestTransport._BaseUpdateTraceScope,
                    "_BaseUpdateTraceScope__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.observability_v1.ObservabilityClient.UpdateTraceScope",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "UpdateTraceScope",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ObservabilityRestTransport._UpdateTraceScope._get_response(
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
            resp = observability.TraceScope()
            pb_resp = observability.TraceScope.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_trace_scope(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_trace_scope_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = observability.TraceScope.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.observability_v1.ObservabilityClient.update_trace_scope",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "UpdateTraceScope",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_bucket(
        self,
    ) -> Callable[[observability.CreateBucketRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateBucket(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_link(
        self,
    ) -> Callable[[observability.CreateLinkRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateLink(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_trace_scope(
        self,
    ) -> Callable[[observability.CreateTraceScopeRequest], observability.TraceScope]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateTraceScope(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_link(
        self,
    ) -> Callable[[observability.DeleteLinkRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteLink(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_trace_scope(
        self,
    ) -> Callable[[observability.DeleteTraceScopeRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteTraceScope(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_bucket(
        self,
    ) -> Callable[[observability.GetBucketRequest], observability.Bucket]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetBucket(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_dataset(
        self,
    ) -> Callable[[observability.GetDatasetRequest], observability.Dataset]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDataset(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_link(self) -> Callable[[observability.GetLinkRequest], observability.Link]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetLink(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_scope(
        self,
    ) -> Callable[[observability.GetScopeRequest], observability.Scope]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetScope(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_settings(
        self,
    ) -> Callable[[observability.GetSettingsRequest], observability.Settings]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSettings(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_trace_scope(
        self,
    ) -> Callable[[observability.GetTraceScopeRequest], observability.TraceScope]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetTraceScope(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_view(self) -> Callable[[observability.GetViewRequest], observability.View]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetView(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_buckets(
        self,
    ) -> Callable[
        [observability.ListBucketsRequest], observability.ListBucketsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListBuckets(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_datasets(
        self,
    ) -> Callable[
        [observability.ListDatasetsRequest], observability.ListDatasetsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDatasets(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_links(
        self,
    ) -> Callable[[observability.ListLinksRequest], observability.ListLinksResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListLinks(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_trace_scopes(
        self,
    ) -> Callable[
        [observability.ListTraceScopesRequest], observability.ListTraceScopesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListTraceScopes(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_views(
        self,
    ) -> Callable[[observability.ListViewsRequest], observability.ListViewsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListViews(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_bucket(
        self,
    ) -> Callable[[observability.UpdateBucketRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateBucket(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_link(
        self,
    ) -> Callable[[observability.UpdateLinkRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateLink(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_scope(
        self,
    ) -> Callable[[observability.UpdateScopeRequest], observability.Scope]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateScope(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_settings(
        self,
    ) -> Callable[[observability.UpdateSettingsRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateSettings(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_trace_scope(
        self,
    ) -> Callable[[observability.UpdateTraceScopeRequest], observability.TraceScope]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateTraceScope(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseObservabilityRestTransport._BaseGetLocation, ObservabilityRestStub
    ):
        def __hash__(self):
            return hash("ObservabilityRestTransport.GetLocation")

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
                _BaseObservabilityRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseObservabilityRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.observability_v1.ObservabilityClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ObservabilityRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.observability_v1.ObservabilityAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
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
        _BaseObservabilityRestTransport._BaseListLocations, ObservabilityRestStub
    ):
        def __hash__(self):
            return hash("ObservabilityRestTransport.ListLocations")

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
                _BaseObservabilityRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseObservabilityRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.observability_v1.ObservabilityClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ObservabilityRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.observability_v1.ObservabilityAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "ListLocations",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseObservabilityRestTransport._BaseCancelOperation, ObservabilityRestStub
    ):
        def __hash__(self):
            return hash("ObservabilityRestTransport.CancelOperation")

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
                _BaseObservabilityRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseObservabilityRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.observability_v1.ObservabilityClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ObservabilityRestTransport._CancelOperation._get_response(
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
        _BaseObservabilityRestTransport._BaseDeleteOperation, ObservabilityRestStub
    ):
        def __hash__(self):
            return hash("ObservabilityRestTransport.DeleteOperation")

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
                _BaseObservabilityRestTransport._BaseDeleteOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseObservabilityRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.observability_v1.ObservabilityClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ObservabilityRestTransport._DeleteOperation._get_response(
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
        _BaseObservabilityRestTransport._BaseGetOperation, ObservabilityRestStub
    ):
        def __hash__(self):
            return hash("ObservabilityRestTransport.GetOperation")

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
                _BaseObservabilityRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseObservabilityRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.observability_v1.ObservabilityClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ObservabilityRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.observability_v1.ObservabilityAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
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
        _BaseObservabilityRestTransport._BaseListOperations, ObservabilityRestStub
    ):
        def __hash__(self):
            return hash("ObservabilityRestTransport.ListOperations")

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
                _BaseObservabilityRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseObservabilityRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.observability_v1.ObservabilityClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ObservabilityRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.observability_v1.ObservabilityAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.observability.v1.Observability",
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


__all__ = ("ObservabilityRestTransport",)
